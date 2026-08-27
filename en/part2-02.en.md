# Macro Essay 2: Platform Concentration and NVIDIA's Hardware–Software System Power

Chinese source edition: [part2-02.md](../part2-02.md)

> Retrieval and revision cutoff: **2026-08-27**. The essay uses official system specifications and company disclosures. It does not reconstruct an undisclosed cabinet price or assign an invented dollar value to “software premium.”

## 1. The core question

Does NVIDIA's platform power come primarily from one accelerator's performance, or from the integration of:

- compute dies;
- HBM;
- NVLink/NVSwitch;
- rack architecture;
- liquid cooling;
- networking;
- CUDA/PTX;
- deployment software?

The evidence supports the second interpretation.

The relevant competitive object is increasingly the **system stack**.

## 2. The official NVL72 system boundary

NVIDIA's official GB200 NVL72 materials specify:

- **72 Blackwell GPUs**;
- **36 Grace CPUs**;
- **13.4 TB HBM3E**;
- **17 TB LPDDR5X**;
- a **72-GPU NVLink domain**;
- liquid-cooled rack-scale architecture.

NVIDIA also describes the system as operating like a single massive GPU.

The strategic implication is not one promotional performance multiple.

It is that the product definition now extends across:

- compute;
- memory;
- fabric;
- mechanical design;
- cooling;
- software.

The sales unit has moved upward.

## 3. Why the interconnect matters

Large models require high-volume communication for:

- tensor parallelism;
- pipeline parallelism;
- expert routing;
- collectives.

Once the model exceeds one device, the fabric becomes part of effective compute.

NVLink/NVSwitch turns scale-up communication into an internal platform capability.

That creates a higher substitution requirement for a competitor:

> **A replacement system must reproduce not only accelerator throughput but also useful scaling across a large accelerator domain.**

A single-card benchmark is therefore insufficient.

## 4. Why software power persists across hardware generations

CUDA, PTX, TensorRT-LLM, NeMo, NIM, and related deployment layers create value through:

- compiler maturity;
- libraries;
- kernels;
- debugging;
- profiling;
- framework integration;
- operational tooling.

PTX and the broader toolchain help software survive hardware transitions.

This creates an accumulated software asset whose replacement cost rises with years of production use.

The platform premium is real as a mechanism.

Its exact dollar share of one rack is not publicly disclosed and should not be fabricated.

## 5. The physical BOM still depends on external suppliers

NVIDIA does not manufacture:

- leading-edge wafers;
- HBM;
- most advanced packaging capacity;
- grid power.

Its platform therefore depends on upstream suppliers.

That dependence creates a paradox:

> **NVIDIA controls more of the system definition while relying on external firms for some of the most physically scarce layers.**

The result is asset-light orchestration.

Cash flow, prepayments, roadmap visibility, and long-duration commitments become tools for coordinating a supply chain the platform company does not own.

## 6. Where cloud system stacks attack

Google, AWS, Microsoft, and Meta increasingly build their own combinations of:

- accelerators;
- software;
- interconnect;
- rack/pod systems;
- internal workloads.

They do not need to reproduce CUDA for every developer.

They only need to produce better economics on sufficiently large captive workloads.

This is the strongest structural counter to NVIDIA:

> **system stack vs. system stack**

rather than ASIC vs. GPU.

## 7. Three forward scenarios

### Scenario A — NVIDIA system premium persists

Frontier training and low-latency inference continue to reward tightly integrated scale-up systems.

CUDA migration cost remains high and buyers continue to value turnkey deployment.

### Scenario B — Hyperscalers internalize large workloads

Custom stacks mature and absorb a large share of internal training and inference.

NVIDIA remains strong externally, but platform profit is increasingly segmented by workload.

### Scenario C — Open portability reduces the software barrier

Compiler/runtime and orchestration layers become more portable across accelerators and fabrics.

The hardware stack remains valuable, but switching cost falls materially.

## 8. What to monitor

The most useful indicators are:

- production-scale workload share on TPU/Trainium/Maia/MTIA;
- cluster utilization on alternative fabrics;
- software migration time and engineering cost;
- HBM and packaging allocation across major system buyers;
- changes in NVIDIA supply commitments;
- whether enterprise deployments remain predominantly CUDA-bound.

The central conclusion is not that NVIDIA has already captured every layer.

It is:

> **NVIDIA's strongest moat is the integration of hardware, memory, fabric, software, rack architecture, and deployment into one repeatable system.**

That is the level at which competitors have to win.
