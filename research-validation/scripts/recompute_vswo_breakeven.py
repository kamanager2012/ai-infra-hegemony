#!/usr/bin/env python3
"""Recompute the cost-per-VSWO break-even surface from versioned inputs.

Implements the closure identity already defined in P0-3 §2 / §17.4. It adds no
literature and no new numeric identities: every quantity is a dimensionless
ratio, so no output here is a claim about any process, vendor, or deployment.

Definitions (per workflow class, per attempt):
    per_attempt_cost = labor_minutes * minute_cost * (1 - s + rho) + ai_cost
    cost_per_persistent_verified_outcome = (per_attempt_cost + integration) / p
Integration enters per attempt, before the persistence division, because P0-3
§17.5 forbids allocating it only to successful workflows after the fact.
Normalized by baseline labor cost per outcome (labor_minutes * minute_cost):
    normalized_cost = (1 - s + rho + a + i) / p
Break-even in review share sets normalized_cost == 1:
    rho_breakeven = p - 1 + s - a - i
"""
from __future__ import annotations
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "research-validation" / "data" / "vswo-breakeven-inputs.json"


def normalized_cost(s: float, rho: float, p: float, i: float, a: float) -> float:
    return (1 - s + rho + a + i) / p


def rho_breakeven(s: float, p: float, i: float, a: float) -> float:
    return p - 1 + s - a - i


def p_breakeven(s: float, rho: float, i: float, a: float) -> float:
    return 1 - s + rho + a + i


def a_breakeven(s: float, rho: float, p: float, i: float) -> float:
    return p - 1 + s - rho - i


def main():
    d = json.loads(INPUT.read_text(encoding="utf-8"))
    a0 = d["inference_intensity"]

    # Identity check: each closed form must be the exact root of the direct cost identity.
    for s, rho, p, i in [(0.2, 0.1, 0.9, 0.0), (0.3, 0.05, 0.8, 0.1), (0.1, 0.0, 1.0, 0.0)]:
        rho_be = rho_breakeven(s, p, i, a0)
        assert math.isclose(normalized_cost(s, rho_be, p, i, a0), 1.0, rel_tol=1e-12)
        assert math.isclose(p_breakeven(s, rho_be, i, a0), p, rel_tol=1e-12)
        assert math.isclose(a_breakeven(s, rho_be, p, i), a0, rel_tol=1e-12)
    print("Closed-form break-even verified against the direct cost identity.")
    print(f"Normalized cost at p=1, i=0, a={a0}, s=0.2, rho=0.0: "
          f"{normalized_cost(0.2, 0.0, 1.0, 0.0, a0):.4f}")
    assert math.isclose(normalized_cost(0.2, 0.0, 1.0, 0.0, a0), 0.85, rel_tol=1e-12)

    print()
    print(f"Break-even review+remediation share rho (a={a0}, i=0):")
    header = "".join(f"{f'p={p:.2f}':>10}" for p in d["persistence_grid"])
    print(f"{'gross saving s':>15}{header}")
    for s in d["gross_saving_grid"]:
        row = "".join(f"{rho_breakeven(s, p, 0.0, a0):>10.3f}" for p in d["persistence_grid"])
        print(f"{s:>15.2f}{row}")

    print()
    print(f"Break-even review+remediation share rho with integration cost i=0.10 (a={a0}):")
    print(f"{'gross saving s':>15}{header}")
    for s in d["gross_saving_grid"]:
        row = "".join(f"{rho_breakeven(s, p, 0.10, a0):>10.3f}" for p in d["persistence_grid"])
        print(f"{s:>15.2f}{row}")

    print()
    print(f"Net cost change vs human baseline ({'negative = cheaper'}; p=1.00, i=0, a={a0}):")
    rheader = "".join(f"{f'r={r:.2f}':>10}" for r in d["review_share_grid"])
    print(f"{'gross saving s':>15}{rheader}")
    for s in d["gross_saving_grid"]:
        row = ""
        for r in d["review_share_grid"]:
            nc = normalized_cost(s, r, 1.0, 0.0, a0)
            row += f"{nc - 1:>+10.1%}"
        print(f"{s:>15.2f}{row}")

    print()
    print(f"Break-even persistence p (i=0, a={a0}):")
    print(f"{'gross saving s':>15}{rheader}")
    for s in d["gross_saving_grid"]:
        row = "".join(f"{p_breakeven(s, r, 0.0, a0):>10.3f}" for r in d["review_share_grid"])
        print(f"{s:>15.2f}{row}")

    print()
    print("Published effects from the existing P0-3 source list, run through the identity")
    print(f"(a={a0}, i=0): the table gives the review share at which the effect is exactly erased.")
    ph = "".join(f"{f'p={p:.2f}':>10}" for p in d["persistence_grid"])
    print(f"{'anchor':<58}{ph}")
    for e in d["published_effect_anchors"]:
        s = e["implied_s"]
        row = "".join(f"{rho_breakeven(s, p, 0.0, a0):>10.3f}" for p in d["persistence_grid"])
        print(f"{e['name'][:56]:<58}{row}")
    nber = d["published_effect_anchors"][0]["implied_s"]
    assert math.isclose(rho_breakeven(nber, 1.0, 0.0, a0), 0.0728, rel_tol=5e-3)
    metr = d["published_effect_anchors"][1]["implied_s"]
    print()
    print(f"METR negative control at s={metr:.2f}: break-even rho = "
          f"{rho_breakeven(metr, 1.0, 0.0, a0):.3f}, i.e. the saving is already negative "
          f"before any review or integration cost is added.")
    assert rho_breakeven(metr, 1.0, 0.0, a0) < 0


if __name__ == "__main__":
    main()
