# Part I · 第6章：Advanced Packaging、CoWoS 与系统交付瓶颈


## 1. Advanced packaging 已经从配套环节变成系统交付层

frontier AI accelerator 越来越依赖 multi-die integration、HBM、large interposer 与 high-speed die-to-die connection。于是 advanced packaging 不再只是“芯片做完之后的后段工序”，而成为：

> **决定一个 frontier AI system 能否按数量交付的 scarce manufacturing layer。**

这解释了一个看似矛盾的现象：foundry 逻辑晶圆可以继续扩产，但完整 system 仍然可能因为 packaging/HBM integration 不足而无法交付。

## 2. TSMC 已经一手确认 tightness，但年份口径必须分开

TSMC 的公开表述足以确认 advanced-packaging tightness：

- 2024 Q4：管理层称相关 capacity **very tight**，不能满足全部客户需求；
- 2026 Q2：管理层明确称 packaging capacity **so tight that now it limits my customers' growth**。

收入披露也必须保持原始年份标签：

- 4Q24 transcript：**advanced packaging and testing >8% of revenue**；
- 4Q25 transcript 的公司会后更正口径：**advanced packaging slightly over 10% of 2025 revenue**。

这两个标签并不完全相同，因此出版层**不把 >8% → >10% 当作严格同口径连续时间序列**，也不把 2025 的 advanced packaging 扩写回 “advanced packaging + testing”。

## 3. CoWoS tightness 是 A 级事实，customer allocation 不是

TSMC 公开资料能够支持：advanced packaging 很紧、CoWoS 是其中重要组成、packaging tightness 已经限制客户增长。

但 TSMC 没有公开一张可用于本书的 customer-level CoWoS allocation table，也没有给出按客户拆分的官方 CoWoS share。

因此必须把两个问题分开：

- **A 级事实：** packaging / CoWoS tightness；
- **未披露：** 每个客户究竟获得多少 CoWoS capacity。

年度 customer revenue share、wafer revenue share 与 CoWoS customer share 也不能互换。

## 4. NVIDIA >60% CoWoS demand 是 B 级机构锚

TrendForce 对 2025 CoWoS demand 的研究将 NVIDIA 列为最大需求客户，并估计其需求占比 **超过 60%**。

这条信息很重要，但证据等级必须保持为 **B — institutional estimate**。它可以用于判断需求集中度和设计压力测试，却不能改写成：

- TSMC 官方确认 NVIDIA 拿到 >60% allocation；
- >60% 已经是 2026 actual；
- NVIDIA 拥有排他性 CoWoS 权利。

正确用法是：**高集中 demand 有现实机构锚，但真实 allocation 仍需等待一手披露。**

## 5. 5.37 CoWoS wafers/rack 是 D 级几何压力测试

本书曾使用一个数量级模型：72 个 GPU package ÷ 约 13.4 packages/wafer ≈ **5.37 CoWoS wafers/rack**。

其中：

- 72 GPU 来自 NVL72 官方产品规格；
- ~13.4 packages/wafer 是报告侧 geometry assumption；
- 5.37 因而属于 **D 级 stress test**。

它**不是** TSMC disclosed yield、actual wafer starts、logic-wafer demand 或 customer allocation。

这一边界非常重要，因为 advanced-packaging wafer 与 TSMC 全年 12-inch-equivalent wafer shipments 并不是同一个物理池。

## 6. 为什么不能用全厂 wafer shipments 去除 5.37

TSMC 2025 全年约 **15.0M 12-inch-equivalent wafer shipments** 覆盖 smartphone、HPC、automotive、IoT、mature nodes 等大量前道产品。5.37 则是报告侧对 **CoWoS packaging wafer/rack** 的几何压力测试。

所以如下运算没有物理意义：

> 全厂 annual wafer shipments ÷ 5.37 = 可生产 AI racks

这会把前道逻辑 wafer pool 与后道 advanced-packaging pool 混为一个分母。由此得到的 80 万柜、量纲错误的超大柜数或其他超大柜数，都不能作为系统交付能力事实。

同样，也不能把前道 logic-wafer/rack 与后道 CoWoS-wafer/rack 两个模型直接相加成“每柜吃多少 TSMC wafers”。它们处在不同制造工序和不同 capacity pool。

## 7. Packaging 为什么可能比 node 更早成为数量闸门

leading-edge logic 可以通过 new fab、process migration 与 capacity expansion 逐步增加供给；advanced packaging 则同时受 tool、interposer、substrate、testing、process flow、HBM integration 与 qualification 约束。

于是会出现：

> **logic wafer available ≠ system deliverable**

先进节点更像进入 frontier system 的“入场券”，advanced packaging 则更像决定能交付多少完整 system 的“数量闸门”。两者都重要，但物理单位和扩产时钟不同。

## 8. Incremental Capacity Capture 应该用情景模型，而不是伪造当前 share

如果新增 packaging capacity 为 C，某平台捕获其中比例 s，则其他买方获得的新增 residual capacity 为：

> **Residual = (1 − s) × C**

| 假设捕获率 | 其他买方 residual |
|---:|---:|
| 50% | 50% |
| 60% | 40% |
| 70% | 30% |
| 80% | 20% |

这些 50/60/70/80% 是 **D 级 scenario levels**，不是 TSMC 当前 customer allocation。

这个模型真正说明的是非线性：头部买方如果持续获得更大比例的**新增**资源，第二、第三买方可获得的增量会迅速收缩，即使全行业总 packaging capacity 仍然在增长。

## 9. Cloud custom silicon 不会自动绕开 packaging/HBM

Google、AWS、Microsoft、Meta 的 custom accelerator system 会分流 NVIDIA platform profit，但下一代云系统本身仍大量依赖 advanced logic、HBM 与高密度 integration。

所以两个效应可以同时出现：

1. **platform substitution**：云自研降低对 NVIDIA 完整平台的依赖；
2. **upstream competition**：云自研又增加对同一先进制造、HBM 和 packaging 资源的需求。

这就是为什么“更多 custom silicon”不自动等于“CoWoS/HBM pressure 下降”。

## 10. Bottleneck location 不等于 profit location

advanced packaging 可以是系统交付的短板，但不一定拥有整个价值链最高 margin。TSMC 2Q24 的管理层表述更精确：advanced-packaging gross margin 过去显著低于 corporate average，当时正在接近但尚未达到公司平均。

因此，物理瓶颈与利润池必须分开：

- packaging 可能决定“能不能交付”；
- system platform 则可能通过 software、interconnect、integration 与 customer switching cost 捕获更高 system-level economics。

> **bottleneck location ≠ profit location**

这是分析 AI infrastructure 价值捕获时不能混淆的两个问题。

## 11. Packaging 也是 China Parallel Stack 的独立 closure gate

frontier AI parallel stack 不能只用 logic node 判断。即使 accelerator die 可生产，如果 advanced packaging、substrate、HBM integration、testing 与 high-volume yield 不足，仍然无法稳定交付大型 system。

所以“国产芯片”不能掩盖 packaging 这一独立物理层。China system closure 必须把 logic、HBM、packaging、interconnect、software 和 power 分开验证。

## 12. 当前判断与证伪条件

截至 2026 年 8 月，最稳健的结论是：

- TSMC 已一手确认 advanced-packaging tightness；
- TrendForce 为 NVIDIA 高 CoWoS demand concentration 提供 B 级机构锚；
- customer-level allocation 仍未由 TSMC 官方披露；
- 5.37 wafers/rack 只能作为 D 级 geometry stress test；
- custom silicon 仍可能竞争相同 upstream scarce resources。

如果未来 TSMC 不再描述 packaging 为增长约束、交期显著缩短、customer-level allocation 更分散、以及 HBM/packaging supply elasticity 持续上升，本章对 advanced packaging 作为核心 scarce layer 的判断应下调。

## 关键公开来源

- TSMC 4Q24 Transcript — advanced packaging and testing >8%; capacity very tight: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf
- TSMC 4Q25 Transcript — 2025 advanced packaging slightly over 10%, company-corrected wording: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
- TSMC 2Q26 Earnings Conference Transcript — packaging capacity limits customers' growth: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
- TSMC 2Q24 Transcript — advanced-packaging margin relative to corporate average: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2024-08/5122725a56670882d777a8e8bfe0ed247cc55330/TSMC%202Q24%20Transcript.pdf
- TrendForce, 2025 CoWoS demand structure — NVIDIA estimated >60%: https://www.trendforce.com/research/download/RP250314ZJ
- NVIDIA GB200 NVL72 product page — 72 Blackwell GPUs/rack: https://www.nvidia.com/en-us/data-center/gb200-nvl72/