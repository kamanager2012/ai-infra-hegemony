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


\newpage

# Part II · 第10章：模型单位经济、算法效率与开源竞争


## 1. 模型公司不是脱离基础设施的纯软件生意

API、订阅和 agent service 的底层变量成本包括 accelerator time、HBM bandwidth、KV cache、storage / retrieval、networking、third-party tools、human review、cloud margin 与 serving utilization。

因此，AI 软件无法简单沿用“新增用户几乎没有边际成本”的传统 SaaS 叙事。真正的单位是：

> **Revenue per completed workflow − total variable AI cost per completed workflow**

## 2. Algorithmic efficiency 改变的是需求函数

DeepSeek-V3 一手披露：671B total parameters、37B activated parameters、14.8T pre-training tokens、2.664M H800 GPU-hours pre-training、2.788M H800 GPU-hours full formal training。[^ch10-1]

按论文使用的 US$2/GPU-hour 假设，2.788M GPU-hours 对应约 **US$5.576M formal-training compute conversion**。这不是完整企业研发成本。

它证明的是：frontier capability 与硬件投入之间不是固定线性关系。architecture、sparsity、routing 和 memory design 可以显著改变单位 capability 所需资源。

## 3. MLA 说明 Memory Cost 可以被算法直接攻击

DeepSeek-V2 相对 DeepSeek 67B 报告约 **93.3% KV-cache reduction** 和约 **5.76× maximum generation throughput**。[^ch10-2]

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

## References

[^ch10-1]: DeepSeek-AI, “DeepSeek-V3 Technical Report,” model architecture and formal-training compute, https://arxiv.org/abs/2412.19437
[^ch10-2]: DeepSeek-AI, “DeepSeek-V2,” repository and technical report, MLA / KV-cache and throughput results, https://github.com/deepseek-ai/DeepSeek-V2


\newpage

# Part II · 第11章：NVIDIA 从 Accelerator Vendor 向 AI Factory 扩张

## 1. NVIDIA 的扩张方式不是传统 IDM 式纵向整合

NVIDIA 并不通过拥有 leading-edge fabs、HBM fabs 或整个 data-center real estate 来控制系统。

它的扩张更接近：

> **interface control + reference architecture + software/runtime + supply orchestration**

系统边界已经覆盖 GPU / CPU、NVLink / NVSwitch、networking、rack-scale design、liquid-cooling requirements、CUDA/runtime、AI Enterprise、NIM / NeMo、DGX 与 cloud-service extensions。[^ch11-1][^ch11-2][^ch11-3]

## 2. Rack-scale sales unit 会重新定义 OEM / ODM 的角色

在 accelerator-card 时代，OEM 可以围绕 GPU 定义大量 server architecture。

进入 rack-scale system 后，power delivery、cooling、fabric、cable topology、firmware、rack layout 和 software validation 被更强地绑定到 reference architecture。

这不意味着 Dell、HPE、Lenovo、ODM 等失去产品能力，而是 system-platform owner 对整机设计和 qualification 的约束增强。

## 3. Networking 已经成为 Compute Platform 的一部分

大模型 training/inference 的性能越来越依赖 multi-GPU scaling 与 collective communication。

当 accelerator、NVLink/NVSwitch、InfiniBand/Ethernet networking 与 software communication stack 被一起设计时，network 不再只是第三方附属品，而成为 system performance 与 switching cost 的组成部分。

所以平台竞争逐渐从“GPU + 任意网络”变成一套更统一的 AI Factory architecture。

## 4. DGX Cloud 的价值主要在 Platform Extension

在没有独立大规模收入分项的情况下，不应把 DGX Cloud 写成已经取代 hyperscaler 的第二主业。

更可靠的战略功能是：

1. 展示完整 NVIDIA architecture；
2. 获得真实 workload / deployment feedback；
3. 降低客户首次使用全栈系统的门槛；
4. 增加与 hyperscaler 之间的渠道与议价选择。

它更接近 platform extension 与 reference deployment channel。

## 5. AI Enterprise / NIM / NeMo 的核心作用是强化部署与迁移成本

软件产品让 system platform 从 hardware purchase 延伸到 model serving、deployment、optimization、enterprise support 与 lifecycle management。

在未披露独立软件收入之前，本书不把这些产品的贡献估算成固定“软件税”或单独利润池。

更准确的作用是：

> **降低 platform 内部部署摩擦，提高 platform 外部迁移成本。**

## 6. Asset-light Orchestration 为什么重要

NVIDIA 把大量 manufacturing CapEx 留在 TSMC、memory vendors、packaging ecosystem 与 infrastructure providers，同时用 long-term commitments、prepayments、roadmap coordination 和 volume certainty 影响这些供应商扩产。FY26 10-K 的 manufacturing, supply and capacity commitments 为这一 supply-orchestration 模式提供了公司层事实锚。[^ch11-4]

这形成典型：

> system definition / cash generation 留在平台 → 重资产扩产留在供应链 → 平台用订单和承诺锁定未来资源

它提高了平台资本效率，也把外部 supply elasticity 变成平台战略的一部分。

## 7. Physical AI 是下一层系统延伸，但不能与 Data Center 当前利润混用

Automotive、robotics、simulation 与 edge deployment 延续相同逻辑：hardware architecture、runtime、simulation、developer tooling 与 model deployment 共同形成系统。

但“战略重要”不等于“当前收入已经与 Data Center 相同”。Physical AI 的价值必须独立看 design wins、deployment scale、revenue、reliability 与 ecosystem adoption。

## 8. 纵向扩张的六个边界

NVIDIA 的系统扩张并非没有制衡：

- hyperscaler custom system stack；
- open compiler/runtime / portability；
- alternative networking；
- customer multi-sourcing；
- regulation / interface remedy；
- physical power and supply constraints；
- China parallel stack。

如果这些变量同时增强，NVIDIA 仍可能是最强 system platform，但 system definition 的议价能力会下降。

## 9. “AI Factory” 的正确含义

AI Factory 不应被当成“每个数据中心都是 NVIDIA 工厂”的所有权叙事。

更准确地说，它代表一个设计哲学：compute、memory、networking、software、rack、cooling 与 deployment 被当成统一生产系统优化。

这一思想的产业影响在于销售单位、qualification、supply commitments 与 data-center engineering 都被拉进同一个 roadmap。

## 10. 当前判断

截至 2026 年，最确定的变化是 NVIDIA 已经明显从 accelerator vendor 向 system-platform / AI-Factory architecture 扩张。

但“纵向扩张”与“产业完全被一个平台控制”仍是两个不同命题。下一阶段真正需要观察的是：system definition 能否继续转化成长期 workload、supply commitments 和低迁移成本的跨代客户留存。


## References

[^ch11-1]: NVIDIA, NIM official product page, optimized inference microservices across cloud, data center, workstation and edge, https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/
[^ch11-2]: NVIDIA, AI Foundation Models / NeMo, NVIDIA AI Foundry architecture, https://www.nvidia.com/en-us/ai-data-science/foundation-models/
[^ch11-3]: NVIDIA, “Introducing NVIDIA DGX Cloud Lepton,” unified AI platform and compute marketplace, https://developer.nvidia.com/blog/introducing-nvidia-dgx-cloud-lepton-a-unified-ai-platform-built-for-developers/
[^ch11-4]: NVIDIA Corporation, FY26 Form 10-K, U.S. SEC, Data Center, networking, platform and supply-chain disclosures, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm


\newpage

# Part II · 第12章：Hyperscaler System-Stack Competition

## 1. 竞争已经从 ASIC vs GPU 升级为 System Stack vs System Stack

把 Google TPU、AWS Trainium、Microsoft Maia、Meta MTIA 概括成“几颗 ASIC 挑战 GPU”，已经无法描述 2026 年的竞争状态。真正的竞争单位至少包含：accelerator、HBM、compiler/runtime、scale-up fabric、scale-out network、rack/pod、orchestration 与 production workload。

本书用 **Cloud System-Stack Substitution** 描述这一变化。它衡量的不是某颗芯片 benchmark，而是一套替代系统能否在真实 workload 上形成足够低的 TCO、可接受的迁移成本和稳定的大规模利用率。

## 2. Hyperscaler 的独特优势：自己就是第一批大客户

四大云与普通 chip startup 的结构差异在于，它们同时拥有：

- massive internal workload；
- data-center scale；
- compiler / software engineering；
- cloud distribution；
- capital；
- power procurement；
- custom-silicon teams。

它们不需要第一天就复制 CUDA 的整个外部 developer ecosystem。只要能在自己的大型 captive workload 上持续降低成本，就能产生真实经济价值，并通过生产反馈迭代 compiler、interconnect、rack 与 deployment tooling。

这也是 cloud custom silicon 最强的学习飞轮：**internal workload → production feedback → system optimization → lower TCO → more internal workload**。

## 3. Google：TPU 已经是芯片、软件、互联和 Pod 的组合

Google 的 TPU 路线已经跨越多代。Ironwood 继续把产品定义上移到大规模 pod / system：[^ch12-1]自研 accelerator 与 XLA/software、high-bandwidth interconnect、HBM 和 Google Cloud workload 共同形成完整栈。

所以 Google 的竞争力不是“一颗 TPU 比一颗 GPU 快多少”，而是：

> **TPU + compiler/runtime + network + pod + captive workload + cloud distribution**。

如果这套系统在特定 training/inference workload 上持续降低 total cost of ownership，它就可以分流 NVIDIA platform profit，即使它没有成为全行业通用开发平台。

## 4. AWS：Trainium 把芯片、Neuron 与 UltraServer 组合成系统

AWS Trainium 同样已经从 accelerator 向 system 发展。Trainium3 UltraServers、Neuron software stack、AWS networking/data-center deployment 与大规模 cloud workload 共同构成第二类系统。[^ch12-2]

其战略优势还包括长期 anchor workload。Anthropic 已公开深化与 AWS 的长期 compute relationship，[^ch12-3]这使 Trainium 不只是实验性 silicon，而拥有持续迭代 system economics 的大客户基础。

但“有 anchor workload”不等于已经取代 NVIDIA 外部生态。真正需要验证的是 large-cluster scaling、utilization、software maturity、迁移成本以及外部客户采用。

## 5. Microsoft：Maia 的价值取决于 Azure 内部规模化，而不是复制整个 CUDA

Microsoft Maia 200 的合理评价标准不是“是否第一天支持所有模型”，[^ch12-4]而是它能否在 Azure / Microsoft 内部足够大的 workload 上形成稳定成本优势。

长期竞争力取决于：

- compiler/runtime maturity；
- scale-up / scale-out capability；
- HBM configuration 与 supply；
- rack/data-center integration；
- high utilization；
- broader Azure deployment。

只要这些变量在足够大的内部 workload 上成立，Maia 就可以分流外购 platform economics；要进一步变成通用外部替代，则还需要更低 migration cost 与更广 ecosystem。

## 6. Meta：MTIA 证明“窄 workload 先优化”也是有效路径

Meta 拥有超大 recommendation、ranking 与 generative-AI workload。MTIA 300 的逻辑不是先成为 general-purpose accelerator，[^ch12-5]而是围绕最重要的内部 workload 做 specialization，并把 silicon、software、networking 与 rack deployment 逐步组织成 custom full-stack solution。

这条路线的经济目标是：

> **让自己的最大 workload 获得更低的长期 TCO。**

它不需要在所有 workload 上击败通用 GPU 才能产生价值。

## 7. Cloud custom system 对 NVIDIA 会产生两个同时存在的效应

### 7.1 Platform-profit diversion

自研系统可以减少部分外购 accelerator、降低对外部 software/platform 的依赖、增强采购议价，并把更多 economics 留在 cloud platform 内部。

### 7.2 Upstream resource competition

但下一代 custom system 仍需要先进逻辑、HBM、advanced packaging、networking 和 power。因此，自研系统的扩张又可能增加对与 NVIDIA 相同 upstream scarce resources 的竞争。

所以：

> **Cloud custom silicon 可以同时削弱 NVIDIA 平台利润，并强化 TSMC / HBM / packaging / power 的资源竞争。**

这两个效应并不矛盾。

## 8. Cloud CapEx 不是 NVIDIA revenue 的同义词

hyperscaler CapEx 同时覆盖 custom silicon、外购 accelerator、network、memory、data center、power、办公/履约等不同资产。各公司财年、PPE 与 lease accounting 也不同。

因此：

> **Cloud CapEx ≠ AI hardware subtotal ≠ NVIDIA purchases**

CapEx 上升既可能支持 NVIDIA 出货，也可能加速 NVIDIA 的替代系统。不能把四云资本开支与 NVIDIA revenue 直接对敲成一个“算力税率”。

## 9. DeepSeek 代表另一种竞争：公共算法降本

Cloud custom silicon 属于**私有降本**：Google、AWS、Microsoft 或 Meta 优化自己的 system economics，收益主要留在自己的平台内。

DeepSeek 所代表的算法/架构效率则更接近**公共降本**：如果一种架构显著降低训练或 serving 的 compute/memory requirement，其他开发者也可能采用类似方法，从而改变整个市场的单位智能成本。

DeepSeek-V3 Technical Report 的可核一手锚是：671B total parameters、37B activated parameters、14.8T pre-training tokens；pre-training **2.664M H800 GPU-hours**，完整正式训练 **2.788M H800 GPU-hours**。[^ch12-6]按论文采用的 US$2/GPU-hour 假设，**US$5.576M 对应完整正式训练 compute conversion**，不代表完整 R&D cost。

另一条独立证据来自 DeepSeek-V2：相对 DeepSeek 67B，报告 **93.3% KV-cache reduction** 与 **5.76× maximum generation throughput**。[^ch12-7]V2 与 V3 不能拼成同一个模型的单一结果。

## 10. 算法降本不会自动把基础设施需求清零

architecture efficiency 可以降低 bytes/token、training compute 或 serving cost，但总 infrastructure demand 仍取决于 demand elasticity：单位成本下降之后，新的 workload 是否增长得更快。

因此，DeepSeek 式效率提升对 hyperscaler 有双重影响：

- 可能降低同一 workload 需要的硬件；
- 也可能因为更低价格和更广应用刺激更大 token/workflow volume。

正确问题不是“效率提高，所以 CapEx 应该下降”，而是：**单位 workload 成本下降后，总有效 workload、利用率和收入能否覆盖已经形成的资本基数。**

## 11. 什么情况下才算 System-Stack Substitution 真正成立

单颗芯片 benchmark 不够。至少需要同时观察：

1. compiler/runtime mature；
2. large-cluster scaling；
3. high utilization；
4. workload migration cost acceptable；
5. HBM / packaging / power supply 可持续；
6. rack/pod deployment 稳定；
7. significant real workload share。

内部 workload 上的成功可以形成真实经济价值，但“全面替代 NVIDIA 外部生态”还需要证明跨客户、跨 workload 的迁移与 production reliability。

## 12. 长期均衡更可能是 Workload Segmentation

最现实的长期格局未必是一方完全消灭另一方，而更可能形成 workload segmentation：

**NVIDIA 更强的区域：** general-purpose frontier training、broad external developer ecosystem、heterogeneous enterprise workload。

**Hyperscaler custom stack 更强的区域：** massive internal workload、repeatable architecture、vertically optimized inference/training、cloud-specific TCO optimization。

边界会随着 software maturity、interconnect、memory supply、workload structure 和迁移成本不断移动。

## 13. 当前判断

截至 2026 年 8 月，最稳健的描述是：

- cloud custom silicon 已经成为实质竞争力量；
- 竞争单位已经从自研芯片上移到完整 system stack；
- hyperscaler 已经开始攻击 software、interconnect、rack/pod 与 workload 层，而不是只攻击 accelerator die；
- frontier training 与广泛外部生态仍未证明已经系统性脱离 NVIDIA；
- custom system 仍大量竞争 advanced logic、HBM、advanced packaging 与 power。

因此，**Cloud System-Stack Substitution 是最可能把 S2 Baseline Concentration 推向 S1 Competitive Expansion 的结构变量之一**，但它的强度必须用真实 workload share、迁移成本、利用率和上游资源依赖来衡量。

## References

[^ch12-1]: Google Cloud, “Ironwood TPU,” https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/
[^ch12-2]: Amazon Web Services, “Amazon EC2 Trn3 UltraServers,” https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/
[^ch12-3]: Anthropic, “Anthropic and Amazon expand collaboration,” long-duration AWS compute commitment, https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
[^ch12-4]: Microsoft, “Maia 200: the AI accelerator built for inference,” 2026-01-26, https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/
[^ch12-5]: Meta Engineering, “MTIA 300,” 2026-08-24, https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
[^ch12-6]: DeepSeek-AI, “DeepSeek-V3 Technical Report,” https://arxiv.org/abs/2412.19437
[^ch12-7]: DeepSeek-AI, “DeepSeek-V2,” repository and technical report, https://github.com/deepseek-ai/DeepSeek-V2


\newpage

# Part II · 第13章：Anchor Compute Buyer Effect——模型公司如何重塑基础设施

## 1. 模型公司正在从“算力租户”升级为 Infrastructure Anchor Buyer

传统关系是：

> model company → rent cloud compute

超大模型公司正在把关系改成：

> **model-company demand ↔ cloud / data-center / power buildout**

它们通过 multi-year compute commitments、dedicated campuses、chip selection 与 capacity reservation 给基础设施供应商更高 revenue visibility。

## 2. Anchor Compute Buyer Effect

机制可以写成：

> **long-duration model demand → infrastructure financing certainty → earlier data-center/power buildout → earlier chip/HBM/packaging reservation → priority capacity for anchor workload**

所以模型公司本身已经成为上游资本形成的重要需求信号，而不是仅仅接受 hyperscaler 的投资结果。

## 3. OpenAI Stargate：从 nominal commitment 到 secured / construction state

OpenAI 在 2025-01 宣布 Stargate，计划未来四年在美国投资 **US$500B** 建设 AI infrastructure。[^ch13-1]

随后官方把长期目标描述为到 2029 年确保 **10 GW** 美国 AI infrastructure。[^ch13-2]

状态继续前移：OpenAI 在 **2026-04-29** 表示已**超过 10 GW secured-capacity milestone**，并称此前 90 天新增超过 3 GW；[^ch13-2] **2026-06-01**，Michigan 的 **1 GW The Barn** data-center campus 正式破土。[^ch13-3]

这些状态必须区分：commitment / secured capacity / construction / energized capacity / utilization。超过 10 GW secured 不等于 10 GW 已全部上电运行。

## 4. Anthropic / AWS：Anchor Workload 也能推动 Custom Silicon

Anthropic 在 2026-04 官方披露：[^ch13-4]

- 对 AWS technologies 的未来十年 commitment **>US$100B**；
- 可获得 **up to 5 GW** capacity；
- 已使用 **>1M Trainium2 chips**；
- 到 2026 年底预计接近 **1 GW Trainium2/3 capacity**。

这说明 model-company demand 可以成为 cloud custom silicon 的重要 anchor workload。

但公开披露只能证明规模大，不能在缺乏 workload-share 排名时写成“第一大用户”。

## 5. Anchor Buyer 增强的是需求侧权力，不是物理所有权

模型公司可以影响：

- demand certainty；
- chip / system selection；
- cloud roadmap；
- rack deployment；
- power planning；
- infrastructure financing。

但通常并不直接拥有 leading-edge foundry、HBM fab、advanced-packaging fab 或 transmission grid。

所以 Anchor Buyer 是需求侧 bargaining / coordination power 的上升，而不是完整 supply-chain ownership。

## 6. 为什么换云不是简单换账单

模型公司选择的是 accelerator、HBM、interconnect、compiler/runtime、scheduler、rack/pod 与 cloud operations 的完整 system。

迁移可能需要 kernel adaptation、distributed-training changes、performance tuning、observability rework 与 operational revalidation。

这形成 infrastructure switching cost，也解释了为什么长期 commitment 的退出成本可能高于普通 SaaS contract。

## 7. Algorithmic Efficiency 会直接改变 Anchor Demand

如果 architecture 大幅降低同一 capability 的 compute requirement，model company 可以减少长期 capacity commitment，提高 buyer bargaining power，并提高 infrastructure provider 的 utilization risk。

如果 unit cost 下降反而刺激 workload volume 更快增长，长期 commitment 仍可能继续扩大。

所以 Anchor Buyer Demand 是动态需求函数，不是固定指数增长曲线。

## 8. Anchor Buyer 的产业链传导

大规模模型需求可以沿链条传播：

> model demand → cloud CapEx / custom silicon → accelerator/HBM/packaging → data-center power → grid/generation

因此，评估 AI infrastructure cycle 不能只看 hyperscaler CapEx 和 system-vendor commitments，还要独立看 model-company long-duration contracts 是否扩张、改期或利用不足。

## 9. 风险：Anchor Buyer 也会放大 Stranded-Capacity Risk

如果 model-company revenue、financing、workload growth 或 architecture assumptions 发生逆转，long-duration infrastructure commitments 可能变成低利用率资产。

需要持续观察：

- cancellation / rescheduling；
- take-or-pay / minimum commitments；
- utilization；
- project financing；
- customer concentration；
- power and data-center delivery state。

## 10. 当前判断

截至 2026 年 8 月，模型公司已经成为 AI infrastructure 的独立 Anchor Buyer category。

OpenAI Stargate 的 secured-capacity 与 construction 状态、Anthropic/AWS 的十年 compute commitment 和 Trainium deployment 都说明：模型 workload 正在影响 data-center、power 与 custom-silicon buildout。

这使 Anchor Buyer commitments 成为 S2/S3 expansion 与 S4 capital clearing 之间的重要 leading indicator。

## References

[^ch13-1]: OpenAI, “Announcing The Stargate Project,” 2025-01, https://openai.com/index/announcing-the-stargate-project/
[^ch13-2]: OpenAI, “Building the compute infrastructure for the Intelligence Age,” 2026-04-29, surpassed 10 GW secured-capacity milestone, https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/
[^ch13-3]: OpenAI, “Stargate Michigan Data Center,” 2026-06-01, 1 GW The Barn campus groundbreaking, https://openai.com/index/stargate-michigan-data-center/
[^ch13-4]: Anthropic, “Anthropic and Amazon expand collaboration,” 2026-04, >US$100B over ten years, up to 5 GW and >1M Trainium2 chips, https://www.anthropic.com/news/anthropic-amazon-compute?lang=us


\newpage

# Part II · 第14章：Agent-native Software 与 AI Software Unit Economics

## 1. Agent-native Software 改写的是成本结构

传统 SaaS 的典型特征是 software replication cost 低、seat 增长不一定线性增加 variable compute。

Agent-native software 不同。一次任务可能触发 retrieval、reasoning、multiple model calls、tool invocation、browser/action execution、retry 与 human review。

于是软件成本单位从：

> **account / seat**

逐渐上移到：

> **workflow execution**

## 2. 不存在统一的“AI SaaS 毛利率终点”

不同 agent 产品的 variable cost 取决于 model choice、context length、cache、retrieval、tool/API、failure/retry、human review、pricing model 与 task depth。

因此，本书不使用“传统 SaaS 85% → AI SaaS 55%”这类固定路径作为事实。

统一使用 **AI Software Unit Economics**。

## 3. 核心单位经济公式

生产级 workflow 可以近似写成：

> **Contribution Margin = Revenue / Productivity Value per workflow − Variable AI cost − Tools/APIs − Human review**

Variable AI cost 至少包括：

- inference；
- retrieval / storage；
- model routing；
- retry；
- observability；
- failure handling。

真正要优化的是 **cost per successfully completed workflow**，而不是单纯 cost per token。

## 4. Agent Depth 决定成本曲线

浅层 assistant 可能是 single prompt → single response。

深层 agent 更接近：plan → retrieve → reason → tool call → inspect → retry → finalize。

loop depth 增加时，compute、tool usage 和 failure surface 一起上升。因此 agent 产品必须同时优化：

- task success；
- loop length；
- model routing；
- caching；
- tool reliability；
- failure / retry rate。

## 5. Seat Pricing 为什么会受到挑战

如果产品主要提供 summary、autocomplete 或 shallow assistant，seat pricing 仍然可行。

如果一个 seat 可以运行 research、coding、support、sales、operations 等大量不同深度 workflow，compute variance 会显著扩大。

因此更常见的长期定价组合可能是 usage、credits、workflow、outcome 或 hybrid pricing。

这不是说 seat pricing 会消失，而是 agent depth 会让纯 seat 与真实 variable cost 的相关性下降。

## 6. Multi-model Routing 是新的基础软件能力

所有任务都调用最昂贵模型会直接破坏 unit economics。

更合理的 system design 是：

- cheap / local model：classification、extraction、high-volume routine work；
- medium model：routine reasoning；
- frontier model：复杂任务与高不确定决策；
- specialist/custom model：稳定专业 workload。

routing 本质上是在质量、latency、cost 和 failure probability 之间动态分配资源。

## 7. Open Source 会把利润从“模型能力”推向 Workflow / Distribution

open-source model 提高 model portability，压低 API premium，也增加 private deployment 与 buyer bargaining power。

因此，model capability 本身越来越难成为永久软件 margin。

更稳定的价值来源可能转向：

- proprietary workflow；
- domain data / context；
- distribution；
- integration；
- trust / compliance；
- measurable outcome。

## 8. Cloud System-Stack Competition 会向 Application 成本传导

软件公司通常不会直接购买 HBM、CoWoS 或 grid capacity，但 cloud price 最终包含 accelerator、memory、network、data center 与 power。

如果 hyperscaler custom stack 能降低真实 system TCO，长期可能通过 instance/API price 向 application layer 传导。

因此，Google Ironwood TPU、AWS Trainium3 等基础设施竞争不仅是芯片行业问题，也会影响 software contribution margin。[^ch14-1][^ch14-2]

## 9. Human Review 是经常被低估的变量成本

在 legal、finance、enterprise operations 等高风险 workflow 中，human review 可能长期存在。

如果 agent 生成速度提高 10×，但 review burden 不下降，企业只是把人工从 production 移到 verification。

真实 automation ROI 应计算：

> **Human time before − Human time after − new review / exception handling time**

而不是只统计 AI usage 或 generated tokens。

## 10. Agent-native Software 的高质量利润来自哪里

长期更有机会形成高质量 economics 的产品通常具备：

- high workflow completion；
- low variable AI cost；
- low retry / review burden；
- strong proprietary context；
- distribution；
- measurable customer ROI；
- ability to route across models / providers。

这意味着 software competition 正从 feature competition 上移到 **workflow economics competition**。

## 11. 当前判断

AI 正在把一部分 software 从低边际成本复制品变成实时消耗 compute 的工作流系统。

这会压缩部分传统软件利润，但不会自动把整个软件行业变成低毛利。

真正的分水岭是：

> **谁能把模型调用转化成可重复、可验收、低失败率、可收费的业务结果。**

## References

[^ch14-1]: Google Cloud, “Ironwood TPU,” https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/
[^ch14-2]: Amazon Web Services, “Amazon EC2 Trn3 UltraServers,” https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/

## 交叉引用

- 第10章：模型单位经济、算法效率与开源竞争
- 第12章：Hyperscaler System-Stack Competition
- 第20章：Value Capture Map
- 第25章：AI 与劳动市场


\newpage

# Part II · 第15章：Physical AI 与机器人系统的真正瓶颈

## 1. 机器人竞争单位同样是 System

Physical AI 需要同时解决 perception、planning、control、actuation、power、safety 与 mechanical reliability。

所以一台机器人能否形成生产力，不能只由 AI model 或 edge TOPS 判断。

完整系统至少要把：

> **model capability × sensor quality × control latency × actuator reliability × energy efficiency × manufacturing economics**

同时闭合。

## 2. Cloud Training 与 Edge Control 是两套物理约束

large-scale simulation、policy training 与 foundation-model training 可以在 data center 完成。

实时 control 则受到 latency、thermal、battery、sensor loop 与 safety deadline 约束。

所以很多 Physical AI 系统天然呈现：

> **cloud-side heavy training + edge-side compressed inference/control**

data-center 的约 **120 kW-class rack**[^ch15-4] 与机器人本体的 W/Wh 级 power budget 属于完全不同的物理池。

## 3. Robot BOM 不能套统一百分比模板

humanoid、AMR、industrial arm、autonomous vehicle、drone 的 actuator、reducer、sensor、compute 与 battery 成本结构差异巨大。

因此，本书不采用固定“执行器35% / 传感器20% / 计算25%”之类行业模板。

真正需要识别的是不同机器人形态中的 **scarce component**。

## 4. Actuator / Reducer 可能比 Compute 更难商品化

Physical AI 最容易被软件叙事低估的，是 frameless torque motor、harmonic reducer、planetary roller screw、bearing 与 precision gearbox 等机械部件。

它们的竞争变量包括 durability、backlash、repeatability、noise、yield、maintenance 与 cost。

于是完全可能出现：

> **compute 更便宜，但高精度机械部件仍是系统瓶颈。**

## 5. Sensor Quality 决定模型能否转化成可靠 Control

robot system 需要 camera、depth、force/torque、tactile、IMU、encoder 等多种 sensing。

模型能力只有在 calibration、latency、robustness 与 failure detection 足够好时，才能转化成稳定 control。

因此 sensor stack 的价值不只是 BOM，而是 closed-loop reliability。

## 6. Edge Platform 的战略位置

NVIDIA Jetson Thor、Qualcomm 与其他 edge accelerators 的竞争维度是 compute、software、power efficiency 与 developer ecosystem。NVIDIA Isaac/GR00T 将 simulation/training、robot model 与 Jetson Thor onboard compute 组织成跨 cloud-to-edge workflow。[^ch15-1][^ch15-2]

edge system 不需要复制 data-center rack architecture。

但如果同一平台同时覆盖 cloud training / simulation / edge deployment，就可能形成 cloud-to-robot 的跨层 ecosystem lock-in。

## 7. Physical Deployment 会反向制造更多 Cloud Workload

即使单台 robot 的 edge compute 很有限，大规模 fleet 会持续产生：

- video / sensor data；
- simulation；
- retraining；
- synthetic data；
- fleet analytics；
- model updates。

因此可形成：

> **physical deployment → data generation → retraining → more cloud compute**

机器人普及不一定减少 data-center demand，反而可能扩大新的训练/推理 workload。

### 7.1 机器人本体也可能成为新的 Memory / Storage Demand Pool

Micron 在 2026-06-24 investor presentation 中给出一个值得跟踪、但必须保留“公司前瞻判断”身份的量化锚：[^ch15-3]

- L2+ 及以上车辆的 memory + storage content 已超过 average vehicle 的 **5×**；
- Micron 称 humanoid robots 的 memory content 约为 average L2+ vehicle 的 **10×**；
- 公司预计本十年后段开始形成持续、多十年的 robotics memory demand cycle。

这不是全行业 actual shipment，也不是“每台机器人固定需要数百 GB DRAM + 数 TB SSD”的统一规格。

它真正支持的机制是：

> **Physical AI commercial scale ↑ → edge memory/storage content ↑ + fleet-generated cloud workload ↑**

所以机器人可能同时成为 edge memory 的新需求池和 cloud retraining / storage 的新需求源。

## 8. 机器人侧的 Power Wall 是 Battery / Thermal

data center 的 power bottleneck 是 grid / interconnection；机器人侧则是 battery energy density、runtime、charging、thermal 与 peak actuator demand。作为量纲对照，NVIDIA DGX GB200 rack 的官方功耗约为 120 kW，但该数据只用于说明 cloud 与 edge 属于不同物理池。[^ch15-4]

因此 Physical AI 应比较：

> **Useful task output / Wh**

以及 continuous runtime、recharge time、thermal headroom、maintenance interval 与 field reliability，而不是只比较 TOPS。

## 9. Demo 到 Mass Production 的真正门槛是 Manufacturing

demo 可以容忍 expensive parts、manual calibration、low yield 和 frequent maintenance。

mass production 不行。

规模化临界点包括 component yield、assembly time、field failure rate、maintenance interval、supply-chain stability 与 unit economics。

因此 Physical AI 的产业拐点必须由 manufacturing / deployment data 证明，而不能由演示视频证明。

## 10. 中国在 Physical AI 上的能力结构与 Frontier AI 不同

Physical AI 大量依赖 motors、battery、sensors、manufacturing、consumer-electronics supply chain 与 system integration。

这些层与 frontier AI 的 HBM / advanced-packaging / leading-edge compute 闭环并不完全重合。

所以中国在机器人整机和机械供应链上的竞争力，可以与其在 frontier AI infrastructure advanced layers 的状态不同。

这是独立产业路径，不应被一个“AI 芯片能力”指标覆盖。

## 11. Value Capture 可能分布在多个物理层

长期 value capture 可能同时出现在：

- edge compute / software platform；
- actuator / reducer；
- sensor；
- battery / power electronics；
- manufacturing / integration；
- cloud simulation / training infrastructure。

机器人革命的真正竞争不是“谁模型 benchmark 最好”，而是：

> **谁能把 AI capability 转化成可靠、低成本、可量产、可维护的物理工作。**

## References

[^ch15-1]: NVIDIA Developer, Isaac platform, simulation/training and robotics workflow, https://developer.nvidia.com/isaac
[^ch15-2]: NVIDIA, 2026-06, Isaac GR00T Reference Humanoid Robot, Jetson Thor onboard compute and Isaac GR00T platform, https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design
[^ch15-3]: Micron Technology, investor presentation, 2026-06-24, humanoid-robot memory-content outlook, https://s25.q4cdn.com/621799436/files/doc_financials/2026/q3/Micron_Q3_26_Earnings_Deck.pdf
[^ch15-4]: NVIDIA, DGX GB200 Hardware Guide, rack power approximately 120 kW, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html


\newpage

# Part II · 第16章：AMD、Intel、Qualcomm 与 Apple 的差异化竞争路径

## 1. 不能把四家公司放进一个“传统芯片阵营”

AMD、Intel、Qualcomm、Apple 的 compute layer、software、manufacturing access、workload、distribution 与 capital structure 都不同。

因此，正确问题不是谁“联合挑战 NVIDIA”，而是：

> **每家公司正在攻击 system-stack dominance 的哪一个层级？**

## 2. AMD：最直接的 Data Center System Challenger

AMD Instinct 是最直接的 data-center accelerator alternatives 之一，AMD 当前官方路线也已把 Instinct GPU、EPYC CPU、Pensando networking 与 ROCm 组织为 rack/system 级解决方案。[^ch16-1][^ch16-2]

真正的门槛不只是 GPU design，而是：

- ROCm / software maturity；
- scale-up / scale-out；
- HBM；
- advanced packaging；
- system reference architecture；
- customer migration / production support。

因此 AMD 的竞争单位也已经从 chip 上移到 system。

## 3. AMD 同样暴露于 Scarce-resource Access

AMD 与 NVIDIA 会竞争相同的 advanced logic、HBM 与 packaging。

所以 NVIDIA demand 极强时，AMD 的挑战不仅是 market share，也包括 incremental scarce capacity access。

反过来，如果 HBM/packaging supply elasticity 提高，AMD system expansion 的约束会下降。

这使 AMD 成为观察 **non-anchor-buyer access / Non-AI-and-non-leading residual capacity** 的重要对象，但本书不为它另造新的核心术语。

## 4. Intel：Product Clock 与 Foundry Clock 是两条时间线

Intel 同时承担 CPU/product competition、accelerator attempts、foundry strategy 与 domestic manufacturing policy。Intel 2025 10-K 与 2026 VLSI Symposium 更新显示 Intel Foundry 仍在推进 external-foundry strategy，18A 已进入 production、18A-P 进入 risk production。[^ch16-3][^ch16-4]

Product clock 需要在短周期交付 performance、software 与 customer adoption；foundry clock 则需要长期建立 process、yield、customer trust、packaging 与 high-volume execution。

因此，Intel 的复苏不能由一颗产品或一座 fab 单独证明。

## 5. Qualcomm：从 Edge 改写 Cloud Demand

Qualcomm 的相对优势更接近 smartphone、PC、edge AI、low-power compute 与 connectivity；公司 2026 年公开材料继续强调 Snapdragon X Series PC 上的本地 agentic AI 与 mobile on-device generative AI。[^ch16-5][^ch16-6]

它不需要复制 NVL72 才能获取 AI value。

如果 on-device model capability、memory efficiency 与 local inference 持续提高，更多 workload 可以从 cloud 移到 device，降低一部分 cloud inference demand。

因此 Qualcomm 对 AI infrastructure 的影响主要是**需求函数重构**，而不是直接替代 frontier training system。

## 6. Apple：Vertical Consumer Stack 的力量在 Workload Placement

Apple 的 silicon、OS、device、application ecosystem、distribution 与 installed base 高度垂直。Apple Intelligence 的公开架构同时使用 on-device processing 与 Private Cloud Compute，说明 workload placement 本身就是其 AI system design 的核心。[^ch16-7][^ch16-8]

Apple 不是 frontier training system vendor，但它可以决定大量 consumer workload：哪些在 device 完成，哪些调用 private / public cloud。

如果端侧 capability 快速提高，Apple 会成为影响 cloud inference intensity 的重要平台变量。

## 7. Apple 是 Leading-edge User，但不制造未经披露的客户排名

Apple 长期使用 leading-edge processes，但在没有公司一手客户份额/排名披露时，本书不把某一具体年份的“第一/第二大客户”身份作为事实。

真正要看的是：leading-node launch scale 是否保持、AI/HPC 对 incremental capacity 的吸收是否加速，以及 device-AI strategy 是否改变 wafer / memory mix。

这再次说明 historical revenue share 不能替代 AHICR。

## 8. 四家公司对主栈的影响来自不同方向

**Table 16.1 — 四类差异化竞争路径**

| 公司 | 主要竞争方向 |
|---|---|
| AMD | Data Center accelerator / system |
| Intel | CPU + accelerator + foundry |
| Qualcomm | edge / PC / mobile AI |
| Apple | vertically integrated on-device AI / workload placement |

**Source:** AMD、Intel、Qualcomm、Apple 官方产品与公司材料。[^ch16-1][^ch16-3][^ch16-5][^ch16-7]  
**Note:** 表中为竞争路径分类，不表示四家公司处于相同市场或拥有可直接比较的 market share。

NVIDIA 面对的是多层侵蚀，而不是一个统一对手。

## 9. 哪些变化会提高 S1 Competitive Expansion 的权重

- AMD 在 production system stack 上规模化；
- Intel foundry 与 product execution 同时改善，增加 manufacturing/system diversity；
- Qualcomm / Apple 推动更多 high-volume inference 移到 edge；
- open software / interfaces 降低 migration cost；
- HBM / packaging supply 更宽松。

这些变化可以共同提高 S1 相对 S2 的权重，但 S1/S2 是并列条件情景，不是必然连续阶段。

## 10. 当前判断

传统芯片巨头没有消失，也没有形成统一联盟。

更现实的格局是：AMD 从 data-center system 正面竞争；Intel 同时修复 product 与 manufacturing；Qualcomm/Apple 从 edge / device 改写一部分需求。

它们是否真正削弱 dominant system-stack economics，最终要看 production workload share、software portability、scarce-resource access 与 customer migration，而不是产品发布数量。

## References

[^ch16-1]: AMD, Instinct / Helios official page, rack-scale solution integrating Instinct GPUs, EPYC CPUs, Pensando networking and ROCm, https://www.amd.com/en/products/accelerators/instinct.html
[^ch16-2]: AMD, “ROCm 10: A Simpler Path to Production AI on AMD,” 2026-08-27, https://www.amd.com/en/blogs/2026/amd-rocm-10-a-simpler-path-to-production-ai-on-amd.html
[^ch16-3]: Intel Corporation, 2025 Form 10-K, Intel Foundry and manufacturing strategy, https://www.intc.com/filings-reports/all-sec-filings/content/0000050863-26-000011/intc-20251227.htm
[^ch16-4]: Intel Foundry, 2026-06 VLSI Symposium process milestones, 18A production and 18A-P risk production, https://newsroom.intel.com/intel-foundry/intel-foundry-details-process-milestones-future-innovation-at-vlsi-symposium
[^ch16-5]: Qualcomm, 2026-08, agentic AI applications on Snapdragon X Series PCs, https://www.qualcomm.com/news/onq/2026/08/agentic-ai-apps-snapdragon-x-series
[^ch16-6]: Qualcomm, Mobile AI / on-device generative AI, https://www.qualcomm.com/smartphones/features/mobile-ai
[^ch16-7]: Apple, Apple Intelligence, on-device processing and Private Cloud Compute, https://www.apple.com/apple-intelligence/
[^ch16-8]: Apple Security Research, Private Cloud Compute security documentation, https://security.apple.com/documentation/private-cloud-compute/


\newpage

# Part II · 第17章：中国 Parallel Stack：从产品替代到 Frontier System Closure

## 1. “能运行”与“形成等价系统”不是同一个标准

讨论中国 AI stack，如果不先区分层级，结论会迅速失真。至少需要分成三层：

1. **smartphone / consumer computing**；
2. **PC / workstation / general computing**；
3. **frontier AI system stack**。

三层对 advanced logic、memory、packaging、software、interconnect 与 performance requirement 的要求完全不同。中国在 smartphone supply chain 上形成较强能力，不能自动外推为 frontier training system 已经闭环；反过来，frontier AI 的约束也不能被写成“中国半导体没有替代能力”。

真正需要回答的是：一套系统能否在 **functional availability、performance、scale、software portability、supply sustainability 和 economics** 六个维度同时达到生产级可接受水平。

## 2. 第一层：消费计算最容易形成平行供给

smartphone 与部分 consumer computing 更容易形成完整国内链条，因为这一层可以依托本土 SoC、foundry、LPDDR/NAND、packaging、device manufacturing、operating system/application ecosystem 与大型国内需求。

TSMC 2025 platform mix 仍显示 smartphone 占全年 platform revenue **29%**，而 HPC 为 **58%**。[^ch17-1]这说明消费计算仍是重要市场，但 frontier AI 与 smartphone 已经在同一先进制造体系中竞争不同资源。

### 2.1 “只有华为能规模量产国产手机 SoC”已经不符合 2026 的公开数据

Counterpoint Research 的 2026Q1 global smartphone AP-SoC shipment share 显示：[^ch17-2]

- UNISOC：**14%**；
- HiSilicon：**4%**。

因此，如果“规模”按实际 smartphone SoC shipment 口径衡量，国产供应并不只有华为一家。

Huawei / HiSilicon 的独特优势更适合描述为：**高端自有终端 + 自研 SoC + 自有软件/生态的 vertical closed loop 更成熟**，而不是“唯一有量”。

Xiaomi 也已经跨过纯 demo 阶段。Xinhua 2025-05 报道 XRing O1 已进入 mass production 并搭载 Xiaomi 15S Pro / Pad 7 Ultra；[^ch17-3] Reuters 2026-08 又报道 O1 已覆盖 **超过 1M devices**，新一代 O3 继续采用 TSMC 3 nm，首发产品预计 200k–300k units。[^ch17-4]

这意味着“Xiaomi 只有20–30万片边角料、只是品牌秀”不能作为事实层。更准确的判断是：

> **Xiaomi 已经形成真实量产，但 multi-generation scale、modem/system integration、foundry dependency 与长期 shipment share 仍需要继续验证。**

UNISOC 则代表另一种 commercial loop：它在大众/入门与 entry-5G 市场拥有更大的 shipment scale，但不能据此外推为 premium flagship system equivalence。

因此，消费端的平行供给能力应被评价为一个独立层级，而不是拿来证明或否定 frontier AI closure。

## 3. 第二层：PC / workstation 的难点更多在软件兼容与性能规模

PC、workstation 与 general computing 需要同时解决 CPU/GPU、DDR5、专业软件、driver/tooling、desktop ecosystem 与 developer compatibility。硬件存在替代并不等于使用体验、性能和软件栈已经等价。

“国产 PC CPU/GPU 是一片空白”同样过度。

龙芯当前公开产品线包含面向 desktop/general-purpose 的 3A6000、3B6000 等 CPU；[^ch17-5] Moore Threads 公开销售 MTT S80 gaming GPU。[^ch17-6]

这些事实证明**产品存在且能形成真实 PC/graphics deployment**。

但它们不能证明：

- mainstream consumer-PC shipment share 已接近 Intel/AMD/NVIDIA；
- professional software / game compatibility 已达到同等级覆盖；
- performance/watt、driver maturity、developer ecosystem 与 supply scale 已全面等价。

所以这一层最准确的描述是：**不是“空白”，而是存在产品与自主生态，但主流规模、兼容性和系统经济性仍是闭环门槛。**

## 4. 第三层：Frontier AI 是系统级门槛

frontier AI 需要多个 advanced layer 同时成立：

- advanced accelerator；
- HBM-class memory；
- advanced packaging；
- high-speed scale-up / scale-out interconnect；
- compiler/runtime；
- distributed training；
- rack-scale deployment；
- data-center power。

任一单点突破都不足以自动形成等价系统。有 accelerator 但没有 HBM，有 hardware 但 migration cost 很高，有 cluster 但 utilization 与 interconnect scaling 不足，都可能使 system-level competitiveness 显著下降。

因此，本书不使用“某颗芯片能运行模型”作为 frontier substitution 的充分条件。

## 5. Ascend / CANN 的战略意义在系统完整性，而不是单卡数字

国内 accelerator stack 的核心价值，不在某一代单卡 peak FLOPS，而在于是否形成 compiler/runtime、framework adaptation、distributed communication、deployment tooling 与 production workload 反馈的闭环。

评估这一层应优先观察：

- large-cluster utilization；
- compiler stability；
- operator completeness；
- framework compatibility；
- failure recovery；
- multi-generation compatibility；
- production deployment scale。

由于部分 Ascend/CANN 具体性能和迁移效率数字目前主要来自二手材料，本章不把未逐项核验的一手缺失参数写成已确认事实。

## 6. Memory 是最容易被“国产存储”总词掩盖的层

长鑫科技 **2026-05-27 上交所注册稿**披露 DDR 与 LPDDR 产品。[^ch17-7]对注册稿全文检索 `HBM` 与“高带宽内存”均无命中，因此本报告只保留一个窄结论：

> **该注册稿未披露 HBM 产品线。**

这不证明企业不存在任何 HBM R&D；但要把 HBM 从研发可能性升级为 frontier system supply，必须看到 official product、customer qualification、volume production、bandwidth/capacity 与 packaging integration。

同一注册稿还必须严格区分 project investment 与 planned offering proceeds：三项项目总投资与拟使用募集资金不是同一分母；其中 DRAM 技术升级项目 **RMB18.0B 总投资**与 **RMB13.0B 拟使用募集资金**不得混用。

因此，DDR/LPDDR 供给增强与 HBM-class memory closure 必须分开分析。

### 6.1 普通 DRAM / NAND 与 Frontier HBM 不是同一供应链门槛

长鑫官方当前产品页披露 DDR5 颗粒最高 **8000 Mbps**、16Gb/24Gb，并覆盖 RDIMM/MRDIMM 等 server/workstation/PC 模组；[^ch17-8]这足以确认中国 conventional DRAM / server DRAM 的真实供给能力已经显著增强。

长江存储官方则确认自身是 3D NAND IDM，并披露 Gen5/Xtacking 4.0 相关产品体系以及 raw NAND、embedded memory、client SSD 与 enterprise SSD 产品线。[^ch17-9]

这两条事实说明：

> **consumer/general-purpose memory resilience 可以提高，而不需要先完成 frontier HBM closure。**

普通 DRAM 与 NAND 的 memory-cell front-end manufacturing 并不等同于台积电 leading-edge logic foundry；但 HBM-class AI system 会重新引入 advanced logic / base logic die、advanced packaging 与 accelerator integration 等更高门槛。Micron 就曾公开披露 HBM4E 的 base logic die 与 TSMC 合作制造。[^ch17-10]

所以“普通内存可以绕开台积电”与“frontier AI memory stack 不受台积电影响”是两个完全不同的命题。

### 6.2 国产 Memory Scale：必须区分 Revenue Share 与 Shipment Share

长鑫招股书引用 Omdia 的可审计口径是：按 **2025Q2 DRAM 销售额**测算，长鑫全球市场份额约 **3.97%**，位列全球第四、中国第一。[^ch17-11]

因此，“长鑫已经有 8% 全球 DRAM 份额”不能作为本书事实层。

长江存储的最新机构口径则不同。Counterpoint Research 2026Q2 Memory & Storage Tracker 给出：YMTC 以约 **14% NAND shipment share** 进入全球前三；[^ch17-12] 同一机构 2026Q1 的 **13%** 则是 NAND **revenue share**。[^ch17-13]

这两个数字不能拼成同一时间序列，因为分母不同。

它们真正支持的是：

> **中国 conventional DRAM / NAND 的全球供给存在感已经明显上升，但份额增长本身仍不能证明 HBM、leading-edge logic 或 frontier-system closure。**

关于“2027 产能翻倍”“三期明确达到某个月产量”的说法，如果只来自其他公司的招股书转引、媒体或供应链估算，只能放在 B/C 级背景，不进入本章 A 级事实层。

### 6.3 HDD 不能被 NAND 的国产进展掩盖

AI data-center storage 还包含 nearline HDD。公开产业研究显示，全球 nearline / mass-capacity HDD 仍高度集中于 Seagate、Western Digital 与 Toshiba。

因此，“国产 NAND / SSD 能力增强”不能自动写成“整个 storage stack 已经国产闭环”。

同时，AI 并没有简单淘汰 HDD：mass-capacity / cold-storage demand 仍然存在，只是 QLC nearline SSD 正在部分 workload 上加速替代。

## 7. Foundry share 不能直接等同于 Frontier AI capability

TrendForce 2026 Q1 foundry revenue share 约为：[^ch17-14]

**Table 17.1 — 2026 Q1 全球 foundry revenue share（TrendForce）**

| Foundry | Revenue share |
|---|---:|
| TSMC | 72% |
| Samsung Foundry (excluding System LSI) | 6.5% |
| SMIC | 5.1% |

**Source:** TrendForce, 2026-06-12.[^ch17-14]  
**Note:** 该表为 foundry revenue share，不是 advanced-node yield、AI wafer capacity 或 frontier-system capability。

这些是 foundry **revenue share**，不是先进节点良率、AI wafer capacity 或 frontier-system delivery capability。

中国要形成 frontier AI parallel supply，不只需要 logic die，还需要 advanced packaging、substrate、HBM integration、yield、high-volume qualification 与 power。节点追赶是必要条件之一，不是完整系统本身。

## 8. Algorithmic efficiency 是重要非对称杠杆

DeepSeek-V3 Technical Report 说明，算法与架构设计可以显著降低单位 capability 对硬件的需求。论文给出的 **pre-training 为 2.664M H800 GPU-hours**，完整正式训练为 **2.788M H800 GPU-hours**；[^ch17-15]按论文采用的 US$2/GPU-hour 假设，**US$5.576M 对应完整正式训练**，不等于完整研发成本。

这一案例支持的机制是：在 supply-constrained environment 中，sparse architecture、memory efficiency、routing、quantization 与 scheduling 可以提高 effective compute productivity。

它不支持“物理供给已经不重要”，也不支持“任何受限系统都能复制同样成本”。算法效率是杠杆，不是对 HBM、packaging、interconnect 和 power 的替代品。

## 9. Domestic workload 是平行系统迭代的重要条件

一个 parallel stack 不必先征服全球 developer 才能产生价值。只要拥有足够大的内部 workload，就可以通过真实生产环境积累 compiler feedback、deployment experience、failure recovery、operator coverage 和 utilization 数据。

这一逻辑与 hyperscaler custom silicon 类似：**大规模 captive workload 可以先支持一套较窄但完整的 system stack，再决定是否向更广泛外部生态扩展。**

因此，判断中国栈长期进展，不能只看 benchmark，还要看 production workload 的规模与持续性。

## 10. Export Control：不只是“买不到 GPU”，还影响 Manufacturing Continuity

出口限制在短期会提高先进硬件获取成本并降低 frontier cluster deployment speed；长期则会提高 domestic substitution incentive、local software/hardware integration 与 parallel ecosystem 的战略价值。

更上游还要单独看 semiconductor manufacturing equipment / software / service。ASML 的公开说明确认：EUV 对中国已受限制，最先进 immersion DUV 需要出口许可，后续规则还扩大到部分 advanced manufacturing technology、metrology 与 software。[^ch17-16][^ch17-17]

这不等于“国内所有 memory fab 会因为断供立刻停产”，但它说明：

> **domestic memory capacity growth ≠ upstream manufacturing autonomy**

新增产能能否 ramp、工艺能否升级、既有设备能否长期维护，仍要看关键设备、软件许可、备件、field service 与材料 qualification 的连续性。

因此，export control 不是一个单向变量。它可能同时扩大短期性能/规模差距，并强化长期平行体系建设动机。最终结果取决于 R&D efficiency、capital allocation、ecosystem adoption 与 supply scaling，而不是政策本身自动决定。

## 11. 七个 Frontier System Closure Gate

本书只有在以下七项都达到可验证规模时，才把“中国已经形成完整 frontier AI parallel stack”作为事实层判断：

1. advanced accelerator 可规模化交付；
2. HBM-class memory 可规模化；
3. advanced packaging 可规模化；
4. high-speed interconnect 可支撑大集群；
5. compiler/runtime migration cost 可接受；
6. frontier workload 能稳定运行；
7. system cost / utilization / power 可持续。

这七个 gate 的意义，是把“有没有国产产品”改成“能否形成 production-grade system”。任何一项长期缺失，都可能限制整体等价替代。

## 12. 对全球资源竞争的真正影响

如果中国 parallel stack 在 advanced logic、HBM、packaging、interconnect 与 software 上同时规模化，它不会只是“替代进口”，还会形成第二个大型资源重力中心：新的 foundry demand、memory demand、packaging demand、power demand 与长期资本承诺会进入全球/区域资源分配。

目前公开证据尚不足以证明这一第二个 frontier resource center 已经达到与全球主栈等价的完整规模。长鑫注册稿未披露 HBM product line，SMIC 5.1% 是 foundry revenue share 而非 frontier capability，多个 non-silicon layer 仍需要独立验证。

因此，当前更准确的状态是：**中国已经跨过“没有替代系统”的阶段，但尚未跨过“所有关键层都实现全球等价规模闭环”的阶段。**

## 13. 当前判断与证伪条件

截至 2026 年 8 月：

- smartphone / consumer computing：平行供给能力较强；
- PC / workstation：替代能力扩大，但软件与专业 workload 兼容仍决定闭环程度；
- frontier AI：已经存在真实、持续发展的 accelerator/software parallel stack，但 HBM、advanced packaging、interconnect、software migration、power 与 scale 仍需同时验证。

如果未来出现以下一手信号，应上调 system-closure 判断：公开 HBM product/revenue line；可复核的大集群 utilization 与 frontier workload；advanced-packaging 规模化交付；多代 compiler/runtime 兼容；以及稳定、可持续的 system economics。

如果这些 gate 长期未跨越，则“有国内技术栈”仍不能升级为“frontier 等价替代”。

## References

[^ch17-1]: TSMC, 4Q25 Presentation / 2025 full-year platform mix, HPC 58%, smartphone 29%, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
[^ch17-2]: Counterpoint Research, 2026 Q1 smartphone AP-SoC shipment share, UNISOC 14%, HiSilicon 4%, https://counterpointresearch.com/en/insights/global-smartphone-apsoc-market-share-quarterly
[^ch17-3]: Xinhua, 2025-05-22, Xiaomi XRing O1 entered mass production, https://english.news.cn/20250522/bca3bd53dab946d88696b0fb1625231d/c.html
[^ch17-4]: Reuters, 2026-08-24, XRing O1 device scale and O3 production plan, https://www.reuters.com/world/china/xiaomi-launches-new-xring-chip-partners-with-tsmc-production-sources-say-2026-08-24/
[^ch17-5]: Loongson, official CPU product line, https://www.loongson.cn/product/list?id=4
[^ch17-6]: Moore Threads, MTT S80 official product page, https://en.mthreads.com/product/S80
[^ch17-7]: CXMT, STAR Market registration prospectus, 2026-05-27, Shanghai Stock Exchange, https://static.sse.com.cn/stock/disclosure/announcement/c/202605/002170_20260527_23QQ.pdf
[^ch17-8]: CXMT, official DDR5 product page, https://www.cxmt.com/en/product.html
[^ch17-9]: YMTC, company profile and product portfolio, https://www.ymtc.com/en/aboutus.html ; https://www.ymtc.com/en/buslist.html?cat=35%3Fcat%3D35
[^ch17-10]: Micron Technology, investor material on HBM4E base logic die partnership with TSMC, https://investors.micron.com/static-files/5ea95475-639b-4cfc-91fd-b9b4a2bb5e63
[^ch17-11]: CXMT 2025 prospectus / Omdia, 2025 Q2 DRAM revenue share 3.97%, global #4, https://static.sse.com.cn/stock/disclosure/announcement/c/202512/002170_20251230_B8QS.pdf
[^ch17-12]: Counterpoint Research, 2026 Q2, YMTC 14% NAND shipment share, https://counterpointresearch.com/en/insights/server-led-essds-hit-48-percent-of-nand-shipments
[^ch17-13]: Counterpoint Research, 2026 Q1, YMTC 13% NAND revenue share, https://counterpointresearch.com/en/insights/global-nand-memory-market-share
[^ch17-14]: TrendForce, 2026-06-12, 1Q26 foundry revenue shares, https://www.trendforce.com/presscenter/news/20260612-13095.html
[^ch17-15]: DeepSeek-AI, “DeepSeek-V3 Technical Report,” https://arxiv.org/abs/2412.19437
[^ch17-16]: ASML, 2023 statement on Dutch export-control regulations, https://www.asml.com/en/news/press-releases/2023/statement-regarding-export-control-regulations-dutch-government
[^ch17-17]: ASML, 2024 statement on updated export restrictions covering additional advanced manufacturing technologies, metrology and software, https://www.asml.com/en/news/press-releases/2024/asml-expects-impact-of-updated-export-restrictions-to-fall-within-outlook-for-2025


\newpage

# Part II · 第18章：反垄断、产业政策与 AI 平台权力边界

## 1. System-stack power 给传统相关市场分析带来新难题

AI platform 的力量可能同时分布在 accelerator、interconnect、compiler/runtime、rack reference architecture、deployment software、cloud channel 与 adjacent model products。

于是可能出现：每个单独产品市场都存在竞争者，但多个关键接口由同一平台协调时，system-level switching cost 仍然很高。

因此，监管真正需要理解的是：

> **单一市场份额之外，跨层接口、bundling、migration cost 与 supply coordination 是否共同形成排他效果。**

## 2. Fine 与 Remedy 必须分开

罚款主要影响现金流；结构性或行为救济才可能改变竞争规则。

### Fine

罚款本身未必改变 CUDA migration cost、interconnect ecosystem、rack architecture、customer workflow 或 physical supply。

### Conduct / Structural Remedy

以下措施才可能直接改变 system economics：

- interface openness；
- interoperability requirements；
- tying / bundling restriction；
- non-discriminatory access / supply rules；
- acquisition restriction；
- structural separation。

因此，本书不把“可能罚多少钱”当成平台权力的核心变量。

## 3. 10% Turnover Ceiling 不是未来罚款模型

EU Regulation (EC) No 1/2003 Article 23(2) 规定，相关罚款不得超过 undertaking 前一营业年度 total turnover 的 **10%**。[^ch18-1]

这是一条法定 ceiling，不是：

> **Potential fine = revenue × 10%**

违法是否成立、严重性、持续时间、相关销售、程序结果和 remedy 形式都会影响最终结果。

所以 10% 只能表示法律工具强度，不能进入本书的公司盈利预测。

## 4. 程序状态必须逐层读取

欧盟 Article 102 公开程序本身已经给出清晰状态机：[^ch18-2]

1. complaint / ex officio investigation；
2. request for information；
3. formal investigation / market definition and dominance assessment；
4. Statement of Objections；
5. prohibition / commitment decision；
6. fine / remedy。

不同阶段的法律含义完全不同。RFI、market inquiry 或新闻报道不能直接写成“已经认定违法”。

## 5. 2026 年 Cloud Regulation 说明监管重点正在上移到 Interoperability

European Commission 2026 年仍在推进 DMA cloud-computing market investigation，公开 roundtables 明确讨论 cloud-service interoperability、financial conditions 与 contractual conditions；该 market investigation 的 final report 计划到 **May 2027**。[^ch18-3]

这说明监管关注点已经不只是传统价格，也包括跨服务技术互操作、合同与 switching conditions。

这与 AI system-stack competition 高度相关：如果客户无法低成本迁移 workload，接口和合同本身可能成为竞争变量。

## 6. Antitrust 与 Sovereign / Industrial Policy 不是同一个目标函数

竞争政策关注 market access、tying、exclusion、interoperability 与 customer choice；产业/国家安全政策则关注 domestic compute、semiconductor capacity、export control、data sovereignty 与 strategic autonomy。

同一政府完全可能同时：

- 补贴本土 advanced manufacturing；
- 推动 sovereign AI / cloud capacity；
- 限制敏感 accelerator 出口；
- 又要求本国市场中的平台提高 interoperability。

这些不是逻辑矛盾，而是不同政策目标并存。

## 7. Regulation 能改变四个系统变量

### 7.1 Interface Control

开放 compiler/runtime/network interfaces 可以降低 migration cost。

### 7.2 Bundling / Tying

限制 accelerator、network、software 的不当绑定，可以提高 multi-vendor system 的可执行性。

### 7.3 Access / Supply Rules

如果存在依法确认的 discriminatory access / allocation，non-discrimination remedy 可能改变 buyer bargaining structure。

### 7.4 Acquisition / Vertical Integration

merger control 可以阻止关键中间层进一步被纳入同一控制体系。

这些变量都会影响 system-stack moat。

## 8. Regulation 无法直接创造 Physical Capacity

监管可以降低 switching cost，但不能直接制造：

- HBM bits；
- advanced-packaging capacity；
- N2 wafers；
- grid / energized MW。

因此，即使 interface remedy 显著成功，physical scarcity 仍可能继续存在。

法律竞争与物理供给必须在不同模型中分析。

## 9. 对 China Parallel Stack 的影响也必须分层

美国或欧洲对某一 AI platform 的竞争政策，不会自动解决中国 frontier AI stack 的 advanced logic、HBM、packaging、interconnect 与 production software closure。

相反，中国本土 system capability 的提高也不自动改变欧美市场的 antitrust assessment。

两者可能互相影响 bargaining / strategic policy，但不能互相替代。

## 10. Regulation 如何改变 S1–S4

**Table 18.1 — 监管变量对 S1–S4 的作用路径**

| 情景 | 监管变量的作用 |
|---|---|
| S1 Competitive Expansion | interface openness、interoperability、tying limits 有效降低 switching cost |
| S2 Baseline Concentration | 调查与规则持续存在，但 system structure 基本保持 |
| S3 Resource Hegemony | remedy 不足以降低多层 switching / scarcity |
| S4 Capital Hard Landing | 通常由 utilization / capital clearing 主导，监管更多影响清算后的市场结构 |

**Source:** 本报告情景框架；EU competition / DMA procedure 作为监管机制背景。[^ch18-2][^ch18-3]  
**Note:** 表中为机制映射，不代表欧盟已对任何特定 AI platform 作出最终违法认定或 remedy。

所以监管不是固定“利空平台”的单向变量。它是否改变产业结构，取决于正式 remedy 是否真正触及迁移、bundling 与 access。

## 11. 当前判断

截至 2026 年 8 月，监管已成为 AI system-platform 的重要外部变量，但本书不会把调查、market inquiry 或法定罚款 ceiling 写成已经发生的结构性改造。

真正需要持续更新的是：

- 是否进入正式 proceedings；
- 是否发出 Statement of Objections / equivalent formal complaint；
- 是否形成 binding conduct commitments；
- 是否出现 interoperability / tying / access remedy；
- 是否有最终 decision；
- remedy 是否真实降低 production migration cost。

只有这些正式事件，才足以改变 system-stack scenario weighting。

## References

[^ch18-1]: EUR-Lex, Regulation (EC) No 1/2003, Article 23(2), https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32003R0001
[^ch18-2]: European Commission, Article 102 investigation procedure, https://competition-policy.ec.europa.eu/antitrust-and-cartels/procedures/article-102-investigations_en
[^ch18-3]: European Commission / Digital Markets Act, 2026 cloud-computing market-investigation roundtables, final report due May 2027, https://digital-markets-act.ec.europa.eu/roundtables-cloud-computing-services-2026-05-13_en


\newpage

# Part III · 第19章：AI 基础设施 CapEx 超级周期

## 1. CapEx 大小不是唯一问题，口径一致性才是第一道门

Microsoft、Amazon、Alphabet、Meta 的 infrastructure spending 已处历史高位，但四家公司财年、PPE、finance lease 与 net purchases 定义并不一致。

本书坚持三个分离：

1. company-wide CapEx 与 AI-specific CapEx 分离；
2. IT equipment 与 data-center / power infrastructure 分离；
3. actual CapEx 与 guidance / expectation 分离。

因此不存在一个可以直接从四家公司新闻稿相加得到的“官方四云 AI hardware CapEx”。

## 2. 2026 年当前资本扩张锚

**Table 19.1 — 四大云厂 2026 年公开资本投入口径**

| 公司 | 2026 当前公开口径 | 身份 |
|---|---:|---|
| Microsoft | calendar-2026 reported CapEx expectation ~US$175B | expectation；lease-classification adjustment 后，underlying investment expectation unchanged |
| Alphabet | US$195–205B | Q2 full-year guidance |
| Meta | US$130–145B | Q2 guidance；含 finance-lease principal |
| Amazon | US$169.007B | TTM PPE net purchases actual through 2026-06-30 |

**Source:** Microsoft FY26 Q4 earnings materials；Alphabet Q2 2026 company guidance as reported by Reuters（SEC Exhibit 99.1 separately supports Q2 actual results）；Meta 2026 Q2 SEC Exhibit 99.1；Amazon 2026 Q2 Form 10-Q.[^ch19-1][^ch19-2][^ch19-3][^ch19-4]  
**Note:** 四家公司时间窗和会计口径不同，严禁机械相加为统一 AI hardware CapEx。

这些数据足以证明 infrastructure investment 仍在高位扩张，但不能机械相加：三家是 guidance/expectation，Amazon 是 TTM actual，时间窗与科目都不同。

## 3. 2025 mixed-window aggregate 只能作为 scale anchor

按公开 PPE/equipment purchase 口径复算得到的 2025 mixed-window scale 约 **US$354B**；这是本报告的 **D 级 reconstruction / scale anchor**，不是四家公司共同披露的统一实际值。

它的用途仅是说明资本基数已经很大，不是四家公司共同披露的统一 AI subtotal。

如果把 fulfillment、office、network、power、custom silicon、third-party accelerator 等不同资产全部命名为 AI hardware，就会把会计分类问题伪装成产业事实。

## 4. CapEx 为什么形成长期锁定

AI infrastructure 不是单一 server purchase，而是多个久期不同的资产共同建设：

- accelerator / server：较短技术周期；
- network：中短周期；
- data-center shell / cooling：长周期；
- substation / transmission：更长周期；
- long-duration PPA / generation project：可达十年以上。

因此，技术迭代速度与 infrastructure economic life 之间形成 **duration mismatch**。

## 5. Seller 与 Buyer 的资本再生产对象不同

NVIDIA 的 cash generation 更直接用于 inventory、capacity reservation、supply commitments 与 next-generation roadmap。

Hyperscaler 的资本则要同时覆盖 land、building、power、network、custom silicon、third-party systems 与 operations。

所以“谁现金更多”不是正确比较。真正的差异是：

> **每一美元资本能否直接提高下一代 scarce-resource access 与 productive utilization。**

## 6. Power 把资本周期从 Hardware Clock 拉长到 Infrastructure Clock

rack density 上升后，扩张不再只取决于 server procurement，而取决于 grid connection、substation、transformer、transmission、cooling 与 long-duration power contracts。

这使 semiconductor clock 与 power-permitting clock 叠加。

当 chip supply 缓解但 energized capacity 仍不足时，bottleneck 可以从 manufacturing 转向 Time-to-Power。

## 7. 超级周期与泡沫的区别在 Utilization

高 CapEx 可以是高回报扩张，也可以是 overbuild。

如果 utilization、revenue per deployed compute、workflow volume 与 customer commitments 同步增长，大规模 investment 可以持续形成 barrier。

如果出现低 utilization、weak monetization、next-year guidance cuts、commitment cancellation 与 falling residual value，则同一 CapEx base 会变成资本压力。

## 8. 四类领先清算信号

CapEx cycle 的转折不能只看 stock price。本书观察：

- **Accounting**：impairment / accelerated depreciation / write-down；
- **Utilization / Revenue**：deployed compute utilization / AI revenue；
- **Market Clearing**：used-system price / cloud discounts / delivery lead time；
- **Forward Commitment**：CapEx guidance / supply commitments / compute contracts / power contracts。

只有多类信号同步恶化，才足以把“ROI pressure”升级为“Capital Hard Landing”。

## 9. 当前判断

截至 2026 年 8 月，公开数据仍更支持：

> **CapEx supercycle continues + hurdle rate for utilization and monetization is rising**

而不是已经完成资本清算。

资本基数越大，下一阶段越需要证明真实 workflow、revenue 与 utilization，而不能只依赖“未来需求一定更大”的叙事。

## References

[^ch19-1]: Microsoft, FY26 Q4 earnings / conference call, calendar-2026 reported CapEx expectation, https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast
[^ch19-2]: Alphabet, Q2 2026 earnings-call full-year CapEx guidance **US$195–205B**, company guidance reported by Reuters, 2026-07-22, https://www.reuters.com/business/google-quarterly-cloud-revenue-growth-beats-expectations-2026-07-22/ ; Alphabet SEC Exhibit 99.1 separately supports Q2 actual results, https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
[^ch19-3]: Meta Platforms, 2026 Q2 SEC Exhibit 99.1, FY2026 CapEx guidance including finance-lease principal, https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm
[^ch19-4]: Amazon.com, 2026 Q2 Form 10-Q, TTM purchases of property and equipment, net of proceeds and incentives, https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm


\newpage

# Part III · 第20章：Value Capture Map——资金流、利润池与风险承担

## 1. 同一美元不能在产业链上重复计算

AI infrastructure 的同一笔支出可能同时出现在：

- hyperscaler CapEx；
- system-vendor revenue；
- foundry revenue；
- memory-vendor revenue；
- packaging revenue；
- data-center / power investment。

这些并不是六笔互相独立的钱。买方购入一套 system，卖方确认 revenue；卖方再向 foundry、memory 和 components 采购；cloud 同时建设机房和电力。把各层 headline number 直接相加，会发生严重 double counting。

因此，本章只分析**价值捕获位置**和**风险承担位置**，不制造一个不可审计的全球总利润池。

## 2. Value Capture 由五个维度决定

判断一层产业能留下多少利润，至少要同时看：

1. **Scarcity**：供给能否快速扩张；
2. **Switching cost**：客户迁移到替代方案的工程/组织成本；
3. **Capital intensity**：维持增长需要投入多少固定资本；
4. **Duration**：收入、资产寿命和合同期限是否匹配；
5. **Distribution / workflow control**：是否拥有客户、数据和真实业务入口。

因此，高 revenue share 不自动等于最高 value capture，高 gross margin 也不能跨商业模式直接比较。

## 3. System Platform：把多个 scarce layer 组织成一套高价值产品

NVIDIA 是当前最清晰的 system-platform 案例。FY27 Q2：Revenue **US$96.221B**、Data Center revenue **US$89.0B**、GAAP gross margin **75.0%**、GAAP operating income **US$63.734B**。[^ch20-1]

这一层的价值不只是 accelerator die，而来自 compute、HBM、interconnect、software/runtime、rack architecture 与 deployment tooling 的系统整合。系统平台的优势在于：

- 可以把多个外部 scarce input 组织成一个采购单元；
- software / fabric / deployment 形成 switching cost；
- 高 cash generation 可以支持下一代 supply commitments；
- roadmap coordination 让客户更容易留在同一平台跨代升级。

但 system platform 也不拥有所有物理投入。foundry、HBM、advanced packaging 和 power 仍是外部边界。

## 4. Foundry / Advanced Packaging：重资产制造可以成为数量闸门

TSMC 2025 gross margin 为 **59.9%**，HPC platform 占全年 revenue **58%**。[^ch20-2] 2025 的公司更正口径为 **advanced packaging slightly over 10% of revenue**，[^ch20-3] 而 2026 Q2 管理层进一步表示 packaging tightness 已经限制客户增长。[^ch20-4]

这说明制造价值已经从 transistor scaling 扩展到 system integration。但 foundry / packaging 与 system platform 的经济模型不同：

> **manufacturing service + yield + utilization + CapEx execution**

而不是 software switching cost 主导的 asset-light platform economics。

所以一个制造层可以成为物理 bottleneck，却不必拥有全产业最高 margin；**bottleneck location ≠ profit location**。

## 5. HBM / Memory：高制造投入与产品周期共同创造稀缺利润

SK hynix FY25 官方结果为 Revenue **KRW 97.1467T**、Operating profit **KRW 47.2063T**、Operating margin **49%**，HBM revenue 同比超过一倍。[^ch20-5]

Micron 的一手披露又说明：same node / same bits 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。[^ch20-6]这使 HBM 的 value capture 同时来自 bandwidth value、制造投入密度、stacking/qualification 与短期 supply scarcity。

但 memory 仍具有明显周期性。如果 HBM capacity 超前扩张、generation mismatch 上升或 demand 增速下降，利润可以快速回吐。因此，memory 更接近**高壁垒的制造稀缺周期**，不是永久平台租金。

## 6. Hyperscaler：既拥有 distribution，也承担最大资产风险之一

Microsoft、Amazon、Alphabet、Meta 同时拥有 cloud distribution、internal workload、customer base、custom silicon 和 data-center scale。这让它们有能力把一部分 platform economics 内部化。

但 cloud buyer 同时承担：

- server / accelerator；
- network；
- data-center shell；
- cooling；
- power / land；
- depreciation；
- utilization risk。

所以 hyperscaler 不能简单归为“赢家”或“输家”。它们最强的资产是 distribution + workload + capital；最危险的资产是长期 infrastructure 先建设、workflow revenue 后兑现所形成的 duration mismatch。

## 7. Supply commitments 是 system platform 与 manufacturing 之间的资金桥

NVIDIA manufacturing, supply, and capacity commitments 从 2026-01-25 的 **US$95.2B** 上升到 2026-04-26 的 **US$119B**，再到 2026-07-26 的 **US$279B**。[^ch20-7]

FY27 Q2 10-Q 说明最新 commitments 主要关联 data-center infrastructure systems 所需的 memory 与 manufacturing facilities。它可以作为**未来资源锁定强度的财务 proxy**，但公开文件没有 supplier-level split，因此不能写成 TSMC、SK hynix、Micron 或任何单一供应商“已经收到多少”。

这也是 value capture 的重要动态：高 seller cash flow 可以更早变成下一代 wafer、memory、packaging 和 component commitments。

## 8. Power / Powered Land：价值来自时间稀缺，而不是单纯电价

当 rack power 进入约 **120 kW-class**，[^ch20-8]数据中心需要更强的 grid connection、substation、transformer、cooling 与 firm generation。拥有 powered land、existing interconnection 和可执行许可路径的资产会获得明显 **Time-to-Power** 价值。

这层资产的特点是：复制慢、地理固定、许可周期长、合同期限往往长于 compute generation。

因此 power 可以成为 scarce layer，但其经济性必须与 utilization 和合同久期一起分析。长期 PPA 在高需求情景中是 hedge / moat，在 S4 中也可能成为 long-duration obligation。

## 9. Model / Application：长期利润取决于 Workflow，而不是模型本身

模型公司与 AI software 拥有 model capability、API、user distribution 和 workflow 入口，但也面对 open-source competition、inference/retrieval/tool cost、cloud bargaining 与快速价格压缩。

传统 SaaS 的高毛利不能直接套到 AI application。正确单位是 **AI Software Unit Economics**：

> Revenue or productivity value − inference − retrieval/storage − tools/APIs − human review − AI-specific cloud cost

真正有防御力的 application layer 需要把模型能力转化成 proprietary workflow、data、distribution、retention 和 measurable business outcome。

## 10. Consumer Electronics：不是“输掉 AI”，而是承受 residual-capacity pressure

smartphone、PC、gaming 与 general server 仍然是大型市场。它们承受的主要不是“被 AI 淘汰”，而是 shared upstream resources 的再分配：advanced logic allocation、DRAM residual supply、consumer-GPU availability 与 component pricing。

所以这一层更准确的角色是 **residual-capacity pressure bearer**。当 AI/server demand 抢占高价值增量资源时，传统终端的升级节奏、配置和成本会发生变化。

## 11. Custom Silicon 会重画资金路径，但不一定减少上游需求

传统路径可以近似写成：

> cloud / model buyer → system platform → foundry / HBM / packaging → equipment/materials → power/data-center

当 hyperscaler 使用 custom silicon 时，部分资金可能绕开 NVIDIA：

> cloud → custom system → foundry / HBM / packaging

这会改变 platform profit 的归属，却未必降低 advanced logic、HBM、packaging 与 power 的总需求。

因此，system-stack substitution 既是利润分配变量，也是上游资源竞争变量。

## 12. 不使用固定“赢家排名”，而使用 Scenario Map

不同情景会改变 value capture：

- **S1 Competitive Expansion**：custom stack、open software 和 supply expansion 降低平台租金，价值更分散；
- **S2 Baseline Concentration**：system platform 与 scarce manufacturing 保持强 value capture，cloud 继续高投入；
- **S3 Resource Hegemony**：logic/HBM/packaging/power 进一步集中，scarce-layer owners 与 dominant system platform 获取更强议价；
- **S4 Capital Hard Landing**：buyer utilization 与 commitments 下滑，长期基础设施首先面临 duration/ROI 压力，上游利润随后传导回落。

这比给 system platform、HBM、foundry、cloud、application 排一个永久名次更可靠。

## 13. 当前判断

截至 2026 年 8 月，AI infrastructure 的高质量 value capture 主要出现在两类位置：

1. **能够组织多个稀缺层并制造 switching cost 的 system platform；**
2. **短期供给弹性低、进入壁垒高的 HBM / leading-edge manufacturing / advanced packaging / powered infrastructure。**

而最大资产风险则更多留在需要提前建设大规模 infrastructure 的 buyer 端。应用层是否形成长期利润池，取决于 workflow economics 和 distribution。

因此，真正应该问的不是“AI 一共花了多少钱”，而是：

> **同一笔资本在每一层留下多少可重复现金流、形成多少不可替代性，又把多少长期风险留在资产负债表上。**

## References

[^ch20-1]: NVIDIA, “NVIDIA Announces Financial Results for Second Quarter Fiscal 2027,” https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^ch20-2]: TSMC, 2025 Annual Report, gross margin and platform mix, https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^ch20-3]: TSMC, 4Q25 Earnings Conference Transcript, advanced packaging slightly over 10% of 2025 revenue, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
[^ch20-4]: TSMC, 2Q26 Earnings Conference Transcript, packaging tightness limiting customer growth, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^ch20-5]: SK hynix, FY25 Financial Results, https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
[^ch20-6]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^ch20-7]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^ch20-8]: NVIDIA, DGX GB200 Hardware Guide, rack power approximately 120 kW, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html


\newpage

# Part III · 第21章：消费电子与实体经济的成本传导

## 1. Consumer Electronics 不直接买训练柜，但会共享上游资源

consumer products 与 AI/server systems 共享的主要层包括：

- DRAM / LPDDR wafer input；
- selected leading-edge logic；
- consumer GPU / workstation resources；
- power-management components；
- selected packaging。

所以传导并不是“AI 抢走所有芯片”，而是：

> **AI/server product mix 上升 → shared-resource residual capacity 下降 → consumer contract price / configuration / replacement cycle 承压**

## 2. HBM 的制造投入会放大 DRAM residual pressure

Micron 一手披露：same node / same bits 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。[^ch21-1]

TrendForce 预计 2026 年 HBM + RDIMM 合计约占 DRAM bit supply **51%**。[^ch21-2]

这意味着 consumer DRAM 的压力不能只用 bit share 判断。高价值 memory 如果同时需要更多 manufacturing input，会进一步压缩 conventional DRAM 的有效 residual supply。

## 3. Smartphone memory 已出现机构级合同价冲击

TrendForce 2026-02-11 给出的 1Q26 例子显示，主流 **8GB + 256GB** smartphone memory estimated contract prices 同比接近 **+200%**。[^ch21-3]

到 2Q26，TrendForce 估计 LPDDR4X solution ASP 环比 **+70–75%**、LPDDR5X **+78–83%**。[^ch21-4]

TrendForce 2026-08-03 的 **3Q26 forecast** 预计 mobile DRAM 涨幅将明显收敛到约 **+8–13% QoQ**。[^ch21-5] 与此同时，TrendForce 仍指出 suppliers 持续把 capacity 向 server / HBM applications 倾斜。

因此更准确的判断是：

> **结构性 residual pressure 仍在，但价格涨速并非永远单边加速。**

## 4. Smartphone 仍是巨大市场，不是被 AI 消灭

TSMC 2025 smartphone platform 占全年 net revenue **29%**，platform revenue 同比 **+11%**。[^ch21-6]

因此，AI/HPC growth 并不等于 smartphone demand 消失。

Counterpoint 2026H1 给出了更直接的终端压力证据：[^ch21-7]

- global smartphone SoC shipments 同比 **-15%**；
- MediaTek 与 Qualcomm shipments 均同比下降 **>25%**；
- 2Q26 smartphone memory prices 同比上涨 **>300%**；
- 但 GenAI smartphone SoC shipments 同比 **+24%**；
- UNISOC 在低成本 segment 继续扩大份额。

这说明发生的是**分层重构**而不是统一死亡：entry/mid-range 对 memory/BOM pressure 更敏感，premium/GenAI segment 相对更有韧性，低成本 SoC 路线也可能获得 share。

真正的变化是：HPC 对新增先进资源的吸引更强，memory economics 更偏向 server/HBM，导致 flagship BOM、memory configuration 与中端产品 node strategy 更容易受到约束。

### 4.1 Cross-Market Resource Reordering：AI 打破的是多终端资源配置平衡

TrendForce 2026-04 指出，AI demand 已造成 **3 nm–2 nm wafers 与 2.5D/3D advanced packaging** 的 bottleneck，并称 NVIDIA 较早预先锁定了大量 **4/3 nm wafer capacity、CoWoS、HBM、T-glass、substrates、PCB 与 SSD** 等资源。[^ch21-8]

2026-06 的 foundry research 又指出 TSMC **3 nm capacity remains severely constrained**；[^ch21-9] 同月 TrendForce 进一步指出，foundries 正把更多 wafer capacity 转向 AI-related products，[^ch21-10]高价值 AI demand 与 mature-node output cuts 已经改变 8-inch/12-inch 的供需结构。

因此，本书把这一变化定义为：

> **Cross-Market Resource Reordering = AI 的更高预期回报与更强订单确定性，使多个原本服务不同终端市场的增量资源，被重新排序到 AI/server 优先级更高的用途。**

它不是“过去所有客户平均分产能、现在英伟达拿走一切”。

它支持的是：

- advanced-node / packaging / memory / power-device 资源配置逻辑发生变化；
- traditional end markets 面对更低 Non-AI Residual Capacity；
- allocation assurance 与议价能力的重要性上升；
- 低利润、低议价、短订单客户更容易承受 higher price + lower quantity。

但这些机构证据**不能**直接推出“Apple/Qualcomm/AMD/Intel 各自具体少拿了多少 wafer allocation”，更不能写成“某一家已拿走 100% 先进产能”。

## 5. PC 同时受到 Memory 与 GPU / System Price 两条传导

NVIDIA FY26 10-K 表示 FY26 Gaming revenue 同比 **+41%**，同时预计 supply constraints 会成为 FY27 Q1 及之后 Gaming 的 headwind。[^ch21-11]

到 FY27 Q1，公司新的 Edge Computing 口径又指出，consumer PC demand 较慢，部分原因是 **elevated memory and systems prices**。[^ch21-12]

这形成两条独立但可以叠加的传导：

- consumer GPU / system availability；
- DDR / LPDDR / system memory cost。

## 6. 价格压力通常先改变配置和换机，而不是直接停产

终端厂商常见应对包括：

1. 提价；
2. 降低/延缓 memory configuration；
3. 拉长 mature-node 使用；
4. 延长 replacement cycle；
5. 签更长期 supply agreement。

因此，AI resource pressure 更可能先表现为**升级税**：同样价格获得更慢的规格升级，或者相同规格需要更高 BOM。

### 6.1 Supply Assurance 是独立变量

在极端紧缺期，终端厂商面对的不只是 ASP 上升，还可能是 **allocation fulfillment 不足**。TrendForce 2026-03 指出，allocation 较低的 PC OEM / module maker 需要以更高价格从供应商或模组厂补货；[^ch21-13]2026-05 的 smartphone research 也指出 full-year allocation 收紧，品牌需要更谨慎地管理 LTA 与库存。

因此，分析必须把：

> **price pressure** 与 **quantity assurance**

分开。价格可以上涨而 supply 仍然不足；愿意支付更高价格，也不保证能拿到计划所需数量。

## 7. Channel Price 只是温度计，Institutional Contract Price 更接近产业层

渠道现货可以证明消费者/装机市场在某时点承受压力，但不能反推出 vendor contract ASP 或 long-duration agreements。

所以本报告以 TrendForce contract-price research、vendor filings 与 company commentary 为主要证据，不用渠道口述建立核心结论。

## 8. China Consumer Supply 可以缓冲本地压力，但不等于 HBM Closure

中国在 DDR、LPDDR、NAND、smartphone manufacturing 与终端 supply chain 的能力扩张，可以提高本地 consumer residual capacity。

但 consumer DRAM / NAND capability 不能自动外推成 HBM-class frontier memory supply。

因此，本地替代可以改变 smartphone / PC cost structure，却不会自动解除 frontier AI 的 HBM / advanced-packaging bottleneck。

## 9. Automotive / Industrial：成熟存储也会被高价值产品重排

汽车与工业设备具有更长 qualification cycle，但这不意味着它们不受 AI 时代 product-mix 重排影响。

TrendForce 2026-06 指出，主要 memory suppliers 把 capacity 继续向 HBM 与高层数 3D NAND 等高价值产品倾斜，挤压 NOR Flash 与 SLC NAND 的成熟产能；1H26 两类产品合约价累计涨幅均超过 100%。[^ch21-14]到 2026-07，TrendForce 又把 2H26 SLC NAND 相对 1H26 的涨幅预期提高到 **120–170%**，[^ch21-15]汽车、工业、networking 都是主要受影响客户。

这里能确认的是**具体 mature-memory 品类的结构性短缺与涨价**，不能把它扩大成“所有车规存储涨180%”“单车成本增加 RMB7,000–10,000”或“全年供应满足率不足50%”这类未经一手/机构来源闭合的整车结论。

## 9.1 Routers / Broadband：低议价买家是更清晰的受害层

Counterpoint Research 2026-02 报告称，consumer DRAM/NAND 一年内价格上涨超过 **600%**；router / gateway / set-top-box 等 broadband products 使用的 memory price 接近 **7×**，低中端 router 的 memory BOM 占比从约 **3%** 升至 **>20%**。[^ch21-16]

这条证据很重要，因为它说明：

> **resource crowding-out 的损伤强度，与终端厂商的议价权和 supply assurance 高度相关。**

大客户可以通过 LTA、规模采购和更强资产负债表缓冲冲击；低议价 OEM 更容易同时承受 higher price + lower allocation。

## 9.2 HDD 与 SSD：不是单向“SSD 消灭 HDD”

AI data-center storage 正在形成分层竞争。

TrendForce 2025–2026 同时观察到 nearline HDD supply shortage 与高容量 QLC nearline SSD 的替代加速；[^ch21-17] 但 Seagate FY26 又明确表示，AI 产生的数据增长正在强化 mass-capacity storage demand。[^ch21-18]

因此更准确的结构是：

- latency / inference-sensitive workload 提高 SSD / QLC nearline SSD 的吸引力；
- cold / mass-capacity storage 仍然给 HDD 带来真实需求；
- HDD supply / HAMR ramp 本身也可能形成新的 storage bottleneck。

所以不能写成“AI 数据中心正在让机械硬盘失去战略意义”。

## 10. 实体企业还有第二层 AI Adoption Cost

制造企业使用 AI 时，还要支付 cloud inference、software integration、data pipeline、security/compliance、workflow redesign 与 human review。

因此：

> **Net Productivity Value = Productivity Gain − Upstream Input Pressure − Total AI Adoption Cost**

这解释了为什么“AI 模型更便宜”并不自动意味着实体企业 ROI 提高。

## 11. 当前判断

截至 2026 年 8 月，证据支持：

> **AI infrastructure 已经通过 memory、consumer-system pricing 与 shared leading-edge resources，把部分成本压力传导到消费电子；但这种传导是选择性的、阶段性的，并会随 inventory、demand 与 capacity allocation 变化。**

它不是“消费电子被 AI 淘汰”，而是产品配置、升级速度、利润率和换机周期面对新的上游资源竞争。

## References

[^ch21-1]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^ch21-2]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^ch21-3]: TrendForce, 2026-02-11, 1Q26 mainstream smartphone memory contract cost, https://www.trendforce.com/presscenter/news/20260211-12922.html
[^ch21-4]: TrendForce, 2026-05-14, 2Q26 LPDDR4X and LPDDR5X ASP changes, https://www.trendforce.com/presscenter/news/20260514-13044.html
[^ch21-5]: TrendForce, 2026-08-03, 3Q26 mobile DRAM price outlook, https://www.trendforce.com/research/download/RP260803NC
[^ch21-6]: TSMC, 4Q25 Presentation / 2025 full-year platform mix, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
[^ch21-7]: Counterpoint Research, 2026-07-28, H1 2026 smartphone SoC shipment and memory-price trends, https://counterpointresearch.com/en/insights/global-smartphone-soc-shipments-fall-15percent-yoy-in-h12026
[^ch21-8]: TrendForce, 2026-04-30, AI supply-chain arms race and advanced-node / packaging bottlenecks, https://www.trendforce.com/presscenter/news/20260430-13028.html
[^ch21-9]: TrendForce, 2026-06-08, TSMC 3 nm capacity remains severely constrained, https://www.trendforce.com/research/download/RP260608SX3
[^ch21-10]: TrendForce, 2026-06-30, foundry capacity reallocation toward AI-related products, https://www.trendforce.com/presscenter/news/20260630-13127.html
[^ch21-11]: NVIDIA Corporation, FY26 Form 10-K, Gaming revenue and supply-constraint disclosure, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
[^ch21-12]: NVIDIA, FY27 Q1 CFO commentary, consumer PC demand tempered by elevated memory and systems prices, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27cfocommentary.htm
[^ch21-13]: TrendForce, 2026-03-31, allocation fulfillment and higher-price procurement, https://www.trendforce.com/presscenter/news/20260331-12995.html
[^ch21-14]: TrendForce, 2026-06-16, NOR Flash / SLC NAND mature-capacity squeeze, https://www.trendforce.com/presscenter/news/20260616-13102.html
[^ch21-15]: TrendForce, 2026-07-13, SLC NAND 2H26 price forecast, https://www.trendforce.com/presscenter/news/20260713-13142.html
[^ch21-16]: Counterpoint Research, 2026-02-11, broadband memory-price surge and router BOM impact, https://counterpointresearch.com/en/insights/7times-memory-price-surge-threatens-telcos-broadband-router-set-topbox-supply
[^ch21-17]: TrendForce, 2025-09-15, nearline HDD shortage and QLC SSD substitution, https://www.trendforce.com/presscenter/news/20250915-12714.html
[^ch21-18]: Seagate Technology, FY26 results, AI/cloud data generation and mass-capacity storage demand, https://investors.seagate.com/news/news-details/2026/Seagate-Technology-Reports-Fiscal-Fourth-Quarter-and-Fiscal-Year-2026-Financial-Results/default.aspx


\newpage

# Part III · 第22章：折旧墙与 Duration Mismatch

## 1. 折旧墙不是某一年必然出现的固定美元冲击

更准确的定义是：

> **当 hardware refresh / economic obsolescence 快于 workload monetization 时，已形成资产成本开始压低资本回报，并改变下一轮 CapEx。**

所以折旧墙必须与 utilization、revenue、residual value 和 next-generation investment 一起看。

## 2. 四家主要 Cloud 的 Server Useful Life 并不统一

最新公司披露大致显示：

**Table 22.1 — 主要 Cloud 公司 server / network equipment useful-life disclosure**

| 公司 | server / network equipment useful-life disclosure |
|---|---|
| Microsoft FY26 | 2–6 years |
| Alphabet 2025 | generally 6 years |
| Meta 2025 | 5–5.5 years |
| Amazon 2025 | 5–6 years；部分资产 2025 从 6 年调整到 5 年 |

**Source:** Microsoft FY26 10-K、Alphabet 2025 10-K、Meta 2025 10-K、Amazon 2025 10-K.[^ch22-1][^ch22-2][^ch22-3][^ch22-4]  
**Note:** accounting useful life 不是 economic life；不同公司资产类别与折旧估计不可机械视为同口径。

这已经足以证明：不能用一个统一“4 年直线折旧”去估算整个 AI infrastructure。

## 3. Accounting Useful Life 与 Economic Life 不相同

一个 server 可能会计上还能继续折旧，但新 architecture、memory efficiency、software support 或 power efficiency 已使它在经济上失去竞争力。

这就是 **economic obsolescence**。

反过来，一座 data-center shell、substation 或 PPA 的经济寿命往往远长于一代 accelerator。

因此 AI infrastructure 的根本错配是：

> **short-cycle compute vs long-cycle physical infrastructure**

## 4. Demand 转弱时，清算有明确顺序

最先调整的通常是：

1. next-generation hardware orders；
2. inventory；
3. used-system / lease price；
4. discretionary expansion。

最慢调整的是 data-center shell、grid asset、generation/PPA 等 long-duration infrastructure。

这也是为什么 Capital Hard Landing 不会在一个季度完成。

## 5. CapEx 必须除以 Utilization，而不是只除以年份

作为 **D 级 sensitivity example**，同样 **US$100B** investment 在 **90%** 与 **30%** utilization 下会代表完全不同的经济结果；US$100B、90% 和 30% 都是示例输入，不是行业 actual。

因此必须同时看：

> **Revenue / Deployed Compute**

以及真实 **Utilization**。

固定折旧年限只能描述会计费用节奏，不能描述资产是否在创造足够现金流。

## 6. Market-clearing Price 是比财报更快的 Economic Depreciation 信号

used accelerator / system price、cloud lease rate 与 delivery lead time 可以早于 impairment 反映 generation obsolescence 和 oversupply。

如果新一代系统上线后旧一代 residual value 快速下跌，买方经济折旧会明显快于 accounting depreciation。

这也是 Ch24 把 Market Clearing 单列为 S4 信号的原因。

## 7. Algorithmic Efficiency 也会制造 Economic Obsolescence

如果新 architecture 能用更少 HBM、compute 或 communication 完成相同 workload，旧系统即使物理可运行，也可能在 cost per task 上迅速失去竞争力。

因此，软件/模型创新会直接改变 hardware economic life。

## 8. Power Asset 的风险方向恰好相反

在 S2/S3 高需求环境中，long-duration power / grid asset 可能成为 scarce moat。

在 S4 中，同一个 PPA、substation 或 data-center shell 则可能变成长久期低利用率负担。

所以资产价值取决于 demand duration，而不是“电力资产永远安全”。

## 9. Anchor Buyer 能降低融资风险，也会集中 Demand Risk

长期 model-company compute contracts 提高 revenue visibility，使基础设施更容易融资。

但如果 anchor buyer 的 revenue、financing 或 architecture assumptions 变化，take-or-pay、renegotiation 与 stranded-capacity risk 会集中爆发。

因此 customer concentration 与 contract duration 必须与 useful life 一起看。

## 10. 2036 不能由 2026 一轮折旧直接推出

不同资产在不同日期投入使用、采用不同 useful life，还可能发生 impairment 或 estimate change。

不存在一个统一“2026 CapEx 在某年全部折完”的时间点。

2036 的产业结构取决于第二、第三轮 buildout、workload growth、system substitution、power、China parallel stack 与 regulation，而不是由第一轮会计折旧机械决定。

## 11. 当前判断

截至 2026 年 8 月，更准确的状态是：

> **CapEx expansion + rising duration / utilization risk**

而不是已经确认的大规模 impairment cycle。

折旧墙真正需要警惕的组合是：utilization 下滑、residual value 快速下降、CapEx guidance 下调、commitments 收缩和 impairment 增加同时出现。

## References

[^ch22-1]: Microsoft Corporation, FY26 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
[^ch22-2]: Alphabet Inc., 2025 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
[^ch22-3]: Meta Platforms, Inc., 2025 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
[^ch22-4]: Amazon.com, Inc., 2025 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm


\newpage

# Part III · 第23章：AI 基础设施资本市场与融资结构

## 1. AI Capital Market 已跨越多种资产类别

AI infrastructure 的资本体系已经不只包括 listed technology equity。

它同时覆盖：

- semiconductor manufacturing；
- private infrastructure；
- data center；
- power / grid；
- project finance；
- long-duration compute contracts；
- private credit / institutional capital。

因此，核心问题不是“还有多少钱愿意投 AI”，而是：

> **哪一种资本承担哪一种久期、现金流和 residual-value risk。**

## 2. Asset-light Platform 与 Heavy Infrastructure 不能用同一估值逻辑

NVIDIA 的典型特征是 high system margin、strong cash generation 与相对较低直接 fixed-asset intensity。

FY26 NVIDIA-defined non-GAAP free cash flow 为 **US$96.575B**；[^ch23-1] FY27 Q2 Revenue **US$96.221B**、Data Center **US$89.0B**、GAAP gross margin **75.0%**、GAAP operating income **US$63.734B**。[^ch23-2]

相比之下，hyperscaler、foundry、memory vendor、data-center operator 和 power developer 需要承担大量 fixed assets。

所以同样 revenue growth，在 platform 与 infrastructure 层的 capital return 含义完全不同。

## 3. Hyperscaler 风险来自多资产叠加

cloud CapEx 同时进入 servers、custom silicon、network、buildings、cooling、power 和 land。

这意味着 hyperscaler 必须同时管理多个 useful-life clock。

高 utilization 时，这种 CapEx 可以形成 barrier；低 utilization 时，D&A、FCF 与 residual-value pressure 会迅速显现。

因此需要同时看 growth、D&A、FCF、utilization、AI-related monetization 与 next-year CapEx。

## 4. Manufacturing Capital 具有不同的周期性

TSMC、SK hynix、Micron 等制造商承担 fab、equipment、cleanroom、process migration 与 yield learning。

它们的回报取决于 utilization、product mix、technology leadership、customer demand 与 pricing。

HBM boom 可以显著改善 memory-vendor economics，但制造利润仍比 system-platform economics 更受 cycle 与 utilization 影响。

## 5. 2026 年出现了独立 Compute Financing Platform

NVIDIA 2026-08-10 官方宣布，与 Apollo、BlackRock、Blackstone、Brookfield、Goldman Sachs、KKR 建立独立 compute financing platforms，目标是**随时间动员超过 US$500B third-party capital**用于 AI infrastructure buildout。[^ch23-3]

这条证据的重要性不在“500B 已到账”，而在于：

> **compute 正被尝试组织成可由长期机构资本独立承销和融资的基础设施资产。**

官方同时明确：相关 partnership **subject to execution of final agreements**。

因此 **>US$500B** 只能作为 mobilization target，不能写成 committed / funded / deployed capital。[^ch23-3]

## 6. Compute 为什么能被包装成 Infrastructure Asset

长期资本通常偏好 predictable cash flow、long contract、collateral 与 clear offtaker。

AI compute 正通过 long-term compute commitments、hyperscaler leases、PPA 与 Anchor Compute Buyer demand 尝试创造这种结构。

如果 usage-linked revenue 与 customer transferability 足够稳定，compute asset 可以获得更接近 infrastructure financing 的资本来源。

## 7. 但 Hardware Residual Value 仍是关键风险

compute 与传统 infrastructure 最大差异之一，是 generation obsolescence 更快。

如果下一代 accelerator / system 显著降低 cost per task，旧 hardware 即使仍可工作，也可能快速贬值。

所以融资结构必须回答：

- residual-value risk 谁承担；
- customer contract 是否覆盖 depreciation；
- utilization 是否足够稳定；
- asset 是否可在不同 customers/operators 之间转移；
- leverage 是否建立在过度乐观的 terminal value 上。

## 8. Anchor Buyer 可以降低融资风险，也提高 Customer Concentration

OpenAI、Anthropic 等 long-duration demand 提供 revenue visibility，使 project finance 更容易成立。

但如果 project economics 高度依赖单一 model company，融资风险会从 technology risk 转成 customer-concentration / utilization risk。

因此，Anchor Buyer 既是融资条件，也是风险集中点。

## 9. Sovereign Capital 的意义在 Strategic Capacity

主权基金参与 AI infrastructure 的逻辑通常不仅是财务回报，也包括 domestic compute、data center、power、semiconductor manufacturing 与 strategic autonomy。

所以真正具有战略意义的是对 fab、power、sovereign cloud、compute fund 和 infrastructure project 的直接参与，而不是二手市场股票持仓。

没有官方项目披露时，本书不使用传闻持仓构造“主权资本已经全面入场”的结论。

## 10. Duration Matching 是融资质量核心

**Table 23.1 — AI infrastructure 资产类别与主要融资风险**

| 资产 | 主要风险 |
|---|---|
| GPU/server | technology refresh / residual value |
| Data center | utilization / lease duration |
| Grid/substation | long construction / regulated return |
| PPA | long obligation / demand risk |
| Foundry | utilization / node transition |
| HBM fab | memory cycle / generation timing |

**Source:** 本报告资产久期与融资风险框架。  
**Note:** 表中为机制分类，不代表所有项目具有相同融资结构、杠杆水平或合同条款。

最危险结构是：

> **short-duration demand assumption + long-duration debt / power / real-estate obligation**

## 11. 当前判断

AI infrastructure 正从科技公司内部 CapEx 扩展为：

> **technology capital + infrastructure capital + private capital + sovereign capital**

共同参与的长期资产体系。

这会扩大可获得资本规模，也会把 risk distribution 从单一 corporate balance sheet 扩散到更广的金融体系。

最终决定这类融资是否可持续的，不是 headline target，而是 utilization、cash yield、contract quality 与 hardware residual value。

## References

[^ch23-1]: NVIDIA, “NVIDIA Announces Financial Results for Fourth Quarter and Fiscal 2026,” NVIDIA-defined non-GAAP free cash flow, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
[^ch23-2]: NVIDIA, “NVIDIA Announces Financial Results for Second Quarter Fiscal 2027,” https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^ch23-3]: NVIDIA, 2026-08-10, AI compute infrastructure financing platforms and >US$500B third-party-capital mobilization target, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Partners-With-Apollo-BlackRock-Blackstone-Brookfield-Goldman-Sachs-and-KKR-to-Establish-AI-Compute-Infrastructure-Financing-Platforms-to-Mobilize-Over-500-Billion-of-Third-Party-Capital/default.aspx


\newpage

# Part III · 第24章：泡沫识别、资本清算与 S4

## 1. CapEx 很大，不等于泡沫

AI infrastructure 的资本开支已经进入极高水平，但投资规模本身不能证明泡沫。真正需要判断的是：资产建设速度、利用率、可实现现金流和残值之间是否持续脱节。

因此，本书不使用一个 CapEx 总额、一个估值倍数或一次科技股回撤作为“泡沫已破”的证据。S4 Capital Hard Landing 需要多类产业信号同步恶化。

## 2. 四类清算信号

### 2.1 Accounting

最慢但最硬的信号来自账面确认：impairment、inventory write-down、accelerated depreciation、asset disposal。它们说明企业已经承认原先预期的未来现金流或残值不足。

单季政策/库存项目不能自动升级成结构性崩溃。例如 NVIDIA FY26 的 H20-related charges 影响过利润，但 FY26 Q4 GAAP gross margin 已为 **75.0%**，FY27 Q1 为 **74.9%**，FY27 Q2 维持 **75.0%**。[^ch24-1][^ch24-2][^ch24-3]一次性 charge / release 与长期 system economics 必须分开。

### 2.2 Utilization / Revenue

资本周期最终要由有效 workload 付账。需要观察 compute utilization、revenue per deployed system、enterprise AI revenue 与 workflow monetization。

如果 utilization 高，巨额 CapEx 可以继续产生现金回报；如果大量资产长期低利用，折旧会先于收入形成压力。真正危险的不是“机器很多”，而是：**资产越来越多，而能够产生现金流的有效 workload 没有同步增长。**

### 2.3 Market Clearing

市场往往早于财报反映松动。重要指标包括 used accelerator / system price、lease rate、cloud instance discount、delivery lead time、HBM price、advanced-packaging availability 与 resale liquidity。

如果新一代硬件快速替代旧一代，economic depreciation 会快于 accounting depreciation。持续的二手价格折让和交期缩短，比单一股价回撤更接近真实去库存。

### 2.4 Forward Commitment

下一轮扩张是否继续，要看 hyperscaler CapEx guidance、NVIDIA manufacturing/supply/capacity commitments、long-duration model-company compute contracts 与 power commitments。

NVIDIA commitments 的公开轨迹由 2026-01-25 的 **US$95.2B**、2026-04-26 的 **US$119B** 上升到 2026-07-26 的 **US$279B**。[^ch24-4]FY27 Q2 10-Q 说明最新承诺主要关联 data-center infrastructure systems 所需的 memory 与 manufacturing facilities。当前轨迹更像继续前置锁资源，而不是已经进入普遍撤单。

## 3. 四云 CapEx 必须分公司、分会计口径观察

统一的“2026 AI hardware CapEx”并不存在。当前可公开追踪的规模包括：

**Table 24.1 — 四大云厂 2026 年资本投入公开口径**

| 公司 | 2026 当前公开口径 | 身份 |
|---|---:|---|
| Microsoft | calendar-2026 reported CapEx expectation ~US$175B | expectation；受 lease classification 影响，underlying investment expectation unchanged |
| Alphabet | US$195–205B | Q2 guidance |
| Meta | US$130–145B | Q2 guidance；含 finance-lease principal |
| Amazon | US$169.007B | TTM PPE net purchases actual through 2026-06-30 |

**Source:** Microsoft FY26 Q4 earnings materials；Alphabet Q2 2026 company guidance as reported by Reuters（SEC Exhibit 99.1 separately supports Q2 actual results）；Meta 2026 Q2 SEC Exhibit 99.1；Amazon 2026 Q2 Form 10-Q.[^ch24-5][^ch24-6][^ch24-7][^ch24-8]  
**Note:** expectation / guidance / TTM actual 的时间窗与会计口径不同，不构成可直接相加的统一 AI hardware CapEx。

这些数字的时间窗和会计科目不同，**不能机械相加成统一 AI hardware CapEx**。历史情景中的 US$215B、US$670–750B 等统一总额如果缺乏可比口径，只能保留为旧压力测试，不进入事实层。

## 4. Seller 与 Buyer 的资本时钟不同

NVIDIA 是 system seller，hyperscaler 是 asset buyer。卖方可以在出货时先确认收入和利润，买方则在之后多年承担服务器、机房、网络、电力和长期合同的利用率与折旧风险。

因此，周期下行往往不是同步发生：

**buyer ROI 先恶化 → next-generation orders / commitments 放缓 → seller growth 后续下降 → manufacturing utilization 再向上游传导。**

这解释了为什么 seller margin 仍高，并不能证明 buyer-side ROI 一定健康；同样，buyer ROI 出现压力，也不意味着 seller economics 当季就会崩塌。

## 5. Algorithmic efficiency 既可能制造过剩，也可能延长周期

如果相同 capability 所需 compute 快速下降，而 workload volume 没有同步增长，已部署 capacity 可能出现过剩；如果更低成本刺激大量新 workload，效率提升反而会增加总基础设施需求。

本报告不再使用不可直接计算的“efficiency effect × demand elasticity”表达式，而把需求拆成两个可测量因子：

```text
Infrastructure_Demand_t
= Unit_Resource_Intensity_t
× Workload_Volume_t
```

因此相对于基准期 0：

```text
Infrastructure_Demand_t / Infrastructure_Demand_0
=
(Unit_Resource_Intensity_t / Unit_Resource_Intensity_0)
×
(Workload_Volume_t / Workload_Volume_0)
```

`Unit_Resource_Intensity` 必须绑定明确工作单位，例如 GPU-hours / verified workflow、HBM bytes / token、kWh / completed job；`Workload_Volume` 则是同一期间完成的 workflow / token / job 数量。

如果需要把价格变化与 workload volume 联系起来，可以另外引入常数弹性近似：

```text
Workload_Volume_t / Workload_Volume_0
=
(Effective_Price_t / Effective_Price_0)^(-ε)
```

其中 ε 是对**同一可比工作结果**的需求价格弹性。于是：

```text
Infrastructure_Demand_t / Infrastructure_Demand_0
=
(Unit_Resource_Intensity_t / Unit_Resource_Intensity_0)
×
(Effective_Price_t / Effective_Price_0)^(-ε)
```

**Table 24.2 — 效率下降与需求弹性的 D 级敏感性示例**

假设单位资源强度下降 40%（`URI_t / URI_0 = 0.60`），同一可验收 workflow 的有效价格下降 50%（`P_t / P_0 = 0.50`）：

| 需求弹性 ε | Workload volume factor | Infrastructure demand factor | 相对基准 |
|---:|---:|---:|---:|
| 0.5 | 1.414× | 0.849× | -15.1% |
| 1.0 | 2.000× | 1.200× | +20.0% |
| 1.2 | 2.297× | 1.378× | +37.8% |
| 1.5 | 2.828× | 1.697× | +69.7% |

**Source:** 本报告 D 级 sensitivity model。  
**Note:** 0.60、0.50 与 ε 均为示例假设，不代表当前行业 actual。该表只说明：同样的 efficiency gain，在不同需求弹性下可以导致基础设施需求下降或上升。

模型价格战同理。token/API price 下跌只能证明单位价格变化，不能单独证明 total token volume、workflow adoption 和 infrastructure utilization 同步下降。

## 6. Anchor Compute Buyer 已成为新的领先指标

OpenAI Stargate、Anthropic/AWS 等长期容量承诺使模型公司从普通租户上升为基础设施 anchor buyer。它们可以提高项目融资确定性，让数据中心、电力、芯片和内存提前建设。

这也意味着 S4 的领先信号不再只是“云厂砍 CapEx”，还包括：

- 长期模型容量承诺缩减、改期或重谈；
- GW 级项目实际 ramp 显著落后；
- 已签长期容量利用率不足；
- 上游预付款与卖方 commitments 同时放缓。

如果这些变量与 buyer utilization、市场清算价格一起转弱，资本硬着陆的证据强度会明显上升。

## 7. 清算顺序具有资产久期

短周期资产先清算，长周期资产后清算。典型顺序更接近：

**未上架 hardware / inventory → system residual value → server utilization → data-center lease → long-duration power/project economics**。

因此，S4 可能持续多年，而不是一个季度完成。电厂、变电设施和数据中心壳体不会像 GPU 库存一样快速消失，它们可能降价、换主人、重谈合同，或者在下一轮集中化中重新成为稀缺资产。

## 8. 什么才叫 S4 Capital Hard Landing

本书只有在以下四类变量出现同步恶化时，才把 S4 从压力测试上调为现实主情景：

1. **Accounting**：impairment / write-down / disposal 明显增加；
2. **Utilization / Revenue**：利用率与有效 AI revenue 持续弱于资产扩张；
3. **Market Clearing**：二手价格、租赁价格、交期、HBM/packaging clearing 同步转松；
4. **Forward Commitment**：CapEx guidance、seller commitments、Anchor Buyer contracts 与 power commitments 同时放缓或取消。

股价下跌、模型价格下降、某一季毛利波动或一个历史压力测试不满足，都不足以单独证明 S4。

## 9. 当前判断

截至 2026 年 8 月，公开事实更接近：

> **高强度资本扩张 + ROI 压力上升**

而不是已经确认的 AI-infrastructure bubble collapse。NVIDIA FY26 non-GAAP free cash flow 仍为 **US$96.575B**，[^ch24-1] FY27 Q2 GAAP operating income 为 **US$63.734B**，[^ch24-3] supply/capacity commitments 已升至 **US$279B**；[^ch24-4]同时 hyperscaler 仍在给出极高的基础设施投资口径。

这不证明未来一定软着陆。它只说明：**要宣布资本清算已经成为现实主线，还需要 utilization、clearing price、accounting losses 与 forward commitments 的同步证据。**

## References

[^ch24-1]: NVIDIA, FY26 official results, NVIDIA-defined non-GAAP free cash flow and FY26 Q4 margin, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
[^ch24-2]: NVIDIA Corporation, FY27 Q1 Form 10-Q, GAAP gross margin 74.9%, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm
[^ch24-3]: NVIDIA, FY27 Q2 official results, GAAP gross margin 75.0% and GAAP operating income US$63.734B, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^ch24-4]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^ch24-5]: Microsoft, FY26 Q4 earnings / conference call, https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast
[^ch24-6]: Alphabet, Q2 2026 earnings-call full-year CapEx guidance **US$195–205B**, company guidance reported by Reuters, 2026-07-22, https://www.reuters.com/business/google-quarterly-cloud-revenue-growth-beats-expectations-2026-07-22/ ; Alphabet SEC Exhibit 99.1 separately supports Q2 actual results, https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
[^ch24-7]: Meta Platforms, 2026 Q2 SEC Exhibit 99.1, https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm
[^ch24-8]: Amazon.com, 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm


\newpage

# Part III · 第25章：AI 与劳动市场——Task-to-Job Translation

## 1. AI 首先改变 Task，而不是职业名称

一个职业通常由多种 task 组成，其中一部分可以被自动化，一部分被增强，一部分仍需要 physical presence、judgment、liability 或 trust。

因此，最可靠的起点是 task exposure，而不是直接预测 job loss。

## 2. Exposure 不等于 Unemployment

ILO 与 IMF 的公开研究都要求把 occupational exposure 与实际 adoption、job redesign 和 employment outcome 分开。

ILO 2025 的 refined index 估计全球约**四分之一岗位存在某种 GenAI exposure**，同时强调 transformation 比简单 redundancy 更可能是主要结果。[^ch25-1]

IMF 的全球框架则估计约 **40% global employment**、约 **60% advanced-economy employment** exposed to AI。[^ch25-2]

这些都是 occupational / employment exposure，不是“同等比例任务会被自动化”，更不是同等比例岗位消失。

## 3. Adoption Economics 是技术能力到替代之间的第一道门

企业只有在：

> **AI cost + review + error + compliance + integration < human cost / value alternative**

时，才有更强替代动机。

所以 benchmark improvement 不自动转化为 employment change。

reliability、latency、security、integration 与 legal responsibility 都会改变 adoption。

## 4. 最容易被重构的是 Digital / Repeatable / Evaluable Tasks

例如 drafting、summarization、classification、routine coding、standard support 与 research assistance。

这些 task 输入输出数字化、评价标准相对清晰，更容易被 agent/workflow system 压缩。

但“任务被压缩”仍可能表现为同一岗位产出提高，而不是岗位立即取消。

## 5. Responsibility Constraint 会保留大量 Human-in-the-loop

medical sign-off、engineering sign-off、field maintenance、nuclear operations、complex negotiation、care work 等任务受到 liability、physical presence、licensing 与 trust 约束。

AI 可能改变 preparation / analysis / documentation，但最后责任仍可能由人承担。

因此 human review 既是软件成本，也是劳动转换的重要边界。

## 6. Entry-level Ladder 是最值得观察的结构变化

即使 total employment 短期没有明显下降，junior analyst、junior coder、entry-level support、routine research 等传统入门任务可能先被压缩。

传统职业路径往往是：

> junior work → experience accumulation → senior judgment

如果 junior tasks 大量自动化，企业和教育体系必须重新设计新人如何积累经验。

这可能比一个统一“失业率预测”更重要。

## 7. Wage Outcome 可能出现分化，而不是统一下降

AI 可以提高 high-skill worker leverage，同时降低 routine task value，也可能增加 system/operator/verification skill premium。

因此可能出现 top performers productivity 上升、middle routine roles 收缩、physical/system technical roles 需求提高。

劳动结果更可能是结构分化，而不是所有 knowledge workers 工资同步下降。

## 8. Physical AI 会形成第二波但更慢

warehouse、manufacturing、logistics、inspection、maintenance 等 physical tasks 的自动化还要跨过 hardware cost、reliability、safety、maintenance 与 regulation。

因此 Physical AI 的 labor translation 通常比纯 digital workflow 更慢、更资本密集。

## 9. AI Infrastructure 本身也创造新技能需求

AI expansion 同时增加 data-center technician、liquid-cooling engineer、power engineer、semiconductor process engineer、advanced-packaging engineer、network engineer、safety/compliance 与 model-infrastructure roles。

所以劳动变化是 reallocation，不是单向“AI 减少工作”。

## 10. 企业组织是否变薄，要看 Review 与 Task Volume

agent-native workflow 可能减少部分 coordination work。

但如果 task volume、exception handling、review 与 compliance 同时增加，headcount 不一定按比例减少。

更有价值的指标是 management layers、span of control、junior/senior ratio、revenue per employee 与 human-review ratio。

## 11. 当前判断

截至 2026 年，已有足够证据说明 AI 正在重构任务，但没有足够跨国证据支持一个统一“全经济岗位消失率”。

正式判断顺序应始终是：

> **先看 task automation → 再看 workflow redesign → 最后看 employment / wage outcome**

任何把 exposure percentage 直接转成 unemployment prediction 的做法，都跳过了最重要的企业采用与责任转换层。

## References

[^ch25-1]: International Labour Organization, “Generative AI and Jobs: A Refined Global Index of Occupational Exposure,” Working Paper 140, 2025, https://researchrepository.ilo.org/esploro/outputs/encyclopediaEntry/Generative-AI-and-jobs-a-refined/995653520102676
[^ch25-2]: International Monetary Fund, “Gen-AI: Artificial Intelligence and the Future of Work,” Staff Discussion Note, 2024, https://www.imf.org/-/media/Files/Publications/SDN/2024/English/SDNEA2024001.ashx


\newpage

# Part III · 第26章：AI 时代教育与人才体系

## 1. 教育目标正在从“会用 AI”上移到“理解系统”

prompting、model calling 与基础 automation 很容易随工具进化而商品化。

更耐久的能力包括 model、data、compute、memory、software、network、power、economics 与 responsibility 的跨层理解。

这与产业竞争从 single chip 上移到 system stack 是同一变化。

## 2. AI Adoption 已经快于 Curriculum / Policy

Stanford HAI 2026 AI Index Education 章节给出几个清晰信号：[^ch26-1]

- **4 out of 5** U.S. high-school and college students use AI for schoolwork；[^ch26-1]
- 只有约一半 middle/high schools 有 AI policy；[^ch26-1]
- **just 6% of teachers say those policies are clear**；[^ch26-1]
- U.S. four-year university CS undergraduate enrollment 2024→2025 **下降 11%**；[^ch26-1]
- AI software-related master's graduates 2023→2024 **增长 17%**。[^ch26-1]

这说明：

> **Tool Adoption > Curriculum Update > Institutional Reform**

教育体系的核心问题已经从“学生有没有用 AI”转向“如何验证学生是否理解、控制并对 AI 结果负责”。

## 3. 第一层：AI Literacy

所有专业都需要理解 model limitation、hallucination、source verification、privacy、data leakage、bias 与 responsible use。

它更接近新的基础数字素养，而不是 AI 专业学生的选修技能。

## 4. 第二层：AI Workflow Engineering

大量岗位不需要训练 foundation model，却需要：

- model selection；
- context / prompt design；
- retrieval；
- tool orchestration；
- evaluation；
- automation；
- human review。

这构成应用层 AI engineering。

## 5. 第三层：System Engineering

frontier AI 需要 accelerator、HBM、network、distributed computing、compiler/runtime、data center 与 power。

因此顶级 AI engineering 教育需要跨越：

> **computer science + computer architecture + systems/network + infrastructure economics**

纯模型课程无法覆盖真实产业约束。

## 6. Hardware 与 Software 不能继续完全分科

例如 inference optimization 可能同时涉及 quantization、kernel、HBM bandwidth、interconnect、batching 与 power。

所以未来 curriculum 更需要跨层实验、真实 performance/cost measurement 与 system debugging。

## 7. Multi-stack Capability 是战略技能

工程师不应只会一套 proprietary stack。

更有价值的是理解 CUDA、alternative accelerator stack、cloud custom silicon、open compiler/runtime 与 distributed frameworks，并能在多个 stack 之间迁移 workload。

教育目标不是“站队”，而是建立 portability。

## 8. Physical AI 需要新的跨学科组合

robotics / Physical AI 同时需要 control、mechanics、sensor、embedded compute、AI 与 safety。

未来稀缺人才之一会是能把 model capability 与 physical-world reliability 连接起来的 system engineer。

## 9. Power / Cooling / Operations 也属于 AI 人才体系

AI data-center buildout 让 electrical distribution、power engineering、liquid cooling、networking 与 operations 成为 AI infrastructure 的组成部分。

因此“AI 人才”不能只统计 ML engineer。

## 10. Entry-level Education 必须适应 Routine-task Automation

如果 drafting、routine coding、basic research 等入门任务被 agent 大量完成，学生需要更早接触 system debugging、verification、architecture、real-world project 与 responsibility。

否则学校会继续把大量训练时间投入最容易被自动化的 task。

## 11. Assessment 也必须改变

更合理的 project-based assessment 应要求学生同时解释：

- output correctness；
- source / evidence；
- system design；
- cost；
- reliability；
- power / resource use；
- safety / responsibility。

这比禁止 AI 工具更接近真实产业能力评价。

## 12. 当前判断

AI 教育的核心变化不是“新增一个 AI 专业”，而是：

> **把 AI 变成技术和专业教育中的系统能力，同时把 verification、portability 与 responsibility 提升为核心训练目标。**

未来最有价值的人才不会只是最会调用模型的人，而是能够理解系统、验证结果、计算经济性、跨 stack 迁移并承担现实后果的人。

## References

[^ch26-1]: Stanford Institute for Human-Centered Artificial Intelligence, “2026 AI Index Report — Education,” https://hai.stanford.edu/ai-index/2026-ai-index-report/education


\newpage

# Part IV · 第27章：研究方法与证据架构

## 1. 为什么 AI Infrastructure 研究必须先统一证据语言

AI infrastructure 同时跨越财务、semiconductor、memory、advanced packaging、cloud、power、regulation 与 labor market。不同领域的数字具有不同物理单位、会计口径、时间窗口和证据强度。

如果没有统一规则，最常见的错误包括：

- company disclosure 与 institutional forecast 混写；
- revenue share 被换算成 wafer share；
- contracted MW 被写成 energized / utilized load；
- engineering estimate 被写成 vendor disclosure；
- guidance 被写成 actual；
- future scenario 被写成 current fact；
- 同一个二手数字在多个章节重复后，被误认为 multi-source confirmation。

因此，全书使用两套互补框架：

> **F → H → M → S → X**

以及：

> **A / B / C / D evidence grade**

前者负责判断身份，后者负责证据强度。

## 2. F — Fact

Fact 必须是已经发生、可以回溯到明确公开来源的现实。

优先来源包括：

- 10-K / 20-F / annual report；
- official earnings materials；
- official product specification；
- regulator / government document；
- court filing；
- formal contract / official project disclosure。

Fact 不等于“很多媒体都这么写”。多个媒体引用同一个来源，也不构成独立多源验证。

## 3. H — Hypothesis

Hypothesis 是由事实引出的未来输入条件，但尚未被现实完全确认。

例如：

> **如果一家 system platform 持续拥有更高现金流、长期订单、预付款能力和 roadmap certainty，它获取下一代 scarce capacity 的议价能力可能提高。**

这不是 company filing 中的事实，而是可以被未来 allocation、commitment 与 delivery data 检验的研究假设。

## 4. M — Mechanism

Mechanism 必须解释事实和未来状态之间的中间变量。

例如：

> high system margin → higher cash generation → larger forward commitments → stronger capacity reservation → higher delivery certainty → stronger customer retention

机制不能退化成“因为它强，所以会更强”。至少要说明：哪个变量变化、通过什么约束传导、什么证据可以证明链条断裂。

## 5. S — Scenario

Scenario 是多个 H / M 组合后的条件状态，而不是确定预测。

本书采用四类标准情景：

- **S1 — Competitive Expansion**；
- **S2 — Baseline Concentration**；
- **S3 — Resource Hegemony**；
- **S4 — Capital Hard Landing**。

情景的作用不是给世界分配固定概率，而是回答：

> **如果一组可观察条件同时成立，产业结构更接近哪一种状态？**

## 6. X — Falsification

任何强判断都必须附带反向信号。

例如，“scarce-layer value capture 继续强化”必须在以下变量持续逆转时下调：

- supply commitments 连续下降；
- advanced packaging 不再 tight；
- HBM / DRAM residual supply 显著宽松；
- cloud frontier workload 大规模迁离 dominant stack；
- migration cost 被 open interfaces 显著降低；
- utilization 与 forward commitments 同时转弱。

没有 falsification condition 的长期叙事，不进入本书正式判断。

## 7. A / B / C / D Evidence Grade

**Table 27.1 — 本报告证据等级体系**

| 等级 | 定义 | 典型来源 |
|---|---|---|
| A | First-party / formal evidence | company filing、official product page、regulator、government、court、formal contract |
| B | Institutional research | TrendForce、ILO、IMF、Stanford HAI、academic / industry research |
| C | Sell-side / supply-chain / media estimate | investment bank、channel、supply-chain source、media estimate |
| D | Report model / stress test | geometry、arithmetic、sensitivity、scenario assumption |

**Source:** 本报告研究方法。  
**Note:** evidence grade 衡量来源强度，不等同于结论重要性；D 级模型可用于情景和 sensitivity，但不能冒充已发生事实。

例子：

- Micron HBM3E same-node/same-bits ≈ 3× DDR5 wafer supply：**A**；[^ch27-1]
- TrendForce 对 NVIDIA 2025 CoWoS demand >60% 的估计：**B**；[^ch27-2]
- 卖方对某客户具体 CoWoS 月片数的估计：**C**；
- 72 ÷ 13.4 ≈ **5.37 CoWoS wafers/rack** 的报告侧 geometry：**D**。

证据等级不会因为同一数字被多个章节重复引用而自动上升。

## 8. Dimensional Consistency：量纲比故事更优先

全书禁止以下转换：

### Revenue share ≠ wafer share

TSMC customer revenue share 不能直接变成 N2、3 nm、HPC 或 CoWoS physical share。

### Contracted MW ≠ Energized MW ≠ Utilized AI Load

up-to-1.92-GW revised PPA 不能写成 1.92 GW active AI load。[^ch27-3]

### Product spec × hypothetical quantity ≠ shipment

13.4 TB HBM3E/rack × 50,000 hypothetical racks 只能得到 D-grade scenario demand，不是 actual HBM shipment。[^ch27-4]

### Engineering geometry ≠ fab yield

5.37 CoWoS wafers/rack 是 geometry stress test，不是 TSMC disclosed yield。

### Guidance / expectation ≠ actual

company guidance 必须保留 guidance 身份，不能与另一家 TTM actual 放在同一“已发生总额”里。

## 9. Negative Evidence 的边界

“某份文件没有披露”只证明该文件范围内没有披露。

例如 CXMT 注册稿未披露 HBM product line，只能写成：

> **该注册稿未披露 HBM 产品线。**

不能扩大成“企业没有任何 HBM R&D”。

Negative evidence 的作用是限制可确认事实，不是证明现实中绝对不存在某项活动。

## 10. Forecast / Guidance / Scenario 必须保留时间身份

机构预测必须保留：

- source identity；
- publication date；
- forecast window。

例如 TrendForce “HBM + RDIMM ≈ 51% of 2026 DRAM bit supply”必须写成 **2026E institutional forecast**，不能在跨章引用后变成 2026 actual。

同理，2030 / 2036 node price、monthly packaging capacity、GW campus 等 point estimates 只能在明确假设条件下使用。

## 11. 全书核心机制模型的位置

本书使用的主要模型包括：

- **AI Resource Gravity**；
- **Scarce-layer Value Capture**；
- **AHICR — Advanced/HPC Incremental Capacity Capture Ratio**；
- **Non-AI Residual Capacity**；
- **Cloud System-Stack Substitution**；
- **Anchor Compute Buyer Effect**；
- **Rolling Bottleneck Cascade**；
- **AI Software Unit Economics**；
- **Task-to-Job Translation Layer**。

这些模型用于组织因果关系，不替代原始事实。模型的正确性最终要由新的 F 与 X 检验。

## 12. 全书去重与交叉引用原则

正式报告必须避免同一事实和机制在不同章节被反复重写：

1. 一个高影响事实表只保留一个主要位置；
2. 一个机制只完整定义一次，后续章节通过交叉引用承接；
3. 后续章节只新增 evidence、boundary、counterargument 或 falsification；
4. 同一数字跨章使用时保持原始分母、时间窗和 evidence grade；
5. source 跟随事实，不能因章节重组而丢失；
6. 修订历史、编辑过程和版本施工信息不进入正式正文。

这样做的目的不是减少信息，而是让读者能够分清“第一次定义”“新增证据”和“跨章推论”。

## 13. 正式发布标准

每一章必须同时满足：

- fact 有 source；
- forecast / institutional number 保留身份；
- sell-side estimate 不冒充 first-party；
- D-grade model 明示假设；
- future claim 条件化；
- 有 falsification condition；
- technical unit 使用标准行业符号；
- accounting / physical unit 不混用；
- 正文不携带内部 revision metadata、过程性说明或自我辩护语气。

这套方法不是为了让结论更保守，而是让情景可以更大胆，同时仍然可审计、可证伪、可更新。

## References

[^ch27-1]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^ch27-2]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^ch27-3]: Talen Energy, 2026 Q2 Form 10-Q, revised AWS PPA up to 1,920 MW, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
[^ch27-4]: NVIDIA, “GB200 NVL72,” official product page, 13.4 TB HBM3E per rack, https://www.nvidia.com/en-us/data-center/gb200-nvl72/


\newpage

# Part IV · 第28章：2026–2036 时间线与阶段性里程碑

## 1. 时间线是 Conditional Milestone Map，不是年份故事

未来十年最容易出现的错误，是把技术 roadmap、capital plan 和 power project 的目标年份写成“必然发生”。

本书把时间线分成：

- **Phase I：2026–2027**；
- **Phase II：2028–2030**；
- **Phase III：2031–2033**；
- **Phase IV：2034–2036**。

年份是观察窗口，不是事件保证。

## 2. Phase I：2026–2027 — System Race 与 Infrastructure Lock-in

当前已经确认的主要锚包括：[^ch28-1][^ch28-2][^ch28-3][^ch28-4][^ch28-5][^ch28-6]

- NVIDIA FY27 Q2 Data Center revenue **US$89.0B**；
- GAAP gross margin **75.0%**；
- Rubin **full production**；
- manufacturing, supply, and capacity commitments 由 2026-04-26 **US$119B** 升至 2026-07-26 **US$279B**；
- TSMC advanced-packaging tightness 仍限制 customer growth；[^ch28-7]
- 四大云厂公开资本投入指标仍处高位，但必须保留各自 actual / guidance / expectation 身份；[^ch28-8]
- power project 已出现约 835 MW、up to 1.92 GW、up to 500 MWe 等不同成熟度路径；
- TrendForce **预计** HBM + RDIMM 约占 2026 DRAM bit supply **51%**。

这个阶段的核心问题是：

> **AI workload demand 是否继续快于 scarce-layer supply expansion？**

主要里程碑：

- Rubin volume deployment / customer adoption；
- HBM4 ramp；
- advanced-packaging expansion 是否解除 growth constraint；
- TPU / Trainium / Maia / MTIA 新一代生产部署；
- Stargate / Anthropic 等 Anchor Buyer commitments 的实际 delivery；
- contracted power 向 energized / utilized MW 的转化；
- system-seller commitments 是否继续增长。

## 3. Phase II：2028–2030 — Substitution 是否真正形成规模

这一阶段更可能决定 S1 与 S2/S3 的分叉。

### Cloud System Stack

要看 TPU、Trainium、Maia、MTIA 是否：

- 持续承担大型 production workload；
- 在 frontier training / high-value inference 中扩大份额；
- 获得更多 external customer adoption；
- 形成稳定 utilization 与 system TCO 优势。

### Software Portability

要看 open compiler/runtime、model format、network interface 是否明显降低 CUDA / proprietary-stack migration cost。

### Memory / Packaging

要看 HBM supply 是否进入持续宽松，advanced packaging 是否不再被厂商称为 growth constraint，新 packaging architecture 是否真正提高供给弹性。

### Power

要看 headline contracted GW 有多少转化为 energized、utilized capacity，以及 Time-to-Power 是否仍决定 site selection。

## 4. Phase III：2031–2033 — 地理与产业结构开始固化

如果 AI infrastructure 持续扩大，到这一阶段竞争会进一步从产品路线转向 regional system capability。

需要观察：

- 哪些地区形成 **power + data center + chip access + software / talent** 的组合优势；
- China parallel stack 是否跨过多个 frontier closure gates；
- sovereign AI 是否形成多个 regional system ecosystems；
- supply chain 是继续跨区域互补，还是长期分区；
- advanced manufacturing redundancy 是否真正获得 qualified second-source capability。

这一阶段更重要的指标是：

- deployable compute；
- system utilization；
- energized power；
- cross-stack portability；
- regional supply resilience。

## 5. Phase IV：2034–2036 — 成熟、集中、分散或资本清算

到这一观察窗口，四类结构会更容易区分：

### Competitive Expansion

多套 system stacks 成熟，migration cost 下降，供给弹性提高，市场继续扩大但 value capture 更分散。

### Baseline Concentration

少数 dominant platforms 与 scarce-layer suppliers 长期并存，同时保持真实替代路径。

### Resource Hegemony

logic、HBM、packaging、software / interconnect 与 power 的协调能力进一步集中。

### Capital Hard Landing

已建基础设施相对 workload 过剩，产业从建设竞赛转向利用率、残值与现金流清算。

## 6. 不应预写死的未来技术节点

时间线不预设：

- exact wafer price；
- exact future-node ASP；
- exact CoWoS wafers/month；
- exact GW/rack count；
- exact company market share。

这些变量高度依赖 yield、architecture、product mix、demand、regulation 与 capital cycle。

本报告只记录可证伪的 condition / milestone，不把远期目标年份写成已发生事实。

## 7. Algorithmic Milestones

长期必须跟踪：

- memory compression；
- sparse architecture；
- quantization；
- inference scheduling；
- model routing；
- on-device capability；
- workload orchestration。

如果 unit resource intensity 大幅下降，但 total workload volume 增长更快，aggregate infrastructure demand 仍可能上升。

所以 algorithmic milestone 只有与 demand elasticity 一起观察才有意义。

## 8. Capital Milestones

每个阶段同时监测：

- hyperscaler CapEx；
- D&A / useful-life changes；
- seller supply commitments；
- Anchor Buyer contracts；
- utilization；
- second-hand / lease price；
- enterprise AI monetization；
- infrastructure financing terms。

技术 timeline 与 capital timeline 必须在同一表中读取。

## 9. Power Milestones

power 统一使用：

> **Announced → Contracted → Permitted → Energized → Utilized**

Crane、Talen/AWS、Kairos/Google 等项目都必须按当前 state 更新，不能在合同签署时直接标记为 AI power online。

尤其 Talen 2026 Q2 10-Q 的 April-2026 revised-PPA transition 状态，不等于全部物理转换或 full delivery 已完成；较早 2025 10-K 的 spring-2027 full-transition expectation 与 no-later-than-2032 ramp 仍提供物理时钟背景。[^ch28-5]

## 10. 三个决定未来结构的临界点

未来十年真正决定 S1–S4 的不是某一个年份，而是三个 threshold：

1. **System substitution 是否跨过 production frontier-workload threshold；**
2. **Scarce-layer supply 是否跨过 durable-abundance threshold；**
3. **AI workload monetization 是否跨过 capital-cost coverage threshold。**

只要这三个临界点没有同时明朗，2036 就应继续被视为条件截面，而不是确定答案。

## References

[^ch28-1]: NVIDIA, FY27 Q2 official results, Data Center revenue, GAAP margin and Rubin production status, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^ch28-2]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^ch28-3]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^ch28-4]: Constellation, Crane Clean Energy Center / Microsoft PPA, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
[^ch28-5]: Talen Energy, 2026 Q2 Form 10-Q and 2025 Form 10-K, revised AWS PPA state and ramp, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm ; https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
[^ch28-6]: Kairos Power / Google partnership, 2030 / 2035 development milestones, https://www.kairospower.com/google
[^ch28-7]: TSMC, 2Q26 Earnings Conference Transcript, packaging capacity limiting customer growth, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^ch28-8]: Microsoft FY26 Q4 earnings, https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast ; Alphabet Q2 2026 company CapEx guidance reported by Reuters, https://www.reuters.com/business/google-quarterly-cloud-revenue-growth-beats-expectations-2026-07-22/ ; Meta 2026 Q2 SEC Exhibit 99.1, https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm ; Amazon 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm


\newpage

# Part IV · 第29章：核心指标与证据监测框架

## 1. 长期研究必须设计成可更新系统

AI infrastructure 的 seller economics、CapEx、HBM、packaging、foundry allocation、power、regulation 与 system substitution 都快速变化。

因此，本报告的结论必须设计成可持续更新，而不是只在发布日期成立。

每次更新只回答三件事：

1. **哪个事实改变了？**
2. **它改变了哪个机制变量？**
3. **它是否足以改变 S1–S4 的相对权重？**

## 2. Dashboard A — Seller Economics / Forward Reservation

### NVIDIA 当前锚

**Table 29.1 — NVIDIA seller economics 与 forward-reservation 基线**

| 指标 | 当前公开值 |
|---|---:|
| FY26 Revenue | US$215.938B |
| FY26 Data Center | US$193.737B |
| FY26 NVIDIA-defined non-GAAP FCF | US$96.575B |
| FY27 Q2 Revenue | US$96.221B |
| FY27 Q2 Data Center | US$89.0B |
| FY27 Q2 GAAP gross margin | 75.0% |
| FY27 Q2 GAAP operating income | US$63.734B |
| Rubin | full production |

**Source:** NVIDIA FY26 results、FY27 Q2 results 与 FY27 Q2 Form 10-Q.[^ch29-1][^ch29-2]  
**Note:** company-defined non-GAAP FCF 与 GAAP metrics 必须保留各自口径；commitments 为 aggregate amount，未披露 supplier-level split。

Supply / capacity commitments：[^ch29-2]

- 2026-01-25：US$95.2B；
- 2026-04-26：US$119B；
- 2026-07-26：US$279B。

这组指标回答：system seller 是否仍拥有足够 cash generation 与 forward commitment ability 预订下一代 scarce resources。

US$279B 不具有 supplier-level split，不能拆成 TSMC / HBM vendor revenue。[^ch29-2]

## 3. Dashboard B — Foundry / Packaging

### TSMC 2025

以下基线来自 TSMC 2025 Annual Report。[^ch29-3]

- 12-inch-equivalent wafer shipments：~15.0M；
- annual capacity：>17M；
- 3 nm / 5 nm / 7 nm wafer revenue：24% / 36% / 14%；
- ≤7 nm：74%；
- HPC platform：58%，YoY +48%；
- smartphone platform：29%，YoY +11%；
- largest / second-largest annual customer：19% / 17% revenue。

另一匿名客户表才支持 2024→2025：Customer A 12%→19%，Customer B 22%→17%。[^ch29-7] 两套披露不能拼成同一客户轨迹。

### Packaging

A-grade signal：TSMC 持续描述 packaging capacity tight / growth-limiting。[^ch29-8]

B-grade signal：TrendForce 估计 NVIDIA 占 2025 CoWoS demand >60%。[^ch29-9]

TSMC 未披露 customer-level CoWoS allocation。

## 4. Dashboard C — Memory

### A-grade manufacturing anchor

Micron：HBM3E same-node / same-bits ≈ **3× DDR5 wafer supply**；FY25 10-K 进一步确认 HBM 需要更多 wafers / cleanroom space。[^ch29-5]

### B-grade forward structure

TrendForce：**2026E HBM + RDIMM ≈51% of DRAM bit supply**。[^ch29-4]

### Vendor economics

SK hynix FY25：Revenue KRW97.1467T、Operating profit KRW47.2063T、Operating margin 49%、Net income KRW42.9479T；HBM revenue more than doubled YoY。[^ch29-6]

这组指标用于判断 HBM product mix 是否继续吸收 DRAM manufacturing input，以及 conventional DRAM residual capacity 是否松动。

## 5. Dashboard D — Hyperscaler CapEx

Microsoft、Amazon、Alphabet、Meta 必须逐家公司保存：

- accounting line item；
- fiscal / calendar window；
- actual vs guidance / expectation；
- finance-lease treatment；
- AI/data-center specific disclosure。

监测重点不是“总额创新高”本身，而是新增 capital 是否继续流向 server、network、memory、custom silicon、data center 与 power。

不同口径不得机械相加成 official AI hardware CapEx。

## 6. Dashboard E — Power State Machine

**Table 29.2 — Power project state machine**

| 状态 | 解释 |
|---|---|
| Announced | 项目 / 目标公布 |
| Contracted | 合同成立 |
| Permitted | 关键许可获得 |
| Energized | 实际送电 |
| Utilized | 形成真实负载 |

**Source:** 本报告 power-state framework。  
**Note:** state machine 用于防止把 headline MW/GW、contract quantity 或 project target 写成 active AI load。

当前代表性项目：

- Microsoft / Constellation：~835 MW restart PPA；[^ch29-10]
- Talen / AWS：up to 1.92 GW revised PPA；April-2026 transition status 不能写成 full physical delivery complete；[^ch29-11]
- Google / Kairos：Hermes 2 up to 50 MWe in 2030，fleet up to 500 MWe by 2035。[^ch29-12]

真正需要更新的是 ramp、energized MW、actual load 与 utilization。

## 7. Dashboard F — System-Stack Substitution

对 Google / AWS / Microsoft / Meta，分别跟踪：

- production workload share；
- external availability；
- compiler/runtime maturity；
- large-cluster scaling；
- migration cost；
- utilization；
- system TCO。

单颗 chip benchmark 不是充分替代指标。

## 8. Dashboard G — China Parallel Stack

分别监测：

### Logic

domestic accelerator、foundry scale、yield / volume disclosure。

### Memory

HBM-class product、qualification、volume production。

### Packaging

advanced integration、yield、scale。

### Software

compiler/runtime、framework compatibility、cluster utilization。

### Deployment

frontier workload、data-center power、real system scale。

只有多个 closure gates 同时改善，才上调 frontier-system closure。

## 9. Dashboard H — Regulation

法律状态机统一记录：

> inquiry / RFI → investigation → Statement of Objections / formal complaint → formal proceeding → final decision → remedy / fine

禁止：

- inquiry → “已经起诉”；
- statutory ceiling → “即将罚款”；
- merger review → “已经认定垄断”。

真正改变 scenario 的变量是 interface openness、tying restriction、access / supply remedy 与 structural change。

## 10. Dashboard I — Capital Clearing

### Accounting

impairment、inventory write-down、accelerated depreciation、asset disposal。

### Utilization / Revenue

compute utilization、AI workflow revenue、revenue per deployed compute。

### Market Clearing

used-system price、cloud discount、lease rate、delivery lead time。

### Forward Commitment

CapEx guidance、seller commitments、Anchor Buyer contracts、power contracts。

只有多组信号同步恶化，S4 才从 stress test 升级为主情景。

## 11. Evidence-grade 快速规则

**Table 29.3 — 更新时的默认 evidence grade**

| 数据类型 | 默认等级 |
|---|---|
| company filing / official product / government / court / formal contract | A |
| institutional research | B |
| sell-side / supply-chain / media estimate | C |
| report geometry / stress test / hypothetical rack count | D |

**Source:** 本报告证据方法（见第27章）。  
**Note:** 默认等级可因来源质量上调或下调，但不能因重复引用自动升级。

任何更新都必须保持原始等级；数字更新不等于证据等级自动提升。

## 12. Scenario Weighting 的更新规则

### 向 S1 移动

system substitution 扩大、migration cost 下降、HBM/packaging/power 供给弹性改善、multi-buyer resource access 增强。

### 向 S3 移动

seller commitments 继续扩大、多层 scarcity 持续、switching cost 上升、powered capacity 被少数 anchor buyers 长期锁定。

### 向 S4 移动

utilization、market-clearing price、CapEx / commitments 与 accounting losses 同步恶化。

### 留在 S2

dominant platform economics 强，但 alternative stacks 继续发展；scarce layers 仍紧但持续扩产；CapEx 高且 ROI 仍可支撑。

## 12A. 可执行监测门槛：从“持续/显著”变成触发规则

为了避免“长期”“明显”“大规模”只停留在形容词层，本报告给监测系统增加一套 **D 级 operational trigger policy**。它是研究更新规则，不是行业事实，也不是证券交易信号。

**Table 29.4 — 核心变量的观察频率、持续期与情景触发规则**

| 变量组 | 默认观察频率 | 默认持续期 | 触发规则 |
|---|---|---|---|
| Seller economics / forward commitments | quarterly | 2 consecutive quarters | commitments 或下一代供给承诺连续下降/取消，才记为趋势性 weakening；单季波动只记 observation |
| HBM / DRAM allocation & pricing | monthly + quarterly | 3 monthly observations 或 2 quarters | allocation fulfillment、contract pricing、lead time 与 Absolute AI Capacity Gap 至少两项同向改善，才记为 supply-easing trend |
| Advanced packaging | quarterly + event-driven | 2 quarters | 一手供应商连续两个季度不再把 packaging 描述为 growth constraint，且 B 级 lead-time / pricing 指标同步改善，才上调 S1 supply-elasticity 权重 |
| Cloud system-stack substitution | quarterly + major launch/deployment | 2 reporting periods | production workload、external availability、migration cost / software maturity 中至少两项连续改善，才记为可执行 substitution |
| Power / Time-to-Power | quarterly | 2 quarters | contracted / permitted MW 向 energized MW 的转化持续改善，并伴随部署等待时间下降，才记为 power bottleneck 缓解 |
| Anchor Compute Buyer | event-driven + quarterly | 2 observations when recurring | 正式扩容/履约支持 S2/S3；大规模延期、重谈、取消只有与 utilization 或 financing signal 同向时才上调 S4 |
| Capital clearing | quarterly | **2 consecutive quarters** | Accounting、Utilization/Revenue、Market Clearing、Forward Commitment **四类同时恶化**并持续两个季度，S4 才从 stress case 上调为主情景候选 |
| Regulation | event-driven | legal-state transition | inquiry/RFI 不触发结构重估；formal proceeding / final remedy 只有实质改变 interface、tying、access 或 supply 条件时才改变 S1–S3 weighting |

**Source:** 本报告 D 级 monitoring policy。  
**Note:** “2 quarters / 3 months”是默认更新纪律，用于防止单点新闻改写长期判断；当某数据只有年度披露或事件型披露时，应使用最近两个可比 observation，而不是伪造季度数据。

### 缺数据时的处理

如果某一层无法得到同单位的 `AI_Effective_Demand` 与 `AI_Effective_Capacity`，该层 Absolute AI Capacity Gap 必须标记为 **not measurable from public data**。此时可以跟踪 Growth Gap、lead time、pricing、allocation fulfillment 等 proxy，但不能把 proxy 重新命名成绝对产能缺口。

### Scenario weighting 的最低证据组合

- **向 S1 显著移动**：Supply Elasticity、System Substitution、Buyer Optionality 三组中至少两组满足持续期规则；
- **向 S3 显著移动**：Multi-layer Scarcity、Switching Cost、Forward Reservation 三组同时强化，并持续至少两个可比 observation；
- **向 S4 显著移动**：沿用第24章硬门槛，四类 capital-clearing signal 同时恶化并持续两个季度；
- **否则维持 S2 或仅做局部权重微调**，不因为单一 headline 改主情景。

## 13. 更新纪律

一条新闻不应该重写全书。

只有当新事实改变了核心机制变量，并跨过预先定义的 threshold，才修改 scenario weighting。

这使报告能够长期更新，而不是在每次产品发布、股价波动或传闻后改写产业故事。

## References

[^ch29-1]: NVIDIA, FY26 and FY27 Q2 official results, seller economics and Rubin status, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026 ; https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^ch29-2]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^ch29-3]: TSMC, 2025 Annual Report, https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^ch29-4]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^ch29-5]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E wafer-supply trade ratio, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^ch29-6]: SK hynix, FY25 Financial Results, https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
[^ch29-7]: TSMC, 2025 Consolidated Report, anonymized Customer A/B revenue series, https://www.sec.gov/Archives/edgar/data/1046179/000104617926000024/a2025q4consolidatedreport-.htm
[^ch29-8]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging tightness limiting customer growth, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^ch29-9]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^ch29-10]: Constellation, Crane Clean Energy Center / Microsoft 20-year PPA and approximately 835 MW unit, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
[^ch29-11]: Talen Energy, 2026 Q2 Form 10-Q and 2025 Form 10-K, revised AWS PPA state and ramp, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm ; https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
[^ch29-12]: Kairos Power / Google partnership, Hermes 2 up to 50 MWe in 2030 and fleet up to 500 MWe by 2035, https://www.kairospower.com/google


\newpage

# Part IV · 第30章：S1–S4 四类标准情景

## 1. Scenario Analysis 不是 Point Forecast

本书不为 2030 或 2036 给出一个唯一答案，也不使用固定 40% / 30% / 15% / 15% 之类权重。

情景由以下变量共同决定：

- advanced-capacity allocation；
- HBM supply；
- advanced packaging；
- cloud system-stack substitution；
- Anchor Buyer long-duration demand；
- power / Time-to-Power；
- software migration；
- China parallel stack；
- regulation；
- utilization；
- CapEx / financing discipline。

## 2. S1 — Competitive Expansion / 竞争性扩容

### 定义

AI demand 继续增长，但供给扩张与替代系统成熟速度足以降低 concentration。

典型条件：

- leading-edge capacity 扩张并有更多 qualified supply；
- HBM supply elasticity 提高；
- advanced-packaging tightness 显著缓解；
- cloud custom systems 承担大量真实 workload；
- open software / interfaces 降低 migration cost；
- power / energized capacity 跟上 buildout；
- 多套 system stacks 在 production 中长期并存。

### 经济结果

dominant platform 仍然很大，但 buyer optionality 和 bargaining power 提高，scarcity premium 下行，value capture 更分散。

这是：

> **market expands + concentration declines**

而不是“AI infrastructure 消失”。

## 3. S2 — Baseline Concentration / 基准集中

### 定义

当前主要趋势延续：

- AI demand 高；
- leading system-platform seller economics 强；
- HBM / advanced packaging 仍周期性 tight；
- cloud custom systems 继续扩大但未全面替代 frontier workload；
- power 进入独立部署约束；
- China parallel stack 持续扩展但 frontier closure 未完全完成；
- CapEx / forward commitments 仍高。

### 经济结果

市场继续高速扩大，同时 value capture 集中在少数 system platforms 与 scarce-layer suppliers。

截至 2026 年 8 月，这是最接近当前事实组合的**基准状态**，不是十年固定预测。

## 4. S3 — Resource Hegemony / 资源霸权

### 定义

demand growth 持续快于 substitution 与 supply expansion，多个 scarce layers 同时集中。

典型条件：

- advanced packaging 长期供不应求；
- HBM manufacturing intensity / generation constraint 持续；
- leading-edge incremental capacity 高度集中；
- proprietary software / interconnect migration cost 仍高；
- cloud custom systems 只能局部分流；
- powered land / firm MW 被少数大型 buyers 长期锁定；
- Anchor Buyer 与 seller forward commitments 持续扩大。

### 机制

> high profit → stronger commitments / prepayment → greater future resource reservation → higher delivery certainty → stronger installed base / workload retention

它描述的是 system-level resource coordination 强化，不是法律意义上的 monopoly verdict。

## 5. S4 — Capital Hard Landing / 资本硬着陆

### 定义

AI workload demand、utilization 与 monetization 无法覆盖快速增长的资本基数。

典型同步信号：

- token / workflow volume 增长不足；
- instance / lease price 快速下跌；
- utilization 下降；
- enterprise AI monetization 弱；
- hyperscaler CapEx guidance 下调；
- seller / Anchor Buyer commitments 缩减或取消；
- used hardware residual value 快速下跌；
- impairment / write-down 上升。

### 清算顺序

首先承压通常是：

- next-generation hardware orders；
- inventory；
- short-lived system residual value；
- speculative / highly concentrated financing。

如果弱势持续，才进一步传导到 semiconductor CapEx、data-center expansion 与 power buildout。

S4 不等于 AI usage 消失；资本清算之后，低价 compute 仍可能刺激新的 application demand。

## 5.1 四类标准情景的比较框架

**Table 30.1 — S1–S4 的核心驱动、主要结果与反向信号**

| 情景 | 核心驱动 | 主要产业结果 | 关键反向信号 |
|---|---|---|---|
| S1 — Competitive Expansion | supply elasticity、multi-sourcing、portability 上升 | value capture 更分散，buyer optionality 提高 | scarce-layer tightness 重新强化、migration cost 回升 |
| S2 — Baseline Concentration | demand 强、dominant platforms 强、替代持续但不完全 | 高增长与集中并存 | supply/substitution 明显改善或 ROI/commitments 同步恶化 |
| S3 — Resource Hegemony | 多层 scarcity + switching cost + forward reservation 强化 | incremental capacity 更集中，后来者复制成本提高 | capacity access 分散、open interfaces 显著降低迁移成本 |
| S4 — Capital Hard Landing | utilization / monetization 弱于资本基数 | clearing、orders、CapEx 与资产价值下行 | utilization、clearing price 和 forward commitments 恢复 |

**Source:** 本报告 S1–S4 scenario framework。  
**Note:** 四类情景是并列条件状态，不赋固定概率，也不是必然连续阶段。

## 5A. AI Capacity Gap：S1–S4 的跨情景诊断轴

S1–S4 保持为并列条件状态，不新增第二套情景命名。为了区分“当前是否短缺”和“短缺压力如何变化”，本报告使用两个互补指标。

### 绝对缺口

```text
AI_Capacity_Gap_i(t)
= AI_Effective_Demand_i(t)
- AI_Effective_Capacity_i(t)
```

Demand 与 Capacity 必须在同一物理层、同一交付窗口、同一 qualification / quality boundary 下计算，单位可以是 wafers/month、qualified package starts/month、bits/year 或 MW。

- **Absolute Gap > 0**：当前可交付供给不足；
- **Absolute Gap ≈ 0**：当前供需接近平衡；
- **Absolute Gap < 0**：当前存在有效余量。

### 增长缺口

```text
AI_Capacity_Growth_Gap_i(t)
= Growth(AI_Effective_Demand_i(t))
- Growth(AI_Effective_Capacity_i(t))
```

Growth Gap 用同一期间的增长率差表示，只描述绝对缺口未来更可能扩大还是收敛：

- **Growth Gap > 0**：短缺可能扩大，或既有余量被侵蚀；
- **Growth Gap < 0**：短缺可能收敛，或有效余量扩大；
- **Growth Gap = 0**：供需以相同速度变化，不代表当前不存在短缺。

因此：

- **Absolute Gap > 0 且 Growth Gap > 0，且跨多个关键层持续**：稀缺强化，S2 / S3 权重上升；
- **Absolute Gap > 0 但 Growth Gap < 0**：仍短缺，但供给正在追赶，S1 权重可能上升；
- **Absolute Gap < 0 且 utilization 健康**：供给出现余量，但不等于 S4；
- **Absolute Gap < 0 + utilization 下滑 + clearing price 恶化 + commitments 收缩**：S4 权重显著上升。

AI Capacity Gap / Growth Gap 必须与 Non-AI Residual Capacity 联合读取：前两者回答 AI 自身当前缺多少、缺口怎么变化；NARC 回答优先分配以后非 AI 市场还能拿到多少有效供给。

## 6. 五类决定情景的变量

### Supply

leading-edge wafers、HBM、advanced packaging、power。

### Substitution

cloud custom systems、open compiler/runtime、alternative interconnect、China parallel stack。

### Demand

token/workflow volume、enterprise adoption、Anchor Buyer commitments、sovereign demand。

### Finance

seller cash generation、hyperscaler CapEx、depreciation、utilization、financing cost、residual value。

### Regulation / Geopolitics

export control、antitrust remedy、interface openness、industrial policy、regional fragmentation。

## 7. Anchor Compute Buyer 是新的情景变量

大型 model companies 的多年 compute commitments 已经可以影响 infrastructure financing、custom silicon、power 与 data-center buildout。

如果 Anchor Buyer Demand 持续扩大并兑现 utilization，S2/S3 权重提高。

如果长期 commitments 大规模改期、重谈或利用不足，S4 权重明显提高。

所以 model-company contracts 不能再被当作普通 cloud customer spending。

## 8. S2 → S1 的可观察信号

- alternative system stacks 在 frontier / high-value production workload 中规模化；
- HBM / packaging lead time 持续下降；
- advanced capacity access 更分散；
- open software / interfaces 明显降低 migration cost；
- power expansion 缩短 Time-to-Power；
- buyer multi-sourcing 变成生产常态。

## 9. S2 → S3 的可观察信号

- seller forward commitments 持续快速扩大；
- HBM / packaging tightness 跨代持续；
- proprietary system switching cost 上升；
- leading-edge incremental supply 持续高集中；
- scarce power / powered land 被少数 anchor buyers 长期锁定；
- alternative stacks 无法在 production scale 形成足够选择权。

## 10. S2 → S4 的可观察信号

- CapEx guidance 连续下降；
- utilization 下降；
- seller / Anchor Buyer commitments 取消或明显收缩；
- second-hand system clearing price 快速下跌；
- cloud discounts / lease rates 明显恶化；
- impairment 增加；
- enterprise AI monetization 长期弱于 depreciation / operating cost。

## 11. 为什么 S1、S2、S3、S4 不是顺序阶段

它们是并列条件状态。

例如，某些区域可能出现 S3-style power scarcity，同时某些 workload 已进入 S1-style multi-stack competition；memory 可能暂时进入宽松，而 packaging 仍 tight；capital market 可能局部清算，但 productive workload 继续增长。

因此，全书用 scenario weighting 描述**相对结构**，不把产业强行塞进单一路径。

## 12. 当前基准

截至 2026 年 8 月，本报告的 baseline 是：

> **S2 — Baseline Concentration**

主要原因是：

- NVIDIA / leading platform seller economics 仍强；[^ch30-1]
- HBM 与 advanced packaging 仍是关键 bottlenecks；[^ch30-2][^ch30-3]
- cloud custom systems 已形成真实竞争，但尚未证明全面替代 frontier workload；[^ch30-4]
- infrastructure CapEx 与 forward commitments 仍高；[^ch30-5]
- power constraint 上升；[^ch30-6]
- China parallel stack 尚未在所有 frontier critical layers 形成等价闭环；
- 全行业 Capital Hard Landing 的同步证据尚不足。

这条 baseline 只在上述事实组合继续成立时有效。

## 13. Scenario Framework 的最终用途

未来每次更新时，不问：

> “哪一个十年预测被证明了？”

而问：

> **“哪些可观察变量改变了，S1–S4 的相对权重应如何调整？”**

这使远期判断可以随产业事实更新，而不依赖一次性押注。

## References

[^ch30-1]: NVIDIA, FY27 Q2 official results, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^ch30-2]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E wafer-supply trade ratio, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^ch30-3]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging tightness limiting customer growth, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^ch30-4]: Google Ironwood TPU, https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; AWS Trainium3 UltraServers, https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ ; Microsoft Maia 200, https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ ; Meta MTIA 300, https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
[^ch30-5]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^ch30-6]: NVIDIA, DGX GB200 Hardware Guide, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html ; Talen Energy, 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm

## 交叉引用

- 第29章：核心指标与证据监测框架
- 第32章：总判
- 核心假设矩阵


\newpage

# Part IV · 第31章：2036 终局与战略选择

## 1. 2036 不是一个市场份额预测点

本书不预测 2036 年某家公司拥有多少市场份额，也不赋固定情景概率。2036 的作用是把当前机制拉到更长时间尺度，观察哪些变量如果持续成立，会把产业带向不同结构。

竞争单位已经从单颗芯片上移到 system stack。frontier AI system 同时依赖 advanced logic、HBM、advanced packaging、interconnect、compiler/runtime、rack/pod、data center、power、capital 与可持续 workload demand。

因此，2036 真正的问题不是“谁有最好的一颗芯片”，而是：

> **这些层最终由少数平台高度协调，还是由多套可互操作系统共同提供？**

## 2. 本章使用的事实锚与对应章节

**Table 31.1 — 长期战略判断所依赖的核心结构变量**

| 结构变量 | 对应章节 |
|---|---|
| NVIDIA system stack / switching cost | Part I · Ch02 |
| HBM / memory resource intensity | Part I · Ch05 |
| Advanced Packaging / CoWoS | Part I · Ch06 |
| Power / Time-to-Power | Part I · Ch07 |
| Hyperscaler second system stack | Part II · Ch12 |
| China frontier-system closure | Part II · Ch17 |
| Value Capture Map | Part III · Ch20 |
| Capital clearing / S4 signals | Part III · Ch24 |

**Source:** 本报告章节体系。  
**Note:** 本章只承接前文章节已经建立的事实与机制，不重复复制高影响数据表。

终局章不复制这些章节的财务表和物理公式，只使用已经建立的变量进行情景与行动分析。

## 3. S1 — Competitive Expansion：多系统栈共存

如果 advanced manufacturing、HBM、packaging 与 power 供给弹性提高，同时 cloud custom systems、open compiler/runtime 和 interoperability 显著降低迁移成本，产业会更接近 S1。

可能的结构是：

- NVIDIA 仍是主要通用平台之一；
- Google/AWS/Microsoft/Meta system stacks 在大量 workload 中成熟；
- 多家买方能稳定获得 leading-edge manufacturing；
- open software / interfaces 降低跨栈迁移摩擦；
- China parallel stack 的 system closure 提高；
- value capture 从单一 dominant platform 向 cloud、specialized supplier 与 application/workflow 更分散。

S1 不是“所有硬件商品化”，而是**替代路径足够真实，买方拥有可执行选择权**。

## 4. S2 — Baseline Concentration：高集中与持续竞争并存

S2 的结构是：少数大型 system platform 和 scarce-layer supplier 保持强 value capture，同时 cloud custom silicon、中国平行栈和开放软件持续形成竞争压力。

这意味着：

- 通用 frontier workload 仍高度依赖成熟 system platform；
- cloud 自研在内部 workload 持续扩大；
- HBM / packaging / power 仍周期性形成物理约束；
- buyer 会主动保留第二系统，但不会立即放弃主栈；
- 上游资源分配仍受长期订单、现金流、roadmap certainty 和客户多元化共同影响。

截至 2026 年 8 月，本报告把 S2 作为最接近当前事实组合的**基准状态**，不是不可改变的十年预测。[^ch31-1][^ch31-2][^ch31-3]

## 5. S3 — Resource Hegemony：真正的门槛是复制整套基础设施

S3 不要求某家公司拥有一个夸张的单点市场份额。它的核心是多个 scarce layer 同时高度集中：

- leading-edge capacity；
- HBM；
- advanced packaging；
- scale-up / software interfaces；
- powered land / firm MW；
- long-duration supply commitments。

在这种状态下，后来者面对的不是“设计出更快 accelerator”，而是需要同时复制 manufacturing、memory、packaging、software、power 与 customer migration path。

资本进入门槛会显著上升，Non-AI Residual Capacity 也更容易受到挤压。

## 6. S4 — Capital Hard Landing：资本清算不等于 AI 消失

如果 utilization、effective revenue、market-clearing price 和 forward commitments 同步恶化，产业会进入 S4。

此时可能出现：

- hardware residual value 下跌；
- next-generation orders 放缓；
- hyperscaler / model-company commitments 改期；
- data-center / power 长资产面临低利用率；
- model/application margin 继续压缩；
- 过剩 compute 的使用价格显著下降。

但资本清算与技术扩散可以同时发生。历史上的 fiber、telecom 与 cloud 都显示：**overbuild → asset-price decline → cheaper access → new applications** 是一种可能路径。

所以 S4 的长期结果未必是“AI 失败”，也可能是从建设竞赛转向利用率、workflow 和现金流竞赛。

## 7. 2036 的四个真正分水岭

到更长期，以下四个问题比任何单一市场份额更重要：

1. **System stacks 是否可互操作？**
2. **Scarce manufacturing / memory / packaging 是否足够多元？**
3. **Power / powered land 是否长期成为配额？**
4. **AI workload 是否产生足够现金流覆盖基础设施与资本成本？**

它们分别决定 switching cost、supply elasticity、deployment geography 和资本可持续性。

## 8. 企业：先证明 Workflow Economics，再锁长期 Compute

企业部署 AI 的顺序应当是：

1. 找到可量化的真实 workflow；
2. 建立 evaluation / verification；
3. 计算 cost per completed task 与业务价值；
4. 保留 model / cloud / data portability；
5. 根据需求确定性再决定长期 compute commitment。

高确定性的 workload 可以使用较长期 reservation；不确定的实验和快速变化模型则应保留 flexible / multi-provider 路径。

最危险的顺序是先锁大量长期 capacity，再寻找足以填满它的业务场景。

## 9. 企业：主栈可以集中，但第二路径必须可执行

portability 不意味着所有供应商平均采购。更有效的策略是：

> **主栈追求效率，第二路径追求可执行性。**

至少要保留：

- model portability；
- data portability；
- cloud portability；
- accelerator / runtime optionality；
- open interface；
- workload benchmark 与 cost observability。

第二路径的价值在于降低供应、价格、政策和迁移的单点风险。

## 10. 资本：先区分资产类型，再谈“AI 估值”

至少要把四类资产分开：

**Table 31.2 — AI 相关资产的主要价值来源与风险**

| 资产 | 主要价值 | 主要风险 |
|---|---|---|
| Platform | switching cost / system definition / ecosystem | substitution / regulation |
| Manufacturing | scarcity / yield / technology / capacity | cycle / CapEx / utilization |
| Infrastructure | powered land / grid / data center / duration | utilization / duration mismatch |
| Application | workflow / distribution / data | commoditization / unit economics |

**Source:** 本报告 Value Capture / Duration framework。  
**Note:** 分类用于战略分析，不构成证券估值、评级或投资建议。

高 CapEx 既可能是进入壁垒和增长准备，也可能是未来 depreciation 与 stranded asset。资本判断必须同时看 CapEx、utilization、revenue、FCF、forward commitments 与 clearing price。

## 11. 资本：最危险的不是高估值，而是 Duration Mismatch

短周期 compute demand 如果匹配 long-duration debt、PPA、data-center shells 与 transmission assets，一旦 workload 不及预期，清算会比硬件库存慢得多。

因此，资本配置的核心问题是：

> **demand duration 是否与 asset duration 匹配？**

高需求情景下，长资产是 moat；S4 下，同一资产可能成为长期负担。

## 12. 国家：竞争单位已经不是一座 Fab

完整 frontier AI industrial capability 至少需要：

- equipment / materials；
- advanced logic；
- HBM；
- advanced packaging；
- interconnect；
- compiler/runtime；
- data center；
- power / grid；
- talent / production operations。

因此，单纯补贴先进 fab 无法形成 system closure。制造、memory、packaging、software 与 power 必须在同一产业政策框架中。

## 13. 国家：Power Policy 已经是 Compute Policy

高功率 rack 将 grid planning、generation、interconnection、substation、cooling 和 permit 拉进技术竞争。

如果 chip supply 增长而 time-to-power 不改善，就会形成“有 hardware、无法按期上电”的资产错配。

国家层面的 AI infrastructure strategy 因而需要同时管理：

> **semiconductor clock + power-permitting clock + capital clock**。

## 14. 国家：Interoperability 是战略选择权

系统韧性并不要求拒绝领先平台，而要求避免所有关键层同时依赖一个不可替代入口。

长期应提高：

- open compiler/runtime；
- portable model / data formats；
- interoperable networking；
- multi-architecture engineering education；
- cross-stack production benchmarking。

其目标不是人为平均市场份额，而是让替代路径在供应中断、政策变化或价格失衡时真正可执行。

## 15. 中国：长期关键不是“国产化率”，而是 Frontier System Closure

China parallel stack 是否改变全球资源结构，不取决于一个总国产化率，而取决于 advanced logic、HBM、packaging、interconnect、compiler/runtime、frontier workload 与 power 是否同时达到可验证规模。

smartphone / consumer supply success 不能直接证明 frontier AI closure；同样，frontier AI 的高级约束也不能否定中国在消费、制造与国内 workload 上已经存在的大规模产业基础。

如果七个 closure gate 逐步跨越，中国将形成第二个更强的资源重力中心；如果多个关键 advanced layer 长期未闭环，则 parallel stack 的价值更多体现为 domestic resilience 和部分 workload substitution。

## 16. 个人：长期价值来自对结果负责，而不是绑定某一个工具

当模型、IDE、agent 与生成工具快速商品化，最脆弱的个人定位是把职业价值完全绑定到某一个具体工具的操作方法。

更耐久的能力包括：

- domain knowledge；
- problem decomposition；
- workflow / system design；
- verification；
- cross-stack portability；
- 对结果、风险和质量负责的能力。

工具降低执行门槛后，能够定义问题、验证结果和承担交付责任的能力反而更重要。

## 17. 监测框架：什么会让我们改判

未来不靠“十年后必然如此”维持观点，而靠公开信号持续校准：

- NVIDIA / major system seller commitments 是否持续扩大或开始收缩；
- cloud custom stacks 的 production workload share 与迁移成本；
- HBM / advanced-packaging tightness 是否显著缓解；
- leading-edge capacity 是否更分散；
- energized MW / time-to-power 是否改善；
- Anchor Compute Buyer commitments 是否兑现；
- hyperscaler utilization / AI monetization 是否覆盖资本基数；
- China frontier-system closure gates 是否出现一手规模化证据；
- regulation 是否真正降低 interface / tying / switching barriers。

如果供给弹性和 interoperability 同时提高，权重向 S1 移动；如果 multiple scarce layers 与 switching cost 同时强化，向 S3 移动；如果 utilization、clearing price、CapEx 与 commitments 同步转弱，向 S4 移动。

## 18. 最终战略判断

截至 2026 年 8 月，本报告最合理的总体描述是：

> **AI infrastructure 仍处于高速扩张与高集中并存阶段，竞争单位正在从单颗芯片上移到完整 system stack 与基础设施。**

这不是“永久垄断”判断，也不是“算力迅速商品化”判断。它意味着未来十年的竞争会围绕 system substitution、scarce-layer supply、Anchor Buyer demand、power、utilization、capital duration 与 regulation 反复重新分配。

对所有主体，最重要的共同策略可以压缩成一句：

> **不要押注一个不可改变的终局；建立能够在终局改变时仍然可执行的选择权。**

## References

[^ch31-1]: NVIDIA, FY27 Q2 official results, current system-platform economics, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^ch31-2]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging supply constraint, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^ch31-3]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html

## 交叉引用

- 核心证据台账
- 核心参考文献索引
- Part I · Ch02 NVIDIA System Stack
- Part I · Ch05 HBM
- Part I · Ch06 Advanced Packaging
- Part I · Ch07 Power
- Part II · Ch12 Hyperscaler System Stack
- Part II · Ch17 China Parallel Stack
- Part III · Ch20 Value Capture Map
- Part III · Ch24 Capital Clearing


\newpage

# Part IV · 第32章：总判——从事实、机制到可证伪的长期判断

## 1. 全书的研究语法：F → H → M → S → X

本书所有强判断必须经过五层：

- **F — Fact**：已经发生并可公开核验的事实；
- **H — Hypothesis**：未来输入条件或压力测试假设；
- **M — Mechanism**：事实与假设之间的因果传导；
- **S — Scenario**：多个条件组合形成的未来状态；
- **X — Falsification**：足以迫使原判断下调、重写或失效的反向信号。

这套结构的意义，是防止一个数字在跨章节引用中从“估计”逐渐升级成“事实”，也防止未来判断因为叙事强度而失去证伪条件。

## 2. 第一总判：竞争单位已经从单颗芯片上移到 System Stack

截至 2026 年 8 月，AI infrastructure 的竞争已经不能用 GPU share 或单颗 ASIC benchmark 描述。完整竞争单位包括 advanced logic、HBM、advanced packaging、scale-up / scale-out interconnect、compiler/runtime、rack/pod、data center、power 与 workload。

NVIDIA 当前最强的优势来自把这些层组织成成熟的通用商业 system stack，而不是“拥有所有物理资源”。Google、AWS、Microsoft、Meta 也已从 custom chip 向 software、interconnect、rack/pod 和 captive workload 延伸。

因此未来竞争的主问题是：

> **谁能以更低迁移成本、更高利用率和更稳定供应，把完整 system 持续交付给真实 workload。**

这比“谁有更快的一颗芯片”更接近产业权力本体。

## 3. 第二总判：价值捕获来自 Scarce Layer + Switching Cost，而不是简单市场份额

高利润本身不能直接证明垄断，客户收入份额也不能直接换算成 wafer / CoWoS allocation。

本书使用 **Scarce-layer Value Capture** 描述更窄的机制：如果一个平台同时具备强现金流、长期订单、系统定义权、迁移成本和 supply orchestration，它更有能力提前承诺下一代稀缺资源，从而提高交付确定性。

NVIDIA manufacturing, supply, and capacity commitments 已从 2026-01-25 的 **US$95.2B** 上升到 2026-07-26 的 **US$279B**。[^ch32-1]这证明整体前置供应承诺显著扩大，但公开文件没有把 US$279B 拆分到 TSMC、CoWoS 或任何单一 HBM vendor，因此不能把它写成某家供应商的确定收入。

真正需要跟踪的变量不是历史 customer revenue share，而是：

> **Incremental Scarce-Capacity Capture**

即某个平台在下一代 advanced logic、HBM、packaging 和其他关键增量资源中能持续获得多少有效供给。

### 3.1 Quantity Assurance：极端紧缺时，价格不是唯一清算机制

在 severe shortage 中，真正决定买方能否持续生产的，不只是 willingness-to-pay，还包括 long-term agreement、credit quality、prepayment、purchase scale 与 allocation fulfillment。

因此必须分开：

> **willingness-to-pay ≠ guaranteed quantity**

系统性风险不是“价格上涨”本身，而是 Non-AI Residual Capacity / non-anchor-buyer access 降到足够低，使次级买家即使接受更高报价，也无法获得足够、按时、可持续的交付量。

这条机制比“某一家拿走100%产能”的绝对化说法更可审计。

## 4. 第三总判：HBM、Advanced Packaging 和 Power 是彼此独立的物理池

这三个约束不能用同一个产能数字替代。

### HBM

Micron 一手披露：在 same node / same bits 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。[^ch32-2] TrendForce 预计 2026 年 HBM + RDIMM 合计约占 DRAM bit supply **51%**。[^ch32-3]前者是同-bit manufacturing trade ratio，后者是 2026E bit-supply forecast；两者都不能改写成 HBM market share 或 wafer share。

### Advanced Packaging

TSMC 已一手确认 advanced-packaging capacity tight，并在 2026 Q2 表示 packaging tightness 已限制客户增长。[^ch32-4]TSMC 没有公开 customer-level CoWoS allocation，因此 TrendForce 对 NVIDIA >60% CoWoS demand 的估计只能作为 B 级机构锚。

### Power

约 120 kW-class rack、Crane 约835 MW restart、Talen/AWS up to 1.92 GW revised PPA 和 Kairos/Google 的长期开发路径说明 power 已成为独立物理约束。[^ch32-5]但 Contracted、Permitted、Energized 和 Utilized MW 必须严格分开。

因此，一个 bottleneck 缓解后，另一个 bottleneck 可以上升。这就是 **Rolling Bottleneck Cascade**。

## 5. 第四总判：Non-AI Residual Capacity 比“总供给增长”更有解释力

AI/server demand 上升时，总 wafer、DRAM 或 packaging capacity 即使继续增长，传统终端实际获得的供给也未必增加。

本书用 **Non-AI Residual Capacity** 表示：

> **总供给 − AI / anchor demand 吸收 − 其他优先高价值需求之后，非 AI 市场真正可获得的有效残量。**

这一框架可以解释 memory、consumer GPU 和部分 leading-edge allocation 的价格/配置压力，而无需使用“AI 抢走所有芯片”这种过度叙述。

它也意味着“扩产”与“传统行业恢复宽松”不是同义词。

## 5A. Two-Speed Semiconductor Economy：AI 正在改变“下一美元资本投向哪里”

截至 2026 年，最值得关注的结构变化已经不只是某一季度谁获得更多 wafer，而是未来供给为了谁而建设。

TSMC 2026 Q2 的 platform revenue mix 中，HPC 占 **66%**、Smartphone 占 **22%**；同季 advanced technologies（7 nm 及以下）占 wafer revenue **77%**。TSMC 同时把 2026 年 capital budget 上调至 **US$60B–64B**，主要投向 advanced process technologies，并继续投入 advanced packaging、testing 等。上述数字不能把 HPC 全部等同于 AI，也不能推出 Apple、高通或其他单一客户被“挤掉”；它们能够支持的更窄结论是：高增长 HPC/AI workload 正在显著影响先进制造的增量资本形成。[^ch32-6]

memory 侧同样出现资源优先级变化。Samsung 2026 Q2 表示，在 limited capacity 下 Memory Business 重点满足 server products，并预计 2026 H2 server DRAM、eSSD、HBM demand 加速；[^ch32-7] SK hynix 2026-08-07 宣布 Yongin Y2 与 Cheongju M17 两个项目合计约 **KRW54T** 的中长期投资，分别扩展 DRAM 与 NAND 生产基础。[^ch32-8]

因此，本书把这一宏观状态定义为 **Two-Speed Semiconductor Economy**：

> **AI Infrastructure Economy 的边际需求由少数高资本强度买方集中拉动，而 Traditional Device Economy 继续受到 BOM、零售价格弹性与换机周期约束；两者共享部分上游资源，却拥有不同的价格承受能力和资本形成能力。**

这不是“消费电子被献祭”的事实判决。更准确的长期命题是：半导体产业的边际需求决定权正在增加对少数 hyperscaler、system-platform seller 与 Anchor Compute Buyer CapEx 的依赖，产业由 **Demand Diversification** 向更高程度的 **Capital Concentration** 移动。

是否形成永久结构，取决于 AI Capacity Gap、NARC、utilization、pricing feedback 与未来扩产是否重新建立供需平衡。

## 6. 第五总判：Cloud Custom Silicon 是平台替代，同时也是上游资源竞争

Google TPU/Ironwood、AWS Trainium、Microsoft Maia、Meta MTIA 已证明 hyperscaler 的反击不是裸片，而是第二类 system stack。[^ch32-9]

这会同时产生：

1. **Platform-profit diversion**：部分 workload 不再支付完整外部平台 economics；
2. **Upstream resource competition**：custom systems 自己仍需要 advanced logic、HBM、packaging 与 power。

所以 custom silicon 成功并不自动让上游稀缺缓解。真正决定 S1 Competitive Expansion 能否增强的是 production workload share、migration cost、system utilization 和外部 adoption，而不是产品发布数量。

## 7. 第六总判：模型公司正在成为 Anchor Compute Buyer

OpenAI Stargate、Anthropic/AWS 等长期基础设施承诺显示，头部 model company 已不只是 cloud tenant。[^ch32-10]

它们的长期需求可以：

**提高项目融资确定性 → 促进 cloud / data center / power / chip 提前建设 → 获得更稳定 capacity → 支撑更大 workload。**

这形成 **Anchor Compute Buyer Effect**。

同时，它也是资本周期风险放大器。如果长期需求承诺改期、利用率不足或商业收入无法兑现，原本支持建设的确定性会转化成 stranded-capacity / duration-mismatch 风险。

因此，model-company long-duration commitment 已成为与 hyperscaler CapEx、NVIDIA supply commitments 同级的重要领先指标。

## 8. 第七总判：中国已经形成真实 Parallel Stack，但 Frontier Closure 必须逐层验证

中国供给能力不能用单一“国产化率”判断。

- smartphone / consumer computing：平行供给基础较强；
- PC / workstation：替代能力扩大，但 software compatibility 和专业 workload 仍重要；
- frontier AI：已经形成真实 accelerator/software parallel stack，但完整等价 system 仍需 advanced logic、HBM-class memory、advanced packaging、interconnect、compiler/runtime、frontier workload 和 power 同时规模化。

CXMT 注册稿披露 DDR/LPDDR，但未披露 HBM product line。其招股书引用 Omdia 的可审计口径是：按 **2025Q2 DRAM 销售额**测算，CXMT 全球份额约 **3.97%**、全球第四；[^ch32-11]因此“CXMT 已有 8% 全球 DRAM 份额”不进入事实层。

Counterpoint Research 对 YMTC 的最新口径则是 **2026Q2 NAND shipment share 约14%、全球第三**；[^ch32-12] 同一机构 2026Q1 的 **13%** 是 NAND revenue share。[^ch32-13]两者分母不同，不能拼成同一连续时间序列。

此外，domestic memory capacity growth 不等于 upstream manufacturing autonomy。关键 equipment、software/licensing、spare parts/field service 与 materials qualification 的连续性，仍决定新增产能能否 ramp、既有产线能否维持 yield、下一代工艺能否持续迭代。

TrendForce 2026 Q1 的 SMIC 5.1% 是 foundry revenue share，不是 frontier-AI capability。[^ch32-14]

因此最准确的状态不是“已经全面追平”或“完全没有替代”，而是：

> **中国已经跨过没有替代系统的阶段，但尚未有公开证据证明所有 frontier critical layers 都达到全球等价规模闭环。**

## 9. 第八总判：资本周期的核心不是 CapEx 大小，而是 Utilization 与 Duration

Cloud CapEx、system-vendor revenue、foundry revenue、memory revenue 与 power investment 不能直接相加成“全球 AI 总投入”，因为同一美元会在产业链不同账本重复出现。

AI infrastructure 的资本风险来自：

- 短周期 compute asset；
- 中周期 network / data-center equipment；
- 长周期 shell / grid / PPA；
- 未来 workload revenue。

它们的时间尺度并不一致。

所以真正的泡沫判断必须观察 Accounting、Utilization/Revenue、Market Clearing 与 Forward Commitment 四类信号是否同步恶化，而不是只看股价、模型降价或一个 headline CapEx 总数。

截至 2026 年 8 月，公开事实更符合：

> **高强度资本扩张 + ROI 压力上升**

而不是已经确认的全行业 Capital Hard Landing。

## 10. “算力成为认知生产资料”是条件命题，不是技术神话

本书使用“生产资料化”描述一个可检验的经济变化，而不是赋予模型主体性。

条件是：一个 AI system 能否在给定 compute、energy 和资本成本下，持续完成过去需要人工逐步完成、且可以验收的工作流。

如果不能稳定完成和验收，compute 仍主要是辅助工具；如果能够大规模持续完成并产生可验证经济价值，compute、memory、packaging、power 和 software stack 就会更接近生产性基础设施。

因此，真正的衡量单位不是“模型多聪明”，而是：

> **cost per verified workflow outcome + capital required to sustain it**。

这也是为什么模型能力、基础设施投入和业务收入必须放进同一个单位经济框架。

## 11. 2030 / 2036 的单点价格和产能不是本书事实

node price、CoWoS monthly capacity、HBM future trade ratio、GW-scale campus 与 trillion-dollar CapEx 等远期单点值，只能在明确标记的 scenario / stress-test 条件下使用。

出版版统一规则是：

- 没有一手公开披露的历史数字，不进入 F；
- 2030/2036 单点值只可作为明确标记的 H / D 级 scenario input；
- 机构 forecast 保留机构身份和时间窗口；
- 公司 guidance 不写成 actual；
- 不因为同一个数字被多次引用就提高证据等级。

因此，本书的远期结论依赖变量和机制，而不是依赖某个精确的 2036 数字。

## 12. S1–S4 是条件状态，不是作者概率表

### S1 — Competitive Expansion

供给弹性提高、cloud/custom systems 成熟、interoperability 降低 switching cost，value capture 更分散。

### S2 — Baseline Concentration

少数 system platforms 与 scarce-layer suppliers 保持强经济性，同时替代路线持续发展。当前事实组合最接近这一基准状态。

### S3 — Resource Hegemony

多个 scarce layers 与 switching cost 同时强化，后来者必须复制更完整的 infrastructure stack。

### S4 — Capital Hard Landing

utilization、clearing price、CapEx / commitments 与 accounting losses 同步恶化，资本进入清算。

这四个状态不赋固定世界频率。公开事实变化后，相对权重必须更新。

## 13. 什么会迫使本书改判

以下反向信号具有高证伪价值：

- NVIDIA / leading system-platform supply commitments 持续下降或大规模取消；
- advanced packaging 不再被描述为 growth constraint；
- HBM / DRAM residual supply 显著宽松；
- cloud custom systems 在 frontier workload 上形成大规模、低迁移成本替代；
- open interfaces 明显降低 CUDA / proprietary-fabric switching cost；
- energized power 快速扩张，Time-to-Power 不再构成项目差异；
- Anchor Compute Buyer commitments 大规模改期或利用不足；
- hyperscaler AI monetization 长期无法覆盖新增资本基数；
- China parallel stack 的多个 frontier closure gates 获得或失去规模化一手证据；
- 正式监管 remedy 实质性改变 tying、interface 或市场进入条件。

如果这些信号与当前机制相反，本书必须修改，而不是用“长期仍然成立”解释所有失败。

## 14. 最终总判

截至 2026 年 8 月，本书的核心结论可以压缩为五句话：

**第一，AI infrastructure 的竞争单位已经从 chip 上移到 system stack。**

**第二，真正决定价值捕获的是 scarce-layer access、switching cost、supply coordination、quantity assurance 与 workflow monetization，而不是单一市场份额。**

**第三，HBM、advanced packaging、power 和 capital duration 构成彼此独立、会轮换的约束，cloud custom systems 与 China parallel stack 正在增加替代路径，但尚未消除这些物理约束。**

**第四，大型 model companies 已经成为能够前置拉动基础设施建设的 Anchor Compute Buyers；同一机制也会在利用率不足时放大 duration risk。**

**第五，未来不是一条确定曲线。S1–S4 的相对权重必须由 supply elasticity、system substitution、Anchor Buyer demand、utilization、power、regulation 和 frontier-system closure 的公开事实持续更新。**

因此，这份研究的目标不是给出一个“2036 年必然结果”，而是建立一套能够随事实更新的工业分析框架。

> **预测可以错，证据边界不能乱；情景可以大胆，事实层必须保守；真正有价值的长期研究，不是一次猜中终局，而是知道什么事实出现时必须改变自己的判断。**

## 交叉引用

- 核心证据台账
- 核心参考文献索引
- Part I · Ch02 NVIDIA System Stack
- Part I · Ch05 HBM
- Part I · Ch06 Advanced Packaging
- Part I · Ch07 Power
- Part II · Ch12 Hyperscaler System Stack
- Part II · Ch17 China Parallel Stack
- Part III · Ch20 Value Capture Map
- Part III · Ch24 Capital Clearing
- Part IV · Ch31 Strategy & Endgame

## References

[^ch32-1]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^ch32-2]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^ch32-3]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^ch32-4]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging tightness limiting customer growth, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^ch32-5]: NVIDIA, DGX GB200 Hardware Guide, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html ; Constellation, Crane Clean Energy Center, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs ; Talen Energy, 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm ; Kairos Power / Google, https://www.kairospower.com/google
[^ch32-6]: TSMC, 2Q26 Quarterly Results and Earnings Conference, platform mix and capital budget, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^ch32-7]: Samsung Electronics, 2Q26 Results, memory product prioritization and 2H26 demand outlook, https://news.samsung.com/global/samsung-electronics-announces-second-quarter-2026-results
[^ch32-8]: SK hynix, 2026-08-07, Yongin Y2 and Cheongju M17 investment plan, https://news.skhynix.com/en/fab-facility-investment-2026/
[^ch32-9]: Google Ironwood TPU, https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; AWS Trainium3 UltraServers, https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ ; Microsoft Maia 200, https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ ; Meta MTIA 300, https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
[^ch32-10]: OpenAI, Stargate infrastructure disclosures, https://openai.com/index/announcing-the-stargate-project/ ; Anthropic, AWS compute collaboration, https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
[^ch32-11]: CXMT 2025 prospectus / Omdia, 2025 Q2 DRAM revenue share 3.97%, https://static.sse.com.cn/stock/disclosure/announcement/c/202512/002170_20251230_B8QS.pdf
[^ch32-12]: Counterpoint Research, 2026 Q2, YMTC 14% NAND shipment share, https://counterpointresearch.com/en/insights/server-led-essds-hit-48-percent-of-nand-shipments
[^ch32-13]: Counterpoint Research, 2026 Q1, YMTC 13% NAND revenue share, https://counterpointresearch.com/en/insights/global-nand-memory-market-share
[^ch32-14]: TrendForce, 2026-06-12, 1Q26 foundry revenue shares, https://www.trendforce.com/presscenter/news/20260612-13095.html
