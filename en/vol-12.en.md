# Volume 12: U.S.–China AI Supply-Chain Competition and China's Parallel Stack

Chinese source edition: [vol-12.md](../vol-12.md)

> Retrieval and revision cutoff: **2026-08-28**. China's substitution capacity must be evaluated by layer. Strength in smartphones and consumer computing does not prove frontier-AI closure; frontier-AI constraints do not imply that China is limited to consumer devices.

## 1. China's AI supply capability must be layered

Any claim that “China can replace” or “China cannot replace” is too broad unless the system is divided into distinct capability layers.

At minimum, the analysis should separate:

1. smartphones and consumer computing;
2. PCs, workstations, and general computing;
3. frontier AI system stacks.

These layers require different combinations of logic, memory, packaging, software, and performance.

China's success in smartphone supply chains therefore cannot be extrapolated directly into complete frontier-AI substitution.

The reverse is also wrong: constraints in frontier AI do not justify the claim that China's semiconductor capability is confined to phones.

## 2. Layer one: smartphones and consumer computing

China has a relatively complete industrial base in this layer, including:

- SoC design;
- mature and selected advanced foundry capability;
- LPDDR and NAND;
- packaging;
- device manufacturing;
- operating-system and application ecosystems;
- a very large domestic market.

The layer is characterized by:

- high volume;
- relatively complete local supply chains;
- domestic demand capable of supporting scale;
- performance requirements different from frontier training.

This is therefore the layer in which parallel domestic supply is easiest to establish at meaningful scale.

## 3. Layer two: PCs, workstations, and general computing

This layer is more difficult.

Important constraints include:

- high-performance CPUs and GPUs;
- the Windows/x86 ecosystem or an alternative desktop stack;
- DDR5;
- workstation software compatibility;
- professional graphics;
- developer tooling and ecosystem depth.

China can expand domestic CPU, GPU, operating-system, memory, and device supply.

But a fully substitutable workstation experience also requires mature application compatibility, development tools, and performance at scale.

The correct description is therefore:

> **partial substitution is expanding, but the layer is neither fully closed nor structurally impossible.**

## 4. Layer three: the frontier AI system stack

Frontier AI requires several advanced layers to work together:

- advanced logic;
- HBM-class memory;
- advanced packaging;
- high-speed interconnect;
- compiler/runtime;
- distributed training;
- rack-scale deployment;
- data-center power.

This is the hardest layer of China's parallel stack.

A breakthrough at one point does not automatically create system-level equivalence.

Examples of incomplete closure include:

- an accelerator without sufficient HBM;
- an HBM prototype without packaging at scale;
- hardware with high software-migration cost;
- a cluster that cannot scale efficiently because of interconnect or power limits.

The unit of comparison must therefore be the **complete system**, not one chip specification.

## 5. Strategic significance of Huawei Ascend / CANN

The strategic importance of Ascend + CANN is not one generation's peak single-card specification.

It is the construction of an accelerator software ecosystem outside CUDA, including:

- compiler/runtime;
- framework adaptation;
- distributed communication;
- model deployment;
- a domestic developer ecosystem.

The relevant progress indicators are therefore:

- frontier-model migration cost;
- large-cluster utilization;
- compiler maturity;
- operator coverage;
- deployment stability;
- workload scale.

Peak FLOPS alone does not answer whether the stack is production-competitive.

## 6. Memory is one of the easiest constraints to underestimate

CXMT's **27 May 2026 SSE registration prospectus** discloses DDR and LPDDR products. Full-text checks for `HBM` and the Chinese term for high-bandwidth memory return no match, so this report makes only the narrow claim that the registration prospectus does not disclose an HBM product line.

That evidence should be interpreted narrowly:

> **the public filing does not disclose an HBM product line.**

It does not prove that no HBM R&D exists.

For industry analysis, however, a complete frontier-AI parallel stack ultimately requires HBM-class memory at verifiable scale.

YMTC's NAND capability strengthens storage supply but does not substitute for HBM or DRAM.

The label “domestic memory” therefore cannot be used as one undifferentiated category.

## 7. Foundry and advanced packaging must be analyzed together

TrendForce's 2026 Q1 foundry-revenue estimates were approximately:

| Foundry | Revenue share |
|---|---:|
| TSMC | **72%** |
| Samsung Foundry (excluding System LSI) | **6.5%** |
| SMIC | **5.1%** |

These are foundry **revenue shares**. They are not measures of frontier-AI wafer capability.

A competitive frontier parallel supply chain also requires:

- advanced packaging;
- substrates;
- HBM integration;
- yield;
- high-volume qualification.

Node progress is therefore necessary but not sufficient.

A logic die without scalable packaging and memory integration does not create a complete frontier system.

## 8. Algorithmic efficiency is an important asymmetric lever

DeepSeek and related developments show that model architecture and algorithms can reduce the amount of hardware required for a given level of capability.

For a supply-constrained ecosystem, that is especially valuable.

Potential levers include:

- sparse architectures;
- memory compression;
- better routing;
- quantization;
- scheduling.

If these techniques reduce compute per useful task, scarce hardware can produce more effective output.

But algorithmic efficiency should not be restated as “physical supply no longer matters.”

Its strategic role is:

> **to raise effective compute productivity under supply constraints.**

It is a multiplier on constrained resources, not a substitute for every missing physical layer.

## 9. Export controls create both short- and long-term effects

Export controls operate in two directions.

### Short term

They can:

- limit access to advanced hardware;
- raise acquisition cost;
- slow frontier-cluster deployment.

### Long term

They can:

- strengthen domestic-substitution incentives;
- increase the strategic value of a parallel ecosystem;
- accelerate local software/hardware integration.

Controls can therefore widen the short-run capability gap while simultaneously increasing the incentive to build a long-run alternative stack.

Which effect dominates depends on the speed of substitution across several layers.

## 10. What would constitute genuine frontier-stack closure?

This report uses a system-level test.

A complete frontier AI parallel stack requires all of the following to become viable at scale:

1. advanced accelerators can be delivered in volume;
2. HBM-class memory can be delivered in volume;
3. advanced packaging can be delivered in volume;
4. high-speed interconnect can support large clusters;
5. compiler/runtime migration cost becomes acceptable;
6. frontier-model training runs stably;
7. data-center power and system deployment can be sustained.

Only when those conditions are simultaneously met is it appropriate to describe the stack as closed at the frontier-system level.

## 11. Current judgment

As of **August 2026**:

- **smartphones / consumer computing:** parallel supply is comparatively strong;
- **PCs / workstations:** substitution capability is expanding but remains incomplete;
- **frontier AI:** an important domestic technology stack exists, but several advanced layers have not yet demonstrated equivalent scale and closure.

The most accurate description is therefore neither “China has fully broken through” nor “China is permanently blocked.”

It is:

> **China is moving from product substitution toward system-stack substitution. The global balance will depend on whether advanced logic, HBM, packaging, interconnect, and software can all reach scale together.**


## Key public sources for this volume

- CXMT 27 May 2026 STAR Market registration prospectus (SSE): https://static.sse.com.cn/stock/disclosure/announcement/c/202605/002170_20260527_23QQ.pdf
- TrendForce, 12 June 2026 — 1Q26 foundry revenue shares (TSMC 72%, Samsung Foundry excluding System LSI 6.5%, SMIC 5.1%): https://www.trendforce.com/presscenter/news/20260612-13095.html
