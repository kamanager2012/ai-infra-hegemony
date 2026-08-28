# Part II · Chapter 13: Anchor Compute Buyer Effect — How Model Companies Reshape Infrastructure

## 1. Model companies are moving from compute tenants to Infrastructure Anchor Buyers

The traditional relationship was:

> model company → rent cloud compute

At the largest scale, it is changing toward:

> **model-company demand ↔ cloud / data-center / power buildout**

Multi-year compute commitments, dedicated campuses, chip selection, and capacity reservation give infrastructure providers greater revenue visibility.

## 2. Anchor Compute Buyer Effect

The mechanism can be written as:

> **long-duration model demand → infrastructure-financing certainty → earlier data-center/power buildout → earlier chip/HBM/packaging reservation → priority capacity for anchor workloads**

Model-company demand has therefore become an upstream signal for capital formation, not merely a passive consequence of hyperscaler investment.

## 3. OpenAI Stargate: from nominal commitment to secured / construction state

OpenAI announced Stargate in January 2025, with a plan to invest **US$500B over four years** in U.S. AI infrastructure.

The long-run objective was later described as securing 10 GW of U.S. AI infrastructure by 2029.

The status moved further forward in 2026. On **April 29, 2026**, OpenAI said Stargate had **surpassed the 10 GW secured-capacity milestone** and had added more than 3 GW in the prior 90 days. On **June 1, 2026**, the **1 GW The Barn** data-center campus in Michigan broke ground.

These states must remain separate:

> commitment / secured capacity / construction / energized capacity / utilization

More than 10 GW secured does not mean more than 10 GW is already energized and operating.

## 4. Anthropic / AWS: an anchor workload can also accelerate custom silicon

Anthropic disclosed in April 2026 that:

- its future ten-year commitment to AWS technologies is **more than US$100B**;
- it can access **up to 5 GW** of capacity;
- it is already using **more than 1M Trainium2 chips**;
- by the end of 2026 it expects close to **1 GW of Trainium2/3 capacity**.

Model-company demand can therefore become an important anchor workload for cloud custom silicon.

The public disclosure establishes scale. It does not establish a "largest customer" ranking without a disclosed workload-share denominator.

## 5. Anchor Buyers gain demand-side power, not ownership of the physical stack

A model company can influence:

- demand certainty;
- chip / system selection;
- cloud roadmaps;
- rack deployment;
- power planning;
- infrastructure financing.

But it does not normally own the leading-edge foundry, HBM fab, advanced-packaging fab, or transmission grid.

Anchor Buyer power is therefore an increase in demand-side bargaining and coordination—not full supply-chain ownership.

## 6. Why changing clouds is not merely changing the bill

A model company chooses a full system composed of accelerator, HBM, interconnect, compiler/runtime, scheduler, rack/pod, and cloud operations.

Migration can require kernel adaptation, distributed-training changes, performance tuning, observability rework, and operational revalidation.

That creates infrastructure switching costs and helps explain why exit costs from long-duration capacity commitments can be much higher than those of ordinary SaaS contracts.

## 7. Algorithmic efficiency directly changes Anchor Demand

If architecture sharply lowers the compute required for the same capability, a model company can reduce long-duration capacity commitments, improve buyer bargaining power, and increase utilization risk for infrastructure providers.

If lower unit cost stimulates workload volume even faster, long-duration commitments can continue to expand.

Anchor Buyer Demand is therefore a dynamic demand function, not a fixed exponential curve.

## 8. How Anchor Buyer demand propagates through the supply chain

Large-scale model demand can transmit through:

> model demand → cloud CapEx / custom silicon → accelerator/HBM/packaging → data-center power → grid/generation

AI-infrastructure analysis therefore has to look beyond hyperscaler CapEx and system-vendor commitments and track model-company long-duration contracts as an independent variable.

## 9. Risk: Anchor Buyers can also amplify stranded-capacity risk

If model-company revenue, financing, workload growth, or architecture assumptions reverse, long-duration infrastructure commitments can become low-utilization assets.

The variables that matter include:

- cancellation / rescheduling;
- take-or-pay / minimum commitments;
- utilization;
- project financing;
- customer concentration;
- power and data-center delivery state.

## 10. Current judgment

As of August 2026, large model companies constitute a distinct Anchor Buyer category inside AI infrastructure.

OpenAI Stargate's secured-capacity and construction states, together with Anthropic/AWS's ten-year compute commitment and Trainium deployment, show that model workloads are shaping data-center, power, and custom-silicon buildout.

Anchor Buyer commitments are therefore an important leading indicator between S2/S3 expansion and S4 capital clearing.

## Key public sources

- OpenAI — Announcing The Stargate Project: https://openai.com/index/announcing-the-stargate-project/
- OpenAI — Building the compute infrastructure for the Intelligence Age, 2026-04-29; surpassed 10 GW milestone: https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/
- OpenAI — Michigan 1 GW The Barn groundbreaking, 2026-06-01: https://openai.com/index/stargate-michigan-data-center/
- Anthropic / AWS — >US$100B over ten years; up to 5 GW; >1M Trainium2: https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
