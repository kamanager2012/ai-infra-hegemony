# Phase II · Time-to-Power Energization Surface v0.1

> **Status:** Research-side validation layer; not part of the frozen 32-chapter formal report, and does not change the formal 2026-08-28 evidence cutoff.  
> **Purpose:** compute the conversion the formal report refuses to *assert* — announced GW becoming energized, utilized, and revenue-bearing GW — as a **conditional schedule** over published lead-time ranges, so the physical clock that constrains every other layer becomes a surface a reader can set and challenge.  
> **Reproducible artifact:** `scripts/recompute_energization.py` over `data/energization-inputs.json`. Outputs are D-grade report-side calculations.  
> **Chinese translation (derived):** [17-energization-schedule-surface.zh.md](17-energization-schedule-surface.zh.md)

## 0. Ownership contract v0.1

This file owns:

- the **Time-to-Power schedule arithmetic** — the critical-path reading of the power ladder and its overlap credit;
- the **compounding identity** that converts announced GW into revenue-bearing GW through three explicit factors;
- the energized-share-by-year surface for a cohort, and its falsification conditions.

It does **not** own: the power-state definitions (Ch07, `10` Axis H, Ch29 §6 Dashboard E), the lead-time anchors themselves (Ch07 Table 7.2, IEA / LBNL), any project's actual state, utilization or monetization evidence (`04B`, `04C`, `10` Dashboard K), or the capital-to-cash division (`15`).

**Why a new owner.** The formal report and `10` correctly forbid treating committed / secured / design GW as energized or utilized capacity (`10` §2 rule 4; Axis H's main false positive). The refusal is about **assertion**. But the report's own S4 timeline, its power chapters, and `15`'s coverage arithmetic all require *some* view of when capacity actually energizes, and no layer owned the arithmetic that produces one conditionally. Without it, `15`'s "GW served" is a free dial with no physical anchor, and Ch28's phase structure has no clock behind it.

## 1. What is refused, and what is not

Refused, correctly:

- reading an announced or design figure as energized load;
- adding generation MW, PPA capacity, and IT-GW design capacity into one number (Ch07 §4 note);
- converting the national interconnection queue into unmet AI demand (Ch07 §5).

Not refused, and computed here:

> **Given a stage list and a set of stage durations, what is the schedule, where is the critical path, and how much does the answer move if you read the list as a conjunction instead of a sum?**

That is a statement about arithmetic, not about any project. It becomes a claim about the world only when a reader supplies real durations — which is the point.

## 2. The state ladder

The report's power states, unchanged:

```text
Contracted → Secured → Permitted → Construction → Energized → Utilized
```

Two rules carry over into this layer:

1. **Forward-only, event-gated.** A state change requires a dated event. Silence is not progress.
2. **No back-filling.** A project that is Energized today does not retroactively make last year's announced figure energized. The schedule is evaluated **as of an announcement date**, which is what makes it falsifiable.

## 3. The "+" is a conjunction, not a sum

Ch07 states that energized capacity is constrained by **permitting + interconnection + equipment procurement + construction**. Read as arithmetic, those stages add. Read as a critical path, they overlap and the total is the **maximum** over streams, not the sum.

Using the anchors already carried in Ch07 (IEA / LBNL), and treating each as a stream that *may* run in parallel:

| Reading | Fast end | Slow end |
|---|---:|---:|
| Series (additive) | 6 years | 15 years |
| Parallel (conjunction) | 4 years | 8 years |
| **Overlap credit** | **2 years** | **7 years** |

**This result cuts against the report's own inclination.** This report's house bias is toward caution about Time-to-Power. The arithmetic says that reading a stage list additively — which is the natural reading of a "+"-joined sentence — can overstate time to full energization by up to seven years. Publishing that is the point: a layer that only ever confirms the report's prior would not be worth maintaining.

The size of the credit depends entirely on which streams genuinely overlap. That is a **dial, not a finding**, and §7 names the observation that would settle it.

## 4. The reference band, and its stated limit

Ch07 is explicit that the 4–8 year transmission figure is a **broad grid-build clock, not a project-specific AI-data-center lead time**. It is used here only as a reference band. Every number in §3 moves if a reader substitutes project durations, and the calculator is built for exactly that substitution.

| Stream | Range (years) | Anchor |
|---|---:|---|
| Interconnection / transmission | 4–8 | IEA via Ch07 Table 7.2 |
| Large power transformer | 0–4 | IEA via Ch07 Table 7.2 ("up to 4 years"; 0 because the stream need not bind) |
| Site / equipment construction | 2–3 | IEA via Ch07 §5A |

**These are not project lead times and must never be quoted as such** — including from this file.

## 5. The compounding identity

Announced capacity becomes revenue-bearing capacity through three **nested** discounts, and it is a product:

```text
Revenue-bearing GW
=
Announced GW
x state conversion   (announced → energized)
x utilization
x monetization
```

Each factor is less than one in every case this report can observe, and each is separately owned: state conversion by this file, utilization and monetization by `04B` / `04C` / `10` Dashboard K.

Illustrative cohort of **100 GW** announced:

| Case | state conversion | utilization | monetization | revenue-bearing GW |
|---|---:|---:|---:|---:|
| low | 0.30 | 0.50 | 0.70 | **10.5 GW** |
| mid | 0.50 | 0.70 | 0.90 | **31.5 GW** |
| high | 0.80 | 0.90 | 1.00 | **72.0 GW** |

**This is the cleanest available statement of why announced GW is not a demand figure** — and note that it is a *product of three sub-one factors*, not a haircut someone chose.

Single-factor sensitivity, other factors at their mid values:

| Factor varied | low | mid | high |
|---|---:|---:|---:|
| state conversion | 0.189 | 0.315 | 0.504 |
| utilization | 0.225 | 0.315 | 0.405 |
| monetization | 0.245 | 0.315 | 0.350 |

State conversion moves the product most, which is the arithmetic justification for `15` existing at all: the first discount is both the largest and the least observable.

## 6. The surface

Energized share of a cohort, by year from announcement, under the parallel and series readings and two ramp widths:

| Reading | Ramp | 25% | 50% | 75% | 100% |
|---|---:|---:|---:|---:|---:|
| parallel-fast (4 y) | 2 y | y2.5 | y3.0 | y3.5 | y4.0 |
| parallel-fast (4 y) | 4 y | y1.0 | y2.0 | y3.0 | y4.0 |
| parallel-slow (8 y) | 4 y | y5.0 | y6.0 | y7.0 | y8.0 |
| series-fast (6 y) | 4 y | y3.0 | y4.0 | y5.0 | y6.0 |
| series-slow (15 y) | 4 y | y12.0 | y13.0 | y14.0 | y15.0 |

The 50% milestone spans **y2.0 to y13.0** — an eleven-year range produced entirely by two modelling choices and zero project data. That spread is the honest answer to "when does this capacity arrive," and it is why the report refuses a point estimate.

## 7. What would collapse it

1. **A named project disclosing dated state transitions** (permit granted, transformer delivered, energization) — replaces the streams with observations and shrinks §3's credit to a measured value.
2. **A disclosed partial-energization schedule** for a phased campus — replaces the ramp dial.
3. **A disclosed utilization rate on energized capacity** — removes the second factor in §5 and, together with (1), lets `15` stop using GW-served as a free dial.

## 8. Falsification conditions

1. **Realized schedules outside the 4–15 year envelope** for named large AI campuses would invalidate the reference band's applicability, in either direction.
2. **Overlapping streams shown not to overlap** (for example, transformer procurement gated behind interconnection approval) would collapse the parallel reading toward the series one, cutting the credit to zero.
3. **State conversion, utilization, and monetization shown not to be independent** — for example, if energized capacity is contractually pre-committed at full utilization — would invalidate the product form in §5. It would then be a minimum, not a product.
4. **Announced and energized capacity shown to move together** with a stable ratio would make the compounding identity trivial.

## 9. Boundary rules

- **Not a project lead time.** The §4 band is a system-level reference. Ch07's own warning transfers here verbatim.
- **No queue conversion.** Interconnection-queue GW is never converted into unmet AI demand (Ch07 §5).
- **No unit mixing.** Generation MW, PPA capacity, and IT-GW design capacity remain separate quantities and are never summed.
- **No scenario switch, no S4, no evidence grade.** Nothing here can change `10`'s scenario relevance, confirm S4, or enter the frozen chapters.
- **D-grade labeling is mandatory** wherever an output is reused, under `04-research-transparency`'s hierarchy.
- **The credit runs both ways.** A reader who believes the streams are fully sequential should use the series reading; this file does not argue them out of it. It argues only that the choice must be stated.

## 10. Integration

1. Re-run `scripts/recompute_energization.py` when the Ch07 anchors move or when a ramp/compounding dial changes; update tables rather than appending narrative.
2. **Supplies `15`.** This layer's state conversion is `15`'s "GW served" denominator. The two compose: `15` asks whether cash covers required cash per GW-year, and this file constrains how much GW is actually serving. That composition is now built, as [`18`](18-ramp-period-funding-gap.md). **The prohibition is against the scalar, not against the time axis:** `18` keeps both quantities in their own units on a common clock and produces a curve and three scalars (peak, term-end balance, crossover). No composite index — no single netted score — may be built from `15` and `17`, by `18` or by anything else.
3. **Proposed extension (not yet applied):** `10` Axis H could carry the §6 milestones as a dated sub-row once (1) a project discloses dated state transitions. Until then Axis H is unchanged, and this file remains the only place the schedule lives.

## Sources

- IEA transmission lead times (4–8 years) and grid-component procurement (cables 2–3 years; large power transformers up to 4 years) — carried in Ch07 Table 7.2 and §5A; https://www.iea.org/reports/energy-and-ai and https://www.iea.org/reports/key-questions-on-energy-and-ai
- Lawrence Berkeley National Laboratory, *Queued Up* — carried in Ch07 §5; used only as a friction indicator
- Power state ladder and its unit warnings — [`../publication/part-I-ch07-power-constraint.md`](../publication/part-I-ch07-power-constraint.md) §4, §5, §6
- Scenario-relevance and false-positive rules — [`10`](10-public-proxy-scenario-dashboard.md) §2, Axis H
- Evidence hierarchy and report-side calculation labeling — [Research Transparency](../publication/04-research-transparency.md)
