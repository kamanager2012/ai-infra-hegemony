---
title: "AI基础设施霸权时代"
subtitle: "The Age of AI Infrastructure Hegemony"
author: "James (kamanager2012)"
date: "Research and revision cutoff: 2026-08-28"
lang: zh-CN
---


# 报告定位、证据边界与免责声明

## 报告定位

本报告是一份关于 AI infrastructure、semiconductors、memory、advanced packaging、hyperscaler system stacks、power、capital、software economics 与产业结构变化的长期行业研究。

报告区分：

- 已发生且可验证的事实（F — Fact）；
- 明确的未来假设（H — Hypothesis）；
- 因果传导机制（M — Mechanism）；
- 条件化未来状态（S — Scenario）；
- 足以迫使判断改变的反向信号（X — Falsification）。

研究目标不是给出单一的“2036 年预测”，而是建立一套可随公开事实持续更新的产业分析框架。

## 资料与证据边界

研究主要使用：

- 公司年报、10-K / 20-F、季度财报和官方投资者材料；
- 监管、法院和政府文件；
- 正式合同与项目披露；
- 公司产品规格和技术文档；
- 高质量机构研究；
- 在明确标记条件下使用的本报告模型与压力测试。

机构预测、卖方估计和本报告自算结果不会被升级为公司事实。

## 免责声明

本报告仅用于产业研究与信息交流，不构成投资建议、证券研究评级、法律意见、审计意见或任何交易建议。未来判断均为条件化分析，可能因技术、需求、资本、监管、地缘政治和供给变化而调整。

## 版权

原创报告文本按仓库 LICENSE 所列条款发布。任何第三方材料仍受其各自权利人和许可条件约束；正式出版版仅使用已确认可引用、可改绘或已取得相应许可的第三方内容。

---

## 阅读导航

- [正式目录](01-table-of-contents.md)
- [表格目录](02-list-of-tables.md)
- [缩写与核心术语表](03-abbreviations-and-glossary.md)
- [研究透明度、局限性与纠错机制](04-research-transparency.md)
- [竞争集、替代路径与反方证据矩阵](05-competitive-evidence-matrix.md)
- [Executive Summary — 第1章](part-I-ch01-executive-summary.md)
- [研究方法与证据架构 — 第27章](part-IV-ch27-research-method.md)
- [核心证据台账](../核心证据台账.md)
- [核心参考文献索引](../核心参考文献索引.md)


\newpage


# 表格目录

> 表格编号采用“章号.序号”。每张正式表格在正文中均应包含标题、Source 与必要的 Note。

## Part I

- Table 1.1 — AI 基础设施四类标准情景
- Table 2.1 — GB200 NVL72 的 rack-scale 系统结构
- Table 2.2 — NVIDIA 当前 seller-side economics 与前置供应承诺
- Table 4.1 — TSMC 2025 产能、技术与平台收入结构
- Table 5.1 — GB200 NVL72 rack 数量与 HBM3E 情景需求
- Table 6.1 — Incremental packaging capacity capture 的 residual sensitivity
- Table 7.1 — 三类 AI 电力项目的名义规模与交付状态
- Table 8.1 — NVL72 rack 数量与 HBM/LPDDR 情景需求

## Part II

- Table 16.1 — 四类差异化竞争路径
- Table 17.1 — 2026 Q1 全球 foundry revenue share（TrendForce）
- Table 18.1 — 监管变量对 S1–S4 的作用路径

## Part III

- Table 19.1 — 四大云厂 2026 年公开资本投入口径
- Table 22.1 — 主要 Cloud 公司 server / network equipment useful-life disclosure
- Table 23.1 — AI infrastructure 资产类别与主要融资风险
- Table 24.1 — 四大云厂 2026 年资本投入公开口径
- Table 24.2 — 效率下降与需求弹性的 D 级敏感性示例

## Part IV

- Table 27.1 — 本报告证据等级体系
- Table 29.1 — NVIDIA seller economics 与 forward-reservation 基线
- Table 29.2 — Power project state machine
- Table 29.3 — 更新时的默认 evidence grade
- Table 29.4 — 核心变量的观察频率、持续期与情景触发规则
- Table 30.1 — S1–S4 的核心驱动、主要结果与反向信号
- Table 31.1 — 长期战略判断所依赖的核心结构变量
- Table 31.2 — AI 相关资产的主要价值来源与风险


\newpage


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
**AI Capacity Gap** 是同一 physical layer、同一交付窗口下 `AI effective demand − AI effective capacity` 的绝对物理缺口；**AI Capacity Growth Gap** 是需求增长率与有效产能增长率之差，只描述缺口扩大/收敛方向。二者不得互换。

### AHICR
Advanced/HPC Incremental Capacity Capture Ratio。用于分析某买方对某一 physical layer **新增** advanced/HPC capacity 的捕获程度，不等于历史 revenue share。

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


\newpage


# 研究透明度、局限性与纠错机制

## 1. 作者与研究载体

本报告作者署名为 **James (kamanager2012)**。GitHub 仓库既是版本化研究载体，也是证据追踪、纠错、双语同步和出版构建的工作记录。

本文件不把“仓库可追踪”解释成“已经过外部同行评审”。

## 2. 外部评审状态

截至 2026-08-28，仓库**不声称已经完成正式独立同行评审、审计鉴证或机构评级**。

如果未来获得外部专家、学术机构、行业机构或法律/财务专业人士的正式审阅，应在此处记录：

- reviewer / institution（如允许披露）；
- review scope；
- review date；
- 是否独立；
- 重大修改项；
- 尚未解决的异议。

没有记录的外部意见不能被写成“peer reviewed”。

## 3. Funding / Conflict of Interest

当前仓库**不作“无任何利益冲突”这一未经作者明确确认的声明**。

正式公开发布前，作者应补充一项明确声明，至少覆盖：

- 是否接受与 NVIDIA、TSMC、Samsung、SK hynix、Micron、AMD、Intel、Qualcomm、Apple、Google、Amazon、Microsoft、Meta、OpenAI、Anthropic，以及其他直接分析对象相关的资金、顾问费、商业合作或持仓影响；
- 是否存在会实质影响来源选择或结论表达的商业关系；
- 如无，明确写明“未发现需要披露的相关利益冲突”并由作者确认。

在该声明完成前，**Conflict-of-Interest Gate 保持 open**。

## 4. 证据选择原则与潜在偏差

本报告优先级为：

1. 法定申报、监管/政府文件、正式合同；
2. 公司官方 IR / product / technical materials；
3. 高质量机构研究；
4. sell-side / supply-chain / media estimate；
5. 报告自身 D 级模型。

这套顺序降低“二手报道反复引用后变成事实”的风险，但仍存在公开资料偏差：

- 公司更可能披露有利于投资者理解或战略叙事的资料；
- customer-level allocation、yield、contract pricing、utilization 等核心变量经常不公开；
- 中国与美国供应链的公开披露深度不对称；
- 机构研究模型可能包含未公开假设；
- 快速变化行业会产生明显的 publication-lag risk。

因此，“未公开披露”只支持“公开资料无法确认”，不自动证明“不存在”。

## 5. 研究局限

本报告不具备以下能力：

- 对未公开合同、内部采购、真实 customer allocation 进行审计；
- 从 revenue share 反推出 wafer / HBM / CoWoS physical share；
- 从 contracted MW 反推出 energized / utilized AI load；
- 证明未来 scenario 一定发生；
- 用公开材料精确计算所有公司的 AI-specific ROI；
- 把 40 卷、8 篇宏观专题和 32 章中的所有数字自动升级为已审计事实。

全量历史数字 claim-by-claim audit 仍是正式发布前硬门禁；机器可读 schema 与 candidate extractor 已加入仓库，但不能替代人工/来源核验。

## 6. 纠错原则

发现高影响事实错误时，处理顺序为：

1. 定位 claim 与原始来源；
2. 判断是 Fact 错误、denominator 错误、时间窗错误、forecast/actual 身份错误，还是翻译漂移；
3. 修正中文 canonical publication；
4. 同步英文 publication；
5. 回归核心证据台账、核心参考文献索引、模型索引与相关研究卷；
6. 在 Release Notes / Git history 保留可追踪变更；
7. 如错误影响 scenario weighting，明确说明哪些判断需要重新加权。

不能用“长期逻辑仍然成立”回避已被证据否定的事实。

## 7. 版本与截止日

当前正式研究检索/修订截止日统一为 **2026-08-28**。

发布后新增资料应进入下一版本，不应静默改写已经发布的历史版本。

## 8. 对外使用边界

本报告是行业研究，不构成：

- investment advice；
- securities rating；
- legal advice；
- audit opinion；
- guaranteed forecast。

读者应把 Fact、institutional estimate、report model 与 scenario 分开读取。


\newpage


# 竞争集、替代路径与反方证据矩阵

> 本矩阵用于防止“霸权”主命题只由单一平台的强项材料支撑。它不把所有公司视为同一市场的直接可比对象，而是按物理层、系统层和终端层分别定义竞争问题。

| 分析层 | 主要观察对象 | 主要替代 / 竞争集合 | 核心比较指标 | 必须保留的反方证据 / 边界 | 主章节 |
|---|---|---|---|---|---|
| General-purpose AI system stack | NVIDIA | Google TPU/Ironwood、AWS Trainium、Microsoft Maia、Meta MTIA、AMD Instinct/ROCm | production workload、external availability、migration cost、system utilization、TCO、supply assurance | custom silicon 已是第二路线；不能用单芯片 benchmark 证明完整 system substitution | Ch02, Ch12, Ch16 |
| Advanced logic | TSMC | Samsung Foundry、Intel Foundry、SMIC，以及未来 qualified second source | qualified node、volume、yield disclosure、customer diversity、time-to-capacity | foundry revenue share ≠ frontier yield / node capacity；HPC share ≠ AI share | Ch04, Ch09, Ch17 |
| HBM / DRAM | SK hynix、Samsung、Micron | conventional DRAM economics、CXMT conventional DRAM、future HBM entrants | HBM qualification、bits/wafer input、product mix、contract pricing、allocation fulfillment | DDR/RDIMM per-wafer economics 可反向改善；HBM 资源拉力不是无限单向 | Ch05, Ch21 |
| Advanced packaging | TSMC CoWoS | Samsung/Intel packaging、OSAT expansion、alternative integration architectures | qualified capacity、lead time、yield/throughput disclosure、customer access | customer-level CoWoS allocation 未公开；B-grade demand share 不能升级为 TSMC fact | Ch06 |
| Interconnect / software | CUDA/NVLink/NVSwitch ecosystem | ROCm、XLA/TPU stack、AWS Neuron、open compiler/runtime、alternative fabrics | migration cost、framework coverage、cluster scale、debuggability、production uptime | proprietary stack 可被部分 workload 绕开；“可运行”不等于低迁移成本 | Ch02, Ch12, Ch16 |
| Power / powered land | hyperscaler / AI-campus demand | utility expansion、restart projects、SMR / nuclear、grid/transmission buildout、regional alternatives | Announced→Contracted→Permitted→Energized→Utilized、Time-to-Power | headline GW 不能相加成 active AI load；供给扩张可能把 bottleneck 移到 utilization | Ch07 |
| Model-company demand | OpenAI、Anthropic 等 Anchor Buyers | hyperscaler internal workloads、enterprise demand、sovereign demand | contract duration、delivered capacity、utilization、monetization、financing support | long-duration commitment 既提高 buildout certainty，也放大 duration mismatch | Ch13, Ch23 |
| China frontier stack | domestic accelerator/software/memory/foundry ecosystem | global frontier stack、domestic consumer/general-compute substitutes | advanced logic、HBM、packaging、interconnect、compiler/runtime、frontier workload、power closure | conventional DRAM/NAND 或 smartphone substitution 不等于 frontier-AI closure；出口限制也不等于“完全无替代” | Ch17 |
| Client / edge AI | Apple、Qualcomm、AMD、Intel | local inference、hybrid cloud-edge、NVIDIA edge products | performance/W、memory footprint、OS integration、distribution、privacy / latency | data-center system economics 不能直接外推到 battery/power-constrained edge | Ch15, Ch16 |
| Capital cycle | hyperscalers、system sellers、memory/foundry/power projects | capacity overshoot / ROI shock as counter-scenarios | utilization、D&A、FCF、clearing price、commitments、asset duration | 高 CapEx 既可能是 moat 也可能是 future write-down source；同一美元不能跨产业链账本重复相加 | Ch19, Ch22, Ch24 |

## 使用规则

1. 任何“dominance / hegemony”判断都必须至少同时回答：**替代是否存在、迁移成本多高、稀缺资源是否可多源、反向价格反馈是否正在工作。**
2. 竞争集合按 layer 定义，不把 smartphone SoC、frontier training accelerator、foundry、HBM vendor 强行放进同一个 market-share 表。
3. “没有等价替代”与“没有任何替代”必须分开。
4. 每次 major update 至少检查一条会**削弱**主论点的证据，而不只增加支持性证据。
5. 如果反方证据跨过第29章 operational trigger，应调整 S1–S4 weighting，而不是仅放在脚注中。


\newpage


# Part I · 第1章：执行摘要与未来十年核心判断

## 1. 核心结论

> **AI infrastructure 的竞争单位已经从单颗芯片上移到完整 system stack。长期价值捕获越来越取决于谁能同时协调 advanced logic、HBM、advanced packaging、interconnect、software、rack/data center 与 power 等多个 scarce layers，并把这些物理资源转化为高利用率、可迁移、能够产生现金流的真实 workload。**

这不是“永久垄断”判断，也不是对 2036 年市场份额的单点预测。本报告讨论的是一套正在变化的资源配置机制：当 AI/HPC workload 的支付能力、订单期限、预付款和资本回报显著高于传统终端时，新增资本与稀缺资源更容易向 AI infrastructure 倾斜；当供给扩张、系统替代、利用率或商业回报发生变化时，这一结构也会重新平衡。

截至 **2026 年 8 月 28 日**，公开事实更符合 **S2 — Baseline Concentration**：少数 system platform 与 scarce-layer supplier 保持强经济性，HBM、advanced packaging 与 power 等物理约束仍然重要，同时 hyperscaler custom systems、中国 parallel stack 与供给扩张继续提供真实替代路径。

## 2. 八个事实锚

### 2.1 NVIDIA 的商业交付单位已经上移到 rack-scale system

GB200 NVL72 官方规格包含 **72 Blackwell GPU、36 Grace CPU、13.4 TB HBM3E 与 17 TB LPDDR5X**。这说明高端 AI infrastructure 的采购与交付对象已经从 accelerator card 上移到 compute、memory、interconnect、software 与 rack architecture 的组合。[^ch01-1]

### 2.2 NVIDIA 的 seller-side economics 仍处高位

NVIDIA FY27 Q2 披露 Revenue **US$96.221B**、Data Center revenue **US$89.0B**、GAAP gross margin **75.0%**、GAAP operating income **US$63.734B**；公司同时表示 Vera Rubin 已进入 full production。[^ch01-2]

### 2.3 Forward supply commitments 显著扩大

NVIDIA manufacturing, supply and capacity commitments 从 2026-01-25 的 **US$95.2B** 上升到 2026-07-26 的 **US$279B**。FY27 Q2 10-Q 说明，最新承诺主要涉及 data-center infrastructure systems 所需的 memory 与 manufacturing facilities，但没有披露 supplier-level split，因此不能把该总额直接分配给 TSMC、CoWoS 或任何单一 HBM vendor。[^ch01-3]

### 2.4 TSMC 的需求结构已经明显向 HPC 倾斜

TSMC 2025 年 HPC platform 占全年 net revenue **58%**，smartphone 占 **29%**；3 nm、5 nm、7 nm 分别占 wafer revenue **24% / 36% / 14%**。这些是 revenue mix，不是 customer-level wafer allocation，更不能直接换算成 CoWoS share。[^ch01-4]

2026 Q2，TSMC 的 HPC platform revenue 占季度营收 **66%**，smartphone 为 **22%**；同季 advanced technologies（7 nm 及以下）占 wafer revenue **77%**。这进一步显示 HPC 已成为先进制造增量需求的核心驱动力之一，但 HPC 仍不能与 AI 一一等同。[^ch01-5]

### 2.5 HBM 已进入制造资源竞争层

Micron 一手披露：在 **same technology node / same number of bits** 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。这是一项 wafer-supply trade ratio，不是售价倍数，也不是所有 HBM 世代固定不变的制造常数。[^ch01-6]

TrendForce 预计 HBM + RDIMM 约占 **2026 年 DRAM bit supply 的 51%**。该数字是机构预测而非 full-year actual；与 Micron 的约 3× trade ratio 联合观察，可以解释为什么 AI/server memory 对 conventional DRAM residual supply 的影响可能大于 bit share 本身。[^ch01-7]

### 2.6 Advanced Packaging 已成为可验证的 growth constraint

TSMC 在 4Q24 表示 advanced packaging capacity “very tight”，无法满足全部客户需求；在 2Q26 earnings call 中又明确表示 packaging capacity tightness 正在限制客户增长。TSMC 没有公开 customer-level CoWoS allocation，因此第三方对客户集中度的估计必须保留机构估计身份。[^ch01-8]

### 2.7 Power 已成为与 wafer、memory、packaging 并列的独立物理约束

NVIDIA DGX GB200 hardware guide 给出的 rack power 约为 **120 kW**。与此同时，835 MW 级核电重启、最高 1.92 GW 的长期 PPA、以及面向 2030–2035 的数百 MW 级先进核电开发计划，显示 Time-to-Power、grid connection、substation、firm power 与 permitting 已进入 AI system delivery 的约束集合。Contracted、Permitted、Energized、Utilized MW 必须严格分开。[^ch01-9]

### 2.8 Hyperscaler custom systems 已经形成真实第二路线

Google Ironwood、AWS Trainium3 UltraServers、Microsoft Maia 200 与 Meta MTIA 300 均显示，hyperscaler 的竞争已经从“自研一颗 ASIC”上移到 accelerator、compiler/runtime、interconnect、rack/pod 与 captive workload 的 system-stack competition。[^ch01-10]

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

中国已经形成真实且持续发展的 accelerator/software parallel stack，并在 consumer computing、DRAM/NAND、部分通用计算与本土软件生态上形成更强的平行供给能力；但 frontier AI 的等价闭环仍需要 advanced logic、HBM-class memory、advanced packaging、high-speed interconnect、compiler/runtime、frontier workload 与 power 同时达到可验证规模。[^ch01-11]

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

[^ch01-1]: NVIDIA, “GB200 NVL72,” official product page, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^ch01-2]: NVIDIA, “NVIDIA Announces Financial Results for Second Quarter Fiscal 2027,” 2026, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^ch01-3]: NVIDIA Corporation, Form 10-Q for quarter ended 2026-07-26, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm ; NVIDIA Corporation, FY26 Form 10-K, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
[^ch01-4]: TSMC, 4Q25 Presentation / 2025 full-year platform and technology mix, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
[^ch01-5]: TSMC, “2Q26 Quarterly Results,” platform and technology revenue mix, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^ch01-6]: Micron Technology, FY24 Q2 Prepared Remarks, 2024-03-20, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^ch01-7]: TrendForce, 2026-08-25, HBM + RDIMM 2026E DRAM bit-supply structure, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^ch01-8]: TSMC, 4Q24 Earnings Conference Transcript, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf ; TSMC, 2Q26 Earnings Conference Transcript, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^ch01-9]: NVIDIA, DGX GB200 Hardware Guide, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html ; Constellation, Crane Clean Energy Center announcement, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs ; Talen Energy, 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm ; Kairos Power / Google partnership, https://www.kairospower.com/google
[^ch01-10]: Google, “Ironwood TPU,” https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; AWS, “Amazon EC2 Trn3 UltraServers,” https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ ; Microsoft, “Maia 200,” https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ ; Meta, “MTIA 300,” https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
[^ch01-11]: CXMT, STAR Market registration prospectus, 2026-05-27, Shanghai Stock Exchange, https://static.sse.com.cn/stock/disclosure/announcement/c/202605/002170_20260527_23QQ.pdf ; Moore Threads, MTT S80 official product page, https://en.mthreads.com/product/S80 ; DeepSeek, “DeepSeek-V3 Technical Report,” https://arxiv.org/abs/2412.19437 ; TrendForce, 2026-06-12, 1Q26 foundry revenue shares, https://www.trendforce.com/presscenter/news/20260612-13095.html


\newpage


# Part I · 第2章：NVIDIA 系统栈与平台权力


## 1. 竞争单位已经从 GPU 上移到系统栈

NVIDIA 当前最重要的竞争优势，不是某一代 GPU 的单点性能，而是把 accelerator、HBM、scale-up fabric、compiler/runtime、libraries、rack architecture 与部署工具组织成一个可重复交付的系统。GB200 NVL72 的官方产品规格已经清楚显示这种销售单元上移：[^ch02-1]

**Table 2.1 — GB200 NVL72 的 rack-scale 系统结构**

| 层 | 官方规格 / 结构 |
|---|---|
| GPU | 72 Blackwell GPU |
| CPU | 36 Grace CPU |
| GPU memory | 13.4 TB HBM3E |
| CPU memory | 17 TB LPDDR5X |
| Scale-up domain | 72-GPU NVLink domain |
| Rack | liquid-cooled rack-scale system |

**Source:** NVIDIA GB200 NVL72 official product page.[^ch02-1]  
**Note:** 该表描述官方系统规格，不代表实际出货量、利用率或客户部署规模。

这改变了竞争的比较方式。单卡时代可以主要比较 FLOPS、显存和卡价；rack-scale 时代必须同时比较 memory hierarchy、scale-up/scale-out interconnect、compiler/runtime、distributed training stack、power/cooling、部署工具和 workload migration cost。

因此，“更便宜的一颗 ASIC”并不自动等于“更便宜的一套生产级 AI system”。

## 2. NVLink / NVSwitch：把通信从外部网络问题变成系统内部能力

frontier model training 的瓶颈并不只在单卡计算。tensor parallel、pipeline parallel、expert parallel 和 collective communication 会把性能越来越多地交给 bandwidth、topology、synchronization 与 collective implementation。

NVLink/NVSwitch 的战略价值，是把 scale-up communication 设计为平台内部能力。GB200 NVL72 把 72 颗 GPU 组织在一个 NVLink domain 中；NVIDIA 当前产品页给出整柜 **130 TB/s aggregate NVLink bandwidth**。[^ch02-1]这并不能证明任何以太网方案天然无法替代，但它改变了替代问题：

> 竞争者必须替代的不是一颗 GPU，而是“计算 + 内存 + 域内互联 + 软件执行模型”这一整组生产能力。

因此，本报告不使用未经公开仪器验证的 ns 级延迟对比，也不把宣传性 benchmark 直接写成第三方实测结论。真正需要观察的是可复核的 production workload：迁移后吞吐、利用率、工程成本与可靠性是否仍有显著差距。

## 3. CUDA / PTX：护城河不是“软件税”，而是跨代软件资产

CUDA 的战略价值不能被简化成一个不存在于财报中的固定“软件溢价”。它更接近长期积累的软件资产：

- compiler 与 kernel ecosystem；
- libraries；
- profiling / debugging；
- framework integration；
- distributed communication；
- inference / training runtime；
- deployment tooling；
- developer knowledge。

PTX 的作用尤其重要：它提供稳定的 intermediate representation，使上层软件不必在每一代 GPU 变化时完全重写。硬件路线可以从 Hopper 进入 Blackwell、再进入 Rubin，而相当一部分上层软件资产可以继续复用。

这形成一种跨代机制：

**更大的 installed base → 更多 production software assets → 更低的平台内升级成本 → 更高的平台外迁移成本。**

它解释了为什么 NVIDIA 的优势不能只用一次 benchmark 测量，也不能用一个未经披露的“CUDA 毛利率”证明。

## 4. Rack-scale architecture 把 switching cost 延伸到数据中心

当采购单位上移到 rack，迁移成本也从 software 延伸到 physical infrastructure。客户围绕特定系统建设的，不只是代码，还包括：

- rack / pod topology；
- power distribution；
- liquid cooling；
- networking；
- firmware；
- cluster management；
- scheduling 与 performance validation。

因此，换一颗 accelerator 可能只是一个采购动作；换一套 rack-scale system，往往意味着重新验证软硬件协同和数据中心工程。

这一点是 NVIDIA 系统权力最容易被“芯片 benchmark”低估的地方。系统越往 rack/pod 和园区层延伸，竞争者越需要在部署时间、可靠性和总拥有成本上证明替代，而不是只在峰值算力上接近。

## 5. 平台利润为什么会转化为下一代资源预订能力

系统级优势如果能够产生高利润和高自由现金流，就会进一步影响供应链。当前最重要的公司层锚点不需要在多个章节反复铺开，只保留一组：

**Table 2.2 — NVIDIA 当前 seller-side economics 与前置供应承诺**

| 指标 | 当前公开值 |
|---|---:|
| FY26 Data Center revenue | US$193.737B |
| FY26 NVIDIA-defined non-GAAP free cash flow | US$96.575B |
| FY27 Q2 revenue | US$96.221B |
| FY27 Q2 Data Center revenue | US$89.0B |
| FY27 Q2 GAAP gross margin | 75.0% |
| FY27 Q2 GAAP operating income | US$63.734B |
| 2026-07-26 manufacturing, supply, and capacity commitments | US$279B |

**Source:** NVIDIA FY26 results, FY27 Q2 results and FY27 Q2 Form 10-Q.[^ch02-2][^ch02-3][^ch02-4]  
**Note:** US$279B 为 aggregate manufacturing, supply and capacity commitments；公开文件未提供 supplier-level split。

FY27 Q2 10-Q 说明，最新 commitments 主要与 data-center infrastructure systems 所需的 memory 和 manufacturing facilities 有关。[^ch02-4]公开文件没有把 US$279B 拆分到 TSMC、CoWoS、SK hynix、Micron 或 Samsung，因此它只能证明整体前置供应承诺规模，不能写成任何单一供应商的确定收入。

这构成一个可检验的跨代强化机制：

**高系统利润 → 更强供应承诺与资源预订能力 → 更高交付确定性 → 更强客户留存 → 下一轮系统收入。**

它不是自动垄断公式。供应商仍会考虑客户多元化、信用、利用率、地缘政治和长期议价平衡。

## 6. NVIDIA 的系统权力也有明确物理边界

NVIDIA 并不直接制造所有关键稀缺层。它仍依赖：

- leading-edge foundry；
- HBM vendors；
- advanced packaging ecosystem；
- data-center operators；
- grid / power suppliers。

因此，平台权力强并不意味着物理供给完全内生。TSMC、HBM、advanced packaging 和 power 中任一层失配，都可能成为下一代交付约束。

这也是为什么本报告把 **Scarce-layer Value Capture** 与“市场份额垄断”分开。系统平台可以拥有很强的组织和出价能力，但仍然受到外部物理供应弹性约束。

## 7. 真正的反击是 Cloud System Stack，而不是单颗 ASIC

Google TPU/Ironwood、AWS Trainium、Microsoft Maia、Meta MTIA 的战略意义，不在于“有另一颗芯片”，而在于 hyperscaler 同时拥有：[^ch02-5]

- 自有大规模 workload；
- cloud distribution；
- data-center control；
- internal compiler/runtime；
- 自研 interconnect / rack/pod；
- 针对较窄 workload 做系统级优化的能力。

所以未来竞争不是：

> NVIDIA GPU vs custom ASIC

而是：

> **NVIDIA system stack vs cloud system stack**

这会同时产生两个方向相反但可以并存的效应：

1. **Platform-profit diversion**：云自研系统减少部分对 NVIDIA 平台利润池的依赖；
2. **Upstream resource competition**：自研系统本身仍会争夺先进逻辑、HBM、advanced packaging 和 power。

因此，cloud custom silicon 的成功并不自动意味着上游物理稀缺缓解。

## 8. 云系统需要达到什么程度才算真正削弱护城河

判断 NVIDIA system moat 是否发生结构性削弱，不能靠新闻数量或单卡性能，而要看以下变量是否同时变化：

- cloud system stack 是否进入 frontier training / high-value inference 的生产规模；
- open software 是否显著降低 CUDA migration cost；
- alternative scale-up fabric 是否达到 production-grade scale；
- workload 在多套 system stack 间迁移时，工程成本与性能损失是否持续下降；
- scarce upstream resources 是否不再明显支持 NVIDIA roadmap；
- 大客户是否能够把真实 workload 分散到多套系统，而不是只做 benchmark 或内部窄场景试验。

如果这些变化中的多项持续出现，NVIDIA 的平台权力会从“系统级定价权”逐步退回更可谈判的“集成优势”。如果迁移仍然昂贵，而平台内跨代升级继续保持低摩擦，则系统护城河仍然成立。

## 9. 当前判断

截至 2026 年 8 月，最准确的描述不是“GPU 竞争已经结束”，也不是“云 ASIC 已经替代 NVIDIA”。

更准确的是：

> **NVIDIA 当前拥有最成熟的商业化通用 AI system stack；hyperscaler 已经形成真实的第二条 system-stack 路线，但其替代程度必须用生产级 workload、迁移成本、利用率和上游资源依赖来验证。**

这也是本书后续分析 TSMC、HBM、advanced packaging、power 与 capital cycle 的起点：真正的竞争单位已经从裸片上移到系统，而系统仍然受多个外部 scarce layer 共同约束。

## References

[^ch02-1]: NVIDIA, “GB200 NVL72,” official product page, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^ch02-2]: NVIDIA, “NVIDIA Announces Financial Results for Fourth Quarter and Fiscal 2026,” https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
[^ch02-3]: NVIDIA, “NVIDIA Announces Financial Results for Second Quarter Fiscal 2027,” https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^ch02-4]: NVIDIA Corporation, Form 10-Q for quarter ended 2026-07-26, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^ch02-5]: Google, “Ironwood TPU,” https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; AWS, “Amazon EC2 Trn3 UltraServers,” https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ ; Microsoft, “Maia 200,” https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ ; Meta, “MTIA 300,” https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/


\newpage


# Part I · 第3章：AI Resource Gravity 与 Non-AI Residual Capacity


## 1. “AI 虹吸”不是把所有半导体产能一起抽走

AI infrastructure 对供应链的影响具有强烈层级性。真正容易被重排的，是与 frontier AI 共享且短期供给弹性较低的资源：

- advanced logic；
- HBM / RDIMM / selected DRAM；
- advanced packaging；
- high-end substrate / networking；
- power-management components；
- data-center power。

本书将这种高价值 demand 对资本与供给的吸引定义为 **AI Resource Gravity**。

## 2. Resource Gravity 的经济机制

如果一个需求池能够同时提供更高 willingness-to-pay、更长订单、更高利用率确定性和更强信用，供应商有经济动机优先把新增资本和产能投向它。

传导链可写成：

> high-value AI/server demand → higher expected return → product-mix / capacity allocation shift → lower residual capacity for lower-priority demand

这不意味着供应商只服务第一名，也不意味着所有传统市场都被停止供货。它描述的是**边际新增资源的优先级变化**。

### 2.1 价格不是唯一清算机制：Allocation Assurance 比 Spot Price 更关键

在极端紧缺期，市场并不只通过涨价清算。**长期协议、客户信用、预付款、采购规模和供应商给出的 allocation fulfillment** 会先决定谁能拿到足够的量。

TrendForce 2026-01 明确指出，美国 CSP 锁定 capacity 后，其他买家为了确保 supply allocation 被迫接受更高价格；2026-03 又指出，PC OEM / module maker 如果 allocation fulfillment 较低，只能从供应商或模组厂以更高价格补货。[^ch03-1][^ch03-2]

因此：

> **willingness-to-pay ≠ guaranteed quantity**

真正的系统性风险不是“价格涨了多少”，而是 residual capacity 低到使次级买家即使接受更高报价，也无法获得足够、按时、可持续的交付量。

这比“某一家拿走100%产能”的绝对化说法更可验证，也更接近产业现实。

## 3. 为什么 Non-AI Residual Capacity 比总产能更重要

传统市场真正获得的供给可以抽象为：

> **Non-AI Residual Capacity = total effective supply − AI/server absorption − other priority demand**

如果 total supply +20%，但 AI/server demand 同期吸收 +40%，非 AI 市场的有效 residual capacity 仍可能下降。

因此，“全球产能增长”不能自动推出 PC、smartphone、general server 或消费 GPU 的供给恢复宽松。

### 3.1 Two-Speed Semiconductor Economy：不同终端共享资源，但资本形成速度不同

AI Infrastructure Economy 与 Traditional Device Economy 共享部分 advanced logic、memory、packaging 与 power-management 资源，却具有不同的 willingness-to-pay、合同期限、预付款结构、BOM 约束与终端价格弹性。

这意味着 AI Resource Gravity 的长期结果不只是当期 allocation 变化，更会影响下一轮资本形成：供应商会根据风险调整后回报决定下一美元 CapEx 投向哪里。**Two-Speed Semiconductor Economy** 描述的是这种资源经济差异，而不是“消费电子被永久献祭”的事实判决。

### 3.2 AI Capacity Gap：绝对缺口与增长缺口必须分开

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

## 4. Memory 是最清晰的 observed crowding-out 路径

Micron 一手披露 same node / same bits 条件下 HBM3E 约需要 DDR5 **3× wafer supply**；TrendForce 预计 2026 年 HBM + RDIMM 合计约占 DRAM bit supply **51%**。[^ch03-3][^ch03-4]

这使 memory 层出现一条可观察机制：

> HBM/RDIMM demand 上升 → wafer/cleanroom/capital 向高价值 server products 倾斜 → conventional DDR/LPDDR residual supply 改变 → consumer/general-compute price 与 configuration 承压

51% 是 2026E bit-supply forecast，不是 HBM-only share，也不是 wafer share。

## 5. PC 与 Gaming：GPU allocation + memory residual 双重暴露

NVIDIA FY26 10-K 披露 Gaming revenue **US$16.0B、同比 +41%**，同时预计 supply constraints 会成为 FY27 Q1 及之后 Gaming 的 headwind。[^ch03-5]

这证明消费 GPU 侧存在供应约束，但不能直接推出所有约束都由 Data Center allocation 造成。

PC 还承受第二条链：server/HBM demand 改变 DRAM product mix，进而影响 DDR5/LPDDR residual supply。于是 PC 更容易出现 GPU availability 与 memory pricing 的双重压力。

## 6. General Server：RDIMM 已进入同一高价值 memory pool

general server 不一定使用 HBM，但大量使用 DDR5 RDIMM。TrendForce 把 RDIMM 与 HBM 一起纳入 2026 DRAM bit-supply 前向结构。[^ch03-4] 这说明 traditional server memory 并不是完全独立的 commodity river。

所以 AI/server infrastructure expansion 可以通过 memory allocation 间接提高 general-server cost，即使服务器本身没有使用 frontier accelerator。

## 7. Smartphone：没有被 AI 挤掉，但增量资源竞争已改变

TSMC 2025 smartphone platform 占全年 net revenue **29%**，platform revenue 同比增长 **11%**；HPC 占 **58%**。[^ch03-6]

这不能写成“AI 取代 smartphone”。更准确的是：

- smartphone 仍是巨大需求平台；
- HPC 对新增 leading-edge investment 的吸引更强；
- LPDDR / selected packaging / power-management components 可能与 AI/server demand 共享部分资源；
- flagship input cost 与中端 node migration 节奏更容易受到 residual-capacity pressure。

## 8. Automotive：暴露更慢、更选择性

automotive 具有长 qualification cycle、高 reliability requirement 和大量 mature-node usage，因此不会在所有环节与 frontier AI 直接竞争。

其主要共享层更接近 central compute、memory、power management 与 selected advanced packaging。汽车更适合描述为**第二阶段选择性传导**，而不是第一波全面 shortage。

## 9. Residual pressure 通常先表现为升级税，而不是停产

当有效残量下降，企业常见的应对是：

1. 涨价；
2. 降规格；
3. 延后升级；
4. 延长 mature node / alternative supplier 的使用周期。

所以供应链压力更可能先表现为 flagship BOM 上升、replacement cycle 延长、high-end feature 下放变慢和 product segmentation 加剧，而不是整个行业立即停产。

## 10. China parallel supply 会改变本地 residual structure，但不能自动关闭 frontier bottleneck

中国本地 logic、DRAM、NAND 与终端制造能力增强，可以缓解部分 domestic consumer-market pressure。

但替代必须分层：consumer computing 较强，general compute 部分替代，frontier AI 则仍取决于 advanced logic、HBM-class memory、packaging、interconnect 与 software closure。

因此，本地消费供给扩张可以改善国内终端 residual capacity，却不会自动消除全球 frontier AI 的上游瓶颈。

## 11. 实体企业还承担第二层 AI adoption cost

制造企业采用 AI 时，不只面对硬件/input cost，还要支付 cloud inference、software integration、data pipeline、security/compliance 和 workflow redesign。

真正的 productivity return 应按：

> **Net productivity value = productivity gain − total AI adoption cost**

因此，上游 resource inflation 与下游 AI-service cost 可以同时作用于实体企业。

## 12. 当前判断与证伪

截至 2026 年 8 月，证据更支持：

> **选择性传导 + 产品分层 + Non-AI Residual Capacity pressure**

而不是“所有芯片都被 AI 抢走”。

如果 DDR/LPDDR 价格与供给恢复宽松、consumer GPU availability 明显改善、smartphone/general-server upgrade 不再受到 shared-resource pressure，且 memory/packaging product mix 不再持续向 AI/server 倾斜，本章对 crowding-out 的判断应下调。

## References

[^ch03-1]: TrendForce, 2026-01-05, CSP capacity locking and allocation pricing, https://www.trendforce.com/presscenter/news/20260105-12860.html
[^ch03-2]: TrendForce, 2026-03-31, allocation fulfillment and higher-price procurement by OEMs/module makers, https://www.trendforce.com/presscenter/news/20260331-12995.html
[^ch03-3]: Micron Technology, FY24 Q2 Prepared Remarks, 2024-03-20, HBM3E wafer-supply trade ratio versus DDR5, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^ch03-4]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^ch03-5]: NVIDIA Corporation, FY26 Form 10-K, U.S. SEC, Gaming revenue and supply-constraint disclosure, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
[^ch03-6]: TSMC, 4Q25 Presentation / 2025 full-year platform mix, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf


\newpage


# Part I · 第4章：TSMC、N2 与先进制造资源分配


## 1. 真正的竞争对象不是一个“2 nm wafer price”

frontier AI system 同时需要 leading-edge logic、HBM、advanced packaging、substrate、interconnect 与 power。node leadership 只是进入下一代 system 的必要条件之一。

所以先进制造竞争的核心不是某个市场传闻报价，而是：

> **谁能在 N2/N2P/A16 等下一代资源进入 volume production 时，稳定获得足够规模，并同时匹配 memory、packaging 与 system roadmap。**

## 2. TSMC 2025 的关键事实

**Table 4.1 — TSMC 2025 产能、技术与平台收入结构**

| 指标 | 2025 |
|---|---:|
| 12-inch-equivalent wafer shipments | ~15.0M |
| annual capacity | >17M |
| 3 nm wafer-revenue share | 24% |
| 5 nm | 36% |
| 7 nm | 14% |
| ≤7 nm | 74% |
| HPC platform | 58% of net revenue; +48% YoY platform growth |
| Smartphone platform | 29%; +11% YoY platform growth |
| largest / second-largest customer | 19% / 17% of annual revenue |

**Source:** TSMC 2025 Annual Report、2025 Form 20-F 与 4Q25 Presentation.[^ch04-1][^ch04-2][^ch04-3]  
**Note:** platform share 与 node share 均为 revenue-based metrics；customer revenue share 不能换算为 wafer、node 或 CoWoS allocation。

这些数字证明 HPC 已成为 TSMC 最大 platform，同时 TSMC 仍服务广泛客户。它们不支持“TSMC 已成为某一家客户专属 fab”。

## 3. Customer revenue share 不能换算成 wafer / node / CoWoS share

2025 largest customer 19% 与 second-largest customer 17% 是**年度收入排名口径**。[^ch04-2]

它们不能换算成 N2 wafer share、3 nm wafer share、CoWoS share、HPC wafer share 或 physical wafer count。

另一张匿名客户表才支持跨年比较：Customer A **12%→19%**、Customer B **22%→17%**（2024→2025）。[^ch04-4]annual largest/second-largest ranking 与 anonymized A/B series 回答不同问题，不能拼成同一客户的虚假轨迹。

同样，HPC 58% 是 platform revenue share，不是 wafer shipment share。

## 4. N2 的战略价值来自“增量首发资源”

N2 的意义不只是 transistor density。竞争者真正关心：

- volume production timing；
- available scale；
- yield / delivery stability；
- HBM 与 packaging 配套；
- system-level performance conversion；
- roadmap continuity。

拿到某个 node 并不自动构成 system victory。如果 memory、packaging、interconnect 或 power 缺失，完整交付仍然受限。

## 5. AHICR：比历史 revenue share 更适合分析未来分配

本书使用 **Advanced/HPC Incremental Capacity Capture Ratio（AHICR）** 分析下一代增量资源：

> AHICR = 某买方获得的新增 advanced AI/HPC resource ÷ 全行业对应新增 resource

AHICR 必须按 physical layer 分别看 logic、HBM、packaging、power，不能把不同单位硬加在一起。

50/60/70/80% 只能作为 D 级 scenario levels，用于观察 residual capacity 的非线性变化，不是当前披露的客户份额。

## 6. TSMC 的资源分配不是单变量决定

先进产能 allocation 更可能同时考虑：price、committed volume、contract duration、prepayment、credit quality、utilization certainty、roadmap stability、customer diversification 与 geopolitical risk。

所以不能用“第一客户一定得到全部最好资源”的决定论。

更合理的机制是：订单规模、信用、预付款与 roadmap certainty 提高买方对新增资源的议价能力；供应商同时仍有客户多元化、长期议价权和地缘风险管理的动机。

## 7. Advanced Packaging 必须与 logic pool 分开

TSMC 一手资料已确认 advanced-packaging tightness，但 customer-level CoWoS allocation 未披露。[^ch04-5] TrendForce 对 NVIDIA 2025 CoWoS demand >60% 的估计属于 B 级机构数据。[^ch04-6]

5.37 CoWoS wafers/rack 是报告侧 D 级 geometry stress test，不是 TSMC yield，也不能拿 TSMC 全年 15M front-end wafer shipments 去除。

这说明“leading-edge logic available”与“complete AI system deliverable”不是同一个问题。

## 8. Samsung / SMIC 的 foundry share 不能直接等同于 frontier substitution

TrendForce 2026 Q1 foundry revenue share 约为：TSMC **72%**、Samsung Foundry **6.5%（excluding System LSI）**、SMIC **5.1%**。[^ch04-7]

这些是 revenue share，不是 frontier-AI capacity share。形成第二套可替代 supply system 还要同时验证 node performance、yield、advanced packaging、HBM ecosystem、customer qualification 与 software/system integration。

因此，“有第二家 foundry”与“有完整第二套 frontier AI supply stack”是不同命题。

## 9. 当前判断

TSMC 的战略地位来自三个同时存在的条件：leading-edge logic 强、HPC 已成为最大 platform、advanced packaging 仍是公开确认的增长约束。

未来最关键的观察变量不是某一季 customer revenue share，而是：N2/N2P/A16 增量资源的客户结构、HBM / packaging supply、cloud custom silicon 的新增资源竞争，以及第二制造体系能否在 logic + packaging + memory 上形成组合替代。

## References

[^ch04-1]: TSMC, 2025 Annual Report, https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^ch04-2]: Taiwan Semiconductor Manufacturing Company Limited, 2025 Form 20-F, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm
[^ch04-3]: TSMC, 4Q25 Presentation / 2025 full-year platform and technology mix, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
[^ch04-4]: TSMC, 2025 Consolidated Report, anonymized Customer A/B revenue series, https://www.sec.gov/Archives/edgar/data/1046179/000104617926000024/a2025q4consolidatedreport-.htm
[^ch04-5]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging tightness, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^ch04-6]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^ch04-7]: TrendForce, 2026-06-12, 1Q26 foundry revenue shares, https://www.trendforce.com/presscenter/news/20260612-13095.html


\newpage


# Part I · 第5章：HBM 与存储资源重构


## 1. HBM 已从 GPU 配件变成系统级资源

在 frontier AI system 中，HBM 同时影响模型容量、batch、context、并发、communication pattern 与 accelerator utilization。GB200 NVL72 官方配置包含 **13.4 TB HBM3E/rack**，[^ch05-1]说明采购单位上移到 rack scale 后，memory demand 也从“每颗 GPU 多少 GB”上移到“一个部署需要多少 PB”。

因此 HBM 的产业影响不只发生在 accelerator BOM，还会传导到 DRAM wafer allocation、cleanroom space、advanced packaging、memory-vendor product mix 与 conventional DRAM residual supply。

## 2. Micron 的约 3× 是当前最重要的一手物理锚

Micron FY24 Q2 prepared remarks 给出了明确适用边界：在 **same technology node / same number of bits** 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。[^ch05-2] Micron FY25 10-K 又确认，生产相同比特的 HBM 需要更多 wafers 与 cleanroom space。[^ch05-3]

因此这条证据可以支持：

- HBM3E 对制造投入的占用高于同 bit DDR5；
- HBM 扩张会更强地占用 DRAM wafer / cleanroom input；
- conventional DRAM 的有效 residual capacity 可能受到更大压力。

但它**不能**被改写成 HBM 售价是 DDR5 的 3×，也不能当作每座 fab、每一代 HBM 都固定不变的“3:1 定律”。Micron 对 HBM4 的公开表述只是 trade ratio 预计进一步上升；具体 HBM4/HBM4E 数值仍需未来 vendor disclosure。

## 3. 51% 是 2026E DRAM bit-supply 预测，不是 HBM 实绩

TrendForce **预计**，2026 年 **HBM + RDIMM 合计约占 DRAM bit supply 的 51%**。[^ch05-4]这是一条 B 级机构前向预测，必须同时保留三个边界：

1. 51% 包含 HBM **和 RDIMM**，不能写成“51% DRAM 都是 HBM”；
2. 它是 **bit supply**，不是 wafer share；
3. 它是 **2026E forecast**，不是已经完成的全年 actual。

这条预测与 Micron 的同-bit wafer trade ratio 结合后，给出一个更重要的机制：**bit share 不能完整反映制造投入压力。** 当一部分高价值 bit 需要更多 wafer/cleanroom input 时，它对制造资源的吸收可能高于其 bit 占比。

## 4. Non-AI Residual Capacity 在 memory 层如何形成

memory 资源重分配可以写成一条清晰链条：

**AI/server memory demand 上升 → HBM/RDIMM product mix 上升 → wafer / cleanroom / packaging input 向高价值产品倾斜 → conventional DDR/LPDDR residual capacity 收紧 → 非 AI 终端更容易承受价格与配置压力。**

这里的关键变量不是全球 DRAM 总产能，而是 AI/server demand 吸收之后，消费电子和其他传统 workload 实际能获得多少有效供给。

因此，本书把 memory 层的核心指标定义为 **Non-AI Residual Capacity**，而不是简单用“DRAM 总产能增长”判断传统市场是否恢复宽松。

## 5. SK hynix 的 FY25 财务显示 HBM 已经改变产品经济性

SK hynix FY25 官方结果为：Revenue **KRW 97.1467T**、Operating profit **KRW 47.2063T**、Operating margin **49%**、Net income **KRW 42.9479T**，且公司披露 HBM revenue 同比超过一倍。[^ch05-5]

这些数据不能证明 HBM 单独贡献全部利润，但足以说明高价值 memory product mix 已显著改善 memory-vendor economics。与此同时，conventional server memory demand 仍然重要，这进一步说明 HBM 与 DDR5/RDIMM 并非完全隔离的资本和制造体系。

## 6. HBM 供给集中，但不制造未经披露的精确份额表

高端 HBM 供给主要集中在 SK hynix、Samsung 与 Micron。真正的进入壁垒不仅是 DRAM fab CapEx，还包括：

- TSV / stacking；
- yield learning；
- advanced-packaging integration；
- customer qualification；
- generation timing；
- high-volume manufacturing stability。

公开一手资料不足以支持一张完全同口径、可审计的三厂精确 HBM market-share 表，因此本报告不把媒体或卖方估算升级为公司官方份额。

### 6.1 价格反馈：HBM 的资源虹吸不是无限单向过程

资源重分配存在价格反馈。TrendForce 2026-06-02 的模型估算显示，随着 conventional DRAM 自 2025 年下半年起大幅涨价，**DDR5 64GB RDIMM 在 2026 Q1 的 per-wafer revenue 已超过 HBM**；该机构同时估算 HBM profitability 低于 DDR5 64GB RDIMM。[^ch05-6]

这是 B 级机构估算，不是 Samsung、SK hynix 或 Micron 披露的产品级实际毛利率。但它揭示了重要的自我修复机制：

> HBM/AI demand 上升 → conventional DRAM residual supply 收紧 → DDR5/RDIMM price 上升 → conventional DRAM per-wafer economics 改善 → 继续向 HBM 转产的相对激励下降 → memory vendor 重新平衡 product mix。

因此，AI Resource Gravity 不是无限的单向抽水机。长期 allocation 取决于不同产品的风险调整后单位稀缺资源回报、qualification、yield、generation transition 与客户合同结构。

## 7. Rack-scale 需求只能做情景算术，不能伪装成 shipment

以 GB200 NVL72 **13.4 TB HBM3E/rack** 为产品规格锚，可做数量级压力测试：

**Table 5.1 — GB200 NVL72 rack 数量与 HBM3E 情景需求**

| 情景 rack 数 | HBM3E demand |
|---:|---:|
| 1,000 | 13.4 PB |
| 10,000 | 134 PB |
| 30,000 | 402 PB |
| 50,000 | 670 PB |

**Source:** NVIDIA GB200 NVL72 official specification；本报告情景算术。[^ch05-1]  
**Note:** rack count 为 D 级假设，表中 PB 数值不是实际 shipment 或 consumption。

这些都是 **D 级 scenario demand arithmetic**。NVIDIA 没有披露可直接用于这一乘算的全年 rack shipments，memory vendors 也没有披露与这些 rack 一一对应的 customer-level annual HBM bits，因此不得把 50,000 racks 或 670 PB 写成实际消费量。

## 8. HBM4 会提高跨层资本密度，但不能提前编出固定倍率

下一代 HBM 的复杂度不只来自更高 stack count，还可能来自 logic base die、advanced foundry、packaging、testing 与 qualification 的进一步耦合。

如果 logic base 使用更先进 process，memory bottleneck 会进一步向 foundry / packaging 层扩展，形成：

**HBM vendor → logic base die → advanced foundry → advanced packaging → accelerator qualification**。

这意味着 HBM 可能从“memory bottleneck”演化为跨 memory/foundry/packaging 的 system bottleneck。但在 vendor 正式披露之前，不能把 HBM3E 的 ~3× 机械改成 HBM4 4×、5×，也不能把某一种 12-Hi / 16-Hi configuration 当成所有 HBM4 的统一量产规格。

## 9. HBM 的库存属性与标准 commodity 不同

HBM 与标准 commodity memory 的一个重要差别是 generation-specific qualification。产品代际推进快、与具体 accelerator generation 强绑定、qualification 周期长、obsolete risk 高。

因此可以同时出现：

> **旧一代 HBM 出现供给宽松，而下一代 frontier HBM 仍然短缺。**

一代产品的过剩不会自动解决下一代产品的 qualification、yield 与 packaging 约束。

## 10. “推理转向 DDR”不会自动逃离 memory constraint

部分 inference workload 可以用更多 DDR/LPDDR 换取较低单位 memory cost，但 frontier inference 仍受 KV cache、long context、large batch、MoE routing、low-latency serving 与 multi-accelerator communication 影响。

更重要的是，RDIMM 本身已经被计入 TrendForce 的 AI/server memory 前向结构。于是从 HBM 向 DDR5 转移，更像是在同一个更宽 memory resource pool 中改变 cost/bandwidth tradeoff，而不是凭空创造一条完全独立的供给河流。

## 11. 什么会削弱 HBM 的长期战略价值

HBM 的长期稀缺不是必然。以下变化会显著削弱当前机制：

- memory architecture 大幅降低对高带宽堆叠的依赖；
- algorithmic efficiency 持续降低 memory bandwidth / capacity demand；
- HBM wafer/cleanroom trade ratio 显著改善；
- stacking、yield、logic-base 与 advanced packaging 的供给弹性大幅提高；
- conventional DRAM 与 HBM 的制造资源逐渐充分解耦。

因此，长期判断不是“HBM 永远短缺”，而是：

> **只要 frontier-system bandwidth demand 增长快于 HBM supply elasticity，且每 bit 制造投入仍显著高于 conventional DRAM，HBM 就会继续作为 AI infrastructure 的核心 scarce layer。**

## References

[^ch05-1]: NVIDIA, “GB200 NVL72,” official product page, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^ch05-2]: Micron Technology, FY24 Q2 Prepared Remarks, 2024-03-20, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^ch05-3]: Micron Technology, FY25 Form 10-K, HBM wafer and cleanroom requirements, U.S. SEC, https://www.sec.gov/Archives/edgar/data/723125/000072312525000028/mu-20250828.htm
[^ch05-4]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^ch05-5]: SK hynix, FY25 Financial Results, https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
[^ch05-6]: TrendForce, 2026-06-02, per-wafer revenue comparison for HBM and DDR5 64GB RDIMM, https://www.trendforce.com/presscenter/news/20260602-13074.html


\newpage


# Part I · 第6章：Advanced Packaging、CoWoS 与系统交付瓶颈


## 1. Advanced packaging 已经从配套环节变成系统交付层

frontier AI accelerator 越来越依赖 multi-die integration、HBM、large interposer 与 high-speed die-to-die connection。于是 advanced packaging 不再只是“芯片做完之后的后段工序”，而成为：

> **决定一个 frontier AI system 能否按数量交付的 scarce manufacturing layer。**

这解释了一个看似矛盾的现象：foundry 逻辑晶圆可以继续扩产，但完整 system 仍然可能因为 packaging/HBM integration 不足而无法交付。

## 2. TSMC 已经一手确认 tightness，但年份口径必须分开

TSMC 的公开表述足以确认 advanced-packaging tightness：[^ch06-1][^ch06-2]

- 2024 Q4：管理层称相关 capacity **very tight**，不能满足全部客户需求；
- 2026 Q2：管理层明确称 packaging capacity **so tight that now it limits my customers' growth**。

收入披露也必须保持原始年份标签：

- 4Q24 transcript：**advanced packaging and testing >8% of revenue**；
- 4Q25 transcript 的公司会后更正口径：**advanced packaging slightly over 10% of 2025 revenue**。[^ch06-6]

这两个标签并不完全相同，因此本报告**不把 >8% → >10% 当作严格同口径连续时间序列**，也不把 2025 的 advanced packaging 扩写回 “advanced packaging + testing”。

## 3. CoWoS tightness 是 A 级事实，customer allocation 不是

TSMC 公开资料能够支持：advanced packaging 很紧、CoWoS 是其中重要组成、packaging tightness 已经限制客户增长。

但 TSMC 没有公开一张可用于本书的 customer-level CoWoS allocation table，也没有给出按客户拆分的官方 CoWoS share。

因此必须把两个问题分开：

- **A 级事实：** packaging / CoWoS tightness；
- **未披露：** 每个客户究竟获得多少 CoWoS capacity。

年度 customer revenue share、wafer revenue share 与 CoWoS customer share 也不能互换。

## 4. NVIDIA >60% CoWoS demand 是 B 级机构锚

TrendForce 对 2025 CoWoS demand 的研究将 NVIDIA 列为最大需求客户，并估计其需求占比 **超过 60%**。[^ch06-3]

这条信息很重要，但证据等级必须保持为 **B — institutional estimate**。它可以用于判断需求集中度和设计压力测试，却不能改写成：

- TSMC 官方确认 NVIDIA 拿到 >60% allocation；
- >60% 已经是 2026 actual；
- NVIDIA 拥有排他性 CoWoS 权利。

正确用法是：**高集中 demand 有现实机构锚，但真实 allocation 仍需等待一手披露。**

## 5. 5.37 CoWoS wafers/rack 是 D 级几何压力测试

本报告使用一个数量级模型：72 个 GPU package ÷ 约 13.4 packages/wafer ≈ **5.37 CoWoS wafers/rack**。其中 72 GPU 来自 NVIDIA 官方 NVL72 配置。[^ch06-4]

其中：

- 72 GPU 来自 NVL72 官方产品规格；[^ch06-4]
- ~13.4 packages/wafer 是报告侧 geometry assumption；
- 5.37 因而属于 **D 级 stress test**。

它**不是** TSMC disclosed yield、actual wafer starts、logic-wafer demand 或 customer allocation。

这一边界非常重要，因为 advanced-packaging wafer 与 TSMC 全年 12-inch-equivalent wafer shipments 并不是同一个物理池。

## 6. 为什么不能用全厂 wafer shipments 去除 5.37

TSMC 2025 全年约 **15.0M 12-inch-equivalent wafer shipments** 覆盖 smartphone、HPC、automotive、IoT、mature nodes 等大量前道产品。[^ch06-7]5.37 则是报告侧对 **CoWoS packaging wafer/rack** 的几何压力测试。

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

**Table 6.1 — Incremental packaging capacity capture 的 residual sensitivity**

| 假设捕获率 | 其他买方 residual |
|---:|---:|
| 50% | 50% |
| 60% | 40% |
| 70% | 30% |
| 80% | 20% |

**Source:** 本报告 D 级情景模型。  
**Note:** capture rate 不是 TSMC 当前客户分配事实，只用于观察新增资源集中度对 residual capacity 的敏感性。

这些 50/60/70/80% 是 **D 级 scenario levels**，不是 TSMC 当前 customer allocation。

这个模型真正说明的是非线性：头部买方如果持续获得更大比例的**新增**资源，第二、第三买方可获得的增量会迅速收缩，即使全行业总 packaging capacity 仍然在增长。

## 9. Cloud custom silicon 不会自动绕开 packaging/HBM

Google、AWS、Microsoft、Meta 的 custom accelerator system 会分流 NVIDIA platform profit，但下一代云系统本身仍大量依赖 advanced logic、HBM 与高密度 integration。

所以两个效应可以同时出现：

1. **platform substitution**：云自研降低对 NVIDIA 完整平台的依赖；
2. **upstream competition**：云自研又增加对同一先进制造、HBM 和 packaging 资源的需求。

这就是为什么“更多 custom silicon”不自动等于“CoWoS/HBM pressure 下降”。

## 10. Bottleneck location 不等于 profit location

advanced packaging 可以是系统交付的短板，但不一定拥有整个价值链最高 margin。TSMC 2Q24 的管理层表述更精确：advanced-packaging gross margin 过去显著低于 corporate average，当时正在接近但尚未达到公司平均。[^ch06-5]

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

## References

[^ch06-1]: TSMC, 4Q24 Earnings Conference Transcript, advanced packaging and testing >8% of revenue; capacity “very tight,” https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf
[^ch06-2]: TSMC, 2Q26 Earnings Conference Transcript, packaging capacity limiting customer growth, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^ch06-3]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^ch06-4]: NVIDIA, “GB200 NVL72,” official product page, 72 Blackwell GPUs per rack, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^ch06-5]: TSMC, 2Q24 Earnings Conference Transcript, advanced-packaging margin relative to corporate average, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2024-08/5122725a56670882d777a8e8bfe0ed247cc55330/TSMC%202Q24%20Transcript.pdf
[^ch06-6]: TSMC, 4Q25 Earnings Conference Transcript, corrected 2025 advanced-packaging revenue identity, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
[^ch06-7]: TSMC, 2025 Annual Report, annual wafer shipments and manufacturing footprint, https://investor.tsmc.com/static/annualReports/2025/english/index.html


\newpage


# Part I · 第7章：从 120 kW Rack 到 GW 级电力约束


## 1. 电力为什么从运营成本变成基础设施配额

当 rack-scale AI system 的整柜功耗进入约 **120 kW/rack** 量级时，电力不再只是运行费用，而开始决定系统能否按期交付和利用。[^ch07-1]

NVIDIA 官方 GB200/GB300 NVL72 级机柜文档给出约 **120 kW/rack** 的整柜功耗口径。用它做一个明确标注的 **D 级情景算术**：500 racks × 120 kW/rack = **60 MW rack-level full-load power**。

这只是数量级，不代表任何园区已经部署 500 柜，也不包含完整 facility overhead。它能说明的是：数百柜部署很快会把局部供电需求推到数十 MW 级，变电站、输电、许可、冷却和 firm power 因而进入交付链。

所以 AI 基础设施的关键物理层不只包括 wafer / HBM / advanced packaging，还包括 **powered land / grid interconnection / substation / firm MW / cooling**。

## 2. 能源分析必须使用状态机，而不是把 GW 相加

电力项目至少要区分五种状态：**Announced → Contracted → Permitted → Energized → Utilized**。

一个 1 GW PPA 不能直接写成“已有 1 GW AI compute online”；一个 500 MW 开发目标也不能直接换算成 active rack count。项目的经济价值和对 AI 供给的现实影响，取决于它从宣布向真正高利用率运行推进了多少，而不是 headline 中的最大 MW/GW。

## 3. 三条代表性路径处在完全不同的时钟

### 3.1 Microsoft / Constellation：约 835 MW 的存量核电重启

Microsoft 与 Constellation 的 **20 年 PPA** 支持原 Three Mile Island Unit 1 以 Crane Clean Energy Center 名义重启，公开机组规模约 **835 MW**。[^ch07-2]这一案例说明 hyperscaler 开始用长期需求承诺支持大型电力资产重新进入供给。

但 835 MW 是项目/机组容量锚，不是 835 MW 已经实时送达 AI 数据中心。项目仍受监管、设备修复、重启执行、并网和商业运行时钟约束。Constellation 官方稿只说重启需要 significant investments，**没有披露 US$1.6B restart CapEx**；因此该数字不进入本章事实层。

### 3.2 Talen / AWS：up to 1,920 MW 的 revised PPA

Talen/AWS revised PPA 的 full contract quantity **up to 1,920 MW**，合同延续至 2042。Talen 2026 Q2 10-Q 写明 transition to the revised AWS PPA **occurred in April 2026**；较早的 2025 10-K 又曾写 **full transition expected in spring 2027**。[^ch07-3][^ch07-4]

因此 April 2026 可以作为 revised-PPA transition 的当前披露状态，**不能被解释成全部物理转换、输电改造和 full delivery 都已经完成**。后续真正需要追踪的是 capacity ramp、energized MW、AWS load 与 utilization。

这一案例说明，监管和商业结构可以改变供电路径，但并不会让大规模 AI 用电需求自动消失。

### 3.3 Google / Kairos：2030 的 50 MWe 与 2035 的 500 MWe

Google/Kairos 的公开时钟更长：**Hermes 2 up to 50 MWe in 2030**，随后 fleet **up to 500 MWe by 2035**。[^ch07-5]这更像长期 supply option、industrial learning path 和 capacity hedge，而不是 2026–2028 可以立刻调用的现货电力。

因此，SMR 对当前 AI 扩张的价值主要在未来选择权，不应被拿来抵消眼前的 interconnection / transformer / powered-site 约束。

## 4. 三个项目不能加成“3.255 GW 已运行 AI power”

把约 835 MW、up to 1.92 GW 和 up to 500 MWe 机械相加，会得到一个名义规模，但不会得到一个可用的 AI-load 数字。

**Table 7.1 — 三类 AI 电力项目的名义规模与交付状态**

| 项目 | 名义规模 | 主要状态 |
|---|---:|---|
| Crane / Microsoft | ~835 MW | restart + regulatory process |
| Talen / AWS | up to 1,920 MW | revised-PPA transition / ramp |
| Kairos / Google | 50 MWe in 2030; up to 500 MWe by 2035 | long-duration development |

**Source:** Constellation、Talen Energy、Kairos Power / Google.[^ch07-2][^ch07-3][^ch07-4][^ch07-5]  
**Note:** 名义容量处于不同合同、许可、建设、上电与利用状态，严禁机械相加为 active AI load。

这三条路径分别代表重启既有大电源、重构大用户与既有电源的商业/电网关系、以及建设下一代先进核电供给。技术成熟度、许可时钟和可利用时间完全不同。

## 5. Grid queue 是拥堵证据，不是“AI 缺电量”

Berkeley Lab 的 Queued Up 数据显示，美国 active generation/storage interconnection queue 在 **2023 年末**接近 **2,600 GW** 的峰值；到 **2025 年末**约为 **2,061 GW**。[^ch07-6]

这个数字不能直接变成“美国缺 2,061 GW 数据中心电力”，因为 queue 主要包含 generation / storage 项目，也包括退出、重复或延迟项目。它能支持的结论更窄：**并网流程和 transmission buildout 可能跨越多年，time-to-power 是一个真实约束。**

真正与 AI system delivery 有关的，是特定区域在特定硬件代际窗口内能真正交付的 MW，而不是全国 queue 的总 GW。

## 6. Time-to-Power：新的系统竞争变量

先进芯片可以按月/季度推进新一代，电力基础设施却常以多年推进。于是出现一个与 chip roadmap 并列的竞争变量：**Time-to-Power**。

拥有 existing grid connection、powered land、substation / transformer capacity、firm generation 与 executable permitting path 的项目会获得时间优势。这意味着 hyperscaler 的竞争不仅是“谁拿到更多 accelerator”，还包括一个**示意性的部署量级问题**：谁能让下一批 50 MW / 100 MW / 500 MW 的系统更早真正上电。这里的 50 / 100 / 500 MW 是用于说明 Time-to-Power 尺度的情景量级，不是已披露项目容量。

## 7. 电力与 semiconductor bottleneck 会轮换

AI 基础设施没有一个永远固定的唯一瓶颈。一种可能的 Rolling Bottleneck Cascade 是：HBM / advanced packaging 紧张 → hardware delivery 受限 → 制造约束缓解后更多 rack 到达园区 → power / interconnection 成为下一瓶颈 → deployment rate 与 utilization 下降 → 下一轮 hardware order / commitments 增速放缓。

反过来，如果 power 大量提前建设而 workload 不足，约束会从供给不足转向低利用率与资本回报。所以“电力已经成为核心约束”与“电力尚未成为唯一主导瓶颈”可以同时成立。

## 8. Power contract 与 hardware 存在 duration mismatch

AI server 的技术和经济寿命通常短于大型电力资产与长期 PPA。Crane 对应 **20 年 PPA**，而计算硬件会更快迭代。这会产生典型 duration mismatch：**shorter-cycle compute asset vs longer-cycle power/infrastructure asset**。

在高需求情景中，长期电力是护城河；在 S4 Capital Hard Landing 中，长期 obligation 也可能变成负担。因此，评估 power contract 必须同时看 duration、ramp、take-or-pay / cancellation、project execution、utilization 与 residual value。

## 9. 什么证据会证明 power 已经成为主导瓶颈

如果未来出现多项同步信号，才可以把 power 从“核心约束之一”升级成“主导约束”：major buyers 持续明确披露 power/interconnection 是增长上限；delivered hardware 大规模等待上电；energized capacity 长期显著落后于计划；next-generation orders 因 power delay 被推迟；high-value powered sites 的 time-to-power 持续成为项目决定因素；utilization 与资本回报因电力时钟而系统性恶化。

截至 2026 年 8 月，公开事实更支持：**power 已进入与 HBM、advanced packaging 并列的核心物理约束层，但尚不足以证明它已经压倒其他瓶颈、单独决定整个 AI 基础设施扩张速度。**

## References

[^ch07-1]: NVIDIA, DGX GB200 Hardware Guide, rack power approximately 120 kW, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
[^ch07-2]: Constellation, Crane Clean Energy Center / Microsoft 20-year PPA and approximately 835 MW unit, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
[^ch07-3]: Talen Energy, 2026 Q2 Form 10-Q, revised AWS PPA transition and up to 1,920 MW, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
[^ch07-4]: Talen Energy, 2025 Form 10-K, expected full transition timing, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
[^ch07-5]: Kairos Power / Google partnership, Hermes 2 up to 50 MWe in 2030 and fleet up to 500 MWe by 2035, https://www.kairospower.com/google
[^ch07-6]: Lawrence Berkeley National Laboratory, “Queued Up” 2026 update, active interconnection queue, https://emp.lbl.gov/news/backlog-power-plants-seeking-transmission-grid-connection-eased-somewhat-2025-amidst


\newpage


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

DeepSeek-V3 Technical Report 的一手锚包括：671B total parameters、37B activated parameters、14.8T pre-training tokens、**2.664M H800 GPU-hours pre-training** 与 **2.788M H800 GPU-hours full formal training**。[^ch08-1]

DeepSeek-V2 的独立结果则包括：相对 DeepSeek 67B，约 **93.3% KV-cache reduction** 与约 **5.76× maximum generation throughput**。[^ch08-2]

这两组数字属于不同模型版本，不能混写。

它们的共同方法意义是：architecture 可以改变 bytes/token、activated compute、communication pattern 与 serving concurrency，因此会直接改变对 HBM、network 和 compute 的需求函数。

但需求函数变化不等于物理约束消失。更高效率是否减少总基础设施需求，仍取决于 workload volume 与 demand elasticity。

## 4. Formal-training compute conversion 不是完整研发成本

DeepSeek-V3 full formal training 为 **2.788M H800 GPU-hours**；论文同时使用 **US$2/GPU-hour** 的租金假设。[^ch08-1] 因此可做一项明确标注的 **D 级算术换算**：

> **2.788M × US$2 ≈ US$5.576M**

这一数字只代表该次 formal-training compute conversion，不包括 research iteration、failed runs、data engineering、engineering payroll、cluster depreciation、networking、storage 与 post-training ecosystem。

因此本书允许把 US$5.576M 用作**公开训练运行量级**，不允许把它写成“一个 frontier model 的完整企业成本”。

## 5. Rack-scale BOM 可以量化，但 rack shipment 不能凭空补齐

GB200 NVL72 官方配置为：72 Blackwell GPU、36 Grace CPU、13.4 TB HBM3E、17 TB LPDDR5X。[^ch08-3]

如果情景 rack 数为 R，则：

> **HBM(R) = 13.4 TB × R**

> **LPDDR(R) = 17 TB × R**

**Table 8.1 — NVL72 rack 数量与 HBM/LPDDR 情景需求**

| 情景 rack 数 | HBM3E | LPDDR5X |
|---:|---:|---:|
| 1,000 | 13.4 PB | 17 PB |
| 10,000 | 134 PB | 170 PB |
| 30,000 | 402 PB | 510 PB |
| 50,000 | 670 PB | 850 PB |

**Source:** NVIDIA official GB200 NVL72 specification；本报告情景算术。[^ch08-3]  
**Note:** rack count 为假设输入；表中 PB 数值不是实际出货或消费量。

这是 **D 级 scenario arithmetic**。NVIDIA 没有公开可用于这一乘算的全年 NVL72 rack shipment，因此不能先用 Data Center revenue 除一个自拟 ASP，再把假设 rack 数继续传播成 HBM、CoWoS 和 power 的“实际值”。

## 6. HBM trade ratio 会放大 bit-demand 对 wafer input 的压力

Micron FY24 Q2 prepared remarks 给出重要一手边界：在 **industrywide / same technology node / same number of bits** 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。[^ch08-4]

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

约 **120 kW/rack** 可以作为 rack-level power-density input。[^ch08-5] 以 500 racks 为情景输入，可做 **D 级算术**：500 racks × 120 kW = **60 MW rack-level full-load power**。

但这一算术不包括完整 facility overhead，也不代表某个园区已经部署 500 柜。

更重要的是，电力要区分：Announced、Contracted、Permitted、Energized、Utilized。contracted MW 不等于 energized MW，energized MW 也不等于高利用率 AI load。

因此，power quantity 与 hardware quantity 一样，必须保留状态身份。

## 9. 当 shipment 无法闭合时，Forward Commitment 比自拟出货更有价值

NVIDIA manufacturing, supply, and capacity commitments 的公开轨迹为：[^ch08-6]

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

本报告采用以下顺序：

> **official system spec → material identity → scenario demand → supply constraint → forward commitment → utilization → falsification**

而不是先设定一个宏大终局，再反向搜索数字把公式填满。

这套纪律的价值不是让所有未来判断变保守，而是允许情景大胆，同时保证事实层和物理量纲始终可审计。

## References

[^ch08-1]: DeepSeek-AI, “DeepSeek-V3 Technical Report,” https://arxiv.org/abs/2412.19437
[^ch08-2]: DeepSeek-AI, “DeepSeek-V2,” repository and technical report, https://github.com/deepseek-ai/DeepSeek-V2
[^ch08-3]: NVIDIA, “GB200 NVL72,” official product page, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^ch08-4]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^ch08-5]: NVIDIA, DGX GB200 Hardware Guide, rack power approximately 120 kW, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
[^ch08-6]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm


\newpage


# Part I · 第9章：全球半导体供应链与制造冗余


## 1. Frontier AI 背后是一条跨企业、跨国家的工业链

一套 frontier AI system 的 physical supply chain 至少涉及：

- lithography / deposition / etch / metrology equipment；
- silicon wafers 与高纯材料；
- leading-edge foundry；
- HBM；
- advanced packaging / substrates；
- testing；
- data-center power / cooling。

因此，accelerator designer 的 supply security 不是由 chip design 单独决定，而取决于多层工业能力是否同时可用。

## 2. ASML 说明设备本身也是 system-level capability

ASML 2025 Annual Report 披露全年销售 **48 台 EUV lithography systems**；其 High-NA TWINSCAN EXE 平台仍在进入高量产前的客户验证阶段。ASML 表示，到 2025 年末客户已在 High-NA systems 上运行超过 400,000 wafers，并继续推进系统向 high-volume manufacturing qualification。[^ch09-1]

这说明先进光刻的战略约束不是一个“单台机器报价”就能描述。真正重要的是：

- system availability；
- throughput；
- imaging / overlay performance；
- customer qualification；
- field service；
- optics / source / stage / metrology 的长期协同。

所以 High-NA 的关键意义是下一代 process roadmap 与工业化成熟度，而不是媒体上的单机价格。

## 3. 一座 fab 不能脱离 supplier ecosystem 独立存在

leading-edge manufacturing 依赖设备安装、备件、软件、process recipe、materials、metrology 与长期 field service。

即使两个地区都拥有厂房，如果供应商网络、工程人才、qualification cycle、tool service 与材料稳定性不同，effective capacity 也不会完全等价。

因此，本书把 supply-chain independence 定义为 **system-level continuity**，而不是“地图上有一个 fab”。

### 3.1 Upstream Continuity：设备、软件、备件和服务本身就是独立约束

“国内有 fab”也不能自动推出“扩产不再受外部供给影响”。

ASML 的公开出口管制说明给出了一个可审计边界：[^ch09-2][^ch09-3]

- EUV systems 对中国的销售已受限制；
- 最先进 immersion DUV systems 需要荷兰政府 export license；
- 2024 更新后的美国规则进一步扩大到部分 advanced semiconductor manufacturing equipment、metrology 与 software。

这支持的不是“所有中国晶圆厂都会因断供停摆”——ASML 自己也明确指出，限制针对 advanced technologies / specific fabs，其他系统并非全部受同一规则控制。

真正应该监测的是：

> **critical equipment availability + software/license + spare parts/field service + materials qualification**

这些上游变量决定新增产能能否按计划 ramp、既有产线能否长期维持 yield，以及下一代工艺能否持续迭代。

所以“存储产能扩张”与“存储供应链完全自主”也是两个不同命题。

## 4. Material Qualification 是经常被低估的时间成本

advanced node 对 contamination、particle、uniformity、defect density 与 long-term stability 极为敏感。

材料供应商替换不是普通采购切换。即便化学成分类似，也可能要求重新 qualification，并在 yield、tool recipe 与 reliability 上重新建立生产经验。

所以材料层的风险不需要一个夸张的市场份额数字才能成立。真正的约束是：

> **qualified alternative supplier 是否存在，以及切换需要多长时间。**

## 5. TSMC 的地理扩张证明“冗余正在发生”，也证明核心集群不会瞬间复制

TSMC 2025 Annual Report 显示：[^ch09-4]

- Arizona 第一座 fab 已在 **4Q24** 进入 4 nm volume production；
- 第二座 Arizona fab 计划生产 3 nm 及更先进技术；
- 2025 年第三座 Arizona fab 已开始建设，并宣布后续更多 fabs、advanced-packaging facilities 与 R&D expansion；
- 日本 Kumamoto 第一座 fab 在 2024 年末进入量产，第二座 fab 规划包含 3 nm；
- Germany Dresden 项目面向 automotive / industrial specialty technologies；
- Taiwan 仍持续建设 Hsinchu / Kaohsiung 2 nm，并继续投入 leading-edge 与 advanced-packaging facilities。

这说明 geographic diversification 是真实趋势，但不是“Taiwan cluster 一夜复制到海外”。

不同地区承担的 node、product mix、packaging、workforce、supplier density 与 power/water 条件仍不同。

## 6. 政府补贴的作用是降低冗余建设成本，而不是创造即时独立

美国 Department of Commerce 对 TSMC Arizona 的 CHIPS final award 包括 up to **US$6.6B direct funding**，支持三座 leading-edge fabs；对 advanced packaging 的 NAPMP final awards 合计 **US$1.4B**，另对 Amkor Arizona advanced-packaging/test facility 提供 up to **US$407M** direct funding。[^ch09-5][^ch09-6][^ch09-7]

这些项目直接证明：

> **战略冗余需要额外公共资本来补偿 geographic duplication、cluster formation 与早期利用率风险。**

但补贴无法立即复制 decades of yield learning、supplier qualification 与 engineering density。subsidy 可以加快 capacity formation，却不是 instant supply-chain independence。

## 7. 冗余为什么天然提高成本

更高 resilience 往往要求：

- duplicated fabs / packaging lines；
- duplicated inventories；
- spare / reserve capacity；
- regional supplier qualification；
- lower initial utilization；
- government incentives；
- additional engineering / compliance overhead。

因此，供应链可能从：

> **lowest-cost global optimization**

逐步转向：

> **higher-cost strategic redundancy**

这不是效率失败，而是安全目标改变后的成本函数变化。

## 8. AI demand 会加速这种地理重构

AI 对 leading-edge logic、HBM、packaging 与 power 的需求使先进制造从商业周期资产进一步变成战略基础设施。

TSMC 2025 年报明确把 Arizona expansion 与 strong multi-year AI-related demand 联系起来；美国 CHIPS awards 也把 AI/HPC 作为 leading-edge 与 advanced-packaging investment 的重要应用背景。[^ch09-4][^ch09-5][^ch09-6]

因此，AI infrastructure cycle 与 industrial-policy cycle 已经发生明显叠加。

## 9. Geographic Redundancy 不等于所有层都本地化

一套区域 supply stack 需要分别验证：

- equipment / service；
- materials；
- foundry；
- HBM；
- packaging / substrate；
- testing；
- power / water；
- workforce；
- customer qualification。

某一层完成本地化，只能降低该层 dependency，不能自动关闭其他层风险。

这也是为什么 China、US、EU、Japan 的“本地化率”不能用一个总百分比描述 frontier system resilience。

## 10. China localization 与 Western reshoring 本质上面对相同系统问题

中国推动 equipment、materials、foundry、memory、packaging localization，美国/欧洲/日本推动 reshoring / friend-shoring，目标方向不同，但都面对同一工程现实：

> **performance + yield + scale + qualification + cost 必须同时成立。**

单点产品存在不是 system closure；真实替代需要在生产规模、稳定性与长期 service 上达到可持续水平。

## 11. 地缘分化可能让全球总投资上升而单一体系效率下降

如果全球形成两套或多套相对独立的 semiconductor / AI system ecosystems，可能出现：

- repeated fab investment；
- repeated packaging investment；
- duplicated software/runtime；
- higher strategic inventory；
- lower cross-region fungibility；
- more policy-driven capacity。

因此，地缘 fragmentation 不一定意味着全球 semiconductor CapEx 下降，反而可能意味着**更多重复建设、较低单一体系利用效率与更高 resilience**。

## 12. 什么才叫真正的 Supply-Chain Resilience

本书不把“完全自主”设为唯一目标。更现实的指标是：

1. single-point failure 是否减少；
2. critical layer 是否存在 qualified second source；
3. disruption 后 system-level recovery 需要多久；
4. regional capacity 是否有足够 power / workforce / supplier support；
5. redundancy cost 是否仍能被最终 workload economics 覆盖。

真正的竞争不是哪个国家在所有环节完全自产，而是：

> **关键中断发生时，谁能以可接受成本维持最高的 system-level continuity。**

## 13. 当前判断

截至 2026 年，公开事实支持一个相对清晰的方向：

- core leading-edge technologies 仍高度集中；
- geographic redundancy 正在加速；
- government participation 明显提高；
- advanced packaging 已被单独列为政策与投资对象；
- 冗余提高 resilience，同时提高资本与运营成本；
- 海外 fab expansion 仍需要时间复制 supplier / workforce / packaging / infrastructure ecosystem。

因此，未来十年的半导体供应链更可能是**高集中核心技术 + 更多区域冗余 + 更高战略库存与公共资本参与**，而不是快速回到完全分散、完全可替代的全球市场。

## References

[^ch09-1]: ASML, 2025 Annual Report and Strategy & Stories, EUV / High-NA roadmap and system shipments, https://www.asml.com/en/investors/annual-report/2025
[^ch09-2]: ASML, 2023 statement on Dutch export-control regulations, EUV and advanced immersion DUV licensing, https://www.asml.com/en/news/press-releases/2023/statement-regarding-export-control-regulations-dutch-government
[^ch09-3]: ASML, 2024 statement on updated export restrictions covering additional advanced manufacturing technologies, metrology and software, https://www.asml.com/en/news/press-releases/2024/asml-expects-impact-of-updated-export-restrictions-to-fall-within-outlook-for-2025
[^ch09-4]: TSMC, 2025 Annual Report, Arizona/Japan/Germany/Taiwan manufacturing footprint and AI-related demand context, https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^ch09-5]: U.S. Department of Commerce, TSMC Arizona CHIPS final award, 2024-11, https://www.commerce.gov/news/press-releases/2024/11/biden-harris-administration-announces-chips-incentives-award-tsmc
[^ch09-6]: U.S. Department of Commerce, US$1.4B NAPMP advanced-packaging final awards, 2025-01, https://www.commerce.gov/news/press-releases/2025/01/us-department-commerce-announces-14-billion-final-awards-support-next
[^ch09-7]: U.S. Department of Commerce, Amkor Arizona advanced-packaging and test award, 2024-12, https://www.commerce.gov/news/press-releases/2024/12/biden-harris-administration-announces-chips-incentives-award-amkor
