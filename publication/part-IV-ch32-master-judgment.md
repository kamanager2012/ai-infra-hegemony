# Part IV · 第32章：总判——AI 基础设施重构的产业终局与可证伪判断

## 1. 最终产业判断

截至 **2026 年 8 月 28 日**，本报告对未来十年 AI 产业结构的最终判断可以压缩为八点：

**第一，AI 基础设施的竞争单位已经从单颗芯片上移到完整 system stack。**  
GPU、ASIC 或单一 benchmark 已不足以解释产业权力。真正决定竞争力的是 advanced logic、HBM、advanced packaging、interconnect、compiler/runtime、rack/pod、data center、power 与真实 workload 能否形成高利用率、低迁移成本、可持续交付的完整闭环。

**第二，AI 正在改变全球半导体“下一美元资本投向哪里”。**  
高资本强度 AI/HPC 买方拥有更高的支付能力、更长的订单期限、更强的预付款与融资能力，因此正在提高自己对先进制程、HBM、先进封装、电力和数据中心增量资本形成的影响力。

**第三，传统整机没有失去重要性；改变的是它们按旧规则从共享或相邻上游获得有效供给的确定性。**  
smartphone、PC、汽车、工业设备、机器人以及高可靠长生命周期电子面对的不是同一种短缺，但都必须重新评估 residual capacity、quantity assurance、qualification rigidity 与 supplier product-mix。越接近 advanced logic / memory / selected packaging，传导越直接；越依赖 trusted / long-life / special-process supply，传导越需要通过供应连续性与 supplier economics 单独验证。

**第四，真正决定价值捕获的不是历史市场份额，而是对各关键稀缺层 incremental capacity 的持续可得性。**  
真正需要逐层观察 advanced logic、HBM、packaging、networking、LPS/power 的 quantity assurance、delivery timing 与 supply elasticity，而不是把它们压缩成一个综合“资源捕获率”。

**第五，Hyperscaler custom systems 与中国 parallel stack 正在增加替代路径，但并没有消除上游物理约束。**  
第二类 system stack 的成长可以削弱外部平台利润，却仍然会竞争 advanced logic、HBM、packaging 与 power。

**第六，AI 基础设施的主要风险已经从“有没有需求”转向“资本基数增长速度能否被真实 utilization、monetization 与独立融资能力覆盖”。**  
高 CapEx 本身既不是繁荣证明，也不是泡沫证明。Capital Hard Landing 需要 accounting、utilization/revenue、market clearing、forward commitments 与 demand-financing quality 多组信号广泛、持续并相互印证地恶化。

**第七，基础设施扩张只有转化为可验证、可收费、可重复的工作流产出，才完成需求侧闭环。**  
这是一项**长期经济判据，而不是截至 2026-08-28 已完成经验校准的事实指标**。公开研究仍难在同一 workflow denominator 下完整连接 Compute、Energy、Human Review、Failure/Retry、Capital 与持续业务价值。Agent-Native Software、Physical AI 与企业自动化最终都要回答这一问题；在该判据未完成校准前，单位 Compute 成本下降既不能被默认解释为总需求下降，也不能被默认解释为 Jevons 式总需求上升。

**第八，未来十年不是一个单点预测，而是 supply elasticity、system substitution、workload economics、capital discipline、power 与 frontier-system closure 共同决定的条件状态。**

因此，本报告的真正主题不是“谁会赢得 AI 芯片战争”，而是：

> **谁能够控制或稳定获得关键稀缺层，把它们组织成完整 system stack，并最终把这些资本密集型物理资源转化为可验证、可持续的经济产出。**

---

## 2. 产业权力已经从芯片性能迁移到 System Coordination

NVIDIA 当前最强的优势，不是“拥有所有物理资源”，而是能够把 GPU、CPU、HBM、NVLink、CUDA/runtime、rack-scale architecture、供应链与大规模 workload 组织成成熟的通用商业系统。

NVIDIA manufacturing, supply and capacity commitments 从 2026-01-25 的 **US$95.2B** 上升到 2026-07-26 的 **US$279B**。[^1] 这一数据说明前置供应承诺显著扩大，但公开文件没有披露 supplier-level split，因此不能把 US$279B 直接解释为 TSMC、CoWoS 或某一家 HBM vendor 的确定收入。

真正需要跟踪的不是历史 customer revenue share，而是：

> **Layer-specific Incremental Scarce-Capacity Access：一个平台在下一代 advanced logic、HBM、packaging、networking、LPS/power 等关键物理层中，能否持续获得足够、稳定、可交付的有效供给。**

在 severe shortage 中，价格也不是唯一清算机制。Long-term agreement、credit quality、prepayment、purchase scale 与 allocation fulfillment 都会影响 quantity assurance。

因此必须区分：

> **willingness-to-pay ≠ guaranteed quantity**

这也是为什么产业竞争最终会从“谁愿意出更高价格”升级为“谁能够获得稳定数量、稳定交付和系统级优先级”。

2026 年 8 月的最新变化进一步扩大了 system coordination 的边界。NVIDIA 一方面与六家大型长期资本提供方宣布建立 compute financing platforms，目标是随时间动员 **>US$500B third-party capital**；另一方面在 PORTS-Pike 项目中为 land、power 与 shell buildout 提供 credit support，初始部署设计支持 **4.25 IT-GW**，OpenAI 为客户。[^13][^14] 前者是 mobilization target、后者是 future design capacity，都不是已部署资本或已上电负载；但二者共同表明，领先 system platform 正开始把协调能力从芯片供应扩展到资本与物理基础设施。

---

## 3. AI 正在形成 Two-Speed Semiconductor Economy

截至 2026 年，最重要的结构变化之一，是先进制造和存储资本的边际需求正在更加依赖 AI/HPC。

TSMC 2026 Q2 的 platform revenue mix 中，HPC 占 **66%**、smartphone 占 **22%**；advanced technologies（7 nm 及以下）占 wafer revenue **77%**。TSMC 同期把 2026 年 capital budget 提高至 **US$60B–64B**，主要投向先进制程，并继续投入 advanced packaging、testing 等。[^6]

这些数据不能把 HPC 全部等同于 AI，也不能推出 Apple、Qualcomm 或其他具体客户被“挤掉”。它们支持的更窄结论是：

> **高增长 HPC/AI workload 正在显著影响先进制造增量资本形成。**

memory 侧也出现相同方向。Micron 一手披露，在 same node / same bits 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。[^2] TrendForce 预计 2026 年 HBM + RDIMM 合计约占 DRAM bit supply **51%**。[^3]

因此，本报告把这一结构称为 **Two-Speed Semiconductor Economy**：

> **AI Infrastructure Economy 与 Traditional Device Economy 共享部分上游资源，却具有不同的价格承受能力、订单期限、预付款能力、BOM 约束与资本形成能力。**

这不意味着消费电子消失，而意味着半导体产业的**边际需求决定权**正在更加集中于 hyperscaler、system-platform seller 与 Anchor Compute Buyer。

---

## 4. 物理约束不是一个瓶颈，而是一组会轮换的稀缺池

AI system delivery 同时依赖多个相互独立的物理层。

### HBM

HBM 的问题不是简单“市场份额上升”，而是制造资源强度上升。Micron 的约 **3× wafer-supply trade ratio** 说明，相同 bits 的 HBM3E 可能消耗远高于传统 DDR5 的 wafer input。[^2]

### Advanced Packaging

TSMC 已一手确认 advanced-packaging capacity tight，并在 2026 Q2 表示 packaging tightness 已限制客户增长。[^4]

因此，先进节点 wafer capacity 增加，不代表 AI system capacity 同比例增加。

### Power

约 **120 kW-class rack**、Crane 约 **835 MW** restart、Talen/AWS up to **1,920 MW** revised PPA 与 Kairos/Google 长期电源开发路径说明，power 已成为独立物理约束。[^5]

Contracted / Secured、Permitted、Construction / Transition、Energized、Utilized 必须严格区分；generation MW/GW、PPA capacity 与 IT-GW 也不能机械互换。

因此，一个 bottleneck 缓解后，另一个 bottleneck 可以上升。这就是本报告所称的 **Rolling Bottleneck Cascade**。

---

## 5. Non-AI Residual Capacity 是理解传统产业压力的核心变量

传统终端真正面对的不是“全球总供给”，而是优先需求吸收后剩余多少有效资源：

> **Non-AI Residual Capacity = Effective Supply − AI / Anchor Demand − Other Priority Demand**

这解释了为什么以下两件事可以同时发生：

- 全球 wafer、DRAM、packaging capacity 继续扩张；
- smartphone、PC、汽车或工业客户仍然承受更高价格、更低 allocation 或更慢规格升级。

因此，AI 对传统产业的影响不应写成“AI 全面占用芯片供给”，而应写成：

> **高价值需求改变 product mix、capital priority 与 quantity assurance，从而重新定义非 AI 市场可获得的有效残量。**

这个框架也意味着：低利润、低议价、短订单客户通常比拥有 LTA、规模采购与更强资产负债表的 anchor buyer 更容易承受冲击。

---

## 6. Cloud Custom Silicon：平台替代与资源竞争同时发生

Google Ironwood、AWS Trainium、Microsoft Maia 与 Meta MTIA 已证明，hyperscaler 的反击不是“自研一颗芯片”，而是形成第二类 system stack。[^7]

这一趋势会同时产生两个方向不同的结果：

1. **Platform-profit diversion**：部分 workload 不再支付完整外部平台 economics；
2. **Upstream resource competition**：custom systems 自身仍需要 advanced logic、HBM、packaging 与 power。

因此，custom silicon 的成功不等于上游资源竞争缓解。

真正决定长期格局的不是产品发布数量，而是：

- production workload share；
- migration cost；
- system utilization；
- external adoption；
- software portability；
- scale-up / scale-out efficiency；
- 供应链是否仍依赖同一批 scarce layers。

如果第二类 system stack 在真实生产负载中扩大，而软件迁移成本持续下降，S1 — Competitive Expansion 的权重会上升；反之，如果替代系统仍然高度受限于同一批稀缺资源与软件锁定，S2/S3 更可能强化。

---

## 7. Model Company 已经成为新的 Anchor Compute Buyer

OpenAI Stargate、Anthropic/AWS 等长期基础设施承诺说明，头部 model company 已经不只是 cloud tenant。[^8]

它们可以通过多年 compute commitments：

> **提高项目收入可见性 → 提升融资确定性 → 推动 cloud / data center / power / chip 提前建设 → 获得更稳定 capacity → 支撑更大 workload**

这形成 **Anchor Compute Buyer Effect**。

但同一机制也会放大资本周期风险。如果长期需求承诺改期、利用率不足或商业收入无法覆盖基础设施资本成本，原本支持建设的确定性就可能转化为 stranded-capacity 与 duration-mismatch risk。

因此，model-company long-duration commitment 已经成为与 hyperscaler CapEx、system-vendor supply commitments 同级的重要领先指标；其时间领先性仍需在更多完整周期中持续验证。

PORTS-Pike 又把这一机制推进一步：Anchor Buyer 不再只是“给云厂一个长期订单”，而可以通过 **长期客户需求 + platform credit support + infrastructure developer + long-duration lease** 共同提前形成 land、power 与 shell。[^14] 这提高了基础设施形成速度，也同时增加 customer concentration 与 duration risk。

---

## 8. 中国：真正的问题是 Frontier System Closure，而不是单一国产化率

中国供给能力不能用一个“国产化率”概括。

- consumer computing 与 smartphone supply chain：平行供给基础较强；
- DRAM / NAND：本土能力持续扩大；
- PC / workstation：替代能力增长，但 software compatibility 与专业 workload 仍重要；
- frontier AI：已经形成真实 accelerator/software parallel stack，但完整等价 system 仍需多个 critical layers 同时规模化。

CXMT 公开材料可以支持 DDR/LPDDR 与 DRAM 市场份额判断，但不能自动推导 HBM-class frontier closure。Counterpoint 对 YMTC 的 shipment share 与 revenue share 也必须保持分母区分。[^9][^10][^11]

foundry revenue share 同样不能等同于 frontier-AI capability。TrendForce 2026 Q1 的 SMIC **5.1%** 是 foundry revenue share，而不是先进 AI system closure 指标。[^12]

因此，本报告对中国采用两级判断：

> **Frontier Parallel Stack（未完全闭合）：**中国已经跨过“没有替代系统”的阶段，部分层已进入真实 production deployment；但按第17章七个 Production-Grade Gate，公开证据尚不足以确认完整 production-grade frontier parallel stack 已闭合。  
> **Autonomous Frontier Closure：**公开证据更不足以证明 advanced manufacturing、HBM-class memory、advanced packaging、interconnect、compiler/runtime、equipment/material continuity 与跨代 infrastructure scaling 已全部形成自主、可持续闭环。

未来真正需要跟踪的不是某一颗国产 GPU 的单点性能，而是 production workload 能否持续扩大，以及在关键外部供给受限时，整个 stack 能否跨代维持 performance、supply、power 与 economics。

---

## 9. 资本周期：真正的分水岭是 Utilization，而不是 CapEx 绝对规模

Cloud CapEx、system-vendor revenue、foundry revenue、memory revenue 与 power investment 不能直接相加成“全球 AI 总投入”，因为同一美元会在产业链不同账本重复出现。

AI infrastructure 的资本风险来自不同久期资产之间的错配：

- accelerator / server：技术折旧快；
- network / cooling：中周期；
- data-center shell：长周期；
- grid / substation / generation：更长周期；
- future workload revenue：不确定。

因此，判断资本泡沫必须同时观察五类信号：

- **Accounting**：impairment、write-down、accelerated depreciation；
- **Utilization / Revenue**：deployed compute utilization、AI revenue、verified workflow output；
- **Market Clearing**：lease rate、used-system price、delivery lead time、inventory；
- **Forward Commitment**：CapEx guidance、supply commitments、compute contracts、power contracts；
- **Demand Quality / Financing**：customer cash generation、third-party capital、supplier equity / credit enhancement 与 refinancing dependency。

截至 2026 年 8 月，公开事实更符合：

> **高强度资本扩张仍在继续，但 ROI 门槛和 monetization 压力正在上升。**

这与“全行业 Capital Hard Landing 已经发生”不是同一个判断。

---

## 10. 从基础设施到产业生产率：需求侧闭环决定十年周期能走多远

如果只观察 GPU、HBM、CapEx 或数据中心容量，本报告仍然是不完整的。基础设施只是供给侧；十年产业周期能否成立，最终取决于这些物理资产能否穿过软件、企业流程与实体世界，转化为可验证的经济产出。

### Agent-Native Software：单位经济从“席位”上移到“工作流结果”

传统 SaaS 更接近按 account / seat 扩张，而 Agent-Native Software 会持续消耗 inference、retrieval、tool/API、retry、observability 与 human review。

因此，软件层真正应比较的不是单纯 token price，而是：

> **cost per verified workflow outcome**

模型更便宜、routing 更高效，可以降低单次资源消耗；但如果同时释放更多用户、更多 agent loop、更多工具调用和更多此前不经济的自动化工作流，总 Compute 需求仍可能扩大。

这意味着软件层既是基础设施成本的承接者，也是未来基础设施需求弹性的来源。

### Physical AI：从“能演示”到“能回收资本”

机器人与 Physical AI 的竞争同样不是单一模型能力，而是 perception、control、actuation、battery、sensor、manufacturing、field reliability 与 cloud/edge system 的共同闭合。

真正的商业临界点不是“机器人能否完成一次任务”，而是：

> **Useful Tasks × Uptime × Deployment Scale 是否足以覆盖 Energy、Maintenance、Human Supervision、Depreciation 与 Financing。**

因此，Physical AI 可能成为新的 Compute、Memory、Storage 与 Cloud Workload 需求池，但只有规模化 utilization 与资本回收能够证明其产业价值。

### 劳动市场：Task → Workflow → Job，而不是 Exposure → Unemployment

AI 对劳动的传导必须至少经过：

> **Model Capability → Task Suitability → Workflow Redesign → Adoption Economics / Responsibility → Job Composition → Employment / Wage Outcome**

所以 occupational exposure 不能直接换算成岗位消失。更值得长期观察的是 junior/senior 结构、human-review ratio、output per employee、exception rate 与组织层级变化。

### 人才体系：从“会调用模型”转向“能设计并验证系统”

当基础模型调用逐渐商品化，更耐久的能力将向 workflow engineering、system engineering、cross-stack portability、verification、performance/cost measurement 与责任边界迁移。

因此，未来十年的人才分化不会只发生在“会不会 AI”，而会发生在：

> **能否把 AI 组织成可靠、可迁移、可度量、可承担责任的生产系统。**

把四条链合在一起，本报告的需求侧闭环可以写成：

> **Physical Infrastructure → System Delivery → Workflow Economics → Verified Output → Adoption / Cash Flow → Utilization → Capital Reinvestment**

如果前半段扩张长期快于后半段，S4 风险上升；如果可验证工作流产出、利用率和现金流持续拉动新增需求，即使单位 Compute 成本持续下降，S2/S3 型资本扩张仍可能延续。

---

## 11. “算力成为认知生产资料”必须用经济结果验证

本报告使用“生产资料化”描述一种可检验的经济变化，而不是技术神话。

判断标准不是模型“看起来多聪明”，而是：

> **AI system 能否在给定 compute、energy 与资本成本下，持续完成过去需要人工逐步完成、且可以验收的工作流。**

如果不能稳定完成并验收，compute 仍主要是辅助工具；如果能够大规模持续完成并创造可验证经济价值，compute、memory、packaging、power 与 software stack 才真正成为生产性基础设施。

因此，更有意义的指标是：

> **cost per verified workflow outcome + capital required to sustain it**

这也是为什么模型能力、基础设施投入、utilization 与业务收入必须放在同一个单位经济框架内分析。

---

## 12. 2026–2036：四类结构状态而不是一个预测数字

本报告使用四类并列情景：

### S1 — Competitive Expansion

供给弹性提高、custom systems 成熟、interoperability 改善，switching cost 下降，value capture 更分散。

### S2 — Baseline Concentration

少数 system platforms 与 scarce-layer suppliers 保持强经济性，同时替代路线继续扩大。**截至 2026 年 8 月，当前事实组合最接近这一状态。**

### S3 — Resource Hegemony

多个 scarce layers、quantity assurance 与 switching cost 同时强化，后来者必须复制更完整的 infrastructure stack。

### S4 — Capital Hard Landing

utilization、clearing price、CapEx / commitments、accounting losses 与 demand-financing quality 广泛恶化，资本进入清算。

这四个状态不是必然顺序，也不赋固定概率。

真正决定 2030/2036 产业结构的是：

- supply elasticity；
- HBM / packaging / power tightness；
- system substitution；
- software migration；
- Anchor Buyer demand；
- utilization / monetization；
- capital discipline；
- regulation；
- China frontier parallel stack / Production-Grade Gates / autonomous frontier closure；
- demand-financing quality / supplier-assisted financing。

---

## 13. 哪些事实会迫使本报告改判

以下信号具有高证伪价值：

- leading system-platform supply commitments 持续下降或大规模取消；
- advanced packaging 不再被主要供应商描述为 growth constraint；
- HBM / DRAM residual supply 显著宽松；
- cloud custom systems 在 frontier workload 上形成大规模、低迁移成本替代；
- open interfaces 明显降低 proprietary software / fabric switching cost；
- energized power 快速扩张，Time-to-Power 不再形成项目差异；
- Anchor Compute Buyer commitments 大规模改期或利用不足；
- hyperscaler AI monetization 长期无法覆盖新增资本基数；
- China frontier parallel stack 的多个 Production-Grade Gate 或 autonomous frontier closure 获得或失去规模化一手证据；
- supplier equity / credit support 持续上升，同时 independent customer financing 与 utilization 走弱；
- 正式监管 remedy 实质性改变 tying、interface 或市场进入条件。

如果这些事实与当前机制相反，本报告必须修改判断，而不能用“长期仍然成立”解释所有反例。

---

## 14. 研究语法：强判断必须能从 Fact 走到 Falsification

本报告所有强判断都必须经过五层：

- **F — Fact**：已经发生并可公开核验的事实；
- **H — Hypothesis**：未来输入条件或压力测试假设；
- **M — Mechanism**：事实与假设之间的因果传导；
- **S — Scenario**：多个条件组合形成的未来状态；
- **X — Falsification**：足以迫使原判断下调、重写或失效的反向信号。

这套结构的作用不是增加术语，而是防止：

- 机构 forecast 在多次引用后被写成 company fact；
- company guidance 被写成 actual；
- revenue share 被换算成 wafer share；
- contracted MW 被写成 energized MW；
- D 级 stress test 被包装成 2030/2036 必然结果。

未来判断可以大胆，但事实层必须保守。

---

## 15. 最终总判

AI 正在推动一轮比“GPU 景气周期”更深的产业重构。

它正在同时改变：

- 先进半导体增量资本的投向；
- memory 与 advanced packaging 的 product mix；
- system platform 的竞争边界；
- hyperscaler 与 model company 的产业角色；
- power 与 data-center infrastructure 的战略价值；
- traditional device markets 可获得的 residual capacity；
- Agent-Native Software 从 seat economics 向 verified-workflow economics 的迁移；
- Physical AI 从技术 demo 向 utilization、reliability 与 capital payback 的跨越；
- 劳动市场从 task automation 到 workflow redesign 的结构性重组；
- 人才体系从“会使用模型”向 workflow / system engineering 与 verification 的迁移；
- 中国 parallel stack 的战略目标；
- 全球资本市场对 AI workload monetization 的依赖程度。

因此，这一轮 AI 产业竞争最终不是一场单纯的芯片战争，而是一场：

> **System Stack + Scarce Capacity + Capital Formation + Workload Monetization 的复合竞争。**

当前最接近事实的状态仍然是 **S2 — Baseline Concentration**：领先平台和关键稀缺层保持强经济性，替代系统持续成长，但尚未形成足以消除 system-level concentration 与物理约束的全面替代。

未来如果供给弹性、system portability 与 multi-sourcing 显著改善，产业会向 S1 移动；如果多个 scarce layers 与 switching cost 同时强化，则 S3 权重上升；如果 utilization、market clearing、forward commitments、accounting 与 demand-financing quality 广泛、持续地共同恶化，则 S4 才真正成立。

因此，这份报告最终不是在问“是不是只剩 AI 重要”。手机、电脑、汽车、工业设备、机器人以及航空航天、舰船、雷达等战略系统仍然重要。真正需要问的是：

> **这些仍然重要的整机，能不能按自己的 BOM、认证周期、产品寿命与成本约束，从已经被 AI/HPC 改写优先级的上游，持续拿到够用、够稳、付得起的资源。**

这里同样必须保持量纲纪律：smartphone / PC / 部分 edge/ADAS 可以与 AI 直接共享 advanced logic、memory 或 selected packaging；汽车、工控与产线更多承受相邻 product-mix 与 long-qualification pressure；航空、国防与航天电子的核心风险常是 trusted / long-life / low-volume / special-process supply 的经济性、设备与人才连续性，而不是“直接和 AI 服务器抢 HBM”。

这也是“AI Infrastructure Hegemony”真正需要警惕的产业含义：**不是其他整机失去重要性，而是“重要”本身不再保证上游优先级。**

> **预测可以错，证据边界不能乱；情景可以大胆，事实层必须保守。真正有价值的行业研究，不是一次猜中终局，而是知道哪些产业变量正在决定终局，以及什么事实出现时必须改变判断。**

## 交叉引用

- [核心证据台账](../核心证据台账.md)
- [核心参考文献索引](../核心参考文献索引.md)
- [第2章：NVIDIA System Stack](part-I-ch02-nvidia-system-stack.md)
- [第5章：HBM](part-I-ch05-hbm-memory.md)
- [第6章：Advanced Packaging](part-I-ch06-advanced-packaging.md)
- [第7章：Power](part-I-ch07-power-constraint.md)
- [第12章：Hyperscaler System Stack](part-II-ch12-hyperscaler-system-stack.md)
- [第14章：Agent-Native Software 与 AI Software Unit Economics](part-II-ch14-agent-software.md)
- [第15章：Physical AI 与机器人系统的真正瓶颈](part-II-ch15-physical-ai.md)
- [第17章：中国 Parallel Stack](part-II-ch17-china-parallel-stack.md)
- [第25章：AI 与劳动市场](part-III-ch25-labor-market.md)
- [第26章：AI 时代教育与人才体系](part-III-ch26-education-talent.md)
- [第20章：Value Capture Map](part-III-ch20-value-capture-map.md)
- [第24章：Capital Clearing](part-III-ch24-capital-clearing.md)
- [第31章：2036 终局与战略选择](part-IV-ch31-strategy-endgame.md)

## References

[^1]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^2]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^3]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^4]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging tightness limiting customer growth, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^5]: NVIDIA, DGX GB200 Hardware Guide, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html ; Constellation, Crane Clean Energy Center, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs ; Talen Energy, 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm ; Kairos Power / Google, https://www.kairospower.com/google
[^6]: TSMC, 2Q26 Quarterly Results and Earnings Conference, platform mix and capital budget, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^7]: Google Ironwood TPU, https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; AWS Trainium3 UltraServers, https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ ; Microsoft Maia 200, https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ ; Meta MTIA 300, https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
[^8]: OpenAI, Stargate infrastructure disclosures, https://openai.com/index/announcing-the-stargate-project/ ; Anthropic, AWS compute collaboration, https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
[^9]: CXMT prospectus / Omdia, 2025 Q2 DRAM revenue share 3.97%, https://static.sse.com.cn/stock/disclosure/announcement/c/202512/002170_20251230_B8QS.pdf
[^10]: Counterpoint Research, 2026 Q2, YMTC 14% NAND shipment share, https://counterpointresearch.com/en/insights/server-led-essds-hit-48-percent-of-nand-shipments
[^11]: Counterpoint Research, 2026 Q1, YMTC 13% NAND revenue share, https://counterpointresearch.com/en/insights/global-nand-memory-market-share
[^12]: TrendForce, 2026-06-12, 1Q26 foundry revenue shares, https://www.trendforce.com/presscenter/news/20260612-13095.html
[^13]: NVIDIA, 2026-08-10, AI compute infrastructure financing platforms and >US$500B third-party-capital mobilization target, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Partners-With-Apollo-BlackRock-Blackstone-Brookfield-Goldman-Sachs-and-KKR-to-Establish-AI-Compute-Infrastructure-Financing-Platforms-to-Mobilize-Over-500-Billion-of-Third-Party-Capital/default.aspx
[^14]: NVIDIA, 2026-08-17, PORTS-Pike / SB Energy / OpenAI, initial 4.25 IT-GW design capacity, credit support for land/power/shell, phased online plan beginning in 2028, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx
