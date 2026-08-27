# 第十八卷：研究方法与证据架构

## 1. 为什么需要统一方法

AI infrastructure 涉及财务、半导体、存储、封装、云、能源、监管和劳动市场。

这些领域的数字具有完全不同的来源与维度。

如果不建立统一证据架构，最容易出现以下错误：

- 公司披露与机构预测混写；
- revenue share 换算成 wafer share；
- contracted MW 写成 energized load；
- engineering estimate 写成 vendor disclosure；
- future scenario 写成 current fact；
- 同一二手数字在多卷重复后被误认为“多源验证”。

因此，本报告采用统一的：

**F → H → M → S → X**

结构。

## 2. F — Fact

Fact 是已经发生、可以回溯到明确来源的现实。

典型来源：

- 10-K / 20-F / annual report；
- official earnings materials；
- official product specification；
- regulatory document；
- court filing；
- formal contract；
- government document。

Fact 不等于“网上很多文章都这么写”。

## 3. H — Hypothesis

Hypothesis 是基于事实提出、但尚未被现实完全确认的判断。

例如：

> 高利润与长期订单会提高买方获取下一代 advanced capacity 的能力。

这不是财报事实，而是可以被数据验证或推翻的研究假设。

## 4. M — Mechanism

Mechanism 解释事实与未来状态之间的因果链。

例如：

高 system margin  
→ higher FCF  
→ larger prepayment  
→ stronger capacity reservation  
→ higher delivery certainty  
→ stronger customer retention。

机制必须明确中间变量，不能用“因为它强，所以会更强”代替因果解释。

## 5. S — Scenario

Scenario 是未来变量在特定组合下形成的产业状态。

本报告采用：

- S1 Competitive Expansion
- S2 Baseline Concentration
- S3 Resource Hegemony
- S4 Capital Hard Landing

Scenario 不是 prediction certainty。

它表达：

> 如果一组条件成立，产业更可能向哪种结构演化。

## 6. X — Falsification

任何重要判断都必须附带证伪条件。

例如：

如果 supply commitments 连续下降、packaging 不再 tight、cloud frontier training 大规模迁离，那么“稀缺层价值捕获继续强化”的判断必须下调。

没有 falsification condition 的宏大叙事，不进入本报告正式方法层。

## 7. A/B/C/D 证据等级

### A — First-party

包括：

- company filing；
- official product page；
- regulator/government；
- court document；
- formal contract。

例：

Micron FY24 Q3 prepared remarks 披露 HBM3E 约需要 DDR5 3× wafer supply。

### B — Institutional research

高质量机构研究：

- TrendForce；
- IEA；
- OECD；
- Stanford HAI；
- academic research；
- industry association。

例：

TrendForce 对 NVIDIA 占 CoWoS demand 超过 60% 的估计。

### C — Sell-side / supply-chain / media estimate

包括：

- investment bank；
- channel；
- supply-chain report；
- media estimate。

这类信息可以帮助理解方向，但不能冒充公司官方数据。

### D — Report model / stress test

由本报告自行计算：

- geometry；
- arithmetic；
- sensitivity；
- stress test；
- scenario assumption。

例：

5.39 CoWoS wafers/rack。

## 8. 维度一致性原则

全书禁止以下换算：

### Revenue share → wafer share

TSMC largest customer 19% revenue share 不能写成 19% wafer share。

### Contracted MW → utilized compute

1.92 GW PPA 不能写成 1.92 GW active AI load。

### Product spec × hypothetical quantity → shipment

13.4 TB/rack × 50,000 racks 只能是 scenario demand，不是实际 HBM shipment。

### Engineering geometry → fab yield

5.39 CoWoS wafers/rack 不是 TSMC yield。

### CapEx guidance → actual

guidance 必须与 actual 分开。

## 9. Negative evidence 的边界

“某文件没有披露”只证明：

> 在该文件范围内未披露。

它不能自动证明：

> 企业没有研发、没有产品、没有计划。

例如：

CXMT 招股文件没有披露 HBM product line。

正确写法是“该文件未披露 HBM 产品线”，不能扩大为“CXMT 没有任何 HBM R&D”。

## 10. Current fact 与 future scenario 分离

正式报告中的未来判断必须带条件。

不使用：

“某公司一定会垄断 N2。”

使用：

“如果长期订单、预付款、利用率和 roadmap certainty 持续领先，该买方获得更高比例新增 advanced capacity 的概率会上升。”

这种表达仍然可以大胆，但必须可证伪。

## 11. 核心模型的统一位置

报告的重要模型包括：

- AI Resource Gravity
- Scarce-layer Value Capture
- AHICR
- Non-AI Residual Capacity
- Cloud System-Stack Substitution
- Anchor Compute Buyer Effect
- Rolling Bottleneck Cascade
- AI Software Unit Economics
- Task-to-Job Translation Layer

这些模型均用于解释机制，不替代原始事实。

## 12. 发布标准

每一卷必须同时满足：

1. 当前事实有来源；
2. 机构数字标明机构属性；
3. 卖方估计不冒充一手披露；
4. 自算模型标明假设；
5. future claim 条件化；
6. 有 falsification condition；
7. technical unit 使用标准行业符号；
8. 正文不出现内部修订过程。

这套方法不是为了让报告“更保守”，而是为了让未来判断可以更大胆，同时仍然保持可验证性。
