#!/usr/bin/env python3
"""Negative-path self-test for the Phase II layer-consistency gate.

A gate that has only ever been seen to pass is not evidence of anything, and
this repository has no CI, so the only place the gate's *failure* behaviour can
be recorded is here. Each case below mutates a throwaway copy of the tree in a
way the gate is supposed to catch, runs the gate against that copy, and requires
the specific check to fire - not merely that some check fired.

Two things this is designed to prevent:

  * A silent gap. If a mutation is caught by an unrelated check, the case still
    reports a failure but the property it names is unverified, so every case
    names the check it expects in `expect`.
  * A stale fixture. Many cases key off an exact string in a document. When a
    document is edited legitimately, a fixture can stop matching and a weaker
    harness would report a pass. Here a fixture that no longer resolves is
    reported as FIXTURE, separately from a gate that failed to fire.

The `stays green` cases are the other half: an anchor carried by only one of the
two editions must not trip the gate, and prose that touches no registered token
must not either. Without them the suite would reward a gate that fires on
anything.

The real tree is never written to: `--root` points the gate at a copy under a
temporary directory.

Usage: python3 scripts/selftest-layer-consistency-gate.py [-v]
"""

from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATE = ROOT / "scripts" / "check-research-layer-consistency.py"
REGISTRY_REL = "research-validation/data/layer-consistency.json"


class FixtureGone(Exception):
    """A case's anchor text is no longer in the document it points at."""


# --------------------------------------------------------------- mutators

def rewrite(rel: str, old: str, new: str, count: int = -1):
    """Replace `old` with `new` in `rel`. count=-1 replaces every occurrence:
    a token that also appears elsewhere in the same document would otherwise
    survive the edit and the case would silently stop testing anything."""
    def run(tmp: Path) -> None:
        path = tmp / rel
        body = path.read_text(encoding="utf-8")
        if old not in body:
            raise FixtureGone(f"{old!r} is no longer in {rel}")
        path.write_text(body.replace(old, new) if count < 0
                        else body.replace(old, new, count), encoding="utf-8")
    return run


def rename(rel: str, to: str):
    def run(tmp: Path) -> None:
        src, dst = tmp / rel, tmp / to
        if not src.exists():
            raise FixtureGone(f"{rel} is not on disk")
        src.rename(dst)
    return run


def create(rel: str, body: str):
    def run(tmp: Path) -> None:
        (tmp / rel).write_text(body, encoding="utf-8")
    return run


def free_layer_ident(tmp: Path) -> str:
    """The lowest layer id no file in the copy uses.

    Two cases below have to invent a layer. Hardcoding the id they invent works
    until a real layer takes it, and then the case does not go FIXTURE - there
    is no string for `FixtureGone` to miss. It collides: the layer it created
    now exists for real, the check it names is masked by an unrelated one, and
    it reports BAD. That is exactly what happened when layer `22` was added, so
    both fixtures derive the id instead of naming one."""
    used = {p.name[:2] for p in (tmp / R).glob("[0-9][0-9]-*.md")}
    for n in range(14, 100):
        if f"{n:02d}" not in used:
            return f"{n:02d}"
    raise FixtureGone("no free layer id below 100")


def add_unregistered_layer(body: str):
    """A layer file at a genuinely free id, with no registry entry."""
    def run(tmp: Path) -> None:
        (tmp / f"{R}{free_layer_ident(tmp)}-placeholder-experiment.md"
         ).write_text(body, encoding="utf-8")
    return run


def add_ghost_registry_entry():
    """A registry entry whose layer file does not exist, at a free id."""
    def run(tmp: Path) -> None:
        path = tmp / REGISTRY_REL
        data = json.loads(path.read_text(encoding="utf-8"))
        data["layers"][free_layer_ident(tmp)] = {
            "slug": "ghost-layer", "script": None, "data": [],
            "upstream_must_acknowledge": [], "headline_tokens": []}
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
    return run


def append(rel: str, text: str):
    def run(tmp: Path) -> None:
        path = tmp / rel
        if not path.exists():
            raise FixtureGone(f"{rel} is not on disk")
        path.write_text(path.read_text(encoding="utf-8") + text, encoding="utf-8")
    return run


def both_editions(rel_zh: str, rel_en: str, old: str, new: str):
    """A frozen anchor carried by both editions has to be removed from both -
    either one alone satisfies the check."""
    zh, en = rewrite(rel_zh, old, new), rewrite(rel_en, old, new)

    def run(tmp: Path) -> None:
        zh(tmp)
        en(tmp)
    return run


def drop_layer_ref(rel: str, ident: str):
    """Remove every form the acknowledgement check accepts, not just the first.

    The check counts a backticked layer id or a markdown link to the layer's
    document as an acknowledgement, and an upstream file that has been wired
    properly usually carries both - a link whose text is the backticked id, then
    the id again in the prose that follows. Mutating one occurrence leaves the
    other standing and the case stops testing anything."""
    def run(tmp: Path) -> None:
        path = tmp / rel
        body = path.read_text(encoding="utf-8")
        if f"`{ident}`" not in body and f"]({ident}-" not in body:
            raise FixtureGone(f"{rel} carries no reference to {ident}")
        path.write_text(body.replace(f"`{ident}`", "a later layer")
                            .replace(f"]({ident}-", "](moved-"), encoding="utf-8")
    return run


def registry(mutate):
    def run(tmp: Path) -> None:
        path = tmp / REGISTRY_REL
        data = json.loads(path.read_text(encoding="utf-8"))
        mutate(data)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
    return run


# ------------------------------------------------------------------ cases
# (name, mutate, expectation). `expect` is a string or list of strings that must
# all appear in the gate's failure report; None means the gate must stay green.

R = "research-validation/"
CH7_ZH = "publication/part-I-ch07-power-constraint.md"
CH7_EN = "en/publication/part-I-ch07-power-constraint.md"
CH13_ZH = "publication/part-II-ch13-anchor-compute-buyer.md"
CH13_EN = "en/publication/part-II-ch13-anchor-compute-buyer.md"

CASES = [
    # -- publication and translation pairing ------------------------------
    ("canonical number rots away", rewrite(R + "20-demand-side-composition.md",
                                          "32.7%", "33.7%"),
     "headline '32.7%'"),
    ("translation number rots away", rewrite(R + "20-demand-side-composition.zh.md",
                                             "11.1%", "12.1%"),
     "headline '11.1%'"),
    ("translation drops its ownership contract",
     rewrite(R + "20-demand-side-composition.zh.md", "## 0. 归属契约", "## 0x. 归属契约"),
     "20 zh carries an ownership contract"),
    ("canonical drops its Sources section",
     rewrite(R + "18-ramp-period-funding-gap.md", "## Sources", "## Source"),
     "18 doc carries a Sources section"),
    ("canonical renamed, translation orphaned",
     rename(R + "19-chain-concentration-amplification.md",
            R + "19x-chain-concentration-amplification.md"),
     "orphan .zh.md"),

    # -- registry integrity -----------------------------------------------
    ("registry target renamed on disk",
     rename(R + "scripts/recompute_energization.py",
            R + "scripts/recompute_energization_v2.py"),
     "registry target scripts/recompute_energization.py exists on disk"),
    ("unregistered recompute script appears",
     create(R + "scripts/recompute_newlayer.py", "print('hi')\n"),
     "every recompute script has a registry entry"),
    ("a layer added without a registry entry fails",
     add_unregistered_layer(
            "# Phase II · Placeholder Experiment v0.1\n\n"
            "## 0. Ownership contract\n\nNothing, owned by nobody, in this fixture.\n\n"
            "## Sources\n\n"),
     "every layer from the epoch on has a registry entry"),
    ("a registry entry with no layer on disk fails",
     add_ghost_registry_entry(),
     "every registry entry names a layer file on disk"),
    ("recompute script stops exiting 0",
     append(R + "scripts/recompute_energization.py", "\nthis is not python(\n"),
     "recompute_energization.py exits 0"),
    ("registry declares an upstream with no layer file",
     registry(lambda d: d["layers"]["15"]["upstream_must_acknowledge"].append("99x")),
     "has no layer file"),
    ("registry declares an upstream that never acknowledged it",
     registry(lambda d: d["layers"]["15"]["upstream_must_acknowledge"].append("13")),
     "13 acknowledges 15"),

    # -- README wiring -----------------------------------------------------
    ("layer retitled but work order not updated",
     rewrite(R + "19-chain-concentration-amplification.md",
             "# Phase II · Chain Concentration Amplification v0.1",
             "# Phase II · Chain Amplification v0.1"),
     "work order item"),
    ("layer dropped from the authority graph",
     rewrite(R + "README.md", "├─ 19  Chain concentration amplification",
             "├─ 19x Chain concentration amplification"),
     "authority graph lists 19"),
    ("authority rule removed",
     rewrite(R + "README.md", "12. **`20` owns", "12x. **`20` owns"),
     "authority rule"),
    ("file index entry removed",
     rewrite(R + "README.md", "[20 · composition inputs](data/demand-composition-inputs.json)",
             "[20 · composition inputs](data/moved.json)"),
     "file index lists data/demand-composition-inputs.json"),
    ("authority graph top layer falls behind",
     rewrite(R + "README.md",
             "└─ 22  Channel discrimination test / the observable, the statistic and the pre-registered verdicts",
             "└─ 22x Channel discrimination test"),
     "authority graph top layer"),

    # -- back-references ---------------------------------------------------
    ("11 stops acknowledging 19",
     drop_layer_ref(R + "11-financing-reflexivity-map.md", "19"),
     "11 acknowledges 19"),
    ("03 stops acknowledging 16",
     drop_layer_ref(R + "03-verified-workflow-economics.md", "16"),
     "03 acknowledges 16"),
    ("04C stops acknowledging 15",
     drop_layer_ref(R + "04c-project-finance-borrower-panel.md", "15"),
     "04C acknowledges 15"),
    ("14 stops acknowledging 20",
     drop_layer_ref(R + "14-demand-side-reflexivity.md", "20"),
     "14 acknowledges 20"),

    # -- borrowed anchors: the frozen chapters -----------------------------
    # These mutate Table 7.2 itself, which is where the anchor lives; the prose
    # above the table spells the same lead times out in words. See the last
    # case in this file, which records that distinction.
    ("frozen Ch07 transmission lead time changes",
     rewrite(CH7_EN, "| New transmission | 4–8 years in advanced economies",
             "| New transmission | 5–9 years in advanced economies"),
     "anchor '4–8 years'"),
    ("frozen Ch07 cable lead time changes",
     rewrite(CH7_EN, "| Cables | 2–3 years procurement", "| Cables | 3–4 years procurement"),
     "anchor '2–3 years'"),
    ("frozen Ch07 transformer lead time changes",
     rewrite(CH7_EN, "| Large power transformers | up to 4 years procurement",
             "| Large power transformers | up to 5 years procurement"),
     "anchor 'up to 4 years'"),
    ("frozen Ch13 commitment removed from both editions",
     both_editions(CH13_ZH, CH13_EN, "100B", "120B"),
     "anchor '100B'"),
    ("frozen Ch13 capacity ceiling removed from both editions",
     both_editions(CH13_ZH, CH13_EN, "5 GW", "7 GW"),
     "anchor '5 GW'"),

    # -- borrowed anchors: the upstream panels -----------------------------
    ("upstream panel's coupon moves",
     rewrite(R + "04c-project-finance-borrower-panel.md", "9.75%", "10.25%"),
     "anchor '9.75%'"),
    ("upstream panel's concentration moves",
     rewrite(R + "04c-project-finance-borrower-panel.md", "77%", "81%"),
     "anchor '77%'"),
    ("layer 14's adoption base moves",
     rewrite(R + "14-demand-side-reflexivity.md", "18%", "22%"),
     "anchor '18%'"),
    ("layer 17's mid factor moves",
     rewrite(R + "17-energization-schedule-surface.md", "0.315", "0.410"),
     "anchor '0.315'"),
    ("layer 15's recomputed ratio moves",
     rewrite(R + "15-capital-to-cash-bridge.md", "1.87", "1.92"),
     "anchor '1.87'"),

    # -- the affected-layer report ----------------------------------------
    ("a broken anchor names the layer to re-run and its downstream",
     rewrite(R + "04c-project-finance-borrower-panel.md", "9.75%", "10.25%"),
     ["Affected layers, and what each has to update:",
      "re-run: research-validation/scripts/recompute_capital_to_cash.py",
      "downstream of 15"]),

    # -- must stay green ---------------------------------------------------
    ("an anchor carried by only one edition does not trip the gate",
     rewrite(CH13_EN, "100B", "120B"),
     None),
    ("rewording Ch07's prose does not trip the gate, because the anchor is the table",
     rewrite(CH7_EN, "**four to eight years**", "**roughly four to eight years**"),
     None),
    ("prose that touches no registered token does not trip the gate",
     append(R + "21-frozen-text-gate-status.md",
            "\nA sentence added by the self-test, carrying no registered token.\n"),
     None),

    # -- the register's stated size ---------------------------------------
    ("README misstates the register's size",
     rewrite(R + "README.md", "**Registers:** 9 layers", "**Registers:** 10 layers"),
     "README Current status states the register's size"),

    # -- table parity across editions -------------------------------------
    # 18's peak table, whose figures the canonical carries as US$17.58 etc.
    ("a canonical table cell moves and the translation does not",
     rewrite(R + "18-ramp-period-funding-gap.md", "17.58", "17.68"),
     "carries the same quantities"),
    ("a translation table cell moves and the canonical does not",
     rewrite(R + "20-demand-side-composition.zh.md", "11.1%", "12.1%"),
     "carries the same quantities"),
    ("the translation gains a table the canonical does not carry",
     append(R + "19-chain-concentration-amplification.zh.md",
            "\n| 附注 | 值 |\n|---|---:|\n| 自测插入 | 1.00 |\n"),
     "carries the same number of tables"),

    # -- stated derivations ------------------------------------------------
    ("a stated rule no longer reproduces the published value",
     registry(lambda d: d["derivations"][0].update({"to": "0.140"})),
     ["productivity_to_time(14%) = 0.123", "does NOT match the published 0.140"]),
    ("a derivation names a rule the gate does not implement",
     registry(lambda d: d["derivations"][0].update({"rule": "eyeballed"})),
     "names unknown rule"),

    # -- the declared residue, checked in both directions -------------------
    # A value nothing produces, which no declaration covers: this is the shape
    # the check exists for, and it is how `16`'s hand-entered 0.123 would have
    # looked before it was made reproducible.
    ("a layer publishes a quantity nothing produces",
     append(R + "17-energization-schedule-surface.md",
            "\nA sentence the self-test adds, carrying 4.44, which no script, "
            "input or registered token produces.\n"),
     "17 publishes no quantity that nothing produces (unaccounted: ['4.44'])"),
    # The other direction: a declaration that outlived its reason. It is edited
    # in place rather than added so the register keeps its size and check 11
    # stays quiet, which is what makes this case about check 14 alone.
    ("a declared unaccounted value has gone stale",
     registry(lambda d: [u for u in d["unaccounted"]
                         if u["value"] == "55.2"][0].update({"value": "1.23"})),
     "20 declared-unaccounted list is current (now produced, so the "
     "declarations are stale: ['1.23'])"),

    # -- the README's public summary ---------------------------------------
    # Not a hypothetical: this is the defect that motivated the check. 15 moved
    # its coverage cell to 2.52x and the README kept quoting 2.51x, which nothing
    # noticed because the value was registered nowhere at the time.
    ("the README quotes a value its layer no longer produces",
     rewrite(R + "README.md", "2.52× to 0.30×", "2.51× to 0.30×"),
     "states only values 15 produces"),
]


# Which gate check each case exercises, so that a check added to the gate
# without a case fails the self-test instead of sitting unverified. Kept here
# rather than in the case tuples so that a case name is the key: a case can be
# edited freely, but it cannot lose its check silently, and a case the map does
# not know about is an error rather than an omission. `None` marks a case that
# asserts the gate as a whole rather than one check.
CASE_CHECK = {
    "canonical number rots away": 8,
    "translation number rots away": 8,
    "translation drops its ownership contract": 3,
    "canonical drops its Sources section": 3,
    "canonical renamed, translation orphaned": 1,
    "registry target renamed on disk": 4,
    "unregistered recompute script appears": 8,
    "a layer added without a registry entry fails": 2,
    "a registry entry with no layer on disk fails": 2,
    "recompute script stops exiting 0": 7,
    "registry declares an upstream with no layer file": 9,
    "registry declares an upstream that never acknowledged it": 9,
    "layer retitled but work order not updated": 6,
    "layer dropped from the authority graph": 5,
    "authority rule removed": 6,
    "file index entry removed": 4,
    "authority graph top layer falls behind": 5,
    "11 stops acknowledging 19": 9,
    "03 stops acknowledging 16": 9,
    "04C stops acknowledging 15": 9,
    "14 stops acknowledging 20": 9,
    "frozen Ch07 transmission lead time changes": 10,
    "frozen Ch07 cable lead time changes": 10,
    "frozen Ch07 transformer lead time changes": 10,
    "frozen Ch13 commitment removed from both editions": 10,
    "frozen Ch13 capacity ceiling removed from both editions": 10,
    "upstream panel's coupon moves": 10,
    "upstream panel's concentration moves": 10,
    "layer 14's adoption base moves": 10,
    "layer 17's mid factor moves": 10,
    "layer 15's recomputed ratio moves": 10,
    "a broken anchor names the layer to re-run and its downstream": 10,
    "an anchor carried by only one edition does not trip the gate": 10,
    "rewording Ch07's prose does not trip the gate, because the anchor is the table": 10,
    "prose that touches no registered token does not trip the gate": None,
    "README misstates the register's size": 11,
    "a canonical table cell moves and the translation does not": 12,
    "a translation table cell moves and the canonical does not": 12,
    "the translation gains a table the canonical does not carry": 12,
    "a stated rule no longer reproduces the published value": 13,
    "a derivation names a rule the gate does not implement": 13,
    "a layer publishes a quantity nothing produces": 14,
    "a declared unaccounted value has gone stale": 14,
    "the README quotes a value its layer no longer produces": 15,
}


# ------------------------------------------------------------------- runner

def gate_trees(reg: dict) -> list[str]:
    """Top-level directories the gate reads. Derived from the registry so that
    a frozen chapter mapped from a new location is copied without a code
    change here."""
    tops = {"research-validation"}
    for rels in reg.get("frozen_chapter_files", {}).values():
        if not isinstance(rels, list):  # the mapping also carries a prose note
            continue
        for rel in rels:
            tops.add(Path(rel).parts[0])
    return sorted(tops)


def run_gate(root: Path) -> tuple[int, str, str]:
    proc = subprocess.run([sys.executable, str(GATE), f"--root={root}"],
                          capture_output=True, text=True, cwd=root)
    return proc.returncode, proc.stdout, proc.stderr


def reported_failures(out: str) -> list[str]:
    """The gate's failure list, and only that: the lines between the FAIL
    summary and the first blank line. The affected-layer report below it uses
    the same `- ` bullet, so slicing the whole output would read advice as
    diagnosis."""
    lines = out.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if "consistency check FAIL:" in l)
    except StopIteration:
        return []
    reported = []
    for line in lines[start + 1:]:
        if not line.strip():
            break
        reported.append(line.strip()[2:] if line.strip().startswith("- ") else line.strip())
    return reported


def match_region(out: str) -> str:
    """Everything from the FAIL summary onward: the failure list plus the
    affected-layer report, which is where a case's expectation may legitimately
    land. An empty string when the gate passed, so a case can never be satisfied
    by a PASS line that happens to contain the same words."""
    lines = out.splitlines()
    start = next((i for i, l in enumerate(lines) if "consistency check FAIL:" in l), None)
    return "" if start is None else "\n".join(lines[start:])


def load_gate():
    """The gate itself, for its CHECK_NAMES. Executing the module is safe: its
    main() is behind the `__main__` guard.

    Bytecode writing is off for the duration: importing the gate would otherwise
    leave a `scripts/__pycache__/` in the working tree, and a self-test that
    dirties the tree it is checking is a small defect of its own."""
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec = importlib.util.spec_from_file_location("layer_consistency_gate", GATE)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.dont_write_bytecode = previous


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    verbose = "-v" in argv

    names = [name for name, _, _ in CASES]
    problems: list[str] = []
    if len(set(names)) != len(names):
        problems.append("two cases share a name, so the coverage map is ambiguous")
    unmapped = [n for n in names if n not in CASE_CHECK]
    if unmapped:
        problems.append(f"cases with no entry in CASE_CHECK: {unmapped}")
    unknown = [n for n in CASE_CHECK if n not in names]
    if unknown:
        problems.append(f"CASE_CHECK entries for cases that do not exist: {unknown}")
    check_names = load_gate().CHECK_NAMES
    covered = {i for i in CASE_CHECK.values() if i is not None}
    uncovered = sorted(set(check_names) - covered)
    if uncovered:
        problems.append("gate checks with no case that makes them fire: "
                        + ", ".join(f"{i} ({check_names[i]})" for i in uncovered))
    # The README states this suite's size. It is the one count the gate cannot
    # verify, because verifying it would mean running this suite from inside the
    # gate; so the suite verifies it here, from the other end.
    readme = (ROOT / "research-validation" / "README.md").read_text(encoding="utf-8")
    claim = f"{len(CASES)} cases"
    if claim not in readme:
        problems.append(f"the README does not state this suite's size as {claim!r} "
                        f"- update research-validation/README.md")
    if problems:
        print("Self-test is not in a state where a pass would mean anything:")
        for p in problems:
            print(f"  - {p}")
        return 1

    reg = json.loads((ROOT / REGISTRY_REL).read_text(encoding="utf-8"))
    trees = gate_trees(reg)

    bad: list[str] = []
    with tempfile.TemporaryDirectory(prefix="layer-gate-selftest-") as tmpdir:
        tmp = Path(tmpdir)

        def reset() -> None:
            for top in trees:
                shutil.rmtree(tmp / top, ignore_errors=True)
                shutil.copytree(ROOT / top, tmp / top)

        # The baseline is not a formality: if the gate is red before any
        # mutation, every case below would "pass" for the wrong reason.
        reset()
        rc, out, err = run_gate(tmp)
        if rc != 0 or "consistency check PASS" not in out:
            print("baseline: the gate does not pass on an unmutated copy.")
            print(f"  rc={rc}")
            print("\n".join(reported_failures(out)[:5]) or err[-800:])
            return 1
        print(f"baseline: gate passes on an unmutated copy ({len(CASES)} cases follow)\n")

        for name, mutate, expect in CASES:
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
            failures = reported_failures(out)

            if expect is None:
                if rc == 0 and "consistency check PASS" in out:
                    print(f"ok       {name}: stayed green")
                else:
                    bad.append(name)
                    print(f"BAD      {name}: expected green, got rc={rc} "
                          f"-> {failures[:1] or 'no failure list'}")
                continue

            wanted = [expect] if isinstance(expect, str) else expect
            region = match_region(out)
            missed = [w for w in wanted if w not in region]
            if rc == 1 and not missed:
                print(f"ok       {name}")
                if verbose:
                    # A case's expectation may land in the failure list or in
                    # the affected-layer report printed below it. Several expect
                    # a line of guidance, which is never a failure line, so
                    # reading only `failures` raised StopIteration for those -
                    # crashing the run *after* printing their `ok`, which made
                    # `-v` exit 1 on a suite that had passed.
                    hit = next((f for f in failures if wanted[0] in f),
                               next((l.strip() for l in region.splitlines()
                                     if wanted[0] in l), wanted[0]))
                    print(f"           {hit}")
            else:
                bad.append(name)
                reason = (f"check did not fire (wanted {missed!r})" if missed
                          else f"rc={rc}")
                print(f"BAD      {name}: {reason} -> {failures[:2] or 'no failure list'}")

    fired = len([c for c in CASES if c[2] is not None])
    green = len(CASES) - fired
    print()
    print(f"Layer-consistency gate self-test: {len(CASES)} cases "
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
