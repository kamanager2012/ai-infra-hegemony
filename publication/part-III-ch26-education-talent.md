# Part III · 第26章：AI 时代教育与人才体系

## 1. 教育目标正在从“会用 AI”上移到“理解系统”

prompting、model calling 与基础 automation 很容易随工具进化而商品化。

更耐久的能力包括 model、data、compute、memory、software、network、power、economics 与 responsibility 的跨层理解。

这与产业竞争从 single chip 上移到 system stack 是同一变化。

## 2. AI Adoption 已经快于 Curriculum / Policy

Stanford HAI 2026 AI Index Education 章节给出几个清晰信号：[^1]

- **4 out of 5** U.S. high-school and college students use AI for schoolwork；[^1]
- 只有约一半 middle/high schools 有 AI policy；[^1]
- **just 6% of teachers say those policies are clear**；[^1]
- U.S. four-year university CS undergraduate enrollment 2024→2025 **下降 11%**；[^1]
- AI software-related master's graduates 2023→2024 **增长 17%**。[^1]

这些数据共同说明工具采用速度明显快于制度适配，但它们本身并不证明 AI 已经改善学习结果。

教育体系的核心问题已经从“学生有没有用 AI”转向：

> **如何验证学生是否理解模型边界、能够设计 workflow、验证结果，并对最终输出负责。**

## 3. 第一层：AI Literacy

所有专业都需要理解 model limitation、hallucination、source verification、privacy、data leakage、bias 与 responsible use。

它更接近新的基础数字素养，而不是 AI 专业学生的选修技能。

## 4. 第二层：AI Workflow Engineering

大量岗位不需要训练 foundation model，却需要：

- model selection；
- context / prompt design；
- retrieval；
- tool orchestration；
- evaluation；
- automation；
- human review。

这构成应用层 AI engineering。

## 5. 第三层：System Engineering

frontier AI 需要 accelerator、HBM、network、distributed computing、compiler/runtime、data center 与 power。

因此顶级 AI engineering 教育需要跨越：

> **computer science + computer architecture + systems/network + infrastructure economics**

纯模型课程无法覆盖真实产业约束。

## 6. Hardware 与 Software 不能继续完全分科

例如 inference optimization 可能同时涉及 quantization、kernel、HBM bandwidth、interconnect、batching 与 power。

所以未来 curriculum 更需要跨层实验、真实 performance/cost measurement 与 system debugging。

## 7. Multi-stack Capability 是战略技能

工程师不应只会一套 proprietary stack。

更有价值的是理解 CUDA、alternative accelerator stack、cloud custom silicon、open compiler/runtime 与 distributed frameworks，并能在多个 stack 之间迁移 workload。

教育目标不是“站队”，而是建立 portability。

## 8. Physical AI 需要新的跨学科组合

robotics / Physical AI 同时需要 control、mechanics、sensor、embedded compute、AI 与 safety。

如果 Physical AI 从 demo 扩大到 production deployment，对能够把 model capability 与 physical-world reliability、safety、manufacturing economics 连接起来的 system engineer 的需求会提高。

## 9. Power / Cooling / Operations 也属于 AI 人才体系

AI data-center buildout 让 electrical distribution、power engineering、liquid cooling、networking 与 operations 成为 AI infrastructure 的组成部分。

因此“AI 人才”不能只统计 ML engineer。

## 10. Entry-level Education 必须适应 Routine-task Automation

如果 drafting、routine coding、basic research 等入门任务被 agent 大量完成，学生需要更早接触 system debugging、verification、architecture、real-world project 与 responsibility。

否则学校会继续把大量训练时间投入最容易被自动化的 task。

## 11. Assessment 也必须改变

更合理的 project-based assessment 应要求学生同时解释：

- output correctness；
- source / evidence；
- system design；
- cost；
- reliability；
- power / resource use；
- safety / responsibility。

这比禁止 AI 工具更接近真实产业能力评价。

## 12. 当前判断

AI 教育的核心变化不是简单“新增一个 AI 专业”，而是产业能力结构正在改变教育的有效训练目标。

在模型调用越来越商品化的情况下，长期更有区分度的能力更可能来自：

- domain knowledge；
- workflow / system design；
- verification；
- performance / cost measurement；
- cross-stack portability；
- physical / regulatory constraints；
- responsibility。

因此：

> **AI literacy 是底层能力，workflow engineering 是应用层能力，system engineering 与 verification 则是把 AI 转化为现实生产力的关键能力。**

这与本报告的产业主线一致：竞争单位从单一模型或芯片上移到完整 system 后，人才评价也需要从“会使用工具”上移到“能设计、验证并对系统结果负责”。

## References

[^1]: Stanford Institute for Human-Centered Artificial Intelligence, “2026 AI Index Report — Education,” https://hai.stanford.edu/ai-index/2026-ai-index-report/education
