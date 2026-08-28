# Part I · 第1章：执行摘要与未来十年核心判断

## 1. 核心结论

> **AI infrastructure 的竞争单位已经从单颗芯片上移到完整 system stack。长期价值捕获越来越取决于谁能同时协调 advanced logic、HBM、advanced packaging、interconnect、software、rack/data center 与 power 等多个 scarce layers，并把这些物理资源转化为高利用率、可迁移、能够产生现金流的真实 workload。**

这不是“永久垄断”判断，也不是对 2036 年市场份额的单点预测。本报告讨论的是一套正在变化的资源配置机制：当 AI/HPC workload 的支付能力、订单期限、预付款和资本回报显著高于传统终端时，新增资本与稀缺资源更容易向 AI infrastructure 倾斜；当供给扩张、系统替代、利用率或商业回报发生变化时，这一结构也会重新平衡。

截至 **2026 年 8 月 28 日**，公开事实更符合 **S2 — Baseline Concentration**：少数 system platform 与 scarce-layer supplier 保持强经济性，HBM、advanced packaging 与 power 等物理约束仍然重要，同时 hyperscaler custom systems、中国 parallel stack 与供给扩张继续提供真实替代路径。

## 2. 八个事实锚

### 2.1 NVIDIA 的商业交付单位已经上移到 rack-scale system

GB200 NVL72 官方规格包含 **72 Blackwell GPU、36 Grace CPU、13.4 TB HBM3E 与 17 TB LPDDR5X**。这说明高端 AI infrastructure 的采购与交付对象已经从 accelerator card 上移到 compute、memory、interconnect、software 与 rack architecture 的组合。[^1]

### 2.2 NVIDIA 的 seller-side economics 仍处高位

NVIDIA FY27 Q2 披露 Revenue **US$96.221B**、Data Center revenue **US$89.0B**、GAAP gross margin **75.0%**、GAAP operating income **US$63.734B**；公司同时表示 Vera Rubin 已进入 full production。[^2]

### 2.3 Forward supply commitments 显著扩大

NVIDIA manufacturing, supply and capacity commitments 从 2026-01-25 的 **US$95.2B** 上升到 2026-07-26 的 **US$279B**。FY27 Q2 10-Q 说明，最新承诺主要涉及 data-center infrastructure systems 所需的 memory 与 manufacturing facilities，但没有披露 supplier-level split，因此不能把该总额直接分配给 TSMC、CoWoS 或任何单一 HBM vendor。[^3]

### 2.4 TSMC 的需求结构已经明显向 HPC 倾斜

TSMC 2025 年 HPC platform 占全年 net revenue **58%**，smartphone 占 **29%**；3 nm、5 nm、7 nm 分别占 wafer revenue **24% / 36% / 14%**。这些是 revenue mix，不是 customer-level wafer allocation，更不能直接换算成 CoWoS share。[^4]

2026 Q2，TSMC 的 HPC platform revenue 占季度营收 **66%**，smartphone 为 **22%**；同季 advanced technologies（7 nm 及以下）占 wafer revenue **77%**。这进一步显示 HPC 已成为先进制造增量需求的核心驱动力之一，但 HPC 仍不能与 AI 一一等同。[^5]

### 2.5 HBM 已进入制造资源竞争层

Micron 一手披露：在 **same technology node / same number of bits** 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。这是一项 wafer-supply trade ratio，不是售价倍数，也不是所有 HBM 世代固定不变的制造常数。[^6]

TrendForce 预计 HBM + RDIMM 约占 **2026 年 DRAM bit supply 的 51%**。该数字是机构预测而非 full-year actual；与 Micron 的约 3× trade ratio 联合观察，可以解释为什么 AI/server memory 对 conventional DRAM residual supply 的影响可能大于 bit share 本身。[^7]

### 2.6 Advanced Packaging 已成为可验证的 growth constraint

TSMC 在 4Q24 表示 advanced packaging capacity “very tight”，无法满足全部客户需求；在 2Q26 earnings call 中又明确表示 packaging capacity tightness 正在限制客户增长。TSMC 没有公开 customer-level CoWoS allocation，因此第三方对客户集中度的估计必须保留机构估计身份。[^8]

### 2.7 Power 已成为与 wafer、memory、packaging 并列的独立物理约束

NVIDIA DGX GB200 hardware guide 给出的 rack power 约为 **120 kW**。与此同时，835 MW 级核电重启、最高 1.92 GW 的长期 PPA、以及面向 2030–2035 的数百 MW 级先进核电开发计划，显示 Time-to-Power、grid connection、substation、firm power 与 permitting 已进入 AI system delivery 的约束集合。Contracted、Permitted、Energized、Utilized MW 必须严格分开。[^9]

### 2.8 Hyperscaler custom systems 已经形成真实第二路线

Google Ironwood、AWS Trainium3 UltraServers、Microsoft Maia 200 与 Meta MTIA 300 均显示，hyperscaler 的竞争已经从“自研一颗 ASIC”上移到 accelerator、compiler/runtime、interconnect、rack/pod 与 captive workload 的 system-stack competition。[^10]

这并不等于 NVIDIA 已被替代。真正需要观察的是这些系统承担多少 production workload、迁移成本是否下降、利用率是否可持续，以及它们是否仍竞争同一批 advanced logic、HBM、packaging 与 power。

## 3. 七个核心机制

### 3.1 Scarce-layer Value Capture

当某个平台同时拥有高现金流、长期订单、system definition、switching cost 与 supply orchestration 能力时，它更有能力提前承诺下一代稀缺资源，从而提高交付确定性。高毛利率只是这一机制的结果之一，不等于法律意义上的 monopoly finding。

### 3.2 AI Resource Gravity

当 AI/HPC workload 能提供更高风险调整后回报、更长期订单和更强利用率可见性时，资本与有效产能更容易向 advanced logic、HBM、advanced packaging、networking 与 power 等高价值层移动。

### 3.3 Non-AI Residual Capacity

传统行业面对的不是“全球总产能”，而是完成优先分配后仍然能够获得的有效残量：

```text
NonAI_Residual(t)
= Effective_Supply(t)
- AI_Absorption(t)
- Other_Priority_Demand(t)
```

因此，“总供给增长”与“smartphone / PC 等传统终端仍然承受价格和配置压力”可以同时成立。

### 3.4 Two-Speed Semiconductor Economy

AI Infrastructure Economy 与 Traditional Device Economy 共享部分上游资源，却具有不同的价格承受能力、合同期限、预付款结构、BOM 约束与终端价格弹性。

核心变化不是“消费电子消失”，而是：

> **AI/HPC 正在提高少数高资本强度买方对半导体边际需求和新增资本形成的影响力。**

### 3.5 AI Capacity Gap：绝对缺口与增长缺口必须分开

为了判断某一物理层**当前是否真的短缺**，本报告定义绝对缺口：

```text
AI_Capacity_Gap_i(t)
= AI_Effective_Demand_i(t)
- AI_Effective_Capacity_i(t)
```

其中 \(i\) 分别代表 advanced logic、HBM/DRAM、advanced packaging、networking、power 等物理层。Demand 与 Capacity 必须使用**同一交付窗口、同一质量/认证边界和同一物理单位**，例如 wafers/month、qualified package starts/month、bits/year 或 MW。

- **Absolute Gap > 0**：当前存在可交付供给缺口；
- **Absolute Gap ≈ 0**：当前供需接近平衡；
- **Absolute Gap < 0**：当前存在有效余量。

为了判断短缺压力是在扩大还是收敛，再单独定义：

```text
AI_Capacity_Growth_Gap_i(t)
= Growth(AI_Effective_Demand_i(t))
- Growth(AI_Effective_Capacity_i(t))
```

Growth Gap 的单位是同一期间的增长率差（percentage points），它只描述**缺口变化方向**，不能替代绝对缺口：

- **Growth Gap > 0**：短缺可能扩大，或既有余量被侵蚀；
- **Growth Gap < 0**：短缺可能收敛，或有效余量扩大；
- **Growth Gap = 0**：只表示供需以相同速度变化，不表示当前没有短缺。

因此，S4 Capital Hard Landing 的强信号不是“Growth Gap < 0”本身，而是 **Absolute Gap < 0 / excess capacity** 与 utilization、clearing price、forward commitments 同步恶化。

AI Capacity Gap、AI Capacity Growth Gap 与 Non-AI Residual Capacity 是三类不同问题：前两者观察 AI 侧当前缺口及其变化方向，NARC 观察优先分配后非 AI 市场还能获得多少有效资源。

### 3.6 Cloud System-Stack Substitution

Hyperscaler custom stack 可以同时产生两种方向相反但并存的效应：

1. **Platform-profit diversion**：部分 workload 不再支付完整外部平台 economics；
2. **Upstream resource competition**：custom system 自身仍需要先进逻辑、HBM、packaging 与 power。

因此，“更多 custom silicon”并不自动意味着上游物理稀缺缓解。

### 3.7 Anchor Compute Buyer Effect

大型 model company 的多年、十年级 compute commitment 可以提高基础设施项目的 revenue visibility 与融资确定性，推动 cloud、data center、power 与 semiconductor capacity 提前建设；反过来，如果 utilization 或 monetization 不足，长期承诺也会放大 duration-mismatch 与 stranded-capacity risk。

## 4. 中国必须按系统层级判断，而不能用一个“国产化率”概括

中国已经形成真实且持续发展的 accelerator/software parallel stack，并在 consumer computing、DRAM/NAND、部分通用计算与本土软件生态上形成更强的平行供给能力；但 frontier AI 的等价闭环仍需要 advanced logic、HBM-class memory、advanced packaging、high-speed interconnect、compiler/runtime、frontier workload 与 power 同时达到可验证规模。[^11]

因此，本报告不采用“已经全面追平”或“完全没有替代能力”两种极端表述。更准确的状态是：

> **中国已经跨过“没有替代系统”的阶段，但公开证据尚不足以证明所有 frontier critical layers 都已经形成全球等价规模闭环。**

## 5. 资本周期不能用一个 CapEx 总额判断

Cloud CapEx、system-vendor revenue、foundry revenue、memory revenue 与 power/data-center investment 会在产业链不同账本中重复出现，因此不能机械相加为“全球 AI 总投入”。

判断 **S4 — Capital Hard Landing** 必须至少同时观察四组信号：

- **Accounting**：impairment、write-down、折旧压力；
- **Utilization / Revenue**：有效利用率、单位收入、真实 monetization；
- **Market Clearing**：lease rate、二手价格、lead time、inventory；
- **Forward Commitment**：CapEx guidance、supply commitments、Anchor Buyer contracts。

截至 2026 年 8 月，本报告判断公开事实更符合：

> **高强度资本扩张 + ROI 压力上升**

而不是已经确认的全行业 Capital Hard Landing。

## 6. S1–S4：未来不是一条确定曲线

**Table 1.1 — AI 基础设施四类标准情景**

| 情景 | 核心结构 |
|---|---|
| S1 — Competitive Expansion | supply elasticity 与 interoperability 上升，多系统栈共存，value capture 更分散 |
| S2 — Baseline Concentration | 少数 system platform 与 scarce-layer supplier 保持强经济性，同时替代路线持续发展 |
| S3 — Resource Hegemony | 多个 scarce layers 与 switching cost 同时强化，后来者必须复制更完整 infrastructure stack |
| S4 — Capital Hard Landing | utilization、clearing price、CapEx/commitments 与 accounting losses 同步恶化 |

**Source:** 本报告情景框架。  
**Note:** S1–S4 是并列条件状态，不赋固定概率，也不被视为必然连续阶段。

截至 2026 年 8 月，**S2 — Baseline Concentration** 是最接近当前事实组合的基准状态，但不是固定十年预测。

## 7. 什么事实会迫使本报告改判

以下变化应显著降低 S2/S3 权重或迫使相关机制重估：

- leading system-platform commitments 持续下降或大规模取消；
- advanced packaging 不再被主要供应商描述为 growth constraint；
- HBM / DRAM residual supply 长期显著宽松；
- cloud custom systems 在 frontier workload 上形成低迁移成本的大规模替代；
- energized power 与 grid interconnection 大幅改善，Time-to-Power 不再造成项目差异；
- Anchor Compute Buyer commitments 大规模改期或利用不足；
- China frontier-system closure 在多个关键层获得规模化一手证据并显著提高替代能力；
- formal regulatory remedy 实质性降低 proprietary-interface switching cost。

反过来，如果 AI Capacity Gap 在多个物理层长期保持正值、NARC 持续下降、migration cost 仍高、forward commitments 继续扩张，则 S3 Resource Hegemony 的相对权重会上升。

## 8. 本报告结构

本报告分为四部分：

- **Part I — 系统权力与物理稀缺：** system stack、advanced logic、HBM、advanced packaging、power 与 manufacturing redundancy；
- **Part II — 需求、替代与第二系统栈：** model economics、hyperscaler custom systems、Anchor Compute Buyers、China parallel stack 与竞争政策；
- **Part III — 资本周期、利润池与外部传导：** CapEx、value capture、consumer transmission、depreciation、financing、capital clearing 与 labor；
- **Part IV — 方法、情景、监测与战略：** evidence architecture、2026–2036 milestones、monitoring framework、S1–S4 与最终战略判断。

读者如果只阅读一章，应以本章作为全书结论入口；如果需要核验任一高影响数字，应继续进入对应主题章与 References。

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
