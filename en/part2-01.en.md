# Macro Essay 1: Productive Compute and the Macro Measurement Framework

Chinese source edition: [part2-01.md](../part2-01.md)

> **Publication role:** this is the research-layer macro entry point. It defines the test for when compute becomes productive infrastructure and the common measurement units used across the essays. The integrated publication judgment is [Part IV · Chapter 32](../publication/part-IV-ch32-master-judgment.md). Unsupported point estimates for future node prices, CoWoS monthly capacity, 2030/2036 GW campuses, or similar long-range values do not enter the fact layer.

## 1. The core question: when does compute become productive infrastructure?

The phrase “means of production” is not a claim that models possess unconstrained agency. It describes an economic condition:

> **Can an AI system, under measurable compute, power, and capital costs, repeatedly complete verifiable workflows that can be accepted by a real business process and generate enough value to cover the system's long-run cost?**

If it can only assist isolated tasks, compute remains closer to a tool. If it can reliably execute large volumes of accepted work, compute, memory, interconnect, data centers, and power begin to behave like productive infrastructure.

The relevant unit is therefore not “model intelligence” in the abstract. It is:

> **cost per verified workflow outcome + capital required to sustain it**

## 2. Five structural changes are already observable

### 2.1 The sales unit has moved upward to the system stack

NVIDIA now sells rack-scale systems rather than only accelerator cards, while Google, AWS, Microsoft, and Meta have expanded custom silicon into compilers/runtimes, interconnect, rack/pod design, and captive production workloads. Competition has therefore moved from the chip toward the **system stack**.

### 2.2 HBM uses more manufacturing input than conventional DRAM

Micron disclosed that, at the same technology node and for the same number of bits, HBM3E requires roughly **3× the wafer supply of DDR5**. Bandwidth expansion therefore changes manufacturing inputs and residual DRAM capacity, not merely memory pricing.

### 2.3 Advanced packaging is a verified delivery constraint

TSMC has repeatedly described advanced-packaging capacity as tight and in 2Q26 stated that packaging tightness was limiting customer growth. Logic wafer availability does not automatically equal complete-system deliverability.

### 2.4 Power has entered the system-delivery chain

Roughly 120 kW-class racks and several hundred-MW / GW-scale long-duration power projects show that grid connection, substations, firm generation, permits, and **Time-to-Power** are now independent infrastructure variables.

### 2.5 Capital and long-duration commitments are reserving future resources earlier

NVIDIA manufacturing, supply, and capacity commitments rose from **US$95.2B** on 2026-01-25 to **US$279B** on 2026-07-26. Hyperscalers and model companies are also using long-duration compute, data-center, and power commitments to shape future supply. Public filings do not provide a supplier-level split, so these figures are evidence of aggregate forward commitment rather than a disclosed allocation to one foundry, packaging supplier, or HBM vendor.

## 3. The macro analysis uses five measurement axes

### 3.1 Verified Workflow Economics

Compute becomes productive only when each workflow produces measurable value after inference, retrieval, tools, review, and operational cost.

### 3.2 System Substitution

The report tracks whether real workloads can move among NVIDIA, TPU, Trainium, Maia, MTIA, or other stacks at acceptable engineering cost. One-chip benchmarks cannot substitute for production migration evidence.

### 3.3 Scarce Physical Inputs

Advanced logic, HBM, advanced packaging, and power are separate physical pools. Relief in one layer does not imply simultaneous relief in the others.

### 3.4 Capital Duration

Compute hardware, networking, data-center shells, grid assets, and PPAs operate on different useful lives and contractual clocks. Buyer ROI must cover this duration mismatch.

### 3.5 Utilization and Forward Commitments

High CapEx becomes high-quality investment only if the asset base receives enough productive utilization and workflow revenue. Current-state analysis therefore tracks utilization, seller commitments, Anchor Buyer contracts, and market-clearing prices together.

## 4. From workflow demand to scarce-layer value capture

When AI workflows create accepted economic output, demand transmits down the stack:

> workflow demand → system demand → HBM / packaging / power demand → forward commitments → scarce-resource allocation

If one platform combines strong cash generation, switching costs, roadmap certainty, and long-duration orders, it can reserve scarce future inputs earlier and raise delivery certainty.

This is the mechanism behind **Scarce-layer Value Capture**. Economic value tends to accumulate where supply is scarce, substitution is difficult, or multiple layers can be coordinated effectively.

After AI/server demand absorbs high-value capacity, non-AI markets should be analyzed through **Non-AI Residual Capacity**, not industrywide gross capacity alone.

## 5. Algorithmic efficiency can lower unit demand or expand total usage

DeepSeek and other architecture-efficiency examples show that compute and memory required for a particular workload can fall materially.

But lower unit cost does not imply lower total infrastructure demand. The research and publication layers now use the same computable relationship:

```text
Infrastructure_Demand_t
= Unit_Resource_Intensity_t
× Workload_Volume_t
```

Relative to a baseline period:

```text
Infrastructure_Demand_t / Infrastructure_Demand_0
=
(Unit_Resource_Intensity_t / Unit_Resource_Intensity_0)
×
(Workload_Volume_t / Workload_Volume_0)
```

If the analysis also maps effective price changes into workload volume, it can separately introduce an explicitly labeled elasticity assumption:

```text
Workload_Volume_t / Workload_Volume_0
=
(Effective_Price_t / Effective_Price_0)^(-ε)
```

where ε must refer to demand for the same comparable, verifiable outcome. This keeps efficiency improvement and demand expansion separate instead of compressing them into a non-computable slogan.

The relevant evidence is unit resource intensity, total productive workload, effective price, and asset utilization—not one training-cost headline or one API price.

## 6. Multiple regional stacks may increase duplication as well as resilience

Export controls, resilience objectives, and industrial policy can produce parallel technology ecosystems. Multiple stacks can mean:

- duplicated software/runtime;
- duplicated manufacturing capacity;
- duplicated power/data-center reservations;
- lower single-stack efficiency;
- greater resilience and strategic optionality.

Geopolitical fragmentation can therefore increase infrastructure duplication rather than simply reduce global demand.

## 7. Long-range point estimates remain H / D, not facts

The report does not treat exact 2030/2036 node prices, CoWoS monthly capacity, future HBM trade ratios, multi-GW campuses, or trillion-dollar CapEx as confirmed paths.

The rules are:

- historical numbers without public first-party or high-quality institutional evidence do not enter F;
- company guidance remains guidance;
- institutional forecasts retain source identity and time window;
- 2030/2036 point values remain explicit H / D scenario inputs;
- repetition across chapters does not upgrade evidence grade.

The long-range thesis therefore rests on mechanisms and observable variables, not a precise future price table.

## 8. Which state best matches the current evidence?

As of August 2026, the fact pattern is closest to **S2 — Baseline Concentration**:

- leading system-platform economics remain strong;
- cloud custom stacks are a real second route;
- HBM, advanced packaging, and power still create physical constraints;
- China's parallel stack is expanding, but frontier closure still requires several advanced layers to scale together;
- CapEx and forward commitments remain high while buyer-side ROI pressure is rising.

This is not a fixed 2036 forecast. Higher supply elasticity, interoperability, and substitution would shift weight toward S1; tighter scarce layers and switching costs toward S3; synchronized weakness in utilization, clearing prices, CapEx, and commitments toward S4.

## 9. What would falsify a stronger productive-infrastructure thesis?

The current macro judgment should weaken if several of the following persist:

- productive AI workloads fail to cover the growing capital base;
- major system-platform commitments decline repeatedly;
- advanced-packaging and HBM supply becomes durably abundant;
- cloud custom systems sharply lower switching costs and external-platform dependence;
- energized power expands faster than compute demand and Time-to-Power loses scarcity;
- second-hand compute and lease prices clear persistently lower;
- application/workflow monetization remains below inference and infrastructure cost.

The purpose of the framework is not to make every long-range claim survive. It is to make clear which evidence would force the claim to change.

## 10. Current macro conclusion

> **When verifiable workflows convert compute into durable economic output, system stacks, HBM, advanced packaging, power, and capital duration stop being isolated technical parameters and become productive-infrastructure variables that shape value capture and industrial structure.**

This remains conditional. Long-run returns depend not on installed hardware counts, but on whether the infrastructure continuously serves portable, verifiable, cash-generating workloads.

## Key public sources

- NVIDIA FY27 Q2 official results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- NVIDIA FY27 Q2 10-Q — US$279B manufacturing, supply, and capacity commitments: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
- Micron FY24 Q2 prepared remarks — HBM3E ≈3× DDR5 wafer supply: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- TrendForce — 2026E HBM + RDIMM = 51% of DRAM bit supply: https://www.trendforce.com/presscenter/news/20260825-13198.html
- TSMC 2Q26 Earnings Conference Transcript — packaging tightness limits customer growth: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
- NVIDIA DGX GB200 hardware guide — ~120 kW/rack: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html