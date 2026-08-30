# Part II · Chapter 13: Anchor Compute Buyers — How Long-Duration Demand Pulls Infrastructure Forward

## 1. Frontier model demand can pull infrastructure forward

At smaller scale, a model company is primarily a compute tenant. At frontier scale, durable demand can become a financing input for chips, data centers, land, and power.

The relationship changes from:

> model company → rent existing compute

toward:

> **model-company commitment → revenue visibility → financing certainty → earlier cloud / data-center / power / chip buildout**

The analytical question is not whether a model company "owns the stack." It is whether its demand is large and durable enough to change when upstream capacity gets financed, reserved, and built.

## 2. Demand certainty becomes a capital-formation input

The mechanism can be written as:

> **long-duration model demand → infrastructure-financing certainty → earlier data-center/power buildout → earlier chip/HBM/packaging reservation → priority capacity for anchor workloads**

Model-company demand has become an upstream signal for capital formation, not merely a passive consequence of hyperscaler investment.

## 3. OpenAI / Stargate: delivery state matters more than headline scale

OpenAI announced Stargate in January 2025, with a plan to invest **US$500B over four years** in U.S. AI infrastructure.[^1]

The long-run objective was later described as securing **10 GW** of U.S. AI infrastructure by 2029.[^2]

The status moved further forward in 2026. On **April 29, 2026**, OpenAI said Stargate had **surpassed the 10 GW secured-capacity milestone** and had added more than 3 GW in the prior 90 days.[^2] On **June 1, 2026**, the **1 GW The Barn** data-center campus in Michigan broke ground.[^3]

These states must remain separate:

> commitment / secured capacity / construction / energized capacity / utilization

More than 10 GW secured does not mean more than 10 GW is already energized and operating.

### 3.1 PORTS-Pike: anchor demand now reaches LPS and credit support

On August 17, 2026, NVIDIA disclosed its role in the PORTS-Pike Technology Campus with SB Energy in Ohio. NVIDIA is providing credit support to secure land, power, and shell (LPS) capacity; the initial deployment is designed for **4.25 IT-GW** of AI-factory capacity. OpenAI is the customer, while SB Energy will build, own, and operate the data center under a **20-year lease** to OpenAI. Phased capacity is planned to begin coming online in **2028**.[^5]

The significance lies not only in scale; the transaction structure has also changed:

> **Anchor model demand + system-platform credit support + infrastructure developer + long-duration lease**

This shows a system seller participating directly in the bridge between a model company's demand/credit profile and long-duration physical-infrastructure finance.

The state boundaries must remain explicit:

- 4.25 IT-GW is initial deployment **design capacity**, not 2026 energized load;
- future PORTS-Pike capacity is buildout, not current active compute;
- a 20-year lease improves revenue visibility but also raises customer-concentration and duration risk;
- secured land / power / shell does not prove final compute utilization.

On August 26, 2026, NVIDIA management further said on the FY27 Q2 earnings call that OpenAI's existing and planned NVIDIA Compute commitments total approximately **12 GW**.[^6] This is platform-side management commentary about demand visibility. It is not evidence that OpenAI already has 12 GW of energized capacity.

The relationship between PORTS-Pike's **4.25 IT-GW** and OpenAI's previously disclosed **>10 GW secured capacity** is not stated in public materials; this report neither adds the two figures nor assumes a subordination relationship.

---

## 4. Anthropic / AWS: anchor workload can accelerate a second stack

Anthropic disclosed in April 2026 that:[^4]

- its future ten-year commitment to AWS technologies is **more than US$100B**;
- it is securing **up to 5 GW of new compute capacity**;
- it is already using **more than 1M Trainium2 chips**;
- by the end of 2026 it expects close to **1 GW of Trainium2/3 capacity** to be coming online.

The nearly 1 GW end-2026 figure is a deployment milestone within the broader collaboration and should not be added to the up-to-5-GW figure as a separate capacity pool.

Model-company demand can become an important anchor workload for cloud custom silicon.

The public disclosure establishes scale. It does not establish a "largest customer" ranking without a disclosed workload-share denominator.

### 4.1 xAI / Colossus: the self-built variant

xAI is the case of a model company entering infrastructure construction directly. In its December 2024 first-party update, xAI said **Colossus** had become fully operational in **122 days** using **100,000 NVIDIA Hopper GPUs**, and that it planned to double the cluster to a combined **200,000 Hopper GPUs**.[^7] The case shows a model company directly organizing large-scale compute infrastructure instead of relying only on pre-existing cloud capacity.

This path is more direct than Stargate or Anthropic/AWS: rather than renting capacity through a cloud or a joint venture, the model company itself drove front-loaded capital formation in land, power, and chips. Anchor Buyers can guide upstream capital formation through more than one mode: long-duration leased commitments and self-built buildouts can coexist.

The xAI case is subject to the same state boundaries: Colossus going online is not full utilization, and an expansion plan is not installed capacity.

## 5. Anchor Buyers gain coordination power, not ownership

A model company can influence:

- demand certainty;
- chip / system selection;
- cloud roadmaps;
- rack deployment;
- power planning;
- infrastructure financing.

But it does not normally own the leading-edge foundry, HBM fab, advanced-packaging fab, or transmission grid.

Anchor Buyer power is an increase in demand-side bargaining and coordination—not full supply-chain ownership.

## 6. Long-duration commitments create switching costs

A model company chooses a full system composed of accelerator, HBM, interconnect, compiler/runtime, scheduler, rack/pod, and cloud operations.

Migration can require kernel adaptation, distributed-training changes, performance tuning, observability rework, and operational revalidation.

That creates infrastructure switching costs and helps explain why exit costs from long-duration capacity commitments can be much higher than those of ordinary SaaS contracts.

## 7. Anchor demand still depends on workload economics

If architecture sharply lowers the compute required for the same capability, a model company can reduce long-duration capacity commitments, improve buyer bargaining power, and increase utilization risk for infrastructure providers.

If lower unit cost stimulates workload volume even faster, long-duration commitments can continue to expand.

Anchor-buyer demand is a dynamic demand function, not a fixed exponential curve.

## 8. Anchor demand propagates through the infrastructure chain

Large-scale model demand can propagate across the full chain:

> **model demand → cloud CapEx / custom silicon → accelerator / HBM / packaging → data center → power → grid / generation**

AI-infrastructure analysis must look beyond:

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

## 9. Risk: concentration and duration mismatch

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

## 10. Monitoring Anchor-Buyer strength

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

A headline commitment is not the endpoint of the analysis.

The decisive question is:

> **Does long-duration demand ultimately convert into high-utilization, monetizable production workload?**

---

## 11. Current read

As of August 2026, large model companies constitute a distinct Anchor Buyer category within AI infrastructure.

OpenAI Stargate's secured-capacity and construction milestones, Anthropic/AWS's ten-year compute commitment and Trainium deployment, xAI's self-built Colossus buildout, and PORTS-Pike's LPS/credit-support structure show that model workloads are now shaping:

> **cloud architecture, custom silicon, data-center buildout, power procurement, and infrastructure finance**

Anchor-buyer commitments are a key leading indicator connecting **S2/S3 expansion** with **S4 capital clearing**. The leading-indicator value of this signal is supported so far by three documented cases (Stargate, Anthropic/AWS, and xAI Colossus) and must be re-tested across additional full cycles.

They can accelerate AI-infrastructure capital formation, but under weak utilization they can also amplify stranded-capacity and duration-mismatch risk.

## 12. What would change the view

The anchor-buyer mechanism should be downgraded if:

- long-duration commitments are broadly delayed, reduced, or renegotiated;
- secured capacity fails for extended periods to become energized / utilized capacity;
- anchor-workload utilization remains persistently weak;
- model-company monetization cannot cover long-duration infrastructure obligations;
- project finance becomes increasingly dependent on stronger seller support rather than customer / third-party cash flow.

Conversely, larger headline contract values or additional secured GW should not, by themselves, strengthen this chapter's thesis without delivery and utilization evidence.

## References

[^1]: OpenAI, “Announcing The Stargate Project,” 2025-01, https://openai.com/index/announcing-the-stargate-project/
[^2]: OpenAI, “Building the compute infrastructure for the Intelligence Age,” 2026-04-29, surpassed 10 GW secured-capacity milestone, https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/
[^3]: OpenAI, “Building the infrastructure for the Intelligence Age in Michigan,” 2026-06-01, 1 GW The Barn campus groundbreaking, https://openai.com/index/stargate-michigan-data-center/
[^4]: Anthropic, “Anthropic and Amazon expand collaboration for up to 5 gigawatts of new compute,” 2026-04-20, >US$100B over ten years, up to 5 GW of new compute capacity, and >1M Trainium2 chips, https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
[^5]: NVIDIA, “NVIDIA Guarantees SB Energy's PORTS-Pike Technology Campus in Ohio to Exclusively Host NVIDIA AI Compute,” 2026-08-17, initial 4.25 IT-GW design capacity, LPS credit support, 20-year OpenAI lease, and phased online plan beginning in 2028, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx
[^6]: NVIDIA, FY27 Q2 Earnings Call transcript, 2026-08-26, management commentary that OpenAI existing and planned NVIDIA Compute commitments total approximately 12 GW, https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf
[^7]: xAI, “xAI raises $6B Series C,” 2024-12-23, first-party disclosure that Colossus used 100,000 NVIDIA Hopper GPUs, became fully operational in 122 days, and was planned to double to a combined 200,000 Hopper GPUs, https://x.ai/news/series-c
