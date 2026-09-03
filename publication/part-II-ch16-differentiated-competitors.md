# Part II · 第16章：AMD、Intel、Qualcomm 与 Apple 的差异化竞争路径

## 1. Competitor 在 Stack 的不同 Layer 展开竞争

AMD、Intel、Qualcomm 与 Apple 在 system stack 的不同 layer 竞争，同时拥有不同的 manufacturing access、workload base、distribution channel 与 capital structure。

真正的问题不是它们是否组成“反 NVIDIA 联盟”，而是：

> **每家公司能够现实削弱哪一种 system-stack power？**

## 2. AMD：最直接的 Data Center System Challenger

AMD Instinct 是最直接的 data-center accelerator alternatives 之一，AMD 当前官方路线也已把 Instinct GPU、EPYC CPU、Pensando networking 与 ROCm 组织为 rack/system 级解决方案。[^1][^2]

真正的门槛不只是 GPU design，而是：

- ROCm / software maturity；
- scale-up / scale-out；
- HBM；
- advanced packaging；
- system reference architecture；
- customer migration / production support。

AMD 在 2026-08-27 发布 ROCm 10，并把 ROCm.AI 推向 general availability，官方定位明确强调从 Instinct infrastructure access 到 production inference / training 的迁移、validated frameworks/containers、communication libraries 与 developer workflow。[^14] 这说明 AMD 当前最关键的竞争动作之一，已经从“补齐软件功能”上移到**降低 production migration friction**。

因此 AMD 的竞争单位也已经从 chip 上移到 system。

## 3. AMD 同样暴露于 Scarce-Capacity Access

AMD 与 NVIDIA 会竞争相同的 advanced logic、HBM 与 packaging。

所以 NVIDIA demand 极强时，AMD 的挑战不仅是 market share，也包括 incremental scarce capacity access。

反过来，如果 HBM/packaging supply elasticity 提高，AMD system expansion 的约束会下降。

这使 AMD 成为观察**第二买方能否稳定获得 advanced logic、HBM 与 packaging quantity assurance**的重要对象。这里不再另造 residual-capacity 术语，直接使用 layer-specific scarce-capacity access。

## 4. Intel：Product Clock 与 Foundry Clock 运行在不同时间线

Intel 同时承担 CPU/product competition、accelerator attempts、foundry strategy 与 domestic manufacturing policy。Intel 2025 10-K 与 2026 VLSI Symposium 更新显示 Intel Foundry 仍在推进 external-foundry strategy，18A 已进入 production、18A-P 进入 risk production。[^3][^4] 2026-07 ASML / Intel 又确认 High-NA EUV 已在 Intel 18A 的特定 layers 上进入真实 high-volume logic production。[^9]

Product clock 需要在短周期交付 performance、software 与 customer adoption；foundry clock 则需要长期建立 process、yield、customer trust、packaging 与 high-volume execution。

因此，Intel 的复苏不能由一颗产品、一项 process milestone 或一座 fab 单独证明。High-NA HVM 是 manufacturing-execution 的重要正面信号，但 external foundry adoption、yield economics 与 customer trust 仍需独立验证。

## 4A. Historical Memory：Concentration 改变 Cadence Control，不等于改变 Engineering Causality

Intel 客户端 CPU 历史可以作为一个有边界的对照，但不能被写成“霸权必然挤牙膏”。

Intel 自己在 2016–2017 年年度报告中披露，14nm 与下一代 10nm 的 process-technology cadence 正在拉长，公司计划在同一 node 上运行 multiple waves of products；2018 年又明确披露，10nm volume production 从原计划的 2018H2 延迟到 2019。[^10][^11]

这说明的首先是：

> **当一个技术/制造路线承担主要升级节奏时，process execution、architecture cadence 与客户换代节奏会更强地绑定在同一路线图上。**

但这不能被反推为：

> **“市场集中导致了 Intel 10nm 延迟。”**

10nm 延迟有明确的 manufacturing / yield / implementation execution 因素，不能用市场结构代替工程因果。

竞争恢复也没有简单发生为“Intel 内部突然加速”。AMD 在 **2017 年**推出第一代 Zen/Ryzen，重新建立高性能 x86 竞争；Apple 在 **2020 年**推出第一颗为 Mac 设计的 M1，开出另一条 vertically integrated client-compute path。[^12][^13]

因此，这段历史更有价值的制度记忆是：

> **当可执行第二系统很弱时，在位者对产业升级节奏拥有更大的定义权；当新的竞争真正出现，它往往通过另一套 architecture / manufacturing / system path 改写原有边界。**

这与 2026 年 AI infrastructure 的相似处是 **migration cost 与 system definition**，而不是当前产品节奏：

- Intel 客户端后期面对的是成熟市场与 process delay；
- 2026 年 NVIDIA data-center stack 面对的是需求爆发、快速 roadmap 与 scarce-capacity allocation；
- 前者更接近“升级节奏变薄”；
- 后者当前更接近“想升级但资源、迁移和 quantity assurance 受限”。

所以本报告**不把今天的 AI 紧缺称为“第二个 Intel 挤牙膏年代”**。

真正需要观察的长期风险是：

> **如果生产级第二 system stack 长期不能形成，那么今天由 scarce-layer access 与 migration cost 体现的“排队权”，未来可能进一步演变成由少数路线图决定“进步节奏”的权力。**

反过来，如果 AMD、hyperscaler custom systems、open/runtime portability、China parallel alternatives 等形成可执行 production second path，则这一历史类比会失效或显著减弱。

---

## 5. Qualcomm：Edge Substitution 会改变 Cloud Demand

Qualcomm 的相对优势更接近 smartphone、PC、edge AI、low-power compute 与 connectivity；公司 2026 年公开材料继续强调 Snapdragon X Series PC 上的本地 agentic AI 与 mobile on-device generative AI。[^5][^6]

它不需要复制 NVL72 才能获取 AI value。

如果 on-device model capability、memory efficiency 与 local inference 持续提高，更多 workload 可以从 cloud 移到 device，降低一部分 cloud inference demand。

因此 Qualcomm 对 AI infrastructure 的影响主要是**需求函数重构**，而不是直接替代 frontier training system。

## 6. Apple：Vertical Integration 改变 Workload Placement

Apple 的 silicon、OS、device、application ecosystem、distribution 与 installed base 高度垂直。Apple Intelligence 的公开架构同时使用 on-device processing 与 Private Cloud Compute，说明 workload placement 本身就是其 AI system design 的核心。[^7][^8]

Apple 不是 frontier training system vendor，但它可以决定大量 consumer workload：哪些在 device 完成，哪些调用 private / public cloud。

如果端侧 capability 快速提高，Apple 会成为影响 cloud inference intensity 的重要平台变量。

## 7. Leading-Edge Access 不支持虚构 Customer Ranking

Apple 长期使用 leading-edge processes，但在没有公司一手客户份额/排名披露时，本报告不把某一具体年份的“第一/第二大客户”身份作为事实。

真正要看的是：leading-node launch scale 是否保持、AI/HPC 对 incremental capacity 的吸收是否加速，以及 device-AI strategy 是否改变 wafer / memory mix。

这再次说明 historical revenue share 不能替代对下一代 incremental scarce-capacity access 的逐层分析。

## 8. Competitive Pressure 是 Multi-Directional

**Table 16.1 — 四类差异化竞争路径**

| 公司 | 主要竞争方向 |
|---|---|
| AMD | Data Center accelerator / system |
| Intel | CPU + accelerator + foundry |
| Qualcomm | edge / PC / mobile AI |
| Apple | vertically integrated on-device AI / workload placement |

**Source:** AMD、Intel、Qualcomm、Apple 官方产品与公司材料。[^1][^3][^5][^7]  
**Note:** 表中为竞争路径分类，不表示四家公司处于相同市场或拥有可直接比较的 market share。

NVIDIA 面对的是多层侵蚀，而不是一个统一对手。

## 9. 什么变化会提高 S1 Weight

- AMD 在 production system stack 上规模化；
- Intel foundry 与 product execution 同时改善，增加 manufacturing/system diversity；
- Qualcomm / Apple 推动更多 high-volume inference 移到 edge；
- open software / interfaces 降低 migration cost；
- HBM / packaging supply 更宽松。

这些变化可以共同提高 S1 相对 S2 的权重，但 S1/S2 是并列条件情景，不是必然连续阶段。

## 10. Current Read

传统芯片巨头没有消失，也没有形成统一联盟。

更现实的格局是：AMD 从 data-center system 正面竞争；Intel 同时修复 product 与 manufacturing；Qualcomm/Apple 从 edge / device 改写一部分需求。

它们是否真正削弱 dominant system-stack economics，最终要看 production workload share、software portability、scarce-resource access 与 customer migration，而不是产品发布数量。

## References

[^1]: AMD, Instinct / Helios official page, rack-scale solution integrating Instinct GPUs, EPYC CPUs, Pensando networking and ROCm, https://www.amd.com/en/products/accelerators/instinct.html
[^2]: AMD, “ROCm 10: A Simpler Path to Production AI on AMD,” 2026-08-27, https://www.amd.com/en/blogs/2026/amd-rocm-10-a-simpler-path-to-production-ai-on-amd.html
[^3]: Intel Corporation, 2025 Form 10-K, Intel Foundry and manufacturing strategy, https://www.intc.com/filings-reports/all-sec-filings/content/0000050863-26-000011/intc-20251227.htm
[^4]: Intel Foundry, 2026-06 VLSI Symposium process milestones, 18A production and 18A-P risk production, https://newsroom.intel.com/intel-foundry/intel-foundry-details-process-milestones-future-innovation-at-vlsi-symposium
[^5]: Qualcomm, 2026-08, agentic AI applications on Snapdragon X Series PCs, https://www.qualcomm.com/news/onq/2026/08/agentic-ai-apps-snapdragon-x-series
[^6]: Qualcomm, Mobile AI / on-device generative AI, https://www.qualcomm.com/smartphones/features/mobile-ai
[^7]: Apple, Apple Intelligence, on-device processing and Private Cloud Compute, https://www.apple.com/apple-intelligence/
[^8]: Apple Security Research, Private Cloud Compute security documentation, https://security.apple.com/documentation/private-cloud-compute/
[^9]: ASML, “High NA EUV reaches new readiness milestone with first high-volume Logic product,” 2026-07-15, Intel 18A select layers / Panther Lake HVM, https://www.asml.com/en/news/press-releases/2026/high-na-euv-reaches-new-readiness-milestone


[^10]: Intel Corporation, 2016 Form 10-K, lengthened utilization of 14nm and 10nm process technologies with multiple waves of products, https://www.intc.com/filings-reports/all-sec-filings/content/0000050863-17-000012/a10kdocument12312016q4.htm
[^11]: Intel Corporation, 2018 Form 10-K, 10nm volume-production delay from 2H18 into 2019 and process-execution risks, https://www.intc.com/filings-reports/all-sec-filings/content/0000050863-19-000007/a12292018q4-10kdocument.htm
[^12]: AMD, 2017-03-02, first Ryzen desktop processors based on the new Zen core architecture, https://www.amd.com/en/newsroom/press-releases/2017-3-2-amd-ryzen-tm-7-desktop-processors-featuring-recor.html
[^13]: Apple, 2020-11-10, M1 as the first chip designed specifically for Mac, https://www.apple.com/newsroom/2020/11/apple-unleashes-m1/

[^14]: AMD Newsroom, 2026-08-27, ROCm.AI generally available with ROCm 10, https://newsroom.amd.com/news/rocm-10-software-ai-native-developer-experiences/
