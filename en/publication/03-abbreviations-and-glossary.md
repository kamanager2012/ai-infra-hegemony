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
| GDDR | Graphics Double Data Rate memory | Common in gaming GPUs / game consoles; not treated as the same product pool as HBM |
| NAND | NAND Flash | Different memory technology from DRAM/HBM |
| eSSD | Enterprise SSD | Enterprise solid-state storage |
| NVMe | Non-Volatile Memory Express | High-speed SSD interface / protocol; a product specification is not an industry-supply measure |
| UFS | Universal Flash Storage | Mobile / embedded / selected game-console storage; analyzed separately from data-center SSD |
| CoWoS | Chip-on-Wafer-on-Substrate | TSMC advanced-packaging family; customer allocation is not inferred from revenue share |
| TSV | Through-Silicon Via | Important in HBM stacking / 3D integration |
| CUDA | NVIDIA compute platform / programming ecosystem | Analyzed as a software switching-cost variable |
| NVLink / NVSwitch | NVIDIA scale-up interconnect technologies | Not treated as the same layer as scale-out networking |
| CapEx | Capital Expenditure | Guidance, expectation, and actuals remain separate |
| OpEx | Operating Expenditure | Not mechanically combined with CapEx |
| FCF | Free Cash Flow | Company-defined and GAAP/non-GAAP identities are preserved |
| PPA | Power Purchase Agreement | Contracted capacity is not energized/utilized load |
| PUE | Power Usage Effectiveness | Data-center efficiency metric |
| LPS | Land, Power and Shell | Site land, power access, and building shell; secured LPS is not energized / utilized compute |
| IT-GW | Gigawatts of IT load / IT capacity | Design capacity for IT equipment / AI factory load; not interchangeable with generation GW, PPA GW, or grid-delivered GW |
| CSP | Cloud Service Provider | Hyperscalers are an important subset |
| OEM | Original Equipment Manufacturer | End-device / system manufacturer |
| ODM | Original Design Manufacturer | Design-and-manufacturing service provider |
| BOM | Bill of Materials | Used in end-market cost-transmission analysis |
| TCO | Total Cost of Ownership | Preferred system-level comparison unit |
| ASP | Average Selling Price | Product and time denominator must be explicit |
| ROI | Return on Investment | Report-side usage only; not a disclosed company metric unless a source is named |
| GAAP | U.S. Generally Accepted Accounting Principles | GAAP and non-GAAP identities are never merged |
| PPE | Property, Plant and Equipment | Used in hyperscaler capital-base reconstruction; accounting line items differ by company |
| TTM | Trailing Twelve Months | The time window must be stated; not directly comparable with calendar guidance |
| TAM | Total Addressable Market | Institutional / sell-side estimates only; not a disclosed actual |
| EOL | End of Life | Product-continuity risk in long-lifecycle end systems |
| MCU | Microcontroller Unit | Automotive / industrial layer; not a frontier-AI accelerator |
| APU | Accelerated Processing Unit | Console / client SoC context; not an HBM-class AI system |
| RF | Radio Frequency | Aerospace / defense special-process exposure |
| ADAS | Advanced Driver Assistance Systems | Automotive compute context |
| FLOPS | Floating-Point Operations per Second | Peak compute only; not a workload denominator (see Chapter 8) |
| KV cache | Key-Value cache | Inference memory state; one reason inference can remain memory-bound |
| EUV / DUV | Extreme / Deep Ultraviolet lithography | Process-equipment layer; relevant to export controls |

## Standard units

- Data capacity: KB / MB / GB / TB / PB / EB
- Bits and transfer rates: Kb / Mb / Gb / Tb; Mb/s / Gb/s / Tb/s
- Power: W / kW / MW / GW
- Energy: Wh / kWh / MWh / TWh
- Frequency: Hz / kHz / MHz / GHz
- Process / dimensions: nm / μm / mm / mm²
- U.S. dollar values: preserve source precision where material, e.g. US$96.221B and US$279B

## Core analytical concepts

### Resource reallocation pressure
Shorthand for the mechanism by which higher willingness to pay, longer-duration orders, and stronger expected returns from AI/HPC can redirect scarce capital and physical resources toward AI/HPC uses. It is descriptive mechanism language, not a separate empirical law.

### Scarce-layer Value Capture
Value capture arising in layers with low supply elasticity and difficult substitution, strengthened by scarcity, switching costs, and supply coordination. It is not a legal monopoly finding.

### Non-AI Residual Capacity (NARC)
Effective supply available to non-AI markets after AI / Anchor Buyer demand and other priority demand have been allocated.

### Quantity Assurance
Whether a buyer can obtain enough qualified supply on schedule within the relevant quality, generation, qualification, and delivery window. It is distinct from Price Pressure: **willingness to pay more does not guarantee planned quantity.**

### Upgrade Tax
An analytical term, not a tax category. It describes an end-system outcome in which higher upstream opportunity cost produces **slower specification improvement at the same price band, or a higher BOM / weaker subsidy for the same target specification**. It must not be generalized into uniform price inflation across all end markets.

### Two-speed semiconductor economics
Descriptive shorthand for the divergence created when the AI Infrastructure Economy and Traditional Device Economy share parts of the same upstream resource base but differ in willingness to pay, contract duration, BOM constraints, and capital-formation power.

### AI Capacity Gap / AI Capacity Growth Gap
**AI Capacity Gap** is the absolute physical shortfall `AI effective demand − AI effective capacity` within the same layer and delivery window; **AI Capacity Growth Gap** is the difference between demand growth and effective-capacity growth and describes only the direction in which the gap is changing. The two are not interchangeable.

### Incremental Scarce-Capacity Access
A layer-specific framework for evaluating whether different buyers can repeatedly obtain sufficient, qualified, and timely supply in advanced logic, HBM/DRAM, advanced packaging, networking, LPS, and energized power.

It is measured through variables such as qualified suppliers, lead time, allocation fulfillment, long-term agreements/prepayments, delivery schedules, buyer credit quality, and supply elasticity. The report does not compress different physical pools into one synthetic cross-layer percentage.

### Cloud system-stack substitution
An economic substitution test for whether hyperscalers can combine custom accelerators, interconnect, compiler/runtime, racks/pods, and captive workloads into a production-grade alternative system stack.

### Anchor-buyer mechanism
The mechanism by which long-duration compute commitments from large model companies influence data-center, power, chip, memory, and project-financing buildout. It is a demand-formation mechanism, not a separate grand theory.

### Rolling Bottleneck Cascade
The dynamic rotation of the binding constraint across logic, HBM, advanced packaging, networking, power, utilization, and related layers.

### AI inheritance
Shorthand for the mechanism by which AI adds an intelligence / automation layer on top of an existing digital installed base of software, databases, cloud systems, APIs, digital documents, source code, identity/access systems, and workflows. Highly digitized organizations can therefore face lower marginal Digital → AI deployment friction, but **not zero friction**: data quality, integration, security, governance, responsibility, reliability, human review, and unit economics still determine production adoption.

### AI Software Unit Economics
A workflow-level cost framework incorporating inference, retrieval/storage, tools/APIs, retries, human review, and other variable AI costs.

### Financing Reflexivity
The feedback mechanism created when a system seller also uses equity investment, credit enhancement, LPS support, or compute-financing coordination to accelerate customer and infrastructure buildout. It does not prove demand is artificial; it changes how demand independence, risk transfer, and refinancing dependence should be evaluated.

### Production-Grade Parallel Stack
A substitute system that can sustain real production workloads across accelerator / compute, memory subsystem, advanced packaging, interconnect, compiler/runtime, production workload, and utilization / reliability / economics. It does not require every upstream input to be fully autonomous.

### Autonomous Frontier Closure
A higher closure standard in which the system can continue scaling and iterating across generations when critical external inputs are constrained. In addition to a production-grade stack, it requires advanced-manufacturing continuity, equipment / materials / software / service continuity, and durable HBM, packaging, power, LPS, and capital formation.

### Time-to-Power
The time required for a site or project to obtain physically deliverable power. It must remain separate from headline generation capacity, PPA capacity, secured LPS, and future IT-GW design capacity.

### Verified Workflow Output
An AI-assisted workflow outcome that has passed the quality, responsibility, or business-acceptance conditions required for repeatable delivery, billing, or production use. It is the report's demand-side unit linking compute cost, enterprise adoption, cash flow, and capital recovery.

### Task-to-Job Translation
Model Capability → Task Suitability → Workflow Redesign → Adoption Economics / Responsibility → Job Composition → Employment / Wage Outcome. Prevents technical exposure rates from being converted directly into job-loss rates.

## Scenario terminology

- **S1 — Competitive Expansion:** higher supply elasticity, multi-sourcing, and portability distribute value capture more broadly.
- **S2 — Baseline Concentration:** a small number of system platforms / scarce-layer suppliers retain strong economics while real substitution paths continue developing.
- **S3 — Resource Hegemony:** multi-layer scarcity, concentrated quantity assurance / delivery access, switching costs, and financing coordination strengthen together while workload monetization remains sufficient to support associated long-duration commitments, materially raising the cost of replicating the full infrastructure stack.
- **S4 — Capital Hard Landing:** accounting losses, utilization/revenue, market clearing, forward commitments, and demand-financing quality deteriorate broadly and persistently, producing capital clearing.

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
