# Part III · 第19章：AI 基础设施资本形成——Utilization、Commitments 与 Duration Risk

## 1. Capital-Cycle Question 不是一个 Headline CapEx Total

当前产业显然处于高投资状态。真正需要回答的是：**这些资本形成了什么资产、由谁承担、经济寿命有多长，以及 productive workload 是否增长得足够快。**

Microsoft、Amazon、Alphabet、Meta 并不存在一个完全可比的“AI CapEx”口径。其 fiscal period、PPE definition、lease treatment 与 net-purchase metric 均不同。

因此必须先保留三个分离：

1. company-wide CapEx vs. AI-specific investment；
2. IT equipment vs. data-center / power infrastructure；
3. actual investment vs. guidance / expectation。

本章分析顺序是：**先确认 denominator identity，再判断 duration mismatch，最后用 utilization / monetization 检验资本周期是否成立。**

---

## 2. 2026 Public Capital Anchors

Microsoft、Amazon、Alphabet、Meta 的财年、PPE、finance lease、net purchases 与 guidance 定义并不一致。

本报告坚持三个分离：

1. **company-wide CapEx 与 AI-specific CapEx 分离**；
2. **IT equipment 与 data-center / power infrastructure 分离**；
3. **actual CapEx 与 guidance / expectation 分离**。

**Table 19.1 — 四大云厂 2026 年公开资本投入口径**

| 公司 | 2026 当前公开口径 | 身份 |
|---|---:|---|
| Microsoft | calendar-2026 reported CapEx expectation ~US$175B | expectation；lease-classification adjustment 后 underlying investment expectation unchanged |
| Alphabet | US$195–205B | Q2 full-year guidance |
| Meta | US$130–145B | Q2 guidance；含 finance-lease principal |
| Amazon | US$169.007B | TTM PPE net purchases actual through 2026-06-30 |

**Source:** Microsoft FY26 Q4 earnings materials；Alphabet Q2 2026 company guidance as reported by Reuters（SEC Exhibit 99.1 separately supports Q2 actual results）；Meta 2026 Q2 SEC Exhibit 99.1；Amazon 2026 Q2 Form 10-Q.[^1][^2][^3][^4]  
**Note:** 四家公司时间窗和会计口径不同，严禁机械相加为统一 AI hardware CapEx。

这张表能证明的是：**资本投入仍然非常高**。它不能证明“全球 AI CapEx 等于四家公司数字之和”，更不能证明这些支出全部用于 GPU 或 AI hardware。

---

## 2A. Corporate CapEx 只是 Capital Formation 的一个渠道

到 2026 年 8 月，AI infrastructure 的资本形成已经开始明显超出 hyperscaler corporate CapEx：

- operating lease / finance lease 可以改变 reported CapEx identity；
- third-party infrastructure capital 可以由独立 vehicles 承接；
- data-center developer 可以 build / own / operate，再通过长期 lease 回收；
- seller 可以通过 equity / credit enhancement 支持项目；
- PPA / generation / grid investment 可能出现在完全不同主体的资产负债表。

到 2026 年 8 月，AI infrastructure capital formation 已经超出 hyperscaler corporate CapEx。NVIDIA 宣布与六家大型资本提供方签署 MOU，目标是建立独立 compute-financing platforms，并在未来动员 **超过 US$500B 的 third-party capital**。[^5] 另一个 PORTS-Pike structure 则把 secured land / power / shell（LPS）、seller credit support、NVIDIA 对 SB Energy 的 **US$1.5B** investment，以及由 SB Energy build / own / operate、并以 **20-year lease** 租给 OpenAI 的 data center 组合起来。[^6]

风险侧 disclosure 同样重要。NVIDIA FY27 Q2 Form 10-Q 对相关 PORTS-Pike lease guarantees 的 aggregate obligations 设定 **US$105B** 上限，覆盖约 **4.25 GW IT load** 的 leases；guarantees 随九座 data centers 进入 service 分阶段生效，第一阶段预计在 **FY2029** 开始，并随着 OpenAI 履行 lease payments 而下降。[^8] **US$105B 是 maximum conditional guarantee exposure，不是 funded CapEx、当前 cash outflow，也不能与底层 lease demand 再加总一次。**

AMD 提供了独立 cross-vendor check。其 Q2 2026 Form 10-Q 披露，与部分 commercial-partner data-center lease obligations 相关 guarantees 的 **maximum gross exposure 为 US$4.1B**，期限最长 15 年。[^9] 该数字同样是 maximum guarantee exposure，不是 funded CapEx 或 realized loss。两份 filing 合在一起说明 supplier / sponsor credit support 已经是行业融资结构，而不是单一公司异常。

因此：

> **Hyperscaler CapEx 是重要观察变量，但已经不是 AI infrastructure capital formation 的完整分母。**

这也是为什么 2026 年的新 compute-financing platform、PORTS-Pike LPS structure、supplier-side guarantee exposure 与 Anchor Buyer long-duration contracts 必须单独进入资本分析。[^5][^6][^8][^9]

完整融资结构见[第23章：AI 基础设施资本市场与融资结构](part-III-ch23-capital-financing.md)。

## 3. Duration Mismatch 才是核心 Balance-Sheet Risk

AI infrastructure 不是一次性的 server purchase，而是多个经济寿命完全不同的资产共同建设：

- **accelerator / server**：技术迭代快，经济寿命相对短；
- **network / switching / cooling**：中周期；
- **data-center building / shell / mechanical systems**：长周期；Microsoft 自 FY27 起把 datacenter 与 office building 的 estimated useful life 从 **15 年延长到 25 年**。[^1]
- **substation / transmission / grid connection**：更长周期；
- **grid / generation / offtake**：contract / asset-specific，通常明显长于 compute；例如 Constellation / Microsoft Crane agreement 是 **20-year PPA**。[^7]
- **future workload revenue**：不确定，取决于真实客户采用和 monetization。

因此，AI infrastructure 的核心资本风险不是简单“花钱太多”，而是：

> **短周期 compute asset 与长周期 infrastructure asset，是否能够被同一组未来 workload 长期、稳定、足额利用。**

这形成 **Duration Mismatch**。

如果模型能力快速进步、单位 compute cost 持续下降、hardware generation 加速更新，而 data center 与 power assets 仍具有十年以上寿命，资本回收就越来越依赖 utilization 与 workload growth，而不是依赖设备本身保值。

---

## 4. Seller Economics 与 Buyer ROI 在不同 Clock 上清算

NVIDIA、memory supplier、foundry 与 hyperscaler 都在“增加资本投入”，但它们的资本再生产对象并不相同。

**System-platform seller**

现金流更直接用于：

- inventory；
- capacity reservation；
- supply commitments；
- next-generation roadmap；
- ecosystem / software；
- system integration。

其核心目标是提高下一代 scarce-resource access 与 system delivery certainty。

**Hyperscaler / Anchor Buyer**

资本则需要覆盖：

- land；
- building；
- cooling；
- power；
- network；
- custom silicon；
- third-party systems；
- operations；
- long-duration contracts。

更相关的比较不是“谁投得更多”，而是：

> **每一美元资本能否提高 productive utilization、降低单位 workload 成本，并改善下一代资源获取能力。**

---

## 5. Power 把 Hardware Clock 与 Infrastructure Clock 耦合

过去数据中心扩张主要受 server procurement 与 network deployment 影响；高密度 AI rack 使问题明显上移。

rack density 提升后，新增 compute capacity 还依赖：

- grid interconnection；
- substation；
- transformer；
- transmission；
- cooling；
- water / thermal management；
- firm power；
- long-duration generation contract。

semiconductor clock 与 power-permitting clock 由此耦合：

1. **Semiconductor Clock**：芯片、HBM、packaging 快速迭代；
2. **Infrastructure Clock**：电网、建筑、电源项目建设周期更长。

当 chip supply 缓解但 energized capacity 仍不足时，bottleneck 会从 manufacturing 转向 Time-to-Power。

这意味着产业扩张速度越来越不由单一芯片供应决定。

---

## 6. Utilization 是 Capital Cycle 的第一道经济检验

高 CapEx 可以有两种完全不同的含义。

**情形 A：高回报扩张**

如果以下变量同步增长：

- deployed compute utilization；
- token / workflow volume；
- enterprise adoption；
- revenue per deployed compute；
- customer commitments；
- verified workflow output；

那么大规模 CapEx 可以持续形成规模优势、供应优势与进入壁垒。

**情形 B：Overbuild**

如果同时出现：

- utilization 下滑；
- AI monetization 弱；
- next-year guidance cuts；
- commitment cancellation；
- cloud discount / lease rate 恶化；
- used-system residual value 下降；
- impairment / write-down 上升；

那么同一资本基数会从竞争优势转化为资本压力。

所以“超级周期”与“泡沫”的分界线不是 CapEx 绝对值，而是：

> **新增资本的增长速度，是否长期快于可验证 workload 与现金流的增长速度。**

## 6A. Demand Duration：AI 继承全球 Digital Installed Base

如果 AI 基础设施的需求只来自 frontier-model scaling，那么算法效率、模型压缩或一次供给扩张都可能显著缩短资本周期。

但现实需求池还包含另一条传导：

> **Digital Installed Base → AI Overlay → Workflow Penetration → Automation Depth → Workload Volume → Infrastructure Demand**

过去几十年的 IT 投资已经把大量企业活动转化为 software、database、API、digital document、identity system 与 networked workflow。AI 可以在这些既有数字流程上增加理解、生成、预测、决策与执行能力，而不需要重新完成一次完整的“从物理流程到数字化”的基础建设。

AI infrastructure 的 duration 不能只用“下一代模型需要多少 GPU”来判断，还要观察：

- enterprise digital-workflow base；
- AI penetration rate；
- assistant → agent / automation 的深度；
- execution frequency；
- cost per verified workflow；
- production reliability 与 human-review burden。

这也是为什么**算法效率大幅提高与总基础设施需求长期增长可以同时成立**：单位任务资源下降可以被更广的 workflow penetration、更多执行频次或更深 agent loop 抵消甚至超过。

但这一机制不是永久需求保证。若 AI 无法形成足够低成本、可靠、可验证的 workflow output，Digital Installed Base 只代表潜在 TAM，不代表真实 utilization 或 cash flow。

---

## 7. Capital-Cycle Reversal 的领先信号

判断 Capital Hard Landing，应持续观察五类变量，但确认 S4 不要求 five-of-five 同时满足；关键是多类因果独立信号跨主体/层级形成广泛、持续的 cross-confirmation。

**Accounting**

- impairment；
- accelerated depreciation；
- write-down；
- asset-life assumption change。

**Utilization / Revenue**

- deployed compute utilization；
- AI revenue；
- cost per verified workflow；
- revenue per unit of deployed infrastructure。

**Market Clearing**

- used-system price；
- cloud discount；
- lease rate；
- delivery lead time；
- inventory。

**Forward Commitment**

- CapEx guidance；
- supply commitments；
- compute contracts；
- power contracts；
- Anchor Buyer commitments。

**Demand Quality / Financing**

- customer cash generation；
- third-party capital 的 risk premium 与 commitment 变化；
- supplier equity / credit support 占比；
- refinancing dependency。

只有多类因果独立信号广泛、持续恶化，并具备 cross-actor / cross-layer breadth，才足以把“ROI pressure”升级为 **S4 — Capital Hard Landing**。Accounting 是 confirmation / severity evidence，不是 mandatory gate。

单一模型降价、股价调整、某一家公司 CapEx 下降，均不足以独立证明全行业进入资本清算。

---

## 8. 更大的 Capital Base 会提高下一阶段 Performance Hurdle

AI 基础设施的特殊之处在于：资本扩张越成功，下一阶段的业绩门槛反而越高。

原因是：

> **更大的 installed capital base → 更高折旧与 operating cost → 更高 required utilization → 更高 monetization requirement**

这意味着即使 AI demand 继续增长，只要增长速度低于资本基数增长速度，单位资本回报仍可能下降。

更有价值的长期问题不只是“AI 需求是否增长”，而是：

> **AI demand growth 是否足以覆盖 AI capital-base growth。**

这一差额决定资本周期是继续扩张、趋于正常化，还是进入清算。

---

## 9. Current View

截至 2026 年 8 月，公开数据仍更支持：

截至 2026 年 8 月，公开数据仍更支持一种 **capital formation 保持高位、同时 utilization 与 monetization hurdle 继续上升** 的高投资状态，而不是已经完成 capital clearing 的周期。

这还不是已经确认的全行业 Capital Hard Landing。

真正的转折需要看到 utilization/revenue、market clearing、forward commitments、demand-financing quality 与 accounting 等多类独立 signal families 跨主体、跨层级确认广泛恶化。Accounting 出现时会提高 severity assessment，但不是 mandatory gate。

## 10. 什么事实会改变当前判断

如果以下变化持续出现，应下调“capital expansion 仍是 dominant regime”的判断：

- hyperscaler underlying investment expectation 连续下降；
- data-center / power project cancellation 或 deferral 明显增加；
- seller supply commitments 收缩；
- third-party infrastructure capital risk appetite 下降；
- utilization 与 monetization 弱于新增资本；
- financing cost / refinancing pressure 明显上升。

单家公司 accounting reclassification 或单季 CapEx 波动，不足以证明超级周期已经结束。

## References

[^1]: Microsoft, FY26 Q4 earnings conference call, 2026-07-29, calendar-2026 CapEx expectation of approximately US$175B and datacenter / office-building estimated useful lives extended from 15 to 25 years, https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4
[^2]: Alphabet, Q2 2026 earnings-call full-year CapEx guidance **US$195–205B**, company guidance reported by Reuters, 2026-07-22, https://www.reuters.com/business/google-quarterly-cloud-revenue-growth-beats-expectations-2026-07-22/ ; Alphabet SEC Exhibit 99.1 separately supports Q2 actual results, https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
[^3]: Meta Platforms, 2026 Q2 SEC Exhibit 99.1, FY2026 CapEx guidance including finance-lease principal, https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm
[^4]: Amazon.com, 2026 Q2 Form 10-Q, TTM purchases of property and equipment, net of proceeds and incentives, https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm

[^5]: NVIDIA, 2026-08-10, strategic partnerships / MOUs to establish independent compute-financing platforms and mobilize more than US$500B of third-party capital over time, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Partners-With-Apollo-BlackRock-Blackstone-Brookfield-Goldman-Sachs-and-KKR-to-Establish-AI-Compute-Infrastructure-Financing-Platforms-to-Mobilize-Over-500-Billion-of-Third-Party-Capital/default.aspx
[^6]: NVIDIA, 2026-08-17, PORTS-Pike / SB Energy / OpenAI: secured LPS, NVIDIA credit support, US$1.5B SB Energy investment, and 20-year OpenAI lease, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx
[^7]: Constellation Energy, 2024-09-20, 20-year Microsoft power-purchase agreement for the Crane Clean Energy Center, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs

[^8]: NVIDIA Corporation, FY27 Q2 Form 10-Q, PORTS-Pike guarantees covering approximately 4.25 GW of IT load, aggregate obligations capped at US$105B, phased effectiveness across nine data centers with the first phase expected in FY2029, and exposure declining as OpenAI fulfills lease payments, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

[^9]: Advanced Micro Devices, Inc., Q2 2026 Form 10-Q, US$4.1B maximum gross exposure from guarantees tied to certain commercial-partner data-center lease obligations with terms up to 15 years; exposure declines as contractual lease payments are made, https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm
