# Part II · 第10章：模型单位经济、算法效率与开源竞争

> **出版层章节。** 以 [vol-06](../vol-06.md) 为主源，并与 Part I Ch08 的量化边界保持一致。本章不使用固定“AI SaaS 毛利率终点”，而把模型与软件竞争放进 **AI Software Unit Economics + demand elasticity** 框架。

## 1. 模型公司不是脱离基础设施的纯软件生意

API、订阅和 agent service 的底层变量成本包括 accelerator time、HBM bandwidth、KV cache、storage / retrieval、networking、third-party tools、human review、cloud margin 与 serving utilization。

因此，AI 软件无法简单沿用“新增用户几乎没有边际成本”的传统 SaaS 叙事。真正的单位是：

> **Revenue per completed workflow − total variable AI cost per completed workflow**

## 2. Algorithmic efficiency 改变的是需求函数

DeepSeek-V3 一手披露：671B total parameters、37B activated parameters、14.8T pre-training tokens、2.664M H800 GPU-hours pre-training、2.788M H800 GPU-hours full formal training。

按论文使用的 US$2/GPU-hour 假设，2.788M GPU-hours 对应约 **US$5.576M formal-training compute conversion**。这不是完整企业研发成本。

它证明的是：frontier capability 与硬件投入之间不是固定线性关系。architecture、sparsity、routing 和 memory design 可以显著改变单位 capability 所需资源。

## 3. MLA 说明 Memory Cost 可以被算法直接攻击

DeepSeek-V2 相对 DeepSeek 67B 报告约 **93.3% KV-cache reduction** 和约 **5.76× maximum generation throughput**。

这两个数字属于 V2，不属于 V3。

其经济意义在于：同一 HBM capacity 可以承载更高并发，单位 token memory traffic 下降，serving utilization 提高。

但更低单位成本不意味着总基础设施需求必然下降。如果 lower cost 刺激 token、agent 与 workflow volume 更快增长，总需求仍可上升。

## 4. 开源首先压缩模型层利润，不会自动压缩全部基础设施利润

Open-source model 会提高 capability diffusion、private deployment 与 model switching option，并压低 API premium。

但模型层迁移速度通常快于底层 accelerator、HBM、network、packaging 和 data-center infrastructure 的迁移速度。

所以可以出现：

> **model price compression + infrastructure utilization growth**

这也是为什么“API price 下跌”和“AI infrastructure demand 下跌”不能画等号。

## 5. GPU vs ASIC 的正确比较单位是 System TCO

Google TPU、AWS Trainium、Microsoft Maia、Meta MTIA 为模型公司和内部 workload 提供第二条 compute path。

真正要比较的不是 accelerator die price，而是：

- workload compatibility；
- compiler/runtime maturity；
- HBM / interconnect configuration；
- cluster scaling；
- debugging / porting cost；
- effective utilization。

如果理论 chip cost 更低，但 migration、debug 或 utilization 更差，system TCO 未必更低。

## 6. AI Software Unit Economics

一个生产级 workflow 至少应计算：

> **Contribution Margin = Revenue per workflow − inference − retrieval/storage − tools/APIs − retries − human review − compliance/operations**

真正值得比较的指标包括：

- cost per successfully completed task；
- gross margin after inference；
- revenue / productivity value per workflow；
- retention；
- retry / failure rate；
- human review burden；
- utilization of reserved compute。

## 7. Anchor Buyer 让模型公司反向影响基础设施

超大模型公司已经开始通过 multi-year compute commitments、dedicated data-center projects 与 long-duration capacity reservation 影响 cloud / chip / power investment。

这意味着模型公司不是永远只能被动接受 cloud price。达到足够规模后，它们本身可以成为基础设施资本形成的需求锚。

但这也放大风险：如果 architecture efficiency 提高、revenue 增长不及预期或 workload 转移，长期 capacity commitment 会变成 utilization / duration risk。

## 8. Price Compression 与 Jevons-style Rebound

算法效率和开源竞争会降低 unit intelligence cost。最终基础设施需求取决于：

> **Net Infrastructure Demand = Unit Resource Intensity × Total Workload Volume**

如果 resource intensity 下降 50%，但 workload volume 增长 4×，总需求仍增长。

所以长期判断必须观察真实 workload、utilization 和 business outcome，而不是只看训练成本、benchmark 或 token price。

## 9. 当前判断

截至 2026 年，更稳健的状态是：

- model layer price competition 与 capability diffusion 已经发生；
- unit cost 持续下降；
- open-source 提高 buyer bargaining power；
- infrastructure demand 尚未因此进入确认下降周期；
- large model companies 正通过长期 commitment 反向塑造 infrastructure buildout。

因此，算法效率既可能成为基础设施需求的**打断器**，也可能成为总使用量的**放大器**。哪一种占主导，只能由 workload volume、utilization 与 unit economics 证明。

## 关键公开来源

- DeepSeek-V3 Technical Report: https://arxiv.org/abs/2412.19437
- DeepSeek-V2: https://github.com/deepseek-ai/DeepSeek-V2