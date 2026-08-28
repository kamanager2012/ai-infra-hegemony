# Part II · 第14章：Agent-native Software 与 AI Software Unit Economics

## 1. Agent-native Software 改写的是成本结构

传统 SaaS 的典型特征是 software replication cost 低、seat 增长不一定线性增加 variable compute。

Agent-native software 不同。一次任务可能触发 retrieval、reasoning、multiple model calls、tool invocation、browser/action execution、retry 与 human review。

于是软件成本单位从：

> **account / seat**

逐渐上移到：

> **workflow execution**

## 2. 不存在统一的“AI SaaS 毛利率终点”

不同 agent 产品的 variable cost 取决于 model choice、context length、cache、retrieval、tool/API、failure/retry、human review、pricing model 与 task depth。

因此，本书不使用“传统 SaaS 85% → AI SaaS 55%”这类固定路径作为事实。

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

因此，Google TPU、AWS Trainium 等基础设施竞争不仅是芯片行业问题，也会影响 software contribution margin。

## 9. Human Review 是经常被低估的变量成本

在 legal、finance、enterprise operations 等高风险 workflow 中，human review 可能长期存在。

如果 agent 生成速度提高 10×，但 review burden 不下降，企业只是把人工从 production 移到 verification。

真实 automation ROI 应计算：

> **Human time before − Human time after − new review / exception handling time**

而不是只统计 AI usage 或 generated tokens。

## 10. Agent-native Software 的高质量利润来自哪里

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

> **谁能把模型调用转化成可重复、可验收、低失败率、可收费的业务结果。**

## 关键证据导航

- [第10章：模型单位经济、算法效率与开源竞争](part-II-ch10-model-economics.md) — DeepSeek V2/V3、算法效率与 demand elasticity 的一手/技术来源。
- [第12章：Hyperscaler System-Stack Competition](part-II-ch12-hyperscaler-system-stack.md) — cloud custom silicon、system TCO 与 compute-cost transmission。
- [第20章：Value Capture Map](part-III-ch20-value-capture-map.md) — application-layer value capture、workflow monetization 与 infrastructure cost transmission。
- [第25章：AI 与劳动市场](part-III-ch25-labor-market.md) — human review / responsibility constraint 对真实 automation economics 的边界。
