#!/usr/bin/env python3
"""Recompute panel coverage of the frozen Chapter 23 §1B analogy gate.

This D-grade research-side tabulation is NOT a verdict on a bubble, nor is it
part of the frozen 32-chapter formal report. The input describes coverage by
the currently tracked borrower/support panels, not the entire asset market.

v0.2 repairs three identity errors from v0.1:
* lease/payment or completion guarantees ≠ collateral residual-value guarantees;
* collateral valuation ≠ contractual senior/junior loss waterfall;
* secondary-market liquidity can be observable before distress and must not
  be equated with trading in compute-price contracts.

Missing/unevidenced panel fields are not the same as physically impossible
observations. Observed default/restructuring is event-contingent for a given
borrower; matched asset-transfer evidence could be collected before default.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "research-validation" / "data" / "frozen-gate-inputs.json"

EXPECTED_STATES = {
    1: "partly observable",  # Loan-to-value lacks matched collateral valuation
    2: "carried",
    3: "carried",
    4: "not disclosed",      # Lease/payment guarantee is not residual-value floor
    5: "partly observable",  # Contractual waterfall is not asset valuation
    6: "carried",
    7: "not yet observed",    # No event recorded for tracked cohort
    8: "not disclosed",      # No facility-asset-matched resale/liquidity evidence
}
EXPECTED_COUNTS = {
    "carried": 3,
    "partly observable": 2,
    "not disclosed": 2,
    "not yet observed": 1,
}


def main() -> None:
    d = json.loads(INPUT.read_text(encoding="utf-8"))
    assert len(d["gates"]) == 1, "The registered gate count changed"
    gate = d["gates"][0]
    assert gate["gate"] == "CH23-1B", gate["gate"]
    items = gate["items"]
    assert [item["n"] for item in items] == list(range(1, 9))
    assert set(d["states"]) == set(EXPECTED_COUNTS)

    actual_states = {item["n"]: item["state"] for item in items}
    assert actual_states == EXPECTED_STATES, (
        f"Evidence identity changed without adjudication: {actual_states}"
    )
    counts = Counter(item["state"] for item in items)
    assert dict(counts) == EXPECTED_COUNTS, counts

    print(f"Frozen-text gate {gate['gate']} — {gate['chapter']}: {gate['chapter_title']}")
    print(f"  test: {gate['test']}")
    print(f"  rule: {gate['rule']}")
    print()

    for item in items:
        location = item["where"] or "—"
        print(f"  {item['n']}. {item['item']:<58}{item['state']:>18}")
        print(f"       carried by / boundary: {location}")
    print()

    for state in ("carried", "partly observable", "not disclosed", "not yet observed"):
        print(f"  {state}: {counts[state]} of {len(items)}")

    print()
    print("  These are research-panel coverage counts, not a market estimate.")
    print("  Item 4: lease/payment guarantees do not prove residual-value support.")
    print("  Item 5: asset valuation alone cannot disclose a loss waterfall.")
    print("  Item 7: no recorded default/restructuring in this borrower cohort.")
    print("  Item 8: matched collateral-resale evidence is not disclosed in the")
    print("          panel; physical resale may be observable before distress.")
    print("  Compute-price derivatives are not a proxy for collateral liquidity.")
    print()
    print("  The frozen Ch23 §1B analogy remains a research heuristic until")
    print("  adequate contract-level and matched transaction evidence closes")
    print("  the gate. No permanent impossibility theorem, S4 promotion, or")
    print("  change to the formal-report freeze follows from this tabulation.")


if __name__ == "__main__":
    main()
