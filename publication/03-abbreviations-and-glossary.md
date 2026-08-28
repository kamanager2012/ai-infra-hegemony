# 缩写与核心术语表

## 行业缩写

| 缩写 / 术语 | 含义 | 本报告使用边界 |
|---|---|---|
| AI | Artificial Intelligence | 仅在上下文明确时指生成式 AI / frontier AI |
| HPC | High-Performance Computing | 包含 AI/HPC，不与 AI 一一等同 |
| GPU | Graphics Processing Unit | 含 data-center / consumer 等不同产品层 |
| CPU | Central Processing Unit | 不与 accelerator 混用 |
| ASIC | Application-Specific Integrated Circuit | cloud custom accelerator 属于其典型形式之一 |
| SoC | System on Chip | 常用于 smartphone / edge / embedded |
| HBM | High Bandwidth Memory | 与 DDR/RDIMM 的 bit share、wafer input 分开 |
| DRAM | Dynamic Random-Access Memory | HBM、DDR、LPDDR、RDIMM 需按产品层区分 |
| DDR5 | Double Data Rate 5 SDRAM | conventional DRAM 的一种 |
| RDIMM | Registered DIMM | server memory；不等于 HBM |
| LPDDR | Low-Power DDR | 主要用于 mobile / client / selected rack CPU memory |
| NAND | NAND Flash | 与 DRAM/HBM 属不同 memory technology |
| eSSD | Enterprise SSD | 企业级固态存储 |
| CoWoS | Chip-on-Wafer-on-Substrate | TSMC advanced-packaging family；customer allocation 不由 revenue share推导 |
| TSV | Through-Silicon Via | HBM stacking / 3D integration 的关键工艺之一 |
| CUDA | NVIDIA compute platform / programming ecosystem | 作为 software switching-cost 变量分析 |
| NVLink / NVSwitch | NVIDIA scale-up interconnect technologies | 不与 scale-out network 混为同一层 |
| CapEx | Capital Expenditure | guidance、expectation、actual 必须分开 |
| OpEx | Operating Expenditure | 不与 CapEx 直接合并 |
| FCF | Free Cash Flow | 保留公司定义与 GAAP/non-GAAP 身份 |
| PPA | Power Purchase Agreement | contracted capacity 不等于 energized/utilized load |
| PUE | Power Usage Effectiveness | data-center efficiency metric |
| CSP | Cloud Service Provider | hyperscaler 为其中重要类别 |
| OEM | Original Equipment Manufacturer | 终端/整机厂商 |
| ODM | Original Design Manufacturer | 设计制造服务商 |
| BOM | Bill of Materials | 用于分析终端成本传导 |
| TCO | Total Cost of Ownership | system-level 比较单位 |
| ASP | Average Selling Price | 必须明确产品与时间口径 |

## 标准单位

- 数据容量：KB / MB / GB / TB / PB / EB
- bit 与速率：Kb / Mb / Gb / Tb；Mb/s / Gb/s / Tb/s
- 功率：W / kW / MW / GW
- 能源：Wh / kWh / MWh / TWh
- 频率：Hz / kHz / MHz / GHz
- 制程 / 尺寸：nm / μm / mm / mm²
- 美元金额：优先保留来源原始口径，如 US$96.221B、US$279B

## 本报告核心分析概念

### AI Resource Gravity
当 AI/HPC 需求具备更高支付能力、更长期订单和更强资本回报预期时，稀缺资本与物理资源向 AI/HPC 配置的机制。

### Scarce-layer Value Capture
企业在供给弹性低、难替代的产业层通过 scarcity、switching cost 与 supply coordination 获取价值的机制。不是法律意义上的 monopoly finding。

### Non-AI Residual Capacity（NARC）
完成 AI / anchor demand 与其他优先需求分配后，非 AI 市场真正可获得的有效残余供给。

### Two-Speed Semiconductor Economy
AI Infrastructure Economy 与 Traditional Device Economy 共享部分上游资源，但价格承受能力、合同期限、BOM 约束与资本形成能力不同，导致新增资源配置速度分化。

### AI Capacity Gap / AI Capacity Growth Gap
**AI Capacity Gap** 是同一 physical layer、同一交付窗口下 `AI effective demand − AI effective capacity` 的绝对物理缺口；**AI Capacity Growth Gap** 是需求增长率与有效产能增长率之差，只描述缺口扩大/收敛方向。二者不得互换。不同 physical layer 必须分别计算，不能合并成一个综合“资源占有率”。

### Cloud System-Stack Substitution
hyperscaler 通过 custom accelerator、interconnect、compiler/runtime、rack/pod 与 captive workload 形成第二类生产级 system stack 的替代机制。

### Anchor Compute Buyer Effect
大型 model company 的长期 compute commitment 反向影响 data center、power、chip、memory 与 project financing 的机制。

### Rolling Bottleneck Cascade
瓶颈在 logic、HBM、advanced packaging、networking、power、utilization 等层之间轮换的动态过程。

### AI Software Unit Economics
以 successfully completed workflow 为核心单位，计算 inference、retrieval/storage、tools/API、retry、human review 等真实变动成本。

### Task-to-Job Translation
Task Exposure → Adoption Economics → Workflow Redesign → Responsibility Constraint → Employment / Wage Outcome。避免把技术暴露率直接写成岗位消失率。

## 情景术语

- **S1 — Competitive Expansion：** 供给弹性、multi-sourcing 与 portability 提高，value capture 更分散。
- **S2 — Baseline Concentration：** 少数 system platform / scarce-layer supplier 保持强经济性，同时真实替代路径继续发展。
- **S3 — Resource Hegemony：** 多个 scarce layers 与 switching cost 同时强化，后来者复制完整 infrastructure stack 的门槛显著提高。
- **S4 — Capital Hard Landing：** utilization、clearing price、forward commitments 与 accounting losses 同步恶化，资本进入清算。

## 证据身份

- **F — Fact：** 已发生且可公开核验。
- **H — Hypothesis：** 明确的未来假设。
- **M — Mechanism：** 因果传导机制。
- **S — Scenario：** 条件化未来状态。
- **X — Falsification：** 足以迫使判断改变的反向信号。
- **A：** first-party / formal evidence。
- **B：** institutional research。
- **C：** sell-side / supply-chain / media estimate。
- **D：** 本报告 model / arithmetic / sensitivity / stress test。
