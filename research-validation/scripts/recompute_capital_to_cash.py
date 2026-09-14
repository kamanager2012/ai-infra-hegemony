#!/usr/bin/env python3
"""Recompute the Phase II capital-to-cash bridge from versioned inputs.

Every anchor in the input file is an existing graded claim elsewhere in the
repository. The grids, and the energy/opex dials, are report-side
illustrations. Outputs are D-grade report-side calculations and must never be
read as cost, shipment, utilization, or energized-capacity actuals.
"""
from __future__ import annotations
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "research-validation" / "data" / "capital-to-cash-inputs.json"


def load():
    return json.loads(INPUT.read_text(encoding="utf-8"))


def annuity_payment(principal_b: float, rate: float, years: int) -> float:
    """Fully amortizing annual payment, US$B."""
    if rate == 0:
        return principal_b / years
    return principal_b * rate / (1 - (1 + rate) ** -years)


def annuity_present_value(payment_b: float, rate: float, years: int) -> float:
    """Present value of an annual payment stream, US$B."""
    if rate == 0:
        return payment_b * years
    return payment_b * (1 - (1 + rate) ** -years) / rate


def main():
    d = load()
    a = d["anchors"]

    stargate_capital_per_gw = a["stargate_plan"]["value_usd_b"] / a["stargate_plan"]["gw"]
    print(
        f"Plan-scale illustration (NOT an observed cost; plan and secured-GW are different scopes): "
        f"US${stargate_capital_per_gw:.1f}B/GW"
    )
    assert math.isclose(stargate_capital_per_gw, 50.0, rel_tol=1e-12)

    support_per_gw = (
        a["ports_pike_support"]["guarantee_cap_usd_b"] / a["ports_pike_support"]["it_gw"]
    )
    print(f"PORTS-Pike guarantee cap per IT-GW: US${support_per_gw:.2f}B/IT-GW")
    assert math.isclose(support_per_gw, 24.705882352941178, rel_tol=1e-12)

    c = a["anthropic_aws_contract"]
    contract_per_gw_year = c["value_usd_b_floor"] / c["gw_ceiling"] / c["years"]
    print(
        f"Contracted revenue floor: US${contract_per_gw_year:.2f}B per GW-year "
        f"(floor: value >={c['value_usd_b_floor']}, GW <={c['gw_ceiling']})"
    )
    assert math.isclose(contract_per_gw_year, 2.0, rel_tol=1e-12)

    i = a["iren_fy2026"]
    iren_per_target_gw = i["ai_cloud_revenue_usd_m"] / 1000.0 / i["target_it_gw_2026"]
    print(
        f"IREN FY2026 AI cloud revenue per 2026 target GW: "
        f"US${iren_per_target_gw * 1000:.1f}M/GW (denominator is a target, not energized)"
    )
    assert math.isclose(iren_per_target_gw, 0.42933333333333334, rel_tol=1e-12)

    print()
    print("Required cash floor per GW-year (DSCR x annual debt service):")
    print(f"{'regime':<22}{'rate':>7}{'tenor':>7}{'debt sh.':>9}   required US$B/GW-yr by capital per GW")
    capital_grid = d["capital_per_gw_grid_usd_b"]
    header = "".join(f"{f'${g}B':>10}" for g in capital_grid)
    print(f"{'':<22}{'':>7}{'':>7}{'':>9}   {header}")
    required = {}
    for r in d["financing_regimes"]:
        row = []
        for g in capital_grid:
            debt = r["debt_share"] * g
            service = annuity_payment(debt, r["rate"], r["tenor_years"])
            req = r["dscr_covenant"] * service
            required[(r["name"], g)] = req
            row.append(f"{req:>10.2f}")
        print(
            f"{r['name']:<22}{r['rate']:>7.2%}{r['tenor_years']:>7}{r['debt_share']:>9.0%}   "
            + "".join(row)
        )
    assert math.isclose(required[("mid_coupon", 40)], 5.3012, rel_tol=5e-4)
    # §5's convention note divides by this cell at one more decimal than the
    # table displays, because the note's subject is the difference between the
    # unrounded and the displayed value. Printing it is what makes that division
    # reproducible rather than asserted in prose: a figure the document publishes
    # and the script does not print is a figure nothing can be checked against.
    print(f"mid_coupon @ US$30B/GW at 3 decimals, the value §5's note divides by: "
          f"{required[('mid_coupon', 30)]:.3f}")

    print()
    print("Contract-revenue coverage ratio (contracted floor / required cash floor):")
    print("contract revenue per GW-year = (value floor / years) / GW actually served")
    print(f"{'capital/GW':>11}{'GW served':>11}{'rev US$B/GW-yr':>17}{'regime':>22}{'coverage':>11}")
    for g in capital_grid:
        for cgw in d["contract_gw_grid"]:
            revenue = (c["value_usd_b_floor"] / c["years"]) / cgw
            for name in ("ig_backed_long", "mid_coupon", "high_coupon_project"):
                ratio = revenue / required[(name, g)]
                print(
                    f"{'$' + str(g) + 'B':>11}{cgw:>11}{revenue:>17.2f}{name:>22}{ratio:>11.2f}x"
                )

    print()
    print("Breakeven capital per GW at which the contracted floor just covers debt service:")
    for r in d["financing_regimes"]:
        allowed = contract_per_gw_year / r["dscr_covenant"]
        debt = annuity_present_value(allowed, r["rate"], r["tenor_years"])
        breakeven = debt / r["debt_share"]
        print(f"  {r['name']:<22} US${breakeven:.1f}B/GW")
    mid = d["financing_regimes"][1]
    assert math.isclose(
        annuity_present_value(contract_per_gw_year / mid["dscr_covenant"], mid["rate"], mid["tenor_years"])
        / mid["debt_share"],
        15.09,
        rel_tol=5e-3,
    )

    print()
    print("Illustrative energy cost per GW-year (full IT load; not a PPA claim):")
    e = d["energy_dial"]
    for price in e["usd_per_mwh"]:
        for u in e["utilization"]:
            twh = 1_000_000 * e["hours_per_year"] * u / 1e9
            cost = twh * 1e6 * price / 1e9
            print(f"  US${price}/MWh at {u:.0%} utilization: {twh:.2f} TWh -> US${cost:.3f}B/GW-yr")

    print()
    print("IREN denominator demonstration (revenue per DELIVERED GW = per-target-GW / delivery fraction):")
    base = required[("mid_coupon", 40)]
    print(f"  reference requirement: US${base:.2f}B/GW-yr (mid-coupon at US$40B/GW)")
    for f in d["iren_delivery_fraction_sensitivity"]:
        per_delivered = iren_per_target_gw / f
        print(
            f"  delivery fraction {f:.0%}: US${per_delivered * 1000:.1f}M per delivered GW-year"
            f"  (coverage {per_delivered / base:.2f}x)"
        )
    assert math.isclose(
        iren_per_target_gw / d["iren_delivery_fraction_sensitivity"][0] / base, 0.081, rel_tol=1e-2
    )


if __name__ == "__main__":
    main()
