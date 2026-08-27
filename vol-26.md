# 第二十六卷：模型公司、Anchor Compute Buyer 与基础设施共建

## 1. 模型公司正在从“算力租户”升级为长期基础设施买方

传统模型公司通常被视为 cloud customer。

到 2026 年，这个关系已经明显变化。

大型模型公司开始通过：

- multi-year compute commitments；
- dedicated data-center projects；
- long-duration chip procurement；
- power reservation；
- infrastructure co-investment

反向影响 cloud、chip 和 energy investment。

本报告将这种机制定义为 **Anchor Compute Buyer Effect**。

## 2. Anchor Buyer 为什么重要

当模型公司能够提供多年、超大规模需求时，基础设施供应商获得更高建设确定性。

机制可以写成：

long-duration model demand  
→ cloud/infrastructure provider 获得 revenue visibility  
→ 提前建设 data center / power  
→ 提前锁 chip / HBM / packaging  
→ model company 获得 priority capacity。

因此，模型公司不再只是接受 cloud price，而是开始塑造 cloud investment。

## 3. OpenAI Stargate

OpenAI Stargate 的公开目标是未来数年在美国建设大规模 AI infrastructure，目标规模最高达到 **$500B**。

OpenAI 2025 年进一步披露与 Oracle 等合作扩展数据中心，已形成 **>5 GW** under-development capacity 的公开方向。

这类项目的战略意义在于：

> 模型需求被直接转化为 land、power、chips 和 data-center construction。

但必须区分：

- announced investment；
- contracted capacity；
- construction；
- energized capacity；
- actual utilization。

“计划投资 $500B”不能写成“已经投入 $500B”。

## 4. Anthropic / AWS

Anthropic 与 AWS 已形成长期深度基础设施关系。

公开材料已经给出更明确的长期锚：

- Anthropic 对 AWS 的未来十年计算承诺超过 **$100B**；
- 可预留最高 **5 GW** 的 AWS compute capacity；
- 已大规模部署 Trainium；
- Anthropic 已公开使用超过 **1M Trainium2 chips**；
- 预计到 2026 年底形成接近 **1 GW** 的 Trainium2/3 capacity。

这说明：

> model company demand 可以成为 cloud custom silicon 的第一大锚定 workload。

因此，Anchor Buyer 不只是帮助基础设施扩张，也可以改变 accelerator competition。

## 5. 模型公司仍然不拥有全部 physical layer

Anchor Buyer 能影响：

- demand certainty；
- chip selection；
- rack deployment；
- cloud roadmap；
- power planning。

但模型公司通常仍不直接拥有：

- leading-edge foundry；
- HBM fab；
- advanced packaging fab；
- grid。

因此，Anchor Buyer 是**需求侧权力增强**，不是完整基础设施所有权。

## 6. 系统栈依赖仍然存在

模型公司选择 compute provider 时，真正选择的是一整套 system：

- accelerator；
- HBM；
- interconnect；
- compiler/runtime；
- scheduler；
- rack/pod；
- cloud operations。

因此，“换云”不只是换账单。

它可能意味着：

- model porting；
- kernel adaptation；
- performance tuning；
- distributed training changes；
- observability changes。

这构成 infrastructure switching cost。

## 7. Algorithmic efficiency 如何改变 Anchor Buyer 权力

如果模型架构显著降低单位 capability 的 compute demand：

- model company 可以减少长期 capacity commitment；
- buyer bargaining power 提高；
- infrastructure provider 面临更高 utilization risk。

如果更低成本带来更高 workload volume，则长期 commitment 仍可能扩大。

因此，Anchor Buyer Demand 是需求函数，不是固定增长曲线。

## 8. 模型公司与 cloud 的权力正在双向化

过去的结构：

model company  
→ rent cloud compute。

正在变成：

model company demand  
↔ cloud infrastructure buildout。

模型公司依赖 cloud 的物理资产，cloud 又依赖模型公司的长期 workload 填充新建 capacity。

这形成相互依赖。

## 9. Anchor Buyer 对产业链的传导

大型模型需求可以依次影响：

Model demand  
→ cloud CapEx  
→ accelerator orders  
→ HBM / packaging  
→ data-center power  
→ grid / generation。

因此，模型公司已经成为 AI infrastructure 资本形成的重要 upstream demand signal。

## 10. 风险

Anchor Buyer model 也会放大风险。

如果模型公司：

- revenue 不及预期；
- financing 收紧；
- architecture efficiency 显著提高；
- workload 转向其他 system；

长期 infrastructure commitment 可能成为 stranded-capacity risk。

因此，不能只看合同 nominal value，还必须看：

- take-or-pay；
- cancellation；
- utilization；
- financing；
- customer concentration。

## 11. 当前判断

大型模型公司已经从普通 cloud customer 升级为 AI infrastructure 的 Anchor Buyer。

这一变化解释了为什么：

- cloud 愿意提前建设 GW 级项目；
- custom silicon 获得稳定 workload；
- chip/HBM/power contract 期限变长。

因此，未来判断 AI infrastructure demand 时，必须把 OpenAI、Anthropic 等长期需求作为独立变量，而不是只看 hyperscaler CapEx。
