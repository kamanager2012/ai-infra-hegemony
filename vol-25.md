# 第二十五卷：Hyperscaler System-Stack Competition

## 1. Cloud 的反击已经从“自研芯片”升级为“自研系统”

Google、AWS、Microsoft、Meta 的竞争不应再用“ASIC vs GPU”概括。

真正的竞争对象是：

- accelerator；
- HBM；
- compiler/runtime；
- scale-up fabric；
- scale-out network；
- rack/pod；
- orchestration；
- internal workload。

因此，本报告定义：

**Cloud System-Stack Substitution**

来描述 hyperscaler 对 NVIDIA platform 的替代。

## 2. 为什么 hyperscaler 有能力做完整系统

四大云拥有：

- massive internal workload；
- data-center scale；
- software engineering；
- customer distribution；
- capital；
- power procurement；
- custom silicon team。

更重要的是，它们可以先在内部 workload 上部署，而不需要第一天就获得外部 developer ecosystem。

这给 hyperscaler 一个传统 chip startup 不具备的优势：

> 自己就是第一大客户。

## 3. Google：TPU / Ironwood

Google TPU 已经形成多代 architecture、compiler/runtime 和 cluster system。

Ironwood 代表这一路线继续向：

- high HBM capacity；
- large pod；
- AI inference/training system

扩展。

Google 的竞争力不只是 chip design，而是：

TPU + XLA/software + network + cloud workload。

这是完整 system-stack 逻辑。

## 4. AWS：Trainium

AWS Trainium 同样围绕：

- custom accelerator；
- Neuron；
- UltraServer；
- AWS workload；

构建系统。

Anthropic/AWS 的长期 compute commitment 又给这一路线提供 Anchor Compute Buyer。

因此，Trainium 不是孤立芯片，而是：

> cloud + chip + software + anchor workload

组合。

## 5. Microsoft：Maia

Microsoft Maia 的战略意义来自：

- Azure workload；
- model/customer demand；
- internal software；
- data-center scale。

Maia 的长期竞争力取决于它能否形成：

- stable compiler/runtime；
- high utilization；
- strong scale-up；
- large HBM configuration；
- broad Azure deployment。

Microsoft 不需要第一天复制 CUDA 全部 ecosystem，只需要在足够大内部 workload 上形成成本优势。

## 6. Meta：MTIA

Meta 拥有超大 recommendation 与 generative AI workload。

MTIA 路线证明：

> hyperscaler 可以先针对内部特定 workload 做 specialization，再逐渐扩大 system scope。

这一策略与通用 GPU 不同。

它的核心目标不是“任何模型都能跑”，而是：

> 自己最大的 workload 能否获得更低长期 TCO。

## 7. 自研系统对 NVIDIA 的两种影响

### 7.1 Platform-profit diversion

hyperscaler 自研：

- 减少外购 GPU；
- 降低软件依赖；
- 增强采购议价；
- 保留更多 cloud/platform margin。

### 7.2 Upstream resource competition

自研系统仍可能需要：

- advanced logic；
- HBM；
- packaging；
- power。

因此，它们会与 NVIDIA 竞争相同 upstream resource。

所以：

> cloud custom silicon 可以同时削弱 NVIDIA 平台利润，并强化 TSMC/HBM/packaging 的资源紧张。

## 8. 什么情况下 custom silicon 才算真正替代

单颗芯片 benchmark 领先不够。

至少需要：

1. compiler/runtime mature；
2. large-cluster scaling；
3. high utilization；
4. workload migration cost acceptable；
5. HBM/packaging supply；
6. stable rack/pod deployment；
7. significant real workload share。

只有这些条件成立，才是 system-stack substitution。

## 9. Cloud CapEx 的真正意义

hyperscaler 的 CapEx 不只是“买更多 NVIDIA GPU”。

它同时投入：

- custom silicon；
- network；
- memory；
- data center；
- power。

因此，CapEx 增长既可以利好 NVIDIA，也可以加速 NVIDIA 的替代系统。

这也是为什么不能把 cloud CapEx 与 NVIDIA revenue 直接对敲成“算力税率”。

## 10. 竞争的长期均衡

最可能的长期格局不是“一方彻底消灭另一方”，而是 workload segmentation：

### NVIDIA

更强于：

- general-purpose frontier training；
- broad external developer ecosystem；
- heterogeneous enterprise workload。

### Hyperscaler custom stack

更强于：

- massive internal workload；
- repeatable model architecture；
- vertically optimized inference/training；
- cloud-specific TCO optimization。

竞争边界会随着 software maturity 与 workload structure 持续移动。

## 11. 当前判断

截至 2026 年 8 月：

- cloud custom silicon 已是实质竞争力量；
- 竞争单位已经上移到 system stack；
- frontier training 仍没有完全脱离 NVIDIA；
- custom system 仍大量依赖 advanced logic、HBM、packaging 和 power。

因此，cloud system-stack substitution 是最有可能把 S2 Baseline Concentration 推向 S1 Competitive Expansion 的变量之一。
