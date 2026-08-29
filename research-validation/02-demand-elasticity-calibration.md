# P0-2 · AI Demand Elasticity Empirical Calibration v0.1

> **Status:** Research-side validation; not part of the frozen formal report.  
> **Goal:** build empirical anchors for the elasticity mechanism used in Chapters 14 and 24 without turning one scenario coefficient into a universal structural parameter.

## 1. First correction: ε*=0.737 is geometry, not evidence

The current D-grade sensitivity model uses:

```text
Unit Resource Intensity ratio = 0.6
Effective Price ratio         = 0.5

Infrastructure Demand
= 0.6 × 0.5^(-ε)
```

The break-even condition is:

```text
1 = 0.6 × 0.5^(-ε*)

ε*
= ln(1 / 0.6) / ln(2)
≈ 0.73697
```

Therefore **ε≈0.737 is only the mathematical break-even under the assumed 40% reduction in unit resource intensity and 50% reduction in effective price**.

It is not:
- an OpenAI / Anthropic / Google / DeepSeek observed elasticity;
- enterprise workflow elasticity;
- token-market structural elasticity;
- a long-run Jevons coefficient.

The existing 0.5 / 1.0 / 1.2 / 1.5 values remain useful **D-grade sensitivity points**, not empirical estimates.

---

## 2. Strongest current empirical anchor: short-run API own-price elasticity just above one

Demirer, Fradkin, Tadelis & Peng, NBER Working Paper 34608 (2025), use API-usage data from **OpenRouter and Microsoft Azure**.

Their published abstract reports:

> preliminary short-run price elasticities just above one

The same paper documents:
- rapid LLM price declines;
- substantial price heterogeneity within intelligence tiers;
- open-source models roughly 90% cheaper than comparable closed-source models at similar measured intelligence;
- strong horizontal and vertical differentiation;
- different demand for intelligence across applications.

### What this does support

There is now a credible external empirical anchor that **short-run model/API own-price elasticity can be around unit elastic or somewhat above it** in the observed market.

### What this does not support

It does **not** identify:
- total AI-workflow elasticity;
- enterprise outcome elasticity;
- total token-market elasticity net of substitution;
- infrastructure-demand elasticity;
- a 2026–2036 long-run coefficient.

A model/API can gain usage because users substitute away from another model while total market compute barely changes.

---

## 3. Why a second large dataset appears to tell a very different story

OpenRouter + a16z’s **100T-token** empirical study maps effective model cost against total model usage.

Its cross-sectional trendline is nearly flat; the study states that a **10% lower price corresponds to only ~0.5–0.7% higher usage** in that cross-section.

Mechanically this resembles a cross-sectional slope around **0.05–0.07**, far below the NBER short-run price-elasticity estimate.

This is **not evidence that one study must be wrong**.

The estimands and identification are different.

The OpenRouter cross-section mixes:
- model capability;
- reliability;
- provider;
- task mix;
- distribution;
- caching;
- age of model;
- model-market fit;
- open vs. closed source;
- willingness to pay for premium outcomes.

A premium model can be simultaneously more expensive **and** more used because it serves higher-value tasks.

Therefore:

> **cross-sectional cost–usage correlation must not be relabeled as causal price elasticity.**

This becomes a hard research rule for Phase II.

---

## 4. Elasticity must be decomposed into layers

### E1 — Model/API own-price elasticity

Question:

> If the effective price of the same or closely substitutable model/API falls 1%, how much does that model/API’s quantity change?

This is closest to the current NBER estimate.

It contains provider/model substitution and therefore does not answer total-market demand by itself.

### E2 — Workload-category resource elasticity

Question:

> If the resource cost of coding / support / research / creative / agentic workloads falls 1%, how much does total resource consumption in that workload category change?

This begins to net out model switching.

### E3 — Verified-workflow elasticity

Question:

> If cost per verified business outcome falls 1%, how many more verified workflows are run?

This is the demand elasticity most closely aligned with the report’s core demand-side thesis.

Required denominator:
- completed and accepted business outcomes,

not:
- API calls,
- raw tokens,
- generated drafts,
- agent attempts.

### E4 — Infrastructure-demand elasticity

At the physical layer:

```text
Total Infrastructure Demand
=
Verified Workflow Volume
× Attempts per Workflow
× Resource Intensity per Attempt
```

E4 is affected by:
- E3;
- retry depth;
- agent loop length;
- context growth;
- routing;
- model mix;
- hardware efficiency;
- software efficiency.

Therefore:

> **API price elasticity ≠ workflow elasticity ≠ infrastructure-demand elasticity.**

---

## 5. Implication for the current D-grade sensitivity grid

Using the report’s existing hypothetical ratios:

```text
resource-intensity ratio = 0.6
effective-price ratio    = 0.5
```

the mathematical sensitivity remains:

| ε | Demand ratio = 0.6 × 0.5^-ε | Change |
|---:|---:|---:|
| 0.5 | 0.849× | -15.1% |
| 0.737 | ≈1.000× | ≈0% |
| 1.0 | 1.200× | +20.0% |
| 1.2 | 1.378× | +37.8% |
| 1.5 | 1.697× | +69.7% |

If a future empirical estimate **with the same estimand as this model** were reliably above 0.737, then under this exact hypothetical efficiency/price combination, total demand would rise.

But the NBER short-run API elasticity is **not yet the same estimand**, so it must not be dropped into this table as “the correct ε.”

---

## 6. Event-study eligibility rules

Phase II will not estimate elasticity from a price cut unless the event passes the following gate.

### Eligible or near-eligible

Prefer:
- same model identity;
- same capability;
- same context window;
- same quality tier;
- same throughput/rate limit;
- a price change with a measurable pre/post quantity panel;
- no simultaneous major distribution launch.

### Contaminated

Do **not** treat as clean elasticity identification when price change coincides with:
- a new model generation;
- major benchmark/capability gain;
- context-window expansion;
- material speed change;
- rate-limit change;
- new product integration;
- major marketing/distribution change.

### Why this matters

A “3× cheaper and 5× more usage” launch does not imply ε>1 if the new model is also faster, better, newly distributed and given higher limits.

---

## 7. Empirical hierarchy

### Tier A — causal / quasi-causal

- panel with within-model price variation;
- natural experiment;
- randomized pricing;
- fixed-effects model-day/provider-day design;
- credible instrument or discontinuity.

### Tier B — controlled panel

- price and quantity panel with model/task/time controls;
- substitution explicitly modeled;
- confidence intervals reported.

### Tier C — descriptive

- aggregate tokens;
- cross-sectional price vs. usage;
- launch-to-launch comparisons;
- company claims of “usage exploded after price cuts.”

Tier C is useful for market description but must never anchor structural ε.

---

## 8. Current calibration status

| Parameter | Current status | Evidence level |
|---|---|---|
| ε* = 0.73697 break-even | mathematically identified for current D-grade scenario | D / geometry |
| E1 API short-run own-price elasticity | external evidence: just above 1 | empirical external anchor |
| E2 workload-category elasticity | not identified | open |
| E3 verified-workflow elasticity | not identified | open / P0-3 dependent |
| E4 infrastructure-demand elasticity | not identified | open |

The most important result of v0.1 is therefore **not a new coefficient**.

It is a corrected parameter map:

> The report previously had one ε symbol carrying several economic meanings. Phase II separates those meanings so future evidence can update the right layer instead of creating false precision.

---

## 9. P0-2 v0.2 worklist

1. Inspect the NBER paper’s estimation specification, sample construction and uncertainty range;
2. build a model-day / provider-day **price-event catalog**;
3. reject events contaminated by model-generation/capability changes;
4. search for repeated same-model price variation, including time-of-day or provider-level price differences where quantity is observable;
5. estimate E1 first;
6. do not attempt E3 until P0-3 defines “verified workflow outcome” operationally.

## Sources

- Demirer, M.; Fradkin, A.; Tadelis, N.; Peng, S., **The Emerging Market for Intelligence: Pricing, Supply, and Demand for LLMs**, NBER Working Paper 34608, Dec. 2025: https://www.nber.org/papers/w34608
- Aubakirova, M. et al., **State of AI: An Empirical 100 Trillion Token Study with OpenRouter**, OpenRouter / a16z, Dec. 2025: https://openrouter.ai/state-of-ai/
- OpenRouter empirical data program: https://openrouter.ai/data
