# Part II · 第18章：反垄断、产业政策与 AI 平台权力边界

## 1. System-stack power 给传统相关市场分析带来新难题

AI platform 的力量可能同时分布在 accelerator、interconnect、compiler/runtime、rack reference architecture、deployment software、cloud channel 与 adjacent model products。

于是可能出现：每个单独产品市场都存在竞争者，但多个关键接口由同一平台协调时，system-level switching cost 仍然很高。

因此，监管真正需要理解的是：

> **单一市场份额之外，跨层接口、bundling、migration cost 与 supply coordination 是否共同形成排他效果。**

## 2. Fine 与 Remedy 必须分开

罚款主要影响现金流；结构性或行为救济才可能改变竞争规则。

### Fine

罚款本身未必改变 CUDA migration cost、interconnect ecosystem、rack architecture、customer workflow 或 physical supply。

### Conduct / Structural Remedy

以下措施才可能直接改变 system economics：

- interface openness；
- interoperability requirements；
- tying / bundling restriction；
- non-discriminatory access / supply rules；
- acquisition restriction；
- structural separation。

因此，本报告不把“可能罚多少钱”当成平台权力的核心变量。

## 3. 10% Turnover Ceiling 不是未来罚款模型

EU Regulation (EC) No 1/2003 Article 23(2) 规定，相关罚款不得超过 undertaking 前一营业年度 total turnover 的 **10%**。[^1]

这是一条法定 ceiling，不是：

> **Potential fine = revenue × 10%**

违法是否成立、严重性、持续时间、相关销售、程序结果和 remedy 形式都会影响最终结果。

所以 10% 只能表示法律工具强度，不能进入本报告的公司盈利预测。

## 4. 程序状态必须逐层读取

欧盟 Article 102 公开程序本身已经给出清晰状态机：[^2]

1. complaint / ex officio investigation；
2. request for information；
3. formal investigation / market definition and dominance assessment；
4. Statement of Objections；
5. prohibition / commitment decision；
6. fine / remedy。

不同阶段的法律含义完全不同。RFI、market inquiry 或新闻报道不能直接写成“已经认定违法”。

## 5. 2026 年 Cloud Regulation 说明监管重点正在上移到 Interoperability

European Commission 2026 年仍在推进 DMA cloud-computing market investigation。2026-07-01，Commission 已实际举行 stakeholder roundtable，讨论三组主题：cloud interoperability / technical features、financial conditions，以及 contractual / commercial practices；调查 final report 最迟计划在 **May 2027** 发布。[^3][^4]

这说明监管关注点已经不只是传统价格，也包括跨服务技术互操作、合同与 switching conditions。

这与 AI system-stack competition 高度相关：如果客户无法低成本迁移 workload，接口和合同本身可能成为竞争变量。

## 6. Antitrust 与 Sovereign / Industrial Policy 不是同一个目标函数

竞争政策关注 market access、tying、exclusion、interoperability 与 customer choice；产业/国家安全政策则关注 domestic compute、semiconductor capacity、export control、data sovereignty 与 strategic autonomy。

同一政府完全可能同时：

- 补贴本土 advanced manufacturing；
- 推动 sovereign AI / cloud capacity；
- 限制敏感 accelerator 出口；
- 又要求本国市场中的平台提高 interoperability。

这些不是逻辑矛盾，而是不同政策目标并存。

## 7. Regulation 能改变四个系统变量

### 7.1 Interface Control

开放 compiler/runtime/network interfaces 可以降低 migration cost。

### 7.2 Bundling / Tying

限制 accelerator、network、software 的不当绑定，可以提高 multi-vendor system 的可执行性。

### 7.3 Access / Supply Rules

如果存在依法确认的 discriminatory access / allocation，non-discrimination remedy 可能改变 buyer bargaining structure。

### 7.4 Acquisition / Vertical Integration

merger control 可以阻止关键中间层进一步被纳入同一控制体系。

这些变量都会影响 system-stack moat。

## 8. Regulation 无法直接创造 Physical Capacity

监管可以降低 switching cost，但不能直接制造：

- HBM bits；
- advanced-packaging capacity；
- N2 wafers；
- grid / energized MW。

因此，即使 interface remedy 显著成功，physical scarcity 仍可能继续存在。

法律竞争与物理供给必须在不同模型中分析。

## 9. 对 China Parallel Stack 的影响也必须分层

美国或欧洲对某一 AI platform 的竞争政策，不会自动解决中国 frontier AI stack 的 advanced logic、HBM、packaging、interconnect 与 production software closure。

相反，中国本土 system capability 的提高也不自动改变欧美市场的 antitrust assessment。

两者可能互相影响 bargaining / strategic policy，但不能互相替代。

## 10. Regulation 如何改变 S1–S4

**Table 18.1 — 监管变量对 S1–S4 的作用路径**

| 情景 | 监管变量的作用 |
|---|---|
| S1 Competitive Expansion | interface openness、interoperability、tying limits 有效降低 switching cost |
| S2 Baseline Concentration | 调查与规则持续存在，但 system structure 基本保持 |
| S3 Resource Hegemony | remedy 不足以降低多层 switching / scarcity |
| S4 Capital Hard Landing | 通常由 utilization / capital clearing 主导，监管更多影响清算后的市场结构 |

**Source:** 本报告情景框架；EU competition / DMA procedure 作为监管机制背景。[^2][^3]  
**Note:** 表中为机制映射，不代表欧盟已对任何特定 AI platform 作出最终违法认定或 remedy。

所以监管不是固定“利空平台”的单向变量。它是否改变产业结构，取决于正式 remedy 是否真正触及迁移、bundling 与 access。

## 11. 当前判断

截至 2026 年 8 月，监管已成为 AI system-platform 的重要外部变量，但本报告不会把调查、market inquiry 或法定罚款 ceiling 写成已经发生的结构性改造。

真正需要持续更新的是：

- 是否进入正式 proceedings；
- 是否发出 Statement of Objections / equivalent formal complaint；
- 是否形成 binding conduct commitments；
- 是否出现 interoperability / tying / access remedy；
- 是否有最终 decision；
- remedy 是否真实降低 production migration cost。

只有这些正式事件，才足以改变 system-stack scenario weighting。

## References

[^1]: EUR-Lex, Regulation (EC) No 1/2003, Article 23(2), https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32003R0001
[^2]: European Commission, Article 102 investigation procedure, https://competition-policy.ec.europa.eu/antitrust-and-cartels/procedures/article-102-investigations_en
[^3]: European Commission / Digital Markets Act, cloud-computing market investigation and roundtable plan, final report due by May 2027, https://digital-markets-act.ec.europa.eu/roundtables-cloud-computing-services-2026-05-13_en
[^4]: European Commission / Digital Markets Act, stakeholder roundtable on cloud computing services, 2026-07-01, https://digital-markets-act.ec.europa.eu/commission-hosted-stakeholder-roundtable-cloud-computing-services-under-digital-markets-act-2026-07-01_en
