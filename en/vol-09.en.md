# Volume 09: Transmission from AI Infrastructure into the Physical Supply Chain

Chinese source edition: [vol-09.md](../vol-09.md)

> Retrieval and revision cutoff: **2026-08-27**. AI infrastructure does not “take all chips.” The relevant mechanism is selective transmission through manufacturing layers shared by AI systems and non-AI products.

## 1. The shock is selective, not economy-wide

The first products exposed to AI-infrastructure expansion are those that share scarce upstream resources such as:

- advanced logic;
- HBM and DRAM;
- advanced packaging;
- high-end substrates;
- power-management components;
- networking components.

This volume therefore analyzes **supply-chain transmission**, not a generalized claim that all manufacturing is entering a semiconductor shortage.

The correct question is which non-AI products share the same scarce layer, and how much residual capacity remains after higher-value demand absorbs the increment.

## 2. First transmission layer: PCs and gaming

Consumer GPUs and data-center accelerators share parts of the advanced manufacturing system.

NVIDIA has publicly disclosed Gaming supply constraints in prior periods, showing that consumer GPU supply is not completely insulated from Data Center allocation.

PCs also face a second transmission path:

> **higher HBM / server demand  
→ memory vendors change product mix  
→ conventional DDR5 residual supply changes  
→ channel pricing and system configuration respond**

PCs can therefore face both:

- GPU-allocation pressure;
- memory-residual pressure.

The impact may appear through availability, configuration, or pricing rather than an outright halt in shipments.

## 3. Second transmission layer: general-purpose servers

General servers do not necessarily use HBM, but they consume large amounts of DDR5 RDIMM.

TrendForce estimates that **HBM + RDIMM represent approximately 51% of 2026 DRAM bits**.

That means general-server memory already sits inside a memory pool strongly shaped by AI and server demand.

Traditional servers are therefore not fully separated from the AI cycle simply because they use DDR5 instead of HBM.

AI infrastructure can affect their cost structure indirectly through memory allocation.

## 4. Third transmission layer: smartphones

The main overlap between smartphones and frontier AI is in:

- leading-edge logic;
- LPDDR;
- selected packaging;
- power-management components.

TSMC's 2025 smartphone platform still represented approximately **29% of revenue** and continued to grow.

AI has therefore not “displaced smartphones.”

A more accurate description is:

- HPC incremental growth is faster;
- leading-edge investment is more heavily oriented toward HPC;
- some memory and manufacturing allocation can tilt toward higher-value AI/server demand.

The likely consumer effect is not disappearance of the smartphone market, but pressure on flagship input costs and slower migration of some mid-tier products to newer nodes.

## 5. Automotive transmission is slower and more selective

Automotive semiconductors have:

- long qualification cycles;
- high reliability requirements;
- extensive mature-node usage.

Automotive therefore does not compete directly with frontier AI across every manufacturing step.

The more relevant overlap is in:

- central compute;
- memory;
- power management;
- selected advanced packaging.

Automotive is better described as a **second-stage selective transmission channel** than as part of the first wave of a broad semiconductor shortage.

## 6. Manufacturing inflation often appears as an “upgrade tax”

When an industry faces residual-capacity pressure, firms can respond in several ways:

1. raise prices;
2. reduce specifications;
3. delay upgrades;
4. remain on older nodes or use alternative suppliers.

The effect of AI infrastructure on the real economy therefore may not first appear as stopped production.

More common outcomes include:

- higher flagship BOMs;
- longer replacement cycles;
- slower diffusion of high-end features;
- stronger product segmentation.

This is a structural **upgrade tax** created by upstream resource competition.

## 7. China's parallel supply can buffer some domestic residual pressure

China's expanding capabilities in logic, DRAM, NAND, and device manufacturing can reduce some domestic consumer-side supply pressure.

But substitution has to be separated by layer:

- **smartphones / consumer computing:** stronger replacement capability;
- **workstations / general compute:** partial replacement;
- **frontier AI:** still dependent on simultaneous progress in advanced logic, HBM, packaging, interconnect, and software.

Domestic supply expansion can therefore change the cost structure of some terminal products without automatically removing global frontier-AI bottlenecks.

## 8. Digital transformation adds a second cost channel

Manufacturing companies adopting AI also face costs unrelated to semiconductor input prices:

- cloud inference;
- software integration;
- data pipelines;
- security and compliance;
- workflow redesign.

A manufacturer can therefore face both:

1. upstream hardware inflation;
2. downstream AI software and service costs.

The ROI of AI adoption cannot be evaluated from model capability alone.

A simplified economic relationship is:

```text
Net Productivity Value
= Productivity Gain
- Total AI Adoption Cost
```

The second term includes deployment and organizational costs as well as inference.

## 9. Current judgment

AI-infrastructure expansion is already capable of transmitting pressure into selected non-AI markets through memory, advanced packaging, and leading-edge allocation.

The evidence supports:

> **selective transmission + product stratification + residual-capacity pressure**

more strongly than it supports:

> **AI crowding consumer electronics, automotive, and traditional servers out of manufacturing altogether.**

The most useful forward indicators are:

- DDR5 and LPDDR pricing;
- consumer-GPU availability;
- smartphone node mix;
- general-server shipments;
- automotive advanced-compute BOM trends;
- memory-vendor product mix.

Only if several of these weaken together should the transmission mechanism be upgraded from selective scarce-layer pressure to a broader manufacturing-cost shock.

## Key public sources for this volume

- TrendForce — 2026 HBM + RDIMM = 51% of DRAM bit supply: https://www.trendforce.com/presscenter/news/20260825-13198.html
