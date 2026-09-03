# Part II · Chapter 12: The Second System Stack — How Hyperscaler Substitution Actually Works

## 1. The test is workload substitution, not chip availability

The strategic question is not whether a hyperscaler can design an ASIC. It is whether an alternative stack can **absorb production workload at an acceptable TCO, migration cost, reliability, and scale — and keep doing so across generations**.

Google TPU, AWS Trainium, Microsoft Maia, and Meta MTIA therefore must be evaluated as system stacks:

- accelerator;
- HBM / memory subsystem;
- compiler/runtime;
- scale-up fabric;
- scale-out network;
- rack/pod;
- orchestration;
- production workload.

The report treats **cloud system-stack substitution** as an economic substitution test, not a separate theory. A benchmark win is not enough. The stack must survive production utilization, software friction, and workload-specific system economics.

## 2. Captive workload is the structural advantage

The structural difference between the major clouds and an ordinary chip startup is that hyperscalers simultaneously possess:

- massive internal workloads;
- data-center scale;
- compiler / software engineering;
- cloud distribution;
- capital;
- power procurement;
- custom-silicon teams.

They do not need to reproduce CUDA's entire external developer ecosystem on day one.

If an in-house system continuously lowers cost on a large captive workload, it already creates real economic value and generates production feedback for improving the compiler, interconnect, rack, and deployment tooling.

That produces a powerful learning loop:

> **internal workload → production feedback → system optimization → lower TCO → more internal workload**

## 3. Google: TPU is already a system stack

Google's TPU path spans multiple generations.

Ironwood further moves the product definition toward large pod/system scale, combining custom accelerators with Pathways runtime/software, high-bandwidth interconnect, HBM, and Google Cloud workloads.[^1] By **March 31, 2026**, Google Cloud's TPU release notes marked **TPU7x / Ironwood generally available**, moving the evidence beyond product announcement into external cloud availability.[^1]

Google's competitive unit is therefore:

> **TPU + compiler/runtime + network + pod + captive workload + cloud distribution**

If this system continuously lowers total cost of ownership for selected training or inference workloads, it can divert part of NVIDIA's platform profit even without becoming the universal development platform for the entire industry.

## 4. AWS: Trainium is a system, not a component

AWS Trainium has likewise moved from accelerator toward system.

Trainium3 UltraServers, the Neuron software stack, AWS networking/data-center deployment, and large cloud workloads together form an alternative system.[^2] AWS announced **general availability of EC2 Trn3 UltraServers** on December 2, 2025, so this stack is not merely a roadmap artifact.[^2]

AWS also benefits from long-duration anchor demand. Anthropic has publicly deepened its compute relationship with AWS, giving Trainium a large workload base on which to iterate system economics.[^3]

But "having an anchor workload" is not the same as replacing NVIDIA's external ecosystem.

The variables that still need to be tested include large-cluster scaling, utilization, software maturity, migration cost, and external-customer adoption.

## 5. Microsoft: Maia matters only if Azure-scale economics close

The correct standard for Microsoft Maia 200 is not whether it supports every model on day one.[^4] Microsoft states that Maia 200 is **already deployed in its US Central datacenter region**, with US West 3 next, and will serve workloads including OpenAI's GPT-5.2 models, Microsoft Foundry, Microsoft 365 Copilot, and internal synthetic-data / reinforcement-learning pipelines.[^4] That is first-party deployment evidence, not an audited disclosure of fleet-wide utilization, workload share, or realized TCO.

It is whether Maia can create a stable cost advantage on a sufficiently large Azure / Microsoft internal workload.

Long-run competitiveness depends on:

- compiler/runtime maturity;
- scale-up / scale-out capability;
- HBM configuration and supply;
- rack/data-center integration;
- high utilization;
- broader Azure deployment.

If those conditions hold across a large enough captive workload, Maia can divert part of external platform economics.

Becoming a general external substitute would require lower migration cost and a wider ecosystem.

## 6. Meta: specialization can substitute without generality

Meta operates very large recommendation, ranking, and generative-AI workloads.

MTIA 300 is not designed first and foremost to become a general-purpose accelerator.[^5] It targets the company's most important internal workloads and gradually organizes silicon, software, networking, and rack deployment into a custom full-stack solution. Meta's August 2026 engineering disclosure includes a **"Performance in Production"** result on a **150-billion-parameter production recommendation model running across 40 accelerators**.[^5] This is meaningful production-workload evidence, while the reported performance comparison remains vendor-reported rather than an external audit.

The economic objective is:

> **give the company's largest workloads a lower long-run TCO.**

MTIA does not need to beat general-purpose GPUs across every workload to create value.

## 7. Substitution changes platform economics before it changes upstream scarcity

### 7.1 Platform-rent diversion

In-house systems can reduce external accelerator purchases, lower dependence on an external software/platform stack, improve procurement bargaining power, and keep more economics inside the cloud platform.

### 7.2 Upstream scarcity can persist

Next-generation custom systems still need advanced logic, HBM, advanced packaging, networking, and power.

Their expansion can therefore increase competition for the same upstream scarce resources used by NVIDIA.

The combined result is:

> **Cloud custom silicon can weaken NVIDIA platform profit while intensifying competition for TSMC / HBM / packaging / power.**

The two effects are not contradictory.

## 8. Cloud CapEx is not an NVIDIA-revenue proxy

Hyperscaler CapEx includes custom silicon, third-party accelerators, networking, memory, data centers, power, offices, fulfillment assets, and other categories. Fiscal periods, PPE definitions, and lease accounting also differ across companies.

Therefore:

> **Cloud CapEx ≠ AI hardware subtotal ≠ NVIDIA purchases**

Higher CapEx can support NVIDIA shipments while also accelerating systems designed to substitute for NVIDIA.

The four-cloud CapEx numbers cannot be compared directly with NVIDIA revenue to construct an "AI compute tax rate."

## 9. Algorithmic efficiency is a separate axis

Algorithmic and architectural efficiency directly affect system demand, but they are a different competitive axis from hyperscaler custom silicon.

Efficiency can:

- reduce compute / memory required for the same workload;
- lower serving cost;
- increase hardware utilization;
- stimulate additional token / workflow demand.

Efficiency gains can therefore reduce unit hardware demand while increasing aggregate infrastructure demand through demand elasticity.

DeepSeek training-cost, architecture-efficiency, and unit-intelligence economics are analyzed in [Chapter 10](part-II-ch10-model-economics.md). This chapter does not repeat GPU-hours or KV-cache figures, so the same evidence has one canonical home.

---

## 10. Evidence standard for real substitution

Single-chip benchmarks are not enough.

At least the following variables must be observed together:

1. mature compiler/runtime;
2. large-cluster scaling;
3. high utilization;
4. acceptable workload-migration cost;
5. sustainable HBM / packaging / power supply;
6. stable rack/pod deployment;
7. significant production workload share.

Success on internal workloads can already create real economic substitution.

But broader erosion of an external general-purpose platform additionally requires:

- cross-customer portability;
- cross-workload reliability;
- external developer adoption;
- persistently lower migration cost.

---

## 10A. Two thresholds: internal economics and external ecosystem

A cloud custom system can succeed at two distinct levels.

### Internal Economic Substitution

A custom stack already creates real economic substitution if, inside the hyperscaler's own or anchor workloads, it can:

- run reliably;
- sustain high utilization;
- deliver lower TCO than the external alternative;
- continue iterating across generations.

This level does not require reproducing the entire CUDA external ecosystem.

### External Ecosystem Substitution

To weaken a general-purpose external platform more broadly, the system additionally needs:

- external customer adoption;
- developer portability;
- broader workload coverage;
- low migration cost;
- stable commercial support;
- multi-generation compatibility.

Therefore:

> **internal success ≠ external ecosystem replacement**

Internal success can still materially change hyperscaler procurement, bargaining power, and long-run platform-profit distribution.

## 11. The likely equilibrium is workload segmentation

The long-run structure need not involve one side eliminating the other.

A plausible equilibrium is **workload segmentation**.

That segmentation must also distinguish **training topology** from **inference topology**. Frontier training is typically more sensitive to large-scale collective communication, scale-up / scale-out fabrics, and synchronization efficiency. Inference requirements are more workload-dependent, with memory capacity / bandwidth, latency, batching, power efficiency, and cost per token often carrying greater weight. At the same time, this does not mean networking becomes irrelevant for inference: Google Ironwood still integrates a 9,216-chip pod with dedicated ICI, while Microsoft states that Maia 200 scales over standard Ethernet to clusters of up to 6,144 accelerators.[^1][^4]

The report therefore does not generalize frontier-training interconnect barriers to all inference workloads, nor does it assume that custom silicon / Ethernet makes large-scale inference network-insensitive. The correct comparison is **memory, network, latency, utilization, and TCO for the specific workload topology**.

### Areas where NVIDIA can remain stronger

- general-purpose frontier training;
- broad external developer ecosystems;
- heterogeneous enterprise workloads;
- workload portability across customers.

### Areas where hyperscaler custom stacks can be stronger

- massive internal workloads;
- repeatable architecture;
- vertically optimized training / inference;
- cloud-specific TCO optimization;
- captive distribution.

The boundary depends on software maturity, memory supply, interconnect, workload structure, and migration cost.

---

## 11A. System-orchestration rent is workload-topology dependent

The value of a general-purpose system orchestrator is not constant across workload mix.

For highly synchronized frontier training, large-scale collective communication, scale-up fabrics, failure recovery, and cluster-wide software coordination can command a high premium because system-level execution risk is expensive.

As a larger share of production shifts toward inference or narrower fine-tuning workloads, some workloads can become:

- more partitionable;
- more latency / memory / power constrained than collective-communication constrained;
- easier to place on vertically optimized captive systems;
- more sensitive to cost per token / verified outcome than to maximum general-purpose flexibility.

That can reduce the economic rent attached to a universal training-oriented coordination stack **for specific workloads** and increase the value of hyperscaler custom systems.

But the report rejects a fixed threshold such as “inference exceeds 80%, therefore orchestration power collapses.” Public evidence does not support such a universal cutoff, and large-scale inference can still require substantial memory systems, networking, scheduling, reliability, and fleet orchestration.

The relevant monitoring variables are therefore:

- production workload mix by training / inference where disclosed;
- custom-silicon share of captive production workloads;
- cost per token / cost per verified workload on alternative stacks;
- memory and network intensity by workload topology;
- migration cost and software portability;
- external-customer adoption versus captive internal use.

The strategic question is not whether inference “kills” system coordination. It is **which coordination layers remain scarce and monetizable as workload topology changes.**

---

## 12. Current read

As of August 2026, the most defensible description is:

- cloud custom silicon is already a real competitive force;
- the evidence is no longer launch-only: Ironwood / TPU7x and Trn3 UltraServers are generally available, Maia 200 is deployed, and MTIA 300 has vendor-reported production-workload evidence;
- the competitive unit has moved from custom chip to complete system stack;
- hyperscalers are competing across accelerator, software, interconnect, rack/pod, and workload economics together;
- comparable public data on production-workload share, utilization, migration cost, and realized TCO remain incomplete;
- frontier training and the broad external ecosystem have not been shown to have systematically moved away from NVIDIA;
- custom systems still compete heavily for advanced logic, HBM, advanced packaging, and power.

Therefore:

> **cloud system-stack substitution is one of the structural variables most capable of moving S2 — Baseline Concentration toward S1 — Competitive Expansion.**

Its strength must be measured through production workload share, migration cost, utilization, external adoption, and upstream-resource dependence—not product-launch count.

## 13. What would change the view

The cloud system-stack substitution thesis should be downgraded if custom systems remain confined to small internal workloads and the following conditions persist:

- production utilization remains low;
- migration / debugging cost stays high;
- external customer adoption remains weak;
- multi-generation software compatibility remains insufficient;
- HBM / packaging / power access does not improve;
- hyperscalers increase dependence on one external platform again.

The evidence that would genuinely support S1 is not another chip launch. It is simultaneous improvement in production workload share, TCO, portability, and external adoption.

## References

[^1]: Google Cloud, “Ironwood TPU,” system architecture and 9,216-chip pod context, https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; Google Cloud TPU release notes, 2026-03-31, TPU7x / Ironwood generally available, https://docs.cloud.google.com/tpu/docs/release-notes
[^2]: Amazon Web Services, 2025-12-02, general availability of Amazon EC2 Trn3 UltraServers powered by Trainium3, https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/
[^3]: Anthropic, “Anthropic and Amazon expand collaboration,” long-duration AWS compute commitment, https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
[^4]: Microsoft, “Maia 200: the AI accelerator built for inference,” 2026-01-26, Maia 200 deployed in US Central with additional regions planned and named Microsoft/OpenAI workloads, https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/
[^5]: Meta Engineering, “MTIA 300,” 2026-08-24, production-recommendation workload evidence and system/network co-design, https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
