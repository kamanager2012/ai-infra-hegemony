# 研究透明度、局限性与纠错机制

## 1. 作者与研究载体

本报告作者署名为 **James (kamanager2012)**。GitHub 仓库既是版本化研究载体，也是证据追踪、纠错、双语同步和出版构建的工作记录。

本文件不把“仓库可追踪”解释成“已经过外部同行评审”。

## 2. 外部评审状态

截至 2026-08-28，仓库**不声称已经完成正式独立同行评审、审计鉴证或机构评级**。

如果未来获得外部专家、学术机构、行业机构或法律/财务专业人士的正式审阅，应在此处记录：

- reviewer / institution（如允许披露）；
- review scope；
- review date；
- 是否独立；
- 重大修改项；
- 尚未解决的异议。

没有记录的外部意见不能被写成“peer reviewed”。

## 3. Funding / Conflict of Interest

当前仓库**不作“无任何利益冲突”这一未经作者明确确认的声明**。

正式公开发布前，作者应补充一项明确声明，至少覆盖：

- 是否接受与 NVIDIA、TSMC、Samsung、SK hynix、Micron、AMD、Intel、Qualcomm、Apple、Google、Amazon、Microsoft、Meta、OpenAI、Anthropic，以及其他直接分析对象相关的资金、顾问费、商业合作或持仓影响；
- 是否存在会实质影响来源选择或结论表达的商业关系；
- 如无，明确写明“未发现需要披露的相关利益冲突”并由作者确认。

在该声明完成前，**Conflict-of-Interest Gate 保持 open**。

## 4. 证据选择原则与潜在偏差

本报告优先级为：

1. 法定申报、监管/政府文件、正式合同；
2. 公司官方 IR / product / technical materials；
3. 高质量机构研究；
4. sell-side / supply-chain / media estimate；
5. 报告自身 D 级模型。

这套顺序降低“二手报道反复引用后变成事实”的风险，但仍存在公开资料偏差：

- 公司更可能披露有利于投资者理解或战略叙事的资料；
- customer-level allocation、yield、contract pricing、utilization 等核心变量经常不公开；
- 中国与美国供应链的公开披露深度不对称；
- 机构研究模型可能包含未公开假设；
- 快速变化行业会产生明显的 publication-lag risk。

因此，“未公开披露”只支持“公开资料无法确认”，不自动证明“不存在”。

## 5. 研究局限

本报告不具备以下能力：

- 对未公开合同、内部采购、真实 customer allocation 进行审计；
- 从 revenue share 反推出 wafer / HBM / CoWoS physical share；
- 从 contracted MW 反推出 energized / utilized AI load；
- 证明未来 scenario 一定发生；
- 用公开材料精确计算所有公司的 AI-specific ROI；
- 把 40 卷、8 篇宏观专题和 32 章中的所有数字自动升级为已审计事实。

截至 2026-08-28，strict every-number **source-coverage** 已覆盖中英文 research layer **96/96 files / 1,052 unit-bearing numeric candidates / 0 unresolved**，Publication Layer **64/64 chapters / 529 candidates / 0 unresolved**。这证明数字主张已具备来源锚、明确的模型/情景身份或可解释的反例边界；它**不等于**逐句外部审计鉴证，也不替代低风险 claim 在最终 editorial proof 阶段对 source meaning、denominator 与 time window 的人工 semantic sign-off。机器可读 schema、candidate extractor 与 high-risk claim ledger 共同用于降低漏审风险。

## 6. 纠错原则

发现高影响事实错误时，处理顺序为：

1. 定位 claim 与原始来源；
2. 判断是 Fact 错误、denominator 错误、时间窗错误、forecast/actual 身份错误，还是翻译漂移；
3. 修正中文 canonical publication；
4. 同步英文 publication；
5. 回归核心证据台账、核心参考文献索引、模型索引与相关研究卷；
6. 在 Release Notes / Git history 保留可追踪变更；
7. 如错误影响 scenario weighting，明确说明哪些判断需要重新加权。

不能用“长期逻辑仍然成立”回避已被证据否定的事实。

## 7. 版本与截止日

当前正式研究检索/修订截止日统一为 **2026-08-28**。

发布后新增资料应进入下一版本，不应静默改写已经发布的历史版本。

## 8. 对外使用边界

本报告是行业研究，不构成：

- investment advice；
- securities rating；
- legal advice；
- audit opinion；
- guaranteed forecast。

读者应把 Fact、institutional estimate、report model 与 scenario 分开读取。