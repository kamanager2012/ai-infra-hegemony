# Volume 21: AI-Infrastructure Capital Flows and Profit-Pool Structure

Chinese source edition: [vol-21.md](../vol-21.md)

> **Publication role:** [Volume 14](vol-14.en.md) owns the Value Capture Map; this volume is the capital-flow companion focused on double counting, capital intensity, and upstream commitments. The integrated Chinese publication chapter is [Part III · Chapter 20](../publication/part-III-ch20-value-capture-map.md).

> Retrieval and revision cutoff: **2026-08-28**. Capital-flow analysis must avoid counting the same dollar multiple times as hyperscaler CapEx, vendor revenue, foundry revenue, memory revenue, and infrastructure investment.

## 1. The same dollar cannot be counted three times

AI-infrastructure spending appears on several corporate statements:

- hyperscaler CapEx;
- system-vendor revenue;
- foundry revenue;
- memory-vendor revenue;
- power and data-center investment.

Adding these figures together can double- or triple-count the same underlying capital flow.

This volume therefore does not estimate one synthetic “global AI profit pool.”

It asks:

> **Where does revenue become cost, where does cost become upstream revenue, and where does profit remain at each layer?**

## 2. Four major capital nodes

### 2.1 Hyperscalers

Microsoft, Amazon, Alphabet, and Meta report buyer-side capital expenditure.

Depending on the company and accounting scope, that capital can include:

- servers;
- networking;
- custom silicon;
- third-party accelerators;
- data centers;
- power infrastructure;
- land;
- fulfillment and other infrastructure.

Cloud CapEx therefore cannot be treated as “money paid to NVIDIA.”

It finances a broader asset system.

### 2.2 System platform

NVIDIA Data Center revenue is seller-side revenue.

Current anchors include:

| Indicator | Value |
|---|---:|
| FY26 Data Center revenue | **US$193.737B** |
| FY26 non-GAAP free cash flow (NVIDIA definition) | **US$96.575B** |
| FY27 Q2 Data Center revenue | **US$89.0B** |
| FY27 Q2 GAAP operating income | **US$63.734B** |

These figures show that a system platform can retain a very large share of value while remaining relatively asset-light compared with foundries and data-center owners.

### 2.3 Foundry and packaging

TSMC earns revenue through:

- wafer manufacturing;
- advanced packaging;
- testing.

For 2025:

- gross margin: **59.9%**;
- HPC platform: **58% of revenue**;
- 2025 advanced packaging: slightly above **10%** under the company-corrected 4Q25 wording; the 2024 >8% disclosure used the distinct label “advanced packaging and testing.”

TSMC carries heavy manufacturing CapEx and yield risk.

Its economics are structurally different from those of an asset-light system platform.

### 2.4 Memory

SK hynix, Samsung, and Micron capture AI demand through HBM and server memory.

SK hynix FY25 reported:

- revenue: **KRW 97.1467T**;
- operating profit: **KRW 47.2063T**;
- operating margin: **49%**;
- net income: **KRW 42.9479T**;
- HBM revenue: **more than doubled year over year**.

Public source: https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/

Memory has therefore become a major profit pool within the AI-infrastructure chain.

## 3. Why platform margin and manufacturing margin should not be compared mechanically

NVIDIA's model is closer to:

> **system definition + software + integration + supply orchestration**

TSMC's model is closer to:

> **manufacturing service + CapEx + yield + utilization**

Memory vendors sit between them:

> **product cycle + manufacturing scarcity + technology transition**

A single gross-margin comparison therefore cannot answer which layer is strategically stronger.

The report also tracks:

- capital intensity;
- switching cost;
- supply scarcity;
- customer concentration;
- ability to reinvest profit into the next scarce increment.

## 4. Supply commitments connect financial power to physical allocation

NVIDIA's manufacturing, supply, and capacity commitments were:

- **US$95.2B** as of 2026-01-25;
- **US$119B** as of 2026-04-26;
- **US$279B** as of 2026-07-26.

The FY27 Q2 10-Q says the latest commitments are primarily tied to memory and manufacturing facilities; they still cannot be decomposed into supplier-level amounts. Source: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm .

These commitments show that future cash demand is being translated into:

- inventory;
- wafer capacity;
- HBM;
- advanced packaging;
- other components.

But the filing does not provide a supplier-level split.

The commitments therefore cannot be restated as:

- a specific amount paid to TSMC;
- a specific amount paid to SK hynix;
- a specific amount paid to Micron.

Their correct role is as a **financial proxy for forward resource reservation**.

## 5. Why hyperscaler cash is different from platform cash

Hyperscalers also generate very large cash flows.

But their capital requirements are more dispersed across:

- land;
- buildings;
- power;
- networking;
- cooling;
- silicon;
- third-party systems;
- operations.

The strategic difference is therefore not simply “who has more cash?”

It is:

> **Whose cash can be deployed most directly into the next scarce layer?**

A platform seller can often reserve upstream resources without carrying the full data-center asset base.

## 6. HBM extends the capital flow beyond the accelerator

TrendForce estimates that HBM + RDIMM represent approximately **51% of 2026 DRAM bits**.

Micron's FY24 Q3 **industrywide / same-node / same-bits** disclosure puts HBM3E at roughly **3× the wafer supply of DDR5**, showing higher manufacturing-input intensity without turning that ratio into a Micron-specific constant.

AI-infrastructure capital therefore increasingly flows into:

- HBM;
- RDIMM;
- advanced packaging;
- memory-fab expansion.

This helps explain why consumer and conventional DRAM can feel AI-driven pressure even when the end product does not use a frontier accelerator.

## 7. Power is becoming another capital-absorption layer

At roughly 120 kW-class rack density, large data-center projects require early investment in:

- substations;
- transformers;
- grid interconnection;
- cooling;
- firm-power contracts.

Capital flow is therefore expanding from semiconductors into energy and infrastructure.

Future value capture can increasingly sit in:

- powered land;
- firm MW;
- grid access;
- long-duration energy assets.

That does not mean power owners automatically earn platform-like margins.

It means the value chain is becoming physically broader.

## 8. AI software requires its own profit-pool framework

Application-layer economics increasingly include:

- inference;
- retrieval;
- storage;
- tool/API costs;
- human review.

AI software therefore should be analyzed through **AI Software Unit Economics**, not through a fixed inherited SaaS-margin assumption.

Useful indicators include:

- gross margin after inference;
- cost per successful workflow;
- retention;
- revenue per task;
- human-review cost.

Fast software revenue growth does not automatically imply a high-quality profit pool.

## 9. The correct way to read the capital chain

A simplified chain is:

> **Hyperscaler / model company  
> → system platform  
> → foundry / memory / packaging  
> → equipment / materials  
> → power / data-center infrastructure**

But the path is not always linear.

Cloud custom silicon can redirect part of the flow around NVIDIA:

> **cloud  
> → foundry / HBM / packaging**

System-stack competition can therefore change profit allocation without reducing upstream demand.

The same physical bottleneck can serve different platform winners.

## 10. Current judgment

The strongest AI-infrastructure profit pools today are concentrated around:

1. system platforms;
2. HBM;
3. leading-edge foundry and advanced packaging;
4. powered infrastructure.

Whether the application layer becomes an equally durable profit pool depends on unit economics and distribution.

The important question is not:

> “How much money is being spent on AI?”

It is:

> **How much profit does the same capital leave at each layer, how much long-duration lock-in does it create, and how much repeatable cash flow does the resulting asset generate?**

## Key public sources for this volume

- TrendForce — 2026E HBM + RDIMM = 51% of DRAM bit supply: https://www.trendforce.com/presscenter/news/20260825-13198.html
- Micron FY24 Q2 prepared remarks — HBM3E ≈ 3× DDR5 wafer supply: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf

- NVIDIA FY27 Q2 official results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- TSMC 2025 Annual Report: https://investor.tsmc.com/static/annualReports/2025/english/index.html
- TSMC 2025 20-F: https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm
- TSMC 2025 consolidated report (Customer A/B): https://www.sec.gov/Archives/edgar/data/1046179/000104617926000024/a2025q4consolidatedreport-.htm

- TSMC 4Q25 Transcript — 2025 advanced packaging slightly above 10%, company-corrected: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
- NVIDIA FY26 official results (FY26 Data Center revenue / NVIDIA-defined non-GAAP FCF): https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
