# Volume 37: AI Infrastructure Bubble Detection and Market-Clearing Framework

Chinese source edition: [vol-37.md](../vol-37.md)

> Retrieval and revision cutoff: **2026-08-28**. This volume does not define a bubble by market capitalization or headline CapEx. It looks for a synchronized deterioration in utilization, realized cash flow, market clearing, and forward commitments.

## 1. Large CapEx is not, by itself, evidence of a bubble

AI infrastructure investment is already extremely large, but investment scale alone does not prove that the system is in a bubble.

A bubble becomes economically meaningful when:

> **asset prices, construction scale, and future cash-flow expectations remain persistently detached from realized utilization and achievable returns.**

This volume therefore does not use one valuation multiple, one stock-price move, or one aggregate CapEx figure as the test.

The relevant question is whether the assets being built can generate enough useful workload and cash flow over their economic lives.

## 2. Four classes of market-clearing signals

This report uses four signal groups.

### 2.1 Accounting

Watch for:

- impairment;
- inventory write-downs;
- accelerated depreciation;
- asset disposals.

These indicate that companies are beginning to recognize, on their own books, that future cash flows may be lower than previously expected.

Accounting pressure alone is not a bubble burst. It becomes more informative when it appears together with weaker utilization and weaker forward orders.

### 2.2 Utilization / Revenue

Watch for:

- compute utilization;
- revenue per deployed system;
- enterprise AI revenue;
- workflow monetization.

If utilization remains high and workloads generate cash, high CapEx can be rational.

If utilization stays weak while depreciation and operating costs rise, capital pressure becomes progressively harder to absorb.

### 2.3 Market Clearing

Watch for:

- second-hand GPU or rack prices;
- cloud-instance discounts;
- delivery lead times;
- HBM pricing and availability;
- advanced-packaging availability.

Market prices and delivery conditions can move before annual financial statements do.

A meaningful shift from quota allocation and long lead times toward readily available supply, discounts, and liquid resale markets would be a stronger clearing signal than a stock-price correction by itself.

### 2.4 Forward Commitments

Watch for:

- hyperscaler CapEx guidance;
- NVIDIA supply commitments;
- long-duration compute contracts;
- power commitments.

Forward commitments show whether the next investment cycle is still being funded.

NVIDIA's manufacturing, supply, and capacity commitments rose from **US$119B** as of 2026-04-26 to **US$279B** as of 2026-07-26. The FY27 Q2 10-Q says the latest commitments are primarily tied to memory and manufacturing facilities. They are not proof of permanent scarcity, but they are evidence that the next round of supply was still being reserved at that point. Source: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm .

## 3. What qualifies as a Capital Hard Landing

This report defines **S4 Capital Hard Landing** as a state in which several classes of evidence deteriorate together:

1. utilization falls;
2. AI-related revenue or workflow economics disappoint;
3. hardware residual value declines;
4. CapEx guidance is reduced;
5. supply commitments slow, are rescheduled, or are cancelled;
6. impairments and write-downs increase.

Only a combination of signals at this level is strong enough to move the industry from “high-intensity expansion with rising ROI pressure” into “capital clearing.”

A large drawdown in technology equities is not sufficient. Neither is one weak quarter at one supplier.

## 4. Why sellers and buyers can diverge for a long time

NVIDIA is primarily a system seller.

Hyperscalers are large asset buyers.

When demand weakens, the sequence can be:

**buyer reduces next-generation orders → seller revenue growth slows → manufacturing utilization weakens upstream.**

That means seller margins can remain high for a period even while buyer ROI has already started to deteriorate.

The reverse is also possible: a supplier can experience an inventory or regulatory charge while the underlying demand system remains strong.

That is why the bubble question cannot be answered from seller gross margin alone.

## 5. Inventory shocks and structural collapse are different events

NVIDIA's FY26 H20-related charges affected full-year profitability.

FY26 Q4 GAAP gross margin was already **75.0%**, FY27 Q1 was 74.9%, and FY27 Q2 **held at 75.0%**, with revenue of **$96.221B**, Data Center revenue of **$89.0B**, and GAAP operating income of **$63.734B**.

The implication is narrow but important:

> **H20-related charges/releases and other one-time or policy-related items can damage a quarter or fiscal year without proving that system economics have structurally collapsed. “Regulatory shock” is an analytical label, not NVIDIA's wording.**

Structural deterioration requires a more persistent combination of:

- weaker volume;
- weaker pricing;
- weaker commitments;
- weaker utilization.

## 6. Algorithmic efficiency is a core variable in the bubble model

If the compute required to deliver the same capability falls rapidly while workload volume does not rise enough, then previously ordered infrastructure can become excessive.

That can lead to:

- lower system prices;
- lower utilization;
- weaker residual values;
- order cuts.

But if lower cost unlocks much more demand, efficiency can extend the capital cycle rather than end it.

The directional relationship is:

```text
Net Infrastructure Demand
= Efficiency Effect × Demand Elasticity
```

Efficiency is therefore not automatically bearish or bullish for infrastructure. The result depends on how strongly usage responds.

## 7. A model-layer price war can arrive before infrastructure clearing

Model APIs and open-source competition can push down:

- token prices;
- subscription prices;
- model-layer margins.

But lower model prices do not by themselves prove that GPU infrastructure is in oversupply.

Infrastructure clearing still depends on:

- total token and workload volume;
- enterprise adoption;
- utilization;
- workflow revenue;
- the speed at which lower unit cost expands demand.

The correct analytical unit is **AI Software Unit Economics**, not a fixed inherited SaaS-margin assumption.

A model-layer price war can therefore coexist with continued infrastructure expansion for some time.

## 8. The second-hand market is an important leading indicator

When new hardware generations replace older ones quickly, **economic depreciation** can run ahead of **accounting depreciation**.

Useful indicators include:

- used accelerator prices;
- lease rates;
- resale liquidity;
- old-generation cloud discounts.

A liquid market in discounted training systems would indicate that the industry has begun actively clearing prior compute investment.

This is different from an accounting impairment that appears only after management formally resets expectations.

## 9. Power and other long-duration assets clear more slowly

Data-center shells, substations, grid connections, and PPAs usually have much longer lives than accelerators.

A hard landing can therefore propagate in stages:

**hardware orders  
→ system residual value  
→ server utilization  
→ data-center leases  
→ power and project economics**

This matters because the capital cycle can take years to clear even if technology demand changes quickly.

A GPU can be repriced in months. A substation or twenty-year power contract cannot.

## 10. How the four formal scenarios differ

### S1 — Competitive Expansion

CapEx remains high, supply expands, custom systems mature, competition increases, and ROI remains healthy.

### S2 — Baseline Concentration

CapEx remains high, scarce-layer suppliers and major system platforms retain strong value capture, and utilization stays adequate.

### S3 — Resource Hegemony

Resource reservation becomes more concentrated across advanced logic, HBM, packaging, software, and power. Entry barriers rise further.

### S4 — Capital Hard Landing

Utilization, pricing, forward commitments, and new investment weaken together. Impairments and asset clearing become visible across several layers.

These are conditional states, not fixed-probability forecasts.

## 11. Current judgment

As of **August 2026**, the public evidence is more consistent with:

> **high-intensity capital expansion + rising ROI pressure**

than with a confirmed AI-infrastructure bubble collapse.

The fact base still includes:

- NVIDIA FY27 Q2 revenue of **$96.221B**;
- Data Center revenue of **$89.0B**;
- GAAP gross margin of **75.0%**;
- FY27 Q2 manufacturing, supply, and capacity commitments of **US$279B**;
- continuing HBM and advanced-packaging constraints;
- large hyperscaler infrastructure programs.

S4 remains a serious scenario because the asset base and depreciation burden are rising quickly.

For S4 to become the dominant interpretation, the report would need to see **CapEx, utilization, market-clearing prices, and forward commitments weaken together**.

The central danger is not simply that AI is attracting too much money.

It is:

> **that the stock of infrastructure keeps rising while the volume of economically productive workload fails to rise with it.**


## Key public sources for this volume

- NVIDIA FY26 official results / 10-K — H20-related charges; FY26 Q4 GAAP gross margin 75.0%: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
- NVIDIA FY27 Q1 10-Q — Q1 GAAP gross margin 74.9%: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm
- NVIDIA FY27 Q2 official results — Q2 GAAP gross margin 75.0%: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
