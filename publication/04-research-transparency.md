# 研究透明度、局限性与纠错机制

## 1. 研究定位

本报告作者署名为 **James（kamanager2012）**。

GitHub 仓库用于保存版本化研究文本、来源索引、证据台账与修订记录。仓库的可追踪性有助于读者核对研究变化，但**不等于外部同行评审、审计鉴证或机构评级**。

本报告的资料检索与修订截止日为 **2026-08-28**。

**日期解释：** **Evidence cutoff** 用于界定本版哪些外部事实与材料可以进入证据集合；**Edition revision date** 记录当前文本最后一次实质编辑日期。详细纠错过程保留在下方记录与 Git history 中；这些日期不代表外部审稿、审计或机构认证。

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

### 8A. Material revisions after the evidence cutoff

The evidence cutoff and the revision date are different controls.

After 2026-08-28, the report was edited only when one of the following conditions applied:

- a pre-cutoff fact, denominator, evidence identity, translation, or calculation required correction;
- a definition-level inconsistency affected scenario classification or falsification;
- bilingual analytical parity required repair;
- reader-facing structure required editorial reorganization without changing the evidence set.

These revisions did **not** authorize post-cutoff events to be backdated into the 2026-08-28 evidence snapshot.

Several material corrections made during 2026-08-29–31 remain analytically relevant and are therefore disclosed here in compressed form:

1. **End-system / residual-capacity framing was strengthened.** Consumer electronics, game consoles, industrial systems, and other non-AI end markets are analyzed through shared-resource exposure, Quantity Assurance, and Non-AI Residual Capacity rather than a blanket “AI displaces everything” claim.
2. **China's frontier assessment was separated into Production-Grade Parallel Stack and Autonomous Frontier Closure.** A system that can run production workloads is not automatically an autonomous multi-generation frontier stack.
3. **Capital-clearing decision logic was corrected.** Accounting impairment is a high-value confirmation / severity channel, not a mandatory gate. Direct falsification of a mechanism cannot be ignored merely because system-level cross-signal breadth has not yet accumulated.
4. **Developer-distribution risk was added as a conditional mechanism.** The 2026-08-27 Reuters report, citing The Information, concerning a reported NVIDIA / Hugging Face agreement remains C-grade transaction evidence and is not treated as a completed acquisition or realized software foreclosure.
5. **Strategy optionality language was corrected.** Chapter 31 no longer treats a continuously maintained executable second production path as universally optimal. The hard rule is to price executable optionality / resilience against carrying cost; maintaining a second production path remains conditional on continuity, bargaining, recovery and switching value exceeding that cost.
6. **English-first canonical workflow and translation parity were formalized.** English is the sole canonical analytical layer; Chinese is the professional translation of that text, not an independent analytical edition. Claims, section order, evidence grades, denominators, mechanisms, scenario identities, and falsification boundaries must remain equivalent.

The report therefore preserves a simple public rule:

> **Correct the research record when the evidence or definition is wrong; do not turn editorial history into a second research narrative.**

Detailed file-by-file chronology remains available through repository history and research-side validation materials rather than being repeated in the reader-facing report.

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
