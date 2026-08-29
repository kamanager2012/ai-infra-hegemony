# Part III · 第19章：AI 基础设施 CapEx 超级周期

## 1. 核心判断：资本扩张仍在继续，但产业问题已经从“投多少”转向“这些资本能否被有效利用”

截至 2026 年 8 月，Microsoft、Amazon、Alphabet、Meta 等 hyperscaler 的 infrastructure spending 仍处历史高位。真正重要的变化不是某一个 CapEx 绝对规模，而是：

> **AI infrastructure 已经从短周期 server procurement，扩展为 advanced logic、HBM、network、data center、cooling、substation、grid connection 与 long-duration power contract 共同驱动的资本周期。**

这使产业面临两个同时存在的现实：

1. **资本仍在扩张**：AI/HPC demand、model-company commitments 与 hyperscaler competition 继续推动大规模基础设施建设；
2. **回报门槛正在提高**：资本基数越大，未来越需要真实 utilization、workflow volume 与 monetization 去证明投资可持续性。

因此，本章不把“高 CapEx”直接等同于繁荣，也不把“高 CapEx”直接等同于泡沫。

---

## 2. 四大云厂的公开数字不能机械相加

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

## 2A. Corporate CapEx 已不再等于全部 AI Infrastructure Capital Formation

到 2026 年 8 月，AI infrastructure 的资本形成已经开始明显超出 hyperscaler corporate CapEx：

- operating lease / finance lease 可以改变 reported CapEx identity；
- third-party infrastructure capital 可以由独立 vehicles 承接；
- data-center developer 可以 build / own / operate，再通过长期 lease 回收；
- seller 可以通过 equity / credit enhancement 支持项目；
- PPA / generation / grid investment 可能出现在完全不同主体的资产负债表。

因此：

> **Hyperscaler CapEx 是重要观察变量，但已经不是 AI infrastructure capital formation 的完整分母。**

这也是为什么 2026 年的新 compute-financing platform、PORTS-Pike LPS structure 与 Anchor Buyer long-duration contracts 必须单独进入资本分析。

完整融资结构见[第23章：AI 基础设施资本市场与融资结构](part-III-ch23-capital-financing.md)。

## 3. CapEx 的真正结构：不同久期资产被绑定到同一 AI workload

AI infrastructure 不是一次性的 server purchase，而是多个经济寿命完全不同的资产共同建设：

- **accelerator / server**：技术迭代快，经济寿命相对短；
- **network / switching / cooling**：中周期；
- **data-center shell / mechanical systems**：长周期；
- **substation / transmission / grid connection**：更长周期；
- **PPA / generation projects**：可跨越十年以上；
- **future workload revenue**：不确定，取决于真实客户采用和 monetization。

因此，AI infrastructure 的核心资本风险不是简单“花钱太多”，而是：

> **短周期 compute asset 与长周期 infrastructure asset，是否能够被同一组未来 workload 长期、稳定、足额利用。**

这形成 **Duration Mismatch**。

如果模型能力快速进步、单位 compute cost 持续下降、hardware generation 加速更新，而 data center 与 power assets 仍具有十年以上寿命，资本回收就越来越依赖 utilization 与 workload growth，而不是依赖设备本身保值。

---

## 4. Seller 与 Buyer 的资本作用不同

NVIDIA、memory supplier、foundry 与 hyperscaler 都在“增加资本投入”，但它们的资本再生产对象并不相同。

### System-platform seller

现金流更直接用于：

- inventory；
- capacity reservation；
- supply commitments；
- next-generation roadmap；
- ecosystem / software；
- system integration。

其核心目标是提高下一代 scarce-resource access 与 system delivery certainty。

### Hyperscaler / Anchor Buyer

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

因此，比较“谁投得更多”意义有限。更有价值的问题是：

> **每一美元资本能否提高 productive utilization、降低单位 workload 成本，并改善下一代资源获取能力。**

---

## 5. Power 正把资本周期从 Semiconductor Clock 拉长到 Infrastructure Clock

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

因此，AI infrastructure 同时运行两套时钟：

1. **Semiconductor Clock**：芯片、HBM、packaging 快速迭代；
2. **Infrastructure Clock**：电网、建筑、电源项目建设周期更长。

当 chip supply 缓解但 energized capacity 仍不足时，bottleneck 会从 manufacturing 转向 Time-to-Power。

这意味着产业扩张速度越来越不由单一芯片供应决定。

---

## 6. 超级周期是否可持续，最终取决于 Utilization 与 Monetization

高 CapEx 可以有两种完全不同的含义。

### 情形 A：高回报扩张

如果以下变量同步增长：

- deployed compute utilization；
- token / workflow volume；
- enterprise adoption；
- revenue per deployed compute；
- customer commitments；
- verified workflow output；

那么大规模 CapEx 可以持续形成规模优势、供应优势与进入壁垒。

### 情形 B：Overbuild

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

---

## 7. 五类领先清算信号

判断 Capital Hard Landing，应持续观察五类变量，但确认 S4 不要求 five-of-five 同时满足；关键是多类因果独立信号跨主体/层级形成广泛、持续的 cross-confirmation。

### Accounting

- impairment；
- accelerated depreciation；
- write-down；
- asset-life assumption change。

### Utilization / Revenue

- deployed compute utilization；
- AI revenue；
- cost per verified workflow；
- revenue per unit of deployed infrastructure。

### Market Clearing

- used-system price；
- cloud discount；
- lease rate；
- delivery lead time；
- inventory。

### Forward Commitment

- CapEx guidance；
- supply commitments；
- compute contracts；
- power contracts；
- Anchor Buyer commitments。

### Demand Quality / Financing

- customer cash generation；
- third-party capital 的 risk premium 与 commitment 变化；
- supplier equity / credit support 占比；
- refinancing dependency。

只有多类因果独立信号广泛、持续恶化，并具备 cross-actor / cross-layer breadth，才足以把“ROI pressure”升级为 **S4 — Capital Hard Landing**。Accounting 是 confirmation / severity evidence，不是 mandatory gate。

单一模型降价、股价调整、某一家公司 CapEx 下降，均不足以独立证明全行业进入资本清算。

---

## 8. 资本周期的一个关键二阶效应：投资规模本身会提高未来业绩门槛

AI 基础设施的特殊之处在于：资本扩张越成功，下一阶段的业绩门槛反而越高。

原因是：

> **更大的 installed capital base → 更高折旧与 operating cost → 更高 required utilization → 更高 monetization requirement**

这意味着即使 AI demand 继续增长，只要增长速度低于资本基数增长速度，单位资本回报仍可能下降。

所以未来最值得追踪的不是“AI 需求是否增长”，而是：

> **AI demand growth 是否足以覆盖 AI capital-base growth。**

这一差额决定资本周期是继续扩张、趋于正常化，还是进入清算。

---

## 9. 当前判断

截至 2026 年 8 月，公开数据仍更支持：

> **AI infrastructure CapEx supercycle continues, while the hurdle rate for utilization and monetization is rising.**

也就是说：

- 资本扩张仍然真实；
- 供给与基础设施建设仍在推进；
- 但资本基数增大正在提高对 utilization、workflow revenue 与长期 demand visibility 的要求。

这还不是已经确认的全行业 Capital Hard Landing。

真正的转折需要看到：**utilization/revenue、market clearing、forward commitments、demand-financing quality 与 accounting 中的多类独立信号跨主体/层级形成广泛、持续的交叉确认；Accounting 出现时强化严重度，但不是必要条件。**

## 10. 什么事实会迫使本章改判

应下调“资本扩张仍是主线”的判断，如果持续出现：

- hyperscaler underlying investment expectation 连续下降；
- data-center / power project cancellation 或 deferral 明显增加；
- seller supply commitments 收缩；
- third-party infrastructure capital risk appetite 下降；
- utilization 与 monetization 弱于新增资本；
- financing cost / refinancing pressure 明显上升。

单家公司 accounting reclassification 或单季 CapEx 波动，不足以证明超级周期已经结束。

## References

[^1]: Microsoft, FY26 Q4 earnings / conference call, calendar-2026 reported CapEx expectation, https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast
[^2]: Alphabet, Q2 2026 earnings-call full-year CapEx guidance **US$195–205B**, company guidance reported by Reuters, 2026-07-22, https://www.reuters.com/business/google-quarterly-cloud-revenue-growth-beats-expectations-2026-07-22/ ; Alphabet SEC Exhibit 99.1 separately supports Q2 actual results, https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
[^3]: Meta Platforms, 2026 Q2 SEC Exhibit 99.1, FY2026 CapEx guidance including finance-lease principal, https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm
[^4]: Amazon.com, 2026 Q2 Form 10-Q, TTM purchases of property and equipment, net of proceeds and incentives, https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
