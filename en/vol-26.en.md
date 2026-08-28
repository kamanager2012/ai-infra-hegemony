# Volume 26: Model Companies, Anchor Compute Buyers, and Infrastructure Co-Build

Chinese source edition: [vol-26.md](../vol-26.md)

> Retrieval and revision cutoff: **2026-08-28**. Large model companies are increasingly influencing infrastructure investment through long-duration demand. Announced investment, reserved capacity, constructed capacity, energized capacity, and utilization remain separate states.

## 1. Model companies are moving from compute tenants toward long-duration infrastructure buyers

The traditional model-company relationship was straightforward:

> model company → rents cloud compute.

By 2026, the relationship has become materially more complex.

Large model companies increasingly influence:

- multi-year compute commitments;
- dedicated data-center projects;
- long-duration accelerator procurement;
- power reservation;
- infrastructure co-investment.

This report calls the mechanism the **Anchor Compute Buyer Effect**.

The model company may not own the physical infrastructure, but its long-duration demand can shape what gets built.

## 2. Why an Anchor Buyer matters

When a model company can provide large multi-year demand, infrastructure providers gain more revenue visibility.

The mechanism is:

**long-duration model demand  
→ greater revenue visibility for cloud/infrastructure providers  
→ earlier data-center and power construction  
→ earlier chip, HBM, and packaging reservations  
→ higher probability of priority capacity for the model company**

The model company therefore becomes more than a price-taking cloud customer.

Its demand can influence the cloud's capital plan.

## 3. OpenAI and Stargate

Stargate's public ambition is to build very large-scale AI infrastructure in the United States over several years, with an original commitment of **US$500B / 10 GW**.

By October 2025, OpenAI disclosed **more than 8 GW of planned capacity** and **more than US$450B of planned investment over the next three years**. In June 2026, the **1 GW** Michigan Stargate campus broke ground.

The strategic significance is:

> **model demand is being translated directly into land, power, chips, and data-center construction.**

But the states must remain separate:

- announced investment;
- contracted capacity;
- construction;
- energized capacity;
- actual utilization.

A **US$500B commitment** or **>US$450B planned-investment figure** is not the same as cash already spent. Planned or under-construction capacity is not the same as energized, highly utilized compute.

## 4. Anthropic and AWS

Anthropic and AWS have developed a deep long-duration infrastructure relationship.

Public materials provide unusually concrete anchors, including:

- more than **US$100B** of compute commitments over the coming decade;
- the ability to reserve up to **5 GW** of AWS compute capacity;
- large-scale Trainium deployment;
- public use of more than **1M Trainium2 chips**;
- a path toward roughly **1 GW** of Trainium2/3 capacity by the end of 2026.

This matters because an Anchor Buyer can do more than support cloud expansion.

It can also anchor a **custom-silicon ecosystem** with a stable flagship workload.

Model-company demand can therefore influence accelerator competition directly.

## 5. Anchor Buyers still do not own every physical layer

An Anchor Buyer can influence:

- demand certainty;
- chip selection;
- rack deployment;
- cloud roadmaps;
- power planning.

But model companies generally do not own:

- leading-edge foundries;
- HBM fabs;
- advanced-packaging fabs;
- the grid.

Anchor-buyer power is therefore an increase in **demand-side bargaining and coordination power**, not complete ownership of infrastructure.

Physical scarcity remains upstream.

## 6. System-stack dependence still exists

Choosing a compute provider means choosing more than an accelerator.

The production system can include:

- accelerator;
- HBM;
- interconnect;
- compiler/runtime;
- scheduler;
- rack or pod architecture;
- cloud operations.

Changing providers can therefore require:

- model porting;
- kernel adaptation;
- performance tuning;
- distributed-training changes;
- observability changes.

Infrastructure switching cost is a system-stack problem.

The larger and more specialized the workload, the more important that migration burden can become.

## 7. Algorithmic efficiency can strengthen or weaken Anchor Buyer demand

If model architecture materially reduces compute required per unit of capability, a model company may need less long-duration reserved capacity.

That can:

- improve buyer bargaining power;
- reduce future commitment requirements;
- raise utilization risk for the infrastructure provider.

But lower cost can also unlock much higher workload volume.

If elasticity is strong enough, total capacity commitments can still rise.

Anchor Buyer demand is therefore a **demand function**, not a fixed upward curve.

The relevant variable is effective workload volume after efficiency gains.

## 8. Power between model companies and clouds is becoming two-way

The older structure was:

> model company → rents cloud compute.

The emerging structure is:

> **model-company demand ↔ cloud infrastructure buildout**

Model companies still depend on cloud balance sheets and physical assets.

Cloud providers increasingly depend on large model workloads to fill the new capacity they are building.

That creates mutual dependence rather than one-directional customer power.

## 9. Anchor Buyer demand propagates upstream

Large model demand can travel through the infrastructure stack:

**model demand  
→ cloud CapEx  
→ accelerator orders  
→ HBM and advanced packaging  
→ data-center power  
→ grid and generation**

Model companies are therefore becoming an important upstream demand signal for AI-infrastructure capital formation.

Hyperscaler CapEx alone no longer captures the full demand mechanism.

## 10. Anchor Buyer concentration also creates risk

Long-duration anchor demand can make infrastructure easier to finance.

It can also amplify concentration risk.

If a model company experiences:

- weaker-than-expected revenue;
- tighter financing;
- a large architecture-efficiency improvement;
- workload migration to another system;

then infrastructure built around its commitments can face stranded-capacity risk.

The relevant contract variables include:

- take-or-pay terms;
- cancellation rights;
- utilization;
- financing;
- customer concentration.

Nominal contract value is not enough to assess risk.

## 11. Current judgment

Large model companies have moved beyond the role of ordinary cloud customers.

They increasingly act as **Anchor Compute Buyers** whose long-duration demand can shape:

- GW-scale cloud projects;
- custom-silicon roadmaps;
- accelerator and memory commitments;
- power planning.

This mechanism explains why infrastructure providers are willing to build ahead of current usage.

Future AI-infrastructure demand analysis therefore has to track OpenAI, Anthropic, and other large model-company commitments as independent variables alongside hyperscaler CapEx.


## Key public sources for this volume

- Anthropic / AWS compute partnership — >US$100B over 10 years; up to 5 GW; >1M Trainium2 chips: https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
- OpenAI — Announcing The Stargate Project — US$500B / 10 GW long-run framework: https://openai.com/index/announcing-the-stargate-project/
