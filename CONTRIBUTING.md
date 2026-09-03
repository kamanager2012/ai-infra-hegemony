# Contributing / 参与研究协作

This repository welcomes factual corrections, source repairs/upgrades, mechanism challenges, counter-evidence, falsification signals, and translation corrections that restore bilingual factual or analytical parity. Unsupported estimates must not be rewritten as confirmed facts.

The **English 32-chapter formal report on `main` is the sole canonical analytical text** for claims, mechanisms, denominators, evidence identities, scenario states, falsification boundaries, and section hierarchy. The Chinese edition is the professional Chinese translation and must remain synchronized to the same research state.

**Formal-text freeze:** the 32-chapter bilingual report was refrozen on **2026-08-30**, with evidence/retrieval cutoff **2026-08-28**. The current edition revision is **2026-08-31** because permitted post-freeze evidence-boundary and bilingual-parity repairs continued without changing the evidence set, the S2 baseline judgment, or the S1–S4 taxonomy. Post-freeze changes to the formal chapters are limited to factual corrections, source-link repairs, citation-scope/time-window/unit/denominator corrections, bilingual parity fixes, and material-error fixes. Style-only rewrites, chapter expansion, framework redesign, terminology renaming, and post-cutoff evidence additions do not belong in the frozen formal text unless the freeze is explicitly reopened.

## Start with these files

- [Research Method and Evidence Architecture](en/publication/part-IV-ch27-research-method.md)
- [Core Evidence Ledger](en/核心证据台账.en.md)
- [Core Source Index](en/核心参考文献索引.en.md)
- [Master Judgment](en/publication/part-IV-ch32-master-judgment.md)
- [Professional Chinese edition](README.zh-CN.md)

The report uses one common analytical chain:

**F — Fact → H — Hypothesis → M — Mechanism → S — Scenario → X — Falsification**

## Two useful issue types

### 1. Data / definition / source correction

Please include:
1. chapter and section;
2. current wording or number;
3. what you believe is wrong;
4. the primary or high-quality institutional source;
5. the corrected definition, denominator, period, or unit.

Preferred sources include statutory filings, company IR, official product pages, formal contracts, court or regulatory records, technical reports, and high-quality institutional research.

Institutional estimates must remain attributed to the institution and must not be upgraded into company disclosure.

### 2. Mechanism / scenario challenge

A useful challenge identifies where the causal chain breaks:
- which fact **F** is wrong or incomplete;
- which hypothesis **H** is unreasonable;
- which mechanism **M** fails;
- which scenario **S** does not follow;
- or which observable **X** would falsify the conclusion.

A strong counterargument looks like:

> If variable A changes, mechanism B no longer holds; scenario C should therefore be weakened.

## Pull requests that are useful

- correct or restore verified facts that belong within the fixed retrieval cutoff;
- correct dates, accounting definitions, units, denominators, or evidence grades;
- correct missing or misstated conditions/falsification signals when the omission materially changes the conclusion;
- repair broken links, navigation, duplication, or bilingual parity errors;
- replace repeated cross-chapter numbers with a canonical source link;
- add better primary or institutional sources;
- keep English and Chinese research states synchronized without style-only post-freeze rewrites.

## Pull requests that should not be submitted

- unsourced production, pricing, market-share, rack-count, or capacity figures;
- forecasts written as already-observed facts;
- institutional estimates rewritten as first-party disclosure;
- revenue share converted into wafer or packaging-volume share without evidence;
- contracted power capacity written as already energized load;
- different hyperscaler accounting categories added together as a single comparable “AI hardware CapEx” number;
- stress-test outputs presented as inevitable 2030/2036 outcomes;
- removal of counter-evidence or falsification conditions merely to strengthen the thesis;
- post-2026-08-28 evidence additions to the frozen formal chapters;
- style-only rewrites, chapter expansion, framework redesign, or terminology renaming without a material-error basis.

## Evidence grades

- **A** — first-party company, regulatory, court, contract, or formal technical evidence;
- **B** — high-quality institutional research with transparent methodology;
- **C** — sell-side, single-source supply-chain reporting, or media relay;
- **D** — report hypotheses, models, calculations, and stress tests.

Cross-chapter reuse never upgrades an evidence grade automatically.

## Bilingual synchronization rule

After the formal-text freeze, a permitted material correction or evidence repair is resolved in the **English canonical analytical text first**; the corresponding Chinese chapter or framework file should then be updated in the same research cycle. Bilingual synchronization should restore factual and analytical parity; it must not introduce style-only rewrites, post-cutoff evidence, changes in evidence strength, numerical definitions, scenario logic, or the F→H→M→S→X structure.

---

# 中文说明

这是《AI基础设施格局重塑》的研究协作规范。欢迎提交事实纠错、来源修复/升级、机制挑战、反方证据、证伪信号与双语实质一致性修复；不接受把缺乏来源支持的数字写成已确认事实。

**英文 `main` 的 32 章正式报告是唯一 canonical analytical text。** 中文版是专业中文译本，必须与英文版保持同一事实、证据等级、分母、机制、情景状态、证伪边界与章节层级。

**正式正文冻结：**32 章中英文正式报告于 **2026-08-30** 再次冻结，证据/检索截止日仍为 **2026-08-28**。当前 edition revision 为 **2026-08-31**，原因是冻结规则允许的 evidence-boundary 与双语实质一致性修复继续完成；这些修复没有改变 evidence set、当前 S2 baseline judgment 或 S1–S4 taxonomy。冻结后，正式章节仅接受事实纠错、来源失效修复、引用范围/时间窗/单位/分母纠错、双语实质一致性修复与重大错误修复。纯风格重写、章节扩张、框架改造、术语改名，以及截止日之后的新证据，不进入冻结后的正式正文，除非明确重新开启正文冻结状态。

## 先看这些文件

- [研究方法与证据架构](publication/part-IV-ch27-research-method.md)
- [核心证据台账](核心证据台账.md)
- [核心参考文献索引](核心参考文献索引.md)
- [最终总判](publication/part-IV-ch32-master-judgment.md)
- [完整中文入口](README.zh-CN.md)

全书统一使用：

**F 事实 → H 假设 → M 机制 → S 情景 → X 证伪**

## 两类 Issue

### 1. 数字 / 口径 / 来源纠错

请写清：
1. 哪一章、哪一节或哪一段；
2. 现在写的是什么；
3. 你认为哪里错；
4. 原始来源或高质量机构来源；
5. 正确口径、分母、期间或单位是什么。

优先来源包括 SEC / 年报 / 公司 IR、官方产品页、正式合同、法院 / 监管文件、技术报告，以及 OECD / IEA / ILO / Stanford / TrendForce 等高质量机构研究。

机构预测必须保留机构身份，不得升级成公司官方披露。

### 2. 机制 / 情景挑战

如果你认为结论方向不对，请指出：
- 哪个事实 **F** 不成立或不完整；
- 哪个假设 **H** 不合理；
- 哪条机制 **M** 断裂；
- 哪个情景 **S** 不是由前面推出来的；
- 或者给出会推翻结论的 **X** 证伪信号。

最有价值的反方不是“我不同意”，而是：

> 在变量 A 改变后，机制 B 不再成立，因此情景 C 应下调。

## 可以提的 PR

- 修正 **2026-08-28 截止日前** 已存在、但在正式章节中写错或遗漏的已核准事实；
- 修正时间、会计口径、单位、分母、来源等级或引用范围；
- 修正会实质改变结论的成立条件、反方证据或证伪条件；
- 修复失效来源，并在同一 claim identity 下替换为更稳定的一手或高质量机构来源；
- 修复断链、目录、重复与中英文实质不一致；
- 把跨章重复数字改成回链；
- 同步已接受的事实纠错与证据修复，但不进行冻结后的风格性重写。

## 不要提的 PR

- 没有来源的产量、价格、份额、柜数或产能；
- 把预测写成已经发生；
- 把机构预测升级成公司披露；
- 把收入份额换算成晶圆 / 封装片数份额；
- 把合同容量写成已经上电；
- 把四云不同会计科目直接加成统一“AI hardware CapEx”；
- 把压力测试数字包装成 2030 / 2036 必然结果；
- 为了“让观点更强”而删除反方或证伪条件；
- 把 **2026-08-28 之后** 的新事实或新证据加入冻结后的正式章节；
- 仅为了表达更漂亮而进行风格性重写、章节扩张、框架改造或术语改名。

## 证据等级

- **A**：一手公司 / 监管 / 法院 / 正式合同 / 正式技术报告；
- **B**：高质量机构研究、方法透明的行业跟踪；
- **C**：券商、单一供应链消息、媒体转述；
- **D**：本报告假设、模型、计算与压力测试。

跨章引用不得自动升级等级。

## 中英文同步规则

正式正文冻结后，符合冻结规则的重大纠错或证据修复必须先在**英文 canonical analytical text** 中裁定，再在同一研究周期同步对应中文章节或框架文件。双语同步的目标是恢复事实与分析实质一致性，不得借同步之名进行风格性重写、引入截止日后的新证据，或改变证据强度、数字口径、情景逻辑与 F→H→M→S→X 结构。
