#!/usr/bin/env python3
"""Recompute the chain concentration-amplification surface.

Layer 11 draws the propagation chain

    anchor economics -> CoreWeave contract economics -> CoreWeave debt service
                     -> Core Scientific colocation cash flow
                     -> Core Scientific debt service

and states the discriminating variable -- independent cash generation
relative to fixed capital obligations -- without quantifying it. Layer 04C
records each link's obligations and the observed concentration between them.
This script computes what neither owns: how far an anchor shock travels down
a fixed-obligation chain, and how much headroom a link must already hold to
survive it.

The two quantities are dimensionless in the shock and require only observed
concentration ratios, so no revenue level has to be asserted. Every anchor is
read from 04C; nothing is inferred from another borrower. All outputs are
D-grade report-side calculations.
"""
from __future__ import annotations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "research-validation" / "data" / "chain-amplification-inputs.json"


def load():
    return json.loads(INPUT.read_text(encoding="utf-8"))


def coverage_after(coverage_before: float, c: float, x: float) -> float:
    """Coverage after an anchor decline x propagates through concentration c."""
    return coverage_before * (1.0 - c * x)


def absorbable_decline(coverage_before: float, c: float, floor: float) -> float:
    """Largest anchor decline the link survives at the given floor."""
    return (1.0 - floor / coverage_before) / c


def required_coverage(c: float, x: float, floor: float) -> float:
    """Coverage the link must already hold to sit exactly at the floor."""
    return floor / (1.0 - c * x)


def main():
    d = load()
    links = {l["name"]: l for l in d["chain"]["links"]}
    downstream = links["Core Scientific"]
    upstream = links["CoreWeave"]
    c = downstream["concentration_from_upstream"]
    floor = d["covenant_floor"]
    floor_ic = d["interest_coverage_floor"]

    assert c == 0.77
    assert floor == 1.15

    print("The chain, as observed (11 §2 / 04C §11B.5):")
    print(f"  {d['chain']['origin']}")
    for name in ("CoreWeave", "Core Scientific"):
        l = links[name]
        conc = l["concentration_from_upstream"]
        conc_s = "not disclosed (a dial)" if conc is None else f"{conc:.0%}"
        print(f"    -> {name:<16} concentration from upstream: {conc_s}")
    print(f"  observed covenant convention: {floor:.2f}x")
    print(f"  observed concentration anchor: c = {c:.2f} "
          f"({downstream['concentration_basis']})")

    print()
    print("1. Pass-through and residual")
    print(f"  a decline x at the origin reaches this link as c x = {c:.2f} x")
    print(f"  coverage_after = coverage_before x (1 - {c:.2f} x)")
    for x in (0.25, 0.5, 1.0):
        print(f"    anchor decline {x:>5.0%}  ->  revenue retained "
              f"{(1 - c * x):>6.1%}  coverage multiplier {(1 - c * x):.3f}x")
    residual = 1.0 - c
    assert abs(residual - 0.23) < 1e-12
    print(f"  at total shutdown the link keeps {residual:.0%} of its revenue: "
          f"the concentration ratio is")
    print("  simultaneously the amplification factor and the residual.")

    print()
    print("2. Required headroom — the coverage a link must already hold "
          f"to sit at the {floor:.2f}x floor")
    print(f"{'anchor decline':>16}{'at 1.15x floor':>18}{'at 1.00x floor':>18}")
    for x in d["anchor_decline_grid"]:
        rc15 = required_coverage(c, x, floor)
        rc10 = required_coverage(c, x, floor_ic)
        print(f"{x:>16.0%}{rc15:>18.3f}{rc10:>18.3f}")
    shutdown = required_coverage(c, 1.0, floor)
    assert abs(shutdown - 5.0) < 1e-12, shutdown
    print(f"  a total anchor shutdown requires {shutdown:.2f}x coverage "
          f"= {floor:.2f} / {residual:.2f}.")

    print()
    print(f"3. Absorbable decline at the {floor:.2f}x covenant floor")
    print(f"{'coverage before':>18}{'absorbable decline':>22}")
    for cb in d["coverage_before_grid"]:
        print(f"{cb:>18.2f}{absorbable_decline(cb, c, floor):>22.1%}")
    at_covenant = absorbable_decline(floor, c, floor)
    assert abs(at_covenant) < 1e-12
    print(f"  a link already sitting at the {floor:.2f}x covenant absorbs "
          f"{at_covenant:.0%}.")
    print("  The covenant floor, not the concentration, consumes most of the "
          "budget:")
    for cb in (1.3, 1.5):
        tot = absorbable_decline(cb, c, floor_ic)
        net = absorbable_decline(cb, c, floor)
        print(f"    at {cb:.2f}x: {tot:.1%} down to pure interest cover, "
              f"but only {net:.1%} before breaching the covenant")

    print()
    print("4. Chain depth — the shock attenuates downward")
    print("  cumulative pass-through = product of the concentrations; each")
    print("  additional link multiplies the arriving shock by its own c.")
    print(f"{'upstream c':>12}{'cumulative':>13}{'retained at shutdown':>23}"
          f"{'required coverage':>20}")
    for c1 in d["upstream_concentration_dial"]:
        cum = c1 * c
        print(f"{c1:>12.2f}{cum:>13.3f}{1 - cum:>23.1%}"
              f"{required_coverage(cum, 1.0, floor):>20.3f}x")
    print("  The nearest link therefore absorbs the larger fraction of any")
    print("  origin shock; position alone predicts consequence backwards.")

    print()
    print("5. The two transmission channels")
    ch = d["transmission_channels"]
    print(f"  A proportional: {ch['A_proportional']}")
    print(f"  B counterparty: {ch['B_counterparty']}")
    print("  The channels do not differ in expected level so much as in")
    print("  shape: A drifts, B steps. Where the upstream link breaches at")
    print("  an origin decline x*, B inflicts the full c at once while A")
    print("  would have inflicted only c x* at the same point — a step")
    print("  ratio of 1/x*.")
    print(f"{'upstream breach x*':>20}{'A damage at x*':>16}"
          f"{'B damage at x*':>16}{'step ratio':>13}")
    for xs in d["upstream_breach_decline_grid"]:
        a_dmg = c * xs
        print(f"{xs:>20.0%}{a_dmg:>16.3f}{c:>16.3f}{1 / xs:>13.2f}x")
    assert abs(c * 0.77 - 0.5929) < 1e-9
    print("  Distinguishing signature: under A the downstream link's revenue")
    print("  from the chain tracks the origin proportionally; under B it stays")
    print("  flat and then moves in a step. That is directly observable in the")
    print("  next downstream filing — the cheapest test this layer has.")

    print()
    print("6. The observed tiebreaker — concentration and immediacy point "
          "at different links")
    avail = upstream["undrawn_availability_usd_b"]
    due26 = upstream["principal_remainder_2026_usd_b"]
    due27 = upstream["principal_2027_usd_b"]
    print(f"  CoreWeave:   {due26:.1f} due remainder-2026 (+{due27:.1f} in 2027) "
          f"on {upstream['total_debt_usd_b']:.1f} total debt")
    print(f"               {avail:.1f} undrawn availability "
          f"(as of {upstream['undrawn_availability_as_of']})")
    r26 = avail / due26
    r2627 = avail / (due26 + due27)
    print(f"               committed undrawn / 2026 wall      = {r26:.2f}x")
    print(f"               committed undrawn / 2026+2027 wall = {r2627:.2f}x")
    assert abs(r26 - 1.6393) < 0.001 and abs(r2627 - 0.8475) < 0.001
    print(f"  Core Scientific: {downstream['principal_due_2026_2028_usd_b']:.1f} "
          f"due 2026-2028; {downstream['principal_due_2029_usd_m']:.1f} in 2029")
    print(f"               structural: {downstream['structural_note']}")
    print("  The more concentrated link has the milder wall and a lockbox;")
    print("  the link facing the immediate wall is the one the origin pays")
    print("  directly, and its 2027 wall is not covered by committed liquidity.")

    print()
    print("7. Fixed-obligation state at each link (observed)")
    for name in ("CoreWeave", "Core Scientific"):
        l = links[name]
        if name == "CoreWeave":
            rep, inc, cap = (l["q1_reported_interest_usd_m"],
                             l["q1_contractual_interest_usd_m"],
                             l["q1_capitalized_usd_m"])
            debt = l["total_debt_usd_b"] * 1000.0
            label = "Q1 2026"
        else:
            rep, inc, cap = (l["q2_reported_interest_usd_m"],
                             l["q2_interest_incurred_usd_m"],
                             l["q2_capitalized_usd_m"])
            debt = (l["senior_secured_notes_usd_b"] * 1000.0
                    + l["converts_2029_usd_m"] + l["converts_2031_usd_m"])
            label = "Q2 2026"
        print(f"  {name:<16} {label}  debt {debt / 1000:>6.1f}B  "
              f"reported interest {rep:>6.1f}M  "
              f"annualised {rep * 4:>7.1f}M  "
              f"blended {100 * rep * 4 / debt:>5.2f}%  "
              f"capitalised {cap / inc:>5.1%}")
    print("  The more concentrated link carries the cheaper blended cost of")
    print("  debt — but its blended rate includes a 0%-stated convertible,")
    print("  so the blended figure is not a like-for-like cost comparison.")

    print()
    print("Ranking rule (stated, not computed): pressure at a link is")
    print("  cumulative concentration x obligation due in window")
    print("  / (headroom above its own floor x revenue)")
    print("Per-link revenue and coverage are not carried in the repository,")
    print("so the rule is stated and the observed structural facts are placed")
    print("against it. No ranking is asserted.")
    print()
    print("Every anchor is read from 11 / 04C; no new numeric identity.")


if __name__ == "__main__":
    main()
