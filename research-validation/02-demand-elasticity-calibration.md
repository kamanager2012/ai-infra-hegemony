# P0-2 · AI Demand Elasticity Empirical Calibration v0.5

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

## 9. NBER identification audit

The working paper's preferred OpenRouter specification is materially stronger than the abstract alone suggests.

At the provider-model-day level, the paper estimates approximately:

```text
log(Q_imt)
=
β1 log(Price_imt)
+ β2 log(Throughput_imt)
+ β3 log(Latency_imt)
+ β4 log(Context_imt)
+ Date×Model FE
+ Provider×Model FE
+ error
```

where:

- (Q_{imt}) = daily total tokens for provider (i), model (m), date (t);
- Price = prompt-token price;
- Throughput = tokens/second;
- Latency = time-to-first-token;
- Context = maximum context window.

The preferred specification uses **32,539 provider-model-day observations** and identifies price sensitivity from variation **within the same model**, including:

1. provider entry / exit for the same model;
2. price changes by existing providers.

Because closed-source models generally lack comparable within-model provider-price variation, this estimation sample is centered on **open-source models**.

The reported progression is informative:

| Specification | Price coefficient |
|---|---:|
| date FE, limited quality controls | about **-0.55** |
| + model FE | about **-1.08** |
| + provider×model FE and date×model FE | about **-1.11** |

The preferred estimate is therefore approximately:

> **E1 provider-model short-run own-price elasticity ≈ -1.11**

### 9.1 Why -1.11 is not the report's universal ε

This estimate is much better identified than a cross-sectional price/usage slope, but four boundaries remain.

1. **Provider substitution is included.** A cheaper provider can gain tokens from another provider serving the *same model* without increasing model-level or market-level compute by the same amount.
2. **OpenRouter routing is endogenous to price and quality.** Users can pin providers, but OpenRouter can also route requests using price and other provider characteristics. The paper controls for throughput, latency, context and fixed effects, but routing still complicates a pure end-user demand interpretation.
3. **The estimation sample is mainly open-source models.** External validity to proprietary flagship APIs is not automatic.
4. **It is short-run.** New workflows, organizational adoption and budget reallocation can take months or years.

Therefore the correct identity is:

> **-1.11 = a strong external anchor for E1 provider-model short-run elasticity, not E2/E3/E4 and not a 2026–2036 long-run Jevons parameter.**

---

## 10. 2026 GPT-5.6 discount program: a new event-study candidate

OpenRouter published a useful post-cutoff natural-experiment-like event on **2026-08-25**.

### 10.1 Event design

The three GPT-5.6 models launched on July 9, 2026.

OpenRouter reports:

- **Pre:** Jul 8–Jul 26;
- **Program:** Jul 27–Aug 14;
- **Post:** Aug 15–Aug 20.

Terra and Luna received large discounts beginning Jul 27.

On Jul 30, OpenAI also reduced list prices:
- Luna list price: **-80%**;
- Terra list price: **-20%**;

on top of OpenRouter's 50% discount, making effective discounts from Jul 30 roughly:
- Luna: **90%**;
- Terra: **60%**.

Sol remained at list price through Aug 16 and therefore acts as an approximate within-family control before receiving its own 50% discount on Aug 17.

### 10.2 Observed quantity response

OpenRouter reports:

| Model | Discount state | Program token volume vs. pre |
|---|---|---:|
| Terra | discounted | **5.6×** |
| Luna | discounted | **13.8×** |
| Sol | not discounted through Aug 16 | **1.11×** |

Terra + Luna combined token share rose from **0.7% to 7.8%** of OpenRouter tokens.

OpenRouter further reports that roughly three-quarters of the share gain came from competitors outside the OpenAI family, while some came from other OpenAI models.

About **32%** of customers who tried Terra/Luna during the program had some usage in the short post-program window.

### 10.3 Why this is stronger than the 100T cross-section

This event holds model identity largely fixed.

It therefore avoids the worst problem in:

> cheaper model A vs. expensive model B

cross-sectional comparisons.

The untreated Sol path also provides a useful contemporaneous control before Aug 17.

### 10.4 Why it still cannot yield one clean structural ε

Do **not** calculate:

> elasticity = log(5.6) / log(price change)

or the equivalent for Luna and label it causal.

The program contains several contaminations:

- Terra/Luna list prices changed again on Jul 30, so the treatment price is not constant;
- models had launched only shortly before the experiment;
- OpenRouter routing can react to price;
- competitor displacement is substantial, so own-model growth is not equal to market expansion;
- the post-program window in the published analysis is only six days;
- Sol itself becomes treated on Aug 17.

Therefore the event is classified:

> **Tier B event-study candidate — highly informative for price response and substitution, insufficient for a single structural E1/E4 coefficient without daily panel re-estimation.**

---

## 11. Price-event catalog v0.1

| Event / dataset | Same model? | Quantity panel? | Control / FE? | Main contamination | Status |
|---|---|---|---|---|---|
| NBER OpenRouter provider variation, 2025 | Yes | Yes | provider×model + date×model FE | routing / provider substitution | **Best current E1 anchor** |
| GPT-5.6 Terra/Luna discount, Jul–Aug 2026 | Yes | Yes | Sol approximate control | mid-program price reset, routing, substitution | **Tier B candidate** |
| GPT-5.6 Sol 50% discount from Aug 17, 2026 | Yes | Yes | short pre-period / family comparison | very short published post-window | **Tier B provisional** |
| OpenRouter 100T cost-vs-usage cross-section | No | aggregate/cross-sectional | No causal control | quality/task/provider segmentation | **Tier C descriptive only** |
| New-model launch price comparisons | Usually no | sometimes | weak | capability + context + distribution change | **Reject for structural ε** |

---

## 12. Two additional boundary results

### 12.1 Multi-homing does not imply persistent multi-model demand

The NBER market study adds an important interpretation constraint.

It finds that:

- more than half of firms rely on a **single model** in a given month;
- the share of firms using multiple models rose from roughly **25% to 50%** between mid-2023 and mid-2025;
- among multi-homers, most still allocate **more than 90%** of usage to one model.

This means observed cross-model switching can represent:

> **experimentation / evaluation**

rather than:

> **stable workload substitution across several production models.**

For elasticity work, this matters because a price cut can produce a large provider/model share response even when the firm's underlying production workflow volume barely changes.

So future event studies should separate:

1. **provider substitution**;
2. **model substitution**;
3. **new workflow creation**;
4. **higher intensity on existing workflows**.

Only (3) and part of (4) are direct candidates for E3/E4 expansion.

### 12.2 Do not confuse demand elasticity with task-substitution elasticity

Anthropic's January 2026 Economic Index uses a **task elasticity of substitution** in its macro-productivity aggregation.

Illustrative values such as:

- σ = 0.5;
- σ = 1;
- σ = 1.5

change how easily gains on AI-accelerated tasks can substitute for bottleneck tasks.

That parameter answers:

> **Can work reallocate across tasks when some tasks become much faster?**

It does **not** answer:

> **How much more AI is demanded when inference price falls?**

This is a separate economic object from E1–E4 price/demand elasticities.

The report must therefore reserve notation carefully:

- **ε** → price / demand elasticity;
- **σ_task** → elasticity of substitution across tasks.

This avoids a serious symbol collision: both can be “greater than one” while describing entirely different mechanisms.

Anthropic also shows why this distinction matters empirically: adjusting task-level speedups for success rates materially reduces implied aggregate productivity gains, and complementary bottleneck tasks can reduce them further.

That supports a broader Phase II rule:

> **price response, task substitution, task success and workflow creation must remain separate layers.**

---

## 13. Updated calibration map

| Parameter | Current status | Evidence level |
|---|---|---|
| ε* = 0.73697 break-even | mathematically identified for current D-grade scenario | D / geometry |
| E1 provider-model short-run elasticity | preferred external estimate about **-1.11** | empirical / quasi-experimental anchor |
| E1 proprietary flagship event response | GPT-5.6 discounts show very large token response, coefficient not yet identified | Tier B event candidate |
| E2 workload-category elasticity | not identified | open |
| E3 verified-workflow elasticity | operational denominator now defined in P0-3, coefficient not identified | open |
| E4 infrastructure-demand elasticity | not identified | open |

The evidence now supports a stronger statement than v0.1:

> **Short-run API/provider demand can be approximately unit elastic or slightly elastic in well-identified settings, and very large same-model discounts can trigger large token reallocations. But neither result establishes that total AI infrastructure demand has elasticity above one, because provider/model substitution and workflow creation are different mechanisms.**

---

## 13A. GPT-5.6 event-study data-access audit

The OpenRouter August 25 post exposed enough methodology to define the event cleanly. A later OpenRouter data-product update materially changes the data-access conclusion: OpenRouter now documents a machine-readable daily rankings dataset API that can provide model-day token totals back to 2025-01-01.

Publicly visible:
- Pre window: **Jul 8–Jul 26**;
- Program: **Jul 27–Aug 14**;
- Post: **Aug 15–Aug 20**;
- Jul 30 additional OpenAI list-price cuts changed effective treatment intensity;
- Sol is usable as a control only through **Aug 16**;
- Terra/Luna daily token usage rose **5.6× / 13.8×** versus pre-period daily averages;
- Terra/Luna token share rose **0.7% → 7.8%**;
- competitor labs lost **5.3 share points** and other OpenAI models lost **1.9 points**;
- roughly **32%** of program users had some post-program usage;
- post-period daily Terra/Luna token volume averaged **1.38×** the program-period level;
- Sol averaged **79.1B tokens/day** during the Terra/Luna program versus **71.2B/day** pre-period.

The original event page itself did not surface a downloadable daily raw-price / raw-token panel. That page-level limitation is no longer equivalent to platform-level data unavailability because OpenRouter now documents a separate daily rankings dataset API.

Therefore Phase II should not:
- digitize chart pixels into fake daily observations;
- compute a single `log(volume ratio) / log(price ratio)` coefficient;
- treat Jul 27–Aug 14 as one constant treatment price;
- use Sol as an untreated control after Aug 16;
- interpret the 5.6× / 13.8× headline as net market expansion.

The current identification status is:

> **Tier B event-study candidate with a now-documented reproducible daily token-data path; causal estimation still requires coverage verification, price-path reconstruction, and event-window controls.**

### What can still be measured without fake precision

Even without raw daily data, the public aggregates allow a decomposition of the observed share gain:

```text
Terra/Luna share gain = +7.1 points
  ├─ competitors: -5.3 points
  └─ other OpenAI: -1.9 points
```

Rounding explains the 0.1-point difference.

This implies that roughly three quarters of the observed share gain came from **outside the OpenAI family**.

That is evidence of substantial **substitution / displacement**.

It is not yet a measure of:
- net new workflows;
- total-market token elasticity;
- E3 verified-workflow elasticity;
- E4 infrastructure elasticity.

### v0.4 rule

Until a machine-readable daily series becomes public or a reproducible data export is available:

> **reopen the GPT-5.6 event for reproducible model-day panel construction, but do not estimate a structural coefficient until the coverage and treatment-path checks below pass.**

Do not manufacture an elasticity point estimate from the charts.

---

## 13B. OpenRouter Rankings Daily API — data-access status reopened

OpenRouter now documents a public-data API endpoint:

```text
GET /api/v1/datasets/rankings-daily
```

with:
- `start_date` / `end_date` UTC query parameters;
- coverage beginning **2025-01-01**;
- up to the top **50 public models per day** by token volume;
- one aggregated `other` row per day for all models outside the top 50;
- `total_tokens = prompt_tokens + completion_tokens`;
- stable `model_permaslug` identifiers;
- a dataset `as_of` timestamp / version;
- authentication via a valid OpenRouter API key.

OpenRouter states that the rankings dataset is reusable with attribution under **CC BY 4.0**.

This is a material upgrade from the previous audit.

### 13B.1 What the API can support

If Terra, Luna, and Sol each appear in the top-50 rows for the necessary dates, Phase II can construct:

```text
date
model_permaslug
total_tokens
treatment_state
effective_price_state
event_time
```

for the Jul–Aug 2026 discount episode.

That is enough to move from headline pre/post ratios toward a reproducible model-day event panel.

### 13B.2 Top-50 censoring rule

The API does **not** provide every model separately.

Models outside the daily top 50 are pooled into `other`.

Therefore:

> **A target model that drops outside the top 50 on a date becomes interval-censored / unidentified at model level for that date.**

Do not:
- allocate part of `other` back to the model;
- interpolate a hidden model value;
- treat missing top-50 membership as zero usage.

Coverage audit must be the first step.

For every target model:

```text
Coverage Rate
=
days with model-specific row
/
required event-window days
```

If coverage is incomplete, the event design must either:
- shorten the window to common observed dates;
- use a different aggregation;
- or remain descriptive.

### 13B.3 Token-comparability rule

OpenRouter explicitly warns that token counts come from each upstream provider's tokenizer.

Therefore:
- within-model time-series comparisons are much cleaner;
- cross-model raw-token level comparisons are not perfectly cardinal;
- model-share calculations across providers remain platform traffic shares, not standardized compute units.

This matters especially for:

```text
Terra vs Luna vs Sol
```

if their tokenizer / reasoning-token accounting differs.

Prefer:
- within-model percentage change;
- model-specific event coefficients;
- share-of-platform traffic with caveats.

Do not interpret one model's token as physically equivalent to another model's token.

### 13B.4 Public-traffic boundary

OpenRouter rankings measure:
- traffic routed through OpenRouter;
- public-ranking-eligible activity.

They do **not** measure:
- provider-direct API traffic;
- all enterprise private traffic;
- the full global model market.

OpenRouter's rankings documentation states that private/hidden requests are excluded before public aggregation.

Therefore:

> **the estimand is OpenRouter-visible adoption / substitution, not global demand elasticity.**

### 13B.5 Price-path reconstruction remains separate

The daily token API solves the quantity side.

It does not by itself provide a historical daily transaction-price panel.

For the GPT-5.6 event, treatment reconstruction should use the documented event schedule:

```text
Pre
→ Jul-27 program discount begins
→ Jul-30 Terra/Luna list-price reset changes effective treatment intensity
→ Aug-15 program ends
→ Aug-17 Sol receives its own discount
```

So treatment is piecewise, not one constant percentage.

No regression should code the whole program as one binary treatment without sensitivity checks.

### 13B.6 Minimum reproducible event-study protocol

Before estimating anything:

1. resolve exact Terra/Luna/Sol permanent slugs;
2. query the complete common window;
3. audit top-50 coverage by model/day;
4. preserve `as_of` and dataset version;
5. encode the documented piecewise price/treatment path;
6. limit Sol as untreated control to dates before its own Aug-17 treatment;
7. report raw token levels and within-model indexed values;
8. test pre-trends;
9. separate:
   - own-price response;
   - within-OpenAI substitution;
   - competitor displacement;
   - total OpenRouter traffic change;
10. do not map the resulting coefficient directly into E3/E4 verified-workflow or infrastructure elasticity.

### 13B.7 Revised status

The previous conclusion:

> "no reproducible daily panel exists"

is now obsolete.

The correct v0.5 execution status is:

> **data path = closed**  
> **actual Terra / Luna / Sol extraction = authentication blocked**  
> **coefficient = not estimated**

The Rankings Daily endpoint and required fields are documented, but requests require a valid OpenRouter API key. Phase II will not bypass authentication, infer hidden model-day values from charts, or manufacture a coefficient from aggregate pre/post ratios.

This is a meaningful data-path closure, not an empirical estimate.

---

## 15. P0-2 v0.6 worklist

1. obtain/reconstruct daily provider-model price and token panels for eligible events;
2. use the documented Rankings Daily API to build the Terra/Luna/Sol common-window panel; audit top-50 censoring before any estimation;
3. separate **share displacement** from **net market token expansion**;
4. test whether elasticity differs by workload category where usage labels are observable;
5. report confidence intervals / robustness specifications;
6. keep E3 separate until real VSWO datasets are populated;
7. do not replace the D-grade sensitivity grid with -1.11 unless the estimand is explicitly E1.

## Sources

- Demirer, M.; Fradkin, A.; Tadelis, N.; Peng, S., **The Emerging Market for Intelligence: Pricing, Supply, and Demand for LLMs**, NBER Working Paper 34608, Dec. 2025 (revised 2026): https://www.nber.org/papers/w34608
- Demirer, M.; Fradkin, A.; Tadelis, N., **The Emerging Market for Intelligence: How Firms Buy and Sell AI**, *Journal of Economic Perspectives* 40(3), 2026: https://pubs.aeaweb.org/doi/10.1257/jep.20261506
- Aubakirova, M. et al., **State of AI: An Empirical 100 Trillion Token Study with OpenRouter**, OpenRouter / a16z, Dec. 2025: https://openrouter.ai/state-of-ai/
- OpenRouter empirical data program: https://openrouter.ai/data
- Demirer et al., author-hosted working-paper version, empirical strategy / provider-model-day specification: https://andreyfradkin.com/assets/LLM_Demand_12_12_2025.pdf
- OpenRouter, **GPT 5.6 Discounts & Jevons Paradox**, 2026-08-25: https://openrouter.ai/blog/insights/gpt-5-6-discounts-jevons-paradox/
- Anthropic, **Economic Index: Economic primitives**, 2026-01-15: https://www.anthropic.com/research/anthropic-economic-index-january-2026-report


- OpenRouter, “Daily token totals for top 50 models” API documentation: https://openrouter.ai/docs/api/api-reference/datasets/get-rankings-daily
- OpenRouter Data — datasets API / research data program: https://openrouter.ai/data
- OpenRouter Rankings methodology and CC BY 4.0 reuse notice: https://openrouter.ai/rankings
- OpenRouter Activity Export documentation — account/org CSV export is separate from the public rankings dataset: https://openrouter.ai/docs/cookbook/administration/activity-export
