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

OpenAI announced Stargate in January 2025, with a plan to invest **US$500B over four years** in U.S. AI infrastructure.[^1]

The long-run objective was later described as securing **10 GW** of U.S. AI infrastructure by 2029.[^2]

The status moved further forward in 2026. On **April 29, 2026**, OpenAI said Stargate had **surpassed the 10 GW secured-capacity milestone** and had added more than 3 GW in the prior 90 days.[^2] On **June 1, 2026**, the **1 GW The Barn** data-center campus in Michigan broke ground.[^3]

These states must remain separate:

> commitment / secured capacity / construction / energized capacity / utilization

More than 10 GW secured does not mean more than 10 GW is already energized and operating.

### 3.1 PORTS-Pike: Anchor demand is moving into Land + Power + Shell and credit support

On August 17, 2026, NVIDIA disclosed its role in the PORTS-Pike Technology Campus with SB Energy in Ohio. NVIDIA is providing credit support to secure land, power, and shell (LPS) capacity; the initial deployment is designed for **4.25 IT-GW** of AI-factory capacity. OpenAI is the customer, while SB Energy will build, own, and operate the data center under a **20-year lease** to OpenAI. Phased capacity is planned to begin coming online in **2028**.[^5]

The significance is not only the scale. The transaction structure has changed:

> **Anchor model demand + system-platform credit support + infrastructure developer + long-duration lease**

This shows a system seller participating directly in the bridge between a model company's demand/credit profile and long-duration physical-infrastructure finance.

The state boundaries must remain explicit:

- 4.25 IT-GW is initial deployment **design capacity**, not 2026 energized load;
- future PORTS-Pike capacity is buildout, not current active compute;
- a 20-year lease improves revenue visibility but also raises customer-concentration and duration risk;
- secured land / power / shell does not prove final compute utilization.

On August 26, 2026, NVIDIA management further said on the FY27 Q2 earnings call that OpenAI's existing and planned NVIDIA Compute commitments total approximately **12 GW**.[^6] This is platform-side management commentary about demand visibility. It is not evidence that OpenAI already has 12 GW of energized capacity.

---

## 4. Anthropic / AWS: an anchor workload can also accelerate custom silicon

Anthropic disclosed in April 2026 that:[^4]

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

Large-scale model demand can propagate across the full chain:

> **model demand → cloud CapEx / custom silicon → accelerator / HBM / packaging → data center → power → grid / generation**

AI-infrastructure analysis therefore has to look beyond:

- NVIDIA revenue;
- hyperscaler CapEx;
- foundry / memory CapEx.

It must also track independently:

- model-company long-duration contracts;
- secured capacity;
- project construction;
- utilization;
- commitment rescheduling.

If Anchor Buyer commitments keep expanding and are absorbed by real workloads, the capital-formation force behind S2/S3 strengthens.

If commitments are delayed, reduced, renegotiated, or underutilized, S4 risk rises.

---

## 9. Risk: Customer Concentration + Duration Mismatch

Anchor Buyers improve financing certainty, but they also concentrate risk.

If a large infrastructure project depends on a small number of model-company workloads, capital recovery becomes more exposed to those customers' future:

- revenue;
- financing;
- technical roadmap;
- workload growth;
- contract performance.

At the same time, AI hardware has a relatively short technology cycle while:

- data-center shells;
- power contracts;
- grid interconnections;
- generation assets

have much longer economic lives.

That creates a structural mismatch:

> **shorter-cycle AI workload / compute technology vs longer-cycle infrastructure obligation**

If the model-company growth thesis fails, a long-duration commitment can move from a financing anchor to a stranded-capacity risk.

---

## 10. What to monitor to determine whether Anchor Buyers are strengthening

### Strengthening signals

- long-duration compute commitments continue to expand;
- secured capacity grows;
- dedicated campus / power projects move into construction;
- custom silicon receives more anchor workloads;
- utilization and workload revenue grow together;
- commitments are renewed or extended.

### Weakening signals

- project rescheduling;
- commitment renegotiation;
- cancellation;
- utilization below plan;
- model-company financing or revenue pressure;
- capacity delivery materially outrunning workload growth.

Headline commitment is therefore not the endpoint.

The decisive question is:

> **Does long-duration demand ultimately convert into high-utilization, monetizable production workload?**

---

## 11. Current judgment

As of August 2026, large model companies constitute a distinct Anchor Buyer category inside AI infrastructure.

OpenAI Stargate's secured-capacity and construction states, Anthropic/AWS's ten-year compute commitment and Trainium deployment, and PORTS-Pike's LPS/credit-support structure show that model workloads are now shaping:

> **cloud architecture, custom silicon, data-center buildout, power procurement, and infrastructure finance**

Anchor Buyer commitments are therefore a key leading indicator connecting **S2/S3 expansion** with **S4 capital clearing**.

They can accelerate AI-infrastructure capital formation, but under weak utilization they can also amplify stranded-capacity and duration-mismatch risk.

## 12. What evidence would force this chapter to change its judgment

The Anchor Compute Buyer Effect should be downgraded if:

- long-duration commitments are broadly delayed, reduced, or renegotiated;
- secured capacity fails for extended periods to become energized / utilized capacity;
- anchor-workload utilization remains persistently weak;
- model-company monetization cannot cover long-duration infrastructure obligations;
- project finance becomes increasingly dependent on stronger seller support rather than customer / third-party cash flow.

Conversely, larger headline contract values or additional secured GW should not, by themselves, strengthen this chapter's thesis without delivery and utilization evidence.

## References

[^1]: OpenAI, “Announcing The Stargate Project,” 2025-01, https://openai.com/index/announcing-the-stargate-project/
[^2]: OpenAI, “Building the compute infrastructure for the Intelligence Age,” 2026-04-29, surpassed 10 GW secured-capacity milestone, https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/
[^3]: OpenAI, “Stargate Michigan Data Center,” 2026-06-01, 1 GW The Barn campus groundbreaking, https://openai.com/index/stargate-michigan-data-center/
[^4]: Anthropic, “Anthropic and Amazon expand collaboration,” 2026-04, >US$100B over ten years, up to 5 GW, and >1M Trainium2 chips, https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
[^5]: NVIDIA, “NVIDIA Guarantees SB Energy's PORTS-Pike Technology Campus in Ohio to Exclusively Host NVIDIA AI Compute,” 2026-08-17, initial 4.25 IT-GW design capacity, LPS credit support, 20-year OpenAI lease, and phased online plan beginning in 2028, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx
[^6]: NVIDIA, FY27 Q2 Earnings Call transcript, 2026-08-26, management commentary that OpenAI existing and planned NVIDIA Compute commitments total approximately 12 GW, https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf
