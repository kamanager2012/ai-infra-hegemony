# Part III · 第24章：泡沫识别、资本清算与 S4

## 1. CapEx 很大，不等于泡沫

AI infrastructure 的资本开支已经进入极高水平，但投资规模本身不能证明泡沫。真正需要判断的是：资产建设速度、利用率、可实现现金流和残值之间是否持续脱节。

因此，本书不使用一个 CapEx 总额、一个估值倍数或一次科技股回撤作为“泡沫已破”的证据。S4 Capital Hard Landing 需要多类产业信号同步恶化。

## 2. 四类清算信号

### 2.1 Accounting

最慢但最硬的信号来自账面确认：impairment、inventory write-down、accelerated depreciation、asset disposal。它们说明企业已经承认原先预期的未来现金流或残值不足。

单季政策/库存项目不能自动升级成结构性崩溃。例如 NVIDIA FY26 的 H20-related charges 影响过利润，但 FY26 Q4 GAAP gross margin 已为 **75.0%**，FY27 Q1 为 **74.9%**，FY27 Q2 维持 **75.0%**。[^1][^2][^3]一次性 charge / release 与长期 system economics 必须分开。

### 2.2 Utilization / Revenue

资本周期最终要由有效 workload 付账。需要观察 compute utilization、revenue per deployed system、enterprise AI revenue 与 workflow monetization。

如果 utilization 高，巨额 CapEx 可以继续产生现金回报；如果大量资产长期低利用，折旧会先于收入形成压力。真正危险的不是“机器很多”，而是：**资产越来越多，而能够产生现金流的有效 workload 没有同步增长。**

### 2.3 Market Clearing

市场往往早于财报反映松动。重要指标包括 used accelerator / system price、lease rate、cloud instance discount、delivery lead time、HBM price、advanced-packaging availability 与 resale liquidity。

如果新一代硬件快速替代旧一代，economic depreciation 会快于 accounting depreciation。持续的二手价格折让和交期缩短，比单一股价回撤更接近真实去库存。

### 2.4 Forward Commitment

下一轮扩张是否继续，要看 hyperscaler CapEx guidance、NVIDIA manufacturing/supply/capacity commitments、long-duration model-company compute contracts 与 power commitments。

NVIDIA commitments 的公开轨迹由 2026-01-25 的 **US$95.2B**、2026-04-26 的 **US$119B** 上升到 2026-07-26 的 **US$279B**。[^4]FY27 Q2 10-Q 说明最新承诺主要关联 data-center infrastructure systems 所需的 memory 与 manufacturing facilities。当前轨迹更像继续前置锁资源，而不是已经进入普遍撤单。

## 3. 四云 CapEx 必须分公司、分会计口径观察

统一的“2026 AI hardware CapEx”并不存在。当前可公开追踪的规模包括：

**Table 24.1 — 四大云厂 2026 年资本投入公开口径**

| 公司 | 2026 当前公开口径 | 身份 |
|---|---:|---|
| Microsoft | calendar-2026 reported CapEx expectation ~US$175B | expectation；受 lease classification 影响，underlying investment expectation unchanged |
| Alphabet | US$195–205B | Q2 guidance |
| Meta | US$130–145B | Q2 guidance；含 finance-lease principal |
| Amazon | US$169.007B | TTM PPE net purchases actual through 2026-06-30 |

**Source:** Microsoft FY26 Q4 earnings materials、Alphabet 2026 Q2 SEC Exhibit 99.1、Meta 2026 Q2 SEC Exhibit 99.1、Amazon 2026 Q2 Form 10-Q.[^5][^6][^7][^8]  
**Note:** expectation / guidance / TTM actual 的时间窗与会计口径不同，不构成可直接相加的统一 AI hardware CapEx。

这些数字的时间窗和会计科目不同，**不能机械相加成统一 AI hardware CapEx**。历史情景中的 US$215B、US$670–750B 等统一总额如果缺乏可比口径，只能保留为旧压力测试，不进入事实层。

## 4. Seller 与 Buyer 的资本时钟不同

NVIDIA 是 system seller，hyperscaler 是 asset buyer。卖方可以在出货时先确认收入和利润，买方则在之后多年承担服务器、机房、网络、电力和长期合同的利用率与折旧风险。

因此，周期下行往往不是同步发生：

**buyer ROI 先恶化 → next-generation orders / commitments 放缓 → seller growth 后续下降 → manufacturing utilization 再向上游传导。**

这解释了为什么 seller margin 仍高，并不能证明 buyer-side ROI 一定健康；同样，buyer ROI 出现压力，也不意味着 seller economics 当季就会崩塌。

## 5. Algorithmic efficiency 既可能制造过剩，也可能延长周期

如果相同 capability 所需 compute 快速下降，而 workload volume 没有同步增长，已部署 capacity 可能出现过剩；如果更低成本刺激了大量新 workload，则效率提升反而会增加总基础设施需求。

所以正确关系不是“模型更高效 → GPU 必然过剩”，而是：

**Net Infrastructure Demand = efficiency effect × demand elasticity**。

模型价格战同理。token/API price 下跌只能证明单位价格变化，不能单独证明 total token volume、workflow adoption 和 infrastructure utilization 同步下降。

## 6. Anchor Compute Buyer 已成为新的领先指标

OpenAI Stargate、Anthropic/AWS 等长期容量承诺使模型公司从普通租户上升为基础设施 anchor buyer。它们可以提高项目融资确定性，让数据中心、电力、芯片和内存提前建设。

这也意味着 S4 的领先信号不再只是“云厂砍 CapEx”，还包括：

- 长期模型容量承诺缩减、改期或重谈；
- GW 级项目实际 ramp 显著落后；
- 已签长期容量利用率不足；
- 上游预付款与卖方 commitments 同时放缓。

如果这些变量与 buyer utilization、市场清算价格一起转弱，资本硬着陆的证据强度会明显上升。

## 7. 清算顺序具有资产久期

短周期资产先清算，长周期资产后清算。典型顺序更接近：

**未上架 hardware / inventory → system residual value → server utilization → data-center lease → long-duration power/project economics**。

因此，S4 可能持续多年，而不是一个季度完成。电厂、变电设施和数据中心壳体不会像 GPU 库存一样快速消失，它们可能降价、换主人、重谈合同，或者在下一轮集中化中重新成为稀缺资产。

## 8. 什么才叫 S4 Capital Hard Landing

本书只有在以下四类变量出现同步恶化时，才把 S4 从压力测试上调为现实主情景：

1. **Accounting**：impairment / write-down / disposal 明显增加；
2. **Utilization / Revenue**：利用率与有效 AI revenue 持续弱于资产扩张；
3. **Market Clearing**：二手价格、租赁价格、交期、HBM/packaging clearing 同步转松；
4. **Forward Commitment**：CapEx guidance、seller commitments、Anchor Buyer contracts 与 power commitments 同时放缓或取消。

股价下跌、模型价格下降、某一季毛利波动或一个历史压力测试不满足，都不足以单独证明 S4。

## 9. 当前判断

截至 2026 年 8 月，公开事实更接近：

> **高强度资本扩张 + ROI 压力上升**

而不是已经确认的 AI-infrastructure bubble collapse。NVIDIA FY26 non-GAAP free cash flow 仍为 **US$96.575B**，[^1] FY27 Q2 GAAP operating income 为 **US$63.734B**，[^3] supply/capacity commitments 已升至 **US$279B**；[^4]同时 hyperscaler 仍在给出极高的基础设施投资口径。

这不证明未来一定软着陆。它只说明：**要宣布资本清算已经成为现实主线，还需要 utilization、clearing price、accounting losses 与 forward commitments 的同步证据。**

## References

[^1]: NVIDIA, FY26 official results, NVIDIA-defined non-GAAP free cash flow and FY26 Q4 margin, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
[^2]: NVIDIA Corporation, FY27 Q1 Form 10-Q, GAAP gross margin 74.9%, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm
[^3]: NVIDIA, FY27 Q2 official results, GAAP gross margin 75.0% and GAAP operating income US$63.734B, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^4]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^5]: Microsoft, FY26 Q4 earnings / conference call, https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast
[^6]: Alphabet, 2026 Q2 SEC Exhibit 99.1, https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
[^7]: Meta Platforms, 2026 Q2 SEC Exhibit 99.1, https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm
[^8]: Amazon.com, 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
