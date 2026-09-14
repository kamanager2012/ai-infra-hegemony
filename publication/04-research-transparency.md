# 研究透明度、局限性与纠错机制

## 1. 研究定位

本报告作者署名为 **James（kamanager2012）**。

GitHub 仓库用于保存版本化研究文本、来源索引、证据台账与修订记录。仓库的可追踪性有助于读者核对研究变化，但**不等于外部同行评审、审计鉴证或机构评级**。

**Evidence cutoff：** 2026-08-28  
**Edition revision：** 2026-09-14

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
- contracted / secured capacity → energized / utilized AI load；
- IT-GW → generation GW；
- company-wide CapEx → AI-specific hardware CapEx；
- model-training compute → full corporate R&D cost；
- occupational exposure → unemployment rate；
- conventional DRAM / NAND capability → frontier HBM closure；
- production-grade substitution → autonomous frontier closure；
- foundry revenue share → frontier-AI system capability。

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

### 8A. 证据截止日之后的实质修订

Evidence cutoff 与 revision date 是两个独立控制项。

2026-08-28 之后，只有在以下情形之一成立时，才允许修改报告：

- cutoff 前的事实、分母、证据身份、翻译或计算需要纠正；
- definition-level inconsistency 影响 scenario classification 或 falsification；
- 双语分析 parity 需要修复；
- 在不改变 evidence set 的前提下，需要对面向读者的结构进行编辑性重组。

这些修订**不授权**把 cutoff 后才发生的事件倒写进 2026-08-28 evidence snapshot。

2026-08-29 至 2026-09-03 期间完成的若干实质纠错仍具有分析意义，因此在此压缩披露：

1. **强化 end-system / residual-capacity 框架。** Consumer electronics、game consoles、industrial systems 与其他 non-AI end markets 统一通过 shared-resource exposure、Quantity Assurance 与 Non-AI Residual Capacity 分析，而不是笼统表述为“AI 挤压一切”。
2. **将中国 frontier assessment 拆分为 Production-Grade Parallel Stack 与 Autonomous Frontier Closure。** 能够运行 production workload 的系统，不自动等于已经形成自主、可跨代延续的 frontier stack。
3. **纠正 capital-clearing decision logic。** Accounting impairment 属于高价值 confirmation / severity channel，而不是 S4 的强制 gate；即使 system-level cross-signal breadth 尚未积累，只要某一机制已被直接证伪，也不能忽略。
4. **将 developer-distribution risk 纳入条件性机制。** 2026-08-27 Reuters 援引 The Information 报道的 NVIDIA / Hugging Face 交易仍属于 C-grade transaction evidence，不得写成已完成收购，也不得写成已经实现 software foreclosure。
5. **纠正 strategy optionality 表述。** Chapter 31 不再把“持续维护一条可执行的第二生产路径”写成普遍最优策略。硬规则是把 executable optionality / resilience 的价值与 carrying cost 一并定价；只有 continuity、bargaining、recovery 与 switching value 高于该成本时，维护第二生产路径才成立。
6. **修复 downstream evidence boundaries。** Chapter 15 纳入 cutoff 前 BMW/Figure 02、Amazon DeepFleet 与 GXO/Digit 的 production evidence，同时继续保留 intervention、uptime、safety、TCO 与 broad fleet economics 的证据缺口；Chapter 25 改用 Stanford/ADP direct revision 区分 reduced hiring 与 separations，并保持 descriptive / non-causal identity；Chapter 26 纳入 cutoff 前 Khanmigo school-scale RCT 与 NUMI delayed-assessment RCT，同时继续保留 engagement、transfer、teacher workload、implementation cost 与 long-run system effects 的未决边界。
7. **正式固定 English-first canonical workflow 与 translation parity。** English 是唯一 canonical analytical layer；中文版只是该文本的专业翻译，不是独立分析版本。Claims、section order、evidence grades、denominators、mechanisms、scenario identities 与 falsification boundaries 必须保持等价。
8. **正式冻结在 2026-09-14 被明确重开一次，用于一处有界新增：S4 之下的需求侧反身性机制。** 第24章（§7B）、第29章（Dashboard I 需求腿）、第30章（S4 signals）与第32章（§10）现在说明 AI 驱动的劳动收入压缩如何通过消费与家庭信用传导到 enterprise monetization 与 capital clearing。该机制是本报告自有的条件化构造：不采用任何外部情景的数字、失业率、指数点位或带年份判断，不新增第五种情景，也不改变 evidence cutoff。外部校准参照记录在 External Research Comparison Index 中。

除第 8 项这一处重开外，此后至 **2026-09-14** 的许可修复仍限于上述四类情形，保留在 repository history 中，不在此重复；它们未改变 evidence set、S2 baseline 或 S1–S4 taxonomy。

对外规则因此很简单：

> **证据或定义错误时就纠正研究记录；不要把编辑历史变成第二套研究叙事。**

逐文件的详细修订历史保留在 repository history 与 research-side validation materials 中，不在面向读者的正式报告里重复展开。

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
