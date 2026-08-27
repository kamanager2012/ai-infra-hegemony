# Volume 02: NVIDIA Platform Dominance and the System-Stack Moat

Chinese original: [../vol-02.md](../vol-02.md)

## 1. The competitive unit has moved above the GPU

NVIDIA's most important current advantage is not the isolated performance of one GPU generation. It is the ability to organize accelerators, HBM, interconnect, compilers, runtimes, and rack-scale systems into one procurement and deployment unit.

The official GB200 NVL72 configuration is:

| Component | Official configuration |
|---|---|
| GPU | **72 Blackwell GPUs** |
| CPU | **36 Grace CPUs** |
| HBM | **13.4 TB HBM3E** |
| CPU memory | **17 TB LPDDR5X** |
| Scale-up domain | 72-GPU NVLink domain |
| Rack design | Liquid-cooled rack-scale system |

Source: https://www.nvidia.com/en-us/data-center/gb200-nvl72/

This changes the buyer's comparison object. In the accelerator-card era, FLOPS, memory capacity, and card price dominated. At rack scale, buyers must compare at least:

1. GPU / accelerator architecture;
2. HBM capacity and bandwidth;
3. scale-up interconnect;
4. scale-out networking;
5. compiler/runtime;
6. distributed-training stack;
7. rack, power, and cooling;
8. real workload-migration cost.

A cheaper ASIC therefore does not automatically imply a cheaper or more competitive training system.

## 2. CUDA/NVLink is not a separately disclosed “software tax”

CUDA's strategic value is that it lowers software-friction inside NVIDIA's system while increasing the engineering cost of moving production workloads to another stack.

The effect spans:

- kernels and operator ecosystems;
- compiler/runtime;
- profiling and debugging;
- collective communication;
- inference software;
- framework integration;
- distributed scheduling;
- system-level coordination with NVLink/NVSwitch.

This lock-in cannot be converted into an undisclosed fixed “software premium.” NVIDIA does not report a standalone CUDA contribution to rack gross margin.

The defensible conclusion is narrower: **the software stack raises system-level substitutability costs and therefore strengthens pricing power and retention.**

Open migration routes exist. oneAPI, UXL, ROCm, cloud-native compilers, and other multi-architecture approaches continue to improve. Public evidence, however, does not yet establish that frontier AI workloads can migrate from CUDA/NVLink to another general-purpose stack at large scale with negligible engineering cost.

## 3. The moat is system-definition power

NVIDIA's platform control can be separated into four layers.

### 3.1 Compute

The GPU remains the central compute unit, but the commercial product has moved from accelerator cards toward integrated systems.

FY26 Data Center revenue was **$193.737B**. Compute and networking are both material parts of the platform economics.

### 3.2 Interconnect

NVLink/NVSwitch moves multi-GPU systems away from independent accelerators connected only through an external network and toward a large shared compute domain.

This matters particularly for frontier training, where bottlenecks include:

- all-to-all communication;
- model parallelism;
- memory movement;
- synchronization;
- cluster utilization.

### 3.3 Software

CUDA, TensorRT-LLM, NeMo, NIM, and related tooling reduce deployment friction inside the NVIDIA ecosystem.

These assets strengthen system usability and switching costs. They do **not** prove the existence of a separately audited second software profit pool.

### 3.4 Roadmap coordination

Hopper → Blackwell → Rubin is not a GPU-only roadmap. It coordinates:

- logic node;
- HBM generation;
- advanced packaging;
- interconnect;
- rack architecture;
- power and cooling design.

By FY27 Q2, NVIDIA disclosed that Rubin had entered **full production**. The competitive unit is therefore continuing to move toward the complete system rather than back toward a single-chip comparison.

## 4. Why high profitability can become capacity-reservation power

Key financial anchors include:

| Metric | Value |
|---|---:|
| FY26 free cash flow | **$96.575B** |
| FY26 operating income | **$130.387B** |
| FY27 Q2 revenue | **$96.221B** |
| FY27 Q2 Data Center revenue | **$89.0B** |
| FY27 Q2 GAAP gross margin | **75.0%** |
| FY27 Q2 GAAP operating income | **$63.734B** |

Supply-related commitments reached **$119.0B** at FY27 Q1.

Strong platform economics can therefore be recycled into the next generation of:

- wafers;
- HBM;
- advanced packaging;
- substrates;
- networking components;
- system inventory.

The reinforcing mechanism is:

**high system profit → stronger resource reservation → greater delivery certainty → stronger customer retention → larger next-generation system revenue.**

This is not an automatic monopoly formula. Suppliers still optimize customer diversification, credit, utilization, long-duration contracts, geopolitical exposure, and bargaining balance.

## 5. What cloud custom silicon is actually attacking

Google TPU/Ironwood, AWS Trainium, Microsoft Maia, and Meta MTIA should not be understood as a few ASICs challenging a GPU.

The real substitution path is **Cloud System-Stack Substitution**.

A credible substitute must coordinate:

- accelerator architecture;
- compiler/runtime;
- framework support;
- HBM;
- scale-up fabric;
- scale-out network;
- rack/pod architecture;
- large internal workloads;
- developer migration.

These systems can reduce NVIDIA's value capture in chips, software, and interconnect while still consuming the same advanced logic, HBM, advanced packaging, and power.

Two effects can therefore occur simultaneously:

1. **Platform-profit diversion** — cloud-owned stacks capture economics that would otherwise accrue to NVIDIA.
2. **Upstream resource competition** — those same stacks increase demand for scarce manufacturing and power resources.

## 6. The actual boundary of the moat

The strongest part of NVIDIA's moat is the interaction among:

> GPU + HBM + NVLink/NVSwitch + CUDA/runtime + rack architecture + deployment tooling

But the moat is not unbreakable.

The following developments would materially weaken platform dominance:

- cloud custom silicon reaches large-scale frontier training;
- open software materially lowers CUDA migration cost;
- alternative scale-up fabrics mature;
- HBM and advanced-packaging supply becomes materially loose;
- large customers deploy the same workloads across multiple system stacks;
- regulatory remedies force interface opening or limit tying in ways that lower switching costs.

## 7. Current judgment

As of August 2026, NVIDIA has clear system-level platform dominance, but the evidence does not justify saying competition is over.

The more precise state is:

- competition is moving from chips to system stacks;
- NVIDIA still has the most mature commercial general-purpose AI system stack;
- cloud custom silicon has become a real second technical path;
- the competitive question is shifting from “who has the better chip?” toward “who controls total system cost, migration, supply, and utilization?”

That system-level framing is the starting point for the supply-chain analysis in the rest of the report.

---

Evidence grades and forward assumptions follow [Research Methodology and Evidence Grading](研究方法与证据分级.en.md), [Core Evidence Ledger](核心证据台账.en.md), and [Core Hypothesis Matrix](核心假设矩阵.en.md).