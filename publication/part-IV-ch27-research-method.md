# Part IV · 第27章：研究方法与证据架构

## 1. Research Quality 从 Claim Identity 与 Denominator Discipline 开始

AI infrastructure research 横跨 finance、semiconductor、memory、packaging、cloud、power、regulation 与 labor，而这些领域没有统一 denominator、clock 或 evidence standard。

方法上的第一步不是先组织 narrative，而是先保留 **claim identity、physical unit、time identity 与 evidence strength**。

如果没有统一规则，最常见的错误包括：

- company disclosure 与 institutional forecast 混写；
- revenue share 被换算成 wafer share；
- contracted MW 被写成 energized / utilized load；
- engineering estimate 被写成 vendor disclosure；
- guidance 被写成 actual；
- future scenario 被写成 current fact；
- 同一个二手数字在多个章节重复后，被误认为 multi-source confirmation。

分析由两套互补框架共同约束：

> **F → H → M → S → X**

以及：

> **A / B / C / D evidence grade**

前者负责判断“这是什么类型的命题”，后者负责判断“证据有多强”。

---

## 2. F — Fact：已经发生且可公开核验

Fact 必须满足两个条件：

1. 已经发生；
2. 可以回溯到明确公开来源。

优先来源包括：

- 10-K / 20-F / annual report；
- official earnings materials；
- official product specification；
- regulator / government document；
- court filing；
- formal contract / official project disclosure。

Fact 不等于“很多媒体都这么写”。

如果多个媒体引用同一原始来源，仍然只能算同一证据链。

---

## 3. H — Hypothesis：明确写出未来输入条件

Hypothesis 是由事实引出的未来输入条件，但尚未被现实确认。

例如：

> **如果一家 system platform 持续拥有更高现金流、长期订单、预付款能力和 roadmap certainty，其获取下一代 scarce capacity 的议价能力可能提高。**

这不是 company filing 中的事实。

它必须由未来的：

- allocation；
- commitment；
- delivery；
- utilization；

等数据继续验证。

---

## 4. M — Mechanism：必须解释中间传导，而不是重复结论

Mechanism 要回答：

> **为什么 A 会导致 B？**

例如：

> high system margin → higher cash generation → larger forward commitments → stronger capacity reservation → higher delivery certainty → stronger customer retention

一个合格机制至少要说明：

- 哪个变量变化；
- 通过什么约束传导；
- 哪个中间环节可能失效；
- 什么证据会证明链条断裂。

“因为它强，所以会更强”不构成机制。

---

## 5. S — Scenario：条件状态，不是单点预测

四类标准情景构成 scenario 分析：

- **S1 — Competitive Expansion**；
- **S2 — Baseline Concentration**；
- **S3 — Resource Hegemony**；
- **S4 — Capital Hard Landing**。

Scenario 的作用不是给未来分配一个固定概率，而是回答：

> **如果一组可观察条件同时成立，产业结构更接近哪一种状态？**

因此，2030 / 2036 的 point estimate 只有在明确条件下才有意义。

---

## 6. X — Falsification：任何强判断都必须允许被现实推翻

例如，“scarce-layer value capture 继续强化”必须在以下变量持续逆转时下调：

- supply commitments 连续下降；
- advanced packaging 不再 tight；
- HBM / DRAM residual supply 显著宽松；
- cloud frontier workload 大规模迁离 dominant stack；
- migration cost 被 open interfaces 显著降低；
- utilization 与 forward commitments 同时转弱。

没有 falsification condition 的长期叙事，不进入正式强结论层。

---

## 7. A / B / C / D Evidence Grade

**Table 27.1 — 本报告证据等级体系**

| 等级 | 定义 | 典型来源 |
|---|---|---|
| A | First-party / formal evidence | company filing、official product page、regulator、government、court、formal contract |
| B | Institutional research | TrendForce、ILO、IMF、Stanford HAI、academic / industry research |
| C | Sell-side / supply-chain / media estimate | investment bank、channel、supply-chain source、media estimate |
| D | Report model / stress test | arithmetic、sensitivity、scenario assumption |

**Source:** 本报告研究方法。  
**Note:** evidence grade 衡量来源强度，不等同于结论重要性。

例如：

- Micron HBM3E same-node / same-bits ≈ **3× DDR5 wafer supply**：A；[^1]
- TrendForce 对 NVIDIA 2025 CoWoS demand >60% 的估计：B；[^2]
- 卖方对某客户具体 CoWoS 月片数的估计：C；
- 本报告基于公开规格进行的假设敏感性计算：D。

D 级模型可以用于情景分析，但不能被写成已经发生的产业事实。

---

## 8. Dimensional Consistency：量纲一致性优先于叙事

### Revenue Share ≠ Wafer Share

TSMC customer revenue share 不能直接变成：

- N2 share；
- 3 nm share；
- HPC wafer share；
- CoWoS share。

### Demand Share ≠ Allocation Share

机构估计某客户需求占比，不等于供应商确认的实际 allocation。

### Contracted / Secured Capacity ≠ Energized Capacity ≠ Utilized AI Load

长期 PPA、secured LPS 或 future IT-GW design capacity 不能直接写成 active AI load。[^3]

同时必须区分：

- generation MW/GW；
- PPA capacity；
- IT-GW；
- energized facility load；
- utilized AI load。

### Product Spec ≠ Industry Shipment

13.4 TB HBM3E/rack 是 system specification。[^4]

如果没有真实 rack shipment，就不能进一步推出行业 actual HBM consumption。

### Guidance ≠ Actual

company guidance、expectation 与 TTM actual 必须保持各自身份。

### Physical Pool A ≠ Physical Pool B

front-end logic wafer、advanced-packaging capacity、HBM bits 与 energized MW 不能因为都服务同一个 AI system 就被放进同一分母。

### Production-Grade Parallel Stack ≠ Autonomous Frontier Closure

一套替代系统可以在真实 production workload 中形成可用闭环，同时仍依赖部分外部 equipment、materials、services 或 upstream manufacturing。

因此必须分别判断：

1. **production-grade substitution 是否成立**；
2. **关键外部供给受限后，系统是否仍能跨代扩张和迭代**。

前者不能因为存在进口依赖就被否定；后者也不能因为系统已经能运行就被提前宣布完成。

### Seller-Assisted Financing ≠ Independent End Demand

seller equity、credit enhancement、LPS support 或 compute-financing platform 可以加速真实基础设施形成，但也会改变 demand signal 的独立性。

因此融资质量分析必须区分：

- independently financed customer demand；
- long-duration Anchor Buyer commitments；
- third-party infrastructure capital；
- supplier equity / credit support。

---

## 9. Negative Evidence 也有 Boundary

“某份公开文件没有披露某项内容”只能证明：

> **在这份文件和当前公开材料范围内，没有足够证据确认该事项。**

例如，如果公开发行材料未确认可规模交付 HBM 产品线，合理结论是：

> **公开材料不足以确认已形成规模化 HBM supply。**

不能由此证明：

> 企业内部不存在任何 HBM R&D。

Negative evidence 的作用是限制事实层，不是证明现实中的绝对不存在。

---

## 10. Forecast / Guidance / Scenario 必须保留时间身份

机构预测必须保留：

- source identity；
- publication date；
- forecast window。

例如 TrendForce “HBM + RDIMM ≈ 51% of 2026 DRAM bit supply”必须保留为 **2026E institutional forecast**，不能在跨章引用后变成 2026 actual。

同样：

- company guidance 不能写成 actual；
- announced project capacity 不能写成 delivered capacity；
- secured capacity 不能写成 utilized capacity；
- 2030 / 2036 point estimates 必须保留 hypothesis / scenario 身份。

---

## 11. Concept Hierarchy：Load-Bearing Mechanism 与 Supporting Language

为避免把“命名数量”误当成“理论数量”，本报告把分析语言分成两层：**承重核心机制**与**辅助描述 / 测量语言**。

### Table 27.2 — 核心概念层级

| 层级 | 概念 | 在主链中的作用 |
|---|---|---|
| 承重核心 | **Non-AI Residual Capacity** | 解释优先分配后传统整机真正可获得的有效供给 |
| 承重核心 | **Layer-specific Incremental Scarce-Capacity Access** | 按 logic / HBM / packaging / networking / power 分层判断新增稀缺资源可得性 |
| 承重核心 | **Rolling Bottleneck Cascade** | 解释约束如何在不同物理层迁移、缓解或反转 |
| 承重核心 | **Cloud system-stack substitution + parallel-stack closure boundary** | 区分第二系统栈的真实替代能力，以及 production-grade substitution 与 autonomous frontier closure |
| 承重核心 | **Financing Reflexivity** | 判断订单、资本形成与 seller-assisted financing 之间的反馈和需求独立性 |
| 承重核心 | **AI inheritance** | 解释 IT installed base 如何扩张 AI workflow penetration 与长期需求池 |
| 辅助描述 / 测量 | resource reallocation pressure、scarce-layer value capture、two-speed semiconductor economics、anchor-buyer mechanism、AI Capacity Gap / Growth Gap、AI Software Unit Economics、Task-to-Job Translation | 用于描述方向、分层测量或延伸传导，不单独构成新的“总理论” |

**Source:** 本报告研究方法。  
**Note:** 辅助术语可以很重要，但其作用是提高因果表达和量纲清晰度；不能因为有独立名称，就被视为已经得到独立实证验证的理论。

这些概念只用于组织因果关系。

它们不能：

- 替代原始数据；
- 混合不同物理单位；
- 用模型名称掩盖证据缺失；
- 因为跨章重复出现而自动升级可信度。

---

## 12. Deduplication 与 Canonical-Home Rules

正式研究正文避免同一事实和机制在不同章节被反复重写。

规则是：

1. 一个高影响事实只在最相关章节完整展开；
2. 一个机制只完整定义一次；
3. 后续章节只增加新的 evidence、boundary、counterargument 或 falsification；
4. 同一数字跨章使用时保持原始分母、时间窗和 evidence grade；
5. source 跟随事实，不能因章节重组而丢失；
6. 修订历史与过程性编辑记录不进入研究正文。

这样读者才能区分：

> **第一次定义**

与

> **新增证据 / 新的产业推论**

而不是在不同章节反复看到同一段论证。

---

## 13. Research-Quality Standard

每一章至少应满足：

- fact 有 source；
- forecast / institutional number 保留身份；
- sell-side / supply-chain estimate 不冒充 first-party；
- D-grade calculation 明示假设；
- future claim 条件化；
- 强判断有 falsification condition；
- technical unit 使用标准行业符号；
- accounting / physical unit 不混用；
- 关键分母明确；
- 正文不携带 revision metadata、过程性编辑措辞或自我辩护语气；
- 章节围绕明确产业问题展开，而不是简单罗列数字；
- 结论能够回答“这对产业结构意味着什么”。

这套方法不是为了让结论更保守。

它的目标是：

> **允许未来推演足够大胆，同时保证事实层、量纲、证据身份和因果链始终可审计、可证伪、可更新。**

## References

[^1]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^2]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^3]: Talen Energy, 2026 Q2 Form 10-Q, revised AWS PPA up to 1,920 MW, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
[^4]: NVIDIA, “GB200 NVL72,” official product page, 13.4 TB HBM3E per rack, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
