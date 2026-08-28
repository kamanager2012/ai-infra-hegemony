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
