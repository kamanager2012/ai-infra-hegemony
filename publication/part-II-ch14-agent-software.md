# Part II · 第14章：Agent-Native Software 与 AI Software Unit Economics

## 1. Agent-Native Software 改写的是成本结构

传统 SaaS 的典型特征是 software replication cost 低、seat 增长不一定线性增加 variable compute。

Agent-native software 不同。一次任务可能触发 retrieval、reasoning、multiple model calls、tool invocation、browser/action execution、retry 与 human review。

于是软件成本单位从：

> **account / seat**

逐渐上移到：

> **workflow execution**

## 1A. 2026 Adoption Baseline：AI 已广泛进入企业，但 Agent Deployment 仍处早期

Stanford AI Index 2026 汇总的组织调查显示，**88%** 的受访组织报告已经使用 AI，**70%** 报告至少一个业务功能使用 Generative AI；但 AI agent 在几乎所有业务功能中的 deployment 仍处于**个位数比例**。[^3]

这组数据的意义不是给“Agent 经济”下一个固定渗透率结论，而是提供当前阶段定位：

> **AI adoption 已广泛发生，但从 assistant / feature use 走向可长期运行的 autonomous or semi-autonomous workflow，仍处于早期扩散阶段。**

因此，Agent-Native Software 的十年判断必须同时处理两件事：一方面，潜在 workflow volume 很大；另一方面，production reliability、review burden、integration 与 unit economics 尚未被大规模证明。

Anthropic 2026 Economic Index 也显示，其产品使用形态正在从短对话增加到更长时间运行的 agentic tasks，并观察到更高 Compute 消耗与更高估计工作价值之间存在相关性。[^4] 但该数据来自 Anthropic 自身产品使用样本，不能直接代表整个企业软件市场。

## 1B. AI Inheritance Effect：AI 继承的是几十年 Information Technology 的 Installed Base

工业企业从纯物理流程走向信息化，通常需要补齐 sensor、network、database、software、identity、process digitization 与人员流程。已经完成较高程度信息化的企业则不同：ERP、CRM、MES、CAD/PLM、database、cloud、API、digital document、source code、identity/access 与 workflow logs 已经构成可复用的数字底座。

本报告把这种**AI 可以在既有数字资产与工作流之上叠加 intelligence layer，而不必重新建设完整数字基础设施**的结构优势定义为 **AI Inheritance Effect**。

其需求传导可以写成：

> **Digital Installed Base → AI Overlay → Workflow Penetration → Automation Depth → Workload Volume → Infrastructure Demand**

它意味着 AI 基础设施的长期需求不只取决于单个模型是否继续放大，也取决于**有多少既有数字工作流开始调用 AI，以及每个 workflow 从 assistant feature 走向 semi-autonomous / autonomous execution 的深度**。

这一机制与 Algorithmic Efficiency 并不矛盾：

- 单次任务所需 compute / memory 可以持续下降；
- 但可经济使用 AI 的 workflow 数量可以扩大；
- 同一 workflow 的调用频率与 agent depth 也可以上升；
- 因此总 infrastructure demand 取决于 **unit resource intensity 的下降速度** 与 **workflow penetration / execution volume 的上升速度** 谁更快。

### 边界：Digital → AI 的摩擦显著降低，不等于“升级障碍为 0”

已有信息化基础可以降低边际部署摩擦，但 production-grade AI 仍可能受限于：

- data quality / access；
- legacy integration；
- identity / permission；
- security / privacy；
- compliance / responsibility；
- workflow redesign；
- reliability / observability；
- human review；
- unit economics。

而尚未数字化的 Physical AI / industrial process 仍需要 sensorization、control integration、qualification、safety 与现场改造。

因此，更稳健的判断是：

> **相对 Industrial → Digital，已经高度信息化的组织通常具有更低的 Digital → AI 边际改造成本；AI 的扩散可以继承 IT 时代的 installed base，但不能跳过生产级集成与责任约束。**

## 2. 不存在统一的“AI SaaS 毛利率终点”

不同 agent 产品的 variable cost 取决于 model choice、context length、cache、retrieval、tool/API、failure/retry、human review、pricing model 与 task depth。

因此，本报告不使用“传统 SaaS 85% → AI SaaS 55%”这类固定路径作为事实。

统一使用 **AI Software Unit Economics**。

## 3. 核心单位经济公式

生产级 workflow 可以近似写成：

> **Contribution Margin = Revenue / Productivity Value per workflow − Variable AI cost − Tools/APIs − Human review**

Variable AI cost 至少包括：

- inference；
- retrieval / storage；
- model routing；
- retry；
- observability；
- failure handling。

真正要优化的是 **cost per successfully completed workflow**，而不是单纯 cost per token。

## 4. Agent Depth 决定成本曲线

浅层 assistant 可能是 single prompt → single response。

深层 agent 更接近：plan → retrieve → reason → tool call → inspect → retry → finalize。

loop depth 增加时，compute、tool usage 和 failure surface 一起上升。因此 agent 产品必须同时优化：

- task success；
- loop length；
- model routing；
- caching；
- tool reliability；
- failure / retry rate。

## 5. Seat Pricing 为什么会受到挑战

如果产品主要提供 summary、autocomplete 或 shallow assistant，seat pricing 仍然可行。

如果一个 seat 可以运行 research、coding、support、sales、operations 等大量不同深度 workflow，compute variance 会显著扩大。

因此更常见的长期定价组合可能是 usage、credits、workflow、outcome 或 hybrid pricing。

这不是说 seat pricing 会消失，而是 agent depth 会让纯 seat 与真实 variable cost 的相关性下降。

## 6. Multi-model Routing 是新的基础软件能力

所有任务都调用最昂贵模型会直接破坏 unit economics。

更合理的 system design 是：

- cheap / local model：classification、extraction、high-volume routine work；
- medium model：routine reasoning；
- frontier model：复杂任务与高不确定决策；
- specialist/custom model：稳定专业 workload。

routing 本质上是在质量、latency、cost 和 failure probability 之间动态分配资源。

## 7. Open Source 会把利润从“模型能力”推向 Workflow / Distribution

open-source model 提高 model portability，压低 API premium，也增加 private deployment 与 buyer bargaining power。

因此，model capability 本身越来越难成为永久软件 margin。

更稳定的价值来源可能转向：

- proprietary workflow；
- domain data / context；
- distribution；
- integration；
- trust / compliance；
- measurable outcome。

## 8. Cloud System-Stack Competition 会向 Application 成本传导

软件公司通常不会直接购买 HBM、CoWoS 或 grid capacity，但 cloud price 最终包含 accelerator、memory、network、data center 与 power。

如果 hyperscaler custom stack 能降低真实 system TCO，长期可能通过 instance/API price 向 application layer 传导。

因此，Google Ironwood TPU、AWS Trainium3 等基础设施竞争不仅是芯片行业问题，也会影响 software contribution margin。[^1][^2]

## 8A. Workflow Elasticity：单位成本下降不等于总基础设施需求下降

Agent software 把模型调用转化成 workflow execution 后，总基础设施需求可以近似拆成：

```text
Total AI Infrastructure Demand
≈ Workflow Count
× Attempts per Workflow
× Resource Intensity per Attempt
```

因此，模型更便宜或 routing 更高效只会降低其中一部分。

如果更低价格带来：

- 更多用户；
- 更长 agent loop；
- 更多 tool calls；
- 更高 retry / exploration depth；
- 更多过去不经济的 workflow 被自动化；

那么总 compute / memory / network demand 仍然可能上升。

所以 software layer 对 infrastructure 的真正反馈变量不是“API 单价”，而是：

> **cost per verified workflow × demand elasticity**

这也是为什么 agent adoption 既可能压低 model-layer margin，又可能扩大 cloud / accelerator / memory 的总使用量。

## 9. Human Review 是经常被低估的变量成本

在 legal、finance、enterprise operations 等高风险 workflow 中，human review 可能长期存在。

如果 agent 生成速度提高 10×，但 review burden 不下降，企业只是把人工从 production 移到 verification。

真实 automation ROI 应计算：

> **Human time before − Human time after − new review / exception handling time**

而不是只统计 AI usage 或 generated tokens。

## 10. Agent-Native Software 的高质量利润来自哪里

长期更有机会形成高质量 economics 的产品通常具备：

- high workflow completion；
- low variable AI cost；
- low retry / review burden；
- strong proprietary context；
- distribution；
- measurable customer ROI；
- ability to route across models / providers。

这意味着 software competition 正从 feature competition 上移到 **workflow economics competition**。

## 11. 当前判断

AI 正在把一部分 software 从低边际成本复制品变成实时消耗 compute 的工作流系统。

这会压缩部分传统软件利润，但不会自动把整个软件行业变成低毛利。

真正的分水岭是：

> **谁能把模型调用转化成可重复、可验收、低失败率、可收费的业务结果，同时把 workflow demand growth 控制在可持续的 unit economics 内。**

## References

[^1]: Google Cloud, “Ironwood TPU,” https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/
[^2]: Amazon Web Services, “Amazon EC2 Trn3 UltraServers,” https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/
[^3]: Stanford HAI, “2026 AI Index Report — Economy,” organizational AI adoption, Generative AI use and early-stage agent deployment, https://hai.stanford.edu/ai-index/2026-ai-index-report/economy
[^4]: Anthropic, “Anthropic Economic Index report: Cadences,” 2026-06-26, long-running agentic tasks and the relationship between compute use and estimated artifact value; first-party product sample, https://www.anthropic.com/research/economic-index-june-2026-report

## 交叉引用

- [第10章：模型单位经济、算法效率与开源竞争](part-II-ch10-model-economics.md)
- [第12章：Hyperscaler System-Stack Competition](part-II-ch12-hyperscaler-system-stack.md)
- [第20章：Value Capture Map](part-III-ch20-value-capture-map.md)
- [第25章：AI 与劳动市场](part-III-ch25-labor-market.md)
