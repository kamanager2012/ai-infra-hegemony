# Phase II · Capital-to-Cash Bridge v0.1

> **Status:** Research-side validation layer; not part of the frozen 32-chapter formal report, and does not change the formal 2026-08-28 evidence cutoff.  
> **Purpose:** perform the one division the formal report deliberately refuses — required cash per GW-year versus contracted revenue per GW-year — using only anchors already graded elsewhere in this repository, so that the disagreement is computable by a third party rather than asserted by this report.  
> **Reproducible artifact:** `scripts/recompute_capital_to_cash.py` over `data/capital-to-cash-inputs.json`. Outputs are D-grade report-side calculations.  
> **Chinese translation (derived):** [15-capital-to-cash-bridge.zh.md](15-capital-to-cash-bridge.zh.md)

## 0. Ownership contract v0.1

This file owns:

- the **per-GW-year normalization** — cash per unit of deployed AI capacity — and its arithmetic;
- the conversion of observed financing terms (coupon, tenor, debt share, DSCR covenant) into a **required cash floor** per GW-year;
- the conversion of observed contract and plan disclosures into **contracted revenue per GW-year** and **capital per GW**;
- the coverage surface between them, and its falsification conditions.

It does **not** own: company capital state (`04B`), facility / borrower / support state (`04C`, `04D`), anchor-buyer commitment facts (`13`), workflow cost and verification units (`03`), scenario aggregation (`10`), financing taxonomy and anti-double-counting (`11`), demand-side variables (`14`), or live clearing adjudication (`01A`).

**Why a new owner rather than an existing layer.** The formal report's S4 condition is a comparison — capital formation against utilization and cash generation (Ch24 §9, Ch30 §5). `04C` records DSCR covenants and coupons as *facility state* but never converts them into a cash requirement per unit of capacity; `03` owns cost per **verified workflow**, a bottom-up micro unit with a different denominator; `04B` owns company-level headroom under four incompatible accounting definitions; `10` is forbidden from maintaining facts or creating them. The per-GW-year unit therefore has no owner, and the report's central question has no arithmetic. That is the gap this file fills.

## 1. The division the report refuses — and what the refusal costs

`10` §2 and the formal text forbid several conversions. Two of them are relevant here:

- announced / committed / design GW **→** energized GW (Ch07's power states, `10` §2 rule 4);
- contracted value and guarantee caps **→** "total demand" (`10` §6.1A).

The refusals are correct. But they leave the report unable to answer a question a reader will ask anyway:

> **Does the cash that is contractually coming in cover the cash that is contractually going out, per unit of capacity?**

Answering it does not require violating either refusal, because the DSCR covenant makes the **required** side observable from public filings. `04C` §11B.5 records Nebius's secured facility at a **1.15× DSCR covenant**, and the same panel records observed coupons from **~5.96%** (IREN Microsoft-linked) to **9.75%** (CoreWeave April-2026 notes). Those are market-observed terms, not assumptions.

## 2. The unit, and the two sides

Unit: **US$ per GW-year.**

**Required side — contractual cash floor.**

```text
Debt Service (annual)      = PMT(rate, tenor, debt_share x capital_per_GW)
Required Cash Floor        = DSCR_covenant x Debt Service
```

This is a **floor**, not a total return requirement. It excludes equity return, tax, and all operating cost. A project must clear it before any equity return exists.

**Observed side — contracted revenue floor.**

```text
Contracted Revenue per GW-year = (contract value floor / contract years) / GW actually served
```

This is a **floor** on value and a **ceiling** on GW. Both directions push the true revenue-per-GW-year up if the disclosure is a boundary rather than an actual.

**The comparison is a necessary condition, not a verdict.** It asks whether revenue alone covers contractual debt service. It deliberately ignores opex, tax, and equity return, so passing it is not evidence of viability and failing it is not evidence of failure — failing it means *something other than this contract at this GW spread* must carry the difference.

## 3. Inputs — every number is an existing graded anchor

No new numeric identities are created in this file. Each anchor below is already carried, with its source, in the formal chapters or the Phase II panels.

| Input | Value | Existing anchor | Grade as used here |
|---|---|---|---|
| Plan-level capital | **US$500B long-term plan** | OpenAI Stargate (Ch13, `外部研究对照索引` §9) | A for the announcement; **D** as a realized cost |
| Secured-capacity milestone | **>10 GW secured** (2026-04) | OpenAI disclosure (Ch13) | A for the disclosure; **D** as energized capacity |
| Credit-support cap per design GW | **US$24.71B/IT-GW** = US$105B cap ÷ 4.25 IT-GW design capacity | PORTS-Pike (Ch23, `04C` §11B.7A, `04D`) | A for both caps; **D** as a cost |
| Contracted revenue per GW-year | **US$2.00B** at the full 5 GW ceiling | Anthropic / AWS >US$100B over ten years, up to 5 GW (Ch13) | A for the disclosure; **D** as an economic quantity |
| Observed DSCR covenant | **1.15×** | Nebius secured facility (`04C` §11B.5) | A |
| Observed coupons | **5.96% / 8.00% / 9.75%** | IREN Microsoft-linked; mid-case; CoreWeave April-2026 notes (`04C` §11B.5) | A for the endpoints; the 8% mid-case is **D** |
| Debt share | **60%** | Illustration only — no facility discloses its full stack | **D** |
| IREN FY2026 AI cloud revenue | **US$128.8M** on a 0.3 GW 2026 *target* | IREN FY2026 filing (`04C` §11B.7A) | A for revenue; **D** as a denominator |
| Full-load energy per GW | **8.76 TWh/GW-year** | arithmetic on 1 GW × 8,760 h | geometry |

**Scope-conflation rule.** The first two rows are **not the same scope**: the US$500B is a *plan*, the >10 GW is a *secured-capacity milestone*, and nothing in the disclosures establishes that the plan's capital is the cost of the milestone's capacity. Dividing them would be the exact error this file exists to expose. The US$50B/GW cell at the top of the §4 grid is therefore a **plan-scale illustration**, not an observed capital cost — it is included so a reader can see the arithmetic at plan scale and may substitute any realized figure.

**Anti-mixing rule.** Plan capital, capped credit support, and revenue per year are three *different units*. They must never be added to, divided by, or netted against each other. `10` §6.1A's discipline applies unchanged.

## 4. Required cash floor per GW-year

Computed at 60% debt share and the 1.15× covenant:

| Financing regime | Rate | Tenor | $20B/GW | $30B/GW | $40B/GW | $50B/GW |
|---|---:|---:|---:|---:|---:|---:|
| IG-backed long | 6.00% | 10 yr | 1.87 | 2.81 | 3.75 | 4.69 |
| Mid-coupon | 8.00% | 7 yr | 2.65 | 3.98 | 5.30 | 6.63 |
| High-coupon project | 9.75% | 7 yr | 2.81 | 4.22 | 5.62 | 7.03 |

*US$B per GW-year.*

The **annuity convention is an approximation.** Project facilities typically use sculpted amortization; a level annuity is the reproducible stand-in, and it is stated rather than hidden.

For scale, the energy row: at US$65–85/MWh and 70–100% utilization, full-load electricity is **US$0.40–0.75B/GW-year**. Power is therefore *not* the binding item in this comparison — capital recovery is, by roughly an order of magnitude. That is a computable statement, not an opinion.

## 5. Coverage surface

Contracted revenue per GW-year = (US$100B floor / 10 years) / GW served:

| GW served | Revenue US$B/GW-yr | vs $30B/GW mid | vs $40B/GW mid | vs $50B/GW mid |
|---:|---:|---:|---:|---:|
| 1 | 10.00 | 2.52× | 1.89× | 1.51× |
| 2 | 5.00 | 1.26× | 0.94× | 0.75× |
| 3 | 3.33 | 0.84× | 0.63× | 0.50× |
| 5 (ceiling) | 2.00 | 0.50× | 0.38× | 0.30× |

*Coverage is computed from the unrounded required-cash values, so dividing a revenue cell above by §4's displayed 2-decimal cash cell can differ in the last digit: the 1-GW/$30B cell is 10.00 / 3.976 = 2.5202, while dividing by the displayed 3.98 gives 2.5126. The table carries the first, because a published ratio should be the ratio of the quantities rather than of their rounded renderings. Rounding required cash first is how this cell came to read 2.51× — a value no computation produced.*

**Breakeven capital per GW** — the capital cost at which the contracted floor exactly covers the required floor, spread over the full 5 GW ceiling:

| Regime | Breakeven capital per GW |
|---|---:|
| IG-backed long (6%, 10 yr) | **US$21.3B/GW** |
| Mid-coupon (8%, 7 yr) | **US$15.1B/GW** |
| High-coupon project (9.75%, 7 yr) | **US$14.2B/GW** |

### What this does and does not say

**It does not say the economics fail.** The surface is driven by two unknowns that the public evidence bounds rather than fixes:

1. **GW actually served by the contract.** The single largest lever: the same US$100B spans a 5× range in revenue per GW-year between 1 GW and 5 GW.
2. **Realized capital per GW.** No public disclosure in this repository gives a realized capital cost per GW. The US$50B/GW cell is a plan-scale illustration, and the US$24.71B/IT-GW is a **cap divided by a design figure** — two ceilings, not two actuals. Neither is a cost observation.

**It does say something falsifiable:** at the observed financing terms, and reading the announced GW as the capacity the anchor contract serves, contracted revenue does **not** cover the contractual debt-service floor unless realized capital per GW is materially below the plan-level anchor — or unless other tenants, equity, or non-debt capital carry the difference.

**The point of the artifact is the surface, not a verdict.** The report previously could only assert that denominators matter. Here the denominator *is* the answer: the disagreement between a bull and a bear case is now two dials a reader can set and defend.

## 6. The denominator demonstration — IREN

IREN's FY2026 AI cloud revenue of **US$128.8M** against its 2026 **target** of ~0.3 GW IT delivery gives **US$429.3M per target GW-year**. Held against the mid-coupon requirement at US$40B/GW (US$5.30B/GW-yr), that is **0.08×**.

That ratio is not an economic statement. It is a denominator error, and it is the cleanest available illustration of the report's core discipline:

| Delivery fraction of target | Revenue per *delivered* GW-year | Coverage at $40B/GW mid |
|---:|---:|---:|
| 100% | US$429.3M | 0.08× |
| 50% | US$858.7M | 0.16× |
| 25% | US$1,717.3M | 0.32× |

The delivery fraction is **not estimated here** — it is a dial, because FY2026 revenue was earned on whatever capacity was actually serving, and that number is not in the public row used. The lesson is structural: **a target-GW denominator and a delivered-GW denominator differ by the delivery fraction, and any per-GW claim that does not name its denominator is uninterpretable.**

## 7. Falsification conditions

This layer is weakened or overturned by any of the following, all observable:

1. **Realized capital per GW is disclosed** below the breakeven band for a named project — the coverage question then resolves positively for that project and the surface narrows.
2. **A named facility reports DSCR and capacity together**, converting the required side from covenant-plus-coupon into observed cash.
3. **Lease or contract value per energized GW-year is disclosed** for a facility that is actually delivering, removing the delivery-fraction dial.
4. **Coverage stays below 1.0× across multiple named facilities once energized**, with no offsetting equity or non-debt capital — this would move the capital-to-cash leg from a monitoring state to a clearing-relevant one.
5. **The annuity approximation is replaced by disclosed sculpted amortization** and the required floor moves materially — in either direction.

## 8. Boundary rules

- **Necessary, not sufficient.** The test ignores opex, tax, equity return, refresh capex, and residual value.
- **No facility inference.** Nothing here is a claim about any named project's actual capital cost, utilization, PPA price, or economics.
- **No scope conflation.** Plan capital, secured-capacity milestones, guarantee caps, design capacity, and energized capacity are five different scopes. A ratio between any two of them is a boundary of boundaries and must be labeled as such wherever it is reused.
- **No external scenario numbers.** No third-party forecast, unemployment rate, index level, or crisis year enters this file.
- **No S4 confirmation.** A coverage shortfall is a financing-and-monetization observation. S4 still requires multiple causal-independent families across actors and layers (Ch24 §9, Ch30 §5) and is adjudicated by `01A`.
- **No state inflation.** This layer cannot switch a scenario (`10` §2), cannot create an evidence grade, and cannot write into the frozen chapters.
- **D-grade labeling is mandatory.** Every computed output in §4–§6 is a report-side calculation under `04-research-transparency`'s evidence hierarchy and must carry that label wherever it is reused.

## 9. Integration

1. Re-run `scripts/recompute_capital_to_cash.py` whenever an input anchor updates in `04C`, `04D`, or `13`; update the tables rather than appending narrative.
2. **Proposed extension (not yet applied):** `10` §6D's Axis F sub-rows and Dashboard K's Layer 5 (monetization) could consume the **coverage ratio** as a derived state once at least one named facility discloses DSCR and energized capacity together. Until then, `10` is unchanged.
3. `01A` adjudication: if coverage arrives below 1.0× on energized, contract-backed facilities, record it as a financing-family contribution — never multiplied into a composite index, and never as a standalone S4 confirmation.

## Sources

All anchors are cited through their existing repository owners; this file introduces no new external source.

- OpenAI Stargate plan (US$500B / 10 GW) — Ch13; https://openai.com/index/announcing-the-stargate-project/
- Anthropic / AWS ten-year commitment (>US$100B / up to 5 GW) — Ch13; https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
- NVIDIA PORTS-Pike guarantee cap (US$105B / ~4.25 IT-GW) — Ch23, `04C` §11B.7A, `04D`; https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm
- CoreWeave April-2026 senior notes (9.75%) — `04C` §11B.5
- Nebius secured facility (SOFR + 2.50%, 1.15× DSCR covenant, Oct-2030) — `04C` §11B.5
- IREN Microsoft-linked GPU financing (~5.96%) and FY2026 AI cloud revenue — `04C` §11B.5, §11B.7A
- Evidence hierarchy and report-side calculation labeling — [Research Transparency](../publication/04-research-transparency.md)
