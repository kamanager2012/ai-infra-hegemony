# P0-1 · Chapter 24 五类资本清算信号历史回测 v0.9

> **状态：Research-side validation，非正式正文。**  
> 目的：检验 Chapter 24 的五类信号能否区分“系统性资本清算”“局部行业清算”和“强烈库存调整但未进入系统性 S4”。  
> 本版本不修改 Chapter 24，也不把回测结果升级为正式预测阈值。

## 1. 回测对象

Chapter 24 的五类信号：

1. **Accounting** — impairment / inventory write-down / accelerated depreciation / asset disposal；
2. **Utilization / Revenue** — 已部署资产利用率、收入、monetization 是否弱于资产扩张；
3. **Market Clearing** — 库存、二手/渠道价格、折扣、交期、resale liquidity 是否转松；
4. **Forward Commitment** — CapEx guidance、订单、供给承诺、长期容量/项目承诺是否削减、延期或取消；
5. **Demand Quality / Financing** — 客户现金流、融资可得性、supplier support、refinancing dependency、第三方风险资本意愿。

## 2. 预注册式回测规则

为降低 hindsight bias，本回测采用以下规则：

- **只使用当时或随后正式披露、但描述当期状态的资料**，不以“后来确实崩了”反推当时信号；
- 每类信号独立判定，不允许用股价下跌替代产业信号；
- 不要求五类信号同季出现，因为 accounting、市场清算、资本承诺具有不同披露时钟；
- 必须保留反证。若一个大子市场仍扩张，不能因为另一子市场库存崩塌就判定整个系统进入 S4；
- **不在 v0.1 优化权重或阈值**。本轮只检验方向、一致性、提前量和误报；
- “不可观测 / 不适用”必须记为 N/A，不能为了凑满五类强行映射。

### 2.1 研究侧 ordinal score

仅用于跨案例比较，不是 Chapter 24 的正式触发阈值：

- **0**：无恶化或存在明显反证；
- **1**：出现至少一项可信恶化证据，但持续性/广度不足；
- **2**：出现正式确认、重复恶化或多条相互独立证据；
- **N/A**：该历史案例无法可靠观测该类变量。

研究侧判定：

- **Broad clearing**：至少 4 类信号恶化，且 Accounting / Utilization / Forward Commitment 至少两类达到 2；
- **Partial clearing**：2–3 类明显恶化，或只集中在单一子市场；
- **No systemic clearing**：信号明显分化，关键需求/利用率或未来承诺仍有强反证。

这只是防止事后自由解释的校准工具；阈值本身仍为 D 级，必须经过更多历史样本与未来 prospective runs 才能升级。

### 2.2 Proxy hierarchy：每类信号先看什么

为避免未来每次遇到数据缺口就临时换指标，固定如下 proxy hierarchy。后续案例必须优先使用更高层级；只有高层级不可得时才下沉。

| Signal | Tier 1：优先证据 | Tier 2：次级证据 | Tier 3：仅作辅助 |
|---|---|---|---|
| Accounting | 10-K/10-Q/年报中的 impairment、inventory provision、write-down、asset disposal、accelerated depreciation | 公司正式 earnings materials / CFO commentary | 媒体转述、分析师估计 |
| Utilization / Revenue | 公司披露的 utilization、segment revenue、revenue per deployed asset、已部署容量 monetization | 出货/订单/usage 的机构统计 | 单一渠道调查、股价 |
| Market Clearing | 官方/公司披露的 channel inventory、pricing program、lead time、resale/lease clearing | 高质量行业价格与库存数据库 | 二手平台零散报价 |
| Forward Commitment | CapEx guidance、采购/供给承诺、合同容量、项目延期/取消的一手披露 | 监管文件、项目融资文件、机构汇总 | 市场传闻 |
| Demand Quality / Financing | 客户现金流、债务/信用条件、正式融资、supplier credit/equity support、refinancing | Fed/央行/监管信用环境与高质量机构融资数据 | 估值、风险偏好等间接代理 |

**硬规则：**
- 股价、估值和媒体情绪不能独立把任何一类信号从 0 提升到 2；
- 同一公司同一份披露里的多句话，原则上仍算**一个证据源**，不能伪装成多源确认；
- “价格下降”若来自技术代际进步而非库存/利用率失衡，不能直接记作 Market Clearing 恶化；
- “CapEx 下调”若同时明确说明只是项目时点迁移、架构切换或非目标资产削减，最多记 1，除非后续出现取消/重谈/利用率同步恶化。

### 2.3 Segment breadth：防止局部清算误报系统性 S4

每个案例除五类信号外，再记录一个不计入 10 分总分的 **Segment Breadth**：

- **Narrow**：主要集中在单一需求源、产品代际或一个下游；
- **Multi-segment**：至少两个关键子市场同步恶化；
- **System-wide**：上游供给、核心买方、资本承诺和融资条件跨层同步恶化。

若 Segment Breadth = Narrow，即使可观测信号全部为 2，也不得直接标记 system-wide S4。

### 2.4 Lead / lag 记录规则

后续每个案例都记录三个时间点：

1. **First deterioration date**：首次出现可信、当时可观察的恶化；
2. **Cross-confirmation date**：至少三个不同信号类别开始相互印证；
3. **Accounting confirmation date**：正式 write-down / impairment / annual-statistical confirmation 出现。

由此计算：

- Market Clearing 相对 Accounting 的领先期；
- Forward Commitment 相对 Accounting 的领先/滞后期；
- 从首次恶化到跨信号确认需要多久。

历史资料无法精确到月时，只记录 quarter / half-year，不伪造精度。

### 2.5 False-positive constraint

任何候选 S4 必须主动搜索至少一条反证：

- 核心 segment revenue / utilization 仍扩张；
- forward commitment 只是延期而非取消；
- 资本开支从 legacy/non-AI 资产迁移到新架构，而非总需求崩塌；
- inventory clearing 由产品换代而非终端需求断裂解释；
- financing tightening 尚未传导到实际项目取消。

若存在强反证，必须在表格中显式记录，不能只放进脚注。

---

# 3. Case A — 2000–2002 Internet / Telecom Capital Bust

## 3.1 已知结局，但回测不使用结局作输入

1999–2000 年通信基础设施和网络设备投资高速扩张，2001 年进入急剧资本清算。Federal Reserve 后来汇总的当期数据表明：美国 communications equipment 实际支出从 1998–2000 年平均每年增长超过 20%，转为 **2001 年下降超过 30%**。

这是一组适合检验五信号系统的“系统性资本清算”正样本。

## 3.2 信号回放

| Signal | 当期可观测证据 | v0.1 |
|---|---|---:|
| Accounting | Cisco FY2001 对库存及采购承诺计提 **US$2.77B** provision；另有约 **US$1.17B** restructuring / impairment / excess-facility charges | 2 |
| Utilization / Revenue | Cisco 2001-04-16 预计 fiscal Q3 revenue 较 Q2 **环比下降约 30%**；Fed 记录 communications-equipment investment 在 2001 年下降超过 30% | 2 |
| Market Clearing | 2001-03 Beige Book 已报告 telecom-equipment inventories high；Cisco FY2001 inventory turns 从上一年 Q4 的 7.8 降至 4.1，库存反映需求下滑与长交期采购错配 | 2 |
| Forward Commitment | Cisco 2001-03 已判断 capital-spending slowdown 可能持续超过两个季度；行业公司披露 carriers 大幅放缓网络部署与资本开支；Fed 2001 年末仍记录 telecom/high-tech orders 与 capex plans 疲弱 | 2 |
| Demand Quality / Financing | 2001 telecom filings明确提到 constrained capital markets、high debt、carrier bankruptcies、融资困难与 excess network capacity 共同压低资本开支 | 2 |

**研究侧结果：10/10，Broad clearing。**

## 3.3 时间顺序

- **2000 Q4**：Fed 已观察到高科技投资增速突然减速，但 telecom equipment 仍未全面转负；
- **2001-03**：高 telecom inventories + 企业削减资本开支 + Cisco 宣布成本削减；
- **2001-04**：Cisco 正式披露需求突然下滑、Q3 revenue 预计环比约 -30%；其 FY2001 年报随后确认 fiscal Q3 已记录约 **US$2.25B** excess-inventory charge，全年 inventory/purchase-commitment provision 共 **US$2.77B**；
- **2001 H2**：carrier 融资约束、过剩网络容量、破产和资本开支削减广泛出现；
- **2002 early**：Fed 确认 2001 communications equipment investment 已下降超过 30%，且 excess capacity 继续压制需求。

### 3.4 对 Chapter 24 的意义

这一案例支持 Chapter 24 的核心逻辑：

> **真正的资本清算不是“科技股跌了”，而是 Accounting + Utilization/Revenue + Market Clearing + Forward Commitment + Financing 同时从扩张转为收缩。**

更重要的是，部分领先信号在全年统计确认之前已经出现：inventory / orders / capex plans 先恶化，正式年度投资数据与部分 accounting recognition 随后确认。

---

# 4. Case B — 2018–2019 Cryptocurrency / GPU Channel Unwind

这是一个“真实清算，但范围明显小于 2001 telecom”的正样本，用来测试五信号是否会错误地把单一需求源崩塌升级为整个加速计算系统崩塌。

## 4.1 信号回放

| Signal | 当期可观测证据 | v0.1 |
|---|---|---:|
| Accounting | NVIDIA FY2019 Q3 因 crypto mining demand sharp fall-off 对 prior-architecture components/chips 计提约 **US$57M** charge；Q4 又有约 **US$128M** excess DRAM / component charges | 2 |
| Utilization / Revenue | FY2019 Q4 revenue **US$2.21B，环比 -31%**；Gaming revenue **US$954M，环比 -46%**；Data Center revenue **环比 -14%** | 2 |
| Market Clearing | NVIDIA 明确披露 post-crypto **excess channel inventory**，并降低 shipment、延后部分新产品 production ramp，让 Pascal mid-range inventory 在 1–2 个季度内消化 | 2 |
| Forward Commitment | 2019-01-28 公司把 Q4 revenue guidance 从 **US$2.70B 下调至 US$2.20B**；production ramp 延后，crypto-specific revenue 预计趋近 negligible | 2 |
| Demand Quality / Financing | crypto-linked demand 本身快速消失，但本案例缺少与 Chapter 24 当前定义完全同构的 customer-cash-flow / supplier-financing / refinancing 资料 | N/A |

**研究侧结果：8/8 observable points；但仅 4 类可可靠观测。判定为 Strong Partial Clearing，而不是完整五信号 Broad Clearing。**

## 4.2 关键反证

FY2019 全年 NVIDIA revenue 仍同比增长 21%，Data Center 全年增长 52%。因此，如果只看 Q4 Gaming 和 channel inventory，会把“crypto/Gaming 子市场清算”错误升级为整个 NVIDIA 平台或整个加速计算产业崩盘。

## 4.3 Timing tightening

Source-level timing now supports a narrower sequence:

- **2018 Aug (FY2019 Q2):** NVIDIA still reported record platform revenues; this is a strong contrary signal against dating systemic clearing too early;
- **2018 Nov (FY2019 Q3):** NVIDIA publicly identified **excess channel inventory post the cryptocurrency boom**;
- **2019 Jan 28:** Q4 revenue guidance was cut from US$2.70B to US$2.20B; NVIDIA said it had delayed planned production ramps to let channel inventory clear;
- **FY2019 Q3–Q4 reporting:** inventory / component charges confirmed the accounting impact;
- **2019 H1:** channel inventory was expected to normalize over roughly one to two quarters.

Research-side timing label:

| Timing field | Case B |
|---|---|
| First public deterioration | 2018 Q4 / Nov-2018 disclosure |
| Cross-confirmation | 2019 Jan |
| Accounting confirmation | FY2019 Q3–Q4 |
| Trough / stabilization | 2019 H1 |
| Confidence | Medium–High |

The August 2018 all-platform record quarter matters because it prevents backdating the clearing signal merely because crypto demand had already started falling.

### 4.4 对 Chapter 24 的意义

这一案例暴露出一个必须写进未来判定协议的限制：

> **五信号必须同时做“signal breadth”和“segment breadth”。单一需求来源造成的库存清算，即使 Accounting、Revenue、Market Clearing 和 Forward Commitment 都很强，也不自动等于系统级 S4。**

这比单纯增加第五个信号更重要。

---

# 5. Case C — 2022–2023 GPU / Channel Correction + Cloud Optimization

这是负对照：如果五信号系统把这一阶段判断成“AI infrastructure system-wide S4”，说明框架特异性不足。

## 5.1 信号回放

| Signal | 当期可观测证据 | v0.1 |
|---|---|---:|
| Accounting | NVIDIA FY2023 总计提 **US$2.17B inventory charges**，主要与 Ampere Gaming / Data Center excess supply 和 purchase obligations 有关 | 2 |
| Utilization / Revenue | Gaming FY2023 revenue **同比 -27%**，但 Data Center revenue **同比 +41%**；系统层信号明显分化 | 1 |
| Market Clearing | NVIDIA Q2 FY2023 Gaming revenue **环比 -44%**，公司实施 channel pricing programs、主动 undership，让渠道去库存 | 2 |
| Forward Commitment | Meta 先把 2023 CapEx 从 US$34–37B 下调至 US$30–33B，后再降至 US$27–30B；但明确说明部分是 non-AI server 节省和项目递延，随后又预计 2024 CapEx 回升并由 AI server / data-center investment 驱动 | 1 |
| Demand Quality / Financing | 没有出现与 2001 telecom 类似的广泛融资断裂；AI demand/commitment 反而在 2023 年重新增强 | 0 |

**研究侧结果：6/10，且关键类别存在强反证。判定为 Partial / Sector Clearing，不能判系统性 S4。**

## 5.2 为什么这个负对照重要

2022 年的 Accounting 和 Market Clearing 如果单独看非常“像崩盘”：

- 巨额 inventory provision；
- Gaming 销量急降；
- channel pricing；
- undershipping；
- 部分 cloud/data-center CapEx 下调。

但如果五信号要求跨类别、跨子市场互证：

- NVIDIA Data Center 仍在增长；
- Meta 对 AI capacity 的投入没有被取消，只是结构调整和时点移动；
- 2024 forward commitment 又重新上升；
- Demand Quality / Financing 没有出现系统性断裂。

因此该框架在这个负对照上**没有必然误报 S4**。

---

# 5A. Case D — 2008–2009 GFC / Enterprise IT（融资主导型系统清算）

这个案例此前保留在汇总表，但详细案例段落缺失。v0.7 将其恢复，因为它检验一个关键问题：

> **如果冲击首先从金融条件进入，是否必须等到卖方出现巨额 impairment 才能确认资本清算？**

答案是否定的。

Federal Reserve 当期材料显示：

- **2008 H1**：企业销售、利润与信用条件已经恶化，一些公司推迟或放弃资本扩张；
- **2008 Q4**：real equipment & software investment 年化下降约 **28%**；
- **2008 H2**：real IT investment 年化平均下降约 **12.5%**；
- **2009 Q1**：real equipment & software investment 再以约 **34% annualized** 下滑；
- 信用可得性对许多企业仍然偏紧，融资成本上升；
- Cisco FY2009 revenue **同比 -9%**，product revenue 约 **-12%**，主要受 enterprise / service-provider spending 减少影响。

但 Cisco 并没有出现 2001 telecom bust 那种同等级的巨额 inventory / asset impairment。

这使 Case D 成为一个重要反例：

> **真实的系统性资本清算可以由 Financing + Forward Commitment + Utilization/Revenue 主导，而 Accounting 保持弱或滞后。**

## 5A.1 信号回放

| Signal | 当期可观测证据 | v0.7 |
|---|---|---:|
| Accounting | 未观察到与 2001 telecom 同等级、可作为系统确认的 enterprise-IT seller write-down | 0 |
| Utilization / Revenue | 2008Q4 E&S 约 -28% annualized；2009Q1 约 -34%；2008H2 IT investment 约 -12.5% annualized；Cisco FY2009 revenue -9% | 2 |
| Market Clearing | broad business inventory liquidation 明显，但 enterprise-IT-specific resale / channel clearing 证据较弱 | 1 |
| Forward Commitment | 2008 年中已出现企业推迟/放弃 expansion；2008Q4–2009H1 investment collapse | 2 |
| Demand Quality / Financing | credit availability reduced / cost increased；2009H1 对许多 borrower 仍然 tight | 2 |

**研究侧结果：7/10，Segment Breadth = Broad / macro-systemic。判定为 Broad clearing。**

## 5A.2 Timing

- **First deterioration:** 2007 Q4–2008 H1 — sales / profits / credit conditions deteriorate，扩张计划开始推迟；
- **Cross-confirmation:** 2008 Q4 — investment、IT spending、credit 与企业需求同步恶化；
- **Accounting confirmation:** **No qualifying hard accounting confirmation** — 这是本案例的核心特征，而不是数据遗漏；
- **Trough / stabilization:** 2009 H1 trough；2009 H2 equipment/software 与 IT spending 开始恢复。

## 5A.3 对 Chapter 24 的意义

Case D 固定一条规则：

> **Accounting 是确认渠道之一，不是 S4 的硬门槛。**

如果：
- credit conditions 显著恶化；
- forward investment collapse；
- utilization/revenue 广泛下滑；
- segment breadth 足够广；

即使卖方没有出现巨额 impairment，资本清算仍然可以成立。

这也说明五信号不是“五票全中才算”。

真正需要的是：

> **不同 shock-entry path 下，多类独立信号形成足够广的 cross-confirmation。**

## 5.3 Timing tightening

Case C is useful because Accounting did **not** materially lag Market Clearing.

On **2022-08-08**, NVIDIA disclosed:
- total revenue approximately US$6.70B versus US$8.10B outlook;
- Gaming revenue -44% q/q;
- lower sell-in following reduced channel-partner sales;
- pricing programs with channel partners;
- approximately **US$1.32B** of inventory / related charges based on revised demand expectations.

The finalized Q2 FY2023 release on **2022-08-24** then said OEMs / channel partners would continue reducing inventory into Q3, while Data Center was expected to grow sequentially.

Research-side timing label:

| Timing field | Case C |
|---|---|
| First public deterioration | 2022 Aug 8 |
| Cross-confirmation | 2022 Aug 8–24, but only at segment level |
| Accounting confirmation | 2022 Aug — nearly synchronous with clearing |
| Trough / stabilization | 2022 H2–2023 H1; AI/Data Center side reversed earlier than Gaming |
| Confidence | High for first signal; Medium for trough |

This is an important counterexample to an overly simple timing rule:

> **Accounting often lags in long-duration capital cycles, but inventory-led clearing can produce accounting confirmation almost immediately.**

---

# 6. Case E — 2001–2003 Semiconductor Downcycle

这个案例与 Case A（Internet/Telecom）发生在同一大周期，因此**不能当作独立宏观事件重复计数**。它的价值是检验：当冲击进入半导体这一更靠上的物理层时，五信号是否仍能识别出 inventory、utilization、pricing 与 capacity commitment 的同步清算。

## 6.1 信号回放

| Signal | 当期可观测证据 | v0.3 |
|---|---|---:|
| Accounting | Micron 2001 年对 semiconductor-memory inventory 计提约 **US$727M** write-down，2002 年再计提约 **US$376M**；Intel 2001 年 flash-memory 业务也受到更高 inventory write-down 与 factory under-utilization 拖累 | 2 |
| Utilization / Revenue | 美国 semiconductor/electronic-component capacity utilization 从 2000-07 约 **93.2%** 降至 2001-11 约 **58.8%**；行业 2001 sales 同比下滑超过 30% | 2 |
| Market Clearing | Micron 2001 ASP 同比约 **-60%**、2002 再约 **-53%**；客户 inventory-reduction programs 与 excess manufacturing capacity 形成持续 pricing pressure | 2 |
| Forward Commitment | STMicroelectronics 披露因需求与利用率大幅下滑而关闭/选择性停产部分 wafer fabs；Fed 同期下修 semiconductor/computer manufacturers 的 capacity-growth estimate | 2 |
| Demand Quality / Financing | 本轮主要由 end-demand collapse、inventory correction 与 excess capacity 驱动；缺少与 2001 telecom 同等强度、可独立识别的 financing-stress 证据 | N/A |

**研究侧结果：8/8 observable points；四类实体信号均为 2。判定为 Broad semiconductor clearing。**

## 6.2 Timing

- **2000 H2**：semiconductor utilization 从高位开始下滑；
- **2001 H1**：利用率、订单、库存和 pricing 已出现跨信号恶化；
- **2001 H2**：利用率跌至约 60%，公司开始 plant closure / selective shutdown / inventory write-down；
- **2002**：行业 sales 低位徘徊，Micron ASP 再大幅下降并继续库存减值；
- **2003**：利用率逐步恢复到 70%–80% 区间，行业开始进入更清晰的复苏阶段。

因此本案例的信号顺序更接近：

> **Utilization / Market Clearing → Accounting / Capacity Retrenchment → Recovery**

而不是“Accounting 最先报警”。

## 6.3 对 Chapter 24 的意义

这一层回测强化三个结论：

1. **Market Clearing 与 Utilization 是半导体资本周期的重要领先/同步信号**；  
2. **Accounting 主要负责确认损失已经进入财务报表，不负责最早预警**；  
3. **Demand Quality / Financing 不是每次物理产业清算都必须可观测**。由 inventory / end-demand / excess capacity 驱动的行业清算，仍可能在没有显著融资断裂证据时成立。

### 6.4 样本相关性警告

Case A 与 Case E 共享 2000–2002 大周期和终端需求冲击。

所以后续如果计算“命中率”，必须：

- 把它们视为**一个宏观 episode 下的两个 layer observations**；
- 不能简单写成“两个独立历史危机都验证成功”；
- 需要继续增加不相关周期，才能提高外部有效性。

---

# 7. Case F — 2014–2016 Oil & Gas Upstream Capital Clearing

这个案例是当前样本中最重要的**跨行业独立资本周期**。它不是互联网、半导体或 GPU 周期，但具有与 AI infrastructure 高度可比的资本结构特征：

- 高前置 CapEx；
- 长资产久期；
- 项目经济性依赖利用率 / commodity price / cash flow；
- 大量外部融资；
- 资产残值与再融资在下行期迅速恶化。

因此它用于检验五信号框架是否具有跨行业资本周期的外部有效性，而不是只会解释科技行业。

## 7.1 信号回放

| Signal | 当期可观测证据 | v0.4 |
|---|---|---:|
| Accounting | Halliburton 2015 因能源市场下行记录约 **US$2.2B impairments and other charges**；Apache 2015 总 impairments 约 **US$9.47B**，主要来自油气资产与设施减值 | 2 |
| Utilization / Revenue | 美国 land rig count 从 2014-11 高点到 2015-12 下降约 **64%**；Halliburton 2015 revenue **同比 -28%**；2016 年美国平均 rig count 较 2014-11 峰值接近 **-75%** | 2 |
| Market Clearing | Halliburton 明确披露 services industry 出现 widespread pricing pressure；offshore drillers 同期披露 dayrate / utilization 下滑并触发 fleet impairment | 2 |
| Forward Commitment | EIA 记录美国 mining/exploration investment **2015 年下降约 35%**；ConocoPhillips 2015 CapEx 较 2014 **下降 41%**；Chevron/Exxon 等同步压低后续投资计划 | 2 |
| Demand Quality / Financing | EIA 记录低油价压缩 operating cash flow、企业削减 CapEx 并更多依赖 debt/equity；Fed SLOOS 显示银行收紧 oil & gas underwriting / credit lines，监管机构记录 oil & gas classified commitments 明显上升 | 2 |

**研究侧结果：10/10，Segment Breadth = Multi-segment / industry-wide，判定为 Broad clearing。**

## 7.2 Timing

- **2014 H2** — oil price 进入快速下跌，first deterioration 首先出现在 commodity clearing；
- **2014 Q4–2015 Q1** — rig count、service activity 与 CapEx plans 开始快速下修；
- **2015 Q2** — Fed SLOOS 已记录银行针对 oil & gas borrower 收紧 underwriting / credit lines，融资压力开始与产业活动相互印证；
- **2015 H2** — debt service / cash-flow pressure、service pricing、rig utilization、CapEx reductions 形成广泛 cross-confirmation；
- **2015–2016 financial reporting** — 大规模 impairments / idle-equipment write-downs 完成 accounting confirmation；
- **2016 Q2** — U.S. oil rig count 触及本轮低点后开始恢复，Halliburton 后续披露也将 2016 视为最深行业下行阶段并观察到复苏信号。

研究侧时间标签：

| Timing field | Case F |
|---|---|
| First deterioration | 2014 H2 |
| Cross-confirmation | 2015 H1–H2 |
| Accounting confirmation | 2015–2016 reporting cycle |
| Trough / stabilization | 2016 Q2–Q4 |

## 7.3 对 Chapter 24 的意义

这一案例给五信号体系增加了三个重要约束。

### A. 框架不应依赖“技术泡沫”叙事

这里没有 GPU 代际替换，也没有软件迁移问题。

真正发生的是：

> **price / cash flow collapse → utilization/activity decline → CapEx cuts → financing deterioration → impairment**

五信号仍然能够工作，说明它更接近一个资本清算框架，而不是某一轮科技泡沫的专用解释。

### B. Demand Quality / Financing 可以成为中段放大器

油气周期表明，融资通常不是最先发生的信号，但会把原始需求/价格冲击放大成：

- credit-line reduction；
- underwriting tightening；
- debt-service burden；
- distressed refinancing；
- 更快的 CapEx retrenchment。

这与 P0-4 Macro-Financial Transmission 的方向一致。

### C. 低价格既可以是 clearing signal，也可以成为后续复苏条件

价格暴跌在本轮首先摧毁 marginal project economics，但低成本、成本削减和资产清算随后又帮助供需重新平衡。

因此：

> **价格下降的含义必须结合 utilization、forward commitment 与 financing state 读取，不能机械等同于永久需求破坏。**

---

# 8. Case G — 2018–2019 Hyperscale Cloud CapEx Digestion（独立负对照）

这个案例用于测试一个常见误判：

> **某一家 hyperscaler 的 CapEx 从极高增速转为持平/下降，是否足以判定 cloud infrastructure 进入系统性清算？**

答案是否定的。

2018 年 Alphabet 的资本开支从 2017 年约 **US$13.2B** 快速上升到约 **US$25.1B**；2019 年回落到约 **US$23.5B**。如果只看这一条 Forward Commitment，很容易把“高增速后的 digestion”误读成需求崩塌。

但同期跨公司数据给出强反证：

- Amazon AWS 2019 revenue **同比 +37%**，从 US$25.7B 增至 US$35.0B；
- AWS net additions to property and equipment 从 2018 年约 **US$9.8B** 升至 2019 年约 **US$13.1B**；
- Facebook 2019 CapEx 从 2018 年约 **US$13.9B** 升至约 **US$15.1B**，并预计 2020 年进一步达到 **US$17–19B**；
- Google Cloud revenue 从 2018 年约 **US$5.84B** 增至 2019 年约 **US$8.92B**。

因此，单一公司的 CapEx digestion 没有跨越到 Accounting、Utilization/Revenue、Market Clearing、Demand Quality/Financing 的同步恶化。

## 8.1 信号回放

| Signal | 当期可观测证据 | v0.5 |
|---|---|---:|
| Accounting | 未见与 cloud-capacity overbuild 对应的大规模 impairment / write-down | 0 |
| Utilization / Revenue | AWS revenue +37%；Google Cloud revenue 继续高速增长 | 0 |
| Market Clearing | 未见跨 hyperscaler 的 channel/inventory/resale clearing 证据 | 0 |
| Forward Commitment | Alphabet CapEx 2019 较 2018 小幅回落，但 AWS asset additions 与 Facebook CapEx 继续增加 | 1 |
| Demand Quality / Financing | hyperscaler operating cash flow 仍强，未见融资断裂传导 | 0 |

**研究侧结果：1/10，Segment Breadth = Narrow / company-specific。判定为 No systemic clearing。**

## 8.2 对 Chapter 24 的意义

这个负对照把一条规则变得更硬：

> **Forward Commitment 的单点恶化不能脱离 cross-company breadth 和 revenue/utilization 读取。**

尤其在高增速资本周期里：

- CapEx 从“翻倍”降到“持平”；
- 某家公司调整建设时点；
- 某个平台把资本从一种资产迁移到另一种资产；

都可能只是 **digestion / mix shift / timing normalization**，而不是 S4。

因此：

> **CapEx growth deceleration ≠ CapEx contraction ≠ system-wide clearing。**

---

# 9. Case H — 2011–2013 Solar PV Manufacturing Overcapacity（独立资本清算）

这个案例用于测试五信号是否只在 IT / GPU / oil & gas 中有效，还是能识别另一种典型的高 CapEx 制造周期：

> **政策驱动需求 + 大规模上游扩产 → 产能过剩 → 价格清算 → 利用率下降 → 产能重组 / impairment → 融资压力。**

公开材料显示：

- 2011–2012 solar industry 出现明显 excess manufacturing capacity，module / wafer / polysilicon price 持续下跌；
- Suntech 2012 investor material 显示 cell capacity utilization 一度约 **60%**，并把 annualized cell capacity 下调至约 **1.8 GW**；
- First Solar 2012 manufacturing restructuring 取消 / 停止部分扩产项目，包含约 **US$127M** restructuring charges，其中约 **US$99.2M** 与停止 Vietnam 4-line plant 相关；
- Applied Materials FY2012 Energy and Environmental Solutions segment 因 solar excess capacity 出现订单/收入大幅下降，并录得 impairment、inventory、restructuring charges；
- 多家 solar manufacturers 披露 module ASP、polysilicon price、margin 与 inventory write-down 恶化；
- 当期行业文件同时明确指出，credit-market contraction / project financing constraints 会导致项目取消、延期或缩减。

这不是单一公司事故，而是跨 polysilicon / wafer / cell / module / equipment / project-finance 的 multi-segment clearing。

## 9.1 信号回放

| Signal | 当期可观测证据 | v0.6 |
|---|---|---:|
| Accounting | First Solar / Applied Materials / multiple manufacturers 出现 impairment、inventory write-down、restructuring | 2 |
| Utilization / Revenue | Suntech cell utilization 约60%；solar-equipment orders / revenue 大幅下降 | 2 |
| Market Clearing | polysilicon / wafer / module price 大幅下跌，部分价格跌破生产成本 | 2 |
| Forward Commitment | First Solar 取消 Vietnam 扩产、idle production lines；industry capacity rationalization | 2 |
| Demand Quality / Financing | project financing 收紧、项目取消/延期/缩减；部分厂商流动性与 going-concern 压力 | 2 |

**研究侧结果：10/10，Segment Breadth = Multi-segment / system-wide manufacturing clearing。**

## 9.2 Lead / lag

- **First deterioration:** 2011 H2 — module / wafer / polysilicon pricing 加速下跌，oversupply 明显；
- **Cross-confirmation:** 2012 H1 — utilization、pricing、capacity rationalization、project financing 同时恶化；
- **Accounting confirmation:** 2012 reporting cycle — impairment / inventory / restructuring charges 大量出现；
- **Trough / stabilization:** 2013–2014 — inventory rationalization、supply reduction 与 demand recovery 后部分价格 / margin 改善。

这里再次出现同一模式：

> **Market Clearing / Utilization 通常早于 Accounting。**

## 9.2A Timing tightening

Additional source-level evidence narrows the start of the solar clearing:

- one 2011 equipment supplier reported a **mid-year deterioration** in LED & Solar orders, with orders slowing sharply in **Q3–Q4 2011** after a Q2 peak;
- a 2011 solar-industry filing described worldwide panel overcapacity and inventory, difficult project financing, and panel prices that had already been declining for several quarters by **2011 Q3**;
- 2012 filings then supplied the stronger utilization / capacity-rationalization / impairment confirmation.

Revised research-side timing label:

| Timing field | Case H |
|---|---|
| First deterioration | 2011 mid-year / Q3 |
| Cross-confirmation | 2011 Q3–Q4 |
| Accounting confirmation | 2012 reporting cycle |
| Trough / stabilization | 2013–2014 |
| Confidence | High for first deterioration; Medium–High for trough |

## 9.3 对 Chapter 24 的意义

这个案例强化三点：

1. **五信号并非只适用于数字技术周期**：manufacturing overbuild + financing + residual-value clearing 在 solar PV 也成立；
2. **Forward Commitment 应包含“取消扩产 / idle lines / capacity rationalization”**，不只看 CapEx guidance；
3. **Demand Quality / Financing 需要保留项目融资层**：即使终端需求仍存在，融资收紧也会切断 project conversion，从而向上游制造传导。

但仍不能把本案例升级为“统计验证”。它只是扩大 cross-industry external validity。

---

# 10. A–H Unified Timing Matrix v0.8

为了减少跨案例叙事自由度，v0.7 将所有现有观察统一成同一时钟。

| Case | First deterioration | Cross-confirmation | Accounting confirmation | Trough / stabilization | Timing confidence |
|---|---|---|---|---|---|
| A · 2000–2002 Internet/Telecom | 2000 Q4 | 2001 Mar–Apr | FY2001 Q3 (Apr-2001 charge), annual confirmation later | 2002 H1–H2，恢复边界较模糊 | High for confirmation; Medium for trough |
| B · 2018–2019 Crypto/GPU | 2018 Q4 / Nov disclosure | 2019 Jan | FY2019 Q3–Q4 | 2019 H1 | Medium–High |
| C · 2022–2023 GPU + Cloud Optimization | 2022 Aug 8 | 2022 Aug 8–24，但 system breadth 不成立 | 2022 Aug，inventory charge 几乎同步 | 2022 H2–2023 H1；AI side 更早反转 | High for first signal; Medium for trough |
| D · 2008–2009 GFC / Enterprise IT | 2007 Q4–2008 H1 | 2008 Q4 | **No qualifying hard accounting signal** | 2009 H1 trough / H2 stabilization | High |
| E · 2001–2003 Semiconductor | 2000 H2 | 2001 H1 | 2001 H2–2002 | 2003 recovery | High |
| F · 2014–2016 Oil & Gas Upstream | 2014 H2 | 2015 H1–H2 | 2015–2016 reporting | 2016 Q2–Q4 | High |
| G · 2018–2019 Hyperscale Cloud Digestion | 2019 CapEx deceleration | **No systemic cross-confirmation** | None | N/A — negative control | High |
| H · 2011–2013 Solar PV Manufacturing | 2011 mid-year / Q3 | 2011 Q3–Q4 | 2012 reporting cycle | late-2012 / early-2013 stabilization candidate；2014 equipment-layer recovery confirmed，full normalization not claimed | High / Medium–High |

### 10.1 目前能看出的 lead / lag

在当前小样本中，最稳定的方向不是某个精确月数，而是：

1. **Market Clearing / Utilization 往往早于或同步于 Accounting，但不是固定顺序。**
   - Semiconductor、Oil & Gas、Solar 最明显；
   - 2022 NVIDIA inventory-led correction 中，inventory charge 与 pricing/channel-clearing 几乎同步出现。
2. **Forward Commitment 常在 Accounting 之前恶化。**
   - Telecom、GFC、Oil & Gas、Solar 都出现先削减 / 推迟资本承诺，再由财务报表确认。
3. **Financing 的位置取决于 shock-entry path。**
   - GFC：Financing 是前导变量；
   - Oil & Gas：Financing 是中段放大器；
   - Semiconductor / Crypto：Financing 不一定可观测或不是必要条件。
4. **Accounting 的缺失不能自动否定系统性 clearing。**
   - Case D 是最重要反例。
5. **“Cross-confirmation 未发生”本身也是结果。**
   - Case G 证明 CapEx digestion 可以停留在单点，而不进入系统清算；
   - Case C 证明强 inventory/accounting 信号也可以因 Data Center / AI 反证而止于 partial clearing。

### 10.2 暂时不能做的事情

8 个 observations 仍然太少，而且 A/E 相关、B/C 都带 GPU exposure。

因此 v0.7 **不**：
- 计算平均 lead time 后包装成“预测提前 X 个月”；
- 做 p-value / regression；
- 优化五信号权重；
- 把“Accounting 通常滞后”写成固定因果定律；
- 把 Case A 与 E 当两个独立危机提高 hit rate。

当前最稳妥的经验结论是：

> **五信号框架的价值更像“跨信号确认协议”，而不是一个固定阈值计分器。Market Clearing、Utilization 与 Forward Commitment 更适合作为前置观察层，Accounting 更适合作为常见但非必需的后验确认层；Financing 的领先性取决于冲击从哪里进入。**

---

# 11. v0.8 回测结论

| 历史案例 | Accounting | Util./Revenue | Clearing | Forward | Demand Quality | 研究侧判定 |
|---|---:|---:|---:|---:|---:|---|
| 2000–2002 Internet/Telecom | 2 | 2 | 2 | 2 | 2 | Broad clearing |
| 2018–2019 Crypto/GPU | 2 | 2 | 2 | 2 | N/A | Strong partial / segment clearing |
| 2022–2023 GPU + Cloud optimization | 2 | 1 | 2 | 1 | 0 | Partial / no system-wide S4 |
| 2008–2009 GFC / Enterprise IT | 0 | 2 | 1 | 2 | 2 | Broad clearing |
| 2001–2003 Semiconductor | 2 | 2 | 2 | 2 | N/A | Broad layer clearing* |
| 2014–2016 Oil & Gas Upstream | 2 | 2 | 2 | 2 | 2 | Broad clearing |
| 2018–2019 Hyperscale Cloud CapEx Digestion | 0 | 0 | 0 | 1 | 0 | No systemic clearing |
| 2011–2013 Solar PV Manufacturing | 2 | 2 | 2 | 2 | 2 | Broad multi-segment clearing |

当前结果说明：

1. **五信号具有基本 face validity**：它能把 2001、2008–2009 的系统性资本清算与 2018、2022–2023 的局部/子市场清算区分开；
2. **Accounting 不是领先指标**：它通常用于确认，而 Market Clearing / Forward Commitment 更早；
3. **需要增加 Segment Breadth 维度**：否则 2018 与 2022 的局部 GPU 清算容易被升级为系统性清算；
4. **Demand Quality / Financing 的历史可观测性不稳定**：2001 很强，2018 很难按当前定义观测。这意味着第五信号在不同产业结构中需要 proxy hierarchy，而不能假装始终有同样的数据；
5. **Accounting 不应成为硬门槛**：2008–2009 显示金融条件主导的系统性清算可以在卖方并无巨额 write-down 时发生；
6. **相关样本不能重复计数**：2000–2002 telecom 与 2001–2003 semiconductor 属于同一宏观 episode 的不同 physical layers；
7. **跨行业外部有效性得到初步支持**：2014–2016 oil & gas 在完全不同的产业机制下仍表现出五类资本清算信号的同步恶化；
8. **新增独立负对照后，特异性得到进一步支持**：2018–2019 hyperscale cloud 显示单一公司 CapEx digestion 并不会在缺乏跨公司 revenue/utilization/clearing/financing 恶化时被升级为 S4；
9. **第二个非传统 IT 资本周期进一步提高外部有效性**：solar PV manufacturing overcapacity 显示价格、利用率、扩产、融资和会计清算可以在完全不同产业结构下同步出现；
10. **目前仍不能称为“验证过的预测系统”**：已经有 8 个 layer/cycle observations，但独立宏观 episode 仍然有限，其中两个案例与 NVIDIA/GPU 有关；不存在盲测，也没有 prospective validation。

因此，当前最准确的表述是：

> **Chapter 24 五信号系统已完成第一轮 retrospective falsification check；它在当前历史样本中尚未出现明显逻辑失效，并已暴露出 Accounting 非硬门槛、Segment Breadth 与样本相关性等重要限制，但仍未达到统计验证或前瞻验证标准。**

---

# 12. Prospective Adjudication Protocol v0.8

历史回放真正需要解决的是 **look-ahead bias**。

一个 2011 年发生、但 2012 年年报才明确披露的 impairment，不能被当作“2011 年实时已知信号”。

因此，P0-1 从 v0.8 开始对每条证据同时记录两种时间：

```text
event_time
=
经济事件实际发生的时期

publication_time
=
外部观察者首次能够合理获得该证据的时间
```

Prospective replay 只允许使用：

> **publication_time ≤ adjudication_time**

的证据。

后续年报、诉讼材料、回顾性管理层解释可以用于 ex-post 验证，但不能倒灌到 earlier decision state。

## 12.1 Prospective research states

这些是 **research adjudication labels**，不是 S1–S4 新情景，也不是统计分类器。

### NO CLEARING — 当前证据不支持 clearing

适用于：
- 没有可信 clearing signal；
- 单点恶化被更强的同时期反证抵消；
- breadth 明显不足；
- 经济活动仍显示扩张 / 正常吸收。

这是负对照必须允许的正式状态。

> **协议必须允许“不升级”。**

否则 prospective replay 会天然产生 false positive。

### WATCH — 单点恶化 / 尚未形成跨信号确认

可以包括：
- 一家公司 guidance cut；
- 一个细分库存问题；
- 单一价格暴跌；
- 单一融资收紧；
- 单一 impairment。

要求：

> 不把单点恶化升级成 system clearing。

### CANDIDATE — 多信号开始交叉确认

至少需要：
- 一个真实经济/资本信号：
  - Utilization / Revenue；
  - Market Clearing；
  - Forward Commitment；
- 加上至少一个独立信号族；
- 并且不能完全由同一公司、同一会计披露或同一底层事件重复计算。

这只是**最低证据地板**，不是校准阈值。

### CONFIRMED — 跨主体 / 跨层的 clearing 已形成

必须同时看到：
- breadth 不再是单一公司 idiosyncratic event；
- 至少一个 quantity / utilization / clearing / commitment 信号持续；
- Accounting、Financing 或第二个真实经济信号形成后续确认；
- 主要反方解释不足以解释全部证据。

不要求 Accounting 一定出现。

2008–2009 GFC 已证明：

> **Accounting absence ≠ no systemic clearing。**

2022 NVIDIA case 又证明：

> **Accounting can be nearly synchronous in inventory-led clearing。**

因此 CONFIRMED 依赖 cross-signal breadth，而不是固定信号顺序。

### STABILIZATION CANDIDATE — 恶化速度停止，但不能实时宣布 trough

Prospective research **禁止实时写“已经触底”**。

当以下现象开始出现时，只能标：

> **Stabilization Candidate**

例如：
- inventory decline stops accelerating；
- utilization stops falling；
- cancellation / capex cuts stop worsening；
- financing terms stop deteriorating；
- clearing price stops making new lows。

### RECOVERY CONFIRMED — 后续数据证明 stabilization 不是短暂反弹

需要后续独立观测确认，例如：
- utilization / revenue recovery；
- inventory normalization；
- forward commitment rebuild；
- financing / credit reopening；
- sustained pricing normalization。

P0-1 不规定“连续两个季度”之类统一阈值，因为不同产业的观测频率不同。

## 12.2 Trough / stabilization anti-look-ahead rule

历史案例表中的：

> trough / stabilization

必须拆成两个概念。

**Trough**
- 是 ex-post local minimum；
- 只有得到未来数据后才能确认；
- 不属于真正的实时决策变量。

**Stabilization Candidate**
- 是 prospective label；
- 表示 leading deterioration has stopped worsening；
- 可以之后被撤销。

因此以后不再问：

> “当时能否准确知道这是最低点？”

而是问：

> **“当时是否已有足够证据停止继续升级 clearing severity，或开始测试恢复假设？”**

这比事后预测最低点更符合真实决策。

## 12.3 Source-time ledger

每一条 prospective evidence 必须具备：

| Field | Required meaning |
|---|---|
| case_id | A–H / future case |
| signal_family | Accounting / Utilization-Revenue / Market Clearing / Forward Commitment / Demand Quality-Financing |
| event_time | underlying economic period |
| publication_time | first externally observable date |
| source_identity | filing / IR / regulator / market data / institutional source |
| actor / layer | company / industry / bank / capital market / supply layer |
| observation | what was actually observed |
| contrary_signal | same-period evidence against clearing |
| status_at_time | WATCH / CANDIDATE / CONFIRMED / STABILIZATION CANDIDATE / RECOVERY CONFIRMED |
| revision_reason | why state changed later |

Hard rule:

> **one underlying event cannot create multiple independent confirmations merely because it appears in several documents。**

For example:
- a guidance cut;
- the 10-Q repeating that guidance cut;
- a media article quoting the 10-Q

remain one evidence origin unless they add genuinely independent information.

## 12.4 Breadth protocol

Systemic clearing requires breadth.

Breadth can come from:

- multiple firms;
- multiple customer groups;
- multiple financing channels;
- multiple supply-chain layers;
- industry utilization + project/capacity decisions;
- market clearing + lender behavior.

But breadth must preserve causal independence.

Examples:

**Strong breadth**
```text
supplier utilization ↓
+
customer orders / CapEx ↓
+
secondary clearing price ↓
+
bank/project credit tightens
```

**Weak breadth**
```text
one company revenue ↓
+
same company gross margin ↓
+
same company inventory charge
```

The second group can be severe company distress without system clearing.

## 12.5 Accounting rule

Accounting is now explicitly classified as:

> **confirmation / severity evidence, not mandatory gate。**

Possible timing states:

1. **lagging accounting**
   - semiconductor / solar / oil-capital cycles;

2. **near-synchronous accounting**
   - inventory-led GPU/channel correction;

3. **no qualifying hard accounting**
   - financing-led systemic contraction such as the GFC enterprise-IT case.

This removes a hidden bias in the original five-signal score.

## 12.6 Financing rule

Financing is not always leading.

Its timing depends on shock entry:

- **GFC:** financing can lead;
- **Oil & Gas:** financing can amplify after commodity/commitment deterioration;
- **Semiconductor / GPU inventory:** financing may be secondary or unobservable.

Therefore:

> **absence of financing stress cannot veto a real clearing event。**

Likewise:

> **higher rates / spreads without project or demand transmission remain macro context, not clearing confirmation。**

This keeps P0-1 consistent with P0-4.

## 12.7 Prospective replay procedure for Cases A–H

For each historical case:

1. choose a sequence of adjudication dates using the information frequency actually available at the time;
2. hide every source published after that adjudication date;
3. assign WATCH / CANDIDATE / CONFIRMED / STABILIZATION CANDIDATE;
4. record contrary evidence;
5. advance one information period;
6. update state only when new independent evidence arrives;
7. compare the first prospective state change with the ex-post historical timing matrix.

Do **not** optimize the protocol separately for each case.

The same information discipline must also preserve:
- Case G as a genuine negative control if breadth never forms;
- Case C as partial/segment clearing rather than forced system clearing;
- A/E dependency warning because the internet/telecom and semiconductor episodes are economically linked.

## 12.8 Prospective evaluation metrics

Given only eight historical observations, P0-1 will **not** report p-values, ROC curves or optimized classifier weights.

It can still report descriptive process metrics:

### Adjudication latency

```text
Latency
=
first CONFIRMED publication_time
-
first credible deterioration publication_time
```

Use a range when evidence timing is only quarterly / semiannual.

### Candidate resolution

For every CANDIDATE:

```text
Candidate
→ Confirmed
or
→ Retracted / Segment-only
```

This is more informative than pretending the current sample estimates a stable false-positive rate.

### Evidence breadth

Record:
- number of independent actors;
- number of independent signal families;
- number of economic layers.

Do not sum them into one fitted score yet.

### Revision count

How many times did the adjudication state change?

Frequent reversals may indicate:
- noisy signals;
- weak breadth;
- protocol instability.

## 12.9 v0.8 prospective output table

Future replay should use:

| adjudication date | known evidence | contrary evidence | breadth | research state | why state changed | unavailable-at-the-time evidence |
|---|---|---|---|---|---|---|
|  |  |  |  | WATCH / CANDIDATE / CONFIRMED / STABILIZATION CANDIDATE / RECOVERY CONFIRMED |  |  |

The final column is essential.

It makes look-ahead contamination visible.

## 12.10 What v0.8 changes in the interpretation of the five-signal framework

The five signals should no longer be read as:

> **five equally weighted boxes whose sum mechanically identifies S4。**

The better interpretation is:

> **a cross-signal confirmation protocol with explicit publication-time discipline, breadth requirements, contrary evidence, and reversible adjudication states。**

This is the main methodological upgrade from retrospective pattern matching to prospective usefulness.

## 12.11 Next empirical step

Do **not** add Case I yet.

First replay at least:
- Case B (crypto/GPU);
- Case D (GFC/enterprise IT);
- Case G (hyperscale digestion negative control);
- Case H (solar)

using only contemporaneously published information.

That four-case subset deliberately includes:
- inventory-led;
- financing-led;
- negative control;
- long-duration manufacturing overcapacity.

Only after the prospective protocol survives those distinct shock types should P0-1 expand the historical sample.

---

## 12A. Prospective Replay 1 — Case B: 2018–2019 Crypto / GPU Channel Unwind

这个 replay 只使用当时已经发布的信息，不允许把 FY2019 10-K 或后续恢复数据倒灌到更早判断。

| Adjudication time | 当时已知证据 | 同期反证 | Breadth | Prospective state | 当时还不知道的后续信息 |
|---|---|---|---|---|---|
| 2018-08-16 | NVIDIA FY19 Q2 revenue US$3.12B，YoY +40%；官方称 Datacenter、Gaming、Professional Visualization、Automotive **全部创纪录** | 多平台仍同步扩张 | 单公司，多平台扩张 | **NO CLEARING** | 11 月 excess channel inventory 披露 |
| 2018-11-15 | NVIDIA 首次明确披露 post-crypto **excess channel inventory**，near-term results 受影响 | Q3 total revenue仍 YoY +21%；Datacenter / Pro Viz / Automotive 仍创纪录 | 单公司、主要是 Gaming/channel | **WATCH** | 2019-01 guidance cut；FY19 Q4 revenue collapse |
| 2019-01-28 | Q4 revenue guidance US$2.70B → **US$2.20B**；公司确认延后 production ramps 以消化库存；同时 Gaming / Datacenter 低于预期、China macro demand 恶化 | channel inventory depletion 本身仍大体按原计划推进 | 单公司，但 Market Clearing + Forward Commitment + broader demand weakness 开始叠加 | **CANDIDATE — company/segment scope** | 2 月实际 Q4 数字和 accounting charge；5–8 月恢复 |
| 2019-02-14 | Q4 revenue约 US$2.21B，QoQ -31%；Gaming / Data Center 明显下滑；库存/component accounting impact得到确认 | FY2019 全年 revenue / Data Center 仍显著增长，系统级 breadth 不足 | NVIDIA 内部多 signal；跨行业 breadth 仍弱 | **CONFIRMED — segment/company clearing, NOT system-wide** | 5 月 sequential stabilization；8 月更明确 recovery |
| 2019-05-16 | Q1 FY20 revenue QoQ +1%；公司称 Gaming returned to growth，Q2 revenue guide约 US$2.55B | YoY revenue仍 -31%；hyperscale demand仍有 near-term pause | 公司内 leading indicators停止恶化 | **STABILIZATION CANDIDATE** | 8 月跨平台 sequential growth |
| 2019-08-15 | Q2 FY20 revenue QoQ +16%；公司称 platforms sequential growth | YoY仍低于前一年高基数 | 公司/平台恢复 breadth 增强 | **RECOVERY CONFIRMED — company/segment scope** | 后续更长周期恢复 |

### 12A.1 What the prospective replay changes

如果只做 retrospective score，2018–2019 Case B 看起来很容易被写成：

> “2018 H2 已经进入 clearing。”

publication-time replay 说明这太早。

**2018-08-16** 的正确实时判断反而是：

> **NO CLEARING：所有主要平台仍创纪录。**

到 **2018-11-15**，虽然 excess inventory 已经公开，但强反证仍存在，因此只能升到：

> **WATCH。**

真正足以形成 CANDIDATE 的时间点更接近 **2019-01-28**，因为这时：
- guidance 被再次大幅下修；
- production ramp 延后；
- channel clearing 持续；
- Gaming / Datacenter demand weakness 扩大。

即便到 2019-02，也只能确认：

> **segment/company clearing，不能升级成 whole accelerated-compute system clearing。**

这验证了 breadth rule 的必要性。

## 12B. Prospective Replay 2 — Case G: 2019 Hyperscale Cloud CapEx Digestion Negative Control

Case G 用来检验协议能否拒绝一个很诱人的错误叙事：

> “Alphabet CapEx 从高位回落 = hyperscale cloud clearing。”

| Adjudication time | 当时已知证据 | 同期反证 | Breadth | Prospective state | 当时还不知道的后续信息 |
|---|---|---|---|---|---|
| 2019 Apr | Alphabet Q1 CapEx约 **US$4.64B**，低于 2018Q1约 US$7.30B；可以形成 company-specific digestion hypothesis | Alphabet revenue仍 +17%；OCF约 US$12.0B；公司称流动性足以覆盖未来 CapEx。AWS Q1 sales **+41%**；Facebook仍预计 2019 CapEx约 **US$17–19B** | 只有 Alphabet 一个 Forward Commitment-style signal；跨公司反证很强 | **WATCH → NO CLEARING** | 年度 Alphabet CapEx最终小幅回落；AWS/Facebook全年投资继续增长 |
| 2019 Jul | Alphabet Q2 CapEx约 **US$6.13B**，反而高于 2018Q2约 US$5.48B；H1累计仍低于上年 | AWS Q2 sales **+37%**；Google继续在 Cloud大量招聘；Facebook H1仍持续投资 data centers / servers / network | cross-company breadth进一步反对 clearing | **NO CLEARING** | 2019全年 AWS asset additions / Facebook CapEx继续上升 |
| 2020 Feb（2019 annual results available） | Alphabet 2019 total CapEx约 **US$23.5B**，低于 2018约 US$25.1B | AWS 2019 revenue **+37%**、AWS PP&E additions约 US$13.1B vs 9.8B；Facebook 2019 PP&E spend约 US$15.1B vs 13.9B，并继续计划更高 2020 CapEx；Google Cloud revenue继续增长 | 多家公司、多真实经济变量均反对系统 clearing | **NEGATIVE CONTROL CONFIRMED / NO SYSTEM CLEARING** | N/A |

### 12B.1 What the negative-control replay proves

如果协议只看：

> CapEx growth deceleration

那么 2019 Alphabet 很容易产生 false positive。

prospective replay 迫使判断同时看到：

- Alphabet 自身 revenue / OCF；
- AWS usage / revenue；
- Facebook infrastructure commitment；
- cross-company capital breadth。

因此 2019Q1 更合理的状态不是 CANDIDATE，而是：

> **company-specific WATCH，随后被独立反证压回 NO CLEARING。**

这说明：

> **协议不仅要能升级，也必须能被反证降级。**

### 12B.2 First prospective validation result

B/G 一正一负的初次 replay 给出两个有用结果：

1. **Case B:** protocol delays the clearing call until evidence breadth actually increases, preventing backdating.
2. **Case G:** protocol rejects a false system-wide clearing narrative even when one large buyer's CapEx has clearly decelerated.

这两个结果还不能称为 prospective statistical validation。

但它们已经比 retrospective 8/10、10/10 score 更接近真实使用条件。

下一步仍按 v0.8 计划继续：
- Case D — financing-led GFC;
- Case H — long-duration solar manufacturing overcapacity.

---

## 12C. Prospective Replay 3 — Case D: 2008–2009 GFC / Enterprise IT

Case D 检验一个最重要的反例：

> **如果 shock 从 credit / financing 先进入，是否需要等待 seller impairment 才能确认 clearing？**

答案仍然是否定的。

| Adjudication time | 当时已知证据 | 同期反证 | Breadth | Prospective state | 当时还不知道的后续信息 |
|---|---|---|---|---|---|
| 2008-07 | Federal Reserve 已公开：business fixed investment 自 2007Q4 明显失速；sales / profits / credit conditions 恶化；部分企业推迟或放弃 capital expansion；E&S Q1 持平且 Q2 indicators 指向下降；银行显著收紧 C&I standards / spreads | corporate profits虽下降但仍高于历史周期低点；部分 financing markets在 Q2 有阶段性改善 | 宏观、多行业、Financing + Forward Commitment | **CANDIDATE — broad macro/business** | 2008Q4 / 2009Q1 E&S collapse；Cisco FY2009 decline |
| 2009-02 | Fed 已确认 E&S 2008Q3约 -7.5% annualized、Q4约 **-28%**；2008H2 IT investment约 **-12.5%**；sales / production / profits 下滑并伴随 credit reduced / more expensive | 尚无 2001 telecom 式大规模 enterprise-IT accounting write-down | Financing + Utilization/Investment + Forward Commitment 跨宏观层确认 | **CONFIRMED — broad systemic clearing** | 2009Q1 E&S约 -34%；2009H2 recovery |
| 2009-07 | Fed 确认 2009Q1 E&S约 **-34%** annualized；credit 对许多 borrowers仍 tight，但 capital-spending declines “may be abating”，business financing conditions有所改善 | deterioration速度开始下降 | broad macro，leading deterioration停止恶化 | **STABILIZATION CANDIDATE** | H2 E&S / IT actual recovery |
| 2010-02 | Fed 已公开：E&S 在 2008及2009H1持续下降后，于 **2009H2 开始扩张**；IT capital在年末加速，部分企业金融条件改善 | nonresidential structures仍弱，劳动力市场仍差 | 多项 business-investment / finance reversal | **RECOVERY CONFIRMED — business E&S / IT scope** | N/A |

### 12C.1 Prospective lesson

Case D 是 v0.8 对 Accounting gate 最强的 falsification。

在 **2009-02** 的实时信息集里，已经可以确认：

- credit conditions恶化；
- investment demand collapse；
- IT / E&S broad decline；
- sales / profits deterioration。

即使没有 seller-side giant impairment，也不应继续停留在 WATCH。

因此：

> **Accounting 是 severity / confirmation channel，但不是必要条件。**

另一个重要点是：

> **2009-07 只能叫 Stabilization Candidate。**

真正的 recovery 需要到 2010-02，等 2009H2 E&S / IT rebound 被后续数据确认。

这避免把“declines may be abating”直接写成“已经触底”。

## 12D. Prospective Replay 4 — Case H: 2011–2013 Solar PV Manufacturing Overcapacity

Solar 是 long-duration manufacturing overcapacity case，用来检验 protocol 是否能在 Accounting 大规模确认之前识别：

> oversupply → price clearing → project-finance difficulty → capacity deferral / restructuring。

| Adjudication time | 当时已知证据 | 同期反证 | Breadth | Prospective state | 当时还不知道的后续信息 |
|---|---|---|---|---|---|
| 2011 Q3 filing window | 一家 solar-equipment supplier 已公开描述：worldwide panel overcapacity + inventory；project financing “very challenging”；panel prices 已连续数季下降；客户推迟新技术投资；预计 Q4 solar-panel-equipment revenue继续下降 | 2011H1仍非常强，9M solar sales同比仍增长；该来源本身不是全行业统计 | Market Clearing + Financing + Forward Commitment，但 actor independence有限 | **CANDIDATE — industry mechanism, breadth not yet fully confirmed** | 2012 First Solar / Applied Materials restructuring；Suntech utilization/capacity cuts |
| 2012 H1 | Applied Materials 已公开：solar PV first-half environment = excess manufacturing capacity relative to end demand；customers defer new-capacity purchases；5月宣布 EES restructuring。First Solar 也已批准调整计划产能 / global footprint | Applied 当时 impairment test first step仍显示 fair value高于 carrying value，说明 hard accounting distress尚未完全同步 | 多公司；capacity deferral + restructuring + clearing | **CONFIRMED — multi-actor manufacturing clearing** | 2012H2 goodwill impairment / deeper utilization cuts |
| 2012 H2 | First Solar 取消 Vietnam 4-line plant并产生约 US$99M相关 impairment；Applied FY2012 solar segment orders / sales大降、inventory charges、restructuring，并录得 US$421M goodwill impairment；Suntech材料显示 cell utilization约60%、annualized cell capacity降至约1.8GW | 终端 solar demand 并未消失；部分公司/技术路线表现不同 | Accounting + Utilization + Forward Commitment + Market Clearing 多主体确认 | **CONFIRMED — severity broadens** | 何时真正 trough / sustainable recovery 尚需未来数据 |
| late-2012 / early-2013 | Applied 披露 Q4 FY2012 new orders从前一季度极低水平 **+86%**，但仍明确称 excess manufacturing capacity持续 | 仍有 impairment / weak sales / excess capacity | deterioration可能停止加速，但 recovery breadth不足 | **STABILIZATION CANDIDATE** | 2013–2014 recovery强度与持续性 |

### 12D.1 Prospective lesson

Solar replay 比 retrospective 10/10 score 更有价值的地方在于：

**2011 Q3**
- price clearing；
- project financing difficulty；
- capacity/inventory overhang；
- forward revenue weakness

已经足以形成 **CANDIDATE**。

但因为 early evidence 对 independent actor breadth 仍有限，不应直接写成：

> system-wide confirmed clearing。

到 **2012 H1**，Applied Materials + First Solar 等独立公司开始同时进行 capacity deferral / restructuring，才升级为：

> **CONFIRMED。**

Accounting 大额 impairment 在之后继续加强 severity，但不是首次确认时点。

### 12D.2 Trough discipline

Solar 的 historical matrix 仍保留：

> 2013–2014 trough / stabilization

作为 ex-post research range。

但当前 prospective replay **不把 2013 或 2014 某一时点硬编码成实时 trough**。

现阶段只确认：

> late-2012 / early-2013 出现 **Stabilization Candidate**。

如要升级 RECOVERY CONFIRMED，需要再做 2013–2014 contemporaneous source replay，而不是引用后来的回顾性“行业已复苏”叙事。

## 12D.3 Solar Recovery Contemporaneous Replay — 2013–2014 v0.9

前一轮只把 late-2012 / early-2013 标成 **STABILIZATION CANDIDATE**。这一轮继续按 publication-time discipline 回放恢复段，避免把后来的“2013–2014 行业复苏”结论倒写回当时。

| Adjudication time | 当时已知证据 | 同期反证 | Breadth / layer | Prospective state | 当时还不知道的后续信息 |
|---|---|---|---|---|---|
| 2013-12-04 · Applied Materials FY2013 filing | Solar end-demand 仍被描述为 robust；EES book-to-bill 从 FY2012 的 0.5 改善到约 1.0，说明订单不再继续坍塌 | 设备资本开支仍 depressed；global PV production capacity 仍超过 anticipated demand；FY2013 EES new orders **US$166M vs US$195M (-15%)**，net sales **US$173M vs US$425M (-59%)**，segment operating loss约 **US$433M** | end-demand 改善，但 manufacturing-equipment layer 仍弱 | **STABILIZATION CANDIDATE — NOT recovery confirmed** | 2014 年设备订单/销售与盈利是否持续改善 |
| 2014-02-12 · Applied Materials Q1 FY2014 filing | EES operating loss缩小至约 **US$11M**；book-to-bill约 1.0 | 公司仍明确写：capital-equipment investment depressed、continued excess manufacturing capacity、tightened access to capital；new orders **US$40M**，同比 -41%；net sales **US$40M**，同比 -13% | 单一设备供应商；盈利恶化速度放缓但订单/销售仍低 | **STABILIZATION CANDIDATE** | 2014 H2 是否形成持续订单、销售和盈利恢复 |
| 2014 Q3 filing window | Applied Materials 已公开：solar equipment environment 在 FY2014 前九个月较上年 **improved slightly**；end-market demand 持续增长 | global PV production capacity 仍超过 anticipated demand；capital-equipment investment 仍低 | demand layer 已明确恢复；equipment layer 只出现温和改善 | **STABILIZATION CANDIDATE — recovery hypothesis strengthened** | FY2014 全年订单、销售、经营利润能否共同确认 |
| 2014 FY results / 10-K | EES new orders约 **US$238M vs US$166M (+43%)**；net sales约 **US$279M vs US$173M (+61%)**；segment operating income约 **US$15M vs -US$433M**，从巨亏转正 | 公司仍称 global capacity exceeded anticipated demand；Q4 orders / sales 又有 sequential weakness，因此不能写成全行业完全正常化 | 同一 manufacturing-equipment layer 的 orders + sales + operating result 同向改善 | **RECOVERY CONFIRMED — solar-equipment supplier layer; NOT full industry normalization** | 更长期的行业扩产周期与企业分化 |

### 12D.3A Recovery must close at the same economic layer

Solar recovery replay 新增一条硬规则：

> **Recovery confirmation inherits the same layer and breadth discipline as clearing confirmation.**

因此：

```text
End-demand installation growth
≠
manufacturing-capital recovery
```

终端装机增长可以成为：
- continued-collapse hypothesis 的反证；
- manufacturing stabilization 的必要背景；

但不能单独把制造设备层从 **STABILIZATION CANDIDATE** 升成 **RECOVERY CONFIRMED**。

对 Case H，真正完成 recovery closure 的证据更接近：

```text
end demand holds / grows
+
equipment orders rebuild
+
equipment sales rebuild
+
operating economics improve
```

而不是只引用后来统计到的装机量。

### 12D.3B Prospective result

这次回放把原来模糊的：

> **2013–2014 trough / recovery**

拆成了两个可实时判定状态：

1. **2013 → STABILIZATION CANDIDATE**
   - 需求层改善；
   - equipment book-to-bill / loss trajectory 改善；
   - 但设备投资、订单和销售仍不足以确认恢复。

2. **2014 full-year information → RECOVERY CONFIRMED at the equipment-supplier layer**
   - orders、sales、operating result 同向改善；
   - 但 excess capacity 仍存在，所以不宣布 “industry normalized”。

这进一步验证了 prospective protocol 的对称性：

> **不能用未来 trough 倒写 clearing，也不能用未来行业复苏叙事倒写 recovery。**

---

## 12E. Four-path prospective validation result v0.8

B / D / G / H 四个 case 已覆盖四种不同 shock-entry path：

| Case | Shock entry | First prospective escalation | Final prospective read | Main protocol test |
|---|---|---|---|---|
| B · Crypto/GPU | inventory / channel | WATCH Nov-2018 → CANDIDATE Jan-2019 | segment/company clearing, then recovery | prevents backdating and system overreach |
| D · GFC/Enterprise IT | financing / macro demand | CANDIDATE Jul-2008 | broad clearing by Feb-2009 | Accounting not mandatory |
| G · Hyperscale digestion | one-buyer CapEx deceleration | WATCH only | negative control / no system clearing | contrary evidence must de-escalate |
| H · Solar manufacturing | oversupply / price / project finance | CANDIDATE 2011Q3 | broad manufacturing clearing by 2012H1 | market/financing signals can lead accounting |

### 12E.1 What survives the prospective test

The strongest version of P0-1 is now:

> **Five-signal framework = publication-time disciplined cross-signal confirmation protocol。**

Not:

> five equal weights + fixed threshold.

The protocol must be able to do all four:

1. **delay** a clearing call when early evidence is narrow;
2. **confirm** clearing without waiting for Accounting when financing / real-economy breadth is strong;
3. **de-escalate** when contrary cross-company evidence appears;
4. **separate** Stabilization Candidate from ex-post trough / Recovery Confirmed.

### 12E.2 What is still not proven

Even after four-path prospective replay, P0-1 is **not**:

- a statistically validated classifier;
- a calibrated probability model;
- a universal early-warning lead-time estimator;
- proof that the same signal ordering will hold in AI infrastructure.

The next empirical improvement should be:

> **one additional truly independent negative control and continued cross-cycle recovery testing—not more score fitting。**

---

# 13. Sources

## 2000–2002 Internet / Telecom

- Cisco Systems, FY2001 Annual Report — inventory provision US$2.77B; restructuring / impairment / excess-facility charges; inventory turns and demand decline:  
  https://www.cisco.com/c/dam/en_us/about/ac49/ac20/downloads/annualreport/ar2001/pdf/AR.pdf
- Cisco Systems, 2001-04-16 Business and Financial Update — expected fiscal Q3 revenue approximately 30% below Q2 amid sudden demand decline:  
  https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2001/m04/cisco-systems-offers-business-and-financial-update.html
- Cisco Systems, 2001-03-09 cost-cutting announcement — capital-spending slowdown expected to extend beyond two quarters:  
  https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2001/m03/cisco-systems-inc-announces-cost-cutting-measures.html
- Federal Reserve, Monetary Policy Report / 2001–early 2002 — communications-equipment spending fell more than 30% in 2001; capital overhang and excess capacity:  
  https://www.federalreserve.gov/boarddocs/hh/2002/february/reportsection2.htm
- Federal Reserve Beige Book, 2001-03-07 — high telecommunications-equipment inventories and firms trimming capital spending:  
  https://www.federalreserve.gov/fomc/beigebook/2001/20010307/default.htm
- Nortel Networks / SEC filing — constrained capital markets, high debt, bankruptcies, excess network capacity and lower carrier CapEx:  
  https://www.sec.gov/Archives/edgar/data/1119664/000113031902000166/t06647e10-k405.htm

## 2018–2019 Crypto / GPU

- NVIDIA FY2019 Form 10-K — crypto after-effects, channel inventory, Q3/Q4 component charges and crypto-specific revenue expected to become negligible:  
  https://www.sec.gov/Archives/edgar/data/1045810/000104581019000023/nvda-2019x10k.htm
- NVIDIA, 2018 Q3 FY2019 Form 10-Q — US$57M charge after sharp fall-off in cryptocurrency mining demand:  
  https://www.sec.gov/Archives/edgar/data/1045810/000104581018000150/nvda2019q310q.htm
- NVIDIA, 2019-01-28 guidance update — Q4 revenue guidance cut from US$2.70B to US$2.20B; excess post-crypto channel inventory:  
  https://nvidianews.nvidia.com/news/nvidia-updates-financial-guidance-for-fourth-quarter-of-fiscal-year-2019
- NVIDIA FY2019 Q4 results — Q4 revenue -31% q/q; Gaming -46% q/q; post-crypto excess inventory:  
  https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2019

## 2022–2023 GPU / Cloud Optimization

- NVIDIA FY2023 Form 10-K — US$2.17B inventory provisions; Gaming -27% y/y; Data Center +41% y/y; channel undershipping:  
  https://www.sec.gov/Archives/edgar/data/1045810/000104581023000017/nvda-20230129.htm
- NVIDIA Q2 FY2023 Form 10-Q — Gaming -44% q/q; US$1.22B inventory-related charge; pricing programs and channel adjustment:  
  https://www.sec.gov/Archives/edgar/data/1045810/000104581022000147/nvda-20220731.htm
- Meta FY2022 Q4 results — 2023 CapEx guidance lowered to US$30–33B from US$34–37B due to lower data-center construction spend:  
  https://investor.atmeta.com/investor-news/press-release-details/2023/Meta-Reports-Fourth-Quarter-and-Full-Year-2022-Results/default.aspx
- Meta 2023 Q2 results — CapEx lowered again to US$27–30B, but reduction attributed to non-AI server savings and project/equipment timing; AI investment remained a priority:  
  https://investor.atmeta.com/investor-news/press-release-details/2023/Meta-Reports-Second-Quarter-2023-Results/default.aspx
- Meta 2023 Q3 results — preliminary 2024 CapEx US$30–35B, with growth driven by AI/non-AI servers and data-center construction:  
  https://investor.atmeta.com/investor-news/press-release-details/2023/Meta-Reports-Third-Quarter-2023-Results/default.aspx

## 2008–2009 Global Financial Crisis / Enterprise IT

- Federal Reserve, Monetary Policy Report, 2009-02-24 — Q4 2008 equipment/software investment collapse; reduced credit availability and higher cost of credit; IT investment contraction:  
  https://www.federalreserve.gov/monetarypolicy/mpr_20090224_part2.htm
- Federal Reserve, Monetary Policy Report, 2009-07-21 — 2009 Q1 equipment/software investment about -34% annualized; high-tech capital spending more than -20% annualized; credit availability remained tight:  
  https://www.federalreserve.gov/monetarypolicy/mpr_20090721_part2.htm
- Federal Reserve, accessible Figure 13/14 — high-tech investment and business-inventory liquidation series for 2008–2009:  
  https://www.federalreserve.gov/monetarypolicy/mpr_20090721_part2_accessible.htm
- Cisco Systems FY2009 Annual Report — FY2009 revenue -9%, product revenue approximately -12% amid reduced enterprise/service-provider spending; inventory and purchase-commitment provisions:  
  https://www.cisco.com/assets/cdc_content_elements/docs/annualreports/media/2009-ar.pdf


## 2001–2003 Semiconductor Downcycle

- Federal Reserve G.17, 2001-05-14 — high-technology capacity utilization fell for the ninth consecutive month; semiconductor/computer capacity growth estimates revised downward:  
  https://www.federalreserve.gov/releases/g17/20010514/
- Federal Reserve / FRED, semiconductor and electronic-component capacity-utilization series — utilization fell from roughly 93% in mid-2000 to roughly 60% by late 2001, then recovered through 2003:  
  https://fred.stlouisfed.org/data/CAPUTLG3344S
- Micron Technology FY2002 Form 10-K — semiconductor-memory ASP declined approximately 60% in 2001 and 53% in 2002; inventory write-downs approximately US$727M in 2001 and US$376M in 2002:  
  https://www.sec.gov/Archives/edgar/data/723125/000091205702038669/a2091284z10-k.htm
- Intel 2001 Annual Report — flash-memory results hurt by lower volume, decreased factory capacity utilization and higher inventory write-downs:  
  https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-05/history-2001-annual-report.pdf
- STMicroelectronics 2001 Form 20-F — 2001 semiconductor TAM down approximately 32%; customer inventory reductions drove lower utilization and fab closures/selective shutdowns:  
  https://www.sec.gov/Archives/edgar/data/932787/000102140802007666/d20f.htm


## 2014–2016 Oil & Gas Upstream

- Halliburton FY2015 Form 10-K — U.S. land rig count down approximately 64% from Nov. 2014 peak through Dec. 2015, 2015 revenue -28%, widespread pricing pressure, and approximately US$2.2B impairments / other charges:  
  https://www.sec.gov/Archives/edgar/data/45012/000004501216000272/hal_12312015-10k.htm
- Halliburton FY2016 Form 10-K — 2016 described as the sharpest/deepest industry decline; average U.S. rig count nearly 75% below Nov. 2014 peak, with recovery signals later in 2016:  
  https://www.sec.gov/Archives/edgar/data/45012/000004501217000047/hal_12312016-10k.htm
- Apache FY2016 Form 10-K — 2014–2016 impairment table, including approximately US$9.47B total impairments in 2015:  
  https://www.sec.gov/Archives/edgar/data/6769/000167337917000004/apa10-k2016.htm
- U.S. EIA, 2016-03-04 — U.S. mining/exploration investment declined about 35% in 2015 and companies planned further CapEx reductions:  
  https://www.eia.gov/todayinenergy/detail.php?id=24912
- U.S. EIA, 2015-09-18 — low oil prices reduced operating cash flow; producers cut CapEx, raised debt/equity, and debt service consumed a larger share of cash flow:  
  https://www.eia.gov/todayinenergy/detail.php?id=22992
- Federal Reserve SLOOS, April 2015 — banks expected oil/gas loan quality to deteriorate and reported tighter underwriting, reduced credit lines and additional collateral requirements:  
  https://www.federalreserve.gov/boarddocs/snloansurvey/201505/default.htm
- Federal Reserve / FDIC / OCC Shared National Credits review, 2015-11-05 — sharp increase in classified oil/gas commitments following the commodity-price collapse:  
  https://www.federalreserve.gov/newsevents/pressreleases/bcreg20151105a.htm
- ConocoPhillips 2016 proxy / 2015 review — 2015 capital expenditures reduced 41% vs. 2014:  
  https://www.sec.gov/Archives/edgar/data/1163165/000104746916011624/a2227560zdef14a.htm


## 2018–2019 Hyperscale Cloud CapEx Digestion

- Alphabet FY2019 Form 10-K — total CapEx approximately US$25.1B in 2018 and US$23.5B in 2019; Google Cloud revenue US$5.84B in 2018 and US$8.92B in 2019:  
  https://www.sec.gov/Archives/edgar/data/1652044/000165204420000008/goog10-k2019.htm
- Amazon FY2019 Form 10-K — AWS sales +37% in 2019; AWS net additions to property and equipment increased from approximately US$9.8B to US$13.1B:  
  https://www.sec.gov/Archives/edgar/data/1018724/000101872420000004/amzn-20191231x10k.htm
- Facebook FY2019 Form 10-K — 2019 CapEx approximately US$15.1B versus US$13.9B in 2018; 2020 CapEx expected at US$17–19B:  
  https://www.sec.gov/Archives/edgar/data/1326801/000132680120000013/fb-12312019x10k.htm


## 2011–2013 Solar PV Manufacturing

- First Solar FY2012 Form 10-K — 2012 manufacturing restructuring, approximately US$127M charges, cancellation of Vietnam 4-line plant, idle/closed manufacturing capacity:  
  https://www.sec.gov/Archives/edgar/data/1274494/000127449413000006/fslrdec1210k.htm
- Suntech 2012 investor materials — industry cell capacity utilization around 60% and capacity rationalization / reduction:  
  https://www.sec.gov/Archives/edgar/data/1342803/000110465912077662/a12-26837_1ex99d1.htm
- Applied Materials FY2012 Form 10-K — solar excess manufacturing capacity, sharp equipment-demand decline, impairment / inventory / restructuring charges:  
  https://www.sec.gov/Archives/edgar/data/6951/000000695112000018/amat10282012-10kdoc.htm
- Solar-industry SEC filing — excess module capacity, polysilicon price down to approximately US$18/kg in 2012, below production cost in some markets:  
  https://www.sec.gov/Archives/edgar/data/1594124/000104746914009214/a2222165z424b4.htm
- JA Solar / industry filing — module ASP fell sharply into 2012; inventory write-downs followed market-price decline below carrying cost:  
  https://www.sec.gov/Archives/edgar/data/1375877/000104746914000764/a2218242z424b5.htm
- Solar financing disclosure — credit-market contraction and higher financing costs caused project cancellations, postponements, and scale-backs:  
  https://www.sec.gov/Archives/edgar/data/1481513/000119312510120053/d424b4.htm


## Timing-tightening sources added in v0.7

- Cisco FY2001 Annual Report — fiscal Q3 excess inventory charge US$2.25B; FY2001 inventory / purchase-commitment provision US$2.77B: https://www.cisco.com/c/dam/en_us/about/ac49/ac20/downloads/annualreport/ar2001/pdf/AR.pdf
- NVIDIA 2018 Q2 FY2019 results — record platform revenues in August 2018, used as contrary evidence against backdating the crypto clearing: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2019
- NVIDIA 2018 Q3 FY2019 results — excess channel inventory post crypto boom publicly identified: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2019
- NVIDIA 2019-01-28 shareholder letter / guidance update — production-ramp delay and 1–2 quarter channel-inventory depletion expectation: https://www.sec.gov/Archives/edgar/data/1045810/000104581019000004/shareholderletter.htm
- NVIDIA 2022-08-08 preliminary Q2 FY2023 results — Gaming -44% q/q, channel pricing programs and ~US$1.32B inventory-related charges disclosed together: https://nvidianews.nvidia.com/news/nvidia-announces-preliminary-financial-resultsfor-second-quarter-fiscal-2023
- NVIDIA 2022-08-24 Q2 FY2023 results — ongoing OEM/channel inventory reduction into Q3 with Data Center growth counterevidence: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2023
- 2011 solar-equipment filing — mid-year deterioration, Q3–Q4 order slowdown after Q2 peak: https://www.sec.gov/Archives/edgar/data/103145/000104746913010200/a2217194z10-k.htm
- 2011 solar-industry filing — worldwide panel overcapacity/inventory, difficult project financing, multi-quarter panel-price decline by Q3 2011: https://www.sec.gov/Archives/edgar/data/927003/000095012311096521/c23205e10vq.htm


## Prospective-replay sources added in v0.8

- NVIDIA FY2019 Q2 results, 2018-08-16 — record revenue across Datacenter, Gaming, Professional Visualization and Automotive: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2019
- NVIDIA FY2019 Q3 results, 2018-11-15 — excess channel inventory post crypto boom disclosed: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2019-6747552
- NVIDIA guidance update, 2019-01-28 — Q4 guidance US$2.70B → US$2.20B; production ramps delayed to deplete excess channel inventory: https://www.sec.gov/Archives/edgar/data/1045810/000104581019000004/shareholderletter.htm
- NVIDIA FY2020 Q1 results — May 16, 2019, sequential stabilization / gaming growth resumed: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2020
- NVIDIA FY2020 Q2 results — Aug 15, 2019, sequential growth across platforms: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2020
- Alphabet 2019 Q1 Form 10-Q — Q1 CapEx US$4.638B vs US$7.299B prior year; revenue +17%; OCF US$12.0B; liquidity statement: https://www.sec.gov/Archives/edgar/data/1652044/000165204419000015/goog10-qq12019.htm
- Alphabet 2019 Q2 Form 10-Q — Q2 CapEx US$6.126B vs US$5.477B prior year; H1 CapEx US$10.764B vs US$12.776B: https://www.sec.gov/Archives/edgar/data/1652044/000165204419000023/goog10-qq22019.htm
- Amazon 2019 Q1 Form 10-Q — AWS sales +41% YoY: https://www.sec.gov/Archives/edgar/data/1018724/000101872419000043/amzn-2019331x10q.htm
- Amazon 2019 Q2 Form 10-Q — AWS sales +37% YoY: https://www.sec.gov/Archives/edgar/data/1018724/000101872419000071/amzn-2019630x10q.htm
- Amazon 2019 Form 10-K — AWS revenue US$35.026B vs US$25.655B; AWS PP&E additions US$13.058B vs US$9.783B: https://www.sec.gov/Archives/edgar/data/1018724/000101872420000004/amzn-20191231x10k.htm
- Facebook 2019 Q1 Form 10-Q — continued infrastructure investment; 2019 CapEx outlook US$17–19B: https://www.sec.gov/Archives/edgar/data/1326801/000132680119000037/fb-03312019x10q.htm
- Facebook 2019 Form 10-K — 2019 PP&E purchases US$15.10B vs US$13.92B in 2018; 2020 CapEx outlook US$17–19B: https://www.sec.gov/Archives/edgar/data/1326801/000132680120000013/fb-12312019x10k.htm


## Prospective D/H source register added in v0.8

- Federal Reserve, July 15, 2008 Monetary Policy Report — business fixed-investment slowdown, tightened credit, postponed/abandoned expansion plans: https://www.federalreserve.gov/monetarypolicy/mpr_20080715_part2.htm
- Federal Reserve, Feb 24, 2009 Monetary Policy Report — E&S -7.5% Q3 / -28% Q4 annualized; H2 IT investment -12.5%; reduced / higher-cost credit: https://www.federalreserve.gov/monetarypolicy/mpr_20090224_part2.htm
- Federal Reserve, July 21, 2009 Monetary Policy Report — Q1 E&S -34%, credit still tight, declines may be abating: https://www.federalreserve.gov/monetarypolicy/mpr_20090721_part2.htm
- Federal Reserve, Feb 24, 2010 Monetary Policy Report — E&S began expanding in H2 2009; IT capital accelerated: https://www.federalreserve.gov/monetarypolicy/mpr_20100224_part2.htm
- Advanced Energy Industries Q3 2011 Form 10-Q — worldwide panel overcapacity/inventory, difficult project financing, multi-quarter panel-price decline and customer investment pause: https://www.sec.gov/Archives/edgar/data/927003/000095012311096521/c23205e10vq.htm
- Applied Materials Q2 FY2012 Form 10-Q — first-half solar excess manufacturing capacity, deferred capacity purchases, May-2012 restructuring: https://www.sec.gov/Archives/edgar/data/6951/000144530512001872/amat-042912x10qxdoc.htm
- First Solar 2012 filing — Feb-2012 capacity restructuring; Vietnam 4-line plant cancellation / impairment: https://www.sec.gov/Archives/edgar/data/1274494/000127449412000048/fslrsep1210qdraft.htm
- Applied Materials FY2012 Form 10-K — solar excess capacity, lower orders/sales, US$421M goodwill impairment, inventory/restructuring charges: https://www.sec.gov/Archives/edgar/data/6951/000000695112000018/amat10282012-10kdoc.htm
- Suntech 2012 investor filing — cell utilization ~60% and annualized cell capacity reduced to ~1.8GW: https://www.sec.gov/Archives/edgar/data/1342803/000110465912077662/a12-26837_1ex99d1.htm


## Solar recovery source register added in v0.9

- Applied Materials FY2013 Form 10-K — robust PV end-demand but depressed capital-equipment investment; EES orders / sales / operating-loss state: https://www.sec.gov/Archives/edgar/data/6951/000000695113000044/amat10272013-10kdoc.htm
- Applied Materials Q1 FY2014 Form 10-Q — continued excess manufacturing capacity, tightened capital access, deferred equipment purchases; EES orders / sales / loss: https://www.sec.gov/Archives/edgar/data/6951/000000695114000007/amat-form10xqq12014.htm
- Applied Materials Q3 FY2014 Form 10-Q — solar equipment environment improved slightly while capital-equipment investment remained low: https://www.sec.gov/Archives/edgar/data/6951/000000695114000028/amat-form10xqq32014.htm
- Applied Materials FY2014 Form 10-K — EES orders US$238M vs US$166M; sales US$279M vs US$173M; operating income US$15M vs loss US$433M; overcapacity still present: https://www.sec.gov/Archives/edgar/data/6951/000000695114000037/amat10262014-10kdoc.htm
- IEA PVPS, *A Snapshot of Global PV 1992–2013* — contemporaneous end-market deployment context; used only as demand-layer evidence, not as manufacturing-recovery proof: https://iea-pvps.org/wp-content/uploads/2020/01/PVPS_report_-_A_Snapshot_of_Global_PV_-_1992-2013_-_final_3.pdf
