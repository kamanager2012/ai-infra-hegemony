# 第一篇：生产资料化与宏观计量框架

> **出版定位：**本篇是研究层的宏观入口，负责定义“算力何时从工具变成生产性基础设施”的可检验条件，以及跨章节统一计量单位。最终出版总判见 [Part IV · 第32章](publication/part-IV-ch32-master-judgment.md)。节点报价、远期 CoWoS 月产能、2030/2036 GW 单点等缺乏一手支撑的参数不进入事实层。

## 1. 核心问题：算力何时具有“生产资料”属性

这里的“生产资料化”不是把模型拟人化，也不是假设 AI 具备不受约束的主体性。它描述一个经济条件：

> **一套 AI system 能否在给定 compute、power 和 capital cost 下，持续完成可验证、可验收、可重复的工作流，并产生足以覆盖其长期成本的经济价值。**

如果只能辅助人类完成局部任务，compute 更接近工具；如果能够大规模连续完成过去需要人工逐步执行的工作，并且结果可被业务系统验收，compute、memory、interconnect、data center 与 power 就开始表现为生产性基础设施。

因此，真正的计量单位不是“模型有多聪明”，而是：

> **cost per verified workflow outcome + capital required to sustain it**

## 2. 当前已经可以确认的五个结构变化

### 2.1 销售单位上移到 System Stack

NVIDIA 的商业产品已经从 accelerator card 上移到 rack-scale system；Google、AWS、Microsoft、Meta 也已把 custom silicon 扩展到 compiler/runtime、interconnect、rack/pod 与 production workload。竞争单位因此从 chip 上移到 **system stack**。

### 2.2 HBM 的制造投入高于 Conventional DRAM

Micron 一手披露：在 same technology node / same number of bits 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。这说明 bandwidth expansion 会改变 DRAM manufacturing input 和 residual capacity，而不是只改变 memory price。

### 2.3 Advanced Packaging 已成为可验证交付约束

TSMC 已在一手逐字稿中多次描述 advanced-packaging capacity tight，2026 Q2 更明确表示 packaging tightness 已经限制客户增长。它说明 logic wafer available 并不自动等于完整 system deliverable。

### 2.4 Power 已进入系统交付链

约 120 kW-class rack 与多个数百 MW / GW 级长期电力项目说明，grid connection、substation、firm generation、permit 与 Time-to-Power 已成为 AI infrastructure 的独立物理变量。

### 2.5 资本与长期承诺正在提前锁定未来资源

NVIDIA manufacturing, supply, and capacity commitments 已由 2026-01-25 的 **US$95.2B** 上升到 2026-07-26 的 **US$279B**；hyperscaler 与 model company 也通过长期 data-center / power / compute commitments 提前塑造未来供给。公开文件并未把这些承诺拆成单一供应商份额，因此只能作为整体 forward commitment 与资源预订强度的锚。

## 3. 宏观分析必须同时看五个计量轴

### 3.1 Verified Workflow Economics

AI 是否真正成为生产性资产，最终取决于每个 workflow 的可验证业务价值、完成成本、人工复核成本与长期使用量。

### 3.2 System Substitution

需要观察 workload 是否能够在 NVIDIA、TPU、Trainium、Maia、MTIA 或其他 system stack 之间以可接受成本迁移。单卡 benchmark 不能替代 production migration data。

### 3.3 Scarce Physical Inputs

advanced logic、HBM、advanced packaging 与 power 是不同物理池。一个约束缓解，并不意味着其他约束同步消失。

### 3.4 Capital Duration

compute hardware、network、data-center shell、grid 与长期 PPA 的 useful life / contract duration 不同。买方 ROI 必须覆盖这种 duration mismatch。

### 3.5 Utilization and Forward Commitments

高 CapEx 只有在资产获得足够 utilization 与 workflow revenue 时才形成高质量回报。未来判断必须同时看实际利用率、seller commitments、Anchor Buyer contracts 和 market-clearing price。

## 4. 从 Workflow 到 Scarce-Layer Value Capture 的传导

当 AI workflow 能持续产生可验收结果时，需求会沿产业链向下传导：

> workflow demand → compute/system demand → HBM / packaging / power demand → forward commitments → scarce-resource allocation

如果某个平台同时拥有高 cash flow、强 switching cost、明确 roadmap 和长期订单，它更有能力提前锁定下一代 scarce input，从而提高交付确定性。

这形成 **Scarce-layer Value Capture**：价值并不只留在拥有最高市场份额的主体，而更容易流向那些控制稀缺、迁移困难或能够协调多层供给的节点。

与此同时，AI/server demand 吸收增量资源后，传统市场真正可获得的供给需要用 **Non-AI Residual Capacity** 衡量，而不能只看行业总产能。

## 5. 算法效率既可能降低资本需求，也可能扩大总使用量

DeepSeek 等案例说明，architecture / algorithmic efficiency 可以显著降低特定训练或 serving workload 的 compute / memory requirement。

但效率提升不会自动意味着总基础设施需求下降。研究层与出版层统一使用：

```text
Infrastructure_Demand_t
= Unit_Resource_Intensity_t
× Workload_Volume_t
```

相对基准期：

```text
Infrastructure_Demand_t / Infrastructure_Demand_0
=
(Unit_Resource_Intensity_t / Unit_Resource_Intensity_0)
×
(Workload_Volume_t / Workload_Volume_0)
```

如果要把有效价格变化映射到 workload volume，可另外使用明确标注的弹性假设：

```text
Workload_Volume_t / Workload_Volume_0
=
(Effective_Price_t / Effective_Price_0)^(-ε)
```

其中 ε 必须对应同一可比、可验收工作结果的需求价格弹性。这样，“效率提升”与“需求扩张”就不会被压缩成一个不可计算的口号。

真正需要观察的是 unit resource intensity、有效 workload 总量、effective price 与 capital utilization，而不是单次训练成本或 API 单价本身。

## 6. 两套或多套系统生态会提高重复建设，也会提高选择权

出口管制、供应韧性和产业自主会推动区域化 system stack。双轨或多轨并不必然减少全球总基础设施；它可能导致：

- duplicated software/runtime；
- duplicated manufacturing capacity；
- duplicated power/data-center reservation；
- lower single-stack efficiency；
- higher resilience and strategic optionality。

因此，地缘分化对资本总量的影响可能是“更多重复建设”，而不是简单的全球需求下降。

## 7. 远期数字必须保持 H / D 身份

本书不把 2030/2036 的 node price、CoWoS monthly capacity、HBM future trade ratio、GW-scale campus 或 trillion-dollar CapEx 写成已确认路径。

统一规则是：

- 历史事实没有一手或高质量公开来源，不进入 F；
- 公司 guidance 必须保留 guidance 身份；
- 机构预测必须保留机构与时间窗口；
- 2030/2036 单点只可作为 H / D 级 scenario input；
- 同一数字被多个章节重复引用，不会自动提高证据等级。

因此，宏观判断依赖机制和可观察变量，而不是依赖一个精确的远期价格表。

## 8. 当前更支持哪一种状态

截至 2026 年 8 月，事实组合更接近 **S2 — Baseline Concentration**：

- leading system platform economics 很强；
- cloud custom stacks 已形成真实第二路线；
- HBM / advanced packaging / power 仍存在明显物理约束；
- China parallel stack 持续扩展，但 frontier closure 仍需多个 advanced layer 同时验证；
- CapEx 和 forward commitments 仍处高位，但 buyer-side ROI 压力上升。

这不是对 2036 的固定预测。若供给弹性、interoperability 和替代系统成熟度快速提高，权重会向 S1 移动；若多个 scarce layer 和 switching cost 同时加强，则向 S3 移动；若 utilization、clearing price、CapEx 与 forward commitments 同步转弱，则向 S4 移动。

## 9. 什么会证伪“生产资料化继续强化”

以下信号若持续出现，应下调当前宏观判断：

- productive AI workload 无法覆盖新增资本基数；
- major system/platform commitments 连续下降；
- advanced packaging / HBM 供给长期显著宽松；
- cloud custom systems 大规模降低 switching cost 和外部平台依赖；
- energized power 增长明显快于 compute demand，Time-to-Power 失去稀缺性；
- second-hand compute / lease price 持续快速下跌；
- application/workflow monetization 长期弱于 inference 与基础设施成本。

宏观研究的目标不是让所有长期判断都“永远成立”，而是明确指出什么证据出现时必须改变判断。

## 10. 当前宏观结论

AI infrastructure 的核心变化可以压缩为一句：

> **当可验证 workflow 把 compute 转化为持续经济产出时，system stack、HBM、advanced packaging、power 与 capital duration 就不再只是技术参数，而成为决定产业价值捕获和竞争结构的生产性基础设施变量。**

这仍是条件命题。最终决定资本回报的不是 hardware 数量，而是这些基础设施能否持续服务可迁移、可验收、能产生现金流的真实 workload。

## 关键公开来源

- NVIDIA FY27 Q2 official results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- NVIDIA FY27 Q2 10-Q — US$279B manufacturing, supply, and capacity commitments: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
- Micron FY24 Q2 Prepared Remarks — HBM3E ≈3× DDR5 wafer supply: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- TrendForce — 2026E HBM + RDIMM = 51% of DRAM bit supply: https://www.trendforce.com/presscenter/news/20260825-13198.html
- TSMC 2Q26 Earnings Conference Transcript — packaging tightness limits customer growth: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
- NVIDIA DGX GB200 hardware guide — ~120 kW/rack: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html