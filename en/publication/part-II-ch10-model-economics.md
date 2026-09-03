# Part II · Chapter 10: Model Unit Economics, Algorithmic Efficiency, and Open-Model Competition

## 1. Model economics cannot be separated from infrastructure economics

APIs, subscriptions, and agent services sit on top of a real variable-cost stack: accelerator time, HBM bandwidth, KV cache, storage / retrieval, networking, third-party tools, human review, cloud margin, and serving utilization.

AI software should therefore not be modeled by default as near-zero-marginal-cost SaaS.

The relevant unit is:

> **Revenue per completed workflow − total variable AI cost per completed workflow**

## 2. Algorithmic efficiency changes the demand function

DeepSeek-V3 first-party disclosures include:[^1]

- 671B total parameters;
- 37B activated parameters;
- 14.8T pre-training tokens;
- 2.664M H800 GPU-hours for pre-training;
- 2.788M H800 GPU-hours for full formal training.

Using the paper's US$2/GPU-hour assumption, 2.788M GPU-hours corresponds to approximately **US$5.576M of formal-training compute conversion**.

The 2.788M total includes the report's formal pre-training, context-extension, and post-training compute categories. The DeepSeek paper explicitly excludes prior research and ablation experiments from this cost figure; it should therefore not be read as the full enterprise R&D cost.[^1]

The important implication is that frontier capability is not linearly fixed to hardware input. Architecture, sparsity, routing, and memory design can materially change the resources required per unit of capability.

## 3. Algorithms can reduce memory cost directly

DeepSeek-V2 reports, relative to DeepSeek 67B:[^2]

- approximately **93.3% KV-cache reduction**;
- approximately **5.76× maximum generation throughput**.

These figures belong to V2, not V3.

Their economic significance is that the same HBM capacity can support greater concurrency, memory traffic per token can fall, and serving utilization can improve.

Lower unit cost, however, does not guarantee lower aggregate infrastructure demand. If lower cost causes token, agent, and workflow volume to rise faster, total demand can still increase.

### 3A. Price compression does not imply falling aggregate compute demand

Stanford AI Index 2025 provides a historical anchor: at the GPT-3.5-equivalent MMLU performance level used in its comparison, inference cost fell from about **US$20 per million tokens** in November 2022 to about **US$0.07 per million tokens** in October 2024—roughly a **280× decline**.[^3]

That comparison depends on a specific benchmark, model set, and time window. It should not be rewritten as "all model prices fell 280×." What it does establish is narrower:

> **The unit price of a benchmark-equivalent capability can compress rapidly; model-layer rent is not fixed.**

Stanford AI Index 2026 also reports further convergence among leading models on Arena-style evaluations, shifting more competitive pressure toward cost, reliability, and domain-specific performance.[^4]

This strengthens the chapter's core mechanism: **falling model prices and rising total infrastructure demand can coexist**. The decisive variables remain workload volume, resource intensity, and utilization.

## 4. Open models compress model-layer rent before infrastructure rent

Open-model and open-weight availability broaden capability diffusion, private deployment, and model-switching options while putting pressure on API premiums.

**Terminology boundary:** this report uses **open-model** as the broader category and **open-weight** when model weights are available. Open-weight availability does not, by itself, establish open-source licensing or unrestricted downstream rights.

Model-layer switching generally happens faster than replacement of accelerators, HBM, networking, packaging, or data-center infrastructure.

The market can therefore experience:

> **model price compression + infrastructure utilization growth**

This is why falling API prices are not equivalent to falling AI-infrastructure demand.

## 5. GPU vs. ASIC should be compared at System TCO

Google TPU, AWS Trainium, Microsoft Maia, and Meta MTIA create alternative compute paths for internal workloads and model companies.[^5]

The comparison should not focus on accelerator-die price alone. It must include:

- workload compatibility;
- compiler/runtime maturity;
- HBM / interconnect configuration;
- cluster scaling;
- debugging / porting cost;
- effective utilization.

A theoretically cheaper chip can still produce a higher system TCO if migration, debugging, or utilization are materially worse. This is a **report-side system-TCO mechanism**, not a claim that the cited vendors disclose one standardized cross-platform TCO comparison.

## 6. AI software unit economics

At minimum, production-workflow economics should include:

> **Contribution Margin = Revenue per workflow − inference − retrieval/storage − tools/APIs − retries − human review − compliance/operations**

The metrics that matter include:

- cost per successfully completed task;
- gross margin after inference;
- revenue / productivity value per workflow;
- retention;
- retry / failure rate;
- human-review burden;
- utilization of reserved compute.

## 7. Anchor Buyers let model companies shape infrastructure formation

The largest model companies increasingly influence cloud, chip, and power investment through multi-year compute commitments, dedicated data-center projects, and long-duration capacity reservations.

A model company therefore need not remain a passive price taker in cloud infrastructure. At sufficient scale, it can become a demand anchor for infrastructure capital formation.

The same mechanism amplifies risk. If architecture efficiency rises, revenue underperforms, or workloads migrate elsewhere, long-duration capacity commitments can turn into utilization and duration risk.

## 8. Price compression and rebound

Algorithmic efficiency and open-model competition reduce the unit cost of intelligence.

Aggregate infrastructure demand depends on:

> **Net Infrastructure Demand = Unit Resource Intensity × Total Workload Volume**

If unit resource intensity falls by 50% while workload volume grows 4×, total demand still increases.

Long-run analysis therefore must observe real workload volume, utilization, and business outcomes rather than training cost, benchmark scores, or token price in isolation.

Chapter 14 adds a third mechanism: **AI inheritance**. A large share of potential AI workload does not start from zero; it can be layered onto existing ERP, CRM, databases, cloud systems, APIs, digital documents, source code, and established workflows. Workload growth can therefore come not only from more calls per task but from **the penetration of AI into an already large digital installed base**. Long-run demand must consequently be read through unit efficiency, workflow penetration, automation depth, and execution frequency together.

## 9. Long-run competitive variables at the model layer

The most important economic variables for model companies include:

### Capability per Unit Resource

How much useful capability can be produced from a given amount of compute and memory.

### Serving Utilization

Whether reserved infrastructure can sustain high utilization.

### Model Portability

Whether customers can switch between models at low cost.

### Distribution

Who can acquire and retain workloads at low marginal distribution cost.

### Monetization

Whether model capability converts into durable revenue or measurable productivity value.

### Infrastructure Commitments

Whether long-duration compute commitments remain aligned with real workload growth.

The final variable links directly to the Anchor Compute Buyer mechanism developed in Chapter 13.

## 10. Current read

At the August 2026 evidence cutoff, the more defensible description from this chapter's cited evidence is:

- model-layer price competition and capability diffusion are real;
- benchmark-equivalent unit cost has fallen sharply in the cited historical series;
- open-model / open-weight availability increases model portability and buyer options;
- **the sources cited in this chapter do not establish a confirmed decline in aggregate infrastructure demand as a consequence of those model-layer changes**;
- large model companies are using long-duration commitments to shape infrastructure buildout.

Algorithmic efficiency can become either a **demand interrupter** or a **usage multiplier** for infrastructure. Which effect dominates can only be determined through workload volume, utilization, and unit economics.

## References

[^1]: DeepSeek-AI, “DeepSeek-V3 Technical Report,” model architecture and formal-training compute, https://arxiv.org/abs/2412.19437
[^2]: DeepSeek-AI, “DeepSeek-V2,” technical report, MLA / KV-cache and throughput results, https://arxiv.org/abs/2405.04434 ; official repository, https://github.com/deepseek-ai/DeepSeek-V2
[^3]: Stanford HAI, “2025 AI Index Report — Research and Development,” inference-price comparison at a GPT-3.5-equivalent MMLU level, https://hai.stanford.edu/ai-index/2025-ai-index-report/research-and-development
[^4]: Stanford HAI, “2026 AI Index Report — Technical Performance,” frontier-model performance convergence and the shift toward cost, reliability, and domain-specific competition, https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance

[^5]: Google, Ironwood TPU, https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; AWS, Amazon EC2 Trn3 UltraServers / Trainium3, https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ ; Microsoft, Maia 200, https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ ; Meta, MTIA 300, https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
