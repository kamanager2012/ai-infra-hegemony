# 研究透明度、局限性与纠错机制

## 1. 研究定位

本报告作者署名为 **James（kamanager2012）**。

GitHub 仓库用于保存版本化研究文本、来源索引、证据台账与修订记录。仓库的可追踪性有助于读者核对研究变化，但**不等于外部同行评审、审计鉴证或机构评级**。

本报告的资料检索与修订截止日为 **2026-08-28**。

**日期解释：** evidence cutoff 与 text freeze 是研究快照的治理日期，用于界定“哪些事实可以进入这一版”以及“何时停止一般性修订”；两者之间的时间间隔**不代表本报告的研究持续时间、资料积累周期或审阅轮次**。

---

## 2. 外部评审边界

截至研究截止日，本报告不声称已经获得：

- 独立同行评审；
- 审计鉴证；
- 证券研究评级；
- 法律意见；
- 任何机构对全部结论的正式背书。

如果某一章节引用外部专家、公司、监管机构或研究机构，其引用只支持相应事实或观点，不代表该机构认可本报告的全部结论。

---

## 3. 证据选择原则

本报告的主要来源优先级为：

1. 法定申报、监管 / 政府文件、正式合同；
2. 公司官方 IR、product 与 technical materials；
3. 高质量机构研究与学术研究；
4. sell-side、supply-chain 与 media estimate；
5. 本报告自己的 calculation、sensitivity 与 scenario。

来源等级与命题身份分开处理。

例如：

- 公司 10-Q 中已经发生的财务数字可以进入 Fact；
- 公司 guidance 必须保留 forward-looking identity；
- 机构 forecast 必须保留机构名称与预测时间窗；
- report-side calculation 必须明确假设和分母；
- scenario 不能因为计算精确而升级成事实。

---

## 4. 公开资料的结构性局限

AI infrastructure 的很多关键变量并不公开，包括：

- customer-level wafer allocation；
- HBM customer mix；
- CoWoS actual allocation；
- process yield；
- private contract pricing；
- cluster utilization；
- workload-level profitability；
- future capacity reservation 的 supplier-level split。

因此，本报告坚持：

> **公开资料无法确认，不等于现实中不存在；但缺乏公开证据的内容也不能被写成已确认事实。**

公开资料还存在其他偏差：

- 公司更倾向披露能够解释战略和财务表现的信息；
- 不同国家和企业的披露深度不对称；
- institution / supply-chain research 可能包含未公开假设；
- 快速变化行业存在 publication-lag；
- 同一变量可能因 shipment、revenue、capacity、bits、wafers 等不同分母产生看似矛盾的数字。

---

## 5. 本报告明确不能从公开数据直接推出什么

除非存在足够直接的公开证据，本报告不做以下推导：

- revenue share → wafer share；
- platform revenue mix → customer allocation；
- HBM demand share → actual packaging allocation；
- contracted / secured MW → energized / utilized AI load；
- company-wide CapEx → AI-specific hardware CapEx；
- model-training compute → full corporate R&D cost；
- occupational exposure → unemployment rate；
- consumer DRAM / NAND capability → frontier HBM closure；
- foundry revenue share → frontier AI system capability。

这些边界是本报告因果推演的基础约束。

---

## 6. 反方证据与不确定性

研究结论只有在能够容纳反方证据时才有意义。

因此，每个强判断都应至少回答：

1. 当前证据支持什么；
2. 当前证据不能支持什么；
3. 哪些替代解释仍然成立；
4. 哪些未来事实会迫使判断下调或改写。

例如，“advanced packaging 是增长约束”必须能够在未来供应明显宽松、lead time 持续下降时被修改；“system-stack concentration 强”也必须能够在真实 production workload 大规模迁移到多套替代系统后被下调。

---

## 7. 纠错原则

如果发现高影响事实错误，应按以下逻辑修正：

1. 回到原始来源；
2. 判断错误来自 fact、denominator、time window、forecast/actual identity、translation 还是 calculation；
3. 修正受影响的事实表达；
4. 检查依赖该事实的机制、情景和结论是否需要同步调整；
5. 保留可追踪的历史修订记录。

不能用“长期逻辑仍然成立”回避已经被证据否定的事实。

---

## 8. 时间边界

本报告只把 **2026-08-28 及之前**能够获得并核验的资料纳入当前研究截面。

研究截止日之后出现的新事实，应视为新的研究输入。它们可能强化、削弱或推翻当前判断，但不应被倒写成截止日前已经存在的事实，也不会自动进入当前冻结的正式正文；只有在明确重新开启正文修订后，才可作为新的研究截面处理。

**冻结后纠错的 pre-cutoff source 规则：**如果某一来源或事实在 **2026-08-28 及之前已经公开可得**，但在 2026-08-29 的冻结纠错 / 补证过程中才被重新检索或核验，则可以用于修正或补强同一 2026-08-28 evidence snapshot，前提是：

- 不引入 2026-08-28 之后才发生的新事实；
- source publication / observation window 仍落在 cutoff 之内；
- evidence ledger 记录真实 access / correction date，不伪写成 2026-08-28；
- Git history 保留实际 post-freeze correction 记录；
- 不借“补证”名义重写未来情景或扩大结论强度。

因此，**evidence-event/source-availability cutoff** 与 **post-freeze verification date** 必须分开记录。

### 8A. 2026-08-29 material-correction pass

正式正文在 2026-08-29 曾被**明确重新开启一次**，用于修正已经识别出的重大实质性问题，而不是进行一般性扩写。修订范围包括：

- 整机 / 非 AI 下游读者入口与 residual-capacity 暴露；
- China frontier parallel stack 的 Production-Grade Gate 口径；
- verified-workflow 判据的“未完成经验校准”身份；
- S1–S4 的公开代理监测与 end-system dashboard；
- pre-cutoff source 的补证与证据边界。

该修订**没有新增第五情景、没有改变 S1–S4 定义、没有把 S2 升格成 S3，也没有把 2026-08-28 之后才发生的新事实倒写进当前 evidence snapshot**。

完成这次 material-correction pass 后，正文重新冻结。

### 8B. 2026-08-29 Developer Distribution material-event supplement

2026-08-29，正式正文又被**定向重新开启一次**，原因不是一般扩写，而是核对并纳入一个发生在既定 evidence cutoff 之内的重大事件：2026-08-27 Reuters 转述 The Information 报道的 NVIDIA / Hugging Face reported acquisition。

本次只修改与该事件直接相关的：

- Ch02 NVIDIA system-stack / platform-power 边界；
- Ch18 antitrust / vertical integration；
- competitive-evidence matrix；
- core evidence ledger / source index；
- Phase II Developer Distribution Chokepoint validation。

治理边界：

- 交易状态保持为 **reported transaction**，不写成 completed acquisition；
- 媒体交易报道保持 C-grade，Hugging Face 官方产品功能单独用 A-grade first-party docs 支撑；
- 不把 Hugging Face ownership 自动写成 open-model IP ownership；
- 不把 potential vertical foreclosure 自动写成 realized self-preferencing / software monopoly；
- 不改变 S1–S4 定义与当前 S2 baseline judgment。

完成上述定向补充后，正式正文再次冻结。

### 8C. 2026-08-30 清算与 optionality 定义级修正

2026-08-30，正式正文仅因 Phase II validation 发现的**定义级不一致**而再次定向开启。

第一，历史清算回放证明：Accounting 是高价值 confirmation / severity channel，但**不是 system clearing 的 mandatory gate**。financing-led 或 real-economy clearing 可以在 qualifying impairment / write-down 出现之前被确认，前提是 cross-signal confirmation 与 cross-actor / cross-layer causal breadth 已足够强。

**Mechanism-break override：** breadth 要求约束的是**系统级情景裁决**，不是给底层机制提供“必须等多信号才承认反例”的保护。如果一条高质量证据在同一 denominator、同一 time identity 下直接击穿某个机制的必要前提，该机制必须立即降级、重写或废弃，即使此时尚未形成 cross-signal breadth。breadth 决定是否改判整个 S1–S4 状态，但不能被用来忽略已经失效的前提。

第二，Decision Invariants 的 falsification pass 证明：长期维护一套 production-like second path **不是普适 Hard Invariant**。更耐久的原则是显式给 executable optionality 定价，只有 continuity / bargaining / recovery value 高于 carrying cost 时才维护第二路径。

本次修正仅涉及受影响的定义 / 策略口径：
- Ch01 — Executive Summary；
- Ch19 — CapEx Supercycle；
- Ch22 — Depreciation Wall；
- Ch24 — Capital Clearing；
- Ch29 — Monitoring Framework；
- Ch30 — S1–S4 Scenarios；
- Ch31 — Strategic Optionality；
- Ch32 — Master Judgment；
- 对应的 publication-status metadata。

本次修正**没有改变**：
- 2026-08-28 evidence cutoff；
- 当前 S2 baseline judgment；
- 四情景 taxonomy；
- 任何截止日前事实；
- S4 必须依赖广泛、持续、因果独立交叉确认的总体要求。

完成该定义级修正后，正式正文再次冻结。

### 8D. 2026-08-30 Ch32 双语 Master Judgment 一致性修正

随后进行的双语 parity audit 发现：中文版 Ch32 开头将最终总判压缩为**八点**，而英文版只有七点，原因是英文开头遗漏了“传统整机仍然重要，但从共享或相邻上游获得有效供给的确定性发生变化”这一核心判断。

因此只对英文 Ch32 做了双语实质一致性修复：补回缺失的第三点，并将后续编号恢复为八点。该修正属于 **translation / analytical-parity repair only**：
- 没有加入新证据；
- 没有修改中文版 source of truth 的任何判断；
- 2026-08-28 evidence cutoff 不变；
- 当前 S2 baseline judgment 与 S1–S4 taxonomy 不变。

完成该双语一致性修复后，正式正文再次冻结。

### 8E. 2026-08-30 English-first editorial restructuring pass

随后，正文因**语言与论证架构**被明确重新开启一次。该次修订的目的不是改变事实层，而是把正式研究生产顺序调整为：

> **Evidence → English canonical analytical text → technical review → Chinese professional parallel edition**

本次 editorial restructuring 的范围包括：

- 明确 English 为 canonical research language，中文为 professional parallel edition；
- 将 Ch01、Ch03、Ch17、Ch21、Ch32 的论证顺序改为 thesis / baseline / denominator / mechanism / boundary / falsification 优先；
- 将中文对应章节同步为专业平行版，而不是逐句机械翻译；
- 更新章节标题、目录、README、网站 chapter labels 与静态全文入口；
- 保留已经成立的事实、证据等级、分母、引用、S1–S4 taxonomy 与 current S2 baseline。

本次修订**没有**：
- 引入 2026-08-28 之后才发生的新事实；
- 提高任何 evidence grade；
- 改写任何已核定数值或分母；
- 把 S2 改成 S3；
- 为了英文表达而降低专业技术密度。

编辑原则被正式收敛为：

> **Simplify navigation, not analysis.**

完成该 English-first editorial restructuring 后，正式正文再次冻结。

---


## 9. 对外使用边界

本报告用于产业研究与信息交流，不构成：

- investment advice；
- securities rating；
- legal advice；
- audit opinion；
- guaranteed forecast。

读者应始终区分：

> **Fact / Company Guidance / Institutional Estimate / Report Calculation / Scenario**

本报告的目标不是消除不确定性，而是让不确定性的来源、证据强度和可能改变结论的条件保持清楚。
