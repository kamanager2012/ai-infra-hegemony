#!/usr/bin/env python3
"""Recompute the demand-side composition and incidence surface.

Layer 14 owns the demand-side loop, its state variables and its clocks, and
explicitly declines to put a number on gate G2 because no same-denominator
consumption-propensity-by-cohort source exists. This script computes what can
be computed anyway:

  1. the adoption -> augmentation -> displacement funnel, by putting the
     three observed BTOS rates on a common denominator;
  2. the denominator-sensitivity factor, i.e. how much the conditional
     displacement rate moves purely on the choice of adoption base;
  3. the augmentation elasticity of the substitution-eligible population;
  4. the incidence identity, which shows the demand leg is anchored to the
     employment effect rather than free to be larger than it.

Every rate is read from 14 §2; nothing is estimated. Propensity stays a dial.
All outputs are D-grade report-side calculations.
"""
from __future__ import annotations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "research-validation" / "data" / "demand-composition-inputs.json"


def load():
    return json.loads(INPUT.read_text(encoding="utf-8"))


def main():
    d = load()
    b = d["adoption_panel_btos"]
    x = d["adoption_panel_cross_country"]
    a = b["firms_using_ai_share"]
    u = b["adopters_mainly_augmenting_share"]
    r = b["firms_reporting_employment_reductions_share"]

    assert (a, u, r) == (0.18, 0.66, 0.02), (a, u, r)

    print("1. The adoption -> augmentation -> displacement funnel")
    print("   All three rates come from the same instrument and the same")
    print("   denominator, so they compose.")
    print(f"   firms using AI in at least one function      {a:>8.1%}")
    print(f"   of adopters, mainly augmenting               {u:>8.1%}")
    print(f"   of adopters, not mainly augmenting           {1 - u:>8.1%}")
    print(f"   firms reporting employment reductions        {r:>8.1%}")

    non_aug = a * (1.0 - u)
    rate_on_adopters = r / a
    rate_on_non_aug = r / non_aug
    print()
    print("   Two conditional rates the raw 2% hides:")
    print(f"     reductions / all adopters                  "
          f"{rate_on_adopters:>8.1%}")
    print(f"     reductions / non-augmenting adopters       "
          f"{rate_on_non_aug:>8.1%}")
    assert abs(rate_on_adopters - 0.111111) < 1e-5
    assert abs(rate_on_non_aug - 0.326797) < 1e-5
    assert abs(non_aug - 0.0612) < 1e-9
    print(f"   non-augmenting adopters are {non_aug:.2%} of all firms — the")
    print("   substitution-eligible population under this instrument.")

    print()
    print("   The last step of the funnel is NOT measured: the panel cannot")
    print("   say whether the reductions reported come from non-augmenting")
    print("   adopters or are spread across all adopters. Both readings are")
    print(f"   consistent with the same row — {rate_on_non_aug:.1%} if they")
    print(f"   concentrate, {rate_on_adopters:.1%} if they do not. That is a")
    print("   `not measured` boundary, not a zero and not a range.")

    print()
    print("2. Denominator sensitivity — the same numerator, a different base")
    s = x["firms_actively_using_share"]
    rate_on_cross = r / s
    spread = s / a
    print(f"   reductions / BTOS adoption base    ({a:.0%})   "
          f"{rate_on_adopters:>8.1%}")
    print(f"   reductions / cross-country base    ({s:.0%})   "
          f"{rate_on_cross:>8.1%}")
    print(f"   base spread {spread:.2f}x  ->  conditional-rate spread "
          f"{spread:.2f}x")
    assert abs(spread - 3.833333) < 1e-5
    print(f"   Because the numerator is identical, the choice of adoption base")
    print(f"   moves the answer by exactly {spread:.2f}x with no new evidence.")
    print("   The two panels are never pooled: population, question and")
    print("   recall window all differ.")

    print()
    print("3. Augmentation elasticity of the substitution-eligible population")
    print("   (holding the adoption rate fixed)")
    print(f"{'augmenting share u':>20}{'non-augmenting share':>22}"
          f"{'vs. observed':>15}")
    for uu in d["augmentation_share_dial"]:
        na = a * (1.0 - uu)
        print(f"{uu:>20.2f}{na:>22.2%}{na / non_aug:>15.2f}x")
    d_u = 0.66 - 0.50
    elast = (a * (1.0 - 0.50)) / non_aug - 1.0
    print(f"   a {d_u * 100:.0f}-point fall in the augmentation share raises the")
    print(f"   substitution-eligible population by {elast:.0%}.")
    assert abs(elast - 0.470588) < 1e-5
    print("   The augmentation share is the loop's own brake, and it is")
    print("   observed directly — which is why gate G1's first contrary")
    print("   signal in 14 §6 is 'augmentation share stays dominant'.")

    print()
    print("4. The incidence identity — why the demand leg is anchored")
    print("   demand_effect = employment_effect x rho")
    print("   rho = consumption propensity of the displaced / average")
    print(f"{'rho':>8}{'demand effect per unit of employment effect':>46}")
    for rho in d["incidence"]["rho_dial"]:
        print(f"{rho:>8.2f}{rho:>46.2f}x")
    print("   The demand effect is the employment effect times a ratio that")
    print("   the evidence places near 1 and cannot place far from 1 without a")
    print("   same-denominator propensity-by-cohort source. Incidence therefore")
    print("   cannot make a small employment effect large, or a large one")
    print("   small. This is the quantitative form of 14 §4's rule against")
    print("   computing an 'output without income' residual across")
    print("   different-denominator accounts.")
    print("   The repository carries no propensity-by-cohort panel, so rho")
    print("   stays a dial — the identity is the result, not the dial.")

    print()
    print("5. Gate state, 2026 — the loop is a conjunction, so it opens only")
    print("   when every gate is open independently.")
    counts = {}
    for g in d["gate_states_2026"]:
        counts[g["state"]] = counts.get(g["state"], 0) + 1
        print(f"   {g['gate']}  {g['name']:<34} {g['state']:<18} "
              f"[{g['owner']}]")
    print()
    print(f"   open: {counts.get('open', 0)} of {len(d['gate_states_2026'])}")
    for k in ("closed", "not measured", "not yet triggered", "unresolved",
              "policy variable", "structural rule"):
        if k in counts:
            print(f"   {k}: {counts[k]}")
    print("   No weight, probability or score may be assigned to a conjunction")
    print("   with an unmeasured member. The honest 2026 statement is not that")
    print("   the loop is mild — it is that three of its six gates are not")
    print("   observable states: one is not measured, one is unresolved, and")
    print("   one is a policy variable that no evidence can settle in advance.")
    print()
    print("Every rate is read from 14 §2; no new numeric identity.")


if __name__ == "__main__":
    main()
