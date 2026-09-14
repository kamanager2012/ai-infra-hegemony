#!/usr/bin/env python3
"""Negative-path self-test for the formal-report numeric source-coverage gate.

A gate that has only ever been seen to pass is not evidence of anything, and
this repository has no CI, so the one place this gate's failure behaviour can be
recorded is here. Each case mutates a throwaway copy of the two publication
trees in a way the gate is supposed to catch, runs the gate against that copy,
and requires the specific candidate to be named in the failure list - not merely
that the gate went red. The `stays green` cases are the other half: the gate
grants four concessions (a footnote or URL or sourced table, a stated model
boundary, a stated arithmetic block, and a repetition of an already-sourced
value) and each one needs a case that shows it still works, or the suite would
reward a gate that fires on anything.

Two things this is designed to prevent:

  * A silent gap. When the gate was written, a candidate was covered if a
    "not a fact" phrase appeared in its paragraph, its list lead, or a nine-line
    window around it. The window is the broadest of the three and it crossed
    paragraph boundaries, so a phrase this corpus cannot avoid - 截至, "as of",
    the report, if - covered sentences it had nothing to do with. A fabricated
    figure inserted near the top of a chapter passed the gate on the strength of
    the word 截至 four lines below it. The window now accepts only phrases that
    name a number's epistemic status. The first two cases are that defect and
    its control: one leaves only an unavoidable label near the claim, the other
    moves the claim out of every window, so the pair isolates what the window
    was covering rather than what the gate always caught.

  * A stale fixture. Every case inserts text at an exact anchor. When a chapter
    is edited legitimately an anchor can stop resolving, and a weaker harness
    would report a pass; here that is reported as FIXTURE, separately from a
    gate that failed to fire.

Each case also declares how many candidates its fixture must add. That is what
keeps a `stays green` case from being vacuous: text that is not a candidate at
all would leave the gate green for the wrong reason, and would keep it green
after the concession the case claims to test had been removed.

The real tree is never written to: `--root` points the gate at a copy under a
temporary directory.

Usage: python3 scripts/selftest-publication-numeric-gate.py [-v]
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATE = ROOT / "scripts" / "check-publication-numeric-claims.py"
TREES = ["publication", "en/publication"]
ZH = "publication/part-I-ch01-executive-summary.md"
EN = "en/publication/part-I-ch01-executive-summary.md"
TITLE = "# Part I"
# The README that describes the check suite states this suite's size. Like the
# layer-gate suite, the count lives in prose and prose is what rots, so the
# suite verifies it here: the gate cannot, because that would mean running this
# suite from inside the gate.
README = ROOT / "data" / "claim-ledger" / "README.md"


class FixtureGone(Exception):
    """A case's anchor text is no longer in the document it points at."""


# --------------------------------------------------------------- mutators

def insert_after_title(rel: str, *paragraphs: str):
    """Insert `paragraphs` as complete, blank-line-separated lines directly
    under the chapter title. The location is deliberate: it puts the fixture
    inside the nine-line window of the prose that follows the title, which is
    where the concession this suite exists to pin down lives."""
    def run(tmp: Path) -> None:
        path = tmp / rel
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        for i, line in enumerate(lines):
            if line.strip().startswith(TITLE):
                block = "\n" + "\n\n".join(paragraphs) + "\n\n"
                lines.insert(i + 1, block)
                path.write_text("".join(lines), encoding="utf-8")
                return
        raise FixtureGone(f"no line starting {TITLE!r} in {rel}")
    return run


# ------------------------------------------------------------- the cases
#
# (name, mutation, candidates the fixture must add, expected failure substring)
# `None` in the last column means the gate must stay green.

UNSOURCED = "The segment shipped 47,318 racks in the quarter, and nothing sources it."
GENERIC_ONLY = "本报告的口径以截至 2026 年 8 月 28 日 的观察窗口为准，示例与公式同前。"

CASES = [
    # --- the window: what it accepts and what it must not
    ("a label this corpus cannot avoid no longer covers a neighbouring claim",
     insert_after_title(ZH, GENERIC_ONLY, UNSOURCED),
     1, "nothing sources it"),

    ("the same claim is still caught when no boundary is anywhere near it",
     insert_after_title(ZH, UNSOURCED),
     1, "nothing sources it"),

    ("a phrase naming the bound still covers from the neighbouring paragraph",
     insert_after_title(ZH, UNSOURCED, "本节为 scenario 尺度标记，不用于行业事实。"),
     1, None),

    # The asymmetry between the window and the paragraph is measured, not
    # incidental: restricting the paragraph to named bounds as well turns nine
    # frozen sentences into failures, every one of them a real boundary whose
    # marker happens to be a common word ("but the report rejects a fixed
    # 阈值", "如果 ... 但 review burden 不下降", "does not upgrade ... into
    # unverified claims", "the paper's US$2/GPU-hour 假设"). This case records
    # that the paragraph keeps the full phrase set, so that tightening it is a
    # deliberate act with a measurement behind it rather than a quiet edit.
    ("a label in the candidate's own paragraph still covers it",
     insert_after_title(ZH, "截至 2026 年 8 月 28 日，该细分出货 47,320 racks。"),
     1, None),

    # --- the four concessions
    ("a footnote reference is an anchor",
     insert_after_title(ZH, "该细分在本季度出货 47,321 racks。[^99]"),
     1, None),

    ("a later repetition of an already-sourced value needs no anchor of its own",
     insert_after_title(ZH,
                        "该细分在本季度出货 47,322 racks。[^98]",
                        "同一口径下，全年仍为 47,322 racks，未作修订。"),
     2, None),

    ("a stated arithmetic block is not a fact claim",
     insert_after_title(ZH, "> 10.00 ÷ 3.976 ≈ 2.52×"),
     1, None),

    ("a table with a source line covers its rows",
     insert_after_title(ZH,
                        "| 细分 | 出货 |\n|---|---|\n| 某细分 | 47,323 racks |",
                        "**Source:** 本报告第 4 章。"),
     1, None),

    # --- the same rules on the English edition, which the gate must also cover
    ("an unsourced claim in the English edition is caught too",
     insert_after_title(EN, "The segment shipped 47,324 racks in the quarter."),
     1, "47,324 racks"),

    ("an unsourced table row is caught",
     insert_after_title(ZH, "| 细分 | 出货 |\n|---|---|\n| 某细分 | 47,325 racks |"),
     1, "47,325 racks"),
]


# ----------------------------------------------------------------- runner

def run_gate(root: Path) -> tuple[int, str, str]:
    proc = subprocess.run([sys.executable, str(GATE), f"--root={root}"],
                          capture_output=True, text=True, cwd=root)
    return proc.returncode, proc.stdout, proc.stderr


def candidate_count(out: str) -> int | None:
    m = re.search(r"candidates checked:\s*(\d+)", out)
    return None if m is None else int(m.group(1))


def reported_failures(out: str) -> list[str]:
    """The gate's failure list and only that: the `- ` lines between the FAIL
    summary and the first blank line. Slicing the whole output would let a
    future advice block satisfy a case that names a candidate."""
    lines = out.splitlines()
    start = next((i for i, l in enumerate(lines) if "gate FAILED:" in l), None)
    if start is None:
        return []
    reported = []
    for line in lines[start + 1:]:
        if not line.strip():
            break
        reported.append(line.strip()[2:] if line.strip().startswith("- ") else line.strip())
    return reported


def main() -> int:
    verbose = "-v" in sys.argv[1:]

    # The README states this suite's size; if it drifts, the prose is wrong
    # somewhere a reader will look. Checked before anything runs, so a stale
    # count is reported as such rather than as a bad case.
    readme = README.read_text(encoding="utf-8")
    claim = f"{len(CASES)} cases"
    if claim not in readme:
        print(f"the claim-ledger README does not state this suite's size as {claim!r}")
        print(f"  - update {README.relative_to(ROOT)}")
        return 1

    with tempfile.TemporaryDirectory(prefix="pubnum-selftest-") as tmpdir:
        tmp = Path(tmpdir)

        def reset() -> None:
            for top in TREES:
                shutil.rmtree(tmp / top, ignore_errors=True)
                shutil.copytree(ROOT / top, tmp / top)

        # The baseline is not a formality: if the gate is red before any
        # mutation, every case below could "pass" for the wrong reason.
        reset()
        rc, out, err = run_gate(tmp)
        baseline = candidate_count(out)
        if rc != 0 or "gate PASS" not in out or baseline is None:
            print("baseline: the gate does not pass on an unmutated copy.")
            print(f"  rc={rc}")
            print("\n".join(reported_failures(out)[:5]) or err[-800:])
            return 1
        print(f"baseline: gate passes on an unmutated copy, {baseline} candidates "
              f"({len(CASES)} cases follow)\n")

        bad: list[str] = []
        for name, mutate, adds, expect in CASES:
            reset()
            try:
                mutate(tmp)
            except FixtureGone as exc:
                bad.append(name)
                print(f"FIXTURE  {name}: {exc}")
                continue
            rc, out, err = run_gate(tmp)
            if "Traceback" in err:
                bad.append(name)
                last = err.strip().splitlines()[-1] if err.strip() else "(no stderr)"
                print(f"CRASH    {name}: gate raised - {last}")
                continue

            # A fixture that adds no candidate proves nothing about coverage:
            # the gate would stay green with the concession deleted.
            grew = candidate_count(out)
            if grew != baseline + adds:
                bad.append(name)
                print(f"BAD      {name}: fixture adds {None if grew is None else grew - baseline} "
                      f"candidates, expected {adds}")
                continue

            failures = reported_failures(out)
            if expect is None:
                if rc == 0 and "gate PASS" in out:
                    print(f"ok       {name}: stayed green on a real candidate")
                else:
                    bad.append(name)
                    print(f"BAD      {name}: expected green, got rc={rc} "
                          f"-> {failures[:1] or 'no failure list'}")
                continue

            hit = [f for f in failures if expect in f]
            if rc == 1 and hit:
                print(f"ok       {name}")
                if verbose:
                    print(f"           {hit[0]}")
            else:
                bad.append(name)
                reason = (f"the candidate was not named (wanted {expect!r})"
                          if not hit else f"rc={rc}")
                print(f"BAD      {name}: {reason} -> {failures[:2] or 'no failure list'}")

    fired = len([c for c in CASES if c[3] is not None])
    green = len(CASES) - fired
    print()
    print(f"Publication numeric gate self-test: {len(CASES)} cases "
          f"({fired} must fire, {green} must stay green), {len(bad)} bad")
    if bad:
        for name in bad:
            print(f"  - {name}")
        print("self-test FAIL")
        return 1
    print("self-test PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
