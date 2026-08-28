# Part II · 第16章：AMD、Intel、Qualcomm 与 Apple 的差异化竞争路径

## 1. 不能把四家公司放进一个“传统芯片阵营”

AMD、Intel、Qualcomm、Apple 的 compute layer、software、manufacturing access、workload、distribution 与 capital structure 都不同。

因此，正确问题不是谁“联合挑战 NVIDIA”，而是：

> **每家公司正在攻击 system-stack dominance 的哪一个层级？**

## 2. AMD：最直接的 Data Center System Challenger

AMD Instinct 是最直接的 data-center accelerator alternatives 之一，AMD 当前官方路线也已把 Instinct GPU、EPYC CPU、Pensando networking 与 ROCm 组织为 rack/system 级解决方案。[^1][^2]

真正的门槛不只是 GPU design，而是：

- ROCm / software maturity；
- scale-up / scale-out；
- HBM；
- advanced packaging；
- system reference architecture；
- customer migration / production support。

因此 AMD 的竞争单位也已经从 chip 上移到 system。

## 3. AMD 同样暴露于 Scarce-resource Access

AMD 与 NVIDIA 会竞争相同的 advanced logic、HBM 与 packaging。

所以 NVIDIA demand 极强时，AMD 的挑战不仅是 market share，也包括 incremental scarce capacity access。

反过来，如果 HBM/packaging supply elasticity 提高，AMD system expansion 的约束会下降。

这使 AMD 成为观察 **non-anchor-buyer access / Non-AI-and-non-leading residual capacity** 的重要对象，但本书不为它另造新的核心术语。

## 4. Intel：Product Clock 与 Foundry Clock 是两条时间线

Intel 同时承担 CPU/product competition、accelerator attempts、foundry strategy 与 domestic manufacturing policy。Intel 2025 10-K 与 2026 VLSI Symposium 更新显示 Intel Foundry 仍在推进 external-foundry strategy，18A 已进入 production、18A-P 进入 risk production。[^3][^4]

Product clock 需要在短周期交付 performance、software 与 customer adoption；foundry clock 则需要长期建立 process、yield、customer trust、packaging 与 high-volume execution。

因此，Intel 的复苏不能由一颗产品或一座 fab 单独证明。

## 5. Qualcomm：从 Edge 改写 Cloud Demand

Qualcomm 的相对优势更接近 smartphone、PC、edge AI、low-power compute 与 connectivity；公司 2026 年公开材料继续强调 Snapdragon X Series PC 上的本地 agentic AI 与 mobile on-device generative AI。[^5][^6]

它不需要复制 NVL72 才能获取 AI value。

如果 on-device model capability、memory efficiency 与 local inference 持续提高，更多 workload 可以从 cloud 移到 device，降低一部分 cloud inference demand。

因此 Qualcomm 对 AI infrastructure 的影响主要是**需求函数重构**，而不是直接替代 frontier training system。

## 6. Apple：Vertical Consumer Stack 的力量在 Workload Placement

Apple 的 silicon、OS、device、application ecosystem、distribution 与 installed base 高度垂直。Apple Intelligence 的公开架构同时使用 on-device processing 与 Private Cloud Compute，说明 workload placement 本身就是其 AI system design 的核心。[^7][^8]

Apple 不是 frontier training system vendor，但它可以决定大量 consumer workload：哪些在 device 完成，哪些调用 private / public cloud。

如果端侧 capability 快速提高，Apple 会成为影响 cloud inference intensity 的重要平台变量。

## 7. Apple 是 Leading-edge User，但不制造未经披露的客户排名

Apple 长期使用 leading-edge processes，但在没有公司一手客户份额/排名披露时，本书不把某一具体年份的“第一/第二大客户”身份作为事实。

真正要看的是：leading-node launch scale 是否保持、AI/HPC 对 incremental capacity 的吸收是否加速，以及 device-AI strategy 是否改变 wafer / memory mix。

这再次说明 historical revenue share 不能替代对下一代 incremental scarce-capacity access 的逐层分析。

## 8. 四家公司对主栈的影响来自不同方向

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

## 9. 哪些变化会提高 S1 Competitive Expansion 的权重

- AMD 在 production system stack 上规模化；
- Intel foundry 与 product execution 同时改善，增加 manufacturing/system diversity；
- Qualcomm / Apple 推动更多 high-volume inference 移到 edge；
- open software / interfaces 降低 migration cost；
- HBM / packaging supply 更宽松。

这些变化可以共同提高 S1 相对 S2 的权重，但 S1/S2 是并列条件情景，不是必然连续阶段。

## 10. 当前判断

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
