# 第一卷：执行摘要与未来十年核心判断

## 1. 核心结论

AI 基础设施竞争正在从“单颗芯片竞争”上移为“系统栈竞争”。决定长期价值捕获能力的，不再只是 GPU 市占率，而是先进逻辑、HBM、先进封装、互联、编译器与运行时、整柜系统、数据中心以及电力等关键稀缺层，能否被同一平台持续协调并形成跨代优势。

本报告将这一机制定义为 **Scarce-layer Value Capture（稀缺层价值捕获）**。这一概念并不预设任何企业能够永久垄断市场，而是强调：当某个平台同时具备高利润、高自由现金流、长期订单、软件迁移成本和系统级产品定义权时，其预订下一代稀缺资源的能力通常更强，也更有可能把本代优势延续到下一代。

NVIDIA 当前最重要的变化，是销售单元已经从单卡上移至 rack-scale system。GB200 NVL72 的官方配置为 **72 Blackwell GPU、36 Grace CPU、13.4 TB HBM3E、17 TB LPDDR5X**。客户采购对象由单颗芯片扩展为计算、互联、内存、软件和机柜共同组成的系统。

因此，Google TPU/Ironwood、AWS Trainium、Microsoft Maia、Meta MTIA 等路线也不应再被简化为“ASIC 对 GPU”。真正的竞争单位，是包含编译器、运行时、互联、机柜/Pod、大规模内部工作负载和供应链能力在内的完整 system stack。

## 2. 当前事实基础

### 2.1 NVIDIA：平台利润与资源预订能力

NVIDIA FY26（截至 2026-01-25）官方数据如下：

| 指标 | FY26 |
|---|---:|
| Revenue | **US$215.938B** |
| Data Center revenue | **US$193.737B** |
| GAAP gross margin | **71.1%** |
| Operating income | **US$130.387B** |
| Net income | **US$120.067B** |
| Non-GAAP free cash flow（NVIDIA 定义） | **US$96.575B** |
| R&D | **US$18.497B** |

主要来源：
- SEC CFO commentary: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26cfocommentary.htm
- NVIDIA FY26 results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
- FY26 10-K: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm

FY27 Q2（截至 2026-07-26）进一步显示平台盈利能力仍处于高位：

| 指标 | FY27 Q2 |
|---|---:|
| Revenue | **US$96.221B** |
| Data Center revenue | **US$89.0B** |
| GAAP gross margin | **75.0%** |
| GAAP operating income | **US$63.734B** |
| Net income | **US$59.688B** |
| Vera Rubin | **full production** |
| FY27 Q3 revenue guidance | **US$108.0B ±2%** |

FY26 的 H20 相关减值并未改变当前平台利润结构。到 FY27 Q2，GAAP gross margin 已回到 75.0%。

更重要的是资源承诺。NVIDIA manufacturing, supply, and capacity commitments 由 2026-01-25 的 **US$95.2B** 上升至 2026-04-26 的 **US$119B**，并在 2026-07-26 进一步升至 **US$279B**。FY27 Q2 10-Q 说明，最新承诺主要关联 data-center infrastructure systems 所需的 memory 与 manufacturing facilities，用于 current / future architectures 的长期需求。

需要特别说明的是，公开文件并未将这 **US$279B** 拆分至 TSMC、CoWoS、SK hynix、Micron 或 Samsung，因此该数字只能说明 NVIDIA 的整体供应与产能承诺规模，不能直接视为任何单一供应商的收入。来源：https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm 。

### 2.2 TSMC：先进制造与先进封装仍是核心物理约束

TSMC 2025 年公开数据包括：

| 指标 | 2025 |
|---|---:|
| 12-inch equivalent wafer shipments | 约 **15.0M** |
| 年产能 | 超过 **17M** |
| 3 nm wafer revenue share | **24%** |
| 5 nm wafer revenue share | **36%** |
| 7 nm wafer revenue share | **14%** |
| ≤7 nm wafer revenue share | **74%** |
| HPC platform share | **58% of 2025 net revenue**；platform revenue YoY **+48%** |
| Smartphone platform share | **29% of 2025 net revenue**；platform revenue YoY **+11%** |
| Largest customer revenue share | **19%** |
| Second-largest customer revenue share | **17%** |
| Back-end revenue disclosure | 2024：**advanced packaging and testing >8%**；2025：**advanced packaging slightly over 10%**（company-corrected；两年标签不完全同口径） |

TSMC 管理层关于先进封装的公开表述，是判断供给约束的重要一手依据。2024 Q4，魏哲家称相关产能“very tight”，并表示无法满足全部客户需求；2026 Q2，又明确指出 packaging capacity 已经紧到限制客户增长。

这里需要严格区分三个不同概念：

1. 客户年度收入占比；
2. leading-edge wafer share；
3. CoWoS customer share。

TSMC 的 19% 最大客户收入占比既不是 N2 wafer share，也不是 CoWoS share；公司同样没有披露 CoWoS 客户级分配表。因此，客户对先进制造资源的影响应通过**增量资源捕获能力**分析，而不能把年度营收占比机械换算成 wafer share。

### 2.3 HBM：AI 对存储供给的影响已经进入晶圆层

Micron FY24 Q2 prepared remarks 提供了一条关键的一手物理锚：在相同 technology node、生产相同比特时，HBM3E 约需要 DDR5 **3× 的 wafer supply**。Micron FY25 10-K 又进一步确认，HBM 为生产相同比特需要更多 wafers 与 cleanroom space。

因此，约 3× 应作为 **A 级公司一手证据**使用。它代表 HBM3E 相对 DDR5 的行业级 wafer-supply trade ratio，而不是每座 fab 固定不变的 MES 常数。

TrendForce 的机构研究进一步显示，2026 年 HBM + RDIMM 约占 DRAM bits 的 **51%**。这意味着 AI 与服务器需求不仅吸收高价值 HBM，也正在改变 conventional DRAM 的剩余供给结构。

### 2.4 Cloud CapEx：规模巨大，但口径不可混用

Microsoft、Amazon、Alphabet、Meta 的 CapEx 均处于历史高位，但不同公司的时间窗口和会计科目并不一致。

2025 混年口径下，四家公司设备购置合计约 **$354B** 量级；2026 年 Microsoft、Alphabet、Meta 已给出更高的公开 CapEx 预期或指引，Amazon 的 TTM net PPE 也继续上升。

这些数字不能直接等同于“AI hardware CapEx”，原因在于：

- Amazon 同时包含 fulfillment/network infrastructure；
- Meta 包含非 AI 基础设施；
- Alphabet 包含办公及其他技术设施；
- Microsoft 的财年与其他公司的日历年并不完全一致。

因此，更有分析价值的问题不是“四家公司一共花了多少钱”，而是 AI server、network、memory、data center、power 与自研 silicon 在各自投资结构中的占比是否持续提高。

## 3. 稀缺层价值捕获机制

### 3.1 从芯片竞争到系统栈竞争

AI 基础设施至少包含八个相互依赖的层：

1. Advanced logic
2. HBM / DRAM
3. Advanced packaging
4. Scale-up / scale-out interconnect
5. Compiler / runtime / framework
6. Rack / pod / system design
7. Data center
8. Power

单独替代其中一个层，并不等同于替代整个系统。

Cloud custom silicon 可以减少 NVIDIA 在芯片、互联或软件层的利润捕获，但如果新系统仍需要先进节点、HBM、advanced packaging 和大规模电力，它同时会强化对上游稀缺资源的竞争。这两种作用可以同时发生，并不矛盾。

### 3.2 增量资源比历史份额更重要

本报告采用 **AHICR（Advanced HPC Incremental Capacity Capture Ratio）**，观察下一代先进 AI/HPC 增量资源的捕获程度。

历史客户收入占比只能描述过去的收入结构。真正影响下一代竞争的变量包括：

- long-duration orders
- prepayment
- credit quality
- utilization
- roadmap certainty
- supplier diversification
- geopolitics

因此，本报告不采用“TSMC 必然偏向某一家客户”的单因素判断。更准确的机制是：当某一买方在订单规模、预付款能力、信用、利用率和 roadmap certainty 上显著领先时，其对下一批增量产能的议价能力会上升；与此同时，供应商仍然存在客户多元化、长期议价权和地缘风险管理的动机。

### 3.3 Non-AI Residual Capacity

AI 需求扩大后，消费电子和传统服务器真正面对的并不是“AI 把所有晶圆拿走”，而是 **Non-AI Residual Capacity（非 AI 剩余产能）** 的变化。

这种挤压具有明显的层级差异：

- Smartphone 仍是 TSMC 第二大平台；
- PC 和 conventional server 仍然存在；
- Automotive 具有独立认证周期和节点结构；
- HBM、RDIMM、advanced packaging、power management 等与 AI/服务器共用的资源，更容易受到高价值需求重排。

因此，“AI 挤压消费电子”应理解为特定稀缺层上的 residual capacity 下降，而不是整个半导体行业停止服务非 AI 市场。

## 4. 中国供给栈：必须分层讨论

中国供给能力既不能被压缩成“只能做手机”，也不能被表述为“已经完成 frontier AI 全栈替代”。更合理的分析方式，是按供给层级分别判断。

### 第一层：Smartphone / consumer computing

中国已经能够形成相对完整的平行供给，包括部分逻辑、DRAM/NAND、终端设计、系统软件和整机生态。

### 第二层：PC / workstation / general computing

替代能力正在提高，但仍受到 CPU/GPU 生态、先进节点、软件兼容和高性能存储等因素约束。

### 第三层：frontier AI system stack

若要实现与当前最先进平台的等价替代，需要同时解决：

- advanced logic
- HBM-class memory
- advanced packaging
- high-speed interconnect
- compiler/runtime
- distributed training software
- large-scale system deployment

CXMT 招股材料没有披露 HBM 产品线。这只能解释为“该文件未披露”，不能进一步推导为“企业不存在任何 HBM R&D”。

因此，中国栈是否能够形成第二个全球级资源重力中心，仍属于未来情景变量，而不是已经完成的事实。

## 5. 1999 Intel 为什么不是完全可比对象

Intel 1999 年主要财务数据：

| 指标 | 1999 |
|---|---:|
| Net revenue | **US$29.389B** |
| Gross margin | 约 **59.7%** |
| Operating income | **US$9.767B** |
| Net income | **US$7.314B** |

公开来源：Intel Corporation 1999 Annual Report  
https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-05/history-1999-annual-report.pdf

Intel 当时的优势主要集中在 CPU、x86 软件兼容和自有制造。

今天的 AI 平台优势更加分散，也更加系统化。要削弱一个领先 AI system stack，不仅需要第二颗性能接近的芯片，还需要：

- 可迁移的软件栈；
- 可扩展的高速互联；
- 可获得的 HBM；
- 可获得的 advanced packaging；
- 可部署的 rack/pod；
- 足够的数据中心与电力；
- 足够大的真实 workload。

因此，“芯片份额下降”和“平台价值捕获下降”不能视为同一个事件。

## 6. 五类主要打断机制

当前主线并非不可逆。至少有五类变量可能改变稀缺层价值捕获：

1. **Cloud system-stack substitution**  
   Google、AWS、Microsoft、Meta 的系统栈在训练和推理中持续扩大替代范围。

2. **Buyer coordination**  
   大型买方通过联合标准、软件兼容和长期采购形成更强的第二买盘。

3. **Power constraint**  
   已采购系统无法按时上电，导致 utilization、提货和下一轮订单下降。

4. **China parallel stack**  
   中国在 advanced logic、HBM、packaging、interconnect 与 software 上形成足够规模的平行系统。

5. **Regulatory structural remedy**  
   强制开放接口、限制 tying、供应约束或结构性分拆真正降低迁移成本。

这些变量必须通过公开、可验证的事件判断，而不能依赖单一新闻标题或情绪化叙事。

## 7. 当前基准情景

截至 2026 年 8 月，最符合当前事实的基准方向仍然是：

- AI system sales unit 继续向 rack/pod 上移；
- NVIDIA seller-side economics 仍然很强；
- advanced packaging 与 HBM 继续保持稀缺；
- cloud custom silicon 持续分流平台利润，但尚未消除对先进上游资源的需求；
- power 正在成为与 packaging/HBM 并列的重要部署约束；
- 中国供给栈继续扩张，但 frontier AI 等价替代尚未完全闭环。

这一组合对应正式情景矩阵中的 **S2 — Baseline Concentration**，而不是“永久垄断”。

如果 Cloud system-stack substitution、buyer coordination 或 China parallel stack 明显加速，系统可能向 **S1 — Competitive Expansion** 转移；如果先进资源进一步集中，并伴随软件与互联锁定增强，则可能向 **S3 — Resource Hegemony** 转移；如果 utilization、token economics、CapEx 和后续供应承诺同时转弱，则可能进入 **S4 — Capital Hard Landing**。

## 8. 证伪条件

以下变化出现时，应主动下调“稀缺层价值捕获继续强化”的判断：

- NVIDIA supply commitments 连续下降或出现大规模取消；
- advanced packaging 不再被 TSMC 描述为 growth constraint；
- HBM/DRAM 供给重新显著宽松；
- cloud custom silicon 在 frontier training 中形成规模化迁移；
- CUDA/NVLink 等迁移成本被开放接口显著降低；
- 大规模 AI data center 出现持续低 utilization；
- power connection 成为公开披露的提货延期主因；
- 中国平行 AI system stack 在先进逻辑、HBM、packaging、interconnect 与 software 上形成可验证规模。

反过来，如果上述变量没有出现，而 seller cash flow、capacity commitments、HBM demand 与 advanced packaging tightness 继续同步增强，则 S2 向 S3 偏移的可能性会上升。

---

本卷采用统一证据分级体系。公司一手披露、机构研究、卖方估计与本报告压力测试分别按 A/B/C/D 等级处理，具体定义见 [《研究方法与证据分级》](研究方法与证据分级.md) 与 [《核心证据台账》](核心证据台账.md)。

## 本卷关键公开来源

- NVIDIA GB200 NVL72 official product page（36 Grace CPU、72 Blackwell GPU、13.4 TB HBM3E、17 TB LPDDR5X）：https://www.nvidia.com/en-us/data-center/gb200-nvl72/
- NVIDIA FY26 official results：https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
- NVIDIA FY26 10-K：https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
- NVIDIA FY27 Q2 official results：https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- NVIDIA FY27 Q2 10-Q（US$279B manufacturing, supply, and capacity commitments）：https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
- TSMC 2025 Annual Report：https://investor.tsmc.com/static/annualReports/2025/english/index.html
- TSMC 4Q25 Presentation（2025 platform mix / growth）：https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
- TSMC 4Q24 Transcript（advanced packaging and testing >8%）：https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf
- TSMC 4Q25 Transcript（2025 advanced packaging slightly over 10%，company-corrected）：https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
- TSMC 2Q26 Earnings Conference Transcript（packaging capacity limits customers' growth）：https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
- TSMC 2025 20-F（annual customer rankings）：https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm
- TSMC 2025 consolidated report（Customer A/B）：https://www.sec.gov/Archives/edgar/data/1046179/000104617926000024/a2025q4consolidatedreport-.htm
- TrendForce（2026E HBM + RDIMM = 51% of DRAM bit supply）：https://www.trendforce.com/presscenter/news/20260825-13198.html
- Micron FY24 Q2 event page：https://investors.micron.com/events/event-details/microns-second-quarter-2024-financial-call
- Micron FY24 Q2 Prepared Remarks（HBM3E ≈ 3× DDR5 wafer supply）：https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- Microsoft FY26 Q4 earnings / call：https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast
- Alphabet 2026 Q2 SEC Exhibit 99.1：https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
- Meta 2026 Q2 SEC Exhibit 99.1：https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm
- Amazon 2026 Q2 Form 10-Q：https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
