# AI基础设施格局重塑：2026–2036结构性产业展望
### AI Infrastructure Reordering, 2026–2036: A Structural Industry Outlook

**AI 算力扩张如何重配半导体、存储、先进封装、电力、资本与终端产能**

一份研究 AI 基础设施、半导体、云系统、资本形成与产业战略的长期行业报告。

**Canonical research language：English。** 英文版是唯一 canonical analytical text；中文版是英文版的专业中文译本。中文可以调整句法并保留 HBM、CoWoS、CapEx、TCO、utilization、system stack 等标准行业术语，但不得独立新增、删除、重排或重定义论点、机制、分母、证据身份、情景状态、证伪边界与章节层级。任何实质性修订必须先在英文版完成，再翻译到中文版。


**Evidence cutoff：** 2026-08-28  
**Edition revision：** 2026-08-30  
本版研究判断只使用 cutoff 前可获得的证据。cutoff 后的本版编辑仅用于纠错、证据边界修复、双语一致性与论证结构调整；完整修订记录单独保留。

[网页版源码](docs/) · [开始阅读 32 章中文版](publication/README.md) · [执行摘要](publication/part-I-ch01-executive-summary.md) · [Master View](publication/part-IV-ch32-master-judgment.md) · [English](README.md)

---

## 报告研究什么

本报告不是在论证“只有 AI 重要”。手机、电脑、游戏主机、汽车、工业设备、机器人以及高可靠长生命周期电子仍然重要。核心问题是：**当 AI/HPC 以更高支付能力、更长锁量周期和更强资本形成能力改变部分共享或相邻上游的优先级时，非 AI 整机还能否按自己的 BOM、认证周期、产品寿命和价格约束，获得够用、够稳、付得起的资源。**

AI 产业竞争正在从“谁拥有更快的一颗 accelerator”上移到完整 **system stack**：

> **advanced logic + HBM + advanced packaging + interconnect + compiler/runtime + rack/data center + power + capital + workload**

本报告研究这一变化如何进一步影响：

- NVIDIA 与 hyperscaler custom systems 的竞争；
- TSMC、HBM 与 advanced packaging 的资源配置；
- AI 对 semiconductor capital formation 的影响；
- power / Time-to-Power 对 compute deployment 的约束；
- model company 从 cloud tenant 向 Anchor Compute Buyer 演化；
- smartphone、PC、game console、automotive、industrial 等传统终端的 residual capacity；
- 中国 frontier parallel stack、Production-Grade Gates 与 autonomous frontier closure；
- AI infrastructure CapEx、折旧、融资与资本清算；
- Agent-Native Software、Physical AI、劳动市场与人才体系；
- 2026–2036 的条件化产业情景。

这些主题并不是彼此独立的章节集合，而是同一条产业传导链上的不同环节：

> **物理供给 → System Stack 交付 → Compute 成本与可用性 → Workflow Economics → 企业采用与现金流 → 资本回收 → 劳动、人才与 Physical AI 的二阶重构**

这条传导链也是本报告判断未来十年的主轴：基础设施扩张只有最终转化为可验证、可收费、可持续的真实工作流产出，才会形成长期经济闭环。

---

## 2026 承重证据快照

这张表刻意保持窄口径：只列当前最承重的公开观察与本报告计算，同时把 denominator / evidence identity 写在同一行，避免数字离开边界后被过度解释。

| Signal | 2026 observation / calculation | Evidence identity | Boundary |
|---|---|---|---|
| TSMC demand mix | 2026 Q2 HPC 占 revenue **66%**；7 nm 及以下占 wafer revenue **77%** | first-party actual | revenue mix ≠ customer wafer allocation |
| HBM manufacturing intensity | Micron：same node / same bits 下 HBM3E 约需 DDR5 **3× wafer supply** | first-party physical trade ratio | 不是售价倍数；不是所有 HBM generation 的永久比例 |
| HBM allocation intensity | TrendForce 2026E：HBM wafer input **在前三大供应商中**约占 total DRAM wafer input 的 **22%**；HBM bit supply 约占 total DRAM bit supply 的 **9%** | B 级 institutional forecast | 两个 scope 不完全一致，不能把 22%/9% 正式相除；同口径 physical anchor 继续使用 Micron same-node / same-bits ≈3× |
| Aggregate DRAM balance | 2026 sufficiency ratio 约 **−1% 到 −2%** | B 级 institutional forecast | 是 aggregate DRAM，不是 HBM-specific |
| Forward supply commitments | NVIDIA manufacturing / supply / capacity commitments 从 2026-01-25 的 **US$95.2B** 增至 2026-07-26 的 **US$279B** | first-party filing | aggregate commitments；没有 supplier-level split |
| LPS / power coordination | PORTS-Pike 初始 **4.25 IT-GW design capacity**，计划自 2028 分阶段交付 | first-party project disclosure | design / secured capacity ≠ energized ≠ utilized load |
| Infrastructure finance | NVIDIA 与金融机构公布 **>US$500B** third-party-capital mobilization target | first-party target | target ≠ funded / committed / deployed capital |

完整 denominator audit 与计算见[第8章：Quantitative Framework](publication/part-I-ch08-quantitative-framework.md)。

---

## 核心判断

### 1. 竞争单位已经从 Chip 上移到 System Stack

NVIDIA 当前优势不能只用 GPU benchmark 或 market share 解释。

完整竞争已经覆盖 compute、memory、interconnect、software、rack architecture、data center 与 power。Google Ironwood、AWS Trainium3、Microsoft Maia、Meta MTIA 与 AMD Instinct/ROCm 也都在向更完整的 system stack 演化。

因此，长期竞争的关键不是：

> 谁拥有一颗更快的芯片

而是：

> **谁能够以更低迁移成本、更高利用率和更稳定供应，把完整 system 持续交付给真实 workload。**

### 2. AI 正在改变半导体“下一美元资本投向哪里”

TSMC 2026 Q2 的 HPC platform revenue 占比达到 **66%**，advanced technologies（7 nm 及以下）占 wafer revenue **77%**。这些是 revenue mix，不是 AI wafer share，但说明 HPC 已成为先进制造资本形成的重要边际驱动力之一。

本报告把这种结构称为 **Two-Speed Semiconductor Economy**：

> AI Infrastructure Economy 与 Traditional Device Economy 共享部分上游资源，却拥有不同的价格承受能力、订单期限与资本形成能力。

### 3. 总供给增长不等于传统行业获得更多供给

本报告使用 **Non-AI Residual Capacity**：

```text
NonAI_Residual
= Effective_Supply
- AI_Server_Absorption
- Other_Priority_Demand
```

因此，全球 wafer、DRAM 或 packaging capacity 可以增长，同时 smartphone、PC、automotive 等终端仍然面对更高价格、更低 allocation 或更慢规格升级。

### 4. HBM 的资源占用不能只看 Bit Share

Micron 一手披露，在 **same technology node / same number of bits** 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。

这是一项 wafer-supply trade ratio，不是售价倍数，也不是所有 HBM 世代永远固定的制造常数。

TrendForce 对 HBM + RDIMM 占 2026 DRAM bit supply 约 **51%** 的判断则属于 **2026E institutional forecast**，不能写成 full-year actual。

### 5. Advanced Packaging 与 Power 都已经成为独立约束

TSMC 已一手确认 advanced-packaging capacity tightness 会限制 customer growth。

同时，高密度 AI rack 让竞争继续上移到：

- powered land；
- grid interconnection；
- substation；
- cooling；
- firm power；
- permitting。

2026-08-17 的 PORTS-Pike 项目进一步显示，system platform 正开始直接协调 **land + power + shell（LPS）**：NVIDIA 披露通过 credit support 锁定初始 **4.25 IT-GW** 设计容量，OpenAI 为客户，项目计划从 2028 年开始分阶段上线。

这里必须严格区分：

> **secured / contracted capacity ≠ energized capacity ≠ utilized AI load**

### 6. 模型公司正在成为 Anchor Compute Buyer

OpenAI Stargate、Anthropic/AWS 等长期 compute commitments 表明，头部 model company 已经不只是租用现成 cloud capacity。

长期模型需求可以形成：

> **revenue visibility → financing certainty → earlier infrastructure buildout → earlier resource reservation**

但同一机制也会提高 customer concentration 与 duration mismatch risk。

### 7. 资本竞争正在从 Corporate CapEx 扩展到 Infrastructure Finance

NVIDIA 2026-08-10 宣布与 Apollo、BlackRock、Blackstone、Brookfield、Goldman Sachs、KKR 建立 AI compute infrastructure financing platforms，目标是**随时间动员超过 US$500B third-party capital**。

这是一项 mobilization target，不是已经 funded / committed / deployed 的资本。

它说明 compute 正被尝试组织成更接近长期 infrastructure asset 的融资对象。

### 8. 中国判断必须分成两级：Production-Grade Parallel Stack 与 Autonomous Frontier Closure

中国已经跨过“没有替代系统”的阶段，但 frontier 层必须区分“存在真实平行栈与部分 production deployment”和“七个 Production-Grade Gate 已经闭合”两个不同问题。按本报告现有公开证据，后者**尚不能确认**。

**Production-Grade Parallel Stack** 关注：

- accelerator / compute；
- HBM-class 或 equivalent memory subsystem；
- advanced packaging；
- high-speed interconnect；
- compiler/runtime；
- frontier / high-value production workload；
- system utilization、reliability 与 economics。

**Autonomous Frontier Closure** 则进一步关注：

- advanced manufacturing continuity；
- equipment / materials / software / service；
- cross-generation process upgrade；
- HBM / packaging / LPS / power / capital 的跨代持续性。

因此，存在进口依赖不等于“没有 production-grade parallel stack”；同样，系统已经能运行也不等于 autonomous frontier closure 已完成。

### 9. 当前最接近 S2 — Baseline Concentration

本报告不用一个 2036 单点预测描述未来，而采用四类条件状态：

- **S1 — Competitive Expansion**
- **S2 — Baseline Concentration**
- **S3 — Resource Hegemony**
- **S4 — Capital Hard Landing**

截至 2026 年 8 月，公开事实组合最接近 **S2**：

> 高增长、高集中与真实替代路径同时存在。

### 10. 基础设施最终必须由“可验证工作流产出”完成需求侧闭环

AI 基础设施的长期价值不能只由 GPU 出货、CapEx 或 token volume 证明。下面的 verified-workflow 标准是**长期经济判据，不是截至证据截止日已经完成经验校准的事实指标**。公开研究仍很少在同一 workflow denominator 下同时连接 AI cost、human time、verification、failure/retry、persistence 与 business value。Agent-Native Software、Physical AI 和企业自动化最终都要回到同一个经济问题：

> **单位可验证工作流结果需要多少 Compute、Energy、Human Review 与 Capital，产生的业务价值能否持续覆盖这些成本。**

因此，在该判据完成经验校准之前，单位 Compute 成本下降既不能被默认解释为基础设施总需求下降，也不能被默认解释为 Jevons 式总需求上升。若未来证据显示更低成本确实释放更多可验证工作流，总需求可以扩张；反过来，如果基础设施增长长期快于可验证业务产出与现金流，S4 — Capital Hard Landing 的风险才会系统性上升。

---

## 研究方法

全报告使用：

> **F → H → M → S → X**

- **F — Fact：** 已发生且可公开核验；
- **H — Hypothesis：** 明确的未来输入条件；
- **M — Mechanism：** 事实与假设之间的因果传导；
- **S — Scenario：** 条件组合形成的未来状态；
- **X — Falsification：** 足以迫使判断改变的反向信号。

证据同时分为：

- **A：** company / regulator / formal contract 等 first-party evidence；
- **B：** institutional / academic research；
- **C：** sell-side / supply-chain / media estimate；
- **D：** report-side calculation / sensitivity / scenario input。

基本原则：

> **已经发生的必须准确；未来可以大胆推演，但必须明示条件、分母、证据身份和证伪条件。**

---

## 阅读入口

### 整机 / 消费电子 / 游戏主机 / 汽车 / 工业读者

建议第一遍直接按：

**Ch01 → Ch03 → Ch21 → Ch20 §10 → Ch32**

这条路径先解释 residual capacity、quantity assurance、upgrade tax 与整机传导；NVIDIA、Hyperscaler、中国 parallel stack 与 S1–S4 可在第二遍作为机制背景阅读。

### 快速阅读

1. [第1章：执行摘要](publication/part-I-ch01-executive-summary.md)
2. [第32章：Master View](publication/part-IV-ch32-master-judgment.md)
3. [第30章：S1–S4 四类标准情景](publication/part-IV-ch30-scenarios.md)

### 完整报告

- [32章中文总目录](publication/README.md)
- [报告说明与证据边界](publication/00-front-matter.md)
- [表格目录](publication/02-list-of-tables.md)
- [缩写与核心术语表](publication/03-abbreviations-and-glossary.md)
- [研究透明度、局限性与纠错机制](publication/04-research-transparency.md)
- [竞争集、替代路径与反方证据矩阵](publication/05-competitive-evidence-matrix.md)

### 证据与方法

- [第27章：研究方法与证据架构](publication/part-IV-ch27-research-method.md)
- [核心证据台账](核心证据台账.md)
- [核心参考文献索引](核心参考文献索引.md)
- [核心概念与模型索引](核心概念与模型索引.md)
- [核心假设矩阵](核心假设矩阵.md)
- [正式报告架构与历史来源映射](出版结构.md)
- [四云 CapEx 口径核对](四云Capex口径核对.md)
- [外部研究对照索引](外部研究对照索引.md)

---

## 重要证据边界

本报告不做以下直接推导，除非存在足够公开证据：

- revenue share → wafer share；
- customer revenue → CoWoS allocation；
- HBM demand share → actual packaging allocation；
- contracted / secured MW → energized / utilized load；
- company-wide CapEx → AI hardware CapEx；
- model training compute → full R&D cost；
- occupational exposure → unemployment；
- conventional DRAM / NAND capability → HBM closure；
- production-grade substitution → autonomous frontier closure；
- foundry revenue share → frontier AI capability。

研究截止日后的新事实应视为新的研究输入，而不能倒写成 2026-08-28 前已经发生。

---

## 免责声明

本报告用于产业研究与信息交流，不构成：

- 投资建议；
- 证券研究评级；
- 法律意见；
- 审计意见；
- 任何交易建议或保证性预测。

未来判断会随技术、需求、资本、监管、地缘政治与供给变化而调整。

## 版权与引用

原创研究文本采用 **All Rights Reserved（保留全部权利）**。公开可阅读不代表授予一般复制、改编、再分发、商业利用、批量抓取或 AI 训练/数据集使用许可；具体权利保留与许可规则见 [LICENSE](LICENSE)。第三方材料仍受其各自权利人和许可条件约束。

引用信息见 [CITATION.cff](CITATION.cff)。

## 纠错与反方意见

欢迎提交：

- 事实或数字纠错；
- 更高等级来源；
- denominator / time-window 修正；
- mechanism challenge；
- counter-evidence；
- falsification signal。

[参与研究与纠错说明](CONTRIBUTING.md)
