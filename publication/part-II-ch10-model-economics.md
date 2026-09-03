# Part II · 第10章：模型单位经济、算法效率与开放模型竞争

## 1. Model Economics 不能脱离 Infrastructure Economics

API、subscription 与 agent service 都建立在真实 variable-cost stack 之上：accelerator time、HBM bandwidth、KV cache、storage / retrieval、networking、third-party tools、human review、cloud margin 与 serving utilization。

因此，AI software 不应默认按 near-zero-marginal-cost SaaS 建模。

真正相关的单位是：

> **Revenue per completed workflow − total variable AI cost per completed workflow**

## 2. Algorithmic Efficiency 改变的是 Demand Function

DeepSeek-V3 一手披露：

- 671B total parameters；
- 37B activated parameters；
- 14.8T pre-training tokens；
- **2.664M H800 GPU-hours** pre-training；
- **2.788M H800 GPU-hours** full formal training。[^1]

论文同时采用 **US$2/GPU-hour** 的假设；按这一论文假设做机械换算，**2.788M × US$2 = US$5.576M**。因此 US$5.576M 是基于论文参数的 **formal-training compute conversion / report-side arithmetic**，不是 DeepSeek 披露的完整企业研发成本。[^1]

2.788M H800 GPU-hours **包含 formal pre-training、context extension 与 post-training compute**。DeepSeek 论文明确说明，这一 compute figure **排除了 prior research 与 ablation experiments**，因此不能被理解成完整 enterprise R&D cost。[^1]

完整企业研发成本还会包含论文未覆盖或未按该 compute figure 计入的项目，例如：

- prior research / ablation experiments；
- data engineering；
- payroll；
- networking；
- storage；
- cluster depreciation；
- inference infrastructure。

这一案例真正说明的是：

> **frontier capability 与硬件投入之间不是固定线性关系。**

architecture、sparsity、routing 与 memory design 可以显著改变单位 capability 所需资源。

---

## 3. Algorithm 可以直接攻击 Memory Cost

DeepSeek-V2 相对 DeepSeek 67B 报告约：

- **93.3% KV-cache reduction**；
- **5.76× maximum generation throughput**。[^2]

这两个数字属于 DeepSeek-V2，不属于 V3。

其产业意义不在于“某个模型更便宜”，而在于：

> **算法可以直接攻击 memory traffic、cache requirement 与 serving concurrency，从而改变同一 HBM / accelerator 资产的有效产出。**

因此，模型竞争不只发生在 benchmark capability，也发生在：

- bytes/token；
- active parameters；
- cache；
- routing；
- utilization；
- serving throughput。

### 3A. Price Compression 不能直接推出 Aggregate Compute Demand 下降

Stanford AI Index 2025 给出一个历史量化锚：达到其所定义 GPT-3.5 等效 MMLU 水平的模型查询成本，从 2022 年 11 月约 **US$20 / million tokens** 降至 2024 年 10 月约 **US$0.07 / million tokens**，约下降 **280×**。[^3]

这个比较依赖特定 benchmark、时间窗口与模型集合，不能写成“所有模型价格都下降 280×”。但它足以证明：

> **单位能力价格可以快速压缩，model-layer rent 并不是固定不变。**

到 Stanford AI Index 2026，头部模型在 Arena 类评价中的表现进一步收敛，竞争压力因此更多转向 cost、reliability 与 domain-specific performance。[^4]

这强化了本章的核心机制：**单位模型价格下降与总基础设施需求增长可以同时发生**。真正决定总需求的仍然是 workload volume、resource intensity 与 utilization 的乘积。

---

## 4. Open Model 先压缩 Model-Layer Rent，再影响 Infrastructure Rent

open-model 与 open-weight availability 会扩大 capability diffusion、private deployment 与 model-switching option，同时压低 API premium。

**术语边界：** 本报告用 **open-model** 作为更宽的上位概念；只有在 model weights 可获得时才明确使用 **open-weight**。open-weight availability 本身不等于 open-source licensing，也不能自动推出 downstream rights 不受限制。

但模型层迁移速度通常快于：

- accelerator；
- HBM；
- networking；
- advanced packaging；
- data-center power。

因此完全可能出现：

> **model price compression + infrastructure utilization growth**

也就是说：

> **API price down ≠ infrastructure demand down**

开放模型首先压缩的是模型能力本身的稀缺租金。

基础设施是否受压，要看单位资源需求下降是否快于 workload volume 增长。

---

## 5. GPU vs ASIC 必须按 System TCO 比较

Google TPU、AWS Trainium、Microsoft Maia、Meta MTIA 为模型公司与 hyperscaler internal workload 提供第二条 compute path。[^5]

但真正应该比较的不是 accelerator die price，而是：

- workload compatibility；
- compiler/runtime maturity；
- HBM / interconnect configuration；
- cluster scaling；
- debugging / porting cost；
- failure recovery；
- effective utilization。

因此：

> **cheaper chip ≠ cheaper production system**

如果 theoretical chip cost 更低，但 migration、debug、reliability 或 utilization 更差，system TCO 未必更低。

完整的 hyperscaler system-stack competition 见第12章。

---

## 6. AI Software Unit Economics

单纯 cost/token 越来越不足以解释商业价值。

一个模型调用即使 token price 很低，如果：

- retry 很高；
- tool failure 很高；
- human review 很高；
- outcome 不稳定；

真实经济性仍然可能很差。

因此更有价值的指标是：

- cost per successful task；
- cost per verified workflow outcome；
- gross margin after model serving；
- revenue / productivity value per successful outcome；
- retry / failure rate；
- reserved-compute utilization。

模型公司最终出售的不是 token 本身，而是：

> **可以被用户接受、可以进入业务流程、可以创造价值的有效智能输出。**

Agent-native software 的完整 workflow economics 见第14章。

---

## 7. Anchor Buyer 让 Model Company 反向塑造 Infrastructure Formation

最大的模型公司正通过多年 compute commitments、dedicated data-center projects 与长期 capacity reservation 影响 cloud、chip 与 power investment。

因此，模型公司并不永远只是被动接受 cloud pricing 的软件买方。规模足够大时，它可以成为基础设施资本形成的 demand anchor。

同一机制也会放大风险：如果 architecture efficiency 提高、收入不及预期或 workload 迁移，长期 capacity commitments 会转化为 utilization 与 duration risk。

这一机制在第13章的 anchor-buyer analysis 中展开。

---

## 8. Price Compression 与 Rebound 可以同时成立

算法效率和 open-model competition 会降低 unit intelligence cost。

总基础设施需求可以抽象为：

> **Total Infrastructure Demand = Unit Resource Intensity × Total Workload Volume**

如果 resource intensity 下降，但 workload volume 增长得更快，总 demand 仍然会上升。

例如，从机制上讲：

- unit cost ↓；
- adoption threshold ↓；
- more workloads become economic；
- token / agent / workflow volume ↑。

因此，算法进步具有两种相反效应：

1. **Efficiency Effect**：同一任务需要更少资源；
2. **Rebound Effect**：更低成本刺激更多任务。

哪一种占主导，不能靠直觉判断。

例如，如果 unit resource intensity 下降 **50%**，而 workload volume 增长 **4×**，总基础设施需求仍然会上升。

这里还要加入第14章定义的 **AI inheritance**：大量潜在 AI workload 并不是从零生成，而是建立在 ERP、CRM、database、cloud、API、digital documents、source code 与既有 workflow 之上的增量 overlay。于是 workload volume 的长期增长既来自“单个任务调用更多”，也来自**已有数字流程逐步进入 AI penetration**。这使总需求判断必须同时观察 unit efficiency、workflow penetration、automation depth 与 execution frequency。

---

## 9. Model Layer 的 Long-Run Competitive Variables

未来模型公司之间最重要的经济变量包括：

### Capability per Unit Resource

相同 compute / memory 能产生多少有效能力。

### Serving Utilization

已预留基础设施能否保持高利用率。

### Model Portability

客户能否在不同模型之间低成本切换。

### Distribution

谁拥有持续、低成本获取 workload 的渠道。

### Monetization

模型能力能否转化为真实收入或可衡量生产率。

### Infrastructure Commitments

长期 compute commitment 是否与真实 workload growth 匹配。

最后一项会进一步进入 Anchor Compute Buyer 机制，详见第13章。

---

## 10. Current Read

截至 2026 年，更稳健的状态是：

- model-layer price competition 与 capability diffusion 已经发生；
- unit intelligence cost 继续下降；
- algorithmic efficiency 正在改变 compute / memory demand function；
- open-model / open-weight availability 正在提高 buyer optionality；
- 但 infrastructure demand 尚未因此进入确认下降周期；
- 总需求越来越取决于 workload growth、utilization 与 monetization。

因此：

> **算法效率既可能成为基础设施需求的打断器，也可能通过降低成本成为使用量的放大器。**

真正的分水岭不是 token price，而是：

> **单位资源效率提升之后，新增 workflow volume 和经济价值是否增长得更快。**

## References

[^1]: DeepSeek-AI, “DeepSeek-V3 Technical Report,” model architecture and formal-training compute, https://arxiv.org/abs/2412.19437
[^2]: DeepSeek-AI, “DeepSeek-V2,” technical report, MLA / KV-cache and throughput results, https://arxiv.org/abs/2405.04434 ; official repository, https://github.com/deepseek-ai/DeepSeek-V2
[^3]: Stanford HAI, “2025 AI Index Report — Research and Development,” inference-price comparison for a GPT-3.5-equivalent MMLU level, https://hai.stanford.edu/ai-index/2025-ai-index-report/research-and-development
[^4]: Stanford HAI, “2026 AI Index Report — Technical Performance,” frontier-model performance convergence and the shift toward cost, reliability and domain-specific competition, https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance

[^5]: Google, Ironwood TPU, https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; AWS, Amazon EC2 Trn3 UltraServers / Trainium3, https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ ; Microsoft, Maia 200, https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ ; Meta, MTIA 300, https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
