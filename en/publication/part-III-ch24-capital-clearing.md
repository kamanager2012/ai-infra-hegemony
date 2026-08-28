# Part III · Chapter 24: Bubble Identification, Capital Clearing, and S4

## 1. Large CapEx does not by itself prove a bubble

AI-infrastructure capital spending is extremely high, but investment size alone cannot prove a bubble.

The relevant question is whether asset buildout persistently outruns utilization, realizable cash flow, and residual value.

This report therefore does not use one CapEx total, one valuation multiple, or one technology-stock drawdown as evidence that the bubble has already burst.

S4 Capital Hard Landing requires synchronized deterioration across multiple industrial signals.

## 2. Four classes of clearing signals

### 2.1 Accounting

The slowest but hardest evidence comes from formal recognition:

- impairment;
- inventory write-down;
- accelerated depreciation;
- asset disposal.

These indicate that companies themselves have reduced expectations for future cash flow or residual value.

One-quarter policy or inventory effects cannot automatically be upgraded into structural collapse.

For example, H20-related charges affected NVIDIA FY26 results, but GAAP gross margin was **75.0% in FY26 Q4**, **74.9% in FY27 Q1**, and **75.0% in FY27 Q2**.[^1][^2][^3]

One-time charges and releases have to remain separate from long-run system economics.

### 2.2 Utilization / Revenue

The capital cycle ultimately has to be paid for by effective workloads.

The key variables are compute utilization, revenue per deployed system, enterprise AI revenue, and workflow monetization.

High utilization can support very large CapEx.

If a growing asset base remains persistently underutilized, depreciation pressure can arrive before sufficient revenue.

The dangerous condition is not "there are many machines."

It is:

> **the asset base keeps growing while cash-generating effective workload does not grow with it.**

### 2.3 Market Clearing

Markets often show easing before financial statements.

Relevant indicators include:

- used accelerator / system prices;
- lease rates;
- cloud-instance discounts;
- delivery lead times;
- HBM prices;
- advanced-packaging availability;
- resale liquidity.

If a new generation rapidly displaces an older one, economic depreciation can move faster than accounting depreciation.

Persistent resale discounts and shorter lead times are therefore more meaningful signs of de-stocking than a stock-market drawdown alone.

### 2.4 Forward Commitment

The next round of expansion depends on hyperscaler CapEx guidance, NVIDIA manufacturing/supply/capacity commitments, long-duration model-company compute contracts, and power commitments.

NVIDIA's public commitment path rose from **US$95.2B** on 2026-01-25 to **US$119B** on 2026-04-26 and **US$279B** on 2026-07-26.[^4]

The FY27 Q2 10-Q states that the latest commitments primarily relate to memory and manufacturing facilities required for data-center infrastructure systems.

The current trajectory looks more like continued forward resource reservation than broad cancellation.

## 3. Four-cloud CapEx has to remain company-specific and accounting-specific

There is no unified official "2026 AI hardware CapEx."

Current public scale includes:

**Table 24.1 — Public 2026 capital-spending metrics for the four major clouds**

| Company | Current 2026 metric | Identity |
|---|---:|---|
| Microsoft | calendar-2026 reported CapEx expectation ~US$175B | expectation; underlying investment expectation unchanged after lease-classification adjustment |
| Alphabet | US$195–205B | Q2 guidance |
| Meta | US$130–145B | Q2 guidance; includes finance-lease principal |
| Amazon | US$169.007B | TTM PPE net purchases actual through 2026-06-30 |

**Source:** Microsoft FY26 Q4 earnings materials, Alphabet 2026 Q2 SEC Exhibit 99.1, Meta 2026 Q2 SEC Exhibit 99.1, and Amazon 2026 Q2 Form 10-Q.[^5][^6][^7][^8]  
**Note:** Expectation, guidance, and TTM actuals use different time windows and accounting treatments and do not form a directly additive AI-hardware CapEx total.

The time windows and accounting categories differ.

They cannot be mechanically added into one AI-hardware CapEx number.

Historical scenario totals such as US$215B or US$670–750B remain stress-test artifacts unless the accounting denominator is made comparable.

## 4. Sellers and buyers operate on different capital clocks

NVIDIA is a system seller. Hyperscalers are asset buyers.

The seller can recognize revenue and profit at shipment, while buyers carry utilization and depreciation risk on servers, data centers, networking, power, and long-duration contracts for years afterward.

A downturn therefore often unfolds sequentially:

> **buyer ROI deteriorates first → next-generation orders / commitments slow → seller growth weakens later → manufacturing utilization transmits upstream**

Strong seller margin does not prove healthy buyer-side ROI.

Buyer-side ROI pressure also does not imply seller economics collapse in the same quarter.

## 5. Algorithmic efficiency can create overcapacity—or extend the cycle

If compute required for the same capability falls rapidly while workload volume does not rise, deployed capacity can become excessive. If lower cost stimulates many new workloads, efficiency can instead increase total infrastructure demand.

The report therefore replaces the non-computable shorthand “efficiency effect × demand elasticity” with two measurable factors:

```text
Infrastructure_Demand_t
= Unit_Resource_Intensity_t
× Workload_Volume_t
```

Relative to a baseline period 0:

```text
Infrastructure_Demand_t / Infrastructure_Demand_0
=
(Unit_Resource_Intensity_t / Unit_Resource_Intensity_0)
×
(Workload_Volume_t / Workload_Volume_0)
```

`Unit_Resource_Intensity` must be tied to a defined work unit, such as GPU-hours / verified workflow, HBM bytes / token, or kWh / completed job. `Workload_Volume` is the number of comparable workflows, tokens, or jobs completed over the same period.

If the analysis also needs to connect price changes to workload volume, a constant-elasticity approximation can be introduced separately:

```text
Workload_Volume_t / Workload_Volume_0
=
(Effective_Price_t / Effective_Price_0)^(-ε)
```

where ε is the demand elasticity for the **same comparable verified outcome**. Then:

```text
Infrastructure_Demand_t / Infrastructure_Demand_0
=
(Unit_Resource_Intensity_t / Unit_Resource_Intensity_0)
×
(Effective_Price_t / Effective_Price_0)^(-ε)
```

**Table 24.2 — D-grade sensitivity example for efficiency and demand elasticity**

Assume unit resource intensity falls 40% (`URI_t / URI_0 = 0.60`) and the effective price of the same verified workflow falls 50% (`P_t / P_0 = 0.50`):

| Demand elasticity ε | Workload volume factor | Infrastructure demand factor | Versus baseline |
|---:|---:|---:|---:|
| 0.5 | 1.414× | 0.849× | -15.1% |
| 1.0 | 2.000× | 1.200× | +20.0% |
| 1.2 | 2.297× | 1.378× | +37.8% |
| 1.5 | 2.828× | 1.697× | +69.7% |

**Source:** Report D-grade sensitivity model.  
**Note:** 0.60, 0.50, and ε are illustrative assumptions, not current industry actuals. The table shows only that the same efficiency gain can reduce or increase infrastructure demand depending on demand elasticity.

The same logic applies to model-price competition. Falling token/API prices prove a change in unit pricing; they do not by themselves prove that total token volume, workflow adoption, and infrastructure utilization are also declining.

## 6. Anchor Compute Buyers are now an additional leading indicator

OpenAI Stargate, Anthropic/AWS, and other long-duration capacity commitments raise model companies from ordinary tenants into infrastructure Anchor Buyers.

They can improve project-financing certainty and pull forward data-center, power, chip, and memory construction.

This also means the leading S4 indicators now include more than "hyperscalers cut CapEx."

They include:

- model-capacity commitments being reduced, delayed, or renegotiated;
- GW-scale project ramps materially missing schedule;
- low utilization on committed long-duration capacity;
- upstream prepayments and seller commitments slowing at the same time.

If those variables weaken alongside buyer utilization and market-clearing prices, the evidence for Capital Hard Landing strengthens materially.

## 7. Clearing order follows asset duration

Short-cycle assets clear first; long-cycle assets clear later.

A representative order is:

> **uninstalled hardware / inventory → system residual value → server utilization → data-center lease → long-duration power/project economics**

S4 can therefore last for years.

Power plants, substations, and data-center shells do not disappear like GPU inventory.

They can be repriced, sold, renegotiated, or become scarce again in the next concentration cycle.

## 8. What qualifies as S4 Capital Hard Landing

This report upgrades S4 from stress test to current main scenario only when all four classes deteriorate together:

1. **Accounting:** impairment / write-down / disposal rises materially;
2. **Utilization / Revenue:** utilization and effective AI revenue remain persistently weaker than asset expansion;
3. **Market Clearing:** resale prices, lease prices, lead times, HBM/packaging clearing all loosen;
4. **Forward Commitment:** CapEx guidance, seller commitments, Anchor Buyer contracts, and power commitments slow or cancel together.

A stock-price decline, lower model prices, one quarter of margin volatility, or one historical stress test is not sufficient on its own.

## 9. Current judgment

As of August 2026, public evidence is still closer to:

> **high-intensity capital expansion + rising ROI pressure**

than to a confirmed AI-infrastructure bubble collapse.

NVIDIA FY26 non-GAAP free cash flow remains **US$96.575B**,[^1] FY27 Q2 GAAP operating income **US$63.734B**,[^3] and supply/capacity commitments have risen to **US$279B**[^4] while hyperscalers continue to report very high infrastructure-spending plans.

This does not guarantee a soft landing.

It only means that declaring capital clearing the dominant reality still requires synchronized evidence across utilization, clearing prices, accounting losses, and forward commitments.

## References

[^1]: NVIDIA, FY26 official results, NVIDIA-defined non-GAAP free cash flow and FY26 Q4 margin, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
[^2]: NVIDIA Corporation, FY27 Q1 Form 10-Q, GAAP gross margin 74.9%, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm
[^3]: NVIDIA, FY27 Q2 official results, GAAP gross margin 75.0% and GAAP operating income US$63.734B, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^4]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^5]: Microsoft, FY26 Q4 earnings / conference call, https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast
[^6]: Alphabet, 2026 Q2 SEC Exhibit 99.1, https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
[^7]: Meta Platforms, 2026 Q2 SEC Exhibit 99.1, https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm
[^8]: Amazon.com, 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
