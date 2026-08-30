# Part IV · Chapter 32: Master View — What Determines AI Infrastructure Power, and What Would Change the View

## 1. Current baseline: S2 is the synthesis, not a second executive summary

**Current baseline (evidence cutoff: August 28, 2026): S2 — Baseline Concentration.**

Chapter 1 already provides the report's eight load-bearing findings as the reader entry. This chapter does not repeat them. The Master View instead compresses the preceding 31 chapters into four adjudication tests and explains why the current state remains S2.

### Test A — Has system power become irreplaceable multi-layer control?

Not yet. A small number of system platforms, especially NVIDIA, combine strong system coordination, software switching costs, supply commitments, and capital formation capacity. But delivery still depends on external foundry, HBM, advanced packaging, networking, and power. Strong platform power is not the same as control of every physical layer.

### Test B — Has AI/HPC resource absorption already forced structural exit across traditional end markets?

Only partially. Non-AI Residual Capacity, Quantity Assurance, and product-mix pressure are visible in smartphones, PCs, game consoles, and other end systems. The evidence supports **repricing, configuration changes, product-mix polarization, and longer replacement cycles**; it does not yet establish terminal decline across smartphones, PCs, gaming, or other complete demand industries.

### Test C — Is the second stack already strong enough to break concentration?

Not yet. Hyperscaler custom systems and China's parallel stack establish that real substitution paths exist. But production-workload share, migration cost, HBM/packaging/power access, and multi-generation manufacturing continuity still determine whether substitution moves from “can run” to “can durably change industry structure.”

### Test D — Has capital formation entered broad systemic clearing?

Not yet. High CapEx, **US$279B** of aggregate supply commitments, seller-assisted financing, and a **>US$500B** third-party-capital mobilization target all raise the importance of future clearing. None allows the report to infer a bubble or hard landing from spending scale alone. S4 still requires broad, persistent, causally coherent deterioration across independent signals such as utilization, market clearing, forward commitments, and demand quality / financing.

Taken together, the four tests describe:

> **high growth + high concentration + real substitution + no broad capital clearing yet.**

That is **S2 — Baseline Concentration**.

The Master View therefore answers a different question from Chapter 1:

> **Which mechanisms still sustain S2, which reverse facts would break those mechanisms, and what would force the report toward S1, S3, or S4?**

## 2. System coordination is the relevant form of industrial power

NVIDIA's current advantage is not ownership of every physical input. It is the ability to organize GPUs, CPUs, HBM, NVLink, CUDA/runtime, rack-scale architecture, supply-chain commitments, and large workloads into a mature general-purpose commercial system.

NVIDIA's manufacturing, supply, and capacity commitments increased from **US$95.2B** on January 25, 2026 to **US$279B** on July 26, 2026.[^1] The filing does not disclose a supplier-level split, so the aggregate cannot be treated as confirmed revenue for TSMC, CoWoS, or any single HBM vendor.

The correct long-run metric is:

> **Layer-specific Incremental Scarce-Capacity Access: whether a platform can repeatedly obtain enough qualified, stable, deliverable supply across advanced logic, HBM, packaging, networking, and LPS/power.**

In severe shortage conditions, price is not the only allocation mechanism. Long-term agreements, credit quality, prepayments, purchase scale, and allocation fulfillment all affect quantity assurance.

Therefore:

> **willingness to pay ≠ guaranteed quantity**

The competition can consequently move from "who is willing to pay more?" toward "who can secure stable quantities, delivery timing, and system-level priority?"

The latest 2026 developments extend system coordination beyond semiconductor supply. NVIDIA announced compute-financing platforms with six large long-duration capital providers, targeting **more than US$500B of third-party capital mobilization over time**, and separately provided credit support for land, power, and shell at the PORTS-Pike project, whose initial deployment is designed for **4.25 IT-GW** with OpenAI as the customer.[^13][^14]

The first figure is a capital-mobilization target, not deployed capital. The second is future design capacity, not energized load.

Together they show that leading system-platform coordination is beginning to extend from chips into **physical infrastructure and capital formation**.

---

## 3. Marginal capital formation is shifting toward AI/HPC

One of the most important structural changes in 2026 is that marginal advanced-manufacturing and memory demand is becoming increasingly dependent on AI/HPC.

In TSMC's 2Q26 platform revenue mix, HPC represented **66%** and smartphone **22%**. Advanced technologies at 7 nm and below represented **77%** of wafer revenue. TSMC also raised its 2026 capital budget to **US$60B–64B**, with continued investment in advanced processes, packaging, and testing.[^6]

These numbers do not mean all HPC is AI, and they do not prove that Apple, Qualcomm, or any other specific customer has been displaced.

They support the narrower conclusion that:

> **High-growth HPC/AI workloads are materially influencing the direction of incremental advanced-manufacturing capital formation.**

Memory shows the same structural shift. Micron disclosed that, under same-node / same-bit conditions, HBM3E requires approximately **3× the wafer supply of DDR5**.[^2] TrendForce forecasts that HBM + RDIMM will represent approximately **51% of 2026 DRAM bit supply**.[^3]

The report describes this structure as a **Two-Speed Semiconductor Economy**:

> **The AI Infrastructure Economy and the Traditional Device Economy share upstream resources but differ in willingness to pay, order duration, prepayment capacity, BOM constraints, and the ability to induce new capital formation.**

Consumer electronics do not disappear. The structural change is that marginal-demand power is shifting toward hyperscalers, system-platform sellers, and Anchor Compute Buyers.

---

## 4. Bottlenecks rotate across independent physical pools

AI-system delivery depends on several independent physical layers.

### HBM

The important point is not simply HBM market share. It is manufacturing-resource intensity. Micron's approximately **3× wafer-supply trade ratio** indicates that equal-bit HBM3E can consume materially more wafer input than DDR5.[^2]

### Advanced Packaging

TSMC has explicitly stated that advanced-packaging capacity is tight and that packaging tightness has constrained customer growth.[^4]

More leading-edge front-end wafer capacity therefore does not automatically produce proportionally more deliverable AI systems.

### Power and LPS

Approximately **120 kW-class racks**, the approximately **835 MW** Crane restart, the Talen/AWS revised PPA with up to **1,920 MW** of contract quantity, and the Kairos/Google long-duration power-development path show that power has become an independent physical constraint.[^5]

The delivery state must remain explicit:

> **Announced → Contracted / Secured → Permitted → Construction / Transition → Energized → Utilized**

Generation MW/GW, PPA capacity, IT-GW, energized facility load, and utilized AI load are different physical quantities.

When one bottleneck eases, another can become dominant. This is the report's **Rolling Bottleneck Cascade**.

---

## 5. Residual capacity is the downstream denominator

Traditional end markets do not face gross worldwide supply. They face effective supply after priority demand has absorbed its share:

> **Non-AI Residual Capacity = Effective Supply − AI / Anchor Demand − Other Priority Demand**

This explains why both of the following can be true at the same time:

- global wafer, DRAM, and packaging capacity keeps expanding;
- smartphone, PC, automotive, or industrial buyers still face higher prices, weaker allocation, or slower configuration upgrades.

The correct transmission mechanism is therefore not "AI takes all chips."

It is:

> **High-value demand changes product mix, capital priority, and quantity assurance, which changes the effective residual supply available to non-AI markets.**

Lower-margin, lower-bargaining-power, shorter-duration buyers are generally more exposed than buyers with LTAs, scale, stronger balance sheets, and end-market pricing power.

---

## 6. Second stacks reduce platform rent before they eliminate scarcity

Google Ironwood, AWS Trainium, Microsoft Maia, and Meta MTIA show that hyperscaler competition is no longer simply "internal ASIC versus external GPU." It is increasingly **system stack versus system stack**.[^7]

This produces two effects that point in different directions:

1. **Platform-profit diversion:** some workloads no longer pay the full economics of an external platform.
2. **Upstream resource competition:** custom systems still require advanced logic, HBM, packaging, networking, and power.

Custom-silicon success therefore does not automatically mean upstream scarcity disappears.

The long-run variables that matter are:

- production workload share;
- migration cost;
- system utilization;
- external adoption;
- software portability;
- scale-up / scale-out efficiency;
- dependence on the same scarce upstream layers.

If second system stacks carry more production workload and migration cost falls, **S1 — Competitive Expansion** gains weight.

If alternative systems remain constrained by the same scarce inputs and proprietary software friction, S2/S3 gains weight.

---

## 7. Anchor Compute Buyers now influence infrastructure formation

OpenAI Stargate and Anthropic/AWS demonstrate that leading model companies are no longer simply cloud tenants.[^8]

Multi-year compute commitments can produce the following chain:

> **higher revenue visibility → greater financing certainty → earlier cloud / data-center / power / chip buildout → more stable capacity → larger workloads**

This is the **Anchor Compute Buyer Effect**.

The same mechanism can amplify capital-cycle risk. If long-duration demand is rescheduled, utilization disappoints, or commercial revenue fails to cover infrastructure capital cost, the certainty that originally supported construction can become stranded-capacity and duration-mismatch risk.

Model-company long-duration commitments have therefore become a leading indicator on par with hyperscaler CapEx and system-vendor supply commitments; their time-leadership still needs to be verified across more full cycles.

PORTS-Pike extends this model further. Anchor demand can now be combined with **platform credit support + infrastructure developer + long-duration lease** to form land, power, and shell ahead of delivered compute.[^14]

That structure can accelerate infrastructure formation while also increasing customer concentration and duration risk.

---

## 8. China must be evaluated through two closure tests

China's supply position cannot be reduced to one localization rate.

Current public evidence supports several distinct statements:

- consumer computing and smartphone supply chains have meaningful domestic capability;
- DRAM / NAND capability is expanding;
- PC / workstation substitution is growing but remains sensitive to software compatibility and professional workloads;
- a real accelerator/software parallel stack exists in frontier AI, but full autonomous closure is a separate question.

CXMT disclosures support conclusions about DDR/LPDDR and DRAM market position, but do not prove HBM-class frontier closure. Counterpoint's YMTC shipment-share and revenue-share figures must also retain their different denominators.[^9][^10][^11]

Foundry revenue share is similarly not a frontier-AI capability measure. TrendForce's **5.1%** SMIC figure for 1Q26 is foundry revenue share, not proof of frontier-system closure.[^12]

The report therefore uses two levels.

### Production-Grade Parallel Stack

China has moved beyond the stage of having no substitute system. Parts of the stack are already in real production deployment.

### Autonomous Frontier Closure

Public evidence is still insufficient to show that advanced manufacturing, HBM-class memory, advanced packaging, interconnect, compiler/runtime, equipment/material continuity, and cross-generation infrastructure scaling are all autonomous and sustainable at frontier scale.

The long-run question is therefore not the benchmark performance of one domestic accelerator.

It is whether production workloads continue expanding and whether the full stack can preserve performance, supply, power, and economics across generations when critical external inputs become constrained.

---

## 9. Capital-cycle risk lives in utilization and financing quality

Cloud CapEx, system-vendor revenue, foundry revenue, memory revenue, and power investment cannot be mechanically added into one "global AI investment" number because the same economic flow appears on different ledgers.

AI infrastructure combines assets with very different durations:

- accelerator / server: fast technological depreciation;
- network / cooling: medium duration;
- data-center shell: long duration;
- grid / substation / generation: still longer duration;
- future workload revenue: uncertain.

The report therefore uses five groups of capital-clearing signals:

- **Accounting:** impairment, write-downs, accelerated depreciation;
- **Utilization / Revenue:** deployed-compute utilization, AI revenue, verified workflow output;
- **Market Clearing:** lease rates, used-system prices, delivery lead times, inventory;
- **Forward Commitment:** CapEx guidance, supply commitments, compute contracts, power contracts;
- **Demand Quality / Financing:** customer cash generation, third-party capital, supplier equity / credit enhancement, refinancing dependency.

These are **monitoring families, not a five-of-five checklist**. Financing-led or real-economy clearing can be confirmed before qualifying impairment / write-down evidence appears, provided independent signal families and causal breadth are strong enough and alternative explanations do not dominate.

As of August 2026, public evidence remains more consistent with:

> **continued high-intensity capital expansion, with rising ROI and monetization pressure**

than with a confirmed industry-wide Capital Hard Landing.

The latest financing structures add one more variable: **Financing Reflexivity**.

When a system seller provides equity, credit enhancement, LPS support, or compute-financing coordination, seller-side demand visibility becomes more correlated with the financing conditions of the customer and infrastructure developer.

That does not make the demand "fake."

It means demand quality must distinguish:

1. independently financed end demand;
2. long-duration Anchor Buyer commitments;
3. third-party infrastructure capital;
4. supplier equity / credit support.

---

## 10. Demand duration depends on workflow penetration and economic output

A report that stops at GPUs, HBM, CapEx, or data-center capacity is incomplete. Infrastructure is the supply side. The ten-year industrial cycle ultimately depends on whether these physical assets can move through software, enterprise workflows, and the physical world into verifiable economic output.

### AI Inheritance Effect: IT is the installed base

Long-run AI diffusion does not require rebuilding the digital world from zero. Decades of information technology have already created software, databases, cloud systems, APIs, digital documents, source code, identity/access systems, and traceable workflows. In highly digitized organizations, AI can act as an intelligence / automation layer on top of that installed base.

The demand side therefore contains an additional diffusion path:

> **Digital Installed Base → AI Overlay → Workflow Penetration → Automation Depth → Workload Volume**

This expands the long-run infrastructure thesis beyond "models keep getting larger" toward "more existing digital workflows become AI workloads."

The boundary remains essential. Marginal Digital → AI deployment friction can be much lower than Industrial → Digital transformation, but it is not zero. Data quality, integration, security, governance, responsibility, reliability, human review, and unit economics still determine whether adoption moves from feature use into production automation.

### Agent-native software: the unit shifts from seats to verified outcomes

Traditional SaaS scales largely around accounts and seats. Agent-native software continuously consumes inference, retrieval, tools/APIs, retries, observability, and human review.

The more relevant unit is therefore:

> **cost per verified workflow outcome**

Cheaper models and better routing can reduce resource intensity per attempt. But if lower prices unlock more users, longer agent loops, more tool calls, and previously uneconomic workflows, total compute demand can still expand.

The software layer is therefore both a receiver of infrastructure cost and a source of demand elasticity for infrastructure.

### Physical AI: deployment has to clear a capital-payback test

Physical AI is also a systems problem: perception, control, actuation, batteries, sensors, manufacturing, field reliability, and cloud/edge infrastructure have to close together.

The commercial threshold is not whether a robot can complete one task. It is whether:

> **Useful Tasks × Uptime × Deployment Scale** can cover **Energy + Maintenance + Human Supervision + Depreciation + Financing**

Physical AI can therefore become a new pool of compute, memory, storage, and cloud-workload demand, but only scaled utilization and capital recovery can validate its industrial value.

### Labor: Task → Workflow → Job

The labor transmission chain has to pass through:

> **Model Capability → Task Suitability → Workflow Redesign → Adoption Economics / Responsibility → Job Composition → Employment / Wage Outcome**

Occupational exposure therefore cannot be converted directly into job-loss forecasts. More useful long-run indicators include junior/senior ratios, human-review burden, output per employee, exception rates, and organizational layers.

### Talent: system design and verification matter more than model access

As model calling commoditizes, more durable capability moves toward workflow engineering, system engineering, cross-stack portability, verification, performance/cost measurement, and responsibility boundaries.

The long-run talent divide is not merely who "uses AI." It is:

> **who can organize AI into reliable, portable, measurable production systems and remain accountable for the result**

Putting these layers together, the report's demand-side loop is:

> **Physical Infrastructure → System Delivery → Workflow Economics → Verified Output → Adoption / Cash Flow → Utilization → Capital Reinvestment**

If the front half of that chain expands persistently faster than the back half, S4 risk rises. If verified workflow output, utilization, and cash flow continue pulling new demand forward, S2/S3-style capital expansion can persist even as unit compute costs fall.

---

## 11. Compute is productive infrastructure only when output validates the capital

The report uses the idea of compute becoming a productive input in an economic, testable sense—not as a technological slogan.

The relevant standard is:

> **Can an AI system, at a given compute, energy, and capital cost, repeatedly complete workflows that previously required human execution and produce outcomes that can be verified?**

If the answer is no, compute remains primarily an assistive tool.

If the answer is yes at scale, compute, memory, packaging, power, and software begin to function as productive infrastructure.

A more useful metric is therefore:

> **cost per verified workflow outcome + capital required to sustain it**

This is why model capability, infrastructure spend, utilization, and business revenue must be analyzed inside one unit-economics framework.

---

## 12. Four structural states

The report uses four parallel scenarios.

### S1 — Competitive Expansion

Supply elasticity rises, custom systems mature, interoperability improves, switching costs fall, and value capture becomes more distributed.

### S2 — Baseline Concentration

A small number of system platforms and scarce-layer suppliers retain strong economics while substitution paths continue expanding. **As of August 2026, this is the state that best matches the current evidence mix.**

### S3 — Resource Hegemony

Multiple scarce layers, quantity assurance, and switching costs strengthen together, forcing challengers to replicate a more complete infrastructure stack.

### S4 — Capital Hard Landing

Multiple causally independent signal families deteriorate broadly and persistently across actors/layers, with at least one real-economy / market-clearing / commitment signal present. Accounting losses strengthen severity when present but are not required.

These states are not sequential stages and do not carry fixed probabilities.

The variables that will determine the 2030/2036 structure include:

- supply elasticity;
- HBM / packaging / power tightness;
- system substitution;
- software migration cost;
- Anchor Buyer demand;
- utilization / monetization;
- capital discipline;
- regulation;
- China's production-grade parallel stack and autonomous frontier closure;
- demand-financing quality and supplier-assisted financing.

---

## 13. What would change the view

High-value falsification signals include:

- sustained declines or large cancellations in leading system-platform supply commitments;
- advanced packaging no longer being described as a growth constraint by major suppliers;
- HBM / DRAM residual supply becoming durably abundant;
- cloud custom systems creating large-scale, low-migration-cost substitution in frontier workloads;
- open interfaces materially lowering proprietary software / fabric switching costs;
- energized power expanding enough that Time-to-Power stops differentiating projects;
- Anchor Compute Buyer commitments being delayed or underutilized at scale;
- hyperscaler AI monetization persistently failing to cover the expanding capital base;
- China's frontier parallel stack gaining or losing scaled first-party evidence across multiple Production-Grade Gates, or autonomous frontier closure changing materially;
- supplier equity / credit support rising while independent customer financing and utilization weaken;
- formal regulatory remedies materially changing tying, interface, or market-entry conditions.

If these signals contradict the current mechanisms, the report must change.

They cannot be explained away by saying the long-run thesis remains intact.

---

## 14. Research discipline: Fact → Hypothesis → Mechanism → Scenario → Falsification

The report uses five layers:

- **F — Fact:** observed and publicly verifiable;
- **H — Hypothesis:** a future input condition or stress-test assumption;
- **M — Mechanism:** the causal transmission between facts and hypotheses;
- **S — Scenario:** a future structural state created by several conditions;
- **X — Falsification:** reverse signals strong enough to weaken, rewrite, or invalidate the original judgment.

**Mechanism-break override:** breadth requirements govern **system-level scenario adjudication**, not whether an underlying mechanism is allowed to survive direct falsification. If a high-quality observation, on the same denominator and time identity, directly breaks a necessary premise of a mechanism, that mechanism must be downgraded, rewritten, or retired immediately even when cross-signal breadth is not yet present. Breadth determines whether the whole S1–S4 state changes; it cannot be used to ignore a broken premise.

The purpose is to prevent:

- an institutional forecast from becoming a company fact through repetition;
- company guidance from becoming an actual;
- revenue share from becoming wafer share;
- contracted capacity from becoming energized load;
- a D-grade stress test from becoming a deterministic 2030/2036 outcome.

Future judgments can be bold.

The fact layer must remain conservative.

---

## 15. Bottom line

AI is driving an industrial restructuring deeper than a conventional GPU demand cycle.

It is changing:

- the destination of incremental advanced-semiconductor capital;
- memory and advanced-packaging product mix;
- the boundary of system-platform competition;
- the industrial role of hyperscalers and model companies;
- the strategic value of power and data-center infrastructure;
- the residual capacity available to traditional device markets;
- the speed and depth at which the global digital installed base is converted into AI-enabled workflows;
- the shift in Agent-Native Software from seat economics toward verified-workflow economics;
- the transition in Physical AI from technical demo toward utilization, reliability, and capital payback;
- labor-market restructuring from task automation through workflow redesign;
- the migration of talent value from "using models" toward workflow/system engineering and verification;
- the strategic objective of China's parallel stack;
- the dependence of global capital markets on AI workload monetization.

The resulting competition is not simply a chip war.

It is:

> **System Stack + Scarce Capacity + Capital Formation + Workload Monetization**

The state closest to current evidence remains **S2 — Baseline Concentration**: leading platforms and scarce layers retain strong economics, while alternative systems continue to grow without yet eliminating system-level concentration or physical constraints.

If supply elasticity, system portability, and multi-sourcing improve materially, the industry moves toward S1.

If multiple scarce layers and switching costs strengthen simultaneously, S3 gains weight.

If multiple causally independent signal families across utilization/revenue, market clearing, forward commitments, financing quality, and accounting cross-confirm broad and persistent deterioration across actors/layers, S4 becomes the dominant interpretation; Accounting is confirmatory rather than mandatory.

The report's final question is therefore not whether “only AI still matters.” Smartphones, PCs, game consoles, vehicles, industrial equipment, robotics, aerospace, and other long-lifecycle high-reliability systems remain important. The relevant question is:

> **Can those still-important end systems continue to obtain enough, stable, affordable electronics on their own BOM, qualification, lifecycle, and cost constraints from an upstream system whose priorities are being rewritten by AI/HPC?**

The dimensional boundary remains essential. Smartphones, PCs, and selected edge/ADAS systems can directly share advanced logic, memory, or selected packaging with AI. Vehicles, industrial control, and factory systems are more often exposed through adjacent product mix and long qualification cycles. Aerospace, defense, and space electronics often face a different problem: the economics and continuity of trusted, long-life, low-volume, special-process supply, equipment, and engineering talent — not direct competition for HBM.

That is the industrial meaning of the **system-level resource concentration risk**: **other end systems do not become unimportant; rather, importance itself no longer guarantees upstream priority.**

> **Forecasts may be wrong; evidence boundaries cannot be. Scenarios may be bold; the fact layer must remain disciplined. The most valuable long-run industry research is not a one-time guess at the end-state, but knowing which variables are deciding the end-state—and what facts would force the judgment to change.**

## Cross-references

- [Core Evidence Ledger](../核心证据台账.en.md)
- [Core Source Index](../核心参考文献索引.en.md)
- [Part I · Ch02 NVIDIA System Stack](part-I-ch02-nvidia-system-stack.md)
- [Part I · Ch05 HBM](part-I-ch05-hbm-memory.md)
- [Part I · Ch06 Advanced Packaging](part-I-ch06-advanced-packaging.md)
- [Part I · Ch07 Power](part-I-ch07-power-constraint.md)
- [Part II · Ch12 Hyperscaler System Stack](part-II-ch12-hyperscaler-system-stack.md)
- [Part II · Ch14 Agent-Native Software and AI Software Unit Economics](part-II-ch14-agent-software.md)
- [Part II · Ch15 Physical AI](part-II-ch15-physical-ai.md)
- [Part II · Ch17 China Parallel Stack](part-II-ch17-china-parallel-stack.md)
- [Part III · Ch25 AI and Labor Markets](part-III-ch25-labor-market.md)
- [Part III · Ch26 Education and Talent Systems](part-III-ch26-education-talent.md)
- [Part III · Ch20 Value Capture Map](part-III-ch20-value-capture-map.md)
- [Part III · Ch24 Capital Clearing](part-III-ch24-capital-clearing.md)
- [Part IV · Ch31 Strategy & Endgame](part-IV-ch31-strategy-endgame.md)

## References

[^1]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^2]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^3]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^4]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging tightness limiting customer growth, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^5]: NVIDIA, DGX GB200 Hardware Guide, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html ; Constellation, Crane Clean Energy Center, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs ; Talen Energy, 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm ; Kairos Power / Google, https://www.kairospower.com/google
[^6]: TSMC, 2Q26 Quarterly Results and Earnings Conference, platform mix and capital budget, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^7]: Google Ironwood TPU, https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; AWS Trainium3 UltraServers, https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ ; Microsoft Maia 200, https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ ; Meta MTIA 300, https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
[^8]: OpenAI, Stargate infrastructure disclosures, https://openai.com/index/announcing-the-stargate-project/ ; Anthropic, AWS compute collaboration, https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
[^9]: CXMT prospectus / Omdia, 2025 Q2 DRAM revenue share 3.97%, https://static.sse.com.cn/stock/disclosure/announcement/c/202512/002170_20251230_B8QS.pdf
[^10]: Counterpoint Research, 2026 Q2, YMTC 14% NAND shipment share, https://counterpointresearch.com/en/insights/server-led-essds-hit-48-percent-of-nand-shipments
[^11]: Counterpoint Research, 2026 Q1, YMTC 13% NAND revenue share, https://counterpointresearch.com/en/insights/global-nand-memory-market-share
[^12]: TrendForce, 2026-06-12, 1Q26 foundry revenue shares, https://www.trendforce.com/presscenter/news/20260612-13095.html
[^13]: NVIDIA, 2026-08-10, AI compute infrastructure financing platforms and >US$500B third-party-capital mobilization target, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Partners-With-Apollo-BlackRock-Blackstone-Brookfield-Goldman-Sachs-and-KKR-to-Establish-AI-Compute-Infrastructure-Financing-Platforms-to-Mobilize-Over-500-Billion-of-Third-Party-Capital/default.aspx
[^14]: NVIDIA, 2026-08-17, PORTS-Pike / SB Energy / OpenAI, initial 4.25 IT-GW design capacity, credit support for land/power/shell, phased online plan beginning in 2028, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx
