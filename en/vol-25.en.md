# Volume 25: Hyperscaler System-Stack Competition

Chinese source edition: [vol-25.md](../vol-25.md)

> Retrieval and revision cutoff: **2026-08-27**. The hyperscaler response is no longer well described as “ASIC vs. GPU.” The relevant unit is the complete cloud system stack.

## 1. The cloud response has moved from custom chips to custom systems

Google, AWS, Microsoft, and Meta should no longer be analyzed only through isolated accelerator programs.

The competitive object now includes:

- accelerators;
- HBM;
- compiler/runtime;
- scale-up fabric;
- scale-out networking;
- racks and pods;
- orchestration;
- internal workloads.

This report uses **Cloud System-Stack Substitution** to describe hyperscaler alternatives to the NVIDIA platform.

## 2. Why hyperscalers can build complete systems

The four large clouds possess several advantages that traditional chip startups do not:

- massive internal workloads;
- data-center scale;
- software-engineering depth;
- customer distribution;
- capital;
- power procurement;
- custom-silicon teams.

Most importantly:

> **they are their own first major customer.**

A hyperscaler can deploy internally before it has a general-purpose external developer ecosystem.

That allows the system to mature inside large captive workloads.

## 3. Google: TPU and Ironwood

Google's TPU program already spans multiple generations of:

- accelerator architecture;
- compiler/runtime;
- cluster design.

Ironwood extends that path toward:

- high HBM capacity;
- large pods;
- AI inference and training systems.

Google's competitive asset is therefore not just a chip.

It is:

> **TPU + XLA/software + interconnect + cloud workload**

That is a complete system-stack logic.

## 4. AWS: Trainium

AWS Trainium similarly combines:

- custom accelerators;
- Neuron software;
- UltraServer architecture;
- AWS workloads.

The Anthropic/AWS long-duration compute relationship gives this stack an **Anchor Compute Buyer**.

Trainium is therefore better understood as:

> **cloud + chip + software + anchor workload**

rather than an isolated accelerator product.

That combination can accelerate software maturity and utilization.

## 5. Microsoft: Maia

Maia's strategic value comes from Microsoft's combination of:

- Azure workloads;
- model and customer demand;
- internal software;
- data-center scale.

Long-run competitiveness depends on whether Maia can develop:

- stable compiler/runtime support;
- high utilization;
- strong scale-up capability;
- large HBM configurations;
- broad Azure deployment.

Microsoft does not need to replicate the entire CUDA ecosystem on day one.

It needs to generate a durable cost or performance advantage across a sufficiently large internal workload base.

## 6. Meta: MTIA

Meta controls very large recommendation and generative-AI workloads.

The MTIA path demonstrates a different strategy:

> **specialize first for internal workloads, then expand the system scope.**

The goal is not “run every model.”

It is:

> **reduce long-run TCO for Meta's largest workloads.**

That is a different optimization target from a general-purpose GPU platform.

## 7. Two simultaneous effects on NVIDIA

### 7.1 Platform-profit diversion

Successful hyperscaler systems can:

- reduce external GPU purchases;
- lower software dependence;
- improve buyer bargaining power;
- retain more platform economics inside the cloud.

### 7.2 Upstream resource competition

The same systems can continue to require:

- advanced logic;
- HBM;
- advanced packaging;
- power.

Cloud custom silicon can therefore weaken NVIDIA's platform profit while intensifying competition for upstream scarce resources.

Both effects can occur at the same time.

## 8. When does custom silicon become real substitution?

A competitive single-chip benchmark is not enough.

System-stack substitution requires, at minimum:

1. mature compiler/runtime support;
2. large-cluster scaling;
3. high utilization;
4. acceptable workload-migration cost;
5. HBM and packaging supply;
6. stable rack/pod deployment;
7. material production workload share.

Only when these conditions are satisfied does custom silicon become meaningful system substitution.

A chip program without production workload remains an option, not a replacement stack.

## 9. What hyperscaler CapEx actually means

Cloud CapEx is not equivalent to “buying more NVIDIA GPUs.”

It also funds:

- custom silicon;
- networking;
- memory;
- data centers;
- power.

Higher hyperscaler CapEx can therefore support NVIDIA and accelerate alternatives to NVIDIA at the same time.

This is why cloud CapEx should not be divided by NVIDIA revenue to manufacture a “compute tax rate.”

The accounting objects and strategic uses differ.

## 10. Likely long-run equilibrium: workload segmentation

The most plausible long-run outcome is not that one side completely eliminates the other.

It is **workload segmentation**.

### NVIDIA can remain strongest in

- general-purpose frontier training;
- broad external developer ecosystems;
- heterogeneous enterprise workloads.

### Hyperscaler custom systems can be strongest in

- massive internal workloads;
- repeatable model architectures;
- vertically optimized inference and training;
- cloud-specific TCO optimization.

The boundary will continue to move as software maturity and workload structure change.

## 11. Current judgment

As of **August 2026**:

- cloud custom silicon is a real competitive force;
- the competitive unit has moved upward to the system stack;
- frontier training has not fully moved away from NVIDIA;
- custom systems still depend heavily on advanced logic, HBM, packaging, and power.

Cloud System-Stack Substitution is therefore one of the most important variables that can move the industry from **S2 Baseline Concentration** toward **S1 Competitive Expansion**.
