# Part II · 第12章：Hyperscaler System-Stack Competition

## 1. 竞争已经从 ASIC vs GPU 升级为 System Stack vs System Stack

把 Google TPU、AWS Trainium、Microsoft Maia、Meta MTIA 概括成“几颗 ASIC 挑战 GPU”，已经无法描述 2026 年的竞争状态。真正的竞争单位至少包含：accelerator、HBM、compiler/runtime、scale-up fabric、scale-out network、rack/pod、orchestration 与 production workload。

本书用 **Cloud System-Stack Substitution** 描述这一变化。它衡量的不是某颗芯片 benchmark，而是一套替代系统能否在真实 workload 上形成足够低的 TCO、可接受的迁移成本和稳定的大规模利用率。

## 2. Hyperscaler 的独特优势：自己就是第一批大客户

四大云与普通 chip startup 的结构差异在于，它们同时拥有：

- massive internal workload；
- data-center scale；
- compiler / software engineering；
- cloud distribution；
- capital；
- power procurement；
- custom-silicon teams。

它们不需要第一天就复制 CUDA 的整个外部 developer ecosystem。只要能在自己的大型 captive workload 上持续降低成本，就能产生真实经济价值，并通过生产反馈迭代 compiler、interconnect、rack 与 deployment tooling。

这也是 cloud custom silicon 最强的学习飞轮：**internal workload → production feedback → system optimization → lower TCO → more internal workload**。

## 3. Google：TPU 已经是芯片、软件、互联和 Pod 的组合

Google 的 TPU 路线已经跨越多代。Ironwood 继续把产品定义上移到大规模 pod / system：自研 accelerator 与 XLA/software、high-bandwidth interconnect、HBM 和 Google Cloud workload 共同形成完整栈。

所以 Google 的竞争力不是“一颗 TPU 比一颗 GPU 快多少”，而是：

> **TPU + compiler/runtime + network + pod + captive workload + cloud distribution**。

如果这套系统在特定 training/inference workload 上持续降低 total cost of ownership，它就可以分流 NVIDIA platform profit，即使它没有成为全行业通用开发平台。

## 4. AWS：Trainium 把芯片、Neuron 与 UltraServer 组合成系统

AWS Trainium 同样已经从 accelerator 向 system 发展。Trainium3 UltraServers、Neuron software stack、AWS networking/data-center deployment 与大规模 cloud workload 共同构成第二类系统。

其战略优势还包括长期 anchor workload。Anthropic 已公开深化与 AWS 的长期 compute relationship，这使 Trainium 不只是实验性 silicon，而拥有持续迭代 system economics 的大客户基础。

但“有 anchor workload”不等于已经取代 NVIDIA 外部生态。真正需要验证的是 large-cluster scaling、utilization、software maturity、迁移成本以及外部客户采用。

## 5. Microsoft：Maia 的价值取决于 Azure 内部规模化，而不是复制整个 CUDA

Microsoft Maia 的合理评价标准不是“是否第一天支持所有模型”，而是它能否在 Azure / Microsoft 内部足够大的 workload 上形成稳定成本优势。

长期竞争力取决于：

- compiler/runtime maturity；
- scale-up / scale-out capability；
- HBM configuration 与 supply；
- rack/data-center integration；
- high utilization；
- broader Azure deployment。

只要这些变量在足够大的内部 workload 上成立，Maia 就可以分流外购 platform economics；要进一步变成通用外部替代，则还需要更低 migration cost 与更广 ecosystem。

## 6. Meta：MTIA 证明“窄 workload 先优化”也是有效路径

Meta 拥有超大 recommendation、ranking 与 generative-AI workload。MTIA 的逻辑不是先成为 general-purpose accelerator，而是围绕最重要的内部 workload 做 specialization，并把 silicon、software、networking 与 rack deployment 逐步组织成 custom full-stack solution。

这条路线的经济目标是：

> **让自己的最大 workload 获得更低的长期 TCO。**

它不需要在所有 workload 上击败通用 GPU 才能产生价值。

## 7. Cloud custom system 对 NVIDIA 会产生两个同时存在的效应

### 7.1 Platform-profit diversion

自研系统可以减少部分外购 accelerator、降低对外部 software/platform 的依赖、增强采购议价，并把更多 economics 留在 cloud platform 内部。

### 7.2 Upstream resource competition

但下一代 custom system 仍需要先进逻辑、HBM、advanced packaging、networking 和 power。因此，自研系统的扩张又可能增加对与 NVIDIA 相同 upstream scarce resources 的竞争。

所以：

> **Cloud custom silicon 可以同时削弱 NVIDIA 平台利润，并强化 TSMC / HBM / packaging / power 的资源竞争。**

这两个效应并不矛盾。

## 8. Cloud CapEx 不是 NVIDIA revenue 的同义词

hyperscaler CapEx 同时覆盖 custom silicon、外购 accelerator、network、memory、data center、power、办公/履约等不同资产。各公司财年、PPE 与 lease accounting 也不同。

因此：

> **Cloud CapEx ≠ AI hardware subtotal ≠ NVIDIA purchases**

CapEx 上升既可能支持 NVIDIA 出货，也可能加速 NVIDIA 的替代系统。不能把四云资本开支与 NVIDIA revenue 直接对敲成一个“算力税率”。

## 9. DeepSeek 代表另一种竞争：公共算法降本

Cloud custom silicon 属于**私有降本**：Google、AWS、Microsoft 或 Meta 优化自己的 system economics，收益主要留在自己的平台内。

DeepSeek 所代表的算法/架构效率则更接近**公共降本**：如果一种架构显著降低训练或 serving 的 compute/memory requirement，其他开发者也可能采用类似方法，从而改变整个市场的单位智能成本。

DeepSeek-V3 Technical Report 的可核一手锚是：671B total parameters、37B activated parameters、14.8T pre-training tokens；pre-training **2.664M H800 GPU-hours**，完整正式训练 **2.788M H800 GPU-hours**。按论文采用的 US$2/GPU-hour 假设，**US$5.576M 对应完整正式训练 compute conversion**，不代表完整 R&D cost。

另一条独立证据来自 DeepSeek-V2：相对 DeepSeek 67B，报告 **93.3% KV-cache reduction** 与 **5.76× maximum generation throughput**。V2 与 V3 不能拼成同一个模型的单一结果。

## 10. 算法降本不会自动把基础设施需求清零

architecture efficiency 可以降低 bytes/token、training compute 或 serving cost，但总 infrastructure demand 仍取决于 demand elasticity：单位成本下降之后，新的 workload 是否增长得更快。

因此，DeepSeek 式效率提升对 hyperscaler 有双重影响：

- 可能降低同一 workload 需要的硬件；
- 也可能因为更低价格和更广应用刺激更大 token/workflow volume。

正确问题不是“效率提高，所以 CapEx 应该下降”，而是：**单位 workload 成本下降后，总有效 workload、利用率和收入能否覆盖已经形成的资本基数。**

## 11. 什么情况下才算 System-Stack Substitution 真正成立

单颗芯片 benchmark 不够。至少需要同时观察：

1. compiler/runtime mature；
2. large-cluster scaling；
3. high utilization；
4. workload migration cost acceptable；
5. HBM / packaging / power supply 可持续；
6. rack/pod deployment 稳定；
7. significant real workload share。

内部 workload 上的成功可以形成真实经济价值，但“全面替代 NVIDIA 外部生态”还需要证明跨客户、跨 workload 的迁移与 production reliability。

## 12. 长期均衡更可能是 Workload Segmentation

最现实的长期格局未必是一方完全消灭另一方，而更可能形成 workload segmentation：

**NVIDIA 更强的区域：** general-purpose frontier training、broad external developer ecosystem、heterogeneous enterprise workload。

**Hyperscaler custom stack 更强的区域：** massive internal workload、repeatable architecture、vertically optimized inference/training、cloud-specific TCO optimization。

边界会随着 software maturity、interconnect、memory supply、workload structure 和迁移成本不断移动。

## 13. 当前判断

截至 2026 年 8 月，最稳健的描述是：

- cloud custom silicon 已经成为实质竞争力量；
- 竞争单位已经从自研芯片上移到完整 system stack；
- hyperscaler 已经开始攻击 software、interconnect、rack/pod 与 workload 层，而不是只攻击 accelerator die；
- frontier training 与广泛外部生态仍未证明已经系统性脱离 NVIDIA；
- custom system 仍大量竞争 advanced logic、HBM、advanced packaging 与 power。

因此，**Cloud System-Stack Substitution 是最可能把 S2 Baseline Concentration 推向 S1 Competitive Expansion 的结构变量之一**，但它的强度必须用真实 workload share、迁移成本、利用率和上游资源依赖来衡量。

## 关键公开来源

- Google Ironwood TPU: https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/
- AWS Trainium3 UltraServers: https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/
- Microsoft Maia 200: https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/
- Meta MTIA 300: https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
- Anthropic / AWS compute collaboration: https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
- DeepSeek-V3 Technical Report: https://arxiv.org/abs/2412.19437
- DeepSeek-V2 repository / technical report: https://github.com/deepseek-ai/DeepSeek-V2