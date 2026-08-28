---
title: "The Age of AI Infrastructure Hegemony"
subtitle: "Structural Reallocation of Compute, Semiconductors, Memory, Advanced Packaging, Power, and Capital"
author: "James (kamanager2012)"
date: "Research and revision cutoff: August 28, 2026"
lang: en-US
---


# Scope, Evidence Boundaries, Disclaimer, and Copyright

## Scope

This report is a long-form industry study of AI infrastructure, semiconductors, memory, advanced packaging, hyperscaler system stacks, power, capital, software economics, and structural industrial change.

The report separates:

- observed and verifiable facts (F — Fact);
- explicit forward assumptions (H — Hypothesis);
- causal transmission mechanisms (M — Mechanism);
- conditional future states (S — Scenario);
- observable reverse signals that would force judgments to change (X — Falsification).

The objective is not to produce one deterministic 2036 forecast. It is to build an industrial-analysis framework that can be updated as public evidence changes.

## Evidence boundary

The report relies primarily on:

- annual reports, 10-K / 20-F filings, quarterly results, and official investor materials;
- regulatory, court, and government documents;
- formal contracts and project disclosures;
- official product specifications and technical documentation;
- high-quality institutional research;
- report-side models and stress tests when explicitly labeled.

Institutional forecasts, sell-side estimates, and report-side calculations are not promoted into company facts.

## Disclaimer

This report is for industry research and information purposes only. It is not investment advice, a securities rating, legal advice, an audit opinion, or a recommendation to enter into any transaction. All forward-looking judgments are conditional and may change with technology, demand, capital, regulation, geopolitics, and supply.

## Copyright

Original report text is distributed under the repository LICENSE. Third-party material remains subject to the rights and licensing terms of its respective owners. The final publication edition should include only third-party material that is clearly permitted, properly cited, redrawn where appropriate, or otherwise cleared for use.

---

## Reading Navigation

- [Table of Contents](01-table-of-contents.md)
- [List of Tables](02-list-of-tables.md)
- [Abbreviations and Core Glossary](03-abbreviations-and-glossary.md)
- [Research Transparency, Limitations, and Correction Policy](04-research-transparency.md)
- [Competitive Set, Substitution Paths, and Counter-Evidence Matrix](05-competitive-evidence-matrix.md)
- [Executive Summary — Chapter 1](part-I-ch01-executive-summary.md)
- [Research Method and Evidence Architecture — Chapter 27](part-IV-ch27-research-method.md)
- [Core Evidence Ledger](../核心证据台账.en.md)
- [Core Source Index](../核心参考文献索引.en.md)


\newpage


# List of Tables

> Table numbering follows the chapter.number convention. Every formal table in the main text should include a title, Source, and where necessary a Note.

## Part I

- Table 1.1 — Four standard AI-infrastructure scenarios
- Table 2.1 — GB200 NVL72 rack-scale system structure
- Table 2.2 — NVIDIA seller-side economics and forward supply commitments
- Table 4.1 — TSMC 2025 capacity, technology, and platform-revenue structure
- Table 5.1 — GB200 NVL72 rack count and HBM3E scenario demand
- Table 6.1 — Residual sensitivity under incremental packaging-capacity capture
- Table 7.1 — Nominal scale and delivery state of three AI-power pathways
- Table 8.1 — NVL72 rack count and HBM/LPDDR scenario demand

## Part II

- Table 16.1 — Four differentiated competitive paths
- Table 17.1 — Global foundry revenue share, 1Q26 (TrendForce)
- Table 18.1 — How regulatory variables map into S1–S4

## Part III

- Table 19.1 — Public 2026 capital-spending metrics for the four major clouds
- Table 22.1 — Major cloud server / network-equipment useful-life disclosures
- Table 23.1 — AI-infrastructure asset classes and primary financing risks
- Table 24.1 — Public 2026 capital-spending metrics for the four major clouds
- Table 24.2 — D-grade sensitivity example for efficiency and demand elasticity

## Part IV

- Table 27.1 — Evidence-grade system used in this report
- Table 29.1 — NVIDIA seller economics and forward-reservation baseline
- Table 29.2 — Power project state machine
- Table 29.3 — Default evidence grade for report updates
- Table 29.4 — Observation frequency, persistence, and scenario triggers for core variables
- Table 30.1 — Core drivers, primary outcomes, and reverse signals for S1–S4
- Table 31.1 — Core structural variables used in the long-run strategic judgment
- Table 31.2 — Primary value sources and risks across AI-related asset classes


\newpage


# Abbreviations and Core Glossary

## Industry abbreviations

| Abbreviation / term | Meaning | Usage boundary in this report |
|---|---|---|
| AI | Artificial Intelligence | Generative / frontier AI only when context makes that scope explicit |
| HPC | High-Performance Computing | Includes AI/HPC workloads; not synonymous with AI |
| GPU | Graphics Processing Unit | Data-center and consumer layers remain distinct |
| CPU | Central Processing Unit | Not interchangeable with accelerators |
| ASIC | Application-Specific Integrated Circuit | Cloud custom accelerators are one important form |
| SoC | System on Chip | Common in smartphone, edge, and embedded systems |
| HBM | High Bandwidth Memory | Bit share, wafer input, and market share remain separate denominators |
| DRAM | Dynamic Random-Access Memory | HBM, DDR, LPDDR, and RDIMM remain product-level distinctions |
| DDR5 | Double Data Rate 5 SDRAM | One conventional-DRAM product class |
| RDIMM | Registered DIMM | Server memory; not equivalent to HBM |
| LPDDR | Low-Power DDR | Used mainly in mobile/client systems and selected rack CPU memory |
| NAND | NAND Flash | Different memory technology from DRAM/HBM |
| eSSD | Enterprise SSD | Enterprise solid-state storage |
| CoWoS | Chip-on-Wafer-on-Substrate | TSMC advanced-packaging family; customer allocation is not inferred from revenue share |
| TSV | Through-Silicon Via | Important in HBM stacking / 3D integration |
| CUDA | NVIDIA compute platform / programming ecosystem | Analyzed as a software switching-cost variable |
| NVLink / NVSwitch | NVIDIA scale-up interconnect technologies | Not treated as the same layer as scale-out networking |
| CapEx | Capital Expenditure | Guidance, expectation, and actuals remain separate |
| OpEx | Operating Expenditure | Not mechanically combined with CapEx |
| FCF | Free Cash Flow | Company-defined and GAAP/non-GAAP identities are preserved |
| PPA | Power Purchase Agreement | Contracted capacity is not energized/utilized load |
| PUE | Power Usage Effectiveness | Data-center efficiency metric |
| CSP | Cloud Service Provider | Hyperscalers are an important subset |
| OEM | Original Equipment Manufacturer | End-device / system manufacturer |
| ODM | Original Design Manufacturer | Design-and-manufacturing service provider |
| BOM | Bill of Materials | Used in end-market cost-transmission analysis |
| TCO | Total Cost of Ownership | Preferred system-level comparison unit |
| ASP | Average Selling Price | Product and time denominator must be explicit |

## Standard units

- Data capacity: KB / MB / GB / TB / PB / EB
- Bits and transfer rates: Kb / Mb / Gb / Tb; Mb/s / Gb/s / Tb/s
- Power: W / kW / MW / GW
- Energy: Wh / kWh / MWh / TWh
- Frequency: Hz / kHz / MHz / GHz
- Process / dimensions: nm / μm / mm / mm²
- U.S. dollar values: preserve source precision where material, e.g. US$96.221B and US$279B

## Core analytical concepts

### AI Resource Gravity
The mechanism by which higher willingness to pay, longer-duration orders, and stronger expected returns from AI/HPC pull scarce capital and physical resources toward AI/HPC uses.

### Scarce-layer Value Capture
Value capture arising in layers with low supply elasticity and difficult substitution, strengthened by scarcity, switching costs, and supply coordination. It is not a legal monopoly finding.

### Non-AI Residual Capacity (NARC)
Effective supply available to non-AI markets after AI / Anchor Buyer demand and other priority demand have been allocated.

### Two-Speed Semiconductor Economy
A structure in which the AI Infrastructure Economy and Traditional Device Economy share parts of the same upstream resource base but have different willingness to pay, contract duration, BOM constraints, and capital-formation power.

### AI Capacity Gap / AI Capacity Growth Gap
**AI Capacity Gap** is the absolute physical shortfall `AI effective demand − AI effective capacity` within the same layer and delivery window; **AI Capacity Growth Gap** is the difference between demand growth and effective-capacity growth and describes only the direction in which the gap is changing. The two are not interchangeable.

### AHICR
Advanced/HPC Incremental Capacity Capture Ratio. Measures a buyer's capture of **incremental** advanced/HPC capacity in one physical layer; it is not a historical revenue-share metric.

### Cloud System-Stack Substitution
The mechanism by which hyperscalers combine custom accelerators, interconnect, compiler/runtime, racks/pods, and captive workloads into a second production-grade system stack.

### Anchor Compute Buyer Effect
The mechanism by which long-duration compute commitments from large model companies influence data-center, power, chip, memory, and project-financing buildout.

### Rolling Bottleneck Cascade
The dynamic rotation of the binding constraint across logic, HBM, advanced packaging, networking, power, utilization, and related layers.

### AI Software Unit Economics
A workflow-level cost framework incorporating inference, retrieval/storage, tools/APIs, retries, human review, and other variable AI costs.

### Task-to-Job Translation
Task Exposure → Adoption Economics → Workflow Redesign → Responsibility Constraint → Employment / Wage Outcome. Prevents technical exposure rates from being converted directly into job-loss rates.

## Scenario terminology

- **S1 — Competitive Expansion:** higher supply elasticity, multi-sourcing, and portability distribute value capture more broadly.
- **S2 — Baseline Concentration:** a small number of system platforms / scarce-layer suppliers retain strong economics while real substitution paths continue developing.
- **S3 — Resource Hegemony:** multiple scarce layers and switching costs strengthen together, materially raising the cost of replicating the full infrastructure stack.
- **S4 — Capital Hard Landing:** utilization, clearing prices, forward commitments, and accounting losses deteriorate together, producing capital clearing.

## Evidence identity

- **F — Fact:** already occurred and publicly verifiable.
- **H — Hypothesis:** explicit forward assumption.
- **M — Mechanism:** causal transmission path.
- **S — Scenario:** conditional future state.
- **X — Falsification:** reverse signal strong enough to force a judgment change.
- **A:** first-party / formal evidence.
- **B:** institutional research.
- **C:** sell-side / supply-chain / media estimate.
- **D:** report model / arithmetic / sensitivity / stress test.


\newpage


# Research Transparency, Limitations, and Correction Policy

## 1. Authorship and research vehicle

The report is authored as **James (kamanager2012)**. The GitHub repository is both a versioned research vehicle and the working record for evidence tracing, corrections, bilingual synchronization, and publication builds.

Repository traceability is not presented as equivalent to external peer review.

## 2. External review status

As of 2026-08-28, the repository **does not claim completion of formal independent peer review, audit assurance, or institutional rating**.

If formal external review is later obtained, this page should record:

- reviewer / institution when disclosure is permitted;
- review scope;
- review date;
- independence;
- material changes;
- unresolved objections.

Unrecorded external feedback must not be described as “peer reviewed.”

## 3. Funding / Conflict of Interest

The repository **does not make an unconfirmed claim that no conflicts of interest exist**.

Before public release, the author should provide an explicit statement covering at minimum:

- funding, consulting fees, commercial relationships, or material holdings connected to companies directly analyzed in the report;
- commercial relationships that could materially affect source selection or conclusions;
- if none are relevant, an explicit author-confirmed statement that there are no material related conflicts requiring disclosure.

Until that statement is completed, the **Conflict-of-Interest Gate remains open**.

## 4. Source-selection principles and potential bias

The evidence priority is:

1. statutory filings, regulator/government documents, and formal contracts;
2. official company IR / product / technical material;
3. high-quality institutional research;
4. sell-side / supply-chain / media estimates;
5. D-grade report models.

This hierarchy reduces the risk that repeated secondary reporting becomes “fact,” but public-source bias remains:

- companies disclose selectively;
- customer allocation, yield, contract pricing, and utilization are often undisclosed;
- disclosure depth differs materially across regions;
- institutional models may contain non-public assumptions;
- fast-moving markets create publication-lag risk.

“Not publicly disclosed” therefore supports only “cannot be confirmed from public evidence,” not absolute non-existence.

## 5. Research limitations

The report cannot:

- audit undisclosed contracts, internal purchasing, or real customer allocation;
- infer wafer / HBM / CoWoS physical share directly from revenue share;
- infer energized / utilized AI load from contracted MW;
- prove that a future scenario must occur;
- calculate every company's AI-specific ROI exactly from public materials;
- automatically treat every number in 40 volumes, 8 macro essays, and 32 publication chapters as audited fact.

Full historical numeric claim-by-claim audit remains a public-release hard gate. The repository now includes a machine-readable schema and candidate extractor, but those do not substitute for source review.

## 6. Correction policy

When a high-impact factual error is found:

1. locate the claim and original source;
2. classify the error as Fact, denominator, time-window, forecast/actual identity, or translation drift;
3. correct the Chinese canonical publication;
4. synchronize the English publication;
5. regress the evidence ledger, source index, model index, and affected research modules;
6. preserve the change in Git history / Release Notes;
7. if scenario weighting changes, state explicitly which judgment is being reweighted.

A claim contradicted by evidence cannot be defended merely by saying that “the long-run story remains intact.”

## 7. Version and cutoff

The current formal research retrieval/revision cutoff is **2026-08-28**.

Post-release evidence should enter a later version rather than silently rewriting a released historical edition.

## 8. External-use boundary

This is industry research. It is not:

- investment advice;
- a securities rating;
- legal advice;
- an audit opinion;
- a guaranteed forecast.

Readers should distinguish Facts, institutional estimates, report models, and scenarios.


\newpage


# Competitive Set, Substitution Paths, and Counter-Evidence Matrix

> This matrix prevents the “hegemony” thesis from being supported only by evidence about one platform's strengths. It does not treat every company as a direct competitor in one market; competition is defined separately by physical layer, system layer, and end market.

| Analytical layer | Primary observed set | Main substitutes / competitors | Core comparison metrics | Required counter-evidence / boundary | Main chapters |
|---|---|---|---|---|---|
| General-purpose AI system stack | NVIDIA | Google TPU/Ironwood, AWS Trainium, Microsoft Maia, Meta MTIA, AMD Instinct/ROCm | production workload, external availability, migration cost, system utilization, TCO, supply assurance | custom silicon is already a real second route; one-chip benchmarks do not prove full system substitution | Ch02, Ch12, Ch16 |
| Advanced logic | TSMC | Samsung Foundry, Intel Foundry, SMIC, and future qualified second sources | qualified node, volume, yield disclosure, customer diversity, time-to-capacity | foundry revenue share ≠ frontier yield/node capacity; HPC share ≠ AI share | Ch04, Ch09, Ch17 |
| HBM / DRAM | SK hynix, Samsung, Micron | conventional-DRAM economics, CXMT conventional DRAM, future HBM entrants | HBM qualification, bits/wafer input, product mix, contract pricing, allocation fulfillment | DDR/RDIMM per-wafer economics can recover; HBM resource pull is not infinitely one-directional | Ch05, Ch21 |
| Advanced packaging | TSMC CoWoS | Samsung/Intel packaging, OSAT expansion, alternative integration architectures | qualified capacity, lead time, yield/throughput disclosure, customer access | customer-level CoWoS allocation is undisclosed; B-grade demand share cannot become TSMC fact | Ch06 |
| Interconnect / software | CUDA/NVLink/NVSwitch ecosystem | ROCm, XLA/TPU stack, AWS Neuron, open compiler/runtime, alternative fabrics | migration cost, framework coverage, cluster scale, debuggability, production uptime | proprietary stacks can be bypassed for selected workloads; “runs” does not mean low migration cost | Ch02, Ch12, Ch16 |
| Power / powered land | hyperscaler / AI-campus demand | utility expansion, restart projects, SMR/nuclear, grid/transmission buildout, regional alternatives | Announced→Contracted→Permitted→Energized→Utilized, Time-to-Power | headline GW cannot be added into active AI load; supply expansion can move the bottleneck toward utilization | Ch07 |
| Model-company demand | OpenAI, Anthropic, other Anchor Buyers | hyperscaler internal workloads, enterprise demand, sovereign demand | contract duration, delivered capacity, utilization, monetization, financing support | long-duration commitments improve buildout certainty and can also amplify duration mismatch | Ch13, Ch23 |
| China frontier stack | domestic accelerator/software/memory/foundry ecosystem | global frontier stack plus domestic consumer/general-compute substitutes | advanced logic, HBM, packaging, interconnect, compiler/runtime, frontier workload, power closure | conventional DRAM/NAND or smartphone substitution does not prove frontier-AI closure; export constraints do not mean “no substitutes exist” | Ch17 |
| Client / edge AI | Apple, Qualcomm, AMD, Intel | local inference, hybrid cloud-edge, NVIDIA edge products | performance/W, memory footprint, OS integration, distribution, privacy/latency | data-center system economics cannot be copied directly into battery/power-constrained edge markets | Ch15, Ch16 |
| Capital cycle | hyperscalers, system sellers, memory/foundry/power projects | capacity overshoot / ROI shock as counter-scenarios | utilization, D&A, FCF, clearing price, commitments, asset duration | high CapEx can be a moat or a future write-down source; the same dollar cannot be added repeatedly across supply-chain ledgers | Ch19, Ch22, Ch24 |

## Use rules

1. Any dominance/hegemony judgment must answer at least four questions: **does substitution exist, what is migration cost, can scarce inputs be multi-sourced, and is price feedback working?**
2. Competitive sets are layer-specific; smartphone SoCs, frontier-training accelerators, foundries, and HBM vendors must not be forced into one market-share table.
3. “No equivalent substitute” and “no substitute at all” are different statements.
4. Every major update should inspect at least one piece of evidence that could **weaken** the main thesis rather than only adding supportive evidence.
5. If counter-evidence crosses Chapter 29's operational trigger, S1–S4 weighting must change rather than burying the evidence in a footnote.


\newpage


# Part I · Chapter 1: Executive Summary and Core Judgments for the Next Decade

## 1. Core conclusion

> **The competitive unit in AI infrastructure has moved from the individual chip to the full system stack. Long-run value capture increasingly depends on who can simultaneously coordinate multiple scarce layers—advanced logic, HBM, advanced packaging, interconnect, software, racks/data centers, and power—and convert those physical resources into highly utilized, portable workloads that generate cash flow.**

This is not a claim of permanent monopoly, nor is it a point forecast of market share in 2036. The report analyzes a changing resource-allocation mechanism: when AI/HPC workloads offer materially higher willingness to pay, longer contract duration, greater use of prepayments, and higher expected returns than traditional end markets, incremental capital and scarce resources are more likely to move toward AI infrastructure. When supply expansion, system substitution, utilization, or commercial returns change, that structure can rebalance.

As of **August 28, 2026**, public evidence is most consistent with **S2 — Baseline Concentration**: a small number of system platforms and scarce-layer suppliers retain strong economics; HBM, advanced packaging, and power remain important physical constraints; and hyperscaler custom systems, China's parallel stack, and supply expansion continue to provide real substitution paths.

## 2. Eight factual anchors

### 2.1 NVIDIA's commercial delivery unit has moved up to the rack-scale system

The official GB200 NVL72 specification includes **72 Blackwell GPUs, 36 Grace CPUs, 13.4 TB of HBM3E, and 17 TB of LPDDR5X**. The delivered product is therefore a combination of compute, memory, interconnect, software, and rack architecture rather than merely an accelerator card.[^ch01-1]

### 2.2 NVIDIA's seller-side economics remain exceptionally strong

NVIDIA reported FY27 Q2 Revenue of **US$96.221B**, Data Center revenue of **US$89.0B**, GAAP gross margin of **75.0%**, and GAAP operating income of **US$63.734B**; the company also said Vera Rubin was in full production.[^ch01-2]

### 2.3 Forward supply commitments have expanded sharply

NVIDIA's manufacturing, supply, and capacity commitments increased from **US$95.2B** on January 25, 2026 to **US$279B** on July 26, 2026. The FY27 Q2 Form 10-Q states that the latest commitments are primarily associated with memory and manufacturing facilities required for data-center infrastructure systems, but it does not provide a supplier-level split. The aggregate cannot therefore be allocated directly to TSMC, CoWoS, or any single HBM vendor.[^ch01-3]

### 2.4 TSMC's demand structure has shifted materially toward HPC

In 2025, TSMC's HPC platform represented **58%** of annual net revenue and smartphone **29%**; 3 nm, 5 nm, and 7 nm represented **24% / 36% / 14%** of wafer revenue, respectively. These are revenue-mix measures, not customer-level wafer allocation, and they cannot be converted directly into CoWoS share.[^ch01-4]

In 2Q26, TSMC's HPC platform represented **66%** of quarterly revenue and smartphone **22%**; advanced technologies, defined as 7 nm and below, represented **77%** of wafer revenue. This further shows that HPC is one of the core drivers of incremental advanced-manufacturing demand, but HPC still cannot be equated one-for-one with AI.[^ch01-5]

### 2.5 HBM has become a manufacturing-resource competition layer

Micron disclosed that, under **same technology node / same number of bits** conditions, HBM3E requires approximately **3× the wafer supply of DDR5**. This is a wafer-supply trade ratio, not a price multiple and not a fixed manufacturing constant for every HBM generation.[^ch01-6]

TrendForce forecasts that HBM + RDIMM will represent approximately **51% of 2026 DRAM bit supply**. That is an institutional forecast rather than a full-year actual. Read together with Micron's ~3× trade ratio, it helps explain why AI/server memory can exert more pressure on conventional-DRAM residual supply than bit share alone suggests.[^ch01-7]

### 2.6 Advanced Packaging has become a verifiable growth constraint

TSMC said in 4Q24 that advanced-packaging capacity was “very tight” and could not satisfy all customer demand; in its 2Q26 earnings call it stated more directly that packaging tightness was limiting customer growth. TSMC does not disclose customer-level CoWoS allocation, so third-party estimates of customer concentration must retain their institutional-estimate identity.[^ch01-8]

### 2.7 Power has become an independent physical constraint alongside wafers, memory, and packaging

NVIDIA's DGX GB200 hardware guide specifies rack power of approximately **120 kW**. At the same time, an approximately 835 MW nuclear restart, a long-duration PPA with up to 1.92 GW of contract quantity, and advanced-nuclear development paths in the hundreds of MW for the 2030–2035 period show that Time-to-Power, grid connection, substations, firm power, and permitting are now part of the AI system-delivery constraint set. Contracted, Permitted, Energized, and Utilized MW must remain separate.[^ch01-9]

### 2.8 Hyperscaler custom systems have become a real second path

Google Ironwood, AWS Trainium3 UltraServers, Microsoft Maia 200, and Meta MTIA 300 show that hyperscaler competition has moved beyond “designing an ASIC” toward system-stack competition spanning accelerators, compiler/runtime, interconnect, rack/pod architecture, and captive workloads.[^ch01-10]

This does not mean NVIDIA has already been displaced. The variables that matter are how much production workload these systems carry, whether migration cost falls, whether utilization is sustainable, and whether they continue to compete for the same advanced logic, HBM, packaging, and power.

## 3. Seven core mechanisms

### 3.1 Scarce-layer Value Capture

When a platform combines strong cash generation, long-duration orders, system-definition power, switching costs, and supply orchestration, it is better positioned to commit early to next-generation scarce resources and thereby improve delivery certainty. High gross margin is only one possible result of this mechanism; it is not a legal monopoly finding.

### 3.2 AI Resource Gravity

When AI/HPC workloads offer higher risk-adjusted returns, longer-duration orders, and stronger utilization visibility, capital and effective capacity are more likely to move toward high-value layers such as advanced logic, HBM, advanced packaging, networking, and power.

### 3.3 Non-AI Residual Capacity

Traditional industries do not face gross worldwide capacity. They face the effective residual supply available after priority allocation:

```text
NonAI_Residual(t)
= Effective_Supply(t)
- AI_Absorption(t)
- Other_Priority_Demand(t)
```

This is why “total supply is growing” and “smartphones, PCs, and other traditional end markets are still facing pricing or configuration pressure” can both be true.

### 3.4 Two-Speed Semiconductor Economy

The AI Infrastructure Economy and the Traditional Device Economy share parts of the same upstream supply chain but differ in willingness to pay, contract duration, prepayment structure, BOM constraints, and end-market price elasticity.

The central structural change is not that consumer electronics disappear. It is:

> **AI/HPC is increasing the influence of a relatively small number of capital-intensive buyers over marginal semiconductor demand and incremental capital formation.**

### 3.5 AI Capacity Gap: separate the absolute gap from the growth gap

To determine whether a physical layer is **actually short of deliverable supply today**, the report defines an absolute gap:

```text
AI_Capacity_Gap_i(t)
= AI_Effective_Demand_i(t)
- AI_Effective_Capacity_i(t)
```

where \(i\) represents physical layers such as advanced logic, HBM/DRAM, advanced packaging, networking, and power. Demand and capacity must use the **same delivery window, qualification/quality boundary, and physical unit**, such as wafers/month, qualified package starts/month, bits/year, or MW.

- **Absolute Gap > 0:** current deliverable supply is insufficient;
- **Absolute Gap ≈ 0:** current supply and demand are near balance;
- **Absolute Gap < 0:** current effective headroom exists.

To determine whether scarcity pressure is widening or converging, the report separately defines:

```text
AI_Capacity_Growth_Gap_i(t)
= Growth(AI_Effective_Demand_i(t))
- Growth(AI_Effective_Capacity_i(t))
```

The Growth Gap is a difference in growth rates over the same period, measured in percentage points. It describes the **direction of pressure**, not the current stock gap:

- **Growth Gap > 0:** scarcity may widen, or existing headroom may be eroded;
- **Growth Gap < 0:** scarcity may converge, or effective headroom may expand;
- **Growth Gap = 0:** supply and demand are changing at the same rate; it does not imply that no shortage exists.

A strong S4 Capital Hard Landing signal therefore requires **Absolute Gap < 0 / excess capacity** together with deterioration in utilization, clearing prices, and forward commitments—not a negative Growth Gap by itself.

AI Capacity Gap, AI Capacity Growth Gap, and Non-AI Residual Capacity answer different questions: the first two measure the current AI-side shortfall and its direction of change; NARC measures effective supply left for non-AI demand after priority allocation.

### 3.6 Cloud System-Stack Substitution

Hyperscaler custom stacks can generate two effects that point in different directions but coexist:

1. **Platform-profit diversion:** part of the workload no longer pays the full economics of an external system platform;
2. **Upstream resource competition:** the custom system itself still requires advanced logic, HBM, packaging, and power.

More custom silicon therefore does not automatically mean less upstream physical scarcity.

### 3.7 Anchor Compute Buyer Effect

Multi-year and decade-scale compute commitments from large model companies can increase infrastructure revenue visibility and financing certainty, pulling forward cloud, data-center, power, and semiconductor construction. Conversely, if utilization or monetization disappoints, long-duration commitments can amplify duration mismatch and stranded-capacity risk.

## 4. China must be assessed by system layer, not by one “localization rate”

China has built a real and continuously developing accelerator/software parallel stack and has strengthened parallel supply in consumer computing, DRAM/NAND, selected general-purpose computing, and domestic software ecosystems. Frontier-AI equivalence, however, still requires advanced logic, HBM-class memory, advanced packaging, high-speed interconnect, compiler/runtime, frontier workloads, and power to reach verifiable scale simultaneously.[^ch01-11]

The report therefore rejects both extremes: “China has already fully caught up” and “China has no meaningful substitute capability.” The more accurate state is:

> **China has moved beyond the stage of having no alternative system, but public evidence is still insufficient to show globally equivalent scaled closure across every frontier critical layer.**

## 5. The capital cycle cannot be judged from one CapEx total

Cloud CapEx, system-vendor revenue, foundry revenue, memory revenue, and power/data-center investment appear on different ledgers along the same supply chain. They cannot be mechanically added into one “global AI investment” number.

A move toward **S4 — Capital Hard Landing** requires simultaneous evidence across at least four groups:

- **Accounting:** impairment, write-downs, and depreciation pressure;
- **Utilization / Revenue:** effective utilization, unit revenue, and real monetization;
- **Market Clearing:** lease rates, second-hand prices, lead times, and inventory;
- **Forward Commitment:** CapEx guidance, supply commitments, and Anchor Buyer contracts.

As of August 2026, the evidence is more consistent with:

> **high-intensity capital expansion + rising ROI pressure**

than with a confirmed industry-wide Capital Hard Landing.

## 6. S1–S4: the future is not one deterministic curve

**Table 1.1 — Four standard AI-infrastructure scenarios**

| Scenario | Core structure |
|---|---|
| S1 — Competitive Expansion | supply elasticity and interoperability rise; multiple system stacks coexist; value capture becomes more distributed |
| S2 — Baseline Concentration | a small number of system platforms and scarce-layer suppliers retain strong economics while substitution paths continue developing |
| S3 — Resource Hegemony | several scarce layers and switching costs strengthen simultaneously; challengers must replicate a more complete infrastructure stack |
| S4 — Capital Hard Landing | utilization, clearing prices, CapEx/commitments, and accounting losses deteriorate together |

**Source:** Report scenario framework.  
**Note:** S1–S4 are parallel conditional states. They do not carry fixed probabilities and are not treated as inevitable sequential stages.

As of August 2026, **S2 — Baseline Concentration** is the state that best matches the current evidence mix, not a fixed ten-year forecast.

## 7. What evidence would force the report to change its judgment

The following developments should materially reduce S2/S3 weight or force the relevant mechanisms to be re-evaluated:

- sustained declines or large cancellations in leading system-platform commitments;
- advanced packaging no longer being described by major suppliers as a growth constraint;
- sustained abundance in HBM / DRAM residual supply;
- large-scale, low-migration-cost substitution by cloud custom systems in frontier workloads;
- energized power and grid interconnection improving enough that Time-to-Power no longer differentiates projects;
- large-scale rescheduling or underutilization of Anchor Compute Buyer commitments;
- first-party evidence showing scaled frontier-system closure across multiple critical layers in China;
- formal regulatory remedies materially reducing proprietary-interface switching costs.

Conversely, if AI Capacity Gap remains positive across several physical layers, NARC continues to fall, migration costs remain high, and forward commitments continue expanding, the relative weight of S3 Resource Hegemony rises.

## 8. Report structure

The report is organized into four parts:

- **Part I — System Power and Physical Scarcity:** system stack, advanced logic, HBM, advanced packaging, power, and manufacturing redundancy;
- **Part II — Demand, Substitution, and the Second System Stack:** model economics, hyperscaler custom systems, Anchor Compute Buyers, China's parallel stack, and competition policy;
- **Part III — Capital Cycles, Profit Pools, and External Transmission:** CapEx, value capture, consumer transmission, depreciation, financing, capital clearing, and labor;
- **Part IV — Method, Scenarios, Monitoring, and Strategy:** evidence architecture, 2026–2036 milestones, monitoring framework, S1–S4, and the final strategic judgment.

Readers who read only one chapter should use this chapter as the entry point to the report's conclusions. Readers who need to verify a high-impact number should continue to the relevant thematic chapter and its References.

## References

[^ch01-1]: NVIDIA, “GB200 NVL72,” official product page, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^ch01-2]: NVIDIA, “NVIDIA Announces Financial Results for Second Quarter Fiscal 2027,” 2026, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^ch01-3]: NVIDIA Corporation, Form 10-Q for quarter ended 2026-07-26, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm ; NVIDIA Corporation, FY26 Form 10-K, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
[^ch01-4]: TSMC, 4Q25 Presentation / 2025 full-year platform and technology mix, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
[^ch01-5]: TSMC, “2Q26 Quarterly Results,” platform and technology revenue mix, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^ch01-6]: Micron Technology, FY24 Q2 Prepared Remarks, 2024-03-20, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^ch01-7]: TrendForce, 2026-08-25, HBM + RDIMM 2026E DRAM bit-supply structure, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^ch01-8]: TSMC, 4Q24 Earnings Conference Transcript, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf ; TSMC, 2Q26 Earnings Conference Transcript, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^ch01-9]: NVIDIA, DGX GB200 Hardware Guide, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html ; Constellation, Crane Clean Energy Center announcement, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs ; Talen Energy, 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm ; Kairos Power / Google partnership, https://www.kairospower.com/google
[^ch01-10]: Google, “Ironwood TPU,” https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; AWS, “Amazon EC2 Trn3 UltraServers,” https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ ; Microsoft, “Maia 200,” https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ ; Meta, “MTIA 300,” https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
[^ch01-11]: CXMT, STAR Market registration prospectus, 2026-05-27, Shanghai Stock Exchange, https://static.sse.com.cn/stock/disclosure/announcement/c/202605/002170_20260527_23QQ.pdf ; Moore Threads, MTT S80 official product page, https://en.mthreads.com/product/S80 ; DeepSeek, “DeepSeek-V3 Technical Report,” https://arxiv.org/abs/2412.19437 ; TrendForce, 2026-06-12, 1Q26 foundry revenue shares, https://www.trendforce.com/presscenter/news/20260612-13095.html


\newpage


# Part I · Chapter 2: NVIDIA's System Stack and Platform Power

## 1. The competitive unit has moved from the GPU to the system stack

NVIDIA's most important current advantage is no longer the point performance of one GPU generation. It is the ability to organize accelerators, HBM, scale-up fabric, compiler/runtime, libraries, rack architecture, and deployment tooling into a repeatable production system. The official GB200 NVL72 specification makes the shift in sales unit explicit:[^ch02-1]

**Table 2.1 — GB200 NVL72 rack-scale system structure**

| Layer | Official specification / structure |
|---|---|
| GPU | 72 Blackwell GPUs |
| CPU | 36 Grace CPUs |
| GPU memory | 13.4 TB HBM3E |
| CPU memory | 17 TB LPDDR5X |
| Scale-up domain | 72-GPU NVLink domain |
| Rack | liquid-cooled rack-scale system |

**Source:** NVIDIA GB200 NVL72 official product page.[^ch02-1]  
**Note:** The table reports the official system specification; it does not represent shipment volume, utilization, or customer deployment scale.

This changes how competition must be measured. In the add-in-card era, FLOPS, memory capacity, and card price could dominate the comparison. At rack scale, the comparison has to include memory hierarchy, scale-up/scale-out interconnect, compiler/runtime, distributed-training software, power/cooling, deployment tooling, and workload-migration cost.

A cheaper ASIC die therefore does not automatically imply a cheaper production AI system.

## 2. NVLink / NVSwitch: turning communication into an internal system capability

Frontier-model training is not limited by single-GPU compute alone. Tensor parallelism, pipeline parallelism, expert parallelism, and collective communication push performance toward bandwidth, topology, synchronization, and collective implementation.

The strategic value of NVLink/NVSwitch is that scale-up communication is designed as a platform-internal capability. GB200 NVL72 organizes 72 GPUs inside one NVLink domain; NVIDIA's current product page reports **130 TB/s of aggregate NVLink bandwidth per rack**.[^ch02-1]

That does not prove Ethernet-based alternatives are inherently incapable of substitution. It changes the substitution problem:

> A challenger must replace not one GPU, but the production capability created by **compute + memory + in-domain interconnect + the software execution model**.

For that reason, this report does not use unverified nanosecond-level latency comparisons or treat promotional benchmarks as independent measurements. The relevant evidence is production workload behavior: post-migration throughput, utilization, engineering cost, and reliability.

## 3. CUDA / PTX: the moat is a cross-generation software asset

CUDA's strategic value should not be reduced to an imaginary fixed "software tax" that does not appear in financial disclosures. It is better understood as a long-lived software asset:

- compiler and kernel ecosystem;
- libraries;
- profiling / debugging;
- framework integration;
- distributed communication;
- inference / training runtime;
- deployment tooling;
- developer knowledge.

PTX matters because it provides a relatively stable intermediate representation. Upper-layer software does not need to be rewritten from scratch every time the GPU generation changes. Hardware can move from Hopper to Blackwell to Rubin while a meaningful share of software assets remains reusable.

That creates a cross-generation mechanism:

**larger installed base → more production software assets → lower in-platform upgrade cost → higher out-of-platform migration cost.**

This is why NVIDIA's advantage cannot be measured by one benchmark or proved by an undisclosed "CUDA margin."

## 4. Rack-scale architecture extends switching costs into the data center

When the purchasing unit becomes the rack, migration costs extend from software into physical infrastructure. Customers build not only code, but also:

- rack / pod topology;
- power distribution;
- liquid cooling;
- networking;
- firmware;
- cluster management;
- scheduling and performance validation.

Changing one accelerator may be a procurement action. Changing a rack-scale system can require revalidating software-hardware coordination and data-center engineering.

This is where chip-only benchmarks most easily understate system power. The farther the system extends into racks, pods, and sites, the more challengers must prove deployment time, reliability, and total cost of ownership—not simply peak compute.

## 5. Why platform profit can become next-generation resource-reservation power

If system-level advantage produces high profit and free cash flow, it can influence the supply chain. The company-level anchors needed here are limited to one set:

**Table 2.2 — NVIDIA seller-side economics and forward supply commitments**

| Metric | Current public value |
|---|---:|
| FY26 Data Center revenue | US$193.737B |
| FY26 NVIDIA-defined non-GAAP free cash flow | US$96.575B |
| FY27 Q2 revenue | US$96.221B |
| FY27 Q2 Data Center revenue | US$89.0B |
| FY27 Q2 GAAP gross margin | 75.0% |
| FY27 Q2 GAAP operating income | US$63.734B |
| 2026-07-26 manufacturing, supply, and capacity commitments | US$279B |

**Source:** NVIDIA FY26 results, FY27 Q2 results, and FY27 Q2 Form 10-Q.[^ch02-2][^ch02-3][^ch02-4]  
**Note:** US$279B is the aggregate manufacturing, supply, and capacity commitment; public filings do not provide a supplier-level split.

The FY27 Q2 10-Q states that the latest commitments are primarily associated with memory and manufacturing facilities required for data-center infrastructure systems.[^ch02-4] The filing does not split the US$279B across TSMC, CoWoS, SK hynix, Micron, Samsung, or any other individual supplier.

The number therefore demonstrates the scale of aggregate forward supply commitments; it is not evidence of any specific supplier's future revenue.

This creates a testable cross-generation reinforcing mechanism:

**high system profit → stronger supply commitments and resource reservation → greater delivery certainty → stronger customer retention → next-cycle system revenue.**

It is not an automatic monopoly formula. Suppliers still optimize for customer diversification, credit quality, utilization, geopolitics, and long-run bargaining balance.

## 6. NVIDIA's system power has clear physical boundaries

NVIDIA does not directly manufacture every critical scarce layer. It still depends on:

- leading-edge foundries;
- HBM vendors;
- the advanced-packaging ecosystem;
- data-center operators;
- grid / power suppliers.

Strong platform power therefore does not make physical supply fully endogenous. A mismatch in TSMC capacity, HBM, advanced packaging, or power can constrain next-generation delivery.

This is why the report separates **Scarce-layer Value Capture** from a simple market-share monopoly story. A system platform can have strong coordination and bidding power while remaining constrained by the supply elasticity of external physical layers.

## 7. The real counterattack is a Cloud System Stack, not a single ASIC

The strategic significance of Google TPU/Ironwood, AWS Trainium, Microsoft Maia, and Meta MTIA is not merely the existence of another chip.[^ch02-5] Hyperscalers also possess:

- captive large-scale workloads;
- cloud distribution;
- control of data-center infrastructure;
- internal compiler/runtime software;
- in-house interconnect and rack/pod design;
- the ability to optimize a narrower workload at system level.

The future competition is therefore not:

> NVIDIA GPU vs. custom ASIC

but:

> **NVIDIA system stack vs. cloud system stack**

This can produce two effects that point in opposite directions yet coexist:

1. **Platform-profit diversion:** in-house cloud systems reduce dependence on part of NVIDIA's platform profit pool;
2. **Upstream resource competition:** those systems still compete for advanced logic, HBM, advanced packaging, and power.

Successful cloud custom silicon does not automatically relieve upstream physical scarcity.

## 8. What would count as genuine erosion of the moat

The NVIDIA system moat should not be judged from product-launch count or single-chip performance. The structure weakens only if several of the following variables move together:

- cloud system stacks reach production scale in frontier training / high-value inference;
- open software materially lowers CUDA migration cost;
- alternative scale-up fabrics reach production-grade scale;
- engineering cost and performance loss during multi-stack migration continue to fall;
- scarce upstream resources stop disproportionately supporting NVIDIA's roadmap;
- major customers distribute real workloads across multiple systems rather than running only benchmarks or narrow internal tests.

If several of these changes persist, NVIDIA's platform power could move from "system-level pricing power" toward a more negotiable "integration advantage." If migration remains expensive while in-platform generational upgrades stay low-friction, the system moat remains intact.

## 9. Current judgment

As of August 2026, the most accurate description is neither "GPU competition is over" nor "cloud ASICs have replaced NVIDIA."

It is:

> **NVIDIA currently has the most mature commercial general-purpose AI system stack; hyperscalers have built a real second system-stack path, but the extent of substitution must be validated through production workloads, migration cost, utilization, and upstream resource dependence.**

That is the starting point for the rest of the book's analysis of TSMC, HBM, advanced packaging, power, and the capital cycle. The competitive unit has moved from the die to the system, and the system remains constrained by multiple external scarce layers.

## References

[^ch02-1]: NVIDIA, “GB200 NVL72,” official product page, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^ch02-2]: NVIDIA, “NVIDIA Announces Financial Results for Fourth Quarter and Fiscal 2026,” https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
[^ch02-3]: NVIDIA, “NVIDIA Announces Financial Results for Second Quarter Fiscal 2027,” https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^ch02-4]: NVIDIA Corporation, Form 10-Q for quarter ended 2026-07-26, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^ch02-5]: Google, “Ironwood TPU,” https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; AWS, “Amazon EC2 Trn3 UltraServers,” https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ ; Microsoft, “Maia 200,” https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ ; Meta, “MTIA 300,” https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/


\newpage


# Part I · Chapter 3: AI Resource Gravity and Non-AI Residual Capacity

## 1. "AI absorption" does not mean every semiconductor capacity pool is being drained

AI infrastructure affects the supply chain unevenly. The resources most exposed to reprioritization are those shared with frontier AI and relatively inelastic in the short run:

- advanced logic;
- HBM / RDIMM / selected DRAM;
- advanced packaging;
- high-end substrates / networking;
- power-management components;
- data-center power.

This report defines the pull that high-value demand exerts on capital and capacity as **AI Resource Gravity**.

## 2. The economics of Resource Gravity

If one demand pool offers higher willingness to pay, longer contracts, greater utilization certainty, and stronger credit quality, suppliers have an economic incentive to direct more incremental capital and capacity toward it.

The transmission chain is:

> high-value AI/server demand → higher expected return → product-mix / capacity-allocation shift → lower residual capacity for lower-priority demand

This does not mean suppliers serve only the top buyer, nor that traditional markets stop receiving supply. It describes a change in the priority of **incremental** resources.

### 2.1 Price is not the only clearing mechanism: Allocation Assurance matters more than spot price

In an extreme shortage, the market does not clear through price alone. **Long-term agreements, customer credit, prepayments, purchasing scale, and allocation fulfillment** can determine first whether a buyer receives enough volume.

TrendForce stated in January 2026 that as U.S. CSPs locked in capacity, other customers had to accept higher prices to secure supply allocations. In March 2026, it further noted that PC OEMs and module makers with lower allocation-fulfillment rates were forced to procure incremental supply at higher prices.[^ch03-1][^ch03-2]

Therefore:

> **willingness-to-pay ≠ guaranteed quantity**

The systemic risk is not only how much prices rise. It is whether residual capacity falls far enough that secondary buyers cannot obtain sufficient, timely, and sustainable supply even after accepting higher prices.

This mechanism is more auditable than the absolute claim that one buyer has captured "100% of capacity."

## 3. Why Non-AI Residual Capacity matters more than gross capacity

The effective supply available to traditional markets can be represented as:

> **Non-AI Residual Capacity = total effective supply − AI/server absorption − other priority demand**

If total supply rises 20% while AI/server demand absorbs 40% more, effective residual capacity for non-AI markets can still decline.

"Global capacity is increasing" therefore does not automatically imply that PCs, smartphones, general servers, or consumer GPUs are returning to abundant supply.

### 3.1 Two-Speed Semiconductor Economy: shared resources, different capital-formation speeds

The AI Infrastructure Economy and the Traditional Device Economy share parts of the same advanced-logic, memory, packaging, and power-management resource base, but they differ materially in willingness to pay, contract duration, use of prepayments, BOM constraints, and end-market price elasticity.

The long-run consequence of AI Resource Gravity is therefore not limited to current-period allocation. It also affects the next round of capital formation: suppliers decide where the next dollar of CapEx goes based on risk-adjusted returns. The **Two-Speed Semiconductor Economy** describes this difference in resource economics; it is not a factual declaration that consumer electronics are being permanently “sacrificed.”

### 3.2 AI Capacity Gap: separate the absolute gap from the growth gap

To determine whether a physical layer is **actually short of deliverable supply today**, the report defines an absolute gap:

```text
AI_Capacity_Gap_i(t)
= AI_Effective_Demand_i(t)
- AI_Effective_Capacity_i(t)
```

where \(i\) represents physical layers such as advanced logic, HBM/DRAM, advanced packaging, networking, and power. Demand and capacity must use the **same delivery window, qualification/quality boundary, and physical unit**, such as wafers/month, qualified package starts/month, bits/year, or MW.

- **Absolute Gap > 0:** current deliverable supply is insufficient;
- **Absolute Gap ≈ 0:** current supply and demand are near balance;
- **Absolute Gap < 0:** current effective headroom exists.

To determine whether scarcity pressure is widening or converging, the report separately defines:

```text
AI_Capacity_Growth_Gap_i(t)
= Growth(AI_Effective_Demand_i(t))
- Growth(AI_Effective_Capacity_i(t))
```

The Growth Gap is a difference in growth rates over the same period, measured in percentage points. It describes the **direction of pressure**, not the current stock gap:

- **Growth Gap > 0:** scarcity may widen, or existing headroom may be eroded;
- **Growth Gap < 0:** scarcity may converge, or effective headroom may expand;
- **Growth Gap = 0:** supply and demand are changing at the same rate; it does not imply that no shortage exists.

A strong S4 Capital Hard Landing signal therefore requires **Absolute Gap < 0 / excess capacity** together with deterioration in utilization, clearing prices, and forward commitments—not a negative Growth Gap by itself.

AI Capacity Gap, AI Capacity Growth Gap, and Non-AI Residual Capacity answer different questions: the first two measure the current AI-side shortfall and its direction of change; NARC measures effective supply left for non-AI demand after priority allocation.

## 4. Memory is the clearest observed crowding-out path

Micron disclosed that HBM3E requires approximately **3× the wafer supply of DDR5** on the same technology node and for the same number of bits; TrendForce forecasts HBM + RDIMM at roughly **51% of 2026 DRAM bit supply**.[^ch03-3][^ch03-4]

That creates an observable memory-layer mechanism:

> HBM/RDIMM demand rises → wafer/cleanroom/capital shifts toward higher-value server products → conventional DDR/LPDDR residual supply changes → consumer/general-compute price and configuration pressure increases

The 51% figure is a 2026E bit-supply forecast. It is not an HBM-only share and not a wafer share.

## 5. PCs and Gaming: dual exposure to GPU allocation and memory residuals

NVIDIA's FY26 10-K reports Gaming revenue of roughly **US$16.0B, up 41% year over year**, while also stating that supply constraints were expected to be a headwind to Gaming in FY27 Q1 and beyond.[^ch03-5]

That is evidence of supply constraints on the gaming side, but it does not prove that every constraint was caused by Data Center allocation.

PCs also face a second channel: server/HBM demand changes DRAM product mix and therefore the residual supply of DDR5/LPDDR. PC economics can therefore be exposed simultaneously to GPU availability and memory pricing.

## 6. General servers: RDIMM sits inside the same high-value memory pool

General servers do not necessarily use HBM, but they consume large amounts of DDR5 RDIMM. TrendForce includes RDIMM and HBM together in its forward view of 2026 DRAM bit supply.[^ch03-4] This shows that traditional server memory is not a fully independent commodity river.

AI/server infrastructure expansion can therefore raise general-server cost through memory allocation even when the server itself does not use a frontier accelerator.

## 7. Smartphones: not displaced by AI, but competing under a new incremental-resource regime

TSMC's 2025 smartphone platform accounted for **29%** of annual net revenue and grew **11% year over year**; HPC accounted for **58%**.[^ch03-6]

This does not support the statement that "AI replaced smartphones." A more accurate description is:

- smartphone remains a very large demand platform;
- HPC has greater pull on incremental leading-edge investment;
- LPDDR / selected packaging / power-management resources can share upstream inputs with AI/server demand;
- flagship input cost and mid-range node-migration cadence become more exposed to residual-capacity pressure.

## 8. Automotive: slower and more selective exposure

Automotive semiconductors have long qualification cycles, high reliability requirements, and extensive mature-node usage. They do not compete directly with frontier AI across every layer.

The strongest overlap is more likely to appear in central compute, memory, power management, and selected advanced packaging. Automotive is therefore better described as a **second-stage selective transmission channel** rather than part of the first broad shortage wave.

## 9. Residual pressure usually appears first as an upgrade tax, not a production stop

When effective residual capacity falls, common corporate responses include:

1. raising prices;
2. reducing specifications;
3. delaying upgrades;
4. extending the use of mature nodes or alternative suppliers.

Supply-chain pressure is therefore more likely to appear first as higher flagship BOM cost, longer replacement cycles, slower diffusion of high-end features, and sharper product segmentation—not immediate shutdown of an entire industry.

## 10. China's parallel supply can change domestic residual structure without closing the frontier bottleneck

China's expansion in logic, DRAM, NAND, and terminal manufacturing can relieve part of the pressure in domestic consumer markets.

But substitution must still be analyzed by layer: consumer computing is relatively strong; general compute has partial alternatives; frontier AI still depends on advanced logic, HBM-class memory, advanced packaging, interconnect, and software closure.

Domestic consumer-supply growth can therefore improve local residual capacity without automatically removing the upstream bottlenecks of global frontier AI.

## 11. Real-economy firms face a second layer of AI adoption cost

Manufacturing and other operating companies adopting AI face not only hardware/input costs but also cloud inference, software integration, data pipelines, security/compliance, and workflow redesign.

The relevant productivity equation is:

> **Net productivity value = productivity gain − total AI adoption cost**

Upstream resource inflation and downstream AI-service cost can therefore affect the same company at the same time.

## 12. Current judgment and falsification

As of August 2026, the evidence is more consistent with:

> **selective transmission + product segmentation + Non-AI Residual Capacity pressure**

than with the claim that "AI is taking every chip."

The crowding-out thesis should be weakened if DDR/LPDDR pricing and supply become sustainably loose, consumer-GPU availability improves materially, smartphone/general-server upgrades no longer show shared-resource pressure, and memory/packaging product mix stops tilting toward AI/server demand.

## References

[^ch03-1]: TrendForce, 2026-01-05, CSP capacity locking and allocation pricing, https://www.trendforce.com/presscenter/news/20260105-12860.html
[^ch03-2]: TrendForce, 2026-03-31, allocation fulfillment and higher-price procurement by OEMs/module makers, https://www.trendforce.com/presscenter/news/20260331-12995.html
[^ch03-3]: Micron Technology, FY24 Q2 Prepared Remarks, 2024-03-20, HBM3E wafer-supply trade ratio versus DDR5, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^ch03-4]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^ch03-5]: NVIDIA Corporation, FY26 Form 10-K, U.S. SEC, Gaming revenue and supply-constraint disclosure, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
[^ch03-6]: TSMC, 4Q25 Presentation / 2025 full-year platform mix, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf


\newpage


# Part I · Chapter 4: TSMC, N2, and Advanced-Manufacturing Resource Allocation

## 1. The real competitive object is not a rumored "2 nm wafer price"

A frontier AI system simultaneously requires leading-edge logic, HBM, advanced packaging, substrates, interconnect, and power. Node leadership is only one necessary condition for entering the next-generation system race.

The core question in advanced manufacturing is therefore not a market-rumored wafer quote. It is:

> **Who can secure sufficient scale when N2/N2P/A16 and other next-generation resources enter volume production, while also matching memory, packaging, and system roadmaps?**

## 2. TSMC 2025 key facts

**Table 4.1 — TSMC 2025 capacity, technology, and platform-revenue structure**

| Metric | 2025 |
|---|---:|
| 12-inch-equivalent wafer shipments | ~15.0M |
| annual capacity | >17M |
| 3 nm wafer-revenue share | 24% |
| 5 nm | 36% |
| 7 nm | 14% |
| ≤7 nm | 74% |
| HPC platform | 58% of net revenue; +48% YoY platform growth |
| Smartphone platform | 29%; +11% YoY platform growth |
| largest / second-largest customer | 19% / 17% of annual revenue |

**Source:** TSMC 2025 Annual Report, 2025 Form 20-F, and 4Q25 Presentation.[^ch04-1][^ch04-2][^ch04-3]  
**Note:** Platform share and node share are revenue-based metrics. Customer revenue share cannot be converted into wafer, node, or CoWoS allocation.

These figures show that HPC became TSMC's largest platform while TSMC continued to serve a broad customer base. They do not support the claim that TSMC has become a dedicated fab for any one customer.

## 3. Customer revenue share cannot be converted into wafer / node / CoWoS share

The 2025 largest-customer share of 19% and second-largest-customer share of 17% are **annual-revenue ranking disclosures**.[^ch04-2]

They cannot be converted into N2 wafer share, 3 nm wafer share, CoWoS share, HPC wafer share, or physical wafer counts.

A different anonymized customer table supports year-over-year comparison: Customer A **12%→19%** and Customer B **22%→17%** from 2024 to 2025.[^ch04-4] The annual largest/second-largest ranking and the anonymized A/B series answer different questions and cannot be combined into a fictional longitudinal trajectory for one customer.

Likewise, HPC at 58% is a platform revenue share, not a wafer-shipment share.

## 4. N2's strategic value comes from incremental launch resources

N2 matters for more than transistor density. Competitors care about:

- timing of volume production;
- available scale;
- yield / delivery stability;
- HBM and packaging support;
- system-level performance conversion;
- roadmap continuity.

Access to a node does not automatically create a system victory. If memory, packaging, interconnect, or power are missing, complete-system delivery remains constrained.

## 5. AHICR is more useful for future allocation than historical revenue share

This report uses the **Advanced/HPC Incremental Capacity Capture Ratio (AHICR)** to analyze next-generation incremental resources:

> AHICR = incremental advanced AI/HPC resources captured by one buyer ÷ total industry increment in the corresponding resource

AHICR must be evaluated separately by physical layer—logic, HBM, packaging, and power. Different units cannot be added into one composite share.

50/60/70/80% are only D-grade scenario levels used to study nonlinear residual-capacity effects. They are not disclosed current customer shares.

## 6. TSMC allocation is not driven by one variable

Advanced-capacity allocation is more likely to reflect a combination of price, committed volume, contract duration, prepayment, credit quality, utilization certainty, roadmap stability, customer diversification, and geopolitical risk.

The deterministic claim that "the number-one customer gets all the best resources" is therefore not supportable.

A more defensible mechanism is that order scale, credit, prepayment, and roadmap certainty increase a buyer's bargaining power over incremental resources, while suppliers retain incentives to diversify customers, protect long-run bargaining power, and manage geopolitical risk.

## 7. Advanced Packaging must remain separate from the logic pool

TSMC first-party material confirms advanced-packaging tightness, but customer-level CoWoS allocation is not disclosed.[^ch04-5] TrendForce's estimate that NVIDIA represented more than 60% of 2025 CoWoS demand is B-grade institutional evidence.[^ch04-6]

The report-side **5.37 CoWoS wafers/rack** figure is a D-grade geometry stress test, not a TSMC yield figure, and it cannot be used to divide TSMC's roughly 15M annual front-end wafer shipments.

This is why "leading-edge logic available" and "complete AI system deliverable" are different questions.

## 8. Samsung / SMIC foundry share is not equivalent to frontier substitution

TrendForce estimates 1Q26 foundry revenue shares at roughly **72% for TSMC**, **6.5% for Samsung Foundry (excluding System LSI)**, and **5.1% for SMIC**.[^ch04-7]

These are revenue shares, not frontier-AI capacity shares. A second supply system capable of substitution must also prove node performance, yield, advanced packaging, the HBM ecosystem, customer qualification, and software/system integration.

"Another foundry exists" and "a complete second frontier-AI supply stack exists" are therefore different propositions.

## 9. Current judgment

TSMC's strategic position rests on three conditions that currently coexist: strong leading-edge logic, HPC as its largest platform, and advanced packaging as a publicly confirmed growth constraint.

The key forward variables are not one quarter's customer revenue shares, but the customer structure of N2/N2P/A16 incremental resources, HBM / packaging supply, competition from cloud custom silicon for new capacity, and whether a second manufacturing system can produce a combined logic + packaging + memory alternative.

## References

[^ch04-1]: TSMC, 2025 Annual Report, https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^ch04-2]: Taiwan Semiconductor Manufacturing Company Limited, 2025 Form 20-F, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm
[^ch04-3]: TSMC, 4Q25 Presentation / 2025 full-year platform and technology mix, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
[^ch04-4]: TSMC, 2025 Consolidated Report, anonymized Customer A/B revenue series, https://www.sec.gov/Archives/edgar/data/1046179/000104617926000024/a2025q4consolidatedreport-.htm
[^ch04-5]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging tightness, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^ch04-6]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^ch04-7]: TrendForce, 2026-06-12, 1Q26 foundry revenue shares, https://www.trendforce.com/presscenter/news/20260612-13095.html


\newpage


# Part I · Chapter 5: HBM and the Restructuring of Memory Resources

## 1. HBM has moved from a GPU component to a system-level resource

In frontier AI systems, HBM affects model capacity, batching, context length, concurrency, communication patterns, and accelerator utilization. The official GB200 NVL72 configuration includes **13.4 TB of HBM3E per rack**,[^ch05-1] showing that once the purchasing unit moves to rack scale, memory demand also moves from "GB per GPU" to "PB per deployment."

HBM therefore affects more than the accelerator BOM. It propagates into DRAM wafer allocation, cleanroom space, advanced packaging, memory-vendor product mix, and the residual supply of conventional DRAM.

## 2. Micron's ~3× disclosure is the most important current first-party physical anchor

Micron's FY24 Q2 prepared remarks provide a clear boundary: at the **same technology node and for the same number of bits**, HBM3E requires approximately **3× the wafer supply of DDR5**.[^ch05-2] Micron's FY25 10-K further confirms that producing the same number of HBM bits requires more wafers and cleanroom space.[^ch05-3]

This evidence supports the following conclusions:

- HBM3E consumes more manufacturing input per bit than DDR5;
- HBM expansion places greater pressure on DRAM wafer / cleanroom input;
- effective residual capacity for conventional DRAM can face stronger pressure.

It does **not** mean that HBM is priced at 3× DDR5, nor can it be treated as an immutable "3:1 law" for every fab and every HBM generation. Micron's public statement on HBM4 is only that the trade ratio is expected to rise further; a specific HBM4/HBM4E ratio still requires future vendor disclosure.

## 3. 51% is a 2026E DRAM bit-supply forecast, not HBM actuals

TrendForce **forecasts** that **HBM + RDIMM together will account for roughly 51% of 2026 DRAM bit supply**.[^ch05-4] This B-grade institutional forecast must retain three boundaries:

1. the 51% includes **HBM and RDIMM** and cannot be rewritten as "51% of DRAM is HBM";
2. it is a **bit-supply** share, not a wafer share;
3. it is a **2026E forecast**, not completed full-year actuals.

Combined with Micron's same-bit wafer trade ratio, this creates a more important mechanism: **bit share does not fully capture manufacturing-input pressure.** When a high-value bit requires more wafer and cleanroom input, its impact on manufacturing resources can exceed its share of bits.

## 4. How Non-AI Residual Capacity forms in memory

Memory reallocation can be expressed as a clear transmission chain:

**AI/server memory demand rises → HBM/RDIMM mix rises → wafer / cleanroom / packaging input shifts toward high-value products → conventional DDR/LPDDR residual capacity tightens → non-AI end markets face greater price and configuration pressure.**

The key variable is not total global DRAM capacity. It is the effective supply actually left for consumer electronics and other traditional workloads after AI/server demand has absorbed the priority resources.

This is why the report uses **Non-AI Residual Capacity** as the central memory metric rather than treating gross DRAM-capacity growth as proof that traditional markets have returned to abundance.

## 5. SK hynix FY25 results show that HBM has changed product economics

SK hynix reported FY25 revenue of **KRW97.1467T**, operating profit of **KRW47.2063T**, operating margin of **49%**, and net income of **KRW42.9479T**, while stating that HBM revenue more than doubled year over year.[^ch05-5]

These figures do not prove that HBM alone generated all profit, but they are sufficient to show that high-value memory product mix has materially improved memory-vendor economics. Conventional server memory remains important as well, reinforcing the point that HBM and DDR5/RDIMM are not fully isolated capital and manufacturing systems.

## 6. HBM supply is concentrated, but this report does not invent a precise share table

High-end HBM supply is concentrated primarily among SK hynix, Samsung, and Micron. The barriers are not just DRAM-fab CapEx. They also include:

- TSV / stacking;
- yield learning;
- advanced-packaging integration;
- customer qualification;
- generation timing;
- high-volume manufacturing stability.

Public first-party material is insufficient to construct a fully comparable and auditable three-vendor HBM market-share table. This report therefore does not upgrade media or sell-side estimates into company-official share data.

### 6.1 Price feedback: HBM resource pull is not infinitely one-directional

Resource reallocation contains a price-feedback mechanism. TrendForce's June 2, 2026 model estimate found that after conventional DRAM prices rose sharply from the second half of 2025, **DDR5 64GB RDIMM per-wafer revenue exceeded HBM in 1Q26**; the same research estimated HBM profitability below that of DDR5 64GB RDIMM.[^ch05-6]

This is B-grade institutional estimation, not product-level realized gross-margin disclosure from Samsung, SK hynix, or Micron. Its analytical value is the self-correcting mechanism it reveals:

> HBM/AI demand rises → conventional-DRAM residual supply tightens → DDR5/RDIMM prices rise → conventional-DRAM per-wafer economics improve → the relative incentive for further HBM conversion declines → memory vendors rebalance product mix.

AI Resource Gravity is therefore not an infinitely one-way pump. Long-run allocation depends on risk-adjusted return per scarce manufacturing input, qualification, yield, generation transitions, and customer-contract structure.

## 7. Rack-scale demand can support scenario arithmetic, not fake shipment estimates

Using the GB200 NVL72 product specification of **13.4 TB HBM3E/rack**[^ch05-1], we can run order-of-magnitude stress tests:

**Table 5.1 — GB200 NVL72 rack count and HBM3E scenario demand**

| Scenario rack count | HBM3E demand |
|---:|---:|
| 1,000 | 13.4 PB |
| 10,000 | 134 PB |
| 30,000 | 402 PB |
| 50,000 | 670 PB |

**Source:** NVIDIA GB200 NVL72 official specification; report scenario arithmetic.[^ch05-1]  
**Note:** Rack count is a D-grade assumption. The PB figures are not actual shipments or consumption.

These are **D-grade scenario-demand calculations**. NVIDIA does not disclose annual rack shipments that can be multiplied directly by this specification, and memory vendors do not disclose customer-level annual HBM bits mapped one-for-one to these racks. Neither 50,000 racks nor 670 PB may therefore be presented as actual consumption.

## 8. HBM4 increases cross-layer capital density without justifying a fabricated fixed multiple

The complexity of next-generation HBM comes not only from higher stack counts. It can also involve logic base dies, advanced foundry processes, packaging, testing, and qualification.

If logic base dies use more advanced processes, the memory bottleneck extends further into foundry and packaging:

**HBM vendor → logic base die → advanced foundry → advanced packaging → accelerator qualification**

HBM can therefore evolve from a "memory bottleneck" into a system bottleneck spanning memory, foundry, and packaging. Before vendors formally disclose the data, however, HBM3E's ~3× ratio cannot be mechanically rewritten as 4× or 5× for HBM4, and one 12-Hi or 16-Hi configuration cannot be treated as the universal HBM4 production standard.

## 9. HBM's inventory properties differ from a standard commodity

One important difference between HBM and standard commodity memory is generation-specific qualification. Product generations move quickly, they are closely tied to accelerator generations, qualification cycles are long, and obsolescence risk is higher.

The industry can therefore experience:

> **looser supply in an older HBM generation while the next frontier generation remains constrained.**

Oversupply in one generation does not automatically solve qualification, yield, and packaging constraints in the next.

## 10. Moving inference toward DDR does not automatically escape the memory constraint

Some inference workloads can trade bandwidth for lower-cost DDR/LPDDR, but frontier inference still faces KV-cache, long-context, large-batch, MoE-routing, low-latency serving, and multi-accelerator communication constraints.

More importantly, RDIMM is already included in TrendForce's forward AI/server memory structure. Shifting some workloads from HBM toward DDR5 therefore changes the cost/bandwidth tradeoff inside a broader shared memory-resource pool rather than creating a completely independent supply river.

## 11. What would weaken HBM's long-run strategic value

HBM scarcity is not inevitable. The current mechanism would weaken materially if:

- memory architecture sharply reduces dependence on high-bandwidth stacked memory;
- algorithmic efficiency persistently lowers memory bandwidth / capacity demand;
- the HBM wafer/cleanroom trade ratio improves materially;
- stacking, yield, logic-base, and advanced-packaging supply elasticity rises sharply;
- conventional DRAM and HBM manufacturing resources become much more decoupled.

The long-run claim is therefore not "HBM will always be scarce." It is:

> **As long as frontier-system bandwidth demand grows faster than HBM supply elasticity and manufacturing input per bit remains materially above conventional DRAM, HBM will remain a core scarce layer of AI infrastructure.**

## References

[^ch05-1]: NVIDIA, “GB200 NVL72,” official product page, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^ch05-2]: Micron Technology, FY24 Q2 Prepared Remarks, 2024-03-20, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^ch05-3]: Micron Technology, FY25 Form 10-K, HBM wafer and cleanroom requirements, U.S. SEC, https://www.sec.gov/Archives/edgar/data/723125/000072312525000028/mu-20250828.htm
[^ch05-4]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^ch05-5]: SK hynix, FY25 Financial Results, https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
[^ch05-6]: TrendForce, 2026-06-02, per-wafer revenue comparison for HBM and DDR5 64GB RDIMM, https://www.trendforce.com/presscenter/news/20260602-13074.html


\newpage


# Part I · Chapter 6: Advanced Packaging, CoWoS, and the System-Delivery Bottleneck

## 1. Advanced packaging has become a system-delivery layer, not a supporting afterthought

Frontier AI accelerators increasingly depend on multi-die integration, HBM, large interposers, and high-speed die-to-die connections. Advanced packaging is no longer merely a downstream step after chip fabrication. It has become:

> **a scarce manufacturing layer that can determine how many complete frontier AI systems can actually be delivered.**

This explains an apparently contradictory state: foundry logic-wafer capacity can keep expanding while complete-system delivery remains constrained by insufficient packaging/HBM integration.

## 2. TSMC has confirmed tightness, but year-specific disclosure labels must remain separate

TSMC's public statements are sufficient to establish advanced-packaging tightness:[^ch06-1][^ch06-2]

- 4Q24: management described relevant capacity as **very tight** and unable to satisfy all customer demand;
- 2Q26: management stated more directly that packaging capacity was **so tight that now it limits my customers' growth**.

Revenue disclosures must retain their original year-specific labels:

- 4Q24 transcript: **advanced packaging and testing >8% of revenue**;
- 4Q25 transcript, using the company's corrected wording: **advanced packaging slightly over 10% of 2025 revenue**.[^ch06-6]

These labels are not perfectly identical. This report therefore does **not** treat >8% → >10% as a strict same-denominator time series, nor does it rewrite the 2025 "advanced packaging" figure back into "advanced packaging + testing."

## 3. CoWoS tightness is A-grade fact; customer allocation is not disclosed

TSMC public material supports the following: advanced packaging is tight, CoWoS is an important part of that system, and packaging tightness is limiting customer growth.

TSMC does not disclose an auditable customer-level CoWoS allocation table for this report, nor does it provide an official CoWoS share by customer.

Two questions therefore have to remain separate:

- **A-grade fact:** packaging / CoWoS tightness;
- **not disclosed:** exactly how much CoWoS capacity each customer receives.

Annual customer revenue share, wafer revenue share, and CoWoS customer share are not interchangeable.

## 4. NVIDIA >60% of CoWoS demand is a B-grade institutional anchor

TrendForce's research on 2025 CoWoS demand identifies NVIDIA as the largest demand customer and estimates its demand share at **more than 60%**.[^ch06-3]

The evidence grade must remain **B — institutional estimate**. The figure is useful for analyzing demand concentration and designing stress tests, but it cannot be rewritten as:

- TSMC officially confirming that NVIDIA received >60% of allocation;
- >60% being a 2026 actual;
- NVIDIA possessing exclusive CoWoS rights.

The correct use is: **highly concentrated demand has a real institutional anchor, while actual allocation still awaits first-party disclosure.**

## 5. 5.37 CoWoS wafers/rack is a D-grade geometry stress test

This report uses an order-of-magnitude geometry model:

72 GPU packages ÷ approximately 13.4 packages/wafer ≈ **5.37 CoWoS wafers/rack**. The 72-GPU input comes from NVIDIA's official NVL72 specification.[^ch06-4]

The inputs are:

- 72 GPUs from the official NVL72 specification;[^ch06-4]
- ~13.4 packages/wafer as a report-side geometry assumption;
- therefore, 5.37 as a **D-grade stress test**.

It is **not** TSMC disclosed yield, actual wafer starts, logic-wafer demand, or customer allocation.

This distinction matters because advanced-packaging wafers and TSMC's annual 12-inch-equivalent wafer shipments are not the same physical capacity pool.

## 6. Why total foundry wafer shipments cannot be divided by 5.37

TSMC shipped roughly **15.0M 12-inch-equivalent wafers** in 2025 across smartphones, HPC, automotive, IoT, mature nodes, and many other front-end products.[^ch06-7] The 5.37 figure is a report-side geometry stress test for **CoWoS packaging wafers per rack**.

The following calculation is physically invalid:

> total annual fab wafer shipments ÷ 5.37 = number of AI racks producible

It mixes the front-end logic wafer pool with the back-end advanced-packaging pool. Any resulting six-figure or million-rack number is not a fact about system-delivery capacity.

Likewise, front-end logic wafers/rack and back-end CoWoS wafers/rack cannot be added into one "TSMC wafers consumed per rack" metric. They sit in different manufacturing stages and capacity pools.

## 7. Why packaging can become the quantity gate before the node does

Leading-edge logic supply can grow through new fabs, process migration, and capacity expansion. Advanced packaging simultaneously depends on tools, interposers, substrates, testing, process flows, HBM integration, and qualification.

The result is:

> **logic wafer available ≠ system deliverable**

Advanced nodes are closer to an entry ticket into a frontier system; advanced packaging can become the quantity gate that determines how many complete systems are delivered. Both matter, but their physical units and expansion clocks are different.

## 8. Incremental Capacity Capture should be modeled as scenarios, not fabricated current shares

If incremental packaging capacity is C and one platform captures a share s, the residual increment available to other buyers is:

> **Residual = (1 − s) × C**

**Table 6.1 — Residual sensitivity under incremental packaging-capacity capture**

| Assumed capture rate | Residual for other buyers |
|---:|---:|
| 50% | 50% |
| 60% | 40% |
| 70% | 30% |
| 80% | 20% |

**Source:** Report D-grade scenario model.  
**Note:** Capture rates are not current TSMC customer-allocation facts; they are sensitivity inputs for studying concentration of incremental resources.

These 50/60/70/80% values are **D-grade scenario levels**, not TSMC's current customer allocation.

The model's purpose is to show nonlinearity: if a leading buyer consistently captures a larger share of **incremental** resources, the capacity left for second- and third-tier buyers can contract quickly even while total industry packaging capacity continues to grow.

## 9. Cloud custom silicon does not automatically bypass packaging/HBM

Google, AWS, Microsoft, and Meta custom accelerator systems can divert part of NVIDIA's platform profit, but their next-generation systems still rely heavily on advanced logic, HBM, and high-density integration.

Two effects can therefore coexist:

1. **platform substitution:** in-house cloud systems reduce dependence on the full NVIDIA platform;
2. **upstream competition:** those same systems increase demand for the same advanced manufacturing, HBM, and packaging resources.

More custom silicon does not automatically mean lower CoWoS/HBM pressure.

## 10. Bottleneck location is not the same as profit location

Advanced packaging can be the system-delivery bottleneck without having the highest margin in the value chain. TSMC management stated in 2Q24 that advanced-packaging gross margin had historically been significantly below corporate average and was approaching, but had not yet reached, the company average.[^ch06-5]

Physical bottlenecks and profit pools therefore have to remain separate:

- packaging may determine **whether the system can be delivered**;
- the system platform can still capture stronger economics through software, interconnect, integration, and customer switching costs.

> **bottleneck location ≠ profit location**

This distinction is essential for AI-infrastructure value-capture analysis.

## 11. Packaging is also an independent closure gate for China's Parallel Stack

A frontier AI parallel stack cannot be judged from logic nodes alone. Even if accelerator dies can be produced, insufficient advanced packaging, substrates, HBM integration, testing, or high-volume yield can still prevent stable delivery of large systems.

"Domestic chip production" therefore cannot hide packaging as an independent physical layer. China system closure must validate logic, HBM, packaging, interconnect, software, and power separately.

## 12. Current judgment and falsification

As of August 2026, the most defensible conclusions are:

- TSMC has confirmed advanced-packaging tightness with first-party evidence;
- TrendForce provides a B-grade institutional anchor for highly concentrated NVIDIA CoWoS demand;
- customer-level allocation remains undisclosed by TSMC;
- 5.37 wafers/rack is only a D-grade geometry stress test;
- custom silicon can still compete for the same upstream scarce resources.

The judgment that advanced packaging is a core scarce layer should be weakened if TSMC stops describing packaging as a growth constraint, lead times fall materially, customer-level allocation becomes more distributed, and HBM/packaging supply elasticity continues to improve.

## References

[^ch06-1]: TSMC, 4Q24 Earnings Conference Transcript, advanced packaging and testing >8% of revenue; capacity “very tight,” https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf
[^ch06-2]: TSMC, 2Q26 Earnings Conference Transcript, packaging capacity limiting customer growth, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^ch06-3]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^ch06-4]: NVIDIA, “GB200 NVL72,” official product page, 72 Blackwell GPUs per rack, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^ch06-5]: TSMC, 2Q24 Earnings Conference Transcript, advanced-packaging margin relative to corporate average, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2024-08/5122725a56670882d777a8e8bfe0ed247cc55330/TSMC%202Q24%20Transcript.pdf
[^ch06-6]: TSMC, 4Q25 Earnings Conference Transcript, corrected 2025 advanced-packaging revenue identity, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
[^ch06-7]: TSMC, 2025 Annual Report, annual wafer shipments and manufacturing footprint, https://investor.tsmc.com/static/annualReports/2025/english/index.html


\newpage


# Part I · Chapter 7: From 120 kW Racks to GW-Scale Power Constraints

## 1. Why power has moved from operating cost to infrastructure quota

Once rack-scale AI systems reach roughly **120 kW/rack**, electricity is no longer merely an operating expense. It becomes a constraint on whether systems can be deployed and utilized on schedule.[^ch07-1]

NVIDIA's official documentation for GB200/GB300 NVL72-class racks gives an approximately **120 kW/rack** full-rack power figure. A clearly labeled **D-grade scenario calculation** is therefore:

> 500 racks × 120 kW/rack = **60 MW of rack-level full-load power**

This is an order-of-magnitude calculation. It does not mean any specific campus has deployed 500 racks, and it does not include complete facility overhead. What it demonstrates is that deployments measured in hundreds of racks quickly create local loads measured in tens of MW, pulling substations, transmission, permitting, cooling, and firm generation into the delivery chain.

The critical physical layers of AI infrastructure therefore extend beyond wafers, HBM, and advanced packaging to include **powered land / grid interconnection / substations / firm MW / cooling**.

## 2. Power analysis requires a state machine, not headline-GW addition

Power projects should be separated into at least five states:

> **Announced → Contracted → Permitted → Energized → Utilized**

A 1 GW PPA cannot be rewritten as "1 GW of AI compute online." A 500 MW development target cannot be converted directly into an active rack count. The real economic value of a project depends on how far it has advanced from announcement toward high-utilization delivery—not on the maximum MW/GW in a headline.

## 3. Three representative paths operate on very different clocks

### 3.1 Microsoft / Constellation: restarting an existing ~835 MW nuclear asset

Microsoft and Constellation entered a **20-year PPA** supporting the restart of the former Three Mile Island Unit 1 as the Crane Clean Energy Center, with an approximately **835 MW** public capacity anchor.[^ch07-2]

The case shows how hyperscaler demand can support a large existing power asset returning to service.

But 835 MW is a project / unit-capacity anchor, not evidence that 835 MW is already being delivered in real time to AI data centers. The project still sits on regulatory, repair, restart, interconnection, and commercial-operation clocks.

Constellation's official release states that the restart requires significant investment but does **not** disclose a US$1.6B restart CapEx figure. That number therefore does not enter this chapter's fact layer.

### 3.2 Talen / AWS: a revised PPA of up to 1,920 MW

The Talen/AWS revised PPA has a full contract quantity of **up to 1,920 MW** and runs through 2042.[^ch07-3]

Talen's 2026 Q2 10-Q states that the transition to the revised AWS PPA **occurred in April 2026**. An earlier 2025 10-K had stated that **full transition was expected in spring 2027**.[^ch07-3][^ch07-4]

April 2026 can therefore be used as the current disclosed status of the revised-PPA transition. It **cannot** be interpreted as proof that every physical conversion, transmission modification, and full-delivery step had already been completed.

The relevant forward indicators are the capacity ramp, energized MW, AWS load, and utilization.

This case shows that regulation and commercial structure can change the delivery path for power without making large-scale AI electricity demand disappear.

### 3.3 Google / Kairos: 50 MWe in 2030 and up to 500 MWe by 2035

The Google/Kairos public timeline is much longer: **Hermes 2 up to 50 MWe in 2030**, followed by a fleet of **up to 500 MWe by 2035**.[^ch07-5]

This is better understood as a long-duration supply option, industrial-learning path, and capacity hedge than as spot power that can be called on in 2026–2028.

The near-term value of SMRs therefore lies mainly in future optionality; they should not be used to erase today's interconnection, transformer, and powered-site constraints.

## 4. These three projects cannot be added into "3.255 GW of active AI power"

Mechanically adding approximately 835 MW, up to 1.92 GW, and up to 500 MWe produces a nominal total but not a usable AI-load number.

**Table 7.1 — Nominal scale and delivery state of three AI-power pathways**

| Project | Nominal scale | Primary status |
|---|---:|---|
| Crane / Microsoft | ~835 MW | restart + regulatory process |
| Talen / AWS | up to 1,920 MW | revised-PPA transition / ramp |
| Kairos / Google | 50 MWe in 2030; up to 500 MWe by 2035 | long-duration development |

**Source:** Constellation, Talen Energy, and Kairos Power / Google.[^ch07-2][^ch07-3][^ch07-4][^ch07-5]  
**Note:** The nominal capacities sit at different contract, permitting, construction, energization, and utilization states and must not be mechanically added into active AI load.

The three paths represent restarting an existing large generator, restructuring the commercial/grid relationship between a large load and existing generation, and developing next-generation nuclear supply. Their technology maturity, permitting clocks, and utilization dates are not comparable.

## 5. Grid queues are evidence of congestion, not a measure of "AI power shortage"

Berkeley Lab's Queued Up data show that active U.S. generation/storage interconnection requests peaked near **2,600 GW at the end of 2023** and stood at approximately **2,061 GW at the end of 2025**.[^ch07-6]

These numbers cannot be converted into "the United States lacks 2,061 GW of data-center power." The queue is primarily generation/storage projects and includes projects that may withdraw, duplicate one another, or experience long delays.

The narrower supported conclusion is that **interconnection and transmission buildout can take years, making Time-to-Power a real constraint.**

What matters for AI system delivery is how many MW a specific region can actually deliver inside a specific hardware-generation window—not the total GW sitting in a national queue.

## 6. Time-to-Power is becoming a system-competition variable

Advanced chips can advance on monthly and quarterly product clocks. Power infrastructure often advances on multi-year clocks.

That creates a variable comparable in importance to the chip roadmap:

> **Time-to-Power**

Projects with existing grid interconnection, powered land, substation / transformer capacity, firm generation, and executable permitting paths gain a timing advantage.

Hyperscaler competition is therefore not only about who acquires more accelerators. It is also about an **illustrative deployment-scale question**:

> **who can energize the next 50 MW / 100 MW / 500 MW of systems sooner.**

The 50 / 100 / 500 MW values are scenario-scale markers used to illustrate Time-to-Power; they are not disclosed project capacities.

## 7. Power and semiconductor bottlenecks can rotate

AI infrastructure does not have one permanent bottleneck.

One possible **Rolling Bottleneck Cascade** is:

> HBM / advanced packaging tight → hardware delivery constrained → manufacturing supply expands → more racks reach sites → power / interconnection becomes binding → deployment and utilization slow → next-cycle hardware orders / commitments decelerate

The reverse is also possible. If power infrastructure is built far ahead of workload demand, the problem can shift from scarcity to low utilization and weak capital returns.

"Power is now a core constraint" and "power is not yet the sole dominant bottleneck" can therefore both be true.

## 8. Power contracts and hardware operate on mismatched durations

AI servers have shorter technological and economic lives than major power assets and long-duration PPAs.

Crane involves a **20-year PPA**, while compute hardware will turn over much faster.[^ch07-2] This creates a classic duration mismatch:

> **shorter-cycle compute asset vs. longer-cycle power / infrastructure asset**

In high-demand scenarios, long-duration power access can be a moat. In S4 Capital Hard Landing, the same long-duration obligation can become a burden.

Power contracts therefore need to be evaluated through duration, ramp, take-or-pay / cancellation terms, project execution, utilization, and residual value.

## 9. What evidence would show that power has become the dominant bottleneck

Power should be upgraded from "one of the core constraints" to "the dominant constraint" only if several signals appear together:

- major buyers repeatedly disclose power/interconnection as the binding growth ceiling;
- delivered hardware sits idle waiting to be energized;
- energized capacity persistently lags deployment plans;
- next-generation orders are delayed by power constraints;
- Time-to-Power remains a decisive differentiator for high-value powered sites;
- utilization and capital returns deteriorate systematically because of power-delivery timing.

As of August 2026, public evidence supports a narrower conclusion:

> **Power has joined HBM and advanced packaging as a core physical constraint, but the evidence is not yet sufficient to show that power alone dominates the entire AI-infrastructure expansion rate.**

## References

[^ch07-1]: NVIDIA, DGX GB200 Hardware Guide, rack power approximately 120 kW, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
[^ch07-2]: Constellation, Crane Clean Energy Center / Microsoft 20-year PPA and approximately 835 MW unit, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
[^ch07-3]: Talen Energy, 2026 Q2 Form 10-Q, revised AWS PPA transition and up to 1,920 MW, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
[^ch07-4]: Talen Energy, 2025 Form 10-K, expected full transition timing, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
[^ch07-5]: Kairos Power / Google partnership, Hermes 2 up to 50 MWe in 2030 and fleet up to 500 MWe by 2035, https://www.kairospower.com/google
[^ch07-6]: Lawrence Berkeley National Laboratory, “Queued Up” 2026 update, active interconnection queue, https://emp.lbl.gov/news/backlog-power-plants-seeking-transmission-grid-connection-eased-somewhat-2025-amidst


\newpage


# Part I · Chapter 8: Quantitative Framework for AI Infrastructure and the Rolling Bottleneck Cascade

## 1. The purpose of quantification is not to manufacture false precision

The most common quantitative error in AI-infrastructure research is to connect different physical pools, accounting categories, and evidence grades into one apparently complete but unauditable total model.

This report allows four classes of quantitative work into the main argument:

1. **Compute / memory intensity**;
2. **Rack-scale material demand**;
3. **Explicit packaging / power stress tests**;
4. **Capacity / commitment / utilization indicators**.

Any link that cannot be closed with public data remains a parameter rather than being filled with an invented point estimate.

## 2. Roofline: why frontier inference cannot be compared through FLOPS alone

The core Roofline relationship is:

> **Performance = min(Peak Compute, Memory Bandwidth × Arithmetic Intensity)**

The critical arithmetic intensity is:

> **I_critical = Peak Compute / Memory Bandwidth**

When workload arithmetic intensity falls below the critical threshold, the system becomes memory-bound.

Autoregressive inference repeatedly reads model state, KV cache, routing, and activation data. Actual token throughput can therefore remain constrained by HBM bandwidth and memory movement even when accelerator peak FLOPS are very high.

This is why HBM, interconnect, and compute have to be analyzed as one system rather than interpreting frontier inference from peak compute alone.

## 3. Algorithmic architecture changes the demand function without deleting physical constraints

First-party anchors from the DeepSeek-V3 Technical Report include:[^ch08-1]

- 671B total parameters;
- 37B activated parameters;
- 14.8T pre-training tokens;
- **2.664M H800 GPU-hours for pre-training**;
- **2.788M H800 GPU-hours for full formal training**.

DeepSeek-V2 separately reports, relative to DeepSeek 67B:[^ch08-2]

- approximately **93.3% KV-cache reduction**;
- approximately **5.76× maximum generation throughput**.

These results belong to different model versions and must not be mixed.

Their shared methodological implication is that architecture can change bytes/token, activated compute, communication patterns, and serving concurrency. It therefore changes the demand function for HBM, networking, and compute.

But a changed demand function does not eliminate physical constraints. Whether higher efficiency reduces aggregate infrastructure demand still depends on workload volume and demand elasticity.

## 4. Formal-training compute conversion is not full R&D cost

DeepSeek-V3 reports **2.788M H800 GPU-hours** for full formal training, and the paper uses a **US$2/GPU-hour** rental-cost assumption.[^ch08-1]

A clearly labeled **D-grade arithmetic conversion** is therefore:

> **2.788M × US$2 ≈ US$5.576M**

This is only a formal-training compute conversion. It excludes research iteration, failed runs, data engineering, engineering payroll, cluster depreciation, networking, storage, and the post-training ecosystem.

The US$5.576M figure can therefore be used as a public training-run scale anchor, but not as "the full company cost of one frontier model."

## 5. Rack-scale BOM can be quantified; rack shipment cannot be invented

The official GB200 NVL72 configuration is:[^ch08-3]

- 72 Blackwell GPUs;
- 36 Grace CPUs;
- 13.4 TB HBM3E;
- 17 TB LPDDR5X.

If a scenario contains R racks:

> **HBM(R) = 13.4 TB × R**

> **LPDDR(R) = 17 TB × R**

**Table 8.1 — NVL72 rack count and HBM/LPDDR scenario demand**

| Scenario rack count | HBM3E | LPDDR5X |
|---:|---:|---:|
| 1,000 | 13.4 PB | 17 PB |
| 10,000 | 134 PB | 170 PB |
| 30,000 | 402 PB | 510 PB |
| 50,000 | 670 PB | 850 PB |

**Source:** NVIDIA official GB200 NVL72 specification; report scenario arithmetic.[^ch08-3]  
**Note:** Rack count is an assumed input; the PB values are not actual shipments or consumption.

These are **D-grade scenario calculations**.

NVIDIA does not disclose an annual NVL72 rack-shipment figure that can be multiplied by these specifications. It is therefore invalid to divide Data Center revenue by an invented rack ASP and propagate the resulting hypothetical rack count into "actual" HBM, CoWoS, or power consumption.

## 6. The HBM trade ratio amplifies bit-demand pressure on wafer input

Micron FY24 Q2 prepared remarks provide an important first-party boundary:

> **industrywide / same technology node / same number of bits**, HBM3E requires approximately **3× the wafer supply of DDR5**.[^ch08-4]

Bit demand and manufacturing input are therefore not one-to-one. As HBM bit share rises, pressure on DRAM wafer / cleanroom input can rise faster than bit share alone would suggest.

The 3× figure is not a fixed Micron-fab MES constant and cannot be mechanically extrapolated into a permanent HBM4/HBM5 ratio.

## 7. Packaging geometry can support sensitivity analysis, not shipment claims

The report uses approximately **5.37 CoWoS wafers/rack** as a D-grade geometry stress test:

> **72 packages ÷ 13.4 packages/wafer ≈ 5.37 wafers/rack**

The 13.4 packages/wafer denominator is a report-side geometry assumption, not a TSMC disclosed yield or packages-per-wafer metric.

The 5.37 figure may therefore be used for:

- packaging-demand order of magnitude;
- scenario comparison;
- bottleneck sensitivity.

It cannot be used to divide TSMC annual front-end wafer shipments, infer actual Blackwell shipments, or derive customer allocation.

## 8. Power must also be quantified with state and physical boundaries

Approximately **120 kW/rack** can be used as a rack-level power-density input.[^ch08-5]

Using 500 racks as a scenario input, a **D-grade arithmetic calculation** is:

> 500 racks × 120 kW = **60 MW of rack-level full-load power**

This calculation does not include complete facility overhead and does not mean any specific campus has deployed 500 racks.

Power must also retain its state identity:

> Announced → Contracted → Permitted → Energized → Utilized

Contracted MW is not energized MW; energized MW is not highly utilized AI load.

## 9. When shipment cannot be closed, Forward Commitment is more useful than an invented shipment model

NVIDIA's disclosed manufacturing, supply, and capacity commitments progressed as follows:[^ch08-6]

- 2026-01-25: **US$95.2B**;
- 2026-04-26: **US$119B**;
- 2026-07-26: **US$279B**.

The FY27 Q2 10-Q states that the latest commitments are primarily associated with memory and manufacturing facilities required for data-center infrastructure systems.

The figure cannot identify how much goes to any individual supplier, but it is an observable proxy for future resource-reservation intensity.

When customer-level HBM bits, CoWoS allocation, and rack shipment are unavailable, forward commitments are more informative than "revenue divided by an invented rack price."

## 10. AHICR: measure incremental capture separately for every scarce layer

The report uses the **Advanced/HPC Incremental Capacity Capture Ratio (AHICR)**:

> **AHICR(layer) = incremental advanced AI/HPC resource captured by one buyer ÷ total industry increment in that physical layer**

AHICR must be observed separately for:

- advanced logic;
- HBM;
- advanced packaging;
- power.

These units cannot be added into one universal "resource ownership" percentage.

The value of AHICR is to test whether next-generation incremental resources are increasingly captured by a small number of buyers—not to reinterpret historical revenue share as future allocation.

## 11. Five risk classes should be separated before testing for cascade

System risk in AI infrastructure can be divided into:

1. **Physical bottleneck:** logic / HBM / packaging / interconnect;
2. **Power bottleneck:** grid / substation / permit / cooling;
3. **Capital / utilization risk:** asset utilization fails to cover depreciation, power, operations, and financing;
4. **System-substitution risk:** cloud custom stacks / open software change platform economics;
5. **Regulatory / geopolitical risk:** export controls, supply interruption, interface remedies, regional fragmentation.

One risk does not equal an industry-wide crisis. The more dangerous state is when several clocks begin to reinforce one another.

## 12. Rolling Bottleneck Cascade

AI-infrastructure bottlenecks rotate rather than remaining permanently fixed at one layer.

A positive expansion cascade can look like:

> HBM / packaging tight → hardware delivery constrained → supply expands → more racks reach sites → power / interconnection becomes binding → utilization becomes the next constraint

A reverse capital cascade can look like:

> power delay → utilization decline → buyer ROI decline → next CapEx slows → hardware orders slow → HBM / packaging tightness eases → upstream CapEx slows

This is the **Rolling Bottleneck Cascade**.

It explains why easing HBM does not prove that AI infrastructure has no constraints, and why power becoming a bottleneck does not mean semiconductor constraints have disappeared permanently.

## 13. Capital return must place all duration clocks into one equation

A minimal economic relationship is:

> **Economic Return = Revenue from deployed compute − Depreciation − Power − Operations − Financing**

The core risk is duration mismatch: hardware can turn over rapidly while data-center shells, grid assets, PPAs, and debt remain in place for much longer.

A technically functional system can therefore produce weak capital returns if utilization is low or long-duration obligations are excessive.

## 14. Quantitative guardrails

The full report maintains the following hard boundaries:

- revenue share ≠ wafer share;
- platform revenue share ≠ physical shipment share;
- contracted MW ≠ energized MW;
- energized MW ≠ utilized AI load;
- rack spec × hypothetical racks ≠ shipment;
- CoWoS geometry ≠ fab yield;
- CapEx guidance ≠ actual CapEx;
- AI exposure ≠ job loss;
- model rental conversion ≠ full company cash cost;
- institutional forecast ≠ company actual;
- one physical pool ≠ another physical pool.

## 15. The most reliable quantitative sequence

The report follows this sequence:

> **official system spec → material identity → scenario demand → supply constraint → forward commitment → utilization → falsification**

The alternative—starting with a grand end-state and searching backward for numbers to fill a model—is not accepted.

This discipline does not require conservative scenarios. It allows scenarios to remain ambitious while preserving an auditable fact layer and consistent physical dimensions.

## References

[^ch08-1]: DeepSeek-AI, “DeepSeek-V3 Technical Report,” https://arxiv.org/abs/2412.19437
[^ch08-2]: DeepSeek-AI, “DeepSeek-V2,” repository and technical report, https://github.com/deepseek-ai/DeepSeek-V2
[^ch08-3]: NVIDIA, “GB200 NVL72,” official product page, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^ch08-4]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^ch08-5]: NVIDIA, DGX GB200 Hardware Guide, rack power approximately 120 kW, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
[^ch08-6]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm


\newpage


# Part I · Chapter 9: Global Semiconductor Supply Chains and Manufacturing Redundancy

## 1. Frontier AI depends on an industrial chain spanning companies and countries

The physical supply chain of a frontier AI system includes at least:

- lithography / deposition / etch / metrology equipment;
- silicon wafers and high-purity materials;
- leading-edge foundry;
- HBM;
- advanced packaging / substrates;
- testing;
- data-center power / cooling.

Supply security for an accelerator designer is therefore not determined by chip design alone. Multiple industrial layers must be simultaneously available.

## 2. ASML shows that equipment itself is a system-level capability

ASML's 2025 Annual Report reports **48 EUV lithography systems sold** during the year. Its High-NA TWINSCAN EXE platform remained in customer qualification toward high-volume manufacturing.[^ch09-1]

ASML stated that by the end of 2025 customers had run more than **400,000 wafers** on High-NA systems while work continued toward high-volume-manufacturing qualification.[^ch09-1]

The strategic constraint in advanced lithography cannot therefore be captured by a single-machine price.

The relevant variables are:

- system availability;
- throughput;
- imaging / overlay performance;
- customer qualification;
- field service;
- long-term coordination across optics / source / stage / metrology.

High-NA matters primarily as a process-roadmap and industrial-maturity path, not as a media-reported price tag.

## 3. A fab cannot exist independently of its supplier ecosystem

Leading-edge manufacturing depends on equipment installation, spare parts, software, process recipes, materials, metrology, and long-duration field service.

Even if two regions both contain fab buildings, their effective capacity will not be equivalent if supplier density, engineering talent, qualification cycles, tool service, and material stability differ.

This report therefore defines supply-chain independence as **system-level continuity**, not simply "a fab exists on the map."

### 3.1 Upstream Continuity: equipment, software, spare parts, and field service are separate constraints

The existence of a domestic fab does not automatically mean that capacity expansion is independent of external upstream supply.

ASML's public export-control statements provide an auditable boundary:[^ch09-2][^ch09-3]

- sales of EUV systems to China are already restricted;
- the most advanced immersion DUV systems require Dutch export licences;
- the 2024 U.S. update expanded restrictions to additional advanced semiconductor-manufacturing technologies, including metrology and software.

This does **not** support the claim that every Chinese fab would stop operating under a supply interruption. ASML itself notes that the controls focus on advanced technologies / specific fabs rather than every system.

The variables that matter are:

> **critical equipment availability + software/licensing + spare parts/field service + materials qualification**

These variables determine whether new capacity can ramp on schedule, whether existing lines can sustain yield, and whether process generations can continue advancing.

"Memory capacity is expanding" and "the memory supply chain is fully autonomous" are therefore different propositions.

## 4. Material qualification is an often-underestimated time cost

Advanced nodes are highly sensitive to contamination, particles, uniformity, defect density, and long-term stability.

Changing a materials supplier is not a normal procurement switch. Even chemically similar materials can require requalification and renewed learning across yield, tool recipes, and reliability.

The relevant materials constraint is therefore not an unsupported market-share statistic. It is:

> **Does a qualified alternative supplier exist, and how long would switching take?**

## 5. TSMC's geographic expansion shows that redundancy is real—and that the core cluster cannot be copied instantly

TSMC's 2025 Annual Report shows:[^ch09-4]

- the first Arizona fab entered **4 nm volume production in 4Q24**;
- the second Arizona fab is planned for 3 nm and more advanced technologies;
- construction of the third Arizona fab began in 2025, alongside announced plans for additional fabs, advanced-packaging facilities, and R&D expansion;
- the first Kumamoto fab in Japan entered volume production by the end of 2024, while the second fab plan includes 3 nm;
- the Dresden project in Germany targets automotive / industrial specialty technologies;
- Taiwan continued building Hsinchu / Kaohsiung 2 nm capacity and investing in leading-edge and advanced-packaging facilities.

Geographic diversification is therefore a real trend. It is not the same as reproducing the Taiwan cluster overnight.

Different regions continue to differ in node mix, product mix, packaging, workforce, supplier density, and power/water conditions.

## 6. Government subsidies reduce the cost of redundancy; they do not create instant independence

The U.S. Department of Commerce final CHIPS award for TSMC Arizona includes up to **US$6.6B of direct funding** supporting three leading-edge fabs. Final NAPMP advanced-packaging awards total **US$1.4B**, while Amkor's Arizona advanced-packaging/test facility received up to **US$407M of direct funding**.[^ch09-5][^ch09-6][^ch09-7]

These programs directly support a broader conclusion:

> **Strategic redundancy requires additional public capital to offset geographic duplication, cluster formation, and early-utilization risk.**

Subsidies cannot instantly reproduce decades of yield learning, supplier qualification, and engineering density. They can accelerate capacity formation, but they are not equivalent to immediate supply-chain independence.

## 7. Why redundancy inherently costs more

Greater resilience often requires:

- duplicated fabs / packaging lines;
- duplicated inventories;
- spare / reserve capacity;
- regional supplier qualification;
- lower initial utilization;
- government incentives;
- additional engineering / compliance overhead.

The supply chain can therefore move from:

> **lowest-cost global optimization**

toward:

> **higher-cost strategic redundancy**

This is not simply an efficiency failure. It is a changed cost function under a changed security objective.

## 8. AI demand accelerates geographic restructuring

Demand for leading-edge logic, HBM, packaging, and power has pushed advanced manufacturing beyond the normal commercial cycle toward strategic infrastructure.

TSMC's 2025 Annual Report links Arizona expansion to strong multi-year AI-related demand, while U.S. CHIPS programs treat AI/HPC as important use cases for leading-edge and advanced-packaging investment.[^ch09-4][^ch09-5][^ch09-6]

The AI-infrastructure cycle and industrial-policy cycle are therefore increasingly overlapping.

## 9. Geographic redundancy does not mean every layer is localized

A regional supply stack has to be tested across:

- equipment / service;
- materials;
- foundry;
- HBM;
- packaging / substrate;
- testing;
- power / water;
- workforce;
- customer qualification.

Localizing one layer reduces dependency in that layer only. It does not automatically close the other risks.

This is why the frontier-system resilience of China, the United States, Europe, or Japan cannot be summarized with one localization percentage.

## 10. China localization and Western reshoring face the same system problem

China's localization of equipment, materials, foundry, memory, and packaging and the U.S./European/Japanese reshoring or friend-shoring programs pursue different strategic objectives.

They nevertheless face the same engineering requirement:

> **performance + yield + scale + qualification + cost must all work at the same time.**

The existence of one product is not system closure. Real substitution must be sustainable at production scale, reliability, and long-duration service.

## 11. Geopolitical fragmentation can increase global investment while lowering single-system efficiency

If the world develops two or more relatively separate semiconductor / AI system ecosystems, the result can include:

- repeated fab investment;
- repeated packaging investment;
- duplicated software/runtime;
- higher strategic inventory;
- lower cross-region fungibility;
- more policy-driven capacity.

Fragmentation does not necessarily reduce global semiconductor CapEx. It can instead produce **more duplicated construction, lower utilization efficiency inside each individual system, and greater resilience**.

## 12. What constitutes real Supply-Chain Resilience

This report does not define complete self-sufficiency as the only valid objective.

More useful tests are:

1. have single points of failure been reduced?
2. does each critical layer have a qualified second source?
3. how long does system-level recovery take after disruption?
4. does regional capacity have sufficient power, workforce, and supplier support?
5. can the cost of redundancy still be covered by the economics of the final workload?

The real competition is therefore not which country produces every input domestically, but:

> **who can maintain the highest level of system continuity at an acceptable cost when a critical disruption occurs.**

## 13. Current judgment

As of 2026, public evidence supports a relatively clear direction:

- core leading-edge technologies remain highly concentrated;
- geographic redundancy is accelerating;
- government participation has increased materially;
- advanced packaging is now an explicit policy and investment object;
- redundancy raises resilience while also raising capital and operating cost;
- overseas fab expansion still needs time to reproduce supplier, workforce, packaging, and infrastructure ecosystems.

The semiconductor supply chain of the next decade is therefore more likely to consist of **highly concentrated core technologies + greater regional redundancy + higher strategic inventories + greater public-capital participation** than to return quickly to a fully dispersed and fully substitutable global market.

## References

[^ch09-1]: ASML, 2025 Annual Report and Strategy & Stories, EUV / High-NA roadmap and system shipments, https://www.asml.com/en/investors/annual-report/2025
[^ch09-2]: ASML, 2023 statement on Dutch export-control regulations, EUV and advanced immersion DUV licensing, https://www.asml.com/en/news/press-releases/2023/statement-regarding-export-control-regulations-dutch-government
[^ch09-3]: ASML, 2024 statement on updated export restrictions covering additional advanced manufacturing technologies, metrology, and software, https://www.asml.com/en/news/press-releases/2024/asml-expects-impact-of-updated-export-restrictions-to-fall-within-outlook-for-2025
[^ch09-4]: TSMC, 2025 Annual Report, Arizona/Japan/Germany/Taiwan manufacturing footprint and AI-related demand context, https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^ch09-5]: U.S. Department of Commerce, TSMC Arizona CHIPS final award, 2024-11, https://www.commerce.gov/news/press-releases/2024/11/biden-harris-administration-announces-chips-incentives-award-tsmc
[^ch09-6]: U.S. Department of Commerce, US$1.4B NAPMP advanced-packaging final awards, 2025-01, https://www.commerce.gov/news/press-releases/2025/01/us-department-commerce-announces-14-billion-final-awards-support-next
[^ch09-7]: U.S. Department of Commerce, Amkor Arizona advanced-packaging and test award, 2024-12, https://www.commerce.gov/news/press-releases/2024/12/biden-harris-administration-announces-chips-incentives-award-amkor
