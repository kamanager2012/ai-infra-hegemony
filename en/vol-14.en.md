# Volume 14: AI Infrastructure Value-Capture Map — Who Captures Profit and Who Bears Residual Pressure

Chinese original: [vol-14.md](../vol-14.md)

## 1. Core question

Which layers capture durable economic value from the AI infrastructure buildout, which layers mainly absorb capital expenditure and depreciation, and which downstream markets bear residual supply pressure?

The report does not classify an industry as a “winner” merely because its revenue grows, and it does not classify an industry as a “loser” merely because input costs rise. The correct map separates **scarcity-layer value capture**, **system/platform value capture**, **capital-intensive capacity ownership**, **application/workflow economics**, and **residual-capacity pressure on non-AI markets**.

## 2. Current evidence anchors

### NVIDIA system platform

NVIDIA FY27 Q2 revenue was **US$96.221B**, Data Center revenue **US$89.0B**, GAAP gross margin **75.0%**, and GAAP operating income **US$63.734B**. This demonstrates exceptional seller-side value capture in the current system-stack cycle.

Source: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027

### TSMC and advanced manufacturing

TSMC's 2025 HPC platform share was **58% of revenue**. Advanced packaging/testing contributed slightly above **10% of revenue**, while management in 2026 Q2 described packaging capacity as tight enough to limit customer growth. A smaller revenue layer can therefore still be a binding delivery constraint.

Sources:
- https://investor.tsmc.com/static/annualReports/2025/english/index.html
- https://investor.tsmc.com/english/quarterly-results/2026/q2

### Memory

Micron disclosed that HBM3E requires roughly **3× the wafer supply of DDR5** for the same node and bit capacity. SK hynix reported FY25 operating margin of **49%** and HBM revenue that more than doubled year over year. Higher resource intensity plus strong demand gives memory makers substantial bargaining power while the cycle remains tight.

SK hynix source: https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/

### Cloud capital

Hyperscalers are spending at historically high levels, but their CapEx is company-wide and sits on the buyer side of the system. High spending does not automatically imply high AI-specific returns. The economic test is utilization and monetization across the life of the assets.

### Consumer transmission

TrendForce reported severe 2026 memory-price pressure in smartphones and other consumer markets. These effects are better described as **residual-capacity pressure and cost transmission** than as a universal “AI tax” with one fixed percentage.

## 3. Value-capture layers

### 3.1 System-stack platforms

A platform captures more value when it controls several complementary layers at once: accelerator systems, interconnect, compiler/runtime interfaces, rack/pod architecture, deployment tooling, and installed workloads.

The economic advantage is not simply market share. It comes from reducing the number of components a customer can substitute independently. If switching hardware also requires changes in kernels, communication primitives, scheduling, topology, validation, and operations, the platform has a system-level moat.

NVIDIA is the clearest current example. The important counterforce is the rise of hyperscaler system stacks—Google Ironwood, AWS Trainium3 UltraServer, Microsoft Maia, and Meta MTIA—which can divert internal workloads and reduce platform profit even if they still consume the same upstream scarce resources.

### 3.2 Advanced foundry and packaging

TSMC captures value from leading-edge manufacturing, but foundry economics and system-platform economics have different denominators and capital structures. Advanced packaging can be a bottleneck even when it is a smaller revenue line than front-end wafers.

The key analytical variable is not “who owns the whole fab.” It is how incremental advanced capacity is allocated among customers with different order scale, prepayments, credit quality, utilization, roadmap certainty, and geopolitical constraints.

### 3.3 HBM and server memory

HBM converts AI demand into disproportionate wafer and cleanroom consumption. While HBM and server-memory demand remain strong, memory makers can capture scarcity value and prioritize higher-value products.

This value capture is cyclical rather than guaranteed. If AI demand weakens, HBM supply expands too far, or conventional-memory capacity returns rapidly, memory margins can compress sharply. A high-margin year should not be mistaken for a permanent structural monopoly.

### 3.4 Power and interconnection

Power providers, grid-connected sites, restartable generation, transformers, and interconnection rights can capture scarcity value where compute demand exceeds executable power supply.

But contracted MW is not energized load. Power assets also carry long duration. The same PPA or interconnection asset that is valuable in S2/S3 can become utilization risk in S4. Power is therefore a scenario-dependent scarcity layer, not an automatically winning asset class.

### 3.5 Hyperscalers

Cloud companies occupy a mixed position: they are large buyers of AI infrastructure; they own data centers and power arrangements; they distribute external model and software demand; they build internal accelerators and system stacks; and they can monetize AI indirectly through advertising, productivity, search, commerce, and internal efficiency.

Their economic outcome cannot be read from CapEx alone. A hyperscaler can spend heavily and still create value if utilization and incremental revenue are high. It can also destroy value if hardware, buildings, and power commitments outrun monetization.

### 3.6 Model companies and AI-native software

Model companies control weights, product distribution, proprietary data, workflow integration, and user relationships, but they do not automatically control the physical infrastructure underneath them.

Their economics should be measured with **AI Software Unit Economics** rather than a fixed SaaS-margin assumption:

```text
AI_Gross_Margin
=
(Revenue
- Model_Inference_Cost
- Retrieval_Storage_Cost
- Tool_API_Cost
- Human_Review_Cost
- AI_Specific_Cloud_Cost)
/ Revenue
```

The strongest model/software businesses will be those that create enough workflow or outcome value to cover compute while preserving distribution and switching costs. Pure per-token scarcity is more vulnerable to open models and price competition.

## 4. Who bears residual pressure?

### 4.1 Smartphones

Smartphones still represent a major TSMC platform and continue to ship at scale. The issue is not disappearance. It is that AI/HPC can absorb a larger share of incremental leading-edge and memory resources, increasing cost or slowing upgrades at the margin.

### 4.2 PCs and gaming

PCs and gaming compete for some of the same advanced logic and memory resources used by data-center products. Where suppliers prioritize higher-value data-center demand, consumer products can experience constrained availability, higher component prices, or slower refresh cycles.

### 4.3 General-purpose servers

General-purpose servers do not use the same full rack-scale AI bill of materials, but they compete with AI infrastructure for server DRAM, power budgets, data-center space, and some upstream semiconductor resources. The pressure is partial and component-specific rather than universal.

### 4.4 Traditional software

Traditional software is not automatically a loser. The relevant distinction is whether AI adds monetizable workflow value faster than it adds inference, tool, review, and infrastructure cost. Products that can price by outcome or embed AI into high-value workflows may expand their profit pool; products that add expensive inference without new willingness to pay may see margin pressure.

## 5. Scenario map

### S1 — Competitive Expansion

Supply loosens, cloud system stacks substitute effectively, and software portability improves. Scarcity premiums fall. Value shifts toward applications, workflows, and differentiated services.

### S2 — Baseline Concentration

System platforms, advanced manufacturing, HBM, packaging, and selected power assets retain strong value capture. Hyperscalers remain large but must manage depreciation and utilization carefully. Consumer markets bear moderate residual pressure.

### S3 — Resource Hegemony

Scarce-layer value capture intensifies. Long-duration commitments and prepayments reinforce leading platforms. Non-AI Residual Capacity remains constrained. The strongest profit pools sit closer to system platforms and physical bottlenecks.

### S4 — Capital Hard Landing

Utilization and forward commitments weaken. GPU/rack pricing and memory/packaging margins compress. Long-duration data-center and power assets clear more slowly. Applications with real workflow value may survive better than infrastructure projects built on weak utilization assumptions.

## 6. Falsification and monitoring

The map should be updated when the following change materially: NVIDIA Data Center growth, gross margin, and supply commitments; TSMC HPC mix and advanced-packaging tightness; HBM/DDR resource intensity and memory-maker margins; cloud system-stack production adoption; hyperscaler utilization and AI monetization; consumer-memory contract pricing and product-cycle behavior; signed power capacity versus actual energization; and model-company revenue quality and compute commitments.

## 7. Boundary conditions

This volume does not treat NVIDIA Data Center revenue as “all global compute rent,” use one fixed consumer cost-inflation percentage, assume a permanent 85% → 55% software-margin path, convert customer revenue share into wafer allocation, or classify every nuclear/power asset as a guaranteed winner.

The durable conclusion is that **AI infrastructure redistributes value according to scarcity, substitutability, capital duration, and workflow monetization. Revenue growth alone does not identify the winner; control of a scarce or difficult-to-substitute layer does.**

## Key public sources for this volume

- NVIDIA FY27 Q2 official results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- TSMC 2025 Annual Report: https://investor.tsmc.com/static/annualReports/2025/english/index.html
- TSMC 2026 Q2 IR / transcript — packaging tightness limiting customer growth: https://investor.tsmc.com/english/quarterly-results/2026/q2
- Micron FY24 Q3 prepared remarks — HBM3E ≈ 3× DDR5 wafer supply: https://investors.micron.com/static-files/4550f98c-1054-4847-a929-c17d520a0564
- SK hynix FY25 official results: https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
