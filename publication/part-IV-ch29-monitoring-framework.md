# Part IV · 第29章：Monitoring Framework——State Variables、Inflection Tests 与 Scenario Reweighting

## 1. 只监测真正能够改变判断的 State Variables

长期判断只有在后续事实能够迫使它改变时才有研究价值。

因此，本章监测的是 **state variables、transition rate 与 evidence quality，而不是新闻数量**。每一个新观察必须回答三个问题：

1. **Fact layer 到底发生了什么变化？**
2. **它改变了哪一个 mechanism variable？**
3. **这种变化是否足够 material、persistent，并足以 reweight S1–S4？**

这是 structured research-update process，不是自动交易模型。Dashboard 的作用，是防止一条 headline、一次 forecast revision 或一次 accounting event 被误读为 structural regime change。

## 2. Dashboard A — Seller Economics / Forward Reservation

### NVIDIA 当前锚

**Table 29.1 — NVIDIA seller economics 与 forward-reservation 基线**

| 指标 | 当前公开值 |
|---|---:|
| FY26 Revenue | US$215.938B |
| FY26 Data Center | US$193.737B |
| FY26 NVIDIA-defined non-GAAP FCF | US$96.575B |
| FY27 Q2 Revenue | US$96.221B |
| FY27 Q2 Data Center | US$89.0B |
| FY27 Q2 GAAP gross margin | 75.0% |
| FY27 Q2 GAAP operating income | US$63.734B |
| Rubin | full production |

**Source:** NVIDIA FY26 results、FY27 Q2 results 与 FY27 Q2 Form 10-Q.[^1][^2]  
**Note:** company-defined non-GAAP FCF 与 GAAP metrics 必须保留各自口径；commitments 为 aggregate amount，未披露 supplier-level split。

Supply / capacity commitments：[^2]

- 2026-01-25：US$95.2B；
- 2026-04-26：US$119B；
- 2026-07-26：US$279B。

这组指标回答：system seller 是否仍拥有足够 cash generation 与 forward commitment ability 预订下一代 scarce resources。

US$279B 不具有 supplier-level split，不能拆成 TSMC / HBM vendor revenue。[^2]

## 3. Dashboard B — Foundry / Packaging

### TSMC 2025

以下基线来自 TSMC 2025 Annual Report。[^3]

- 12-inch-equivalent wafer shipments：~15.0M；
- annual capacity：>17M；
- 3 nm / 5 nm / 7 nm wafer revenue：24% / 36% / 14%；
- ≤7 nm：74%；
- HPC platform：58%，YoY +48%；
- smartphone platform：29%，YoY +11%；
- largest / second-largest annual customer：19% / 17% revenue。

另一匿名客户表才支持 2024→2025：Customer A 12%→19%，Customer B 22%→17%。[^7] 两套披露不能拼成同一客户轨迹。

### Packaging

A-grade signal：TSMC 持续描述 packaging capacity tight / growth-limiting。[^8]

B-grade signal：TrendForce 估计 NVIDIA 占 2025 CoWoS demand >60%。[^9]

TSMC 未披露 customer-level CoWoS allocation。

## 4. Dashboard C — Memory

### A-grade manufacturing anchor

Micron：HBM3E same-node / same-bits ≈ **3× DDR5 wafer supply**；FY25 10-K 进一步确认 HBM 需要更多 wafers / cleanroom space。[^5]

### B-grade forward structure

TrendForce：**2026E HBM + RDIMM ≈51% of DRAM bit supply**。[^4]

### Vendor economics

SK hynix FY25：Revenue KRW97.1467T、Operating profit KRW47.2063T、Operating margin 49%、Net income KRW42.9479T；HBM revenue more than doubled YoY。[^6]

这组指标用于判断 HBM product mix 是否继续吸收 DRAM manufacturing input，以及 conventional DRAM residual capacity 是否松动。

## 5. Dashboard D — Capital Formation

Microsoft、Amazon、Alphabet、Meta 必须逐家公司保存：

- accounting line item；
- fiscal / calendar window；
- actual vs guidance / expectation；
- finance-lease treatment；
- AI/data-center specific disclosure。

监测重点不是“总额创新高”本身，而是新增 capital 是否继续流向 server、network、memory、custom silicon、data center 与 power。

不同口径不得机械相加成 official AI hardware CapEx。

## 6. Dashboard E — Power Delivery State

**Table 29.2 — Power / LPS delivery state machine**

| 状态 | 解释 |
|---|---|
| Announced | 项目或目标公布 |
| Contracted / Secured | 合同成立，或 land / power / shell 等资源已被锁定 |
| Permitted | 关键许可获得 |
| Construction / Transition | 基础设施建设、重启或转换实际推进 |
| Energized | 已具备实际送电条件 |
| Utilized | 已形成真实、可持续 workload |

**Source:** 本报告 power / LPS state framework。  
**Note:** state machine 用于防止把公开的 MW/GW 容量、secured IT-GW、contract quantity 或 project target 写成 active AI load。Generation MW/GW、PPA capacity 与 IT-GW 必须保持各自物理身份。

当前代表性项目：

- Microsoft / Constellation：~835 MW restart PPA；[^10]
- Talen / AWS：up to 1,920 MW revised PPA；April-2026 transition status 不能写成 full physical delivery complete；[^11]
- Google / Kairos：Hermes 2 up to 50 MWe in 2030，fleet up to 500 MWe by 2035；[^12]
- PORTS-Pike / NVIDIA / SB Energy / OpenAI：initial 4.25 IT-GW design capacity，属于 secured LPS / future phased buildout，计划从 2028 年开始分阶段上线。[^13]

真正需要更新的是：每个项目从 secured / contracted 向 construction、energized、utilized 的实际转换速度，而不是公布容量本身。

## 7. Dashboard F — Second-Stack Substitution

对 Google / AWS / Microsoft / Meta，分别跟踪：

- production workload share；
- external availability；
- compiler/runtime maturity；
- large-cluster scaling；
- migration cost；
- utilization；
- system TCO。

单颗 chip benchmark 不是充分替代指标。

## 8. Dashboard G — China Closure Tests

这里不再用一个“国产化率”概括，而是分别跟踪两个层级。

### Production-Grade Parallel Stack

跟踪：

- accelerator / compute delivery；
- HBM-class 或等价 memory subsystem；
- advanced packaging / integration；
- high-speed interconnect；
- compiler/runtime；
- production workload；
- utilization、reliability 与 economics。

### Autonomous Frontier Closure

然后另行跟踪：

- advanced-manufacturing continuity；
- equipment / materials / software / service；
- cross-generation process upgrades；
- HBM / packaging / LPS / power continuity；
- long-duration capital 与 multi-generation scaling。

Production deployment 可以强化第一层判断，但不能据此证明第二层已经闭合。

## 9. Dashboard H — Regulatory State

法律状态机统一记录：

> inquiry / RFI → investigation → Statement of Objections / formal complaint → formal proceeding → final decision → remedy / fine

禁止：

- inquiry → “已经起诉”；
- statutory ceiling → “即将罚款”；
- merger review → “已经认定垄断”。

真正改变 scenario 的变量是 interface openness、tying restriction、access / supply remedy 与 structural change。

## 10. Dashboard I — Capital Clearing / Demand Quality

### Accounting

impairment、inventory write-down、accelerated depreciation、asset disposal。

### Utilization / Revenue

compute utilization、AI workflow revenue、revenue per deployed compute。

### Market Clearing

used-system price、cloud discount、lease rate、delivery lead time。

### Forward Commitment

CapEx guidance、seller commitments、Anchor Buyer contracts、power contracts。

### Demand Quality / Financing

customer cash generation、third-party capital risk-taking、supplier equity / credit enhancement、refinancing dependency、asset transferability。

只有**多类因果独立的信号族**跨主体/层级形成广泛、持续且相互印证的恶化，S4 才从 stress test 升级为主情景。五类信号是 monitoring families，不是“五项必须全部满足”的硬门槛；Accounting 是 confirmation / severity evidence，不是 prerequisite。

## 10A. Dashboard J — End-System Residual Pressure

如果报告的主问题是“重要整机还能不能按自己的产品节奏拿到资源”，监测系统就不能只看 seller economics、HBM、packaging 与 power。

**Table 29.3 — End-system residual-pressure monitoring panel**

| 整机 / 系统 | 主要公开代理 | 需要回答的问题 | 禁止直接推出 |
|---|---|---|---|
| Smartphone / PC | memory contract price、system ASP、allocation fulfillment、configuration change、replacement cycle | 同价位规格是否变慢；quantity assurance 是否分化 | AI 导致全部涨幅；某品牌少拿确定 wafer 数量 |
| Game console | memory procurement、hardware unit plan、promotion、hardware margin、memory/storage BOM、generation cadence | memory / storage pressure 是否改变销量、促销、SKU 与多年 cost-down | 主机直接抢 HBM；下一代一定涨价/延期 |
| Automotive / industrial | mature-memory price、EOL、lead time、qualified alternates、product-longevity commitment | 长认证 / 长寿命是否把供应压力放大成 redesign / continuity risk | 汽车器件与 AI GPU 属同一物理池 |
| Robotics / Physical AI | industrial-electronics lead time + edge accelerator / memory availability | industrial 与 AI-edge 两类约束是否同时出现 | 每台机器人都需要 frontier HBM |
| High-reliability / aerospace / space | trusted access、EOL、qualification capacity、special-process continuity | 小批量、长寿命、特殊工艺供应经济性是否恶化 | AI 已造成某项目确定延期 / 涨幅 |

**Source:** 第3章分层暴露框架、第21章整机传导与 Sony / TrendForce game-console evidence。[^14][^15]  
**Note:** end-system dashboard 的作用不是把所有终端变成同一 shortage index，而是分开观察 **shared-resource exposure、buyer power、qualification rigidity 与 quantity assurance**。只有当上游资源证据和下游结果证据能够沿同一 transmission chain 对上，才升级 AI-era attribution。

### 代表性一手锚：Game Console

Sony FY2025 Q4 / FY2026 outlook 已明确把 PS5 FY26 hardware sales 与可按合理价格获得的 memory volume 联系，并表示可以通过 unit sales / promotional plans 调整 hardware profitability。[^14]

这使 game console 成为当前最干净的 end-system monitoring anchor 之一：

> **memory procurement → hardware volume / promotion → profitability**

TrendForce 对 2026 console shipment / memory-BOM 的估计只能作为 B 级数量范围，不能覆盖 Sony 一手口径。[^15]

### Dashboard J 的更新方向

**Residual pressure 强化：**

- memory / storage / component contract price 上升；
- allocation fulfillment 下降；
- promotion / configuration / SKU 被迫调整；
- long-life part EOL / lead-time 风险增加；
- end-system vendor 明确把采购数量、价格或 supply assurance 与硬件节奏联系起来。

**Residual pressure 减弱：**

- allocation fulfillment 改善；
- contract price / lead time 持续回落；
- same-price configuration 恢复提升；
- long-life supply continuity 改善；
- supplier product mix 更均衡；
- second-source qualification 扩大。

这个 Dashboard 不独立决定 S1–S4，但可以检验：

> **上游 scarcity / concentration 是否真的传导成整机世界的 upgrade tax 与 supply-assurance pressure。**

## 11. Evidence-Weighting Rules

**Table 29.4 — 更新时的默认 evidence grade**

| 数据类型 | 默认等级 |
|---|---|
| company filing / official product / government / court / formal contract | A |
| institutional research | B |
| sell-side / supply-chain / media estimate | C |
| report-side calculation / sensitivity / scenario input | D |

**Source:** 本报告证据方法（见第27章）。  
**Note:** 默认等级可因来源质量上调或下调，但不能因重复引用自动升级。

任何更新都必须保持原始等级；数字更新不等于证据等级自动提升。

## 12. Scenario-Reweighting Rules

### 向 S1 移动

system substitution 扩大、migration cost 下降、HBM/packaging/power 供给弹性改善、multi-buyer resource access 增强。

### 向 S3 移动

seller commitments 继续扩大、多层 scarcity 持续、switching cost 上升、powered capacity 被少数 anchor buyers 长期锁定。

### 向 S4 移动

utilization / revenue、market clearing、forward commitments、demand-financing quality 与 accounting 等多类独立信号形成 cross-confirmation，并具备足够 causal breadth；Accounting 出现时强化严重度，但不是必要条件。

### 留在 S2

dominant platform economics 强，但 alternative stacks 继续发展；scarce layers 仍紧但持续扩产；CapEx 高且 ROI 仍可支撑。

## 12A. Materiality 与 Persistence 必须服从各变量的 Clock

本报告不对所有变量套用统一的“两季度”或“三个月”规则。

那会制造 false precision，因为 semiconductor allocation、memory pricing、power project、regulatory proceeding、customer contract 与 accounting loss 运行在不同时间尺度上。

每一个 monitoring variable 都应明确：

1. **source cadence** — quarterly filing、monthly pricing series、event-driven contract、annual capacity disclosure 等；
2. **physical / economic clock** — hardware、fab、data center、grid、contract 或 accounting；
3. **comparable baseline** — 相同 denominator、unit 与 evidence identity；
4. **materiality** — 变化必须足以改变相关 mechanism，而不是只制造 headline volatility；
5. **persistence / confirmation** — 由适合该变量时钟的可比后续证据确认；
6. **cross-signal confirmation** — 尤其是 S4，单一弱指标不足以改判。

**Mechanism-break override：** breadth requirement 约束的是**系统级 scenario classification**，不是给底层 mechanism 提供“必须等多信号才承认反例”的保护。如果一条高质量 observation 在相同 denominator 与 time identity 下直接击穿某个 mechanism 的必要前提，该 mechanism 必须立即降级、重写或废弃，即使此时尚未形成 cross-signal breadth。breadth 决定的是整个 S1–S4 state 是否改变，不能被用来忽略已经失效的前提。

### Handling missing data

如果某一层没有 same-unit 的 `AI_Effective_Demand` 与 `AI_Effective_Capacity`，其 Absolute AI Capacity Gap 必须标记为 **not measurable from public data**。

Growth Gap、lead time、pricing 与 allocation fulfillment 可以作为 proxy 跟踪，但不能被重新命名为 absolute capacity gap。

### Scenario reweighting

- **Toward S1：** supply elasticity、system substitution、buyer optionality 与 portability 以互相强化的方式改善；
- **Toward S3：** multi-layer scarcity、switching cost、quantity-assurance concentration 与 forward reservation 同时强化；
- **Toward S4：** 多个因果独立 signal families 跨主体/层级广泛、持续恶化；至少包含一个 real-economy / market / commitment signal，Accounting 是 confirmation channel 而不是 mandatory gate；
- **Otherwise：** 保持 S2 baseline，或只做局部 weighting adjustment，不因为单一 headline 改变主情景。

## 12B. 五个 Headline Inflection Tests

为了让读者快速判断长期结构是否正在改变，可以把前述 Dashboard A–J 压缩成五个 headline tests。它们不是新的模型，也不是统一数值阈值，而是对现有监测框架的读者版摘要。

1. **Non-AI Residual Capacity / Quantity Assurance 是否持续改善或恶化。**  
   重点看 smartphone、PC、game console、automotive / industrial 等终端的 contract price、allocation fulfillment、lead time、configuration、promotion 与 qualified alternate，而不是只看全球总 wafer / memory capacity。

2. **第二套 System Stack 是否跨过真实 production-workload 门槛。**  
   重点看 Google / AWS / Microsoft / Meta custom systems 的 production workload share、external availability、migration cost、utilization 与 system TCO。单颗 accelerator benchmark 或一次发布不能证明系统级替代已经成立。

3. **China Parallel Stack 是否同时改善 production-grade economics 与 autonomous closure。**  
   既要看真实 workload、单位经济、software/runtime 与 cluster utilization，也要继续看 advanced logic、HBM-class memory、advanced packaging、equipment / materials / service continuity。可用系统与自主跨代闭环必须继续分开判断。

4. **资本基数是否被 utilization、monetization 与独立融资能力覆盖。**  
   重点看 revenue / utilization、used-system / lease clearing、forward commitments、customer cash generation、third-party risk capital、supplier support 与 refinancing dependency。技术资产寿命短于融资久期时，duration mismatch 会明显放大 S4 风险。

5. **Power / LPS 是否真正从 secured 走到 energized / utilized。**  
   重点不是 headline GW，而是项目从 Contracted / Secured → Permitted → Construction / Transition → Energized → Utilized 的实际转换速度，以及 Time-to-Power 是否持续造成交付差异。

这五项都不使用人为统一的“8 个季度”“30%–40%”之类硬阈值。只有在**同口径连续观察 + 两个以上独立机制维度互相印证**时，才足以推动 S1–S4 的实质重权重。

## 13. Evidence-Update Protocol

任何单一新闻都不应触发整份报告的重新分类。

只有当新事实改变了核心机制变量，并得到足够独立证据支持，才修改 scenario weighting。

这使报告能够长期更新，而不是在每次产品发布、股价波动或传闻后重新判定整个产业状态。

## References

[^1]: NVIDIA, FY26 and FY27 Q2 official results, seller economics and Rubin status, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026 ; https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^2]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^3]: TSMC, 2025 Annual Report, https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^4]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^5]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E wafer-supply trade ratio, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf ; Micron Technology, FY25 Form 10-K, HBM requires more wafers / cleanroom space for the same bits at the same technology node, https://www.sec.gov/Archives/edgar/data/723125/000072312525000028/mu-20250828.htm
[^6]: SK hynix, FY25 Financial Results, https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
[^7]: TSMC, 2025 Consolidated Report, anonymized Customer A/B revenue series, https://www.sec.gov/Archives/edgar/data/1046179/000104617926000024/a2025q4consolidatedreport-.htm
[^8]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging tightness limiting customer growth, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^9]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^10]: Constellation, Crane Clean Energy Center / Microsoft 20-year PPA and approximately 835 MW unit, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
[^11]: Talen Energy, 2026 Q2 Form 10-Q and 2025 Form 10-K, revised AWS PPA state and ramp, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm ; https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
[^12]: Kairos Power / Google partnership, Hermes 2 up to 50 MWe in 2030 and fleet up to 500 MWe by 2035, https://www.kairospower.com/google

[^13]: NVIDIA, PORTS-Pike Technology Campus / SB Energy / OpenAI, 2026-08-17, initial 4.25 IT-GW design capacity and phased online plan beginning in 2028, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx


[^14]: Sony Group, FY2025 Q4 earnings speech / FY2026 outlook, PS5 hardware-sales / promotion management tied to memory procurement at reasonable prices, https://www.sony.com/en/SonyInfo/IR/library/presen/er/pdf/25q4_sonyspeech.pdf
[^15]: TrendForce, 2025-12-02, 2026 game-console shipment forecast and estimated console memory-cost share of BOM, B-grade institutional forecast, https://www.trendforce.com/presscenter/news/20251202-12811.html
