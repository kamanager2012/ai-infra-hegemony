#!/usr/bin/env python3
"""Recompute the Time-to-Power schedule surface from versioned inputs.

Implements the announced -> energized -> utilized -> revenue-bearing schedule
arithmetic. Every lead-time stream is an anchor already carried in Ch07; the
ramp shapes, ramp widths and compounding factors are report-side illustrations.

The structural result computed here is the *overlap credit*: the difference
between reading a stage list as arithmetic addition and reading it as a
conjunction whose streams can run in parallel. Outputs are D-grade report-side
calculations and make no claim about any project.
"""
from __future__ import annotations
from pathlib import Path
import itertools
import json

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "research-validation" / "data" / "energization-inputs.json"


def load():
    return json.loads(INPUT.read_text(encoding="utf-8"))


def series_total(streams: dict, fast: bool) -> float:
    idx = 0 if fast else 1
    return sum(v["years"][idx] for v in streams.values())


def parallel_total(streams: dict, fast: bool) -> float:
    idx = 0 if fast else 1
    return max(v["years"][idx] for v in streams.values())


def energized_share(t: float, t_full: float, ramp_years: float) -> float:
    t_begin = t_full - ramp_years
    if t < t_begin:
        return 0.0
    if t >= t_full:
        return 1.0
    return (t - t_begin) / ramp_years


def milestone_year(t_full: float, ramp_years: float, share: float) -> float:
    return (t_full - ramp_years) + ramp_years * share


def main():
    d = load()
    s = d["lead_time_streams"]

    print("Lead-time streams (years), from anchors already carried in Ch07:")
    for name, v in s.items():
        print(f"  {name:<32}{v['years'][0]:>3}-{v['years'][1]:<3}"

              f" ({v['anchor'].split(':')[0]})")

    print()
    print("Critical-path totals and the overlap credit (years to full energization):")
    print(f"{'reading':<28}{'fast end':>10}{'slow end':>10}")
    ser_f, ser_s = series_total(s, True), series_total(s, False)
    par_f, par_s = parallel_total(s, True), parallel_total(s, False)
    print(f"{'series (additive reading)':<28}{ser_f:>10.0f}{ser_s:>10.0f}")
    print(f"{'parallel (conjunction reading)':<28}{par_f:>10.0f}{par_s:>10.0f}")
    print(f"{'overlap credit':<28}{ser_f - par_f:>10.0f}{ser_s - par_s:>10.0f}")
    assert (ser_f, ser_s) == (6, 15), (ser_f, ser_s)
    assert (par_f, par_s) == (4, 8), (par_f, par_s)

    print()
    print("Energized share of a cohort, by year from announcement:")
    for mode, t_full in (("parallel-fast", par_f), ("parallel-slow", par_s),
                         ("series-fast", ser_f), ("series-slow", ser_s)):
        for ramp in d["ramp_years_grid"]:
            marks = ", ".join(
                f"{int(sh * 100)}% at y{milestone_year(t_full, ramp, sh):.1f}"
                for sh in (0.25, 0.5, 0.75, 1.0)
            )
            print(f"  {mode:<14} ramp {ramp}y (full y{t_full:.0f}): {marks}")
    assert abs(milestone_year(8, 4, 0.5) - 6.0) < 1e-12
    assert abs(milestone_year(15, 2, 1.0) - 15.0) < 1e-12

    print()
    cohort = d["cohort_gw_illustrative"]
    cf = d["compounding_factors"]
    print(f"Compounding: announced {cohort} GW -> revenue-bearing GW")
    print("(state conversion x utilization x monetization; every factor is a dial)")
    lo = min(cf["state_conversion"]) * min(cf["utilization"]) * min(cf["monetization"])
    hi = max(cf["state_conversion"]) * max(cf["utilization"]) * max(cf["monetization"])
    mid = [0.5, 0.7, 0.9]
    print(f"  low case:  {lo:.3f} -> {cohort * lo:.1f} GW")
    print(f"  mid case:  {mid[0] * mid[1] * mid[2]:.3f} -> {cohort * mid[0] * mid[1] * mid[2]:.1f} GW")
    print(f"  high case: {hi:.3f} -> {cohort * hi:.1f} GW")
    assert abs(lo - 0.105) < 1e-12 and abs(hi - 0.72) < 1e-12

    print()
    print("Single-factor sensitivity of the compounding product (mid case on the others):")
    for name, grid in cf.items():
        if name == "note":
            continue
        others = [v for k, v in cf.items() if k not in (name, "note")]
        base = 1.0
        for g in others:
            base *= sorted(g)[len(g) // 2]
        row = "".join(
            f"{sorted(grid)[i] * base:>9.3f}" for i in range(len(grid))
        )
        print(f"  {name:<20} {'':>9}{row}")
    prods = sorted(
        a * b * c
        for a, b, c in itertools.product(
            cf["state_conversion"], cf["utilization"], cf["monetization"]
        )
    )
    print(f"  full product range: {prods[0]:.3f} to {prods[-1]:.3f} "
          f"({len(prods)} combinations)")
    assert prods[0] == lo and prods[-1] == hi


if __name__ == "__main__":
    main()
