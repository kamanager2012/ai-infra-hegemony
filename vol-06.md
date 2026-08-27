# 第六卷：模型公司单位经济、算法效率与开源竞争

## 1. 模型层不是独立于基础设施的“纯软件生意”

模型公司表面上出售 API、订阅和智能体服务，底层成本却来自：

- accelerator time；
- HBM bandwidth；
- KV cache；
- storage / retrieval；
- networking；
- tool/API calls；
- human review；
- cloud margin；
- model serving utilization。

因此，AI 软件不能简单沿用传统 SaaS“复制成本接近零”的成本结构。

本报告将模型公司成本统一放入 **AI Software Unit Economics** 框架，而不是使用固定“毛利率必然从 85% 降到 55%”之类的行业结论。

## 2. 算法效率改变的是需求函数

DeepSeek-V3 等架构的重要意义，不是证明“前沿模型已经不需要昂贵算力”，而是说明算法能够显著改变单位任务的 compute、memory 与 communication 需求。

DeepSeek-V3 技术材料报告约：

- 671B total parameters；
- 37B activated parameters；
- 2.788M H800 GPU-hours for pre-training。

若以 $2/GPU-hour 进行外部成本换算，则约为 **$5.576M**。这一数字属于报告侧租金折算，不等于 DeepSeek 实际现金支出，也不包括完整研发、数据、实验、失败训练和基础设施成本。

这种案例真正说明的是：

> frontier capability 与总算力投入之间并不是固定线性关系。

算法创新可以降低每单位智能所需的 compute，但如果需求量同时快速增长，总基础设施需求仍可能继续上升。

## 3. MLA 与 KV cache：为什么推理成本可能快速下降

自回归推理经常受到 memory bandwidth 与 KV cache 限制，而不只是 peak FLOPS 限制。

Multi-head Latent Attention（MLA）等设计通过压缩 KV 表示，可以显著降低长上下文推理的 memory footprint。

这类优化会产生三个直接结果：

1. 同一块 HBM 可以容纳更多并发；
2. 单位 token 的 memory traffic 下降；
3. 同一套 hardware 的 utilization 提高。

因此，算法效率首先攻击的是**单位推理成本**。

但它不会自动消灭：

- HBM；
- advanced packaging；
- interconnect；
- rack-scale systems。

如果更低价格带来更高 token demand，基础设施总需求仍可能增长。这是典型的 Jevons-style rebound effect。

## 4. 开源模型攻击的是模型层利润，而不是全部基础设施利润

开源模型对闭源厂商形成三种压力：

### 4.1 Price compression

模型权重和推理框架可获得性提高，使 API price 更难维持高溢价。

### 4.2 Capability diffusion

企业可以在自有 cloud 或 private infrastructure 上部署模型，减少对单一模型 API 的依赖。

### 4.3 Switching option

模型层的替代速度通常快于底层 accelerator、HBM、network 与 data center 的替代速度。

因此，开源可能让**模型层利润池变薄**，同时把价值继续向 infrastructure layer 推移。

这也是为什么“模型价格下降”和“AI 基础设施需求下降”不能画等号。

## 5. Cloud custom silicon 改变模型公司的议价结构

Google TPU、AWS Trainium、Microsoft Maia、Meta MTIA 给模型公司和内部 workload 提供 NVIDIA 之外的计算路径。

这种替代的经济意义取决于四项变量：

- workload compatibility；
- compiler/runtime maturity；
- HBM 与 interconnect configuration；
- effective utilization。

如果一个 ASIC 的理论成本更低，但 workload migration、debug、parallel scaling 或 utilization 明显更差，则系统 TCO 未必更低。

所以模型公司的真正选择不是“GPU vs ASIC”，而是：

> 哪一套 system stack 能以最低单位任务成本稳定运行自己的 workload。

## 6. Anchor Compute Buyer Effect

大型模型公司正在从普通 cloud customer 变成长期基础设施买方。

OpenAI Stargate 与 Anthropic/AWS 等公开项目表明，模型公司开始用多年、GW 级、长期 chip / compute commitments 锚定基础设施建设。

这形成 **Anchor Compute Buyer Effect**：

long-duration model demand  
→ cloud / infrastructure provider 获得建设确定性  
→ chip、HBM、packaging、power 可以提前锁定  
→ model company 反过来影响基础设施 roadmap。

因此，模型公司并非只能被动接受 cloud price。超大模型买方本身已经成为基础设施资本形成的重要变量。

## 7. 模型公司面临的核心商业问题

模型公司能否形成可持续利润，最终取决于：

```text
Revenue per task > Total cost per task
```

其中 Total cost 至少包括：

- inference compute；
- memory / storage；
- retrieval；
- third-party tools；
- human review；
- failed/retried tasks；
- safety/compliance；
- cloud margin。

因此，未来 AI 软件公司之间真正有意义的比较不是“毛利率应该是多少”，而是：

- cost per completed task；
- gross margin after inference；
- revenue per workflow；
- retention；
- human replacement or augmentation value；
- utilization of reserved compute。

## 8. 当前判断

截至 2026 年，模型层已经出现明显的价格竞争和能力扩散，但这并没有证明基础设施需求进入下降周期。

更可能同时发生的是：

- 单位 token cost 下降；
- token volume 上升；
- model layer margin 被压缩；
- infrastructure utilization 提高；
- 大模型公司通过长期合同反向锚定基础设施。

因此，算法效率既可能成为 AI infrastructure 的“需求打断器”，也可能成为扩大总需求的“使用量放大器”。

判断哪一种效应占主导，需要观察真实 workload、utilization 与单位任务经济，而不是只看 benchmark。
