# Part II · Chapter 11: NVIDIA's Expansion from Accelerator Vendor to AI Factory

## 1. NVIDIA's expansion is not traditional IDM-style vertical integration

NVIDIA does not control the system by owning leading-edge fabs, HBM fabs, or the full data-center real-estate stack.

Its expansion is better described as:

> **interface control + reference architecture + software/runtime + supply orchestration**

The system boundary now spans GPU / CPU, NVLink / NVSwitch, networking, rack-scale design, liquid-cooling requirements, CUDA/runtime, AI Enterprise, NIM / NeMo, DGX, and cloud-service extensions.

## 2. The rack-scale sales unit changes the role of OEMs and ODMs

In the accelerator-card era, OEMs had wide latitude to define server architecture around the GPU.

At rack scale, power delivery, cooling, fabric, cable topology, firmware, rack layout, and software validation are more tightly coupled to the reference architecture.

This does not mean Dell, HPE, Lenovo, ODMs, or other integrators lose product capability. It means the system-platform owner exerts stronger constraints over whole-system design and qualification.

## 3. Networking has become part of the compute platform

Large-model training and inference increasingly depend on multi-GPU scaling and collective communication.

When accelerators, NVLink/NVSwitch, InfiniBand/Ethernet networking, and the software communication stack are co-designed, the network stops being merely an external component and becomes part of system performance and switching cost.

Platform competition therefore moves from "GPU + arbitrary network" toward a more integrated AI Factory architecture.

## 4. DGX Cloud is primarily a platform extension

Without a separately disclosed large-scale revenue line, DGX Cloud should not be presented as a second business that has already replaced hyperscalers.

Its more defensible strategic functions are:

1. demonstrating the complete NVIDIA architecture;
2. collecting real workload / deployment feedback;
3. lowering the initial adoption barrier for the full stack;
4. increasing NVIDIA's channel and bargaining options relative to hyperscalers.

DGX Cloud is therefore better understood as a platform extension and reference-deployment channel.

## 5. AI Enterprise / NIM / NeMo primarily deepen deployment integration and migration cost

Software products extend the system platform from hardware purchase into model serving, deployment, optimization, enterprise support, and lifecycle management.

Until independent software revenue is disclosed, this report does not estimate a fixed "software tax" or separate software profit pool.

The more accurate strategic effect is:

> **lower deployment friction inside the platform and higher migration friction outside it.**

## 6. Why asset-light orchestration matters

NVIDIA leaves much of the manufacturing CapEx with TSMC, memory vendors, the packaging ecosystem, and infrastructure providers while influencing their expansion through long-duration commitments, prepayments, roadmap coordination, and volume certainty.

The structure is:

> system definition / cash generation stays with the platform → heavy manufacturing CapEx stays with suppliers → the platform uses orders and commitments to reserve future resources

This raises platform capital efficiency and turns external supply elasticity into part of platform strategy.

## 7. Physical AI is the next system extension, but it cannot be mixed with current Data Center profit

Automotive, robotics, simulation, and edge deployment follow the same system logic: hardware architecture, runtime, simulation, developer tooling, and model deployment form a combined platform.

But "strategically important" does not mean "already contributing Data Center-scale revenue."

Physical AI has to be evaluated independently through design wins, deployment scale, revenue, reliability, and ecosystem adoption.

## 8. Seven boundaries to vertical expansion

NVIDIA's system expansion faces real counterforces:

- hyperscaler custom system stacks;
- open compiler/runtime and portability;
- alternative networking;
- customer multi-sourcing;
- regulation / interface remedies;
- physical power and supply constraints;
- China's parallel stack.

If these variables strengthen together, NVIDIA can remain the strongest system platform while losing some bargaining power over system definition.

## 9. The correct meaning of "AI Factory"

AI Factory should not be interpreted as an ownership claim that "every data center is an NVIDIA factory."

It is better understood as a design philosophy in which compute, memory, networking, software, racks, cooling, and deployment are optimized as one production system.

Its industrial importance is that the sales unit, qualification process, supply commitments, and data-center engineering are pulled into one coordinated roadmap.

## 10. Current judgment

As of 2026, the clearest change is that NVIDIA has moved materially from accelerator vendor toward system-platform / AI-Factory architecture.

"Vertical expansion" and "the industry is fully controlled by one platform" remain different propositions.

The next question is whether system definition can continue to translate into long-duration workloads, supply commitments, and cross-generation customer retention with low in-platform migration cost.

## Key public sources

- NVIDIA NIM official product page — optimized inference microservices across cloud, data center, workstation, and edge: https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/
- NVIDIA AI Foundation Models / NeMo — NVIDIA AI Foundry combines foundation models, NeMo, NIM, and DGX Cloud: https://www.nvidia.com/en-us/ai-data-science/foundation-models/
- NVIDIA DGX Cloud Lepton — unified AI platform / compute marketplace and integration with NIM / NeMo: https://developer.nvidia.com/blog/introducing-nvidia-dgx-cloud-lepton-a-unified-ai-platform-built-for-developers/
- NVIDIA FY26 10-K — Data Center, networking, platform, and supply-chain disclosures: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
