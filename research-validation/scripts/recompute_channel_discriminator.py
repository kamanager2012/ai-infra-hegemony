#!/usr/bin/env python3
"""Recompute the two channels' predicted retention curves and the test that
discriminates them.

Layer 11 §2 draws the propagation chain and layer 19 §6 shows that an origin
shock can reach a downstream link by one of two mechanisms: proportional
pass-through (A), where the intermediate obligation is variable, or a
counterparty step (B), where it is fixed. 19 records that the observed lockbox
is evidence for B and says the next downstream filing tests which one is
operating.

That sentence is not executable as it stands: it names no observable, no
statistic and no threshold, and it omits a precondition. This script supplies
the first three and prints the fourth.

The two channels are two claims about **one slope**. Under A the downstream
link's chain revenue falls continuously with the upstream decline; under B it
is flat until the upstream link breaches. Both claims are functions of the
single observed concentration c = 0.77 that 04C §11B.5 carries, so the whole
test is arithmetic on one observed ratio: no revenue level, coverage or breach
probability is asserted anywhere, and no anchor is inferred from another
borrower. All outputs are D-grade report-side calculations.
"""
from __future__ import annotations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "research-validation" / "data" / "channel-discriminator-inputs.json"


def load():
    return json.loads(INPUT.read_text(encoding="utf-8"))


def retention_under_a(c: float, u: float) -> float:
    """Downstream chain revenue retained when the upstream decline u arrives
    through a variable intermediate obligation."""
    return 1.0 - c * u


def retention_under_b(c: float, u: float, breached: bool) -> float:
    """The same quantity when the intermediate obligation is fixed: flat until
    the upstream link breaches, then one step of size c."""
    return 1.0 - c if breached else 1.0


def upstream_decline_for_resolution(c: float, delta: float) -> float:
    """Smallest upstream decline that moves the downstream series by more than
    the disclosure can resolve. The two channels differ by exactly c u, so a
    downstream observation resolves their separation only once c u > delta."""
    return delta / c


def main():
    d = load()
    c = d["concentration"]["value"]
    grid = d["upstream_decline_grid"]
    resolutions = d["resolution_grid"]
    assert c == 0.77, "the only observed link concentration"

    print("Channel discrimination test")
    print(f"concentration c = {c:.2f}  ({d['concentration']['basis']})")
    print()

    print("1. What each channel predicts, in the downstream link's chain revenue")
    print(f"  {'upstream':>9}{'A retention':>14}{'B retention':>14}"
          f"{'separation':>13}")
    for u in grid:
        a = retention_under_a(c, u)
        b = retention_under_b(c, u, breached=False)
        sep = b - a
        print(f"  {u:>8.0%}{a:>14.1%}{b:>14.1%}{sep:>13.1%}")
    print("  A is a straight line of slope -0.770 through (1, 0).")
    print("  B is flat at 100% and then takes one step of size c at the")
    print("  upstream breach, which the row for u = 1.0 stands for.")
    print("  The separation is c u: the downstream series is always a damped")
    print("  copy of the upstream one, because c < 1.")
    print()

    print("2. The precondition 19 §6 did not state")
    print("  At u = 0 both channels predict the same observation: 100%.")
    print("  A flat downstream series is therefore evidence for B only in")
    print("  proportion to a measured upstream decline. Read without one it")
    print("  is consistent with both, so the test is not a single-filing")
    print("  test: it reads the upstream link's reported revenue as the")
    print("  antecedent and the downstream link's chain revenue as the")
    print("  consequent, and needs both.")
    print()

    print("3. Resolving power — the upstream decline each resolution needs")
    print(f"  {'resolution (of downstream chain revenue)':>42}{'upstream decline':>19}")
    for delta in resolutions:
        u_min = upstream_decline_for_resolution(c, delta)
        print(f"  {delta:>40.0%}{u_min:>19.1%}")
    print("  Both columns are fractions of their own series, so the table is")
    print("  dimensionless: the reader substitutes the reporting granularity")
    print("  of the series they actually have.")
    print()

    print("4. Pre-registered verdicts — four outcomes, not two")
    print("  slope near 0        -> B operating. The lockbox reading is")
    print("                         confirmed by behaviour, and 19 §6 collapses")
    print("                         to one mechanism.")
    print("  slope near -0.770   -> A operating. The lockbox does not fix the")
    print("                         obligation, and 19 §6's structural")
    print("                         inference is contradicted by behaviour.")
    print("  slope between       -> neither channel. The dichotomy itself is")
    print("                         falsified by observation and must be")
    print("                         re-derived, not re-labelled.")
    print("  slope steeper       -> the denominator is wrong: something other")
    print("                         than the chain moved the downstream")
    print("                         link's revenue too.")
    print()
    print("  The table is fixed before the data arrives. A verdict table that")
    print("  can be edited after reading the filing is not a test.")
    print()
    print(f"Predicted slope under A: {-c:.3f} (magnitude 0.770); under B: 0.000.")
    print("Every anchor is read from 11 / 04C through 19; no new numeric identity.")


if __name__ == "__main__":
    main()
