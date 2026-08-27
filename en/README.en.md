# The Age of AI Infrastructure Hegemony

An industry research monograph: **40 volumes + 8 macro essays** on AI infrastructure, semiconductors, memory, advanced packaging, hyperscaler system stacks, power, software economics, labor, and the 2026–2036 industrial endgame.

The Chinese research corpus remains the source of truth: [中文主目录](../README.zh-CN.md). The repository root [README](../README.md) is the English-first release landing page.

**Research rule:** facts must be sourced; forecasts remain labeled as hypotheses, mechanisms, scenarios, or stress tests. Revenue share is not wafer share. Contracted MW is not energized load. Guidance is not actual performance.

**Retrieval and revision cutoff: 2026-08-27.** The repository is in private publication-preparation mode. Original report text is licensed under **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**. Commercial use is not permitted; redistribution is limited to unadapted material under the license terms with attribution, and adapted or derivative versions may not be shared. See [LICENSE](../LICENSE).

## Core findings

- **Competition is moving from chips to system stacks.** The relevant unit now includes advanced logic, HBM, advanced packaging, scale-up/scale-out interconnect, compilers/runtimes, racks/pods, data centers, and power.
- **NVIDIA remains exceptionally strong, but the counterfactual is no longer “one GPU versus one ASIC die.”** Official FY27 Q2 results report **US$96,221 million = US$96.221 billion** of revenue, **US$89.0 billion** of Data Center revenue, **75.0%** GAAP gross margin, and **US$63.734 billion** of GAAP operating income; Vera Rubin was in full production. [NVIDIA official FY27 Q2 results](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx). Hyperscaler system-stack evidence includes Google [Ironwood](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/), AWS [Trn3 UltraServers / Trainium3](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/), Microsoft [Maia 200](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/), and Meta [MTIA 300](https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/).
- **Total supply growth does not equal recovery for non-AI industries.** The report tracks **Non-AI Residual Capacity** after AI and other priority demand absorb the increment.
- **HBM has a first-party physical tradeoff.** Micron disclosed that HBM3E requires roughly **3× the wafer supply of DDR5/D5** at the same technology node and bit capacity. This is a wafer-supply trade ratio, not a price multiple. [Micron FY24 Q3 prepared remarks](https://investors.micron.com/static-files/4550f98c-1054-4847-a929-c17d520a0564).
- **Model companies can become Anchor Compute Buyers.** OpenAI [Stargate](https://openai.com/index/announcing-the-stargate-project/) and Anthropic's [up-to-5-GW AWS agreement](https://www.anthropic.com/news/anthropic-amazon-compute?lang=us) show how long-duration model demand can influence chips, data centers, power, cloud capacity, and financing.
- **Power is an independent physical constraint.** Public anchors include approximately **120 kW** GB200/GB300 NVL72 rack power ([NVIDIA](https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html)), approximately **835 MW** for the Constellation/Microsoft Crane restart ([Constellation](https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs)), up to **1,920 MW** in the revised Talen/AWS PPA with the transition occurring in April 2026 ([SEC](https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm)), and up to **500 MW** in the Google/Kairos agreement ([Google](https://blog.google/company-news/outreach-and-initiatives/sustainability/google-kairos-power-nuclear-energy-agreement/)). Contracted MW is not energized or utilized load.
- **AI software must be analyzed through unit economics rather than inherited SaaS-margin assumptions.** Inference, retrieval/storage, tools/APIs, human review, and AI-specific cloud cost all matter.
- **The future is modeled as states rather than one prophecy:** **S1 Competitive Expansion, S2 Baseline Concentration, S3 Resource Hegemony, S4 Capital Hard Landing**.

### Historical fact gate

An already-observed claim may enter **F — Fact** only if it is publicly verifiable. Financial figures must retain period, accounting basis, original units, and denominators. Conversions must be mechanically checkable: **US$96.221B = US$96,221M = 962.21 亿美元**. If a historical number lacks a public source, it must be removed or downgraded from F. Institutional estimates must retain the institution name and evidence grade. Forward-looking values are permitted only when explicitly labeled as hypotheses, model outputs, stress tests, or scenarios.

## Start here

1. [Master Judgment](总判.en.md)
2. [Volume 01 — Executive Summary and Core Judgments for the Next Decade](vol-01.en.md)
3. [Research Methodology and Evidence Grading](研究方法与证据分级.en.md)
4. [Core Evidence Ledger](核心证据台账.en.md)
5. [Core Source Index](核心参考文献索引.en.md)
6. [Core Concepts and Model Index](核心概念与模型索引.en.md)
7. [Core Hypothesis Matrix (2026–2036)](核心假设矩阵.en.md)
8. [Mechanism Index](机制索引.en.md)
9. [X / social launch drafts](SHARE.md)

> **English publication status:** all 40 English volumes and 8 macro essays have completed a repository-wide publication-language and legacy-framing pass. Publication-critical volumes 36, 37, 39, and 40 were additionally re-edited against the current Chinese structure in this release-preparation cycle. This does not replace future sentence-level bilingual synchronization when the Chinese research changes; the Chinese `main` corpus remains the source of truth for resolving any discrepancy.

## Research method

The report uses one causal and evidentiary chain:

**F — Fact → H — Hypothesis → M — Mechanism → S — Scenario → X — Falsification**

Evidence grades are kept separate from scenario confidence. First-party evidence, institutional research, supply-chain estimates, and report-side stress tests are not collapsed into one confidence level.

## Forty volumes

1. [Executive Summary and Core Judgments for the Next Decade](vol-01.en.md)
2. [NVIDIA Platform Dominance and the System-Stack Moat](vol-02.en.md)
3. [AI Resource Gravity and Non-AI Residual Capacity](vol-03.en.md)
4. [TSMC, N2, and Advanced-Manufacturing Resource Allocation](vol-04.en.md)
5. [HBM, the Memory War, and AI Supply-Chain Restructuring](vol-05.en.md)
6. [Model-Company Unit Economics, Algorithmic Efficiency, and Open-Source Competition](vol-06.en.md)
7. [NVIDIA Vertical Expansion and AI Factory Control](vol-07.en.md)
8. [The AI-Infrastructure Supercycle, CapEx, and Depreciation Pressure](vol-08.en.md)
9. [Transmission from AI Infrastructure into the Physical Supply Chain](vol-09.en.md)
10. [Four Standard AI-Infrastructure Scenarios for the Next Decade](vol-10.en.md)
11. [Antitrust, Industrial Policy, and the Boundaries of AI Platform Power](vol-11.en.md)
12. [U.S.–China AI Supply-Chain Competition and China's Parallel Stack](vol-12.en.md)
13. [The AI Energy War — From 120 kW Racks to GW-Scale Power Commitments](vol-13.en.md)
14. [AI Infrastructure Value-Capture Map — Who Captures Profit and Who Bears Residual Pressure](vol-14.en.md)
15. [The 2036 AI-Infrastructure Endgame — System Stacks, Resources, and Power](vol-15.en.md)
16. [Quantitative Framework for AI Infrastructure — Compute, Memory, Packaging, and Capacity](vol-16.en.md)
17. [Ultimate Risks in AI Infrastructure — Physical, Capital, Substitution, and Institutional Constraints](vol-17.en.md)
18. [Research Methodology and Evidence Architecture](vol-18.en.md)
19. [2026–2036 AI-Infrastructure Timeline and Milestones](vol-19.en.md)
20. [Strategic Implications — How Firms, Capital, and States Should Respond](vol-20.en.md)
21. [AI-Infrastructure Capital Flows and Profit-Pool Structure](vol-21.en.md)
22. [Consumer Electronics — DRAM Residual Capacity, PCs, and Smartphone Cost Transmission](vol-22.en.md)
23. [HBM4, Logic Base Dies, and Memory Capital Density](vol-23.en.md)
24. [Advanced Packaging, CoWoS, and AI-System Delivery Bottlenecks](vol-24.en.md)
25. [Hyperscaler System-Stack Competition](vol-25.en.md)
26. [Model Companies, Anchor Compute Buyers, and Infrastructure Co-Build](vol-26.en.md)
27. [Agent-Native Software and AI Software Unit Economics](vol-27.en.md)
28. [Physical AI and the Real Bottlenecks in Robotics](vol-28.en.md)
29. [System-Level Assessment of China's Frontier AI Parallel Stack](vol-29.en.md)
30. [The Depreciation Wall, Capital Clearing, and Long-Run Industry Structure](vol-30.en.md)
31. [Core Indicators and Evidence-Monitoring Framework](vol-31.en.md)
32. [NVIDIA Full-Stack Architecture — GPU, NVLink, CUDA/PTX, and Rack-Scale Systems](vol-32.en.md)
33. [AMD, Intel, Qualcomm, and Apple — Differentiated Competitive Paths](vol-33.en.md)
34. [Restructuring the Global Semiconductor Supply Chain — Equipment, Materials, Manufacturing, and Geopolitical Redundancy](vol-34.en.md)
35. [AI Power Constraints — 835 MW, 1.92 GW, and 500 MW Across Three Delivery Paths](vol-35.en.md)
36. [AI Infrastructure Capital Markets — Asset Duration, Financing Structure, and Sovereign Capital](vol-36.en.md)
37. [AI Infrastructure Bubble Detection and Market-Clearing Framework](vol-37.en.md)
38. [AI and Labor Markets — From Task Exposure to Job Restructuring](vol-38.en.md)
39. [Education and Talent Systems in the AI Era — From Model Use to Systems Engineering](vol-39.en.md)
40. [Final Strategic Synthesis — Individuals, Firms, Capital, and States](vol-40.en.md)

## Eight macro essays

1. [Macro Essay 1: The Means-of-Production Shift and the Overall Judgment](part2-01.en.md)
2. [Macro Essay 2: Platform Concentration and NVIDIA's Hardware–Software System Power](part2-02.en.md)
3. [Macro Essay 3: Physical Manufacturing Limits and the Global Semiconductor Supply Contest](part2-03.en.md)
4. [Macro Essay 4: Hyperscaler CapEx, System-Stack Counterattack, and DeepSeek's Architecture-Driven Cost Reduction](part2-04.en.md)
5. [Macro Essay 5: Resource Reallocation and Cost Transmission into Consumer Electronics and the Real Economy](part2-05.en.md)
6. [Macro Essay 6: The Energy War and Physical Grid Constraints](part2-06.en.md)
7. [Macro Essay 7: The Capital Supercycle, Bubble Mechanisms, and Extreme Stress Tests](part2-07.en.md)
8. [Macro Essay 8: U.S.–China Compute Competition and the 2036 Endgame Decision Tree](part2-08.en.md)

## Core research infrastructure

- [Research Methodology and Evidence Grading](研究方法与证据分级.en.md)
- [Core Evidence Ledger](核心证据台账.en.md)
- [Core Source Index](核心参考文献索引.en.md)
- [Core Concepts and Model Index](核心概念与模型索引.en.md)
- [Core Hypothesis Matrix (2026–2036)](核心假设矩阵.en.md)
- [Mechanism Index](机制索引.en.md)

For the latest research conclusions, use `main`.