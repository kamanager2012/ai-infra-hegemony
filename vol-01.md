# 第一卷：执行摘要与未来十年核心判断

## 1. 核心结论

AI 基础设施竞争正在从“单颗芯片竞争”上移为“系统栈竞争”。决定长期价值捕获的，不再只是 GPU 市占率，而是先进逻辑、HBM、先进封装、互联、编译器/运行时、整柜系统、数据中心与电力等稀缺层能否被同一平台持续协调和锁定。

本报告将这一机制定义为 **Scarce-layer Value Capture（稀缺层价值捕获）**。其核心不是“某家公司永远垄断”，而是：当某个平台同时拥有高利润、高自由现金流、长期订单、软件迁移成本和系统级产品定义权时，它更有能力预订下一代稀缺资源，并把优势从本代延续到下一代。

NVIDIA 当前最重要的变化，不是“过去卖 GPU、现在也卖 GPU”，而是销售单元已经从单卡上移到 rack-scale system。GB200 NVL72 的官方配置为 **72 Blackwell GPU、36 Grace CPU、13.4 TB HBM3E、17 TB LPDDR5X**。客户采购的对象因此从单颗芯片扩展为计算、互联、内存、软件和机柜共同组成的系统。

这也改变了竞争单位。Google TPU/Ironwood、AWS Trainium、Microsoft Maia、Meta MTIA 等自研路线并不只是“ASIC 对 GPU”。真正的竞争是：谁能用自己的编译器、运行时、互联、机柜/Pod 和大规模内部工作负载，形成可持续的替代系统栈。

## 2. 当前事实锚

### 2.1 NVIDIA：平台利润与资源预订能力

NVIDIA FY26（截至 2026-01-25）官方数据：

- Revenue：**$215.938B**
- Data Center revenue：**$193.737B**
- GAAP gross margin：**71.1%**
- Operating income：**$130.387B**
- Net income：**$120.067B**
- Free cash flow：**$96.575B**
- R&D：**$18.497B**

来源：
- SEC CFO commentary: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26cfocommentary.htm
- NVIDIA FY26 results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
- FY26 10-K: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm

FY27 Q2（截至 2026-07-26）进一步把这一趋势推高：

- Revenue：**$96.221B**
- Data Center revenue：**$89.0B**
- GAAP gross margin：**75.0%**
- GAAP operating income：**$63.734B**
- Net income：**$59.688B**
- Vera Rubin：**full production**
- FY27 Q3 revenue guidance：**$108.0B ±2%**

因此，FY26 的 H20 相关减值没有改变当前平台利润结构。到 FY27 Q2，毛利率已重新回到 75.0%。

更重要的是资源承诺。NVIDIA 供应相关承诺从 FY26 年末的 **$95.2B** 上升至 FY27 Q1 的 **$119.0B**。官方披露同时确认公司使用 prepaid manufacturing and capacity agreements 为当前和未来产品锁定制造与产能。公开文件并未把这 $119.0B 拆分到 TSMC、CoWoS、SK hynix、Micron 或 Samsung，因此不能把供应承诺直接等同于某一家供应商的收入。

### 2.2 TSMC：先进制造与先进封装仍是核心物理约束

TSMC 2025 年公开数据：

- 12-inch equivalent wafer shipments：约 **15.0M**
- 年产能：超过 **17M**
- 3 nm：晶圆收入 **24%**
- 5 nm：**36%**
- 7 nm：**14%**
- ≤7 nm：**74%**
- HPC platform：**58%**，同比 +48%
- Smartphone：**29%**
- Largest customer：年度营收 **19%**
- Second-largest customer：**17%**
- Advanced packaging + testing：2024 年约 **8%**，2025 年略高于 **10%**

TSMC 管理层对先进封装的表述比任何供应链传闻更关键。2024 Q4 魏哲家称产能“very tight”且无法满足客户需求；2026 Q2 又明确表示 packaging capacity 已经紧到限制客户增长。

这里必须保持两个边界：

1. TSMC 的 19% 客户收入占比不是 N2 wafer share，也不是 CoWoS share。
2. TSMC 并未披露 CoWoS 客户级分配表。

因此，客户对先进制造资源的影响应通过**增量资源捕获能力**分析，而不是把年度营收占比机械换算成 wafer share。

### 2.3 HBM：AI 对存储供给的影响已经进入晶圆层

Micron FY24 Q3 prepared remarks 给出了一条重要的一手物理锚：

> 在相同 technology node、生产相同比特时，HBM3E 约需要 DDR5 **3× 的 wafer supply**。

Micron FY25 10-K 又确认：HBM 为生产相同比特需要更多 wafers 与 cleanroom space。

因此，约 3× 应作为 **A 级公司一手证据**使用。它代表 HBM3E 相对 DDR5 的行业级 wafer-supply trade ratio，不是每座 fab 固定不变的 MES 常数。

TrendForce 的机构研究进一步显示，2026 年 HBM + RDIMM 约占 DRAM bits 的 **51%**。这意味着 AI/服务器需求不仅吸收高价值 HBM，也开始改变 conventional DRAM 的剩余供给结构。

### 2.4 Cloud CapEx：规模巨大，但口径必须分开

Microsoft、Amazon、Alphabet、Meta 的 CapEx 均处于历史高位，但不同公司的时间窗和会计科目并不一致。

2025 混年口径下，四家设备购置合计约 **$354B** 量级；2026 年 Microsoft、Alphabet、Meta 已给出更高的公开 CapEx 预期/指引，Amazon 的 TTM net PPE 也继续上升。

这些数字不能直接写成“AI hardware CapEx”，原因包括：

- Amazon 包含 fulfillment/network infrastructure；
- Meta 包含非 AI 基础设施；
- Alphabet 包含办公与其他技术设施；
- Microsoft 的财年和其他公司日历年并不完全一致。

正确的分析对象不是“把四家公司所有 CapEx 加起来”，而是观察：AI server、network、memory、data center、power 与自研 silicon 在各自投资结构中的占比是否持续上升。

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

单独替代其中一个层，并不等于替代整个系统。

例如，cloud custom silicon 可以减少 NVIDIA 在芯片、互联或软件层的利润捕获，但如果新系统仍需要先进节点、HBM、先进封装和大规模电力，它同时会增强上游稀缺资源竞争。这两种作用可以同时发生，并不矛盾。

### 3.2 增量资源比历史份额更重要

报告采用 **AHICR（Advanced HPC Incremental Capacity Capture Ratio）** 观察下一代先进 AI/HPC 增量资源的捕获程度。

历史客户收入占比只能说明过去的收入结构。真正影响下一代竞争的是：

- long-duration orders
- prepayment
- credit quality
- utilization
- roadmap certainty
- supplier diversification
- geopolitics

因此，本报告不采用“TSMC 必然偏向某一家客户”这种单因素判断。更准确的机制是：当某买方在订单规模、预付款能力、信用、利用率和 roadmap certainty 上显著领先时，其对下一批增量产能的议价能力会上升；供应商同时仍有客户多元化和地缘风险管理的动机。

### 3.3 Non-AI Residual Capacity

AI 需求扩大之后，消费电子和传统服务器真正面对的不是“AI 把所有晶圆拿走”，而是 **Non-AI Residual Capacity（非 AI 剩余产能）** 的变化。

这种挤压具有选择性：

- Smartphone 仍然是 TSMC 第二大平台；
- PC 和 conventional server 仍然存在；
- Automotive 具有独立认证周期和节点结构；
- 但 HBM、RDIMM、advanced packaging、power management 等与 AI/服务器共用的资源，会优先受到高价值需求重排。

因此，“AI 挤压消费电子”应被理解为特定稀缺层上的 residual capacity 下降，而不是整个半导体行业停止服务非 AI 市场。

## 4. 中国供给栈：必须分层讨论

中国供给能力不能被压缩成“只能做手机”，也不能被写成“已经完成 frontier AI 全栈替代”。

更准确的分层是：

### 第一层：Smartphone / consumer computing

中国已经能够形成更完整的平行供给，包括部分逻辑、DRAM/NAND、终端设计、系统软件和整机生态。

### 第二层：PC / workstation / general computing

替代能力提高，但仍受 CPU/GPU 生态、先进节点、软件兼容和高性能存储等因素约束。

### 第三层：frontier AI system stack

要实现与当前最先进平台的等价替代，需要同时解决：

- advanced logic
- HBM-class memory
- advanced packaging
- high-speed interconnect
- compiler/runtime
- distributed training software
- large-scale system deployment

CXMT 招股材料没有披露 HBM 产品线，只能解释为“该文件未披露”，不能推导为“企业不存在任何 HBM R&D”。

因此，中国栈是否形成第二个全球级资源重力中心，是未来情景变量，而不是已经完成的事实。

## 5. 1999 Intel 为什么不是完全可比对象

Intel 1999 年：

- Revenue：**$29.389B**
- Gross margin：约 **59.7%**
- Operating income：**$9.767B**
- Net income：**$7.314B**

Intel 的优势集中在 CPU、x86 软件兼容和自有制造。

今天的 AI 平台优势更加分散，也更加系统化。要削弱一个领先 AI system stack，不只需要第二颗性能接近的芯片，还需要：

- 可迁移的软件栈；
- 可扩展的高速互联；
- 可获得的 HBM；
- 可获得的先进封装；
- 可部署的 rack/pod；
- 足够的数据中心与电力；
- 足够大的真实 workload。

这也是为什么“芯片份额下降”和“平台价值捕获下降”不能视为同一个事件。

## 6. 五类主要打断机制

当前主线并非不可逆。至少有五类变量能够改变稀缺层价值捕获：

1. **Cloud system-stack substitution**  
   Google、AWS、Microsoft、Meta 的系统栈在训练和推理中持续扩大替代范围。

2. **Buyer coordination**  
   大型买方通过联合标准、软件兼容和长期采购形成更强第二买盘。

3. **Power constraint**  
   已采购系统无法按时上电，导致 utilization、提货和下一轮订单下降。

4. **China parallel stack**  
   中国在 advanced logic、HBM、packaging、interconnect 与 software 上形成足够规模的平行系统。

5. **Regulatory structural remedy**  
   强制开放接口、限制 tying、供应约束或结构性分拆真正降低迁移成本。

这些变量都必须用公开可验证事件判断，而不是用情绪或单一新闻标题判断。

## 7. 当前基准情景

截至 2026 年 8 月，最符合当前事实的基准方向仍然是：

- AI system sales unit 继续向 rack/pod 上移；
- NVIDIA seller-side economics 仍然极强；
- advanced packaging 与 HBM 继续保持稀缺；
- cloud custom silicon 持续分流平台利润，但并未消除对先进上游资源的需求；
- power 开始成为与 packaging/HBM 并列的重要部署约束；
- 中国供给栈继续扩大，但 frontier AI 等价替代仍未完全闭环。

这对应正式情景矩阵中的 **S2 — Baseline Concentration**，而不是“永久垄断”。

如果 Cloud system-stack substitution、buyer coordination 或 China parallel stack 明显加速，系统可以向 **S1 — Competitive Expansion** 转移；如果先进资源进一步集中并伴随软件/互联锁定增强，则可能向 **S3 — Resource Hegemony** 转移；如果 utilization、token economics、CapEx 和后续供应承诺同时转弱，则进入 **S4 — Capital Hard Landing**。

## 8. 证伪条件

以下变化出现时，应主动下调“稀缺层价值捕获继续强化”的判断：

- NVIDIA supply commitments 连续下降或大规模取消；
- advanced packaging 不再被 TSMC 描述为 growth constraint；
- HBM/DRAM 供给重新显著宽松；
- cloud custom silicon 在 frontier training 中形成规模化迁移；
- CUDA/NVLink 等迁移成本被开放接口显著降低；
- 大规模 AI data center 出现持续低 utilization；
- power connection 成为公开披露的提货延期主因；
- 中国平行 AI system stack 在先进逻辑、HBM、packaging、interconnect 与 software 上形成可验证规模。

反过来，如果这些变量没有出现，而 seller cash flow、capacity commitments、HBM demand 与 advanced packaging tightness 继续同步增强，那么 S2 向 S3 偏移的概率会上升。

---

本卷只使用当前有效的证据体系。公司一手披露、机构研究、卖方估计与本报告压力测试分别按 A/B/C/D 等级处理，具体定义见 [《研究方法与证据分级》](研究方法与证据分级.md) 与 [《核心证据台账》](核心证据台账.md)。
