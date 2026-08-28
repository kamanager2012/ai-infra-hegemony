# Volume 06: Model-Company Unit Economics, Algorithmic Efficiency, and Open-Source Competition

Chinese original: [vol-06.md](../vol-06.md)

## 1. Core question

How do algorithmic efficiency, open weights, falling inference prices, and cloud custom silicon change model-company economics without eliminating the physical infrastructure stack underneath them?

This volume separates three questions that older versions mixed together:

1. **Training efficiency:** how much compute is required to reach a given capability level?
2. **Inference unit economics:** what does each useful unit of output cost after model inference, retrieval/storage, tools/APIs, human review, and cloud infrastructure?
3. **Infrastructure dependence:** even if model efficiency improves, which workloads still depend on advanced logic, HBM, packaging, interconnect, racks, and power?

The answer is not “open source kills the model business,” and it is not “better algorithms cancel infrastructure.” Efficiency changes the demand function; it does not automatically remove the underlying system constraints.

## 2. Evidence anchors

### 2.1 DeepSeek-V3: formal training compute is an important counterexample to simple cost extrapolation

DeepSeek-V3 reports **671B total parameters**, **37B activated parameters per token**, and **2.788M H800 GPU-hours** for formal training. The technical report converts that formal-training compute at $2 per H800 GPU-hour to approximately **$5.576M**.

Source: DeepSeek-V3 Technical Report, https://arxiv.org/abs/2412.19437

The scope matters. This number is not the complete economic cost of building DeepSeek-V3. It excludes prior research, architecture exploration, ablations, data work, failed experiments, organizational cost, and the ongoing cost of serving the model. It therefore supports a narrower conclusion: **algorithm/system co-design can materially reduce the formal training-compute bill relative to naive frontier-cost extrapolations.**

### 2.2 Multi-head latent attention changes the memory-demand function

DeepSeek's multi-head latent attention compresses the key/value representation used during autoregressive inference. The **93.3% KV-cache reduction** is a specific DeepSeek-V2 result **relative to DeepSeek 67B**, alongside a reported **5.76× maximum generation throughput**; it is not a universal saving for every model or context. Source: https://github.com/deepseek-ai/DeepSeek-V2 . The durable mechanism is that reducing KV-cache footprint can increase concurrency and lower memory traffic per served token.

That matters because autoregressive decoding is often constrained by memory movement and bandwidth rather than only by peak arithmetic throughput. Better attention architecture can therefore lower the HBM required per unit of useful inference without making HBM, interconnect, or accelerator systems irrelevant.

### 2.3 Cloud custom silicon is now a system-stack competition

Google Ironwood, AWS Trainium3 UltraServer, Microsoft Maia, and Meta MTIA show that hyperscalers are no longer competing only with isolated custom chips. They are building combinations of accelerators, interconnect, compiler/runtime software, racks or pods, internal workloads, and data-center infrastructure.

This creates **Cloud System-Stack Substitution**: internal workloads can move away from NVIDIA where the cloud can control the full deployment path. The key empirical questions are how much training and inference actually migrate, what software-migration cost remains, and whether the alternative stack still competes for the same advanced logic, HBM, advanced packaging, and power.

## 3. Mechanism

### 3.1 Open weights compress model-layer scarcity faster than physical scarcity

Open weights make capability easier to reproduce and compare. When a strong model can be trained with materially lower formal compute and then deployed across multiple providers, the model layer loses some of the scarcity that supported high per-token premiums.

But open weights do not automatically reproduce accelerator supply, HBM capacity, advanced packaging, scale-up / scale-out networking, power and grid connection, optimized compiler/runtime ecosystems, or high-utilization production operations.

The economic consequence is a separation between **model scarcity** and **infrastructure scarcity**. The first can fall quickly; the second may remain constrained.

### 3.2 AI software must be evaluated with AI Software Unit Economics

Traditional SaaS intuition is insufficient because AI-native products carry material variable and semi-variable compute cost.

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

The correct question is not whether AI software “should” have an 85% or 55% gross margin. Those fixed endpoints are not industry facts. The variables that matter include revenue per user or completed outcome, calls/tokens per user, agent-loop depth, routing/batching/caching/quantization, accelerator/cloud price, human-review and tool/API cost, and private-infrastructure utilization.

A lower percentage gross margin can still produce a larger absolute profit pool if AI expands ARPU, usage, or addressable market. Conversely, rapid token-price decline can destroy a model company's economics if usage and product value do not rise fast enough.

### 3.3 Owning infrastructure changes the accounting form, not the physical cost

A model company that rents APIs records an external service cost. A cloud or vertically integrated model company can convert part of that cost into depreciation, power, operations, and capital commitments. The physical resources do not disappear; their accounting location changes.

This is why hyperscaler CapEx and model-company economics must not be collapsed into one line. The clouds can absorb infrastructure depreciation across many workloads, while an independent model company must create enough product value to cover the compute it consumes.

### 3.4 Anchor Compute Buyers change the financing side of the model business

By 2026, model companies are also becoming infrastructure anchor customers.

OpenAI's Stargate program began with a **US$500B / 10 GW** long-run commitment. By October 2025, OpenAI disclosed **more than 8 GW of planned capacity** and **more than US$450B of planned investment over three years**; the 1 GW Michigan campus broke ground in June 2026. Anthropic and AWS announced more than **US$100B** of AWS technology spending over ten years and reservation of up to **5 GW**.

These commitments do not mean all capacity is already energized or utilized. They do show that the model layer can influence the financing and construction of cloud, chip, data-center, and power capacity.

```text
long-duration model demand
→ greater infrastructure-financing certainty
→ earlier cloud / data-center / power construction
→ more stable chip and memory orders
→ priority access to capacity
→ larger training and inference scale
→ future demand commitments
```

This is a two-way dependency. Infrastructure platforms own heavy assets and physical capacity; model companies provide high-value demand and utilization.

### 3.5 Cloud ASIC substitution can reduce platform profit without reducing upstream scarcity

If a hyperscaler moves part of inference from NVIDIA to an internal accelerator, two different effects follow: NVIDIA may lose part of the platform profit pool, while the cloud may still consume advanced logic, HBM, advanced packaging, networking, and power.

Therefore “NVIDIA substitution” and “AI resource-demand reduction” are not the same event. A cloud system stack can be a strong competitive response to NVIDIA while intensifying competition for the same upstream resources.

### 3.6 China's parallel stack must be evaluated layer by layer

China has stronger domestic capability in smartphones, parts of consumer computing, and portions of the accelerator/software stack. Frontier AI remains constrained by the combined maturity and scale of advanced logic, HBM-class memory, advanced packaging, high-speed interconnect, and software migration.

Open models can improve the usefulness of a parallel stack because they reduce dependence on one closed model provider. They do not, by themselves, close every hardware and system-integration gap.

## 4. Scenario implications

### S1 — Competitive Expansion

Algorithmic efficiency improves rapidly, cloud system stacks substitute a meaningful share of training and inference, software portability improves, and upstream supply expands. Model competition intensifies while infrastructure concentration weakens.

### S2 — Baseline Concentration

Open weights and efficiency compress API pricing, but frontier workloads continue to require large-scale advanced infrastructure. Clouds divert some internal workloads while NVIDIA remains a major external platform. Model companies differentiate through workflow integration, distribution, proprietary data, reliability, and long-duration capacity access.

### S3 — Resource Hegemony

Model demand remains high enough that efficiency gains are reinvested into larger workloads, longer context, multimodality, agents, and more inference. Anchor-buyer commitments expand. Physical bottlenecks remain tight even as unit compute efficiency improves. The infrastructure layer captures a large share of value.

### S4 — Capital Hard Landing

Token prices fall faster than useful demand grows, model-company product differentiation weakens, and long-duration compute commitments become underutilized or are rescheduled. GPU/rack pricing and lead times soften before long-duration data-center and power assets can clear.

## 5. What would falsify the main mechanism?

The current framework should be weakened if several of the following become persistent:

- strong models achieve frontier capability with dramatically less total production compute, not only lower formal training compute;
- cloud custom stacks migrate large training and inference workloads with low software-switching cost;
- HBM and advanced packaging stop being scarce even while AI usage remains high;
- inference unit prices fall but model-company revenue per outcome and cash flow rise enough to cover infrastructure comfortably;
- long-duration model-company compute commitments are repeatedly reduced without impairing product growth;
- frontier performance becomes materially less dependent on advanced process nodes, HBM, and rack-scale interconnect.

## 6. Boundary conditions

This volume does **not** treat DeepSeek's $5.576M formal-training conversion as complete R&D cost, one KV-cache compression ratio as universal across models and contexts, fixed 85% → 55% AI-software margins as an observed industry path, cloud custom silicon as proof that upstream resource competition disappears, contract value or reserved GW as already energized load, model-company commitments as guaranteed future utilization, or open weights as equivalent to open hardware/software infrastructure.

The durable conclusion is narrower: **algorithmic efficiency and open competition can materially reduce model-layer scarcity and unit cost, while the physical infrastructure stack can remain scarce. The strategic contest therefore shifts from “who owns the best weights” toward who can combine capability, workflow value, system efficiency, and durable access to compute.**
