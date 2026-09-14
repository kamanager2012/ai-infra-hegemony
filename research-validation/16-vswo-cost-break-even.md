# Phase II · Cost-per-VSWO Break-Even Surface v0.1

> **Status:** Research-side validation layer; not part of the frozen 32-chapter formal report, and does not change the formal 2026-08-28 evidence cutoff.  
> **Purpose:** write down the break-even algebra that is already implicit in P0-3's closure identity, in **dimensionless** form, so that any claimed AI workflow effect can be checked against the review, persistence, and integration conditions it requires — without the report needing primary data it does not have.  
> **Reproducible artifact:** `scripts/recompute_vswo_breakeven.py` over `data/vswo-breakeven-inputs.json`. Outputs are D-grade report-side calculations.  
> **Chinese translation (derived):** [16-vswo-cost-break-even.zh.md](16-vswo-cost-break-even.zh.md)

## 0. Ownership contract v0.1

This file owns:

- the **normalized break-even algebra** of the P0-3 cost-per-VSWO identity;
- the break-even values of each lever (review burden, persistence, integration cost, inference intensity) conditional on the others;
- the application of that algebra to effects already recorded in `03`'s evidence ledger.

It does **not** own: the metric definitions (`03` §2), the companion metrics (`03` §3), the closure identity itself (`03` §17.4), the acquisition contract (`03` §17), the evidence ledger (`03` §8 / §12), or any factual claim about any workflow, vendor, or deployment.

**Why this is a new file and not a `03` upgrade.** `03` §17.9 freezes P0-3 literature expansion and limits further upgrades to three inputs: a public same-`workflow_id` Level-3 dataset, a first-party prospective dataset, or a methodological result that materially changes verification / persistence / attribution. This file is none of those. It adds **no literature** and **no new numeric identities** — it is an implementation of algebra that `03` already states, and `03` therefore remains at v0.7. If this file ever produces a result that changes attribution, that result goes through the `03` upgrade gate rather than into this file.

## 1. What was missing

`03` defines the metric, the closure identity, the required companion metrics, and the minimum publishable output. What it did not contain is the **inverse** question:

> For a claimed effect, what must be true about the parts the vendor does not report, for the effect to survive the full cost stack?

That inverse is what makes the definitions operational. It is also answerable without any dataset, because it can be expressed entirely in ratios.

## 2. Normalized formulation

Per workflow class, per **attempt** (one full pass to a candidate outcome, including internal retries):

```text
per_attempt_cost = labor_minutes x minute_cost x (1 - s + rho) + ai_cost + integration
cost_per_persistent_verified_outcome = per_attempt_cost / p
```

with:

| Symbol | Meaning |
|---|---|
| **s** | gross execution-time saving, as a share of baseline minutes per attempt |
| **rho** | review + remediation minutes, as a share of baseline minutes per attempt |
| **p** | probability a candidate outcome is **verified and persists** over the measurement window |
| **a** | AI / tool / runtime / retry cost per attempt, as a share of baseline labor cost per outcome |
| **i** | allocated integration / mapping cost per attempt, as a share of baseline labor cost per outcome |

Normalizing by baseline labor cost per outcome (so every quantity is dimensionless):

```text
normalized_cost = (1 - s + rho + a + i) / p
```

Setting `normalized_cost = 1` and solving:

```text
rho_breakeven = p - 1 + s - a - i
p_breakeven   = 1 - s + rho + a + i
a_breakeven   = p - 1 + s - rho - i
```

**Placement rule.** `a` and `i` enter the numerator **before** the `/p` division, because `03` §17.5 forbids allocating integration cost only to successful workflows after the fact. A formulation that divides by persistence first systematically understates the penalty of failed attempts.

**Why normalization is the point.** Every quantity is a ratio, so the identity makes **no factual claim about any process**. It states conditions, not measurements. That is what allows a quantitative artifact to exist here at all, given that no public Level-3 dataset does.

**One conversion rule.** A reported *productivity* gain is not a *time* saving. If output per unit time rises by `g`, time per outcome falls by `1 - 1/(1+g)`. A "+14% productivity" claim is `s = 0.123`, not `s = 0.14`. Where a source reports a time change directly, it enters unchanged. The rule is executed, not merely stated: `recompute_vswo_breakeven.py` applies it to the recorded gain and asserts the result against the recorded conversion, so the two cannot drift apart and the published `0.123` is produced by arithmetic rather than entered by hand. The register re-runs the same rule with its own implementation, for the reason a rule stated only in prose cannot fail.

## 3. Break-even review burden

Review + remediation share at which the effect is exactly erased (`a = 0.05`, `i = 0`):

| gross saving s | p = 1.00 | p = 0.95 | p = 0.90 | p = 0.80 |
|---:|---:|---:|---:|---:|
| 0.10 | **0.050** | −0.000 | −0.050 | −0.150 |
| 0.20 | 0.150 | 0.100 | 0.050 | −0.050 |
| 0.30 | 0.250 | 0.200 | 0.150 | 0.050 |
| 0.40 | 0.350 | 0.300 | 0.250 | 0.150 |

With integration cost `i = 0.10` the same surface shifts down by exactly 0.10:

| gross saving s | p = 1.00 | p = 0.95 | p = 0.90 | p = 0.80 |
|---:|---:|---:|---:|---:|
| 0.10 | −0.050 | −0.100 | −0.150 | −0.250 |
| 0.20 | 0.050 | −0.000 | −0.050 | −0.150 |
| 0.30 | 0.150 | 0.100 | 0.050 | −0.050 |
| 0.40 | 0.250 | 0.200 | 0.150 | 0.050 |

**Read the first table directly:** a 10% time saving survives only if review and remediation add less than **5% of baseline minutes**, at perfect persistence. At 90% persistence it is already negative *before* any review time is counted.

## 4. Net cost change, and break-even persistence

Net cost change vs the human baseline (`p = 1.00`, `i = 0`, `a = 0.05`; negative is cheaper):

| gross saving s | rho = 0.00 | rho = 0.05 | rho = 0.10 | rho = 0.20 |
|---:|---:|---:|---:|---:|
| 0.10 | −5.0% | +0.0% | +5.0% | +15.0% |
| 0.20 | −15.0% | −10.0% | −5.0% | +5.0% |
| 0.30 | −25.0% | −20.0% | −15.0% | −5.0% |
| 0.40 | −35.0% | −30.0% | −25.0% | −15.0% |

Break-even persistence `p` (`i = 0`, `a = 0.05`) — below this, the effect is negative:

| gross saving s | rho = 0.00 | rho = 0.05 | rho = 0.10 | rho = 0.20 |
|---:|---:|---:|---:|---:|
| 0.10 | 0.950 | 1.000 | 1.050 | 1.150 |
| 0.20 | 0.850 | 0.900 | 0.950 | 1.050 |
| 0.30 | 0.750 | 0.800 | 0.850 | 0.950 |
| 0.40 | 0.650 | 0.700 | 0.750 | 0.850 |

The last row is the useful one: **a 20% saving with a 10% review burden needs 95% persistence to break even**, and persistence is rarely measured at all — which is the gap `03` §12A and §12C already identify, now stated as a number.

## 5. Effects already in the ledger, read through the identity

No new studies are introduced. Both anchors below are already carried in `03`'s source list. The table gives the review share at which each reported effect is exactly erased.

| Anchor (`03` source list) | Reported | Enters as s | rho_breakeven at p = 1.00 | at p = 0.95 | at p = 0.90 |
|---|---|---:|---:|---:|---:|
| Brynjolfsson / Li / Raymond, *Generative AI at Work* | productivity **+14%** across 5,179 support agents | **0.123** (converted) | **0.073** | 0.023 | **−0.027** |
| METR, experienced open-source developers | completion time **+19%** | **−0.190** | −0.240 | −0.290 | −0.340 |

**Reading the first row.** The most-cited positive estimate in this report's own ledger survives only if review and remediation add **less than 7.3% of baseline handle time** at perfect persistence — and it is **already negative at 90% persistence**, before any review time is counted. The study reports neither quantity at the outcome level, which is precisely why `03` §12C refuses to splice its aggregate onto task-level telemetry. The same aggregate also carries explicitly heterogeneous effects, so it is not applicable to any single workflow class; this row is an illustration of the identity, not a verdict on the study.

**Reading the second row.** The negative control is negative before any review or persistence term is added. That is what a genuine negative control looks like when run through the identity.

## 6. What this does and does not say

**It does not say AI workflows are unprofitable.** It says the profitability condition is a conjunction of four quantities, and that published effects typically report only one of them.

**It does not establish any workflow's economics.** No output here is a measurement.

**It does say something checkable:** any claimed effect can be paired with the break-even value of the quantities it omits. A claim that reports a time saving and no review burden, no persistence rate, and no integration cost is not a weaker version of a complete claim — it is **unfalsifiable as stated**, and the identity supplies the number that would falsify it.

**It inverts the burden of proof in a specific way.** The usual demand is "show me a study with a bigger effect." The identity replaces it with: "name the review burden and the persistence rate, and the effect size can stay as small as you like."

## 7. Falsification conditions

1. **A same-`workflow_id` Level-3 dataset reports `rho`, `p`, and `i` jointly** — the surface becomes an observation for that workflow and the break-even framing is superseded by measurement.
2. **Persistence is shown to be ~1.0** across workflow classes with negligible review burden — then the identity collapses to `s > a + i`, and effects are as large as reported.
3. **Review and remediation are shown to substitute for execution one-for-one** (rho ≈ s) — then no workflow with a reported saving is cost-improving at any effect size, which would be a strong and testable claim.
4. **Integration cost is shown to be negligible per attempt** (`i ≈ 0`) — the second surface collapses onto the first.

## 8. Boundary rules

- **Dimensions only.** Every input and output is a ratio. Reusing any number here as a measurement of a real process is a category error.
- **No aggregation across workflows.** `s`, `rho`, `p`, `i`, and `a` are workflow-class specific (`03` §2). Averaging them across a firm is exactly the splice `03` §12C.2 forbids.
- **No universal threshold.** `03` §17.8 states that no universal ROI threshold is defined; none is defined here either. The output is a condition, not a pass/fail bar.
- **Persistence means verified *and* persistent.** An open persistence window is `not yet observed` (`03` §17.6), never a success. Treating censored windows as successes is the specific bias this identity prices.
- **No factual, vendor, or scenario claim.** Nothing here can switch a scenario (`10` §2), create an evidence grade, confirm S4, or enter the frozen chapters.
- **D-grade labeling is mandatory** under `04-research-transparency`'s hierarchy wherever any output is reused.

## 9. Integration

1. Re-run `scripts/recompute_vswo_breakeven.py` when the input grids change, and update the tables rather than appending narrative.
2. **Proposed extension (not yet applied):** `03` §17.8's minimum publishable output could add the three break-even values as a reporting requirement, so that any Level-3 study states the conditions under which its own effect would be erased. That is a `03` upgrade and therefore requires the §17.9 gate — it is not applied here, and `03` remains v0.7.
3. **Cross-layer note (not yet applied):** the `15` coverage surface and this break-even surface are separate necessary conditions on the same chain — capital must be covered by cash, and workflow cost must be covered by effect. Neither may be multiplied into the other or into a composite index.

## Sources

No new external source is introduced. Both anchors are already carried by `03`.

- Brynjolfsson, E.; Li, D.; Raymond, L., *Generative AI at Work*, NBER Working Paper 31161 — carried in `03` Sources: https://www.nber.org/papers/w31161
- METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* — carried in `03` Level-3 candidate-audit sources: https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf
- Metric and closure definitions — [`03` §2](03-verified-workflow-economics.md), §3, §17.4, §17.5, §17.6, §17.8, §17.9
- Evidence hierarchy and report-side calculation labeling — [Research Transparency](../publication/04-research-transparency.md)
