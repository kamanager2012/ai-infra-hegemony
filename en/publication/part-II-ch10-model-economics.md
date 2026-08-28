# Part II · Chapter 10: Model Unit Economics, Algorithmic Efficiency, and Open-Source Competition

> **Publication-layer chapter.** Based primarily on [Volume 06](../vol-06.en.md) and aligned with the quantitative boundaries in Part I Chapter 8. This chapter does not assume a fixed end-state for "AI SaaS gross margin." It analyzes model and software competition through **AI Software Unit Economics + demand elasticity**.

## 1. Model companies are not pure software businesses detached from infrastructure

The variable cost underneath APIs, subscriptions, and agent services includes accelerator time, HBM bandwidth, KV cache, storage / retrieval, networking, third-party tools, human review, cloud margin, and serving utilization.

AI software therefore cannot simply inherit the traditional SaaS narrative that an incremental user carries almost no marginal cost.

The relevant unit is:

> **Revenue per completed workflow − total variable AI cost per completed workflow**

## 2. Algorithmic efficiency changes the demand function

DeepSeek-V3 first-party disclosures include:

- 671B total parameters;
- 37B activated parameters;
- 14.8T pre-training tokens;
- 2.664M H800 GPU-hours for pre-training;
- 2.788M H800 GPU-hours for full formal training.

Using the paper's US$2/GPU-hour assumption, 2.788M GPU-hours corresponds to approximately **US$5.576M of formal-training compute conversion**.

That is not full enterprise R&D cost.

The important implication is that frontier capability is not linearly fixed to hardware input. Architecture, sparsity, routing, and memory design can materially change the resources required per unit of capability.

## 3. MLA shows that memory cost can be attacked directly by algorithms

DeepSeek-V2 reports, relative to DeepSeek 67B:

- approximately **93.3% KV-cache reduction**;
- approximately **5.76× maximum generation throughput**.

These figures belong to V2, not V3.

Their economic significance is that the same HBM capacity can support more concurrency, memory traffic per token can fall, and serving utilization can improve.

Lower unit cost, however, does not guarantee lower aggregate infrastructure demand. If lower cost causes token, agent, and workflow volume to rise faster, total demand can still increase.

## 4. Open source compresses model-layer profit first; it does not automatically compress all infrastructure profit

Open-source models increase capability diffusion, private deployment, and model-switching options while pressuring API premiums.

Model-layer switching generally happens faster than replacement of accelerators, HBM, networking, packaging, or data-center infrastructure.

The market can therefore experience:

> **model price compression + infrastructure utilization growth**

This is why falling API prices are not equivalent to falling AI-infrastructure demand.

## 5. The correct GPU-vs-ASIC comparison unit is System TCO

Google TPU, AWS Trainium, Microsoft Maia, and Meta MTIA create alternative compute paths for internal workloads and model companies.

The comparison should not focus on accelerator-die price alone. It must include:

- workload compatibility;
- compiler/runtime maturity;
- HBM / interconnect configuration;
- cluster scaling;
- debugging / porting cost;
- effective utilization.

A theoretically cheaper chip can still produce a higher system TCO if migration, debugging, or utilization are materially worse.

## 6. AI Software Unit Economics

A production workflow should at minimum include:

> **Contribution Margin = Revenue per workflow − inference − retrieval/storage − tools/APIs − retries − human review − compliance/operations**

The metrics that matter include:

- cost per successfully completed task;
- gross margin after inference;
- revenue / productivity value per workflow;
- retention;
- retry / failure rate;
- human-review burden;
- utilization of reserved compute.

## 7. Anchor Buyers let model companies influence infrastructure in reverse

The largest model companies increasingly influence cloud, chip, and power investment through multi-year compute commitments, dedicated data-center projects, and long-duration capacity reservations.

A model company is therefore not permanently limited to passively accepting cloud pricing. At sufficient scale, it can become a demand anchor for infrastructure capital formation.

The same mechanism amplifies risk. If architecture efficiency rises, revenue underperforms, or workloads migrate elsewhere, long-duration capacity commitments can turn into utilization and duration risk.

## 8. Price compression and the Jevons-style rebound

Algorithmic efficiency and open-source competition reduce the unit cost of intelligence.

Aggregate infrastructure demand depends on:

> **Net Infrastructure Demand = Unit Resource Intensity × Total Workload Volume**

If unit resource intensity falls 50% while workload volume grows 4×, total demand still increases.

Long-run analysis therefore has to observe real workload, utilization, and business outcomes rather than training cost, benchmark scores, or token price in isolation.

## 9. Current judgment

As of 2026, a more defensible description is:

- model-layer price competition and capability diffusion are real;
- unit cost continues to fall;
- open source raises buyer bargaining power;
- infrastructure demand has not therefore entered a confirmed decline cycle;
- large model companies are using long-duration commitments to shape infrastructure buildout.

Algorithmic efficiency can become either a **demand interrupter** or a **usage multiplier** for infrastructure. Which effect dominates can only be determined through workload volume, utilization, and unit economics.

## Key public sources

- DeepSeek-V3 Technical Report: https://arxiv.org/abs/2412.19437
- DeepSeek-V2: https://github.com/deepseek-ai/DeepSeek-V2
