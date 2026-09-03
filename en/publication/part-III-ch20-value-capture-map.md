# Part III · Chapter 20: Value Capture and Risk Bearing Across the AI Infrastructure Stack

## 1. Value capture and risk bearing are different maps

A single dollar of AI-infrastructure spending can appear as hyperscaler CapEx, system-vendor revenue, foundry revenue, memory revenue, packaging revenue, and data-center / power investment at different points in the chain. Those are accounting views of the same capital flow, not independent dollars.

The correct analytical problem is therefore not "how large is the total profit pool?" It is:

> **Which layer captures economic rent, which layer carries asset risk, and how does that balance change when scarcity, switching cost, utilization, or financing conditions move?**

This chapter maps value capture and risk bearing separately to avoid both double counting and simplistic winner/loser rankings.

## 2. Six variables determine economic rent

At minimum, the economics of a layer depend on:

1. **Scarcity:** how quickly supply can expand;
2. **Switching cost:** engineering / organizational cost of moving to an alternative;
3. **Capital intensity:** fixed capital required to sustain growth;
4. **Duration:** whether revenue, asset lives, and contract periods align;
5. **Distribution / workflow control:** whether the layer controls customers, data, and real business entry points.
6. **Financing / risk-transfer capacity:** whether the layer can reduce project financing friction, improve revenue visibility, and transfer residual-value / duration risk to capital willing to hold it.

High revenue share does not by itself imply the highest value capture, and gross margins cannot be compared across fundamentally different business models without context.

## 2A. Operating value capture and capital-market valuation run on different clocks

A company can capture strong operating economics without receiving the highest valuation multiple, and it can receive a high market valuation before those economics are fully realized.

The report therefore separates:

- **operating value capture:** revenue, gross / operating profit, free cash flow, unit economics, and cash conversion;
- **market position:** scarcity, switching cost, distribution, supply access, and bargaining power;
- **capital-market valuation:** market capitalization, equity multiple, debt pricing, and financing flexibility.

These layers interact but are not interchangeable.

A stronger market position can support higher margins and cash flow. Stronger cash flow can then improve financing capacity. A higher market valuation can lower the effective cost of equity, increase acquisition currency, support employee compensation, and expand the option set for prepayments or strategic investments.

But:

> **market cap ≠ cash flow ≠ economic rent ≠ physical resource control**

The feedback becomes strategically important only when valuation can be converted into executable financing capacity and the underlying operating economics remain credible.

This is the bridge between the value-capture map in this chapter and the **five-lens risk-adjusted-return framework** in Chapter 23.

---

## 3. System platforms monetize coordination and switching cost

NVIDIA is currently the clearest system-platform example.

FY27 Q2:

- Revenue **US$96.221B**;
- Data Center revenue **US$89.0B**;
- GAAP gross margin **75.0%**;
- GAAP operating income **US$63.734B**.[^1]

The value in this layer does not come from the accelerator die alone.

It comes from integrating compute, HBM, interconnect, software/runtime, rack architecture, and deployment tooling.

A system platform can:

- organize multiple external scarce inputs into one purchasing unit;
- create switching costs through software, fabric, and deployment;
- use strong cash generation to support next-generation supply commitments;
- coordinate roadmaps so customers can upgrade across generations with lower friction.

A system platform, however, still does not own every physical input.

Foundry, HBM, advanced packaging, and power remain external boundaries.

## 4. Foundry / packaging can control quantity without owning the highest margin

TSMC's 2025 gross margin was **59.9%**, while HPC represented **58%** of annual revenue.[^2]

The company-corrected 2025 wording was **advanced packaging slightly over 10% of revenue**,[^3] and in 2Q26 management said packaging tightness was limiting customer growth.[^4]

This shows that manufacturing value has expanded from transistor scaling into system integration.

The economic model of foundry / packaging is nevertheless different from an asset-light system platform:

> **manufacturing service + yield + utilization + CapEx execution**

A manufacturing layer can be a physical bottleneck without owning the highest margin in the whole chain.

> **bottleneck location ≠ profit location**

## 5. Memory captures scarcity rent but remains cyclical

SK hynix reported FY25:

- Revenue **KRW97.1467T**;
- Operating profit **KRW47.2063T**;
- Operating margin **49%**;
- HBM revenue more than doubled year over year.[^5]

Micron first-party evidence also shows that at the same node and same number of bits, HBM3E requires roughly **3× the wafer supply of DDR5**.[^6]

HBM value capture therefore reflects a combination of bandwidth value, manufacturing-input density, stacking / qualification complexity, and short-run scarcity.

Memory, however, remains cyclical.

If HBM capacity expands ahead of demand, generation mismatch grows, or demand slows, profit can retrace quickly.

Memory is therefore better understood as a **high-barrier manufacturing scarcity cycle** than as permanent platform rent.

## 6. Hyperscalers combine distribution power with duration risk

As documented in [Chapter 12](part-II-ch12-hyperscaler-system-stack.md), the major hyperscalers combine cloud distribution, captive / customer workloads, custom-silicon programs, and data-center scale.

For value-capture analysis, this gives them the ability to internalize part of system-platform economics without requiring this chapter to duplicate each product-level source.

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

## 7. Supply commitments connect platform cash flow to manufacturing capacity

NVIDIA's disclosed **forward supply / capacity commitment family** increased across three reporting dates:[^7]

- **US$95.2B** on 2026-01-25;
- **US$119B** on 2026-04-26;
- **US$279B** on 2026-07-26.

The FY26 Form 10-K supports the January figure; the FY27 Q2 Form 10-Q supports the April / July sequence and states that the latest commitments are primarily related to memory and manufacturing facilities needed for data-center infrastructure systems. The underlying mix and duration are not identical across reporting dates, so this is a forward-reservation indicator rather than a perfectly homogeneous time series.

The figure can therefore be used as a **financial proxy for future resource-locking intensity**.

But the filing does not disclose a supplier-level split, so it cannot be rewritten as a specific amount "already received" by TSMC, SK hynix, Micron, or any other individual supplier.

This is an important dynamic of value capture:

> high seller cash flow can be converted earlier into next-generation wafer, memory, packaging, and component commitments.

## 7A. Financing coordination is becoming a system capability

Two August 2026 disclosures show system-platform coordination extending from supply commitments into infrastructure finance:

- NVIDIA and Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs, and KKR announced compute-financing platforms targeting **more than US$500B of third-party capital mobilization over time**; the arrangements remain subject to final agreements.[^9]
- In PORTS-Pike, NVIDIA is providing credit support for land + power + shell and investing **US$1.5B** in SB Energy; OpenAI is the customer and SB Energy will build / own / operate the data center.[^10]

A leading system platform can therefore create value not only by organizing technology and supply, but by matching:

> **long-duration workloads + LPS / compute assets + long-duration capital**

This can reduce financing friction and accelerate Time-to-Capacity.

But the same mechanism changes who bears risk.

When a seller also provides equity, credit support, or infrastructure-financing coordination, some customer-concentration, duration, and residual-value risk can move back toward the platform.

Therefore:

> **financing coordination can strengthen platform advantage, but only when analyzed together with risk transfer and workload monetization.**

The full financing and clearing mechanisms are developed in Chapters 23 and 24.

## 8. Powered land captures Time-to-Power scarcity

At approximately **120 kW of rack power consumption for an NVIDIA DGX GB rack-scale system**,[^8] data centers require stronger grid interconnection, substations, transformers, cooling, and firm generation.

Assets with powered land, existing interconnection, and executable permitting paths can capture meaningful **Time-to-Power** value.

This layer has a distinctive profile:

- slow to replicate;
- geographically fixed;
- long permitting cycles;
- contracts that often outlive a compute generation.

Power can therefore be a scarce layer, but its economics must be evaluated together with utilization and contract duration.

A long-duration PPA can be a hedge or moat in high-demand scenarios and a long-duration obligation in S4.

## 9. Model / application value depends on workflow economics

Model companies and AI applications own model capability, APIs, user distribution, and workflow entry points.

They also face open-source competition, inference/retrieval/tool costs, cloud bargaining, and rapid price compression.

Traditional SaaS margins cannot simply be transferred onto AI applications.

The correct framework is **AI Software Unit Economics**:

> Revenue or productivity value − inference − retrieval/storage − tools/APIs − human review − AI-specific cloud cost

A defensible application layer needs to convert model capability into proprietary workflows, data, distribution, retention, and measurable business outcomes.

## 10. End systems absorb residual-capacity and quantity-assurance pressure

Smartphones, PCs, game consoles, automotive, industrial systems, robotics, and selected high-reliability electronics remain important end systems and strategic platforms.

Their primary burden is not being “replaced by AI.” It is the reprioritization of shared or adjacent upstream resources.

For end systems, the relevant exposure is **residual capacity and supply assurance**, and the physical channels differ:

- smartphones / PCs are more directly exposed to selected leading-edge logic, DRAM/LPDDR/NAND, consumer GPUs, and selected packaging;
- game consoles are exposed through custom SoC/APU, GDDR/DRAM, NAND/SSD, and long-generation hardware economics, with memory procurement able to transmit into promotion, unit volume, and hardware margin;
- automotive / industrial systems are more exposed to mature memory, MCU/analog, power, qualification, and long-life supply;
- robotics connects industrial electronics with edge/cloud AI;
- defense / aerospace / space electronics are more constrained by trusted, qualified, low-volume, long-life, RF/power, rad-hard, and special-process continuity than by direct competition for the same HBM pool.

The end-system layer should therefore not receive a single universal profit ranking, and not every downstream pressure should be attributed to AI.

The more useful variables are:

> **shared-resource exposure + buyer power + qualification rigidity + supply assurance + product-mix reallocation**

Chapter 3 defines the resource mechanism; Chapter 21 develops the observed pricing, configuration, longevity, and allocation transmission.

## 11. Custom silicon redistributes platform rent before upstream demand

A simplified traditional path is:

> cloud / model buyer → system platform → foundry / HBM / packaging → equipment/materials → power/data center

When hyperscalers deploy custom silicon, part of the flow can bypass NVIDIA:

> cloud → custom system → foundry / HBM / packaging

This changes the ownership of platform profit.

It does not necessarily reduce total demand for advanced logic, HBM, packaging, or power.

System-stack substitution is therefore both a profit-allocation variable and an upstream-resource competition variable.

## 12. Value capture is scenario-dependent

Value capture changes by scenario:

- **S1 Competitive Expansion:** custom stacks, open software, and supply expansion reduce platform rents and distribute value more broadly;
- **S2 Baseline Concentration:** system platforms and scarce manufacturing retain strong value capture while cloud investment remains high;
- **S3 Resource Hegemony:** logic/HBM/packaging/power concentrate further and scarce-layer owners plus the dominant system platform gain stronger bargaining power;
- **S4 Capital Hard Landing:** buyer utilization and commitments fall, long-duration infrastructure experiences duration/ROI stress first, and upstream profit later transmits downward.

This is more robust than assigning a permanent ranking to system platforms, HBM, foundries, clouds, and applications.

## 13. Current read

As of August 2026, the strongest evidence of durable value capture in AI infrastructure is concentrated mainly in three categories:

1. **system platforms that coordinate multiple scarce layers and create switching costs;**
2. **scarce physical layers with low short-run supply elasticity and high entry barriers, including HBM, leading-edge manufacturing, advanced packaging, and powered infrastructure;**
3. **financing / coordination layers that can match long-duration workloads, LPS / compute assets, and long-duration capital.**

The third category must be analyzed together with risk transfer. If a platform provides equity or credit support, it may gain more infrastructure influence while also reabsorbing part of customer, duration, or residual-value risk.

Whether applications develop a durable profit pool still depends on workflow economics and distribution.

The right question is therefore not "How much money is being spent on AI in total?"

It is:

> **How much repeatable cash flow remains at each layer, how much non-substitutability is created, and how much long-duration risk remains on the balance sheet?**

## 14. What would change the view

The current value-capture map should be reweighted if:

- system portability improves materially and switching costs fall;
- HBM / packaging / power scarcity premiums disappear on a sustained basis;
- financing coordination fails to lower capital cost or improve utilization;
- supplier-assisted financing begins generating material credit or impairment losses;
- application-layer workflow economics improve enough to create more durable profit pools;
- upstream manufacturing develops a genuine qualified second source.

Value capture is not a permanent ranking. It is the dynamic result of scarcity, switching cost, capital intensity, duration, distribution, and risk transfer.

## References

[^1]: NVIDIA, “NVIDIA Announces Financial Results for Second Quarter Fiscal 2027,” https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^2]: TSMC, 2025 Annual Report, gross margin and platform mix, https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^3]: TSMC, 4Q25 Earnings Conference Transcript, advanced packaging slightly over 10% of 2025 revenue, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
[^4]: TSMC, 2Q26 Earnings Conference Transcript, packaging tightness limiting customer growth, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/547d1696765e05ce3adb81c108ce1c8c1682b80c/TSMC%202Q26%20Transcript.pdf
[^5]: SK hynix, FY25 Financial Results, https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
[^6]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^7]: NVIDIA Corporation, FY26 Form 10-K, US$95.2B manufacturing / supply / capacity commitments as of 2026-01-25, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm ; FY27 Q2 Form 10-Q, US$119B last quarter and US$279B as of 2026-07-26, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^8]: NVIDIA, DGX GB Rack Scale Systems User Guide, rack power consumption approximately 120 kW, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
[^9]: NVIDIA, 2026-08-10, AI compute infrastructure financing platforms and >US$500B third-party-capital mobilization target, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Partners-With-Apollo-BlackRock-Blackstone-Brookfield-Goldman-Sachs-and-KKR-to-Establish-AI-Compute-Infrastructure-Financing-Platforms-to-Mobilize-Over-500-Billion-of-Third-Party-Capital/default.aspx
[^10]: NVIDIA, 2026-08-17, PORTS-Pike / SB Energy / OpenAI, LPS credit support, US$1.5B SB Energy investment, and initial 4.25 IT-GW design capacity, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx
