# 第二十七卷：Agent-native Software 与 AI 软件单位经济

## 1. AI 软件正在重写传统 SaaS 成本结构

传统 SaaS 的典型特点是：

- software replication cost 低；
- infrastructure cost 占收入比例较低；
- seat 增长通常不会线性增加 compute cost。

Agent-native software 不同。

一次用户操作可能触发：

- retrieval；
- reasoning；
- multiple model calls；
- tool invocation；
- browser/action execution；
- retry；
- human review。

因此，software cost 从“用户账户成本”转向“workflow execution cost”。

## 2. 不能用固定 85%→55% 代替真实分析

AI software gross margin 不存在统一行业终点。

不同产品取决于：

- model choice；
- token volume；
- cache；
- retrieval；
- tool/API；
- human review；
- pricing model；
- workload depth。

因此，本报告不采用固定“传统 SaaS 85% → AI SaaS 55%”作为事实。

统一使用 **AI Software Unit Economics**。

## 3. 核心单位经济公式

一个 AI workflow 的经济性可以写成：

[
Contribution Margin =
Revenue per workflow
-
Variable AI cost
-
Tool/API
-
Human review
]

其中 Variable AI cost 包括：

- inference；
- retrieval；
- storage；
- model routing；
- retry；
- observability。

真正需要优化的是：

> cost per successfully completed workflow

而不是单纯 cost per token。

## 4. Seat pricing 为什么可能失效

如果产品只是：

- summary；
- autocomplete；
- shallow assistant；

seat pricing 仍然有效。

如果产品替用户完成：

- research；
- coding；
- analysis；
- support；
- sales workflow；
- operations；

一次 seat 可能产生巨大 compute variance。

因此，agent-native software 更可能采用：

- usage；
- credits；
- workflow；
- outcome；
- hybrid pricing。

## 5. Agent 深度决定成本结构

浅层 assistant：

single prompt  
→ single response。

深层 agent：

plan  
→ retrieve  
→ reason  
→ tool call  
→ inspect  
→ retry  
→ finalize。

随着 loop depth 增加，推理与 tool cost 快速上升。

因此，agent 产品必须同时优化：

- task success；
- loop length；
- model routing；
- caching；
- failure rate。

## 6. Multi-model routing 成为新的软件基础能力

未来软件公司不应该把所有任务绑定到最昂贵模型。

更合理的架构是：

- cheap model：classification / extraction；
- medium model：routine reasoning；
- frontier model：complex task；
- local/custom model：high-volume stable task。

这种 routing 能直接改善 unit economics。

## 7. Cloud system-stack competition 会传导到软件成本

软件公司通常不会直接购买 HBM 或 CoWoS。

但 cloud price 最终包含：

- accelerator；
- memory；
- network；
- data center；
- power。

因此，cloud system-stack competition 如果降低 compute TCO，可能通过 instance/API price 传导到 application layer。

这也是 cloud custom silicon 对软件行业的重要意义。

## 8. Open-source model 的利润冲击

open-source model 会：

- 降低 model switching cost；
- 压低 API price；
- 增加 private deployment；
- 提高 buyer bargaining power。

因此，模型能力本身越来越难成为永久软件 margin。

更稳定的价值来源可能转向：

- workflow；
- proprietary data；
- distribution；
- integration；
- trust/compliance；
- outcome。

## 9. Human review 是最容易被忽略的成本

在高风险任务中：

- legal；
- healthcare；
- finance；
- enterprise operations；

human review 可能长期存在。

如果 agent 生成速度提高，但 review workload 没有下降，软件公司可能只是把人工从“生产”移到“审核”。

因此，真正的 automation ROI 必须包含：

[
Human time before
-
Human time after
]

而不是只统计 AI usage。

## 10. Agent-native Software 的长期赢家画像

长期具有高质量利润的软件公司更可能拥有：

- high workflow completion；
- low variable AI cost；
- strong proprietary context；
- low review burden；
- distribution；
- measurable customer ROI。

因此，未来软件竞争不再只是 feature competition，而是：

> **workflow economics competition**。

## 11. 当前判断

AI 正在把 software 从“低边际成本复制品”推向“实时消耗 compute 的工作流系统”。

这会压缩一部分传统软件利润，但不会自动让所有软件变成低毛利。

真正的分水岭是：

> 谁能把模型调用转化成可重复、可收费、低失败率的业务结果。
