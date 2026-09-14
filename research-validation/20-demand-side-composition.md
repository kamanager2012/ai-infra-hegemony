# Phase II · Demand-Side Composition & Incidence v0.1

> **Status:** Research-side validation layer; not part of the frozen 32-chapter formal report, and does not change the formal 2026-08-28 evidence cutoff.  
> **Purpose:** give the demand leg the arithmetic it has been missing — compose the observed adoption rates onto a common denominator, and show that the incidence question reduces to one ratio whose value bounds the demand effect rather than freeing it.  
> **Reproducible artifact:** `scripts/recompute_demand_composition.py` over `data/demand-composition-inputs.json`. Outputs are D-grade report-side calculations.  
> **Chinese translation (derived):** [20-demand-side-composition.zh.md](20-demand-side-composition.zh.md)

## 0. Ownership contract v0.1

This file owns:

- the **adoption → augmentation → displacement funnel**, and the conditional rates it exposes;
- the **denominator-sensitivity factor** between the two adoption instruments `14` §2 keeps separate;
- the **augmentation elasticity** of the substitution-eligible population;
- the **incidence identity** and what it does and does not bound;
- the **gate-state table** for the loop, and the rule that a conjunction with an unmeasured member takes no weight.

It does **not** own: the loop, its state variables, its clocks, or its gates (`14`), the labor and adoption evidence (`07`), the price-versus-margin question (`02`), scenario aggregation (`10`), or clearing adjudication (`01A`). It creates **no anchors** — every rate is read from `14` §2.

**Why a new owner.** `14` is the demand-side authority and is deliberately built out of state variables, clocks and gates: it names what to watch and refuses to put a number on it. That refusal is correct where it applies — `14` §3 gate G2 states outright that the claim that high income deciles drive a disproportionate share of spending is a *scenario assumption* until stated with its own same-denominator source. But the refusal has a boundary, and inside that boundary three things are computable from anchors the repository already carries, with no propensity asserted anywhere. Nothing owned them.

## 1. The funnel: three rates that were being read separately

`14` §2 evidence note B carries three rates from one instrument and one denominator:

| Rate | Value |
|---|---:|
| Firms using AI in at least one business function | 18% |
| Of adopters, mainly reporting task **augmentation** | 66% |
| Firms reporting employment **reductions** | 2% |

Read separately, "2% of firms" sounds negligible and is usually quoted that way. Composed:

| Derived rate | Value | What it means |
|---|---:|---|
| Reductions ÷ all adopters | **11.1%** | among firms that adopted at all |
| Non-augmenting adopters, share of all firms | **6.12%** | the substitution-eligible population |
| Reductions ÷ non-augmenting adopters | **32.7%** | among firms whose adoption is *not* mainly augmentation |

**The raw 2% hides a conditional rate near a third.** That is the first number in this layer and the reason it exists: the demand-side discussion has been conducted on the unconditional rate, which is the rate that makes the phenomenon look smallest.

**And the funnel stops there.** The panel cannot say whether the reductions reported come from non-augmenting adopters or are spread across all adopters. Both readings fit the same row — 32.7% if they concentrate, 11.1% if they do not. **That is a `not measured` boundary, not a zero and not a range**, and it is the specific thing a future filing or survey wave would close.

## 2. Denominator sensitivity: 3.83×

`14` §2 evidence note C carries a cross-country survey with a very different adoption base: **69% of firms actively using AI**, with **over 80% reporting no employment or productivity impact** over three years.

The two panels are never pooled — population, question, and recall window all differ — but they can be placed against the *same numerator*, and that is informative:

| Denominator | Conditional rate |
|---|---:|
| BTOS adoption base (18%) | 11.1% |
| Cross-country base (69%) | **2.9%** |

**Base spread 3.83×, conditional-rate spread 3.83× — identical, because the numerator does not move.** The choice of adoption base moves the answer by a factor of 3.83 with **no new evidence at all**. This is the report's denominator discipline stated as a number rather than as a rule.

The same substitution has a second use. Under the cross-country base, firms reporting **no impact** are `0.80 × 0.69 = 55.2%` of all firms — more than half of all firms using AI while reporting nothing. That is not a contradiction with the BTOS panel; it is what a different question, asked over a different window in a different population, produces. **Reading them as agreement or as disagreement are both errors.**

## 3. The augmentation share is the loop's own brake

Holding the adoption rate fixed, the substitution-eligible population is `18% × (1 − u)`:

| Augmenting share `u` | Non-augmenting share of all firms | vs. observed |
|---:|---:|---:|
| 0.50 | 9.00% | 1.47× |
| **0.66 (observed)** | **6.12%** | 1.00× |
| 0.80 | 3.60% | 0.59× |

**A 16-point fall in the augmentation share raises the substitution-eligible population by 47%.** The augmentation share is observed directly and every quarter, which is why `14` §6 lists "augmentation share stays dominant" as gate G1's first contrary signal. This makes that check quantitative: it is not a qualitative reassurance, it is a quantity with a known elasticity.

## 4. The incidence identity — why the demand leg is anchored

`14` §3 gate G2 asks which cohorts lose income and how much consumption they carry, and correctly refuses to answer without a same-denominator propensity source. What can be said without one is the **identity**:

```text
demand_effect  =  employment_effect  x  rho

rho = consumption propensity of the displaced / average consumption propensity
```

| `rho` | Demand effect per unit of employment effect |
|---:|---:|
| 0.60 | 0.60× |
| 1.00 | 1.00× |
| 1.40 | 1.40× |

**The demand effect is the employment effect times a ratio the evidence places near 1 and cannot place far from 1 without a source the repository does not have. Incidence therefore cannot make a small employment effect large, or a large one small.**

This is a **negative result and it is the layer's most useful one.** A demand-side narrative that wants the loop to be severe needs either a large employment effect or an extreme incidence ratio, and the second is bounded by the same propensities that govern all consumption. **The demand leg's severity is not a separate question from the labor evidence — it is that evidence times something near one.**

It is also the quantitative form of `14` §4's rule against computing an "output without income" residual across different-denominator accounts: `rho` **is** that rule, written as an equation.

`rho` stays a dial. The identity is the result; the dial is the thing to look for a source for.

## 5. The gate state, 2026

The loop is a conjunction — `14` §3 states that each gate can stop it independently — so it opens only when every gate is open. The observed 2026 state:

| Gate | Name | State | Owner |
|---|---|---|---|
| G1 | Substitution depth | **closed** — only a hiring-pipeline divergence; separations not moved | `03` |
| G2 | Income incidence | **not measured** — no same-denominator propensity-by-cohort source | `14` |
| G3 | Credit buffers | **not yet triggered** — no sustained income loss has accumulated | `14` |
| G4 | Price versus margin pass-through | **unresolved** — `02`'s structural E2/E3/E4 remain unestimated | `02` |
| G5 | Replacement demand and policy | **policy variable** — not legislated, not observed | `14` |
| G6 | Clock stacking | **structural rule** — an ordering, not a state | `14` |

**Open: 0 of 6. Not observable states: 3 of 6** — one not measured, one unresolved, one a policy variable that no evidence can settle in advance.

The honest 2026 statement is therefore **not** that the loop is mild. It is that **three of its six gates are not observable states**, and no weight, probability, or score may be assigned to a conjunction with an unmeasured member. Reporting a low probability here would be a number manufactured from the absence of measurement — the exact move `03` §17's `0 ≠ N/A ≠ not measured ≠ not yet observed` rule exists to prevent.

## 6. What would collapse it

1. **A wave of the BTOS panel reporting the reduction question by adoption purpose** would close §1's last step and replace the 11.1%/32.7% pair with one rate.
2. **A same-denominator consumption-propensity-by-cohort source** would replace `rho` with an observation and turn §4 into an estimate.
3. **An estimate of `02`'s E2/E3/E4** would resolve G4 and open or close the loop's price-versus-margin branch.
4. **A harmonized adoption question across instruments** would collapse §2's 3.83× spread.

## 7. Falsification conditions

1. **A reported within-non-augmenting-adopter displacement rate materially below 32.7%** — e.g. evidence that displacement reports cluster in augmentation adopters — would break the reading in §1.
2. **Augmentation share rising while adoption deepens** would shrink the substitution-eligible population and weaken the loop; this is `14` §7's condition 1 and §3 now gives it an elasticity.
3. **Evidence that the displaced carry consumption propensities far from the average** — in either direction — would move §4 off its anchoring result.
4. **A cohort-specific income panel showing the aggregate wage series masking large cohort losses** — `14` §4's own stated limitation of the labor-income proxy — would make the aggregate an unreliable anchor.

## 8. Boundary rules

- **No new numeric identity.** Every rate is read from `14` §2; the derived rates are arithmetic on those rates and nothing else.
- **No propensity asserted.** `rho` is a dial in every table it appears in. The identity is the result; the dial is a stated gap.
- **The two panels are never pooled.** Population, question, and recall window differ; §2 uses them only as a denominator-sensitivity demonstration against a shared numerator.
- **`not measured` is not zero.** §1's last step and §5's G2 and G4 are stated as unmeasured, never as small.
- **No exposure → outcome arithmetic.** `14` §4's anti-overreach rules apply unchanged; exposure indices remain non-convertible into employment or demand effects.
- **No double-counting.** A fact that updates the demand family here does not also update the financing family (`14` §5, `11` §3).
- **No scenario switch, no S4, no evidence grade, no composite index.** Nothing here can change `10`'s scenario relevance, confirm S4, or enter the frozen chapters; the funnel, the elasticity and the incidence identity must never be netted into a score.
- **D-grade labeling is mandatory** wherever an output is reused, under `04-research-transparency`'s hierarchy.

## 9. Integration

1. Re-run `scripts/recompute_demand_composition.py` when `14` §2's rates update, and update the tables rather than appending narrative.
2. **Feeds `14`.** This layer supplies the arithmetic `14` deliberately leaves out. `14` continues to own the loop, the clocks and the gate definitions; a change to any of those is a `14` change, not a change here.
3. **`10` §6D is unchanged.** The demand-side sub-rows already sit on Axis F under `14` ownership; this layer adds no row and changes no state.
4. `01A` adjudication: a within-substitution displacement rate is a demand-family contribution — recorded as one family among several, never as a standalone S4 confirmation and never multiplied into one index.

## Sources

No new external source. Every rate is read through `14` §2 with its evidence note.

- Adoption, augmentation and reduction rates — `14` §2 evidence note B (U.S. Census Bureau BTOS): https://www.census.gov/data/experimental-data-products/business-trends-and-outlook-survey.html
- Cross-country adoption and impact rates — `14` §2 evidence note C
- Labor-income and hiring observables, and the exposure evidence — [`07`](07-downstream-empirical-chains.md) §2; `14` §4
- Price-versus-margin gate — [`02`](02-demand-elasticity-calibration.md)
- Evidence hierarchy and report-side calculation labeling — [Research Transparency](../publication/04-research-transparency.md)
