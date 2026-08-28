# Volume 17: Ultimate Risks in AI Infrastructure — Physical, Capital, Substitution, and Institutional Constraints

Chinese source edition: [vol-17.md](../vol-17.md)

> Retrieval and revision cutoff: **2026-08-28**. AI-infrastructure risk is not one “bubble probability.” The system can fail through several independent channels, and the most severe outcomes come from cascades across them.

## 1. Five distinct risk families

This report separates AI-infrastructure risk into five categories:

1. physical bottlenecks;
2. power bottlenecks;
3. capital and utilization risk;
4. system substitution;
5. regulatory and geopolitical risk.

These risks can develop independently.

They can also reinforce one another through a cascade.

That is why a single risk score or bubble probability is too coarse for the system being analyzed.

## 2. Physical risk: logic, HBM, packaging, and interconnect must all work

A frontier AI system depends on several physical layers:

- advanced logic;
- HBM;
- advanced packaging;
- interconnect.

Failure or tightness at any one layer can limit total system delivery.

Micron's FY24 Q2 prepared remarks use an **industrywide, same-node, same-bits** scope: HBM3E requires roughly **3× the wafer supply of DDR5**. That shows how HBM can amplify DRAM wafer pressure, but it is not a fixed Micron-specific constant.

TSMC's first-party statements on advanced-packaging tightness show that packaging is not merely a supporting process; it can directly limit customer growth.

Physical risk is therefore not a single transistor-scaling problem.

It is a **multi-layer integration risk**.

## 3. Power risk: hardware can exist but remain unusable

GB200 NVL72-class public product documentation is roughly **120 kW per rack**. That is a product-level density anchor, not evidence that a campus is already carrying the corresponding live load; whether power becomes the next bottleneck depends on interconnection, energization, and utilization.

Relevant risks include:

- grid delays;
- substation constraints;
- transformer shortages;
- permitting delays;
- insufficient firm generation;
- cooling constraints.

If power becomes the dominant bottleneck, the first signal is not necessarily a collapse in GPU prices.

The sequence can instead be:

- deployment delay;
- lower utilization;
- slower next-generation orders.

The physical system is only productive once it can be energized and used.

## 4. Capital risk: utilization may fail to cover the asset burden

AI infrastructure combines:

- rapid hardware iteration;
- large annual CapEx;
- long-duration power and data-center assets;
- uncertain workflow monetization.

A simplified economic relationship is:

```text
Economic Return
=
Revenue from Deployed Compute
- Depreciation
- Power
- Operations
- Financing
```

If deployed compute is underutilized, capital pressure can first become visible through:

- impairments;
- second-hand asset prices;
- CapEx guidance;
- order cancellations;
- supply-commitment changes.

The key variable is not how much was spent, but whether the installed asset base earns enough cash over its economic life.

## 5. Model-efficiency risk can change the demand function

Techniques such as:

- MLA;
- MoE;
- quantization;
- speculative decoding;

can reduce compute, memory, or communication required per useful task.

If efficiency improves faster than workload volume grows for a sustained period, infrastructure demand can weaken.

If lower unit cost unlocks much more usage, total infrastructure demand can still rise.

Algorithmic efficiency is therefore one of the largest demand uncertainties.

Its effect depends on **demand elasticity**, not on efficiency improvement alone.

## 6. Cloud system-stack substitution affects platform and upstream layers differently

Google, AWS, Microsoft, and Meta can use self-designed systems to:

- divert platform profit away from NVIDIA;
- lower internal workload cost;
- increase buyer bargaining power.

But those systems can still rely on:

- TSMC advanced logic;
- HBM;
- advanced packaging;
- data-center power.

System substitution can therefore reduce concentration at the platform layer while leaving upstream physical competition unchanged or even stronger.

That distinction is essential.

A custom accelerator does not automatically create a second memory, packaging, or power supply chain.

## 7. China's parallel stack can create a second resource-gravity center

If China closes the frontier stack at scale across:

- advanced logic;
- HBM;
- packaging;
- interconnect;
- software;

then global AI infrastructure can develop a second major resource-gravity center.

That would reduce dependence on one global system ecosystem.

If key advanced layers remain constrained, the global industry is more likely to retain substantial technical segmentation.

The relevant question is therefore system closure, not one domestic-substitution percentage.

## 8. Regulatory risk changes interfaces and commercial rules, not physics

The most consequential regulatory interventions are not necessarily fines.

They include:

- interface openness;
- tying restrictions;
- non-discriminatory supply;
- structural separation.

These measures can directly change:

- switching cost;
- customer bargaining power;
- platform-profit capture.

But regulation cannot directly create physical capacity.

Legal and manufacturing risk must therefore remain separate analytical channels.

## 9. Geopolitical risk is amplified by physical concentration

AI infrastructure is concentrated around:

- a small number of leading foundries;
- a small number of HBM suppliers;
- specific advanced-packaging geographies;
- specific power regions.

Relevant geopolitical risks include:

- export controls;
- trade restrictions;
- supply interruptions;
- regional conflict;
- industrial-policy fragmentation.

Possible consequences include:

- duplicated capacity;
- lower global efficiency;
- higher inventory;
- parallel technology ecosystems.

Geopolitical risk can therefore raise resilience spending even when aggregate global demand is unchanged.

## 10. Risk cascades matter more than isolated shocks

The most dangerous state is not one risk increasing in isolation.

It is a sequence such as:

**power delay  
→ lower utilization  
→ weaker buyer ROI  
→ lower next-cycle CapEx  
→ lower hardware orders  
→ easing HBM/packaging tightness  
→ lower supplier CapEx**

This is the reverse side of the **Rolling Bottleneck Cascade**.

A system can move from scarcity to overcapacity because one downstream bottleneck changes the economics of the layers above it.

## 11. Current risk ranking

As of **August 2026**:

### High-certainty risks already visible

- HBM and advanced-packaging tightness;
- rapidly rising CapEx;
- power-delivery pressure;
- model and software price competition.

### Medium-certainty risks

- cloud system-stack substitution;
- expansion of China's parallel stack;
- regulatory intervention.

### Systemic risks not yet sufficiently demonstrated

- industry-wide chronic underutilization;
- large-scale stranded AI assets;
- broad order cancellation;
- full capital hard landing.

The last group remains important, but it should not be promoted into the present fact layer without synchronized evidence.

## 12. Falsification framework

Any thesis that AI infrastructure will remain highly concentrated must be revised if evidence shows several of the following:

- packaging and HBM become persistently abundant;
- supply commitments decline materially;
- frontier cloud training moves away from NVIDIA at scale;
- power constraints create persistent deployment failure;
- utilization falls materially;
- China's parallel stack closes at scale;
- structural regulatory remedies materially reduce switching costs.

The value of risk analysis is not predicting the exact day a cycle breaks.

It is defining in advance:

> **which observable facts would force the original thesis to change.**

## Key public sources for this volume

- Micron FY24 Q2 prepared remarks — HBM3E ≈ 3× DDR5 wafer supply: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
