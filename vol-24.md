# 第二十四卷：Advanced Packaging、CoWoS 与 AI 系统交付瓶颈

## 1. Advanced packaging 已经从配套环节变成系统约束

AI accelerator 越来越依赖：

- multi-die integration；
- HBM；
- large interposer；
- high-speed die-to-die connection。

因此，advanced packaging 的角色从“封装完成品”上升为：

> 决定一个 frontier AI system 能否实际交付的 scarce manufacturing layer。

## 2. TSMC 一手证据已经足以证明 tightness

TSMC 2024 Q4：

> very tight capacity and cannot even meet customers' need

TSMC 2026 Q2：

> packaging capacity is so tight that now it limits my customers' growth

同时，TSMC 披露：

- 2024 Q4 transcript：**advanced packaging and testing >8% of revenue**；
- 2025 Q4 transcript（公司会后更正）：**advanced packaging slightly over 10% of revenue**。

两条披露的标签不同，因此不能把 2024 的“advanced packaging and testing”直接改写成“advanced packaging”，也不能把 8%→10% 当作严格同口径连续序列。

TSMC 当前公开年报与法说材料没有提供可用于本报告的 CoWoS customer-level allocation 或完整 CoWoS 分项收入表。因此，本报告不能把公开的 advanced-packaging 数据进一步硬拆成 CoWoS 客户份额。

因此：

> CoWoS tightness 是 A 级事实；customer split 不是。

## 3. NVIDIA >60% CoWoS demand 属于 B 级机构研究

TrendForce 对 2025 CoWoS demand 的估计显示 NVIDIA 占比超过 60%。

这是一条重要信息，但证据等级必须严格标为 **B**。

它不能写成：

- TSMC official disclosure；
- actual wafer allocation；
- guaranteed future share。

正确用途是：

> 说明 NVIDIA 对 CoWoS demand 的影响非常大，并用于 scenario analysis。

## 4. 5.37 CoWoS wafers/rack 属于 D 级压力测试

本报告 geometry stress test（其中 **13.4 packages/wafer 是 D 级几何假设，不是 TSMC disclosed yield**）：

```text
72 	ext{packages}
÷
13.4 	ext{packages/wafer}
≈
5.37 	ext{CoWoS wafers/rack}
```

该数字仅表示 rack-scale system 对 CoWoS 的潜在数量级压力。

它不是：

- TSMC yield；
- actual wafer starts；
- logic wafer demand；
- real customer allocation。

因此，5.37 不能与 TSMC annual ~15M **12-inch-equivalent wafer shipments** 混用；两者分母不同。

## 5. 为什么 packaging 比 node 更容易成为短期配额

leading-edge fab 可以通过：

- new fab；
- process migration；
- capacity expansion

逐步增加 supply。

advanced packaging 则同时受：

- tool；
- interposer；
- substrate；
- testing；
- process flow；
- HBM integration

约束。

因此，在某些阶段：

> logic wafer available 并不意味着 system deliverable。

这正是 packaging 成为 bottleneck 的原因。

## 6. Incremental Capacity Capture 场景

如果新增 CoWoS 资源为 (C)，某平台捕获比例为 (s)，则其他买方残量为：

```text
Residual = (1-s)C
```

例如：

| Capture | Residual for others |
|---:|---:|
| 50% | 50% |
| 60% | 40% |
| 70% | 30% |
| 80% | 20% |

这个模型不预测真实 share。

它只说明：

> 当一号买方对新增资源的捕获率继续上升时，第二、第三买方可获得的 residual capacity 会快速下降。

这比争论某一月到底是“13万片还是14万片”这类**未经一手披露验证的月度产能估计**更有分析价值。

## 7. Cloud custom silicon 并没有自动逃离 CoWoS/HBM

Google、AWS、Microsoft、Meta 的新一代 accelerator system 仍然大量采用：

- advanced logic；
- HBM；
- advanced packaging。

因此，cloud custom silicon 会改变：

- 谁定义 chip；
- 谁收 software/platform profit；

但未必降低上游 CoWoS/HBM demand。

它甚至可能提高 upstream resource competition。

## 8. Packaging 与 profit pool 要分开

advanced packaging 可以是 supply bottleneck，但不一定是最大利润池。

TSMC 2Q24 法说的更准确表述是：advanced packaging gross margin **过去显著低于公司平均，正在接近 corporate average；当时尚未达到**。这是一条带明确时点的管理层表述，不能永久化成“advanced packaging margin 始终低于公司平均”。来源：https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2024-08/5122725a56670882d777a8e8bfe0ed247cc55330/TSMC%202Q24%20Transcript.pdf 。

相比之下，system platform 可以通过：

- software；
- interconnect；
- integration；
- customer lock-in

获得更高 system-level margin。

因此：

> bottleneck location ≠ profit location。

这是理解 AI infrastructure 价值链最重要的区别之一。

## 9. China 与 packaging

中国 frontier AI parallel stack 是否闭环，很大程度上取决于：

- domestic advanced packaging；
- HBM integration；
- substrate；
- testing；
- high-volume yield。

只有 logic node，没有 packaging scale，仍然无法稳定交付大型 AI system。

因此，advanced packaging 是评估 China parallel stack 时不能被“国产芯片”总词掩盖的一层。

## 10. 当前判断

截至 2026 年 8 月：

- advanced packaging tightness 已被 TSMC 一手确认；
- NVIDIA 对 CoWoS demand 的高影响力有机构研究支持；
- customer-level share 仍未由 TSMC 披露；
- 5.37 wafers/rack 只能用于 D 级压力测试；
- cloud custom silicon 仍然在竞争相同 scarce upstream resources。

因此，CoWoS 是 AI infrastructure 当前最重要的物理配额之一，但其真实 customer allocation 必须继续保持证据边界。

## 本卷关键公开来源

- TrendForce, 2025 CoWoS demand structure（NVIDIA estimated >60%, B-grade institutional estimate）： https://www.trendforce.com/research/download/RP250314ZJ

- TSMC 4Q24 Transcript（advanced packaging and testing >8%）：https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf
- TSMC 4Q25 Transcript（2025 advanced packaging slightly over 10%，company-corrected）：https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
- TSMC 2Q26 Earnings Conference Transcript（packaging capacity limits customers' growth）：https://investor.tsmc.com/english/quarterly-results/2026/q2
- TSMC 2025 Annual Report（~15.0M 12-inch-equivalent wafer shipments）：https://investor.tsmc.com/static/annualReports/2025/english/index.html
