# Part II · Chapter 12: Hyperscaler System-Stack Competition

## 1. Competition has moved from ASIC vs. GPU to System Stack vs. System Stack

Describing Google TPU, AWS Trainium, Microsoft Maia, and Meta MTIA as "a few ASICs challenging GPUs" no longer captures the 2026 competitive state.

The relevant unit includes at least:

- accelerator;
- HBM;
- compiler/runtime;
- scale-up fabric;
- scale-out network;
- rack/pod;
- orchestration;
- production workload.

This report uses **Cloud System-Stack Substitution** to describe the change.

The metric is not a single-chip benchmark. It is whether an alternative system can deliver sufficiently low TCO, acceptable migration cost, and stable large-scale utilization on real workloads.

## 2. The hyperscaler's unique advantage: it is its own first large customer

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

## 3. Google: TPU is already a combination of chip, software, interconnect, and pod

Google's TPU path spans multiple generations.

Ironwood further moves the product definition toward large pod/system scale, combining custom accelerators with XLA/software, high-bandwidth interconnect, HBM, and Google Cloud workloads.

Google's competitive unit is therefore:

> **TPU + compiler/runtime + network + pod + captive workload + cloud distribution**

If this system continuously lowers total cost of ownership for selected training or inference workloads, it can divert part of NVIDIA's platform profit even without becoming the universal development platform for the entire industry.

## 4. AWS: Trainium combines silicon, Neuron, and UltraServer

AWS Trainium has likewise moved from accelerator toward system.

Trainium3 UltraServers, the Neuron software stack, AWS networking/data-center deployment, and large cloud workloads together form an alternative system.

AWS also benefits from long-duration anchor demand. Anthropic has publicly deepened its compute relationship with AWS, giving Trainium a large workload base on which to iterate system economics.

But "having an anchor workload" is not the same as replacing NVIDIA's external ecosystem.

The variables that still need to be tested include large-cluster scaling, utilization, software maturity, migration cost, and external-customer adoption.

## 5. Microsoft: Maia's value depends on scaled Azure deployment, not copying all of CUDA

The correct standard for Microsoft Maia is not whether it supports every model on day one.

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

## 6. Meta: MTIA shows that narrow-workload specialization can be a valid route

Meta operates very large recommendation, ranking, and generative-AI workloads.

MTIA's logic is not to become a general-purpose accelerator first. It targets the company's most important internal workloads and gradually organizes silicon, software, networking, and rack deployment into a custom full-stack solution.

The economic objective is:

> **give the company's largest workloads a lower long-run TCO.**

MTIA does not need to beat general-purpose GPUs across every workload to create value.

## 7. Cloud custom systems create two simultaneous effects on NVIDIA

### 7.1 Platform-profit diversion

In-house systems can reduce external accelerator purchases, lower dependence on an external software/platform stack, improve procurement bargaining power, and keep more economics inside the cloud platform.

### 7.2 Upstream resource competition

Next-generation custom systems still need advanced logic, HBM, advanced packaging, networking, and power.

Their expansion can therefore increase competition for the same upstream scarce resources used by NVIDIA.

The combined result is:

> **Cloud custom silicon can weaken NVIDIA platform profit while intensifying competition for TSMC / HBM / packaging / power.**

The two effects are not contradictory.

## 8. Cloud CapEx is not synonymous with NVIDIA revenue

Hyperscaler CapEx includes custom silicon, third-party accelerators, networking, memory, data centers, power, offices, fulfillment assets, and other categories. Fiscal periods, PPE definitions, and lease accounting also differ across companies.

Therefore:

> **Cloud CapEx ≠ AI hardware subtotal ≠ NVIDIA purchases**

Higher CapEx can support NVIDIA shipments while also accelerating systems designed to substitute for NVIDIA.

The four-cloud CapEx numbers cannot be compared directly with NVIDIA revenue to construct an "AI compute tax rate."

## 9. DeepSeek represents another type of competition: public algorithmic cost reduction

Cloud custom silicon is a form of **private cost reduction**: Google, AWS, Microsoft, or Meta optimize their own system economics and keep most of the benefit inside their platforms.

The algorithmic / architectural efficiency represented by DeepSeek is closer to **public cost reduction**. If an architecture materially lowers compute or memory requirements for training or serving, other developers can adopt similar ideas and alter the market-wide unit cost of intelligence.

The auditable DeepSeek-V3 first-party anchors are:

- 671B total parameters;
- 37B activated parameters;
- 14.8T pre-training tokens;
- **2.664M H800 GPU-hours** for pre-training;
- **2.788M H800 GPU-hours** for full formal training.

Using the paper's US$2/GPU-hour assumption, **US$5.576M corresponds to the full formal-training compute conversion**, not full R&D cost.

A separate DeepSeek-V2 result reports **93.3% KV-cache reduction** and **5.76× maximum generation throughput** relative to DeepSeek 67B.

V2 and V3 must not be combined into a single model result.

## 10. Algorithmic cost reduction does not automatically eliminate infrastructure demand

Architecture efficiency can reduce bytes/token, training compute, or serving cost, but aggregate infrastructure demand still depends on demand elasticity: how much workload volume expands after unit cost falls.

DeepSeek-style efficiency can therefore affect hyperscalers in two directions:

- reduce the hardware required for the same workload;
- stimulate larger token / workflow volume through lower prices and broader applications.

The correct question is not "efficiency rose, so CapEx should fall."

It is:

> **After unit workload cost falls, do total effective workload, utilization, and revenue still cover the installed capital base?**

## 11. What would count as real System-Stack Substitution

Single-chip benchmarks are not enough.

At least the following variables need to be observed together:

1. mature compiler/runtime;
2. large-cluster scaling;
3. high utilization;
4. acceptable workload-migration cost;
5. sustainable HBM / packaging / power supply;
6. stable rack/pod deployment;
7. significant real workload share.

Success on internal workloads can create real economics, but "full replacement of NVIDIA's external ecosystem" additionally requires evidence of cross-customer, cross-workload migration and production reliability.

## 12. The long-run equilibrium is more likely to be workload segmentation

The most realistic long-run structure may not be one side eliminating the other.

A more plausible equilibrium is workload segmentation.

**Areas where NVIDIA can remain stronger:**

- general-purpose frontier training;
- broad external developer ecosystems;
- heterogeneous enterprise workloads.

**Areas where hyperscaler custom stacks can be stronger:**

- massive internal workloads;
- repeatable architecture;
- vertically optimized training/inference;
- cloud-specific TCO optimization.

The boundary will move with software maturity, interconnect, memory supply, workload structure, and migration cost.

## 13. Current judgment

As of August 2026, the most defensible description is:

- cloud custom silicon is already a real competitive force;
- the competitive unit has moved from custom chip to complete system stack;
- hyperscalers are attacking software, interconnect, rack/pod, and workload layers rather than only the accelerator die;
- frontier training and the broad external ecosystem have not been shown to have systematically moved away from NVIDIA;
- custom systems still compete heavily for advanced logic, HBM, advanced packaging, and power.

**Cloud System-Stack Substitution is therefore one of the most important structural variables that could move S2 Baseline Concentration toward S1 Competitive Expansion**, but its strength must be measured through real workload share, migration cost, utilization, and upstream-resource dependence.

## Key public sources

- Google Ironwood TPU: https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/
- AWS Trainium3 UltraServers: https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/
- Microsoft Maia 200: https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/
- Meta MTIA 300: https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
- Anthropic / AWS compute collaboration: https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
- DeepSeek-V3 Technical Report: https://arxiv.org/abs/2412.19437
- DeepSeek-V2 repository / technical report: https://github.com/deepseek-ai/DeepSeek-V2
