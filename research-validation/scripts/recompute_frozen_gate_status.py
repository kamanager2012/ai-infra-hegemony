#!/usr/bin/env python3
"""Recompute the coverage status of a test the frozen formal text sets itself.

Ch23 §1B states that a defensible historical comparison — is the AI buildout a
replay of the telecom bubble or the 2008 securitization cycle — requires
evidence on eight named contract-level variables, and that without them the
analogy "remains a research heuristic, not a formal report conclusion."

The frozen chapter cannot say which of its eight variables the research panels
now carry, because writing that back would breach the freeze. This script
tabulates it instead, from the research side, without touching the chapter.

The tabulation is the easy half. The result is the distribution: four variables
are carried, two are half-observable, and two — default / restructuring
behavior, and secondary-market liquidity of the underlying assets — are not
merely uncovered but unobservable in advance, because both are outcomes rather
than states. Those are the two that identify a bubble ex post. The test
therefore has a permanent floor: no future disclosure lifts it, which is a
stronger statement than "the evidence is incomplete."

No new numeric identity: every item is quoted from Ch23 §1B, every "where" is a
section of a layer that already exists, and nothing here is promoted into a
chapter. All outputs are D-grade report-side tabulations.
"""
from __future__ import annotations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "research-validation" / "data" / "frozen-gate-inputs.json"


def main():
    d = json.loads(INPUT.read_text(encoding="utf-8"))
    states = d["states"]
    gate = d["gates"][0]
    items = gate["items"]

    print(f"Frozen-text gate {gate['gate']} — {gate['chapter']}: {gate['chapter_title']}")
    print(f"  test: {gate['test']}")
    print(f"  rule: {gate['rule']}")
    print()

    assert len(items) == 8, len(items)
    assert [i["n"] for i in items] == list(range(1, 9)), [i["n"] for i in items]
    counts: dict[str, int] = {}
    for it in items:
        assert it["state"] in states, it["state"]
        counts[it["state"]] = counts.get(it["state"], 0) + 1
        where = it["where"] or "—"
        print(f"  {it['n']}. {it['item']:<58}{it['state']:>18}")
        print(f"       carried by: {where}")
    print()

    # The classification is the artifact, so the counts are asserted rather than
    # printed from whatever the file happens to say.
    assert counts.get("carried") == 4, counts
    assert counts.get("partly observable") == 2, counts
    assert counts.get("not yet observed") == 2, counts
    assert counts.get("not disclosed", 0) == 0, counts

    total = len(items)
    print(f"  carried: {counts['carried']} of {total}")
    print(f"  partly observable: {counts['partly observable']} of {total}")
    print(f"  not yet observed: {counts['not yet observed']} of {total}")
    print(f"  not disclosed: {counts.get('not disclosed', 0)} of {total}")
    print()

    unobservable = [i for i in items if i["state"] == "not yet observed"]
    print("The two variables that are unobservable in advance:")
    for it in unobservable:
        print(f"  - {it['item']}")
    print()
    print("  Both are outcomes rather than states. A bubble is identified ex post")
    print("  by defaults and by assets that fail to transfer; neither can be")
    print("  observed before it happens, and no disclosure supplies them. So the")
    print("  Ch23 §1B test is not 6 of 8 covered with two gaps to close — it has a")
    print("  floor that further reporting cannot lift.")
    print()
    print("  This does NOT make the analogy wrong. It makes it unpromotable, which")
    print("  is exactly what the frozen chapter already says, now with a reason and")
    print("  a bound. The register is not a survey: the frozen corpus was searched")
    print("  in both editions for enumerated evidence-requirement checklists and")
    print("  this is the only one found, so the layer holds one entry.")
    print()
    print("Every item is quoted from Ch23 §1B; no new numeric identity, and no")
    print("formal-text change. The reopen gate is unchanged.")


if __name__ == "__main__":
    main()
