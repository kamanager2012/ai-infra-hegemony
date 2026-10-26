#!/usr/bin/env python3
"""Stdlib-only replication of P0-2's Sol August 17 interrupted time series.

Reads the archived OpenRouter daily ranking CSV directly. Results are
observational, platform-visible price-normalized associations, NOT identified
causal/structural demand elasticities. No SciPy or Statsmodels required.
"""
from __future__ import annotations

import csv
import datetime as dt
import math
from collections import Counter, defaultdict
from pathlib import Path
from statistics import NormalDist

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "research-validation/data/openrouter-rankings-daily-2026-07-30_2026-08-28.csv"
SOL = "openai/gpt-5.6-sol-20260709"
EVENT = dt.date(2026, 8, 17)
PRICE_LOG = math.log(0.5)


def daily(path: Path = SOURCE) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as fd:
        rows = list(csv.DictReader(fd))
    if not rows or set(rows[0]) != {"排名", "日期", "模型", "tokens", "tokens可读"}:
        raise ValueError("Unexpected OpenRouter source columns")
    days = defaultdict(lambda: {"total": 0, "sol": None, "other": False,
                                "seen": set(), "n": 0})
    for row in rows:
        day = dt.date.fromisoformat(row["日期"])
        name = row["模型"]
        tokens = int(row["tokens"])
        if tokens <= 0 or name in days[day]["seen"]:
            raise ValueError(f"Bad count or duplicate model: {day} {name}")
        cell = days[day]
        cell["seen"].add(name)
        cell["n"] += 1
        cell["total"] += tokens
        if name == SOL:
            cell["sol"] = tokens
        if name == "other":
            cell["other"] = True
    dates = sorted(days)
    if dates != [dt.date(2026, 7, 30) + dt.timedelta(days=i) for i in range(30)]:
        raise ValueError("Expected 30 uninterrupted daily observations")
    if any(days[d]["n"] != 51 or not days[d]["other"]
           or days[d]["sol"] is None for d in dates):
        raise ValueError("Daily top 50 + other; Sol must be observed on all days")
    return [{"date": d, "total": days[d]["total"], "sol": days[d]["sol"]}
            for d in dates]


def solve(a: list[list[float]], b: list[float]) -> list[float]:
    """Small dense linear solve with partial pivoting; no external packages."""
    n = len(b)
    z = [a[i][:] + [b[i]] for i in range(n)]
    for j in range(n):
        pivot = max(range(j, n), key=lambda t: abs(z[t][j]))
        if abs(z[pivot][j]) < 1e-10:
            raise ValueError("Rank-deficient event regression")
        z[j], z[pivot] = z[pivot], z[j]
        v = z[j][j]
        for h in range(j, n + 1):
            z[j][h] /= v
        for i in range(n):
            if i == j:
                continue
            v = z[i][j]
            for h in range(j, n + 1):
                z[i][h] -= v * z[j][h]
    return [z[i][-1] for i in range(n)]


def fit(panel: list[dict], end: dt.date, *, market_control: bool = True,
        share_outcome: bool = False, lags: int = 3) -> dict:
    sample = [x for x in panel if x["date"] <= end]
    if sum(x["date"] >= EVENT for x in sample) < 4:
        raise ValueError("Post period must have at least four dates")
    xx, yy = [], []
    for i, r in enumerate(sample):
        x = [1.0, float(r["date"] >= EVENT), float(i)]
        if market_control:
            x.append(math.log(r["total"] - r["sol"]))
        x.extend(float(r["date"].weekday() == d) for d in range(1, 7))
        xx.append(x)
        yy.append(math.log(r["sol"]/r["total"] if share_outcome else r["sol"]))
    n, k = len(xx), len(xx[0])
    cross = [[sum(x[i]*x[j] for x in xx) for j in range(k)] for i in range(k)]
    target = [sum(x[i]*y for x,y in zip(xx,yy)) for i in range(k)]
    coeff = solve(cross, target)
    residuals = [y-sum(a*b for a,b in zip(row,coeff))
                 for row,y in zip(xx,yy)]
    meat = [[0.0]*k for _ in range(k)]
    for lag in range(lags+1):
        weight = 1.0 if lag == 0 else 1.0-lag/(lags+1)
        for t in range(lag,n):
            v = weight*residuals[t]*residuals[t-lag]
            for i in range(k):
                for j in range(k):
                    meat[i][j] += v*xx[t][i]*xx[t-lag][j]
                    if lag:
                        meat[i][j] += v*xx[t-lag][i]*xx[t][j]
    # Inverse row for coefficient index 1. Newey-West Bartlett HAC(3);
    # matches statsmodels HAC default: no finite-sample correction.
    invcol = [solve(cross,[float(j==i) for j in range(k)]) for i in range(k)]
    row = [invcol[j][1] for j in range(k)]
    variance = sum(row[i]*meat[i][j]*row[j]
                   for i in range(k) for j in range(k))
    if variance < 0:
        raise ValueError("Negative covariance diagonal")
    b,se = coeff[1], math.sqrt(variance)
    converted, error = b/PRICE_LOG, se/abs(PRICE_LOG)
    return {"n": n, "beta": b, "se": se,
            "price_normalized": converted, "ci_low": converted-1.96*error,
            "ci_high": converted+1.96*error,
            "p_z": 2*(1-NormalDist().cdf(abs(b/se))),
            "shift_ratio": math.exp(b)}


def main() -> None:
    p = daily()
    pre = [r for r in p if r["date"] < EVENT]
    post = [r for r in p if r["date"] >= EVENT]
    q0 = sum(r["sol"] for r in pre)/len(pre)
    q1 = sum(r["sol"] for r in post)/len(post)
    print("P0-2 / SOL AUG-17 — PLATFORM-VISIBLE ASSOCIATION (NOT CAUSAL)")
    print(f"Observations={len(p)}; rank rows=1530; model=Sol; price ratio=0.5")
    print(f"pre_daily_B={q0/1e9:.4f}; post_daily_B={q1/1e9:.4f}; raw_ratio={q1/q0:.6f}")
    print("Formula: ln(Sol) ~ post + ln(nonSol) + linear time + weekday FE")
    print("HAC: Bartlett, lag 3, no small-sample adjustment, normal CI")
    for end in [dt.date(2026,8,20),dt.date(2026,8,24),dt.date(2026,8,28)]:
        r = fit(p,end)
        print(f"benchmark end={end} n={r['n']} beta={r['beta']:.6f} "
              f"SE={r['se']:.6f} normalized={r['price_normalized']:.6f} "
              f"CI=[{r['ci_low']:.6f},{r['ci_high']:.6f}] p(z)={r['p_z']:.7g}")
    for label, control, share in [
        ("no_market_control", False, False),
        ("share_outcome", False, True),
    ]:
        r = fit(p,dt.date(2026,8,28),market_control=control,share_outcome=share)
        print(f"alternative={label} normalized={r['price_normalized']:.6f} "
              f"CI=[{r['ci_low']:.6f},{r['ci_high']:.6f}]")
    base = fit(p,dt.date(2026,8,28))
    checks = [(base["beta"],0.3236564),(base["se"],0.0792717),
              (base["price_normalized"],-0.4669375)]
    for actual, expected in checks:
        if abs(actual-expected) >= 0.0005:
            raise AssertionError(f"Published benchmark drifted: {actual} != {expected}")
    print("PASS — coefficient, HAC SE, and price-normalized value match archived v0.8")


if __name__ == "__main__":
    main()
