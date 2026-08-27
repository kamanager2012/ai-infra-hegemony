# The Age of AI Infrastructure Hegemony
### AI基础设施霸权时代

**40-volume industry research monograph + 8 macro essays**

> **English release landing page.** The complete Chinese edition remains the research source of truth: [中文版](README.zh-CN.md).

[English](README.md) · [中文版](README.zh-CN.md) · [Research method](en/研究方法与证据分级.en.md) · [Release notes](RELEASE_NOTES.md)

---

# English Edition

This project is a long-form industry research monograph on the restructuring of AI infrastructure, semiconductors, memory, advanced packaging, hyperscaler system stacks, power, capital, software economics, labor, and the 2026–2036 industrial endgame.

The report is built from public statutory filings, company materials, regulatory documents, formal contract disclosures, and high-quality institutional research. Already-observed claims are treated as facts; forward-looking claims are explicitly separated into hypotheses, mechanisms, scenarios, and falsification conditions.

**Retrieval and revision cutoff: August 27, 2026.** This research is not an audit opinion, investment recommendation, or legal opinion.

The original report text is licensed under **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**. Commercial use is not permitted. Redistribution is permitted only for unadapted material under the license terms with attribution; adapted or derivative versions may not be shared. See [LICENSE](LICENSE).

## Core findings

- **The competitive unit in AI infrastructure is moving from the chip to the system stack.** The relevant stack now spans advanced logic, HBM, advanced packaging, scale-up/scale-out interconnect, compilers/runtimes, racks/pods, data centers, and power.
- **NVIDIA remains exceptionally strong, but the counterfactual is no longer “GPU versus one ASIC die.”** NVIDIA's official FY27 Q2 results report **US$96,221 million = US$96.221 billion** of revenue, **US$89.0 billion** of Data Center revenue, **75.0%** GAAP gross margin, and **US$63.734 billion** of GAAP operating income; Vera Rubin was in full production. [NVIDIA official FY27 Q2 results](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx). Google [Ironwood](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/), AWS [Trn3 UltraServers / Trainium3](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/), Microsoft [Maia 200](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/), and Meta [MTIA 300](https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/) show that hyperscalers are also building increasingly complete system stacks.
- **Total supply growth does not equal recovery for non-AI industries.** The report uses **Non-AI Residual Capacity** to separate effective supply, AI absorption, other priority demand, and the residual actually available to consumer and traditional markets.
- **HBM has a measurable physical tradeoff.** Micron disclosed that, at the same technology node and for the same number of bits, HBM3E consumes approximately **3× the wafer supply of DDR5/D5**. This is a wafer-supply trade ratio—not a price multiple and not a universal constant for every generation. [Micron FY24 Q3 prepared remarks](https://investors.micron.com/static-files/4550f98c-1054-4847-a929-c17d520a0564).
- **Model companies are becoming Anchor Compute Buyers.** OpenAI's [Stargate](https://openai.com/index/announcing-the-stargate-project/) and Anthropic's [up-to-5-GW AWS agreement](https://www.anthropic.com/news/anthropic-amazon-compute?lang=us) show how long-duration model demand can shape cloud capacity, chips, data centers, power, and financing rather than merely rent existing infrastructure.
- **Power is an independent physical constraint.** NVIDIA documents approximately **120 kW** rack power for GB200/GB300 NVL72-class systems ([NVIDIA DGX GB rack guide](https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html)); Constellation disclosed the Microsoft-linked Crane restart at approximately **835 MW** ([Constellation](https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs)); Talen's 2026 Q2 filing says the revised AWS PPA provides up to **1,920 MW** and transitioned in April 2026 ([SEC filing](https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm)); and Google/Kairos disclosed up to **500 MW** of new nuclear capacity ([Google](https://blog.google/company-news/outreach-and-initiatives/sustainability/google-kairos-power-nuclear-energy-agreement/)). These figures sit on different contract, construction, energization, and utilization clocks.
- **AI software economics must be measured as unit economics, not inherited SaaS margins.** Inference, retrieval/storage, tool/API calls, human review, and AI-specific cloud cost all matter.
- **The future is modeled as states, not a single prophecy.** The formal endgame is **S1 Competitive Expansion, S2 Baseline Concentration, S3 Resource Hegemony, and S4 Capital Hard Landing**, driven by the H1–H17 variable system.

### Historical fact gate

For this repository, an already-observed historical claim may enter **F — Fact** only when it is publicly verifiable. Financial figures must preserve the reporting period, accounting basis, original unit, and denominator. Unit conversions must be mechanically checkable—for example, **US$96.221B = US$96,221M**. Avoid unnecessary cross-unit rewrites when the source unit is already clear. If a historical number cannot be traced to a public source, it must be removed or downgraded from F. Institutional estimates may be used only with the institution named and the evidence grade preserved. Forward-looking values are allowed only when explicitly labeled as hypotheses, model outputs, stress tests, or scenarios.

## Start here

1. [Master Judgment](en/总判.en.md)
2. [Volume 01 — Executive Summary and Core Judgments for the Next Decade](en/vol-01.en.md)
3. [Research Methodology and Evidence Grading](en/研究方法与证据分级.en.md)
4. [Core Evidence Ledger](en/核心证据台账.en.md)
5. [Core Source Index](en/核心参考文献索引.en.md)
6. [Core Concepts and Model Index](en/核心概念与模型索引.en.md)
7. [Core Hypothesis Matrix (2026–2036)](en/核心假设矩阵.en.md)
8. [Volume 18 — Research Methodology and Evidence Architecture](en/vol-18.en.md)
9. [Mechanism Index](en/机制索引.en.md)
10. [English Edition Index](en/README.en.md)
11. [X / social launch drafts](en/SHARE.md)

All **40 English volumes + 8 English macro essays** have now completed a full repository-wide publication QA pass. High-risk legacy translations were structurally rebuilt against the current Chinese source structure; lower-risk chapters were retained after regression. The current English corpus passes the targeted publication checks for legacy workpaper language, stale FY27 Q2 outlook framing, old fixed scenario weights, malformed unit capitalization, hidden control characters, and incorrect Chinese-source link patterns. The English edition follows the same F→H→M→S→X ontology, A/B/C/D evidence grading, system-stack, Anchor Compute Buyer, Non-AI Residual Capacity, AI Software Unit Economics, layered China stack, FY27 Q2 actuals, and S1–S4 framework. The Chinese `main` corpus remains the source of truth for resolving bilingual discrepancies.

## Research method

The entire report uses one causal and evidentiary chain:

**F → H → M → S → X**

- **F — Fact:** observed and verifiable financial, product, capacity, contract, regulatory, energy, and market evidence.
- **H — Hypothesis:** explicit forward assumptions about demand, resource allocation, memory/packaging expansion, power, price, and capital.
- **M — Mechanism:** the causal transmission from facts and hypotheses through profit, prepayments, utilization, yield, packaging, memory, power, depreciation, and switching costs.
- **S — Scenario:** conditional 2026–2036 industrial states derived from F + H + M.
- **X — Falsification:** observable reverse signals that force a strong judgment to weaken or fail.

Evidence is also graded separately. First-party evidence, high-quality institutional research, sell-side/supply-chain estimates, and report stress tests are not allowed to collapse into one confidence level.

## Main thesis

The central problem is not a simple market-share monopoly. It is **scarce-layer value capture and control over incremental capacity allocation**.

Long-duration orders and prepayments can reserve future supply. The key variable is therefore not gross worldwide semiconductor capacity, but how much **effective residual capacity** remains after AI and other priority demand absorb the increment. Cloud custom silicon can reduce NVIDIA's platform-profit share while simultaneously increasing competition for advanced logic, HBM, advanced packaging, and power. China's stack must be analyzed by layer rather than by one “domestic substitution” percentage. Power must be tracked separately from wafers, packaging, and memory. Regulatory investigations must not be written as complaints, remedies, or breakups before they exist.

## 40-volume English edition

- [Volume 01: Executive Summary and Core Judgments for the Next Decade](en/vol-01.en.md)
- [Volume 02: NVIDIA Platform Dominance and the System-Stack Moat](en/vol-02.en.md)
- [Volume 03: AI Resource Gravity and Non-AI Residual Capacity](en/vol-03.en.md)
- [Volume 04: TSMC, N2, and Advanced-Manufacturing Resource Allocation](en/vol-04.en.md)
- [Volume 05: HBM, the Memory War, and AI Supply-Chain Restructuring](en/vol-05.en.md)
- [Volume 06: Model-Company Unit Economics, Algorithmic Efficiency, and Open-Source Competition](en/vol-06.en.md)
- [Volume 07: NVIDIA Vertical Expansion and AI Factory Control](en/vol-07.en.md)
- [Volume 08: The AI-Infrastructure Supercycle, CapEx, and Depreciation Pressure](en/vol-08.en.md)
- [Volume 09: Transmission from AI Infrastructure into the Physical Supply Chain](en/vol-09.en.md)
- [Volume 10: Four Standard AI-Infrastructure Scenarios for the Next Decade](en/vol-10.en.md)
- [Volume 11: Antitrust, Industrial Policy, and the Boundaries of AI Platform Power](en/vol-11.en.md)
- [Volume 12: U.S.–China AI Supply-Chain Competition and China's Parallel Stack](en/vol-12.en.md)
- [Volume 13: The AI Energy War — From 120 kW Racks to GW-Scale Power Commitments](en/vol-13.en.md)
- [Volume 14: AI Infrastructure Value-Capture Map — Who Captures Profit and Who Bears Residual Pressure](en/vol-14.en.md)
- [Volume 15: The 2036 AI-Infrastructure Endgame — System Stacks, Resources, and Power](en/vol-15.en.md)
- [Volume 16: Quantitative Framework for AI Infrastructure — Compute, Memory, Packaging, and Capacity](en/vol-16.en.md)
- [Volume 17: Ultimate Risks in AI Infrastructure — Physical, Capital, Substitution, and Institutional Constraints](en/vol-17.en.md)
- [Volume 18: Research Methodology and Evidence Architecture](en/vol-18.en.md)
- [Volume 19: 2026–2036 AI-Infrastructure Timeline and Milestones](en/vol-19.en.md)
- [Volume 20: Strategic Implications — How Firms, Capital, and States Should Respond](en/vol-20.en.md)
- [Volume 21: AI-Infrastructure Capital Flows and Profit-Pool Structure](en/vol-21.en.md)
- [Volume 22: Consumer Electronics — DRAM Residual Capacity, PCs, and Smartphone Cost Transmission](en/vol-22.en.md)
- [Volume 23: HBM4, Logic Base Dies, and Memory Capital Density](en/vol-23.en.md)
- [Volume 24: Advanced Packaging, CoWoS, and AI-System Delivery Bottlenecks](en/vol-24.en.md)
- [Volume 25: Hyperscaler System-Stack Competition](en/vol-25.en.md)
- [Volume 26: Model Companies, Anchor Compute Buyers, and Infrastructure Co-Build](en/vol-26.en.md)
- [Volume 27: Agent-Native Software and AI Software Unit Economics](en/vol-27.en.md)
- [Volume 28: Physical AI and the Real Bottlenecks in Robotics](en/vol-28.en.md)
- [Volume 29: System-Level Assessment of China's Frontier AI Parallel Stack](en/vol-29.en.md)
- [Volume 30: The Depreciation Wall, Capital Clearing, and Long-Run Industry Structure](en/vol-30.en.md)
- [Volume 31: Core Indicators and Evidence-Monitoring Framework](en/vol-31.en.md)
- [Volume 32: NVIDIA Full-Stack Architecture — GPU, NVLink, CUDA/PTX, and Rack-Scale Systems](en/vol-32.en.md)
- [Volume 33: AMD, Intel, Qualcomm, and Apple — Differentiated Competitive Paths](en/vol-33.en.md)
- [Volume 34: Restructuring the Global Semiconductor Supply Chain — Equipment, Materials, Manufacturing, and Geopolitical Redundancy](en/vol-34.en.md)
- [Volume 35: AI Power Constraints — 835 MW, 1.92 GW, and 500 MW Across Three Delivery Paths](en/vol-35.en.md)
- [Volume 36: AI Infrastructure Capital Markets — Asset Duration, Financing Structure, and Sovereign Capital](en/vol-36.en.md)
- [Volume 37: AI Infrastructure Bubble Detection and Market-Clearing Framework](en/vol-37.en.md)
- [Volume 38: AI and Labor Markets — From Task Exposure to Job Restructuring](en/vol-38.en.md)
- [Volume 39: Education and Talent Systems in the AI Era — From Model Use to Systems Engineering](en/vol-39.en.md)
- [Volume 40: Final Strategic Synthesis — Individuals, Firms, Capital, and States](en/vol-40.en.md)

## Eight macro essays — English

- [Macro Essay 1: The Means-of-Production Shift and the Overall Judgment](en/part2-01.en.md)
- [Macro Essay 2: Platform Concentration and NVIDIA's Hardware–Software System Power](en/part2-02.en.md)
- [Macro Essay 3: Physical Manufacturing Limits and the Global Semiconductor Supply Contest](en/part2-03.en.md)
- [Macro Essay 4: Hyperscaler CapEx, System-Stack Counterattack, and DeepSeek's Architecture-Driven Cost Reduction](en/part2-04.en.md)
- [Macro Essay 5: Resource Reallocation and Cost Transmission into Consumer Electronics and the Real Economy](en/part2-05.en.md)
- [Macro Essay 6: The Energy War and Physical Grid Constraints](en/part2-06.en.md)
- [Macro Essay 7: The Capital Supercycle, Bubble Mechanisms, and Extreme Stress Tests](en/part2-07.en.md)
- [Macro Essay 8: U.S.–China Compute Competition and the 2036 Endgame Decision Tree](en/part2-08.en.md)

## Contributing

Corrections, source upgrades, mechanism challenges, counterarguments, and falsification signals are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Citation

GitHub reads [CITATION.cff](CITATION.cff). Author: James (kamanager2012). Original report text is licensed under [CC BY-NC-ND 4.0](LICENSE).

