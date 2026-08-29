# Contributing / 参与研究协作

This repository welcomes factual corrections, source upgrades, mechanism challenges, counter-evidence, falsification signals, and translation improvements. Unsupported estimates must not be rewritten as confirmed facts.

The Chinese 32-chapter formal report on `main` is the source of truth for facts, evidence grades, and analytical scope. The English edition should remain synchronized with the same research state.

## Start with these files

- [Research Method and Evidence Architecture](en/publication/part-IV-ch27-research-method.md)
- [Core Evidence Ledger](en/核心证据台账.en.md)
- [Core Source Index](en/核心参考文献索引.en.md)
- [Master Judgment](en/publication/part-IV-ch32-master-judgment.md)
- [Chinese source-of-truth landing page](README.zh-CN.md)

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

- write verified new facts back into the relevant chapter;
- correct dates, accounting definitions, units, denominators, or evidence grades;
- add conditions and falsification signals to strong conclusions;
- repair broken links, navigation, duplication, or translation;
- replace repeated cross-chapter numbers with a canonical source link;
- add better primary or institutional sources;
- keep English and Chinese research states synchronized.

## Pull requests that should not be submitted

- unsourced production, pricing, market-share, rack-count, or capacity figures;
- forecasts written as already-observed facts;
- institutional estimates rewritten as first-party disclosure;
- revenue share converted into wafer or packaging-volume share without evidence;
- contracted power capacity written as already energized load;
- different hyperscaler accounting categories added together as a single comparable “AI hardware CapEx” number;
- stress-test outputs presented as inevitable 2030/2036 outcomes;
- removal of counter-evidence or falsification conditions merely to strengthen the thesis.

## Evidence grades

- **A** — first-party company, regulatory, court, contract, or formal technical evidence;
- **B** — high-quality institutional research with transparent methodology;
- **C** — sell-side, single-source supply-chain reporting, or media relay;
- **D** — report hypotheses, models, calculations, and stress tests.

Cross-chapter reuse never upgrades an evidence grade automatically.

## Bilingual synchronization rule

When a factual or analytical change is accepted into the Chinese source-of-truth corpus, the corresponding English chapter or framework file should be updated in the same research cycle. Translation may improve prose, but it must not change evidence strength, numerical definitions, scenario logic, or the F→H→M→S→X structure.

---

# 中文说明

这是《AI基础设施霸权时代》的研究协作规范。欢迎提交事实纠错、来源补充、机制挑战、反方证据、证伪信号与翻译改进；不接受把缺乏来源支持的数字写成已确认事实。

中文 `main` 的 32 章正式报告是事实、证据等级与分析范围的 source of truth。英文版应与同一研究状态同步维护。

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

- 把已经核准的新事实写回对应章节；
- 修正时间、会计口径、单位、分母、来源等级；
- 给强结论补成立条件和证伪条件；
- 修复断链、目录、重复、翻译；
- 把跨章重复数字改成回链；
- 增加更高质量的一手或机构来源；
- 同步中英文研究状态。

## 不要提的 PR

- 没有来源的产量、价格、份额、柜数或产能；
- 把预测写成已经发生；
- 把机构预测升级成公司披露；
- 把收入份额换算成晶圆 / 封装片数份额；
- 把合同容量写成已经上电；
- 把四云不同会计科目直接加成统一“AI hardware CapEx”；
- 把压力测试数字包装成 2030 / 2036 必然结果；
- 为了“让观点更强”而删除反方或证伪条件。

## 证据等级

- **A**：一手公司 / 监管 / 法院 / 正式合同 / 正式技术报告；
- **B**：高质量机构研究、方法透明的行业跟踪；
- **C**：券商、单一供应链消息、媒体转述；
- **D**：本报告假设、模型、计算与压力测试。

跨章引用不得自动升级等级。

## 中英文同步规则

中文 source of truth 接受事实或分析更新后，对应英文章节或框架文件应在同一研究周期同步。英文可以优化表达，但不得改变证据强度、数字口径、情景逻辑或 F→H→M→S→X 结构。
