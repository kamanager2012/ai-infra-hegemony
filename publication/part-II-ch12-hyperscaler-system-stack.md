# Part II · 第12章：第二类 System Stack——Hyperscaler Substitution 如何真正成立

## 1. 真正的 Test 是 Workload Substitution，不是 Chip Availability

战略问题已经不是 hyperscaler 能不能设计 ASIC，而是 alternative stack 能否**以可接受的 TCO、migration cost、reliability 与 scale 吸收 production workload，并且跨代持续成立**。

因此，Google TPU、AWS Trainium、Microsoft Maia、Meta MTIA 必须按 system stack 判断：

- accelerator；
- HBM / memory subsystem；
- compiler/runtime；
- scale-up fabric；
- scale-out network；
- rack/pod；
- orchestration；
- production workload。

本报告把 **cloud system-stack substitution** 作为 economic substitution test，而不是独立理论。Benchmark win 不够；只有 production utilization、software friction 与 workload-specific system economics 同时过关，才构成真实替代。

---

## 2. Captive Workload 是真正的 Structural Advantage

四大云与普通 chip startup 最大的结构差异在于，它们同时拥有：

- massive internal workload；
- data-center scale；
- compiler / software engineering；
- cloud distribution；
- capital；
- power procurement；
- custom-silicon teams。

这使 hyperscaler 不需要在第一天复制 CUDA 的整个外部 ecosystem。

只要自研系统能够在大型 captive workload 上稳定降低成本，就已经可以创造真实经济价值。

其学习飞轮是：

> **internal workload → production feedback → system optimization → lower TCO → more internal workload**

这比“先做一颗芯片，再寻找客户”的传统 startup 路径更有利。

---

## 3. Google：TPU 已经是 System Stack

Google TPU 路线已经跨越多代。Ironwood 继续把产品定义上移到 large-scale pod / system。[^1] 到 **2026-03-31**，Google Cloud TPU release notes 已把 **TPU7x / Ironwood 标为 generally available**，因此这里已经不是单纯 product announcement，而是 external cloud availability。[^1]

Google 的真正竞争单元是：

> **TPU + XLA / compiler/runtime + high-bandwidth interconnect + HBM + pod + captive workload + cloud distribution**

所以评价 Google TPU 不应只问“一颗 TPU 比一颗 GPU 快多少”。

更重要的问题是：

- 在目标 workload 上 TCO 是否更低；
- large-scale utilization 是否稳定；
- compiler/runtime 是否足够成熟；
- workload 是否持续扩展；
- 外部 cloud customer 是否愿意采用。

即使 TPU 没有成为全行业通用开发平台，只要在足够大的 Google workload 上长期成立，就能分流 NVIDIA platform economics。

---

## 4. AWS：Trainium 是 System，不是 Component

AWS Trainium 同样已经从 accelerator 向 system 发展。

Trainium3 UltraServers、Neuron software stack、AWS networking、data-center deployment 与 cloud workload 共同构成完整路线。[^2] AWS 已在 2025-12-02 宣布 **EC2 Trn3 UltraServers general availability**，所以这条路径不是 roadmap-only。[^2]

AWS 的一个额外优势是 Anchor Workload。Anthropic 与 AWS 的长期 compute relationship 为 Trainium 提供了持续的大规模生产反馈。[^3]

这使 Trainium 的战略意义不再是“Amazon 有一颗自研芯片”，而是：

> **AWS 可以用 captive + anchor workload 持续优化 silicon、software、network 与 system economics。**

但这仍不等于已经取代 NVIDIA 外部生态。

需要继续验证：

- large-cluster scaling；
- compiler/runtime maturity；
- utilization；
- failure recovery；
- migration cost；
- broader customer adoption。

---

## 5. Microsoft：Maia 只有在 Azure-Scale Economics 闭合时才成立

Microsoft Maia 200 的合理评价标准，不是第一天支持所有 workload，而是能否在 Azure / Microsoft 内部足够大的 workload 上形成稳定成本优势。[^4] Microsoft 已明确 Maia 200 **部署在 US Central datacenter region**，US West 3 随后跟进，并将服务 GPT-5.2、Microsoft Foundry、Microsoft 365 Copilot 以及内部 synthetic-data / reinforcement-learning workload。[^4] 这是 first-party deployment evidence，但不是 fleet-wide utilization、production-workload share 或 realized TCO 的审计数据。

决定 Maia 长期竞争力的变量包括：

- compiler/runtime maturity；
- HBM configuration 与 supply；
- scale-up / scale-out capability；
- rack/data-center integration；
- utilization；
- Azure deployment scale。

如果这些变量在大型内部 workload 上成立，Maia 即使不是通用外部平台，也能降低 Microsoft 对第三方 accelerator economics 的依赖。

要进一步成为广泛外部替代，则还需要更低 migration cost、更广 software support 与更强 customer portability。

---

## 6. Meta：Specialization 不需要 Generality 也能形成替代

Meta 拥有超大 recommendation、ranking 与 generative-AI workload。

MTIA 300 的核心逻辑不是先成为 general-purpose accelerator，而是围绕最重要的内部 workload 做 specialization，并逐步把 silicon、software、networking 与 rack deployment 组织成 custom full-stack solution。[^5] Meta 2026-08 的工程披露已经给出 **“Performance in Production”** 证据：一个 **150B-parameter production recommendation model** 在 40 accelerators 上运行。[^5] 这说明 MTIA 300 已不是 demo-only，但其中性能比较仍属于 vendor-reported evidence，不是外部审计。

这条路线的经济目标是：

> **让最大、最重复、最可预测的内部 workload 获得更低长期 TCO。**

因此，custom silicon 不需要在所有 workload 上击败通用 GPU 才能产生价值。

---

## 7. Substitution 会先改变 Platform Economics，再改变 Upstream Scarcity

### 7.1 Platform-Rent Diversion

自研系统可以：

- 减少部分外购 accelerator；
- 降低对外部 software/platform 的依赖；
- 增强采购议价；
- 把更多 economics 留在 cloud platform 内部。

### 7.2 Upstream Scarcity 可以继续存在

但下一代 custom system 仍需要：

- advanced logic；
- HBM；
- advanced packaging；
- networking；
- power。

因此：

> **Cloud custom silicon 可以同时削弱 NVIDIA 平台利润，又强化 TSMC、HBM、packaging 与 power 的资源竞争。**

这两个结果并不矛盾。

---

## 8. Cloud CapEx 不是 NVIDIA-Revenue Proxy

hyperscaler CapEx 同时覆盖：

- custom silicon；
- third-party accelerator；
- network；
- memory；
- data center；
- power；
- office / fulfillment / other PPE。

而且各公司财年、PPE、finance lease 与 accounting definitions 不一致。

因此：

> **Cloud CapEx ≠ AI hardware subtotal ≠ NVIDIA purchases**

CapEx 上升既可能支持 NVIDIA 出货，也可能同时加速 NVIDIA 的替代系统。

所以不能用“四云 CapEx ÷ NVIDIA revenue”构造一个所谓固定“算力税率”。

---

## 9. Algorithmic Efficiency 是独立 Axis

算法与架构效率会直接影响 system demand，但它与 hyperscaler custom silicon 是不同竞争轴。

算法效率可能：

- 降低同一 workload 需要的 compute / memory；
- 降低 serving cost；
- 提高 hardware utilization；
- 刺激更多 token / workflow demand。

因此，效率提升既可能降低单位硬件需求，也可能通过 demand elasticity 扩大总 infrastructure demand。

DeepSeek 等案例的训练成本、架构效率与单位智能经济学详见[第10章：模型单位经济、算法效率与开放模型竞争](part-II-ch10-model-economics.md)。本章不再重复展开具体 GPU-hours 与 KV-cache 数字，以避免不同主题之间重复论证。

---

## 10. Real Substitution 的 Evidence Standard

单颗芯片 benchmark 不够。

至少需要同时观察：

1. compiler/runtime maturity；
2. large-cluster scaling；
3. high utilization；
4. workload migration cost；
5. HBM / packaging / power supply sustainability；
6. rack/pod deployment stability；
7. significant production workload share。

内部 workload 上成功已经可以形成真实经济价值。

但“全面削弱 NVIDIA 外部生态”还需要额外证明：

- 跨客户 portability；
- 跨 workload reliability；
- external developer adoption；
- migration cost 持续下降。

**Table 12.1 — Production substitution 的度量模板（宣称 S1 前必须先填实）。** 未在同一 denominator 下填实每一行，不得把 stack 从“真实第二路径”升级为“经济替代”。

| 指标 | 可观测代理 | 分母/单位 | 频率/时钟 | 不算数 |
|---|---|---|---|---|
| Production-workload share | `custom-stack production workloads / total production workloads`，以同一 workload class（frontier training 或命名 inference tier）为准 | 同 class 的 workload 计数或 compute-time，以可披露者为准 | 可披露时按季度，否则按事件 | 出货量、发布公告、benchmark |
| Utilization | 同一 production workload 上的 fleet 实测利用率 | 同一 workload tier 上的已部署 accelerator | 财报/产品披露 | 名义容量、secured GW、设计 IT-GW |
| System TCO | 每验证 workload 的全成本（accelerator + memory + interconnect + 工程 + 故障） | 同一 workload tier、同一可靠性目标 | 按 generation | 单看 die 价格、单看峰值 FLOPS |
| Migration cost | 迁移命名 workload 的工程时间 + 性能损失 | 按命名 workload | 按 generation | 只存在 compiler/runtime |
| Upstream dependence | 自研 stack 的 logic / HBM / packaging / power 来源 | 按层物理单位 | 按 generation | 营收份额代理 |

截至 2026-08-28 cutoff，这些行在公开数据中尚不完整；因此本报告的结论上限为“真实第二路径”，而非已度量的经济替代。

---

## 10A. 两级 Threshold：Internal Economics 与 External Ecosystem

Cloud custom system 的“成功”至少有两个不同层级。

### Internal Economic Substitution

只要 custom stack 在 hyperscaler 自有或 anchor workload 中：

- 稳定运行；
- utilization 足够高；
- TCO 低于外购替代；
- 能持续跨代迭代；

就已经形成真实经济替代。

这一层不要求复制 CUDA 的全部外部生态。

### External Ecosystem Substitution

如果要进一步削弱通用外部 platform economics，则还需要：

- external customer adoption；
- developer portability；
- broader workload coverage；
- low migration cost；
- stable commercial support；
- multi-generation compatibility。

因此：

> **internal success ≠ external ecosystem replacement**

但 internal success 仍然足以改变 hyperscaler 的采购结构、议价能力和长期 platform-profit distribution。

## 11. 更可能的长期均衡是 Workload Segmentation

长期格局并不必然以一方消灭另一方告终；更合理的均衡是 **workload segmentation**。

这种 segmentation 还必须区分 **training topology** 与 **inference topology**。Frontier training 通常更敏感于大规模 collective communication、scale-up / scale-out fabric 与同步效率；inference 的瓶颈则更依赖 workload 形态，memory capacity / bandwidth、latency、batching、power efficiency 与 cost per token 的权重可以更高。与此同时，inference 并不等于“网络不重要”：Google Ironwood 仍把 9,216-chip pod 与专用 ICI 作为系统的一部分，Microsoft Maia 200 则明确以标准 Ethernet 扩展至最高 6,144 accelerators。[^1][^4]

因此，不能把 frontier-training 的互联壁垒机械外推到全部 inference，也不能因为 inference 更适合 custom silicon / Ethernet，就反过来假设大规模 inference 不需要系统级互联。真正需要比较的是**具体 workload topology 下的 memory、network、latency、utilization 与 TCO**。

### NVIDIA 更强的区域

- general-purpose frontier training；
- broad external developer ecosystem；
- heterogeneous enterprise workload；
- workload portability across customers。

### Hyperscaler Custom Stack 更强的区域

- massive internal workload；
- repeatable architecture；
- vertically optimized inference / training；
- cloud-specific TCO optimization；
- captive distribution。

两者边界取决于：

- software maturity；
- memory supply；
- interconnect；
- workload structure；
- migration cost。

---

## 11A. System-Orchestration Rent 取决于 Workload Topology

通用 system orchestrator 的经济价值并不会在所有 workload 上保持同一强度。

在高度同步的 frontier training 中，大规模 collective communication、scale-up fabric、failure recovery 与 cluster-wide software coordination 的系统复杂度很高，用户愿意为“确定性交付”支付更高 system premium。

当 production workload 中 inference 或较窄 fine-tuning 的比重提高时，一部分 workload 可能变得：

- 更容易拆分和并行；
- 更受 memory / latency / power 约束，而不是 collective communication 约束；
- 更适合 vertically optimized captive system；
- 更看重 cost per token / verified outcome，而不是最大通用性。

这会削弱某些 workload 对“通用 training-oriented coordination stack”的超额支付，并提高 hyperscaler custom system 的相对价值。

但本报告不接受“inference 占比超过 80%，orchestration rent 就崩塌”这种固定阈值。公开证据不足以支持统一 80% cutoff；而且大规模 inference 本身仍可能高度依赖 memory system、networking、scheduling、reliability 与 fleet orchestration。

因此真正需要监测的是：

- production workload 中 training / inference 的占比（仅在可披露时）；
- custom silicon 在 captive production workload 中的真实份额；
- alternative stack 的 cost per token / cost per verified workload；
- 不同 workload topology 的 memory / network intensity；
- migration cost 与 software portability；
- external customer adoption 与 captive internal use 的差异。

战略问题不是“推理会不会杀死系统协调”，而是：

> **当 workload topology 改变后，哪些 coordination layer 仍然稀缺、仍然能够持续变现？**

---

## 12. Current Read

截至 2026 年 8 月，最稳健的描述是：

- cloud custom silicon 已经成为实质竞争力量；
- 证据已经不再是 launch-only：Ironwood / TPU7x 与 Trn3 UltraServers 已 GA，Maia 200 已部署，MTIA 300 已有 vendor-reported production-workload evidence；
- 竞争单位已经从自研芯片上移到完整 system stack；
- hyperscaler 正在 accelerator、software、interconnect、rack/pod 与 workload economics 多层同时竞争；
- production-workload share、utilization、migration cost 与 realized TCO 的可比公开数据仍不完整；
- frontier training 与广泛外部生态仍未证明已经系统性脱离 NVIDIA；
- custom systems 仍大量竞争 advanced logic、HBM、advanced packaging 与 power。

因此：

> **cloud system-stack substitution 是最可能把 S2 — Baseline Concentration 推向 S1 — Competitive Expansion 的结构变量之一。**

但它的强度必须用 production workload share、迁移成本、利用率、外部 adoption 与上游资源依赖来衡量，而不是用产品发布数量衡量。

## 13. 什么事实会改变当前判断

如果 cloud custom systems 长期只停留在小规模 internal workload，且出现以下情况，应下调 cloud system-stack substitution 判断：

- production utilization 低；
- migration / debugging cost 持续高；
- external customer adoption 弱；
- multi-generation software compatibility 不足；
- HBM / packaging / power access 并未改善；
- hyperscaler 重新扩大对单一外部 platform 的依赖。

反过来，真正支持 S1 的不是新芯片发布，而是 production workload share、TCO、portability 与 external adoption 同时改善。

## References

[^1]: Google Cloud, “Ironwood TPU,” system architecture and 9,216-chip pod context, https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; Google Cloud TPU release notes, 2026-03-31, TPU7x / Ironwood generally available, https://docs.cloud.google.com/tpu/docs/release-notes
[^2]: Amazon Web Services, 2025-12-02, general availability of Amazon EC2 Trn3 UltraServers powered by Trainium3, https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/
[^3]: Anthropic, “Anthropic and Amazon expand collaboration,” long-duration AWS compute commitment, https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
[^4]: Microsoft, “Maia 200: the AI accelerator built for inference,” 2026-01-26, Maia 200 deployed in US Central with additional regions planned and named Microsoft/OpenAI workloads, https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/
[^5]: Meta Engineering, “MTIA 300,” 2026-08-24, production-recommendation workload evidence and system/network co-design, https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
