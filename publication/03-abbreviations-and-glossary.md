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
| IC | Integrated Circuit | 通用元件层；process node、packaging 与 system integration 是彼此独立的变量 |
| HBM | High Bandwidth Memory | 与 DDR/RDIMM 的 bit share、wafer input 分开 |
| DRAM | Dynamic Random-Access Memory | HBM、DDR、LPDDR、RDIMM 需按产品层区分 |
| DDR5 | Double Data Rate 5 SDRAM | conventional DRAM 的一种 |
| RDIMM | Registered DIMM | server memory；不等于 HBM |
| LPDDR | Low-Power DDR | 主要用于 mobile / client / selected rack CPU memory |
| GDDR | Graphics Double Data Rate memory | 常用于 gaming GPU / game console；不与 HBM 视为同一产品池 |
| NAND | NAND Flash | 与 DRAM/HBM 属不同 memory technology |
| eSSD | Enterprise SSD | 企业级固态存储 |
| NVMe | Non-Volatile Memory Express | 高速 SSD interface / protocol；产品规格不等于行业供给 |
| UFS | Universal Flash Storage | mobile / embedded / selected game-console storage；与 data-center SSD 分开分析 |
| HDD | Hard Disk Drive | 传统存储；与 NAND / eSSD 不属于同一供给池 |
| CoWoS | Chip-on-Wafer-on-Substrate | TSMC advanced-packaging family；customer allocation 不由 revenue share推导 |
| TSV | Through-Silicon Via | HBM stacking / 3D integration 的关键工艺之一 |
| HVM | High-Volume Manufacturing | qualification 到 volume 的转段；qualification 状态不等于 HVM |
| CUDA | NVIDIA compute platform / programming ecosystem | 作为 software switching-cost 变量分析 |
| NVLink / NVSwitch | NVIDIA scale-up interconnect technologies | 不与 scale-out network 混为同一层 |
| API | Application Programming Interface | 软件集成面；agent-native 工作流的可变成本组成部分之一 |
| CapEx | Capital Expenditure | guidance、expectation、actual 必须分开 |
| OpEx | Operating Expenditure | 不与 CapEx 直接合并 |
| FCF | Free Cash Flow | 保留公司定义与 GAAP/non-GAAP 身份 |
| PPA | Power Purchase Agreement | contracted capacity 不等于 energized/utilized load |
| PUE | Power Usage Effectiveness | data-center efficiency metric |
| LPS | Land, Power and Shell | data-center site 的土地、电力接入与建筑壳体组合；secured LPS 不等于 energized / utilized compute |
| IT-GW | Gigawatts of IT load / IT capacity | 表示 IT equipment / AI factory 的设计负载容量；不能与 generation GW、PPA GW 或 grid-delivered GW 直接视为同一物理量 |
| CSP | Cloud Service Provider | hyperscaler 为其中重要类别 |
| OEM | Original Equipment Manufacturer | 终端/整机厂商 |
| ODM | Original Design Manufacturer | 设计制造服务商 |
| PC | Personal Computer | 传统客户端终端；一个与 NARC 相关的需求池 |
| BOM | Bill of Materials | 用于分析终端成本传导 |
| TCO | Total Cost of Ownership | system-level 比较单位 |
| ASP | Average Selling Price | 必须明确产品与时间口径 |
| SKU | Stock-Keeping Unit | 产品配置单位；SKU 数量不等于出货量或供给量 |
| ROI | Return on Investment | 仅作本报告用法；除非指明来源，否则不是公司披露口径 |
| GAAP | 美国公认会计准则 | GAAP 与 non-GAAP 口径不得混用 |
| PPE | Property, Plant and Equipment | 用于 hyperscaler capital-base 重构；各公司会计科目不同 |
| TTM | Trailing Twelve Months | 必须写明时间窗；不能与 calendar guidance 直接比较 |
| TAM | Total Addressable Market | 仅机构 / sell-side 估计；不是公司披露实绩 |
| EOL | End of Life | 长生命周期终端的部件连续性风险 |
| MCU | Microcontroller Unit | 汽车 / 工业层；不是 frontier-AI accelerator |
| APU | Accelerated Processing Unit | 主机 / 客户端 SoC 语境；不是 HBM 级 AI 系统 |
| RF | Radio Frequency | 航空航天 / 国防 special-process exposure |
| ADAS | Advanced Driver Assistance Systems | 汽车 compute 语境 |
| FLOPS | Floating-Point Operations per Second | 仅 peak compute；不是 workload denominator（见[第 8 章](part-I-ch08-quantitative-framework.md)） |
| KV cache | Key-Value cache | Inference memory state；是 inference 可能持续受 memory bound 的原因之一 |
| EUV / DUV | Extreme / Deep Ultraviolet lithography | 制程设备层；与 export control 相关 |

## 标准单位

- 数据容量：KB / MB / GB / TB / PB / EB
- bit 与速率：Kb / Mb / Gb / Tb；Mb/s / Gb/s / Tb/s
- 功率：W / kW / MW / GW
- 能源：Wh / kWh / MWh / TWh
- 频率：Hz / kHz / MHz / GHz
- 制程 / 尺寸：nm / μm / mm / mm²
- 美元金额：优先保留来源原始口径，如 US$96.221B、US$279B

## 本报告核心分析概念

### Resource reallocation pressure
当 AI/HPC 需求具备更高支付能力、更长期订单和更强资本回报预期时，稀缺资本与物理资源可能向 AI/HPC 重新配置。它只是机制 shorthand，不是独立经验定律。

### Scarce-layer Value Capture
企业在供给弹性低、难替代的产业层通过 scarcity、switching cost 与 supply coordination 获取价值的机制。不是法律意义上的 monopoly finding。

### Non-AI Residual Capacity（NARC）
完成 AI / anchor demand 与其他优先需求分配后，非 AI 市场真正可获得的有效残余供给。

### Quantity Assurance
买方在给定质量、认证、代际与交付窗口内，能否按计划获得足够数量的有效供给。它与 Price Pressure 分开：**愿意付更高价格，不等于一定能拿到计划数量。**

### Upgrade Tax
不是税务概念，而是终端层的分析术语：当上游资源机会成本上升时，消费者或整机厂可能出现**同价位规格提升变慢，或同一目标规格需要更高 BOM / 更弱补贴**的结果。不得把它理解为所有终端统一涨价。

### Two-speed semiconductor economics
用于描述 AI Infrastructure Economy 与 Traditional Device Economy 共享部分上游资源、但在价格承受能力、合同期限、BOM 约束与资本形成能力上存在差异，从而形成不同资源配置节奏。

### AI Capacity Gap / AI Capacity Growth Gap
**AI Capacity Gap** 是同一 physical layer、同一交付窗口下 `AI effective demand − AI effective capacity` 的绝对物理缺口；**AI Capacity Growth Gap** 是需求增长率与有效产能增长率之差，只描述缺口扩大/收敛方向。二者不得互换。不同 physical layer 必须分别计算，不能合并成一个综合“资源占有率”。

### Incremental Scarce-Capacity Access
用于判断不同 buyer 能否在 advanced logic、HBM/DRAM、advanced packaging、networking、LPS 与 energized power 等**各自物理层**持续获得足量、qualified、按时交付供给的框架。

观察变量包括 qualified suppliers、lead time、allocation fulfillment、long-term agreements / prepayments、delivery schedule、buyer credit quality 与 supply elasticity。不同 physical pool 不压缩成一个跨层“综合占有率”。

### Cloud system-stack substitution
用于检验 hyperscaler 能否通过 custom accelerator、interconnect、compiler/runtime、rack/pod 与 captive workload 形成 production-grade alternative system stack 的 economic substitution test。

### Anchor-buyer mechanism
大型 model company 的长期 compute commitment 影响 data center、power、chip、memory 与 project financing buildout 的需求形成机制；它不是独立“总理论”。

### Rolling Bottleneck Cascade
瓶颈在 logic、HBM、advanced packaging、networking、power、utilization 等层之间轮换的动态过程。

### AI inheritance
AI 在既有 software、database、cloud、API、digital document、source code、identity/access 与 workflow 等数字资产之上叠加 intelligence / automation layer 的机制 shorthand。它意味着高度信息化组织通常具有更低的 Digital → AI 边际改造摩擦，但**不表示部署障碍为 0**；data quality、integration、security、governance、responsibility、reliability、human review 与 unit economics 仍然决定 production adoption。

### AI Software Unit Economics
以 successfully completed workflow 为核心单位，计算 inference、retrieval/storage、tools/API、retry、human review 等真实变动成本。

### Financing Reflexivity
当 system seller 同时通过 equity investment、credit enhancement、LPS support 或 compute-financing coordination 加速 customer 与 infrastructure buildout 时形成的反馈机制。它不证明需求“虚假”，但会改变 demand independence、risk transfer 与 refinancing dependency 的判断。

### Production-Grade Parallel Stack
替代系统在真实 production workload 中已经形成可持续闭环，至少需要同时观察 accelerator / compute、memory subsystem、advanced packaging、interconnect、compiler/runtime、production workload，以及 utilization / reliability / economics。它不要求所有上游投入都已完全自主。

### Autonomous Frontier Closure
在关键外部输入受限时，系统仍能跨代扩张、升级与迭代的更高一级 closure。除 production-grade stack 外，还要求 advanced-manufacturing continuity、equipment / materials / software / service continuity，以及 HBM、packaging、power、LPS 与 capital formation 的跨代持续性。

### Time-to-Power
从 site / project 获得真实可交付电力条件所需的时间。必须与公布的 generation capacity、PPA capacity、secured LPS 和 future IT-GW design capacity 区分。

### Verified Workflow Output
已经通过质量、责任或业务验收条件，可以被重复交付、计费或纳入真实生产流程的 AI-assisted workflow outcome。它是本报告连接 compute cost、enterprise adoption、cash flow 与 capital recovery 的需求侧闭环单位。

### Task-to-Job Translation
Model Capability → Task Suitability → Workflow Redesign → Adoption Economics / Responsibility → Job Composition → Employment / Wage Outcome。用于避免把模型能力、职业暴露率或单个 task 自动化直接写成岗位消失率。

## 情景术语

- **S1 — Competitive Expansion：** 供给弹性、multi-sourcing 与 portability 提高，value capture 更分散。
- **S2 — Baseline Concentration：** 少数 system platform / scarce-layer supplier 保持强经济性，同时真实替代路径继续发展。
- **S3 — Resource Hegemony：** multi-layer scarcity、quantity assurance / delivery access 集中、switching cost 与 financing coordination 同时强化，且 workload monetization 足以支撑相关 long-duration commitments，后来者复制完整 infrastructure stack 的门槛显著提高。
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
