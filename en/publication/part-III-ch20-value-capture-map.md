# Part III · Chapter 20: Value Capture Map — Capital Flows, Profit Pools, and Risk Bearing

## 1. The same dollar cannot be counted repeatedly across the supply chain

The same AI-infrastructure spending can appear as:

- hyperscaler CapEx;
- system-vendor revenue;
- foundry revenue;
- memory-vendor revenue;
- packaging revenue;
- data-center / power investment.

These are not six independent dollars.

A buyer purchases a system and the seller recognizes revenue. The seller then buys foundry, memory, and component inputs. The cloud provider also builds data-center and power infrastructure.

Adding the headline numbers across layers creates serious double counting.

This chapter therefore analyzes **where value is captured** and **where risk is carried**, rather than manufacturing an unauditable global profit-pool total.

## 2. Value Capture depends on five dimensions

At minimum, the economics of a layer depend on:

1. **Scarcity:** how quickly supply can expand;
2. **Switching cost:** engineering / organizational cost of moving to an alternative;
3. **Capital intensity:** fixed capital required to sustain growth;
4. **Duration:** whether revenue, asset lives, and contract periods align;
5. **Distribution / workflow control:** whether the layer controls customers, data, and real business entry points.

High revenue share does not automatically mean highest value capture, and gross margins cannot be compared across fundamentally different business models without context.

## 3. System Platform: organizing multiple scarce layers into one high-value product

NVIDIA is currently the clearest system-platform example.

FY27 Q2:

- Revenue **US$96.221B**;
- Data Center revenue **US$89.0B**;
- GAAP gross margin **75.0%**;
- GAAP operating income **US$63.734B**.

The value in this layer is not only the accelerator die.

It comes from integrating compute, HBM, interconnect, software/runtime, rack architecture, and deployment tooling.

A system platform can:

- organize multiple external scarce inputs into one purchasing unit;
- create switching costs through software, fabric, and deployment;
- use strong cash generation to support next-generation supply commitments;
- coordinate roadmaps so customers can upgrade across generations with lower friction.

But a system platform still does not own every physical input.

Foundry, HBM, advanced packaging, and power remain external boundaries.

## 4. Foundry / Advanced Packaging: heavy manufacturing can become the quantity gate

TSMC's 2025 gross margin was **59.9%**, while HPC represented **58%** of annual revenue.

The company-corrected 2025 wording was **advanced packaging slightly over 10% of revenue**, and in 2Q26 management said packaging tightness was limiting customer growth.

This shows that manufacturing value has expanded from transistor scaling into system integration.

The economic model of foundry / packaging is nevertheless different from an asset-light system platform:

> **manufacturing service + yield + utilization + CapEx execution**

A manufacturing layer can be a physical bottleneck without owning the highest margin in the whole chain.

> **bottleneck location ≠ profit location**

## 5. HBM / Memory: manufacturing intensity and product cycles create scarcity profit

SK hynix reported FY25:

- Revenue **KRW97.1467T**;
- Operating profit **KRW47.2063T**;
- Operating margin **49%**;
- HBM revenue more than doubled year over year.

Micron first-party evidence also shows that at the same node and same number of bits, HBM3E requires roughly **3× the wafer supply of DDR5**.

HBM value capture therefore reflects a combination of bandwidth value, manufacturing-input density, stacking / qualification complexity, and short-run scarcity.

Memory, however, remains cyclical.

If HBM capacity expands ahead of demand, generation mismatch grows, or demand slows, profit can retrace quickly.

Memory is therefore better understood as a **high-barrier manufacturing scarcity cycle** than as permanent platform rent.

## 6. Hyperscalers: strong distribution paired with large asset risk

Microsoft, Amazon, Alphabet, and Meta combine cloud distribution, internal workloads, customer bases, custom silicon, and data-center scale.

That gives them the ability to internalize part of system-platform economics.

They also carry:

- servers / accelerators;
- networking;
- data-center shells;
- cooling;
- power / land;
- depreciation;
- utilization risk.

Hyperscalers should therefore not be classified simply as "winners" or "losers."

Their strongest assets are distribution + workload + capital.

Their greatest risk is duration mismatch when long-duration infrastructure is built before workflow revenue materializes.

## 7. Supply commitments are the funding bridge between the system platform and manufacturing

NVIDIA's manufacturing, supply, and capacity commitments rose from:

- **US$95.2B** on 2026-01-25;
- **US$119B** on 2026-04-26;
- **US$279B** on 2026-07-26.

The FY27 Q2 10-Q states that the latest commitments are primarily related to memory and manufacturing facilities needed for data-center infrastructure systems.

The figure can therefore be used as a **financial proxy for future resource-locking intensity**.

But the filing does not disclose a supplier-level split, so it cannot be rewritten as a specific amount "already received" by TSMC, SK hynix, Micron, or any other individual supplier.

This is an important dynamic of value capture:

> high seller cash flow can be converted earlier into next-generation wafer, memory, packaging, and component commitments.

## 8. Power / Powered Land: value comes from time scarcity, not electricity price alone

At roughly **120 kW-class rack density**, data centers require stronger grid interconnection, substations, transformers, cooling, and firm generation.

Assets with powered land, existing interconnection, and executable permitting paths can capture meaningful **Time-to-Power** value.

This layer has a distinctive profile:

- slow to replicate;
- geographically fixed;
- long permitting cycles;
- contracts that often outlive a compute generation.

Power can therefore be a scarce layer, but its economics have to be evaluated together with utilization and contract duration.

A long-duration PPA can be a hedge or moat in high-demand scenarios and a long-duration obligation in S4.

## 9. Model / Application: long-run profit depends on workflow, not the model alone

Model companies and AI applications own model capability, APIs, user distribution, and workflow entry points.

They also face open-source competition, inference/retrieval/tool costs, cloud bargaining, and rapid price compression.

Traditional SaaS margins cannot simply be transferred onto AI applications.

The correct framework is **AI Software Unit Economics**:

> Revenue or productivity value − inference − retrieval/storage − tools/APIs − human review − AI-specific cloud cost

A defensible application layer needs to convert model capability into proprietary workflows, data, distribution, retention, and measurable business outcomes.

## 10. Consumer Electronics: not "losing to AI," but carrying residual-capacity pressure

Smartphones, PCs, gaming, and general servers remain large markets.

Their primary burden is not "being replaced by AI" but the reallocation of shared upstream resources:

- advanced-logic allocation;
- DRAM residual supply;
- consumer-GPU availability;
- component pricing.

This layer is better described as a **residual-capacity pressure bearer**.

As AI/server demand absorbs high-value incremental resources, traditional end markets can experience slower upgrades, changed configurations, and higher costs.

## 11. Custom silicon redraws the flow of money without necessarily reducing upstream demand

A simplified traditional path is:

> cloud / model buyer → system platform → foundry / HBM / packaging → equipment/materials → power/data center

When hyperscalers deploy custom silicon, part of the flow can bypass NVIDIA:

> cloud → custom system → foundry / HBM / packaging

This changes the ownership of platform profit.

It does not necessarily reduce total demand for advanced logic, HBM, packaging, or power.

System-stack substitution is therefore both a profit-allocation variable and an upstream-resource competition variable.

## 12. Use a Scenario Map, not a permanent "winner ranking"

Value capture changes by scenario:

- **S1 Competitive Expansion:** custom stacks, open software, and supply expansion reduce platform rents and distribute value more broadly;
- **S2 Baseline Concentration:** system platforms and scarce manufacturing retain strong value capture while cloud investment remains high;
- **S3 Resource Hegemony:** logic/HBM/packaging/power concentrate further and scarce-layer owners plus the dominant system platform gain stronger bargaining power;
- **S4 Capital Hard Landing:** buyer utilization and commitments fall, long-duration infrastructure experiences duration/ROI stress first, and upstream profit later transmits downward.

This is more robust than assigning a permanent ranking to system platforms, HBM, foundries, clouds, and applications.

## 13. Current judgment

As of August 2026, high-quality value capture in AI infrastructure is concentrated mainly in two categories:

1. **system platforms that coordinate multiple scarce layers and create switching costs;**
2. **scarce physical layers with low short-run supply elasticity and high entry barriers, including HBM, leading-edge manufacturing, advanced packaging, and powered infrastructure.**

The largest asset risks remain more concentrated on buyers that have to build infrastructure ahead of demand.

Whether applications develop a durable profit pool depends on workflow economics and distribution.

The right question is therefore not "How much money is AI spending in total?"

It is:

> **How much repeatable cash flow remains at each layer, how much non-substitutability is created, and how much long-duration risk remains on the balance sheet?**

## Key public sources

- NVIDIA FY27 Q2 official results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- NVIDIA FY27 Q2 10-Q — US$279B manufacturing, supply, and capacity commitments: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
- TSMC 2025 Annual Report: https://investor.tsmc.com/static/annualReports/2025/english/index.html
- TSMC 4Q25 Transcript — 2025 advanced packaging slightly over 10%, company-corrected: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
- TSMC 2Q26 Earnings Conference Transcript — packaging tightness limits customer growth: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
- SK hynix FY25 official results: https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
- Micron FY24 Q2 Prepared Remarks — HBM3E ≈3× DDR5 wafer supply: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- NVIDIA DGX GB200 hardware guide — ~120 kW/rack: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
