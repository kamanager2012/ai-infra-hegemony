# Part I · Chapter 1: Executive Summary and Core Judgments for the Next Decade

## 1. One-sentence judgment

> **The competitive unit in AI infrastructure has moved from the individual chip to the full system stack. Long-run value capture increasingly depends on who can coordinate multiple scarce layers—advanced logic, HBM, advanced packaging, interconnect, software, racks/data centers, and power—and convert those physical resources into highly utilized, portable, cash-generating workloads.**

This is not a claim of permanent monopoly. It describes the current structure of resource competition and the conditions under which concentration could strengthen, weaken, or give way to capital clearing.

## 2. Eight factual anchors that matter most today

### 2.1 NVIDIA's sales unit has moved up to the rack-scale system

The official GB200 NVL72 specification includes **72 Blackwell GPUs, 36 Grace CPUs, 13.4 TB of HBM3E, and 17 TB of LPDDR5X**. The customer is therefore buying a combination of compute, memory, interconnect, software, and rack architecture—not merely an accelerator card.

### 2.2 NVIDIA's seller-side economics remain exceptionally strong

FY27 Q2 revenue was **US$96.221B**, Data Center revenue **US$89.0B**, GAAP gross margin **75.0%**, and GAAP operating income **US$63.734B**; Vera Rubin was in full production.

### 2.3 Forward supply commitments have expanded sharply

NVIDIA's manufacturing, supply, and capacity commitments rose from **US$95.2B** on January 25, 2026 to **US$279B** on July 26, 2026. The Q2 10-Q states that the latest commitments are primarily associated with memory and manufacturing facilities needed for data-center infrastructure systems, but it does not provide a supplier-level split.

### 2.4 TSMC's HPC weight is now above smartphone

In 2025, TSMC's HPC platform accounted for **58%** of annual net revenue and smartphone **29%**; 3 nm / 5 nm / 7 nm accounted for **24% / 36% / 14%** of wafer revenue. Customer revenue share, wafer share, and CoWoS allocation must remain separate denominators.

### 2.5 HBM has become a manufacturing-resource competition layer

Micron disclosed that, on the **same technology node and for the same number of bits**, HBM3E requires approximately **3× the wafer supply of DDR5**. TrendForce forecasts HBM + RDIMM at roughly **51% of 2026 DRAM bit supply**.

### 2.6 Advanced packaging has become a verifiable growth constraint

TSMC said in 4Q24 that relevant capacity was very tight and could not satisfy all customer demand; in 2Q26 it stated more directly that packaging tightness was limiting customer growth. TSMC does not disclose customer-level CoWoS allocation.

### 2.7 Power has become an independent physical constraint

Approximately **120 kW-class racks** and long-duration projects measured in hundreds of MW or GW show that grid interconnection, substations, firm power, permits, and Time-to-Power are now part of system delivery. Contracted, Permitted, Energized, and Utilized MW are not interchangeable.

### 2.8 Cloud custom systems are now a real second path

Google Ironwood, AWS Trainium3 UltraServer, Microsoft Maia, and Meta MTIA show that hyperscalers have moved from "designing a chip" toward system-stack competition spanning compiler/runtime, interconnect, rack/pod architecture, and captive workloads.

## 3. Five core mechanisms

### Scarce-layer Value Capture

High cash generation, long-duration orders, switching costs, system-definition power, and supply orchestration can improve a buyer's ability to reserve next-generation scarce inputs and extend a current advantage across product generations.

### AI Resource Gravity

When AI workloads can pay more, commit for longer, and provide greater utilization certainty, capital and capacity are pulled toward high-value layers such as advanced logic, HBM, packaging, networking, and power.

### Non-AI Residual Capacity

Traditional markets do not face gross industry supply; they face the effective residual capacity that remains after high-value AI/server demand and other priority demand have absorbed the available increment.

### Cloud System-Stack Substitution

Hyperscaler in-house stacks can divert part of NVIDIA's platform profit while still competing for the same advanced logic, HBM, packaging, and power. Platform substitution and upstream resource competition can therefore occur at the same time.

### Anchor Compute Buyer Effect

Multi-year capacity commitments from large model companies can raise infrastructure-financing certainty and pull forward cloud, data-center, power, and semiconductor construction. The same mechanism can amplify duration-mismatch risk if utilization disappoints.

## 4. China must be analyzed by system layer

China's supply capability cannot be summarized with a single "domestic substitution rate." Consumer computing, PC/workstation systems, and frontier AI have different closure requirements.

The most accurate current description is that China has built a real accelerator/software parallel stack and has strong industrial depth in consumer and parts of general-purpose computing. Frontier-AI equivalence, however, still requires advanced logic, HBM-class memory, advanced packaging, interconnect, compiler/runtime, large production workloads, and power to reach verifiable scale at the same time.

## 5. The capital cycle cannot be judged from one CapEx total

Cloud CapEx, system-vendor revenue, foundry revenue, memory revenue, and power/data-center investment appear on different ledgers along the same supply chain. They cannot be mechanically added into a single "global AI investment" number.

A move toward S4 Capital Hard Landing requires simultaneous evidence across:

- Accounting losses / impairment;
- Utilization / effective revenue;
- Market-clearing prices / lead times;
- Forward commitments / CapEx / Anchor Buyer contracts.

As of August 2026, the evidence is more consistent with **high-intensity capital expansion plus rising ROI pressure** than with a confirmed industry-wide hard landing.

## 6. S1–S4: the future is not one deterministic curve

| Scenario | Core structure |
|---|---|
| S1 — Competitive Expansion | supply elasticity and interoperability rise; multiple system stacks coexist; value capture becomes more distributed |
| S2 — Baseline Concentration | a small number of system platforms and scarce-layer suppliers retain strong economics while substitution continues |
| S3 — Resource Hegemony | several scarce layers and switching costs strengthen simultaneously; challengers must replicate a more complete infrastructure stack |
| S4 — Capital Hard Landing | utilization, clearing prices, CapEx/commitments, and accounting losses deteriorate together |

As of August 2026, this report uses **S2** as the state that best matches the current evidence mix—not as a fixed ten-year forecast.

## 7. What evidence would force the judgment to change

The following developments should materially weaken the thesis that scarce-layer value capture will continue to strengthen:

- sustained declines or large cancellations in leading system-platform commitments;
- advanced packaging no longer acting as a growth constraint;
- sustained abundance in HBM / DRAM residual supply;
- large-scale low-migration-cost substitution by cloud custom systems in frontier workloads;
- power / interconnection no longer creating deployment differentiation;
- large-scale rescheduling or underutilization of Anchor Compute Buyer commitments;
- first-party evidence showing China has achieved scaled frontier-system closure across multiple critical layers;
- regulatory remedies that materially reduce proprietary-interface switching costs.

## 8. Recommended reading path

1. [NVIDIA System Stack](part-I-ch02-nvidia-system-stack.md)
2. [HBM](part-I-ch05-hbm-memory.md)
3. [Advanced Packaging](part-I-ch06-advanced-packaging.md)
4. [Power](part-I-ch07-power-constraint.md)
5. [Hyperscaler System Stack](part-II-ch12-hyperscaler-system-stack.md)
6. [China Parallel Stack](part-II-ch17-china-parallel-stack.md)
7. [Value Capture Map](part-III-ch20-value-capture-map.md)
8. [Capital Clearing](part-III-ch24-capital-clearing.md)
9. [Strategy & Endgame](part-IV-ch31-strategy-endgame.md)
10. [Master Judgment](part-IV-ch32-master-judgment.md)

## Core public-source navigation

- [Core Evidence Ledger](../核心证据台账.en.md)
- [Core Source Index](../核心参考文献索引.en.md)
- NVIDIA FY27 Q2 official results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- TSMC 2025 Annual Report: https://investor.tsmc.com/static/annualReports/2025/english/index.html
- Micron FY24 Q2 Prepared Remarks: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- TrendForce 2026E memory structure: https://www.trendforce.com/presscenter/news/20260825-13198.html
