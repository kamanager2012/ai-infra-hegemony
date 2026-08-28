# Part IV · 第27章：研究方法与证据架构

## 1. 为什么 AI Infrastructure 研究必须先统一证据语言

AI infrastructure 同时跨越财务、semiconductor、memory、advanced packaging、cloud、power、regulation 与 labor market。不同领域的数字具有不同物理单位、会计口径、时间窗口和证据强度。

如果没有统一规则，最常见的错误包括：

- company disclosure 与 institutional forecast 混写；
- revenue share 被换算成 wafer share；
- contracted MW 被写成 energized / utilized load；
- engineering estimate 被写成 vendor disclosure；
- guidance 被写成 actual；
- future scenario 被写成 current fact；
- 同一个二手数字在多个章节重复后，被误认为 multi-source confirmation。

因此，全书使用两套互补框架：

> **F → H → M → S → X**

以及：

> **A / B / C / D evidence grade**

前者负责判断身份，后者负责证据强度。

## 2. F — Fact

Fact 必须是已经发生、可以回溯到明确公开来源的现实。

优先来源包括：

- 10-K / 20-F / annual report；
- official earnings materials；
- official product specification；
- regulator / government document；
- court filing；
- formal contract / official project disclosure。

Fact 不等于“很多媒体都这么写”。多个媒体引用同一个来源，也不构成独立多源验证。

## 3. H — Hypothesis

Hypothesis 是由事实引出的未来输入条件，但尚未被现实完全确认。

例如：

> **如果一家 system platform 持续拥有更高现金流、长期订单、预付款能力和 roadmap certainty，它获取下一代 scarce capacity 的议价能力可能提高。**

这不是 company filing 中的事实，而是可以被未来 allocation、commitment 与 delivery data 检验的研究假设。

## 4. M — Mechanism

Mechanism 必须解释事实和未来状态之间的中间变量。

例如：

> high system margin → higher cash generation → larger forward commitments → stronger capacity reservation → higher delivery certainty → stronger customer retention

机制不能退化成“因为它强，所以会更强”。至少要说明：哪个变量变化、通过什么约束传导、什么证据可以证明链条断裂。

## 5. S — Scenario

Scenario 是多个 H / M 组合后的条件状态，而不是确定预测。

本书采用四类标准情景：

- **S1 — Competitive Expansion**；
- **S2 — Baseline Concentration**；
- **S3 — Resource Hegemony**；
- **S4 — Capital Hard Landing**。

情景的作用不是给世界分配固定概率，而是回答：

> **如果一组可观察条件同时成立，产业结构更接近哪一种状态？**

## 6. X — Falsification

任何强判断都必须附带反向信号。

例如，“scarce-layer value capture 继续强化”必须在以下变量持续逆转时下调：

- supply commitments 连续下降；
- advanced packaging 不再 tight；
- HBM / DRAM residual supply 显著宽松；
- cloud frontier workload 大规模迁离 dominant stack；
- migration cost 被 open interfaces 显著降低；
- utilization 与 forward commitments 同时转弱。

没有 falsification condition 的长期叙事，不进入本书正式判断。

## 7. A / B / C / D Evidence Grade

**Table 27.1 — 本报告证据等级体系**

| 等级 | 定义 | 典型来源 |
|---|---|---|
| A | First-party / formal evidence | company filing、official product page、regulator、government、court、formal contract |
| B | Institutional research | TrendForce、ILO、IMF、Stanford HAI、academic / industry research |
| C | Sell-side / supply-chain / media estimate | investment bank、channel、supply-chain source、media estimate |
| D | Report model / stress test | geometry、arithmetic、sensitivity、scenario assumption |

**Source:** 本报告研究方法。  
**Note:** evidence grade 衡量来源强度，不等同于结论重要性；D 级模型可用于情景和 sensitivity，但不能冒充已发生事实。

例子：

- Micron HBM3E same-node/same-bits ≈ 3× DDR5 wafer supply：**A**；[^1]
- TrendForce 对 NVIDIA 2025 CoWoS demand >60% 的估计：**B**；[^2]
- 卖方对某客户具体 CoWoS 月片数的估计：**C**；
- 72 ÷ 13.4 ≈ **5.37 CoWoS wafers/rack** 的报告侧 geometry：**D**。

证据等级不会因为同一数字被多个章节重复引用而自动上升。

## 8. Dimensional Consistency：量纲比故事更优先

全书禁止以下转换：

### Revenue share ≠ wafer share

TSMC customer revenue share 不能直接变成 N2、3 nm、HPC 或 CoWoS physical share。

### Contracted MW ≠ Energized MW ≠ Utilized AI Load

up-to-1.92-GW revised PPA 不能写成 1.92 GW active AI load。[^3]

### Product spec × hypothetical quantity ≠ shipment

13.4 TB HBM3E/rack × 50,000 hypothetical racks 只能得到 D-grade scenario demand，不是 actual HBM shipment。[^4]

### Engineering geometry ≠ fab yield

5.37 CoWoS wafers/rack 是 geometry stress test，不是 TSMC disclosed yield。

### Guidance / expectation ≠ actual

company guidance 必须保留 guidance 身份，不能与另一家 TTM actual 放在同一“已发生总额”里。

## 9. Negative Evidence 的边界

“某份文件没有披露”只证明该文件范围内没有披露。

例如 CXMT 注册稿未披露 HBM product line，只能写成：

> **该注册稿未披露 HBM 产品线。**

不能扩大成“企业没有任何 HBM R&D”。

Negative evidence 的作用是限制可确认事实，不是证明现实中绝对不存在某项活动。

## 10. Forecast / Guidance / Scenario 必须保留时间身份

机构预测必须保留：

- source identity；
- publication date；
- forecast window。

例如 TrendForce “HBM + RDIMM ≈ 51% of 2026 DRAM bit supply”必须写成 **2026E institutional forecast**，不能在跨章引用后变成 2026 actual。

同理，2030 / 2036 node price、monthly packaging capacity、GW campus 等 point estimates 只能在明确假设条件下使用。

## 11. 全书核心机制模型的位置

本书使用的主要模型包括：

- **AI Resource Gravity**；
- **Scarce-layer Value Capture**；
- **AHICR — Advanced/HPC Incremental Capacity Capture Ratio**；
- **Non-AI Residual Capacity**；
- **Cloud System-Stack Substitution**；
- **Anchor Compute Buyer Effect**；
- **Rolling Bottleneck Cascade**；
- **AI Software Unit Economics**；
- **Task-to-Job Translation Layer**。

这些模型用于组织因果关系，不替代原始事实。模型的正确性最终要由新的 F 与 X 检验。

## 12. 全书去重与交叉引用原则

正式报告必须避免同一事实和机制在不同章节被反复重写：

1. 一个高影响事实表只保留一个主要位置；
2. 一个机制只完整定义一次，后续章节通过交叉引用承接；
3. 后续章节只新增 evidence、boundary、counterargument 或 falsification；
4. 同一数字跨章使用时保持原始分母、时间窗和 evidence grade；
5. source 跟随事实，不能因章节重组而丢失；
6. 修订历史、编辑过程和版本施工信息不进入正式正文。

这样做的目的不是减少信息，而是让读者能够分清“第一次定义”“新增证据”和“跨章推论”。

## 13. 正式发布标准

每一章必须同时满足：

- fact 有 source；
- forecast / institutional number 保留身份；
- sell-side estimate 不冒充 first-party；
- D-grade model 明示假设；
- future claim 条件化；
- 有 falsification condition；
- technical unit 使用标准行业符号；
- accounting / physical unit 不混用；
- 正文不携带内部 revision metadata、过程性说明或自我辩护语气。

这套方法不是为了让结论更保守，而是让情景可以更大胆，同时仍然可审计、可证伪、可更新。

## References

[^1]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^2]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^3]: Talen Energy, 2026 Q2 Form 10-Q, revised AWS PPA up to 1,920 MW, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
[^4]: NVIDIA, “GB200 NVL72,” official product page, 13.4 TB HBM3E per rack, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
