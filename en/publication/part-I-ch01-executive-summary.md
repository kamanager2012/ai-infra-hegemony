# Part I · Chapter 1: Executive Summary and Core Judgments for the Next Decade

## 1. Core conclusion

> **The competitive unit in AI infrastructure has moved from the individual chip to the full system stack. Long-run value capture increasingly depends on who can simultaneously coordinate multiple scarce layers—advanced logic, HBM, advanced packaging, interconnect, software, racks/data centers, and power—and convert those physical resources into highly utilized, portable workloads that generate cash flow.**

This is not a claim of permanent monopoly, nor is it a point forecast of market share in 2036. The report analyzes a changing resource-allocation mechanism: when AI/HPC workloads offer materially higher willingness to pay, longer contract duration, greater use of prepayments, and higher expected returns than traditional end markets, incremental capital and scarce resources are more likely to move toward AI infrastructure. When supply expansion, system substitution, utilization, or commercial returns change, that structure can rebalance.

As of **August 28, 2026**, public evidence is most consistent with **S2 — Baseline Concentration**: a small number of system platforms and scarce-layer suppliers retain strong economics; HBM, advanced packaging, and power remain important physical constraints; and hyperscaler custom systems, China's parallel stack, and supply expansion continue to provide real substitution paths.

## 2. Eight factual anchors

### 2.1 NVIDIA's commercial delivery unit has moved up to the rack-scale system

The official GB200 NVL72 specification includes **72 Blackwell GPUs, 36 Grace CPUs, 13.4 TB of HBM3E, and 17 TB of LPDDR5X**. The delivered product is therefore a combination of compute, memory, interconnect, software, and rack architecture rather than merely an accelerator card.[^1]

### 2.2 NVIDIA's seller-side economics remain exceptionally strong

NVIDIA reported FY27 Q2 Revenue of **US$96.221B**, Data Center revenue of **US$89.0B**, GAAP gross margin of **75.0%**, and GAAP operating income of **US$63.734B**; the company also said Vera Rubin was in full production.[^2]

### 2.3 Forward supply commitments have expanded sharply

NVIDIA's manufacturing, supply, and capacity commitments increased from **US$95.2B** on January 25, 2026 to **US$279B** on July 26, 2026. The FY27 Q2 Form 10-Q states that the latest commitments are primarily associated with memory and manufacturing facilities required for data-center infrastructure systems, but it does not provide a supplier-level split. The aggregate cannot therefore be allocated directly to TSMC, CoWoS, or any single HBM vendor.[^3]

### 2.4 TSMC's demand structure has shifted materially toward HPC

In 2025, TSMC's HPC platform represented **58%** of annual net revenue and smartphone **29%**; 3 nm, 5 nm, and 7 nm represented **24% / 36% / 14%** of wafer revenue, respectively. These are revenue-mix measures, not customer-level wafer allocation, and they cannot be converted directly into CoWoS share.[^4]

In 2Q26, TSMC's HPC platform represented **66%** of quarterly revenue and smartphone **22%**; advanced technologies, defined as 7 nm and below, represented **77%** of wafer revenue. This further shows that HPC is one of the core drivers of incremental advanced-manufacturing demand, but HPC still cannot be equated one-for-one with AI.[^5]

### 2.5 HBM has become a manufacturing-resource competition layer

Micron disclosed that, under **same technology node / same number of bits** conditions, HBM3E requires approximately **3× the wafer supply of DDR5**. This is a wafer-supply trade ratio, not a price multiple and not a fixed manufacturing constant for every HBM generation.[^6]

TrendForce forecasts that HBM + RDIMM will represent approximately **51% of 2026 DRAM bit supply**. That is an institutional forecast rather than a full-year actual. Read together with Micron's ~3× trade ratio, it helps explain why AI/server memory can exert more pressure on conventional-DRAM residual supply than bit share alone suggests.[^7]

### 2.6 Advanced Packaging has become a verifiable growth constraint

TSMC said in 4Q24 that advanced-packaging capacity was “very tight” and could not satisfy all customer demand; in its 2Q26 earnings call it stated more directly that packaging tightness was limiting customer growth. TSMC does not disclose customer-level CoWoS allocation, so third-party estimates of customer concentration must retain their institutional-estimate identity.[^8]

### 2.7 Power has become an independent physical constraint alongside wafers, memory, and packaging

NVIDIA's DGX GB200 hardware guide specifies rack power of approximately **120 kW**. At the same time, an approximately 835 MW nuclear restart, a long-duration PPA with up to 1.92 GW of contract quantity, and advanced-nuclear development paths in the hundreds of MW for the 2030–2035 period show that Time-to-Power, grid connection, substations, firm power, and permitting are now part of the AI system-delivery constraint set. Contracted, Permitted, Energized, and Utilized MW must remain separate.[^9]

### 2.8 Hyperscaler custom systems have become a real second path

Google Ironwood, AWS Trainium3 UltraServers, Microsoft Maia 200, and Meta MTIA 300 show that hyperscaler competition has moved beyond “designing an ASIC” toward system-stack competition spanning accelerators, compiler/runtime, interconnect, rack/pod architecture, and captive workloads.[^10]

This does not mean NVIDIA has already been displaced. The variables that matter are how much production workload these systems carry, whether migration cost falls, whether utilization is sustainable, and whether they continue to compete for the same advanced logic, HBM, packaging, and power.

## 3. Seven core mechanisms

### 3.1 Scarce-layer Value Capture

When a platform combines strong cash generation, long-duration orders, system-definition power, switching costs, and supply orchestration, it is better positioned to commit early to next-generation scarce resources and thereby improve delivery certainty. High gross margin is only one possible result of this mechanism; it is not a legal monopoly finding.

### 3.2 AI Resource Gravity

When AI/HPC workloads offer higher risk-adjusted returns, longer-duration orders, and stronger utilization visibility, capital and effective capacity are more likely to move toward high-value layers such as advanced logic, HBM, advanced packaging, networking, and power.

### 3.3 Non-AI Residual Capacity

Traditional industries do not face gross worldwide capacity. They face the effective residual supply available after priority allocation:

```text
NonAI_Residual(t)
= Effective_Supply(t)
- AI_Absorption(t)
- Other_Priority_Demand(t)
```

This is why “total supply is growing” and “smartphones, PCs, and other traditional end markets are still facing pricing or configuration pressure” can both be true.

### 3.4 Two-Speed Semiconductor Economy

The AI Infrastructure Economy and the Traditional Device Economy share parts of the same upstream supply chain but differ in willingness to pay, contract duration, prepayment structure, BOM constraints, and end-market price elasticity.

The central structural change is not that consumer electronics disappear. It is:

> **AI/HPC is increasing the influence of a relatively small number of capital-intensive buyers over marginal semiconductor demand and incremental capital formation.**

### 3.5 AI Capacity Gap: separate the absolute gap from the growth gap

To determine whether a physical layer is **actually short of deliverable supply today**, the report defines an absolute gap:

```text
AI_Capacity_Gap_i(t)
= AI_Effective_Demand_i(t)
- AI_Effective_Capacity_i(t)
```

where \(i\) represents physical layers such as advanced logic, HBM/DRAM, advanced packaging, networking, and power. Demand and capacity must use the **same delivery window, qualification/quality boundary, and physical unit**, such as wafers/month, qualified package starts/month, bits/year, or MW.

- **Absolute Gap > 0:** current deliverable supply is insufficient;
- **Absolute Gap ≈ 0:** current supply and demand are near balance;
- **Absolute Gap < 0:** current effective headroom exists.

To determine whether scarcity pressure is widening or converging, the report separately defines:

```text
AI_Capacity_Growth_Gap_i(t)
= Growth(AI_Effective_Demand_i(t))
- Growth(AI_Effective_Capacity_i(t))
```

The Growth Gap is a difference in growth rates over the same period, measured in percentage points. It describes the **direction of pressure**, not the current stock gap:

- **Growth Gap > 0:** scarcity may widen, or existing headroom may be eroded;
- **Growth Gap < 0:** scarcity may converge, or effective headroom may expand;
- **Growth Gap = 0:** supply and demand are changing at the same rate; it does not imply that no shortage exists.

A strong S4 Capital Hard Landing signal therefore requires **Absolute Gap < 0 / excess capacity** together with deterioration in utilization, clearing prices, and forward commitments—not a negative Growth Gap by itself.

AI Capacity Gap, AI Capacity Growth Gap, and Non-AI Residual Capacity answer different questions: the first two measure the current AI-side shortfall and its direction of change; NARC measures effective supply left for non-AI demand after priority allocation.

### 3.6 Cloud System-Stack Substitution

Hyperscaler custom stacks can generate two effects that point in different directions but coexist:

1. **Platform-profit diversion:** part of the workload no longer pays the full economics of an external system platform;
2. **Upstream resource competition:** the custom system itself still requires advanced logic, HBM, packaging, and power.

More custom silicon therefore does not automatically mean less upstream physical scarcity.

### 3.7 Anchor Compute Buyer Effect

Multi-year and decade-scale compute commitments from large model companies can increase infrastructure revenue visibility and financing certainty, pulling forward cloud, data-center, power, and semiconductor construction. Conversely, if utilization or monetization disappoints, long-duration commitments can amplify duration mismatch and stranded-capacity risk.

## 4. China must be assessed by system layer, not by one “localization rate”

China has built a real and continuously developing accelerator/software parallel stack and has strengthened parallel supply in consumer computing, DRAM/NAND, selected general-purpose computing, and domestic software ecosystems. Frontier-AI equivalence, however, still requires advanced logic, HBM-class memory, advanced packaging, high-speed interconnect, compiler/runtime, frontier workloads, and power to reach verifiable scale simultaneously.[^11]

The report therefore rejects both extremes: “China has already fully caught up” and “China has no meaningful substitute capability.” The more accurate state is:

> **China has moved beyond the stage of having no alternative system, but public evidence is still insufficient to show globally equivalent scaled closure across every frontier critical layer.**

## 5. The capital cycle cannot be judged from one CapEx total

Cloud CapEx, system-vendor revenue, foundry revenue, memory revenue, and power/data-center investment appear on different ledgers along the same supply chain. They cannot be mechanically added into one “global AI investment” number.

A move toward **S4 — Capital Hard Landing** requires simultaneous evidence across at least four groups:

- **Accounting:** impairment, write-downs, and depreciation pressure;
- **Utilization / Revenue:** effective utilization, unit revenue, and real monetization;
- **Market Clearing:** lease rates, second-hand prices, lead times, and inventory;
- **Forward Commitment:** CapEx guidance, supply commitments, and Anchor Buyer contracts.

As of August 2026, the evidence is more consistent with:

> **high-intensity capital expansion + rising ROI pressure**

than with a confirmed industry-wide Capital Hard Landing.

## 6. S1–S4: the future is not one deterministic curve

**Table 1.1 — Four standard AI-infrastructure scenarios**

| Scenario | Core structure |
|---|---|
| S1 — Competitive Expansion | supply elasticity and interoperability rise; multiple system stacks coexist; value capture becomes more distributed |
| S2 — Baseline Concentration | a small number of system platforms and scarce-layer suppliers retain strong economics while substitution paths continue developing |
| S3 — Resource Hegemony | several scarce layers and switching costs strengthen simultaneously; challengers must replicate a more complete infrastructure stack |
| S4 — Capital Hard Landing | utilization, clearing prices, CapEx/commitments, and accounting losses deteriorate together |

**Source:** Report scenario framework.  
**Note:** S1–S4 are parallel conditional states. They do not carry fixed probabilities and are not treated as inevitable sequential stages.

As of August 2026, **S2 — Baseline Concentration** is the state that best matches the current evidence mix, not a fixed ten-year forecast.

## 7. What evidence would force the report to change its judgment

The following developments should materially reduce S2/S3 weight or force the relevant mechanisms to be re-evaluated:

- sustained declines or large cancellations in leading system-platform commitments;
- advanced packaging no longer being described by major suppliers as a growth constraint;
- sustained abundance in HBM / DRAM residual supply;
- large-scale, low-migration-cost substitution by cloud custom systems in frontier workloads;
- energized power and grid interconnection improving enough that Time-to-Power no longer differentiates projects;
- large-scale rescheduling or underutilization of Anchor Compute Buyer commitments;
- first-party evidence showing scaled frontier-system closure across multiple critical layers in China;
- formal regulatory remedies materially reducing proprietary-interface switching costs.

Conversely, if AI Capacity Gap remains positive across several physical layers, NARC continues to fall, migration costs remain high, and forward commitments continue expanding, the relative weight of S3 Resource Hegemony rises.

## 8. Report structure

The report is organized into four parts:

- **Part I — System Power and Physical Scarcity:** system stack, advanced logic, HBM, advanced packaging, power, and manufacturing redundancy;
- **Part II — Demand, Substitution, and the Second System Stack:** model economics, hyperscaler custom systems, Anchor Compute Buyers, China's parallel stack, and competition policy;
- **Part III — Capital Cycles, Profit Pools, and External Transmission:** CapEx, value capture, consumer transmission, depreciation, financing, capital clearing, and labor;
- **Part IV — Method, Scenarios, Monitoring, and Strategy:** evidence architecture, 2026–2036 milestones, monitoring framework, S1–S4, and the final strategic judgment.

Readers who read only one chapter should use this chapter as the entry point to the report's conclusions. Readers who need to verify a high-impact number should continue to the relevant thematic chapter and its References.

## References

[^1]: NVIDIA, “GB200 NVL72,” official product page, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^2]: NVIDIA, “NVIDIA Announces Financial Results for Second Quarter Fiscal 2027,” 2026, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^3]: NVIDIA Corporation, Form 10-Q for quarter ended 2026-07-26, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm ; NVIDIA Corporation, FY26 Form 10-K, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
[^4]: TSMC, 4Q25 Presentation / 2025 full-year platform and technology mix, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
[^5]: TSMC, “2Q26 Quarterly Results,” platform and technology revenue mix, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^6]: Micron Technology, FY24 Q2 Prepared Remarks, 2024-03-20, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^7]: TrendForce, 2026-08-25, HBM + RDIMM 2026E DRAM bit-supply structure, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^8]: TSMC, 4Q24 Earnings Conference Transcript, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf ; TSMC, 2Q26 Earnings Conference Transcript, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^9]: NVIDIA, DGX GB200 Hardware Guide, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html ; Constellation, Crane Clean Energy Center announcement, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs ; Talen Energy, 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm ; Kairos Power / Google partnership, https://www.kairospower.com/google
[^10]: Google, “Ironwood TPU,” https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; AWS, “Amazon EC2 Trn3 UltraServers,” https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ ; Microsoft, “Maia 200,” https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ ; Meta, “MTIA 300,” https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
[^11]: CXMT, STAR Market registration prospectus, 2026-05-27, Shanghai Stock Exchange, https://static.sse.com.cn/stock/disclosure/announcement/c/202605/002170_20260527_23QQ.pdf ; Moore Threads, MTT S80 official product page, https://en.mthreads.com/product/S80 ; DeepSeek, “DeepSeek-V3 Technical Report,” https://arxiv.org/abs/2412.19437 ; TrendForce, 2026-06-12, 1Q26 foundry revenue shares, https://www.trendforce.com/presscenter/news/20260612-13095.html
