#!/usr/bin/env python3
"""Recompute the ramp-period funding gap by composing layers 15 and 17.

Layer 15 owns the required cash floor per GW-year and the contracted revenue
per GW-year; layer 17 owns the energization schedule and the conversion
factors that turn energized capacity into revenue-bearing capacity. Neither
owns the time-phased composition, which is what this script computes:

    F(t) = integral of (required cash rate - revenue rate) dt

the cumulative cash that must come from somewhere other than this contract
before the contract's own revenue covers debt service.

The mechanism the composition exposes is an attachment mismatch: after first
energization the whole drawn facility pays debt service, while revenue
accrues only on the share of capacity that has reached a revenue-bearing
state. No solver, no calibration, no new anchors — every input is read from
the two upstream layers and asserted against their published values. All
outputs are D-grade report-side calculations.
"""
from __future__ import annotations
from pathlib import Path
import itertools
import json

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "research-validation" / "data"
C2C = DATA / "capital-to-cash-inputs.json"
ENERG = DATA / "energization-inputs.json"
RAMP = DATA / "ramp-gap-inputs.json"

# Layer 15 §4, US$B per GW-year, at 60% debt share and the 1.15x covenant.
# Asserted below rather than trusted, so the two layers cannot drift apart.
PUBLISHED_REQUIRED_CASH = {
    ("ig_backed_long", 20): 1.87,
    ("ig_backed_long", 30): 2.81,
    ("mid_coupon", 30): 3.98,
    ("mid_coupon", 40): 5.30,
    ("high_coupon_project", 30): 4.22,
    ("high_coupon_project", 50): 7.03,
}


def load():
    return tuple(
        json.loads(p.read_text(encoding="utf-8")) for p in (C2C, ENERG, RAMP)
    )


def annuity_payment(rate: float, tenor: float, principal: float) -> float:
    """Level annual payment; the same stand-in convention layer 15 uses."""
    return principal * rate / (1.0 - (1.0 + rate) ** -tenor)


def required_cash_per_gw_year(regime: dict, capital_per_gw: float) -> float:
    principal = regime["debt_share"] * capital_per_gw
    payment = annuity_payment(regime["rate"], regime["tenor_years"], principal)
    return regime["dscr_covenant"] * payment


def annual_required(t: float, r: float, cohort: float, deploy_years: float,
                    kappa: float) -> float:
    """Debt service accruing in year t, in US$B per year."""
    if t < deploy_years:
        share = max(0.0, t) / deploy_years
        return r * cohort * share * (1.0 - kappa)
    return r * cohort


def annual_revenue(t: float, v: float, cohort: float, f: float,
                   deploy_years: float, ramp_years: float) -> float:
    """Contracted revenue accruing in year t, in US$B per year."""
    if t <= deploy_years:
        return 0.0
    tau = min(t - deploy_years, ramp_years)
    return v * cohort * f * tau / ramp_years


def integrate(r: float, v: float, cohort: float, f: float, deploy_years: float,
              ramp_years: float, term: float, kappa: float,
              steps_per_year: int = 4000):
    """Return (times, cumulative shortfall) over the contract window."""
    dt = 1.0 / steps_per_year
    end = deploy_years + term
    times, cum, acc = [], [], 0.0
    n = int(round(end * steps_per_year))
    for i in range(n + 1):
        t = i * dt
        times.append(t)
        cum.append(acc)
        acc += (annual_required(t, r, cohort, deploy_years, kappa)
                - annual_revenue(t, v, cohort, f, deploy_years, ramp_years)) * dt
    return times, cum


def closed_form_peak(r: float, v: float, cohort: float, f: float,
                     deploy_years: float, ramp_years: float, kappa: float):
    """Peak cumulative shortfall and the time it occurs, in closed form."""
    coverage = v * f / r
    v_total = v * cohort * f
    r_total = r * cohort
    if coverage > 1.0:
        if kappa >= 1.0:
            tau = r_total * ramp_years / v_total
            peak = r_total * tau - v_total * tau * tau / (2.0 * ramp_years)
        else:
            pre = (1.0 - kappa) * r_total * deploy_years / 2.0
            tau = r_total * ramp_years / v_total
            peak = pre + r_total * tau - v_total * tau * tau / (2.0 * ramp_years)
        return peak, tau, coverage
    return float("inf"), float("inf"), coverage


def main():
    c2c, energ, ramp = load()

    contract = c2c["anchors"]["anthropic_aws_contract"]
    cohort = contract["gw_ceiling"]
    v = (contract["value_usd_b_floor"] / contract["years"]) / cohort
    assert abs(v - 2.00) < 1e-9, v
    assert cohort == 5

    # kappa = 1 is the usual construction-period treatment and is consistent
    # with a DSCR covenant tested post-COD; it is the base case.
    kappa_values = ramp["composition"]["capitalised_interest_share_kappa"]["values"]
    kappa_base = ramp["composition"]["capitalised_interest_share_kappa"]["base"]
    assert kappa_base == 1.0 and kappa_values[0] == 1.0
    term = ramp["contract_term_years"]
    deploy_grid = ramp["deployment_years_grid"]
    ramp_grid = energ["ramp_years_grid"]
    factors = energ["compounding_factors"]
    f_grid = sorted(
        a * b * c
        for a, b, c in itertools.product(
            factors["state_conversion"], factors["utilization"],
            factors["monetization"]
        )
    )
    f_low, f_high = f_grid[0], f_grid[-1]
    # The mid case is the product of each dial's mid value — the same
    # convention layer 17 publishes (0.5 x 0.7 x 0.9), not the median of the
    # 27 combinations, which is a different number (0.28).
    f_mid = 1.0
    for k in ("state_conversion", "utilization", "monetization"):
        g = sorted(factors[k])
        f_mid *= g[len(g) // 2]
    assert abs(f_mid - 0.315) < 1e-12, f_mid
    assert abs(f_low - 0.105) < 1e-12 and abs(f_high - 0.72) < 1e-12

    print("Required cash per GW-year, recomputed from layer 15's financing")
    print("regimes and asserted against its published table:")
    regimes = {}
    for reg in c2c["financing_regimes"]:
        regimes[reg["name"]] = reg
    for (name, cap), published in sorted(PUBLISHED_REQUIRED_CASH.items()):
        r = required_cash_per_gw_year(regimes[name], cap)
        assert abs(r - published) < 0.005, (name, cap, r, published)
        print(f"  {name:<24} US${cap}B/GW  ->  {r:.2f}  (15 publishes {published:.2f})")

    print()
    print(f"Contract anchor: US${contract['value_usd_b_floor']}B floor / "
          f"{contract['years']} yr / {cohort} GW ceiling")
    print(f"  contracted revenue per served GW-year  v = US${v:.2f}B")
    print(f"  full-delivery annual revenue           = US${v * cohort:.2f}B")

    print()
    print("Composed coverage at full deployment = v x f / r")
    print("(layer 15's ratio times layer 17's three conversion factors)")
    header = f"{'required cash r':<26}" + "".join(
        f"{lab:>10}" for lab in ("f=1.000", f"f={f_high:.3f}", f"f={f_mid:.3f}",
                                 f"f={f_low:.3f}")
    )
    print(header)
    for (name, cap), _ in sorted(PUBLISHED_REQUIRED_CASH.items()):
        r = required_cash_per_gw_year(regimes[name], cap)
        row = f"{name + ' @$' + str(cap) + 'B':<26}"
        for f in (1.0, f_high, f_mid, f_low):
            row += f"{v * f / r:>10.3f}"
        print(row)

    print()
    print("Annual contractual shortfall at full deployment, US$B/yr")
    print("(r x cohort - v x cohort x f; negative = contract covers)")
    print(f"{'required cash r':<26}" + "".join(
        f"{lab:>12}" for lab in ("f=1.000", f"f={f_high:.3f}", f"f={f_mid:.3f}",
                                 f"f={f_low:.3f}")
    ))
    for (name, cap), _ in sorted(PUBLISHED_REQUIRED_CASH.items()):
        r = required_cash_per_gw_year(regimes[name], cap)
        row = f"{name + ' @$' + str(cap) + 'B':<26}"
        for f in (1.0, f_high, f_mid, f_low):
            row += f"{r * cohort - v * cohort * f:>12.2f}"
        print(row)

    print()
    print("Ramp-period peak funding requirement, US$B "
          f"(base kappa={kappa_base}, D={deploy_grid[-1]}y, P={ramp_grid[-1]}y)")
    print("Closed form vs numerical integration of the same curve:")
    base_D, base_P = deploy_grid[-1], ramp_grid[-1]
    for (name, cap), _ in sorted(PUBLISHED_REQUIRED_CASH.items()):
        r = required_cash_per_gw_year(regimes[name], cap)
        for f, lab in ((1.0, "f=1.000"), (f_high, f"f={f_high:.3f}"),
                       (f_mid, f"f={f_mid:.3f}")):
            peak, tau, coverage = closed_form_peak(
                r, v, cohort, f, base_D, base_P, kappa_base)
            times, cum = integrate(r, v, cohort, f, base_D, base_P, term,
                                   kappa_base)
            num_peak = max(cum)
            if peak == float("inf"):
                # No peak and no crossover: the shortfall accumulates at a
                # constant annual rate for as long as the contract runs. The
                # cumulative figure is the mechanical consequence of that rate
                # and should be read as "does not close", never as a financing
                # plan.
                rate = r * cohort - v * cohort * f
                print(f"  {name}@${cap}B {lab}  coverage {coverage:.3f}"
                      f"  no crossover; accumulates {rate:5.2f}/yr"
                      f" to {cum[-1]:6.1f} by contract end")
                continue
            assert abs(num_peak - peak) < 0.05, (name, cap, f, num_peak, peak)
            t_peak = times[cum.index(num_peak)]
            # Crossover when the curve is followed beyond the contract window.
            unbounded = base_D + tau + peak / (v * cohort * f - r * cohort)
            t_cross = None
            for i in range(1, len(cum)):
                if cum[i - 1] > 0 and cum[i] <= 0:
                    t_cross = times[i]
                    break
            cross = (f"crosses y{t_cross:.1f} inside the term" if t_cross
                     else f"would cross y{unbounded:.1f}, "
                          f"{unbounded - (base_D + term):.1f}y after term end")
            print(f"  {name}@${cap}B {lab}  coverage {coverage:.3f}"
                  f"  peak {num_peak:6.2f} at y{t_peak:4.2f}"
                  f"  still {cum[-1]:6.2f} at contract end  {cross}")

    print()
    print("Two closed forms the tables above rely on, checked exactly:")
    r_ig = required_cash_per_gw_year(regimes["ig_backed_long"], 20)
    peak1, tau1, cov1 = closed_form_peak(r_ig, v, cohort, 1.0, 3, 4, 1.0)
    assert abs(r_ig - 1.87) < 0.005
    # Exact identities, checked against the computed r rather than the rounded
    # published value, so a rounding change in layer 15 cannot mask a break.
    assert abs(cov1 - v / r_ig) < 1e-12
    assert abs(tau1 - r_ig * 4 / v) < 1e-12
    assert abs(peak1 - cohort * r_ig * r_ig * 4 / (2 * v)) < 1e-12
    peak0, _, _ = closed_form_peak(r_ig, v, cohort, 1.0, 3, 4, 0.0)
    assert abs(peak0 - (r_ig * cohort * 3 / 2 + peak1)) < 1e-12
    # And the rounded values layer 15's published table implies, to 0.2.
    assert abs(peak1 - 17.6) < 0.2 and abs(peak0 - 31.6) < 0.2
    assert abs(cov1 - 1.067) < 0.001
    print(f"  kappa=1: peak {peak1:.2f} = C r^2 P / (2 v f),"
          f" at tau = r P / (v f) = {tau1:.2f}y, coverage {cov1:.3f}")
    print(f"  kappa=0: peak {peak0:.2f} = C r D / 2 + C r^2 P / (2 v f)"
          f"  (difference = {peak0 - peak1:.2f})")

    print()
    print("Sensitivity of the ramp-period peak to the capitalisation convention")
    print(f"(IG-backed long @$20B/GW, f=1.000 — the only covering case — "
          f"D={base_D}y, P={base_P}y):")
    for kappa in kappa_values:
        peak, _, cov = closed_form_peak(r_ig, v, cohort, 1.0, base_D, base_P,
                                        kappa)
        times, cum = integrate(r_ig, v, cohort, 1.0, base_D, base_P, term, kappa)
        assert peak != float("inf")
        print(f"  kappa={kappa:.1f}  coverage {cov:.3f}"
              f"  peak {max(cum):6.2f} at y{times[cum.index(max(cum))]:4.2f}"
              f"  still {cum[-1]:6.2f} at contract end")
    peak_k0, _, _ = closed_form_peak(r_ig, v, cohort, 1.0, base_D, base_P, 0.0)
    peak_k1, _, _ = closed_form_peak(r_ig, v, cohort, 1.0, base_D, base_P, 1.0)
    print(f"  full capitalisation is worth {peak_k0 - peak_k1:.2f} US$B"
          f" off the peak ({100 * (peak_k0 - peak_k1) / peak_k0:.0f}%)")

    print()
    print("Deployment-duration and ramp-width sensitivity "
          f"(IG-backed long @$20B/GW, f=1.000, kappa={kappa_base}):")
    peaks = {}
    for D in deploy_grid:
        for P in ramp_grid:
            peak, _, cov = closed_form_peak(r_ig, v, cohort, 1.0, D, P,
                                            kappa_base)
            times, cum = integrate(r_ig, v, cohort, 1.0, D, P, term, kappa_base)
            assert abs(max(cum) - peak) < 0.05
            peaks[(D, P)] = peak
            print(f"  D={D}y P={P}y  coverage {cov:.3f}  peak {peak:6.2f}"
                  f"  still {cum[-1]:6.2f} at contract end")
    # Under full capitalisation nothing is paid in cash before energization,
    # so the deployment period is cash-neutral and only the ramp sets the peak.
    for P in ramp_grid:
        assert abs(peaks[(deploy_grid[0], P)] - peaks[(deploy_grid[-1], P)]) < 1e-9
    assert abs(peaks[(base_D, 4)] / peaks[(base_D, 2)] - 2.0) < 1e-9
    print("  the peak is invariant in D and exactly linear in P: with full")
    print("  capitalisation the deployment period costs no cash, so only the")
    print("  ramp width moves the number. F_peak = C r^2 P / (2 v f) is linear")
    print("  in P and quadratic in r, so a doubling of the required-cash rate")
    print("  quadruples the peak.")
    print()
    print("Every input is read from layers 15 and 17; no new anchor is created.")


if __name__ == "__main__":
    main()
