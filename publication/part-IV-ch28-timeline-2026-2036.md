# Part IV · 第28章：2026–2036 时间线与阶段性里程碑

## 1. 时间线是 Conditional Milestone Map，不是年份故事

未来十年最容易出现的错误，是把技术 roadmap、capital plan 和 power project 的目标年份写成“必然发生”。

本书把时间线分成：

- **Phase I：2026–2027**；
- **Phase II：2028–2030**；
- **Phase III：2031–2033**；
- **Phase IV：2034–2036**。

年份是观察窗口，不是事件保证。

## 2. Phase I：2026–2027 — System Race 与 Infrastructure Lock-in

当前已经确认的主要锚包括：

- NVIDIA FY27 Q2 Data Center revenue **US$89.0B**；
- GAAP gross margin **75.0%**；
- Rubin **full production**；
- manufacturing, supply, and capacity commitments 由 2026-04-26 **US$119B** 升至 2026-07-26 **US$279B**；
- TSMC advanced-packaging tightness 仍限制 customer growth；
- hyperscaler infrastructure spending 继续处高位；
- power project 已出现约 835 MW、up to 1.92 GW、up to 500 MWe 等不同成熟度路径；
- TrendForce **预计** HBM + RDIMM 约占 2026 DRAM bit supply **51%**。

这个阶段的核心问题是：

> **AI workload demand 是否继续快于 scarce-layer supply expansion？**

主要里程碑：

- Rubin volume deployment / customer adoption；
- HBM4 ramp；
- advanced-packaging expansion 是否解除 growth constraint；
- TPU / Trainium / Maia / MTIA 新一代生产部署；
- Stargate / Anthropic 等 Anchor Buyer commitments 的实际 delivery；
- contracted power 向 energized / utilized MW 的转化；
- system-seller commitments 是否继续增长。

## 3. Phase II：2028–2030 — Substitution 是否真正形成规模

这一阶段更可能决定 S1 与 S2/S3 的分叉。

### Cloud System Stack

要看 TPU、Trainium、Maia、MTIA 是否：

- 持续承担大型 production workload；
- 在 frontier training / high-value inference 中扩大份额；
- 获得更多 external customer adoption；
- 形成稳定 utilization 与 system TCO 优势。

### Software Portability

要看 open compiler/runtime、model format、network interface 是否明显降低 CUDA / proprietary-stack migration cost。

### Memory / Packaging

要看 HBM supply 是否进入持续宽松，advanced packaging 是否不再被厂商称为 growth constraint，新 packaging architecture 是否真正提高供给弹性。

### Power

要看 headline contracted GW 有多少转化为 energized、utilized capacity，以及 Time-to-Power 是否仍决定 site selection。

## 4. Phase III：2031–2033 — 地理与产业结构开始固化

如果 AI infrastructure 持续扩大，到这一阶段竞争会进一步从产品路线转向 regional system capability。

需要观察：

- 哪些地区形成 **power + data center + chip access + software / talent** 的组合优势；
- China parallel stack 是否跨过多个 frontier closure gates；
- sovereign AI 是否形成多个 regional system ecosystems；
- supply chain 是继续跨区域互补，还是长期分区；
- advanced manufacturing redundancy 是否真正获得 qualified second-source capability。

这一阶段更重要的指标是：

- deployable compute；
- system utilization；
- energized power；
- cross-stack portability；
- regional supply resilience。

## 5. Phase IV：2034–2036 — 成熟、集中、分散或资本清算

到这一观察窗口，四类结构会更容易区分：

### Competitive Expansion

多套 system stacks 成熟，migration cost 下降，供给弹性提高，市场继续扩大但 value capture 更分散。

### Baseline Concentration

少数 dominant platforms 与 scarce-layer suppliers 长期并存，同时保持真实替代路径。

### Resource Hegemony

logic、HBM、packaging、software / interconnect 与 power 的协调能力进一步集中。

### Capital Hard Landing

已建基础设施相对 workload 过剩，产业从建设竞赛转向利用率、残值与现金流清算。

## 6. 不应预写死的未来技术节点

时间线不预设：

- exact wafer price；
- exact future-node ASP；
- exact CoWoS wafers/month；
- exact GW/rack count；
- exact company market share。

这些变量高度依赖 yield、architecture、product mix、demand、regulation 与 capital cycle。

publication layer 只记录可证伪的 condition / milestone。

## 7. Algorithmic Milestones

长期必须跟踪：

- memory compression；
- sparse architecture；
- quantization；
- inference scheduling；
- model routing；
- on-device capability；
- workload orchestration。

如果 unit resource intensity 大幅下降，但 total workload volume 增长更快，aggregate infrastructure demand 仍可能上升。

所以 algorithmic milestone 只有与 demand elasticity 一起观察才有意义。

## 8. Capital Milestones

每个阶段同时监测：

- hyperscaler CapEx；
- D&A / useful-life changes；
- seller supply commitments；
- Anchor Buyer contracts；
- utilization；
- second-hand / lease price；
- enterprise AI monetization；
- infrastructure financing terms。

技术 timeline 与 capital timeline 必须在同一表中读取。

## 9. Power Milestones

power 统一使用：

> **Announced → Contracted → Permitted → Energized → Utilized**

Crane、Talen/AWS、Kairos/Google 等项目都必须按当前 state 更新，不能在合同签署时直接标记为 AI power online。

尤其 Talen 2026 Q2 10-Q 的 April-2026 revised-PPA transition 状态，不等于全部物理转换或 full delivery 已完成；较早 2025 10-K 的 spring-2027 full-transition expectation 与 no-later-than-2032 ramp 仍提供物理时钟背景。

## 10. 三个决定未来结构的临界点

未来十年真正决定 S1–S4 的不是某一个年份，而是三个 threshold：

1. **System substitution 是否跨过 production frontier-workload threshold；**
2. **Scarce-layer supply 是否跨过 durable-abundance threshold；**
3. **AI workload monetization 是否跨过 capital-cost coverage threshold。**

只要这三个临界点没有同时明朗，2036 就应继续被视为条件截面，而不是确定答案。

## 关键公开来源

- NVIDIA FY27 Q2 official results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- NVIDIA FY27 Q2 10-Q: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
- TrendForce — 2026E HBM + RDIMM: https://www.trendforce.com/presscenter/news/20260825-13198.html
- Constellation / Microsoft Crane: https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
- Talen 2026 Q2 10-Q: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
- Talen 2025 10-K: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
- Kairos / Google: https://www.kairospower.com/google