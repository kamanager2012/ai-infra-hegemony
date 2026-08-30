# Part IV · 第28章：2026–2036 时间线与阶段性里程碑

## 1. 时间线是 Conditional Milestone Map，不是按年份编排的叙事

未来十年最容易出现的错误，是把技术 roadmap、capital plan 和 power project 的目标年份写成“必然发生”。

本报告把时间线分成：

- **Phase I：2026–2027**；
- **Phase II：2028–2030**；
- **Phase III：2031–2033**；
- **Phase IV：2034–2036**。

年份是观察窗口，不是事件保证。

## 2. Phase I：2026–2027 — System Race 与 Infrastructure Lock-in

当前已经确认的主要锚包括：[^1][^2][^3][^4][^5][^6]

- NVIDIA FY27 Q2 Data Center revenue **US$89.0B**；
- GAAP gross margin **75.0%**；
- Rubin **full production**；
- manufacturing, supply, and capacity commitments 由 2026-01-25 **US$95.2B** → 2026-04-26 **US$119B** → 2026-07-26 **US$279B**；
- TSMC advanced-packaging tightness 仍限制 customer growth；[^7]
- 四大云厂公开资本投入指标仍处高位，但必须保留各自 actual / guidance / expectation 身份；[^8]
- power / LPS project 已出现约 835 MW、up to 1,920 MW、up to 500 MWe，以及 PORTS-Pike initial 4.25 IT-GW design capacity 等不同成熟度路径；[^9]
- TrendForce **预计** HBM + RDIMM 约占 2026 DRAM bit supply **51%**；
- Sony FY2026 hardware planning 已把 PS5 unit-sales / promotion flexibility 与可按合理价格获得的 memory volume 直接联系。[^10]

这个阶段的核心问题是：

> **AI workload demand 是否继续快于 scarce-layer supply expansion？**

主要里程碑：

- Rubin volume deployment / customer adoption；
- HBM4 ramp；
- advanced-packaging expansion 是否解除 growth constraint；
- TPU / Trainium / Maia / MTIA 新一代生产部署；
- Stargate / Anthropic 等 Anchor Buyer commitments 的实际 delivery；
- contracted power 向 energized / utilized MW 的转化；
- system-seller commitments 是否继续增长；
- smartphone / PC / game console 等直接暴露整机的 memory / storage pressure，是继续转化为 configuration / promotion / hardware-cadence pressure，还是开始缓解。

## 3. Phase II：2028–2030 — Substitution 是否真正形成规模

这一阶段更可能决定 S1 与 S2/S3 的分叉。

### Cloud System-Stack

要看 TPU、Trainium、Maia、MTIA 是否：

- 持续承担大型 production workload；
- 在 frontier training / high-value inference 中扩大份额；
- 获得更多 external customer adoption；
- 形成稳定 utilization 与 system TCO 优势。

### Software Portability

要看 open compiler/runtime、model format、network interface 是否明显降低 CUDA / proprietary-stack migration cost。

### Memory / Packaging

要看 HBM supply 是否进入持续宽松，advanced packaging 是否不再被厂商称为 growth constraint，新 packaging architecture 是否真正提高供给弹性。

### End-System Residual Pressure

这一阶段还要看上游扩产是否真正回到整机侧，而不是只看 supply headline：

- smartphone / PC 的 same-price configuration 是否恢复提升；
- game console 的 memory procurement、promotion 与 long-generation cost-down 是否恢复正常；
- automotive / industrial 的 mature-memory、EOL、lead time 与 qualified-alternate 状态是否改善；
- quantity assurance 差距是否缩小；
- supplier product mix 是否重新平衡。

如果上游 supply elasticity 提高，但上述整机代理长期不改善，就说明“总产能增长”尚未转化为 **effective non-AI residual supply**。

### Power / LPS

要看已公布的 contracted / secured capacity 有多少真正转化为 energized、utilized capacity，以及 Time-to-Power 是否仍决定 site selection。

PORTS-Pike 的公开计划是从 **2028 年开始分阶段上线**，因此它是 Phase II 检验“secured LPS 是否真正变成 deployable compute”的重要观察点，而不是 Phase I 的已运行容量。[^9]

## 4. Phase III：2031–2033 — 地理与产业结构可能开始固化

如果 AI infrastructure 持续扩大，到这一阶段竞争会进一步从产品路线转向 regional system capability。

需要观察：

- 哪些地区形成 **power + data center + chip access + software / talent** 的组合优势；
- China frontier parallel stack 是否跨过更多 Production-Grade Gates，以及 autonomous frontier closure 是否跨过更多 upstream / infrastructure gates；
- sovereign AI 是否形成多个 regional system ecosystems；
- supply chain 是继续跨区域互补，还是长期分区；
- advanced manufacturing redundancy 是否真正获得 qualified second-source capability；
- 长生命周期整机的 quantity assurance、qualified second source 与 supplier longevity 是否改善，还是逐步固化为结构性升级税。

这一阶段更重要的指标是：

- deployable compute；
- system utilization；
- energized power；
- cross-stack portability；
- regional supply resilience。

## 5. Phase IV：2034–2036 — 成熟、集中、分散或资本清算

到这一观察窗口，四类结构会更容易区分：

### Competitive Expansion

多套 system stacks 成熟，migration cost 下降，供给弹性提高，市场继续扩大但 value capture 更分散。对整机侧，quantity assurance 改善，same-price configuration 与 long-life supply continuity 恢复。

### Baseline Concentration

少数 dominant platforms 与 scarce-layer suppliers 长期并存，同时保持真实替代路径。整机 residual pressure 仍然选择性存在，但没有演变成所有行业统一短缺。

### Resource Hegemony

logic、HBM、packaging、software / interconnect 与 power 的协调能力进一步集中。若 second path 长期不足，低议价和长认证整机的 quantity-assurance gap 与 upgrade-tax risk 进一步固化。

### Capital Hard Landing

已建基础设施相对 workload 过剩，产业从建设竞赛转向利用率、残值与现金流清算。部分资源可能回吐给传统整机，但 supplier retrenchment、库存清算与专用产能折旧也可能造成新的 supply-chain whiplash。

## 6. 不应预写死的未来技术节点

时间线不预设：

- exact wafer price；
- exact future-node ASP；
- exact CoWoS wafers/month；
- exact GW/rack count；
- exact company market share。

这些变量高度依赖 yield、architecture、product mix、demand、regulation 与 capital cycle。

本报告只记录可证伪的 condition / milestone，不把远期目标年份写成已发生事实。

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
- infrastructure financing terms；
- supplier equity / credit support；
- refinancing dependency / third-party risk capital。

技术 timeline 与 capital timeline 必须在同一表中读取。

## 9. Power Milestones

power / LPS 统一使用：

> **Announced → Contracted / Secured → Permitted → Construction / Transition → Energized → Utilized**

Crane、Talen/AWS、Kairos/Google、PORTS-Pike 等项目都必须按当前 state 更新，不能在合同签署、LPS secured 或 design-capacity 公布时直接标记为 AI power online。Generation MW/GW、PPA capacity 与 IT-GW 也不能机械互换。

尤其 Talen 2026 Q2 10-Q 的 April-2026 revised-PPA transition 状态，不等于全部物理转换或 full delivery 已完成；较早 2025 10-K 的 spring-2027 full-transition expectation 与 no-later-than-2032 ramp 仍提供物理时钟背景。[^5]

## 10. 四个决定未来结构的临界点

未来十年真正决定 S1–S4 的不是某一个年份，而是四个 threshold：

1. **System substitution 是否跨过 production frontier-workload threshold；**
2. **Scarce-layer supply 是否跨过 durable-abundance threshold；**
3. **AI workload monetization 是否跨过 capital-cost coverage threshold；**
4. **基础设施是否能够从 sponsor / seller-supported financing 过渡到更独立、可持续的 long-duration capital structure。**

只要这些临界点没有同时明朗，2036 就应继续被视为条件截面，而不是确定答案。

## References

[^1]: NVIDIA, FY27 Q2 official results, Data Center revenue, GAAP margin and Rubin production status, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^2]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^3]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^4]: Constellation, Crane Clean Energy Center / Microsoft PPA, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
[^5]: Talen Energy, 2026 Q2 Form 10-Q and 2025 Form 10-K, revised AWS PPA state and ramp, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm ; https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
[^6]: Kairos Power / Google partnership, 2030 / 2035 development milestones, https://www.kairospower.com/google
[^7]: TSMC, 2Q26 Earnings Conference Transcript, packaging capacity limiting customer growth, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^8]: Microsoft FY26 Q4 earnings, https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast ; Alphabet Q2 2026 company CapEx guidance reported by Reuters, https://www.reuters.com/business/google-quarterly-cloud-revenue-growth-beats-expectations-2026-07-22/ ; Meta 2026 Q2 SEC Exhibit 99.1, https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm ; Amazon 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
[^9]: NVIDIA, PORTS-Pike Technology Campus / SB Energy / OpenAI, 2026-08-17, initial 4.25 IT-GW design capacity and phased online plan beginning in 2028, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx


[^10]: Sony Group, FY2025 Q4 earnings speech / FY2026 outlook, PS5 hardware-sales / promotion management tied to memory procurement at reasonable prices, https://www.sony.com/en/SonyInfo/IR/library/presen/er/pdf/25q4_sonyspeech.pdf
