# 第九卷：AI 基础设施扩张对实体供应链的传导

## 1. 冲击不是“AI 抢走全部芯片”

AI infrastructure 对实体制造业的影响具有高度选择性。

最先受到影响的不是所有工业部门，而是与 AI system 共享以下资源的品类：

- advanced logic；
- HBM / DRAM；
- advanced packaging；
- high-end substrate；
- power management；
- networking components。

因此，本卷分析的是 **supply-chain transmission**，而不是“全球制造业全面缺芯”。

## 2. 第一层传导：PC 与 gaming

消费 GPU 与 Data Center accelerator 会共享部分先进 manufacturing resources。

NVIDIA 曾公开披露 gaming GPU supply constraints，这说明 consumer GPU 并非完全独立于 Data Center allocation。

PC 同时受到第二条传导：

HBM/server demand 上升  
→ memory vendor 调整 product mix  
→ conventional DDR5 residual supply 变化  
→ channel price 与 system configuration 受到影响。

因此，PC 承受的是“GPU allocation + memory residual”双重压力。

## 3. 第二层传导：general server

General server 不一定使用 HBM，但大量使用 DDR5 RDIMM。

TrendForce 预计 2026 年 HBM + RDIMM 已占 DRAM bits 约 **51%**。

这意味着 general server memory 也已经进入 AI/server-driven memory pool，而不是完全独立的 commodity market。

因此，AI infrastructure expansion 可以通过 memory allocation 间接影响传统服务器成本。

## 4. 第三层传导：smartphone

Smartphone 与 frontier AI 的重叠主要在：

- leading-edge logic；
- LPDDR；
- selected packaging；
- power-management components。

TSMC 2025 smartphone platform 仍占 revenue **29%**，同比增长。

所以 AI 并没有“挤掉 smartphone”。

更准确的变化是：

- HPC 增量增长更快；
- leading-edge investment 更偏向 HPC；
- 部分 memory/resource allocation 更容易向高价值 AI/server demand 倾斜。

这可能提高 flagship device 的 input cost，或推动中端产品更长时间停留在成熟 node。

## 5. Automotive 的冲击更慢

Automotive chip 具有：

- 长认证周期；
- 高可靠性要求；
- 大量 mature-node usage。

因此，汽车不会与 frontier AI 在所有环节直接竞争。

其主要暴露点是：

- central compute；
- memory；
- power management；
- selected advanced packaging。

所以 automotive 更适合描述为**第二阶段选择性挤压**，而不是第一波全面 shortage。

## 6. Manufacturing inflation 的真正来源

当一个行业面对 residual-capacity pressure 时，企业通常有四种应对：

1. 涨价；
2. 降规格；
3. 延后升级；
4. 转向较老 node / alternative supplier。

因此，AI infrastructure 对实体经济的影响未必首先表现为“停产”。

更常见的是：

- flagship BOM 上升；
- replacement cycle 延长；
- high-end feature 下放变慢；
- product segmentation 加剧。

这是一种结构性“升级税”。

## 7. China parallel supply 的作用

中国本地 logic、DRAM、NAND 与整机供给能力增强，可以缓解部分 domestic consumer market 的 residual pressure。

但这种替代必须分层：

- smartphone / consumer computing：替代能力更强；
- workstation/general compute：部分替代；
- frontier AI：仍取决于 advanced logic、HBM、packaging、interconnect 与 software 是否同时闭环。

因此，中国 supply expansion 可以改变国内终端成本结构，却不能直接抵消全球 frontier AI bottleneck。

## 8. 数字化转型的第二重成本

制造企业采用 AI 时，还会面对另一个与芯片价格不同的成本：

- cloud inference；
- software integration；
- data pipeline；
- security/compliance；
- workflow redesign。

因此，实体企业可能同时受到：

1. upstream hardware inflation；
2. downstream AI software/service cost。

这使“AI 提高生产率”的 ROI 不能只看模型能力。

真正需要计算的是：

[
Productivity gain - Total AI adoption cost
]

## 9. 当前判断

AI infrastructure expansion 已经能够通过 memory、advanced packaging 和 leading-edge allocation 影响部分非 AI 市场。

但当前证据更支持：

> **选择性传导、产品分层和 residual-capacity pressure**

而不是：

> **全球消费电子、汽车和传统服务器被 AI 全面挤出。**

未来需要持续观察：

- DDR5/LPDDR price；
- consumer GPU availability；
- smartphone node mix；
- general-server shipment；
- automotive advanced-compute BOM；
- memory vendor product mix。

只有这些指标同步恶化，才能证明 AI infrastructure pressure 已经从少数稀缺层扩散为更广泛的制造业成本冲击。
