# Part I · 第1章：执行摘要与未来十年核心判断

> **出版层入口章。** 以 [vol-01](../vol-01.md) 为事实底座，并引用已生成的 canonical publication chapters。本章只给出读者进入全书所需的事实锚、核心机制、情景框架与证伪条件，不在这里重复后文工程推导。

## 1. 一句话结论

> **AI infrastructure 的竞争单位已经从单颗芯片上移到完整 system stack，而长期价值捕获越来越取决于谁能协调 advanced logic、HBM、advanced packaging、interconnect、software、rack/data center 与 power 等多个 scarce layers，并把这些物理资源转化为高利用率、可迁移、能产生现金流的真实 workload。**

这不是“永久垄断”判断。它描述的是当前资源竞争的结构，以及什么条件会让集中度增强、分散或进入资本清算。

## 2. 当前最重要的八个事实锚

### 2.1 NVIDIA 的销售单位已经上移到 rack-scale system

GB200 NVL72 官方产品规格为 **72 Blackwell GPU、36 Grace CPU、13.4 TB HBM3E、17 TB LPDDR5X**。这意味着客户购买的是 compute、memory、interconnect、software 与 rack architecture 的组合，而不再只是 accelerator card。

### 2.2 NVIDIA 的 seller-side economics 仍处高位

FY27 Q2 Revenue **US$96.221B**、Data Center revenue **US$89.0B**、GAAP gross margin **75.0%**、GAAP operating income **US$63.734B**；Vera Rubin 已进入 full production。

### 2.3 Forward supply commitments 显著扩大

NVIDIA manufacturing, supply, and capacity commitments 由 2026-01-25 的 **US$95.2B** 上升到 2026-07-26 的 **US$279B**。Q2 10-Q 说明最新承诺主要关联 data-center infrastructure systems 所需的 memory 与 manufacturing facilities，但没有 supplier-level split。

### 2.4 TSMC 的 HPC 权重已经高于 smartphone

TSMC 2025 HPC platform 占全年 net revenue **58%**，smartphone **29%**；3 nm / 5 nm / 7 nm 分别占 wafer revenue **24% / 36% / 14%**。customer revenue share、wafer share 与 CoWoS allocation 必须严格分开。

### 2.5 HBM 已进入制造资源竞争层

Micron 一手披露：same node / same bits 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。TrendForce 预计 2026 年 HBM + RDIMM 合计约占 DRAM bit supply **51%**。

### 2.6 Advanced Packaging 已成为可验证 growth constraint

TSMC 4Q24 表示相关 capacity very tight、无法满足全部客户需求；2Q26 更明确指出 packaging tightness 已限制客户增长。TSMC 没有公开 customer-level CoWoS allocation。

### 2.7 Power 已进入独立物理约束层

约 **120 kW-class rack** 与数百 MW / GW 级长期电力项目显示，grid connection、substation、firm power、permit 与 Time-to-Power 已成为 system delivery 的组成部分。Contracted、Permitted、Energized、Utilized MW 不可混用。

### 2.8 Cloud custom systems 已经成为真实第二路线

Google Ironwood、AWS Trainium3 UltraServer、Microsoft Maia、Meta MTIA 均显示 hyperscaler 已从“自研芯片”上移到 compiler/runtime、interconnect、rack/pod 与 captive workload 的 system-stack competition。

## 3. 五个核心机制

### Scarce-layer Value Capture

高现金流、长期订单、switching cost、system definition 与 supply orchestration 可以提高下一代 scarce input 的预订能力，使当前优势跨代延续。

### AI Resource Gravity

当 AI workload 能支付更高价格、提供更长订单与更高确定性时，资本与产能会向 advanced logic、HBM、packaging、networking 与 power 等高价值层移动。

### Non-AI Residual Capacity

传统市场真正面对的不是全行业总供给，而是高价值 AI/server demand 吸收之后仍可获得的有效 residual capacity。

### Cloud System-Stack Substitution

hyperscaler 自研栈既可以分流 NVIDIA platform profit，也可能继续竞争同一 advanced logic、HBM、packaging 与 power，因此平台替代与上游资源竞争可以同时发生。

### Anchor Compute Buyer Effect

大型 model company 的多年容量承诺可以提高基础设施融资确定性，推动 cloud、data center、power 与 semiconductor 提前建设；反过来，利用不足也会放大 duration-mismatch risk。

## 4. 中国必须按系统层级分析

中国供给能力不能用一个“国产化率”概括。consumer computing、PC/workstation 与 frontier AI 的 closure requirements 不同。

当前最准确的描述是：中国已经形成真实的 accelerator/software parallel stack，并在消费与部分通用计算拥有较强产业基础；但 frontier AI 等价闭环仍需 advanced logic、HBM-class memory、advanced packaging、interconnect、compiler/runtime、large workload 与 power 同时达到可验证规模。

## 5. 资本周期不能用一个 CapEx 总额判断

Cloud CapEx、system-vendor revenue、foundry revenue、memory revenue 与 power/data-center investment 会在产业链不同账本重复出现，因此不能机械相加成“全球 AI 总投入”。

判断 S4 Capital Hard Landing 必须同时观察：

- Accounting losses / impairment；
- Utilization / effective revenue；
- Market-clearing prices / lead time；
- Forward commitments / CapEx / Anchor Buyer contracts。

截至 2026 年 8 月，更符合事实的是 **高强度资本扩张 + ROI 压力上升**，而不是已经确认的全行业硬着陆。

## 6. S1–S4：未来不是一条确定曲线

| 情景 | 核心结构 |
|---|---|
| S1 — Competitive Expansion | supply elasticity 与 interoperability 上升，多系统栈共存，value capture 更分散 |
| S2 — Baseline Concentration | 少数 system platform 与 scarce-layer supplier 保持强经济性，同时替代路线持续发展 |
| S3 — Resource Hegemony | 多个 scarce layers 与 switching cost 同时强化，后来者必须复制更完整 infrastructure stack |
| S4 — Capital Hard Landing | utilization、clearing price、CapEx/commitments 与 accounting losses 同步恶化 |

截至 2026 年 8 月，本报告将 **S2** 作为最接近当前事实组合的基准状态，而不是固定十年预测。

## 7. 什么事实会迫使我们改判

以下变化应显著下调“稀缺层价值捕获继续强化”的判断：

- leading system-platform commitments 持续下降或大规模取消；
- advanced packaging 不再是 growth constraint；
- HBM / DRAM residual supply 长期显著宽松；
- cloud custom systems 在 frontier workload 上形成低迁移成本的大规模替代；
- power / interconnection 不再造成部署差异；
- Anchor Compute Buyer commitments 大规模改期或利用不足；
- China frontier-system closure 获得多个关键层的规模化一手证据并显著提高替代能力；
- regulatory remedy 实质性降低 proprietary-interface switching cost。

## 8. 阅读路径

建议按以下顺序理解全书主线：

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

## 核心公开来源导航

- [核心证据台账](../核心证据台账.md)
- [核心参考文献索引](../核心参考文献索引.md)
- NVIDIA FY27 Q2 official results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- TSMC 2025 Annual Report: https://investor.tsmc.com/static/annualReports/2025/english/index.html
- Micron FY24 Q2 Prepared Remarks: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- TrendForce 2026E memory structure: https://www.trendforce.com/presscenter/news/20260825-13198.html