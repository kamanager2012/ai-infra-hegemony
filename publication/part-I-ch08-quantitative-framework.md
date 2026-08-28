# Part I · 第8章：AI 基础设施量化框架与 Rolling Bottleneck Cascade


## 1. 量化的目标不是制造一个伪精确总模型

AI infrastructure 最容易出现的分析错误，是把不同物理池、不同会计科目和不同证据等级的数字串成一个看似完整的总量模型。

本书只允许四类量化进入主链：

1. **Compute / memory intensity**；
2. **Rack-scale material demand**；
3. **Packaging / power 的明确压力测试**；
4. **Capacity / commitment / utilization indicators**。

任何无法由公开数据闭合的环节，都必须保留成参数，而不是用一个“看起来合理”的点值补齐。

## 2. Roofline：为什么 frontier inference 不能只比较 FLOPS

Roofline model 的核心关系是：

> **Performance = min(Peak Compute, Memory Bandwidth × Arithmetic Intensity)**

临界算术强度为：

> **I_critical = Peak Compute / Memory Bandwidth**

当 workload 的 arithmetic intensity 低于临界值，系统进入 memory-bound 区域。自回归推理需要持续读取 model state、KV cache 和 routing / activation 数据，因此即使 accelerator 的 peak FLOPS 很高，真实 token throughput 仍可能受 HBM bandwidth 与 memory movement 限制。

这就是为什么本书把 HBM、interconnect 与 compute 放在同一系统单位里，而不是只用峰值算力解释 frontier inference。

## 3. Algorithmic architecture 会改变需求函数，但不会删除物理约束

DeepSeek-V3 Technical Report 的一手锚包括：671B total parameters、37B activated parameters、14.8T pre-training tokens、**2.664M H800 GPU-hours pre-training** 与 **2.788M H800 GPU-hours full formal training**。

DeepSeek-V2 的独立结果则包括：相对 DeepSeek 67B，约 **93.3% KV-cache reduction** 与约 **5.76× maximum generation throughput**。

这两组数字属于不同模型版本，不能混写。

它们的共同方法意义是：architecture 可以改变 bytes/token、activated compute、communication pattern 与 serving concurrency，因此会直接改变对 HBM、network 和 compute 的需求函数。

但需求函数变化不等于物理约束消失。更高效率是否减少总基础设施需求，仍取决于 workload volume 与 demand elasticity。

## 4. Formal-training compute conversion 不是完整研发成本

DeepSeek-V3 full formal training 为 **2.788M H800 GPU-hours**。按论文使用的 **US$2/GPU-hour** 假设做租金换算：

> **2.788M × US$2 ≈ US$5.576M**

这一数字只代表该次 formal-training compute conversion，不包括 research iteration、failed runs、data engineering、engineering payroll、cluster depreciation、networking、storage 与 post-training ecosystem。

因此本书允许把 US$5.576M 用作**公开训练运行量级**，不允许把它写成“一个 frontier model 的完整企业成本”。

## 5. Rack-scale BOM 可以量化，但 rack shipment 不能凭空补齐

GB200 NVL72 官方配置为：72 Blackwell GPU、36 Grace CPU、13.4 TB HBM3E、17 TB LPDDR5X。

如果情景 rack 数为 R，则：

> **HBM(R) = 13.4 TB × R**

> **LPDDR(R) = 17 TB × R**

| 情景 rack 数 | HBM3E | LPDDR5X |
|---:|---:|---:|
| 1,000 | 13.4 PB | 17 PB |
| 10,000 | 134 PB | 170 PB |
| 30,000 | 402 PB | 510 PB |
| 50,000 | 670 PB | 850 PB |

这是 **D 级 scenario arithmetic**。NVIDIA 没有公开可用于这一乘算的全年 NVL72 rack shipment，因此不能先用 Data Center revenue 除一个自拟 ASP，再把假设 rack 数继续传播成 HBM、CoWoS 和 power 的“实际值”。

## 6. HBM trade ratio 会放大 bit-demand 对 wafer input 的压力

Micron FY24 Q2 prepared remarks 给出重要一手边界：在 **industrywide / same technology node / same number of bits** 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。

因此，bit demand 与 manufacturing input 不是一一对应。HBM bit share 上升时，对 DRAM wafer / cleanroom input 的压力可能高于 bit share 本身。

该 3× 不是 Micron 单厂固定 MES 常数，也不能机械外推成 HBM4/HBM5 的永久倍率。

## 7. Packaging geometry 只能承担 sensitivity，不承担 shipment

报告使用约 **5.37 CoWoS wafers/rack** 作为 D 级 geometry stress test：

> **72 packages ÷ 13.4 packages/wafer ≈ 5.37 wafers/rack**

其中 13.4 packages/wafer 是报告侧 geometry assumption，不是 TSMC 官方 yield 或 packages-per-wafer 指标。

所以 5.37 只可用于：

- packaging demand order-of-magnitude；
- scenario comparison；
- bottleneck sensitivity。

不能用于除 TSMC annual front-end wafer shipments、反推实际 Blackwell shipment 或推导 customer allocation。

## 8. Power 也必须按状态与物理边界计算

约 **120 kW/rack** 可以作为 rack-level power-density input。500 racks × 120 kW = **60 MW rack-level full-load power**。

但这一算术不包括完整 facility overhead，也不代表某个园区已经部署 500 柜。

更重要的是，电力要区分：Announced、Contracted、Permitted、Energized、Utilized。contracted MW 不等于 energized MW，energized MW 也不等于高利用率 AI load。

因此，power quantity 与 hardware quantity 一样，必须保留状态身份。

## 9. 当 shipment 无法闭合时，Forward Commitment 比自拟出货更有价值

NVIDIA manufacturing, supply, and capacity commitments 的公开轨迹为：

- 2026-01-25：**US$95.2B**；
- 2026-04-26：**US$119B**；
- 2026-07-26：**US$279B**。

FY27 Q2 10-Q 说明，最新承诺主要关联 data-center infrastructure systems 所需的 memory 与 manufacturing facilities。

它不能告诉我们某一家 supplier 得到多少，但可以作为 future resource reservation intensity 的可观察 proxy。

在缺乏 customer-level HBM bits、CoWoS allocation 和 rack shipment 时，这类前向 commitment 比“收入÷自拟柜价”的伪精确模型更有价值。

## 10. AHICR：每个 scarce layer 分开测增量捕获

本书使用 **Advanced/HPC Incremental Capacity Capture Ratio（AHICR）**：

> **AHICR(layer) = 某买方获得的新增先进 AI/HPC resource ÷ 该 physical layer 全行业新增 resource**

AHICR 必须分别观察：

- advanced logic；
- HBM；
- advanced packaging；
- power。

这些单位不能相加成一个万能“资源占有率”。AHICR 的价值在于观察下一代增量资源是否持续向少数买方倾斜，而不是把历史 revenue share 当成未来 allocation。

## 11. 五类风险必须分开，再看是否形成级联

AI infrastructure 的系统风险可以分成：

1. **Physical bottleneck**：logic / HBM / packaging / interconnect；
2. **Power bottleneck**：grid / substation / permit / cooling；
3. **Capital / utilization risk**：资产利用率不足以覆盖 depreciation、power、operations 与 financing；
4. **System substitution risk**：cloud custom stacks / open software 改变 platform economics；
5. **Regulatory / geopolitical risk**：export control、supply interruption、interface remedy、regional fragmentation。

单一风险并不等于全行业 crisis。真正危险的是多个时钟开始串联。

## 12. Rolling Bottleneck Cascade

AI infrastructure 的瓶颈会轮换，而不是永久固定在同一层。

一种正向扩张链是：

> HBM / packaging tight → hardware delivery constrained → supply expands → more racks reach sites → power / interconnection becomes binding → utilization becomes next constraint

一种反向资本链则可能是：

> power delay → utilization decline → buyer ROI decline → next CapEx slows → hardware orders slow → HBM / packaging tightness eases → upstream CapEx slows

这就是 **Rolling Bottleneck Cascade**。

它解释了为什么“HBM 已经缓解”并不能证明 AI infrastructure 已经没有约束，也解释了为什么“power 成为约束”并不等于 semiconductor bottleneck 永久消失。

## 13. Capital return 需要把所有现金时钟放进同一方程

最基本的经济式可以写成：

> **Economic Return = Revenue from deployed compute − Depreciation − Power − Operations − Financing**

这里最危险的是 duration mismatch：hardware 快速迭代，而 data-center shell、grid、PPA 与 debt 可能持续更久。

所以一个系统即使技术上可运行，也可能因为低 utilization 或长期 obligations 形成差的资本回报。

## 14. Quantitative Guardrails

全书必须遵守以下硬边界：

- revenue share ≠ wafer share；
- platform revenue share ≠ physical shipment share；
- contracted MW ≠ energized MW；
- energized MW ≠ utilized AI load；
- rack spec × hypothetical racks ≠ shipment；
- CoWoS geometry ≠ fab yield；
- CapEx guidance ≠ actual CapEx；
- AI exposure ≠ job loss；
- model rental conversion ≠ full company cash cost；
- institutional forecast ≠ company actual；
- one physical pool ≠ another physical pool。

## 15. 最可靠的量化顺序

出版层采用以下顺序：

> **official system spec → material identity → scenario demand → supply constraint → forward commitment → utilization → falsification**

而不是先设定一个宏大终局，再反向搜索数字把公式填满。

这套纪律的价值不是让所有未来判断变保守，而是允许情景大胆，同时保证事实层和物理量纲始终可审计。

## 关键公开来源

- DeepSeek-V3 Technical Report: https://arxiv.org/abs/2412.19437
- DeepSeek-V2: https://github.com/deepseek-ai/DeepSeek-V2
- NVIDIA GB200 NVL72 product page: https://www.nvidia.com/en-us/data-center/gb200-nvl72/
- NVIDIA DGX GB200 hardware guide — ~120 kW/rack: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
- Micron FY24 Q2 Prepared Remarks — HBM3E ≈3× DDR5 wafer supply: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- NVIDIA FY27 Q2 10-Q — US$279B commitments: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm