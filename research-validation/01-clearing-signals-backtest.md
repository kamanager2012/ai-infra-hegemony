# P0-1 · Chapter 24 五类资本清算信号历史回测 v0.3

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
- **2001-04**：Cisco 正式披露需求突然下滑、Q3 revenue 预计环比约 -30%，并形成巨额库存 provision；
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

### 4.3 对 Chapter 24 的意义

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

# 7. v0.3 回测结论

| 历史案例 | Accounting | Util./Revenue | Clearing | Forward | Demand Quality | 研究侧判定 |
|---|---:|---:|---:|---:|---:|---|
| 2000–2002 Internet/Telecom | 2 | 2 | 2 | 2 | 2 | Broad clearing |
| 2018–2019 Crypto/GPU | 2 | 2 | 2 | 2 | N/A | Strong partial / segment clearing |
| 2022–2023 GPU + Cloud optimization | 2 | 1 | 2 | 1 | 0 | Partial / no system-wide S4 |
| 2008–2009 GFC / Enterprise IT | 0 | 2 | 1 | 2 | 2 | Broad clearing |
| 2001–2003 Semiconductor | 2 | 2 | 2 | 2 | N/A | Broad layer clearing* |

当前结果说明：

1. **五信号具有基本 face validity**：它能把 2001、2008–2009 的系统性资本清算与 2018、2022–2023 的局部/子市场清算区分开；
2. **Accounting 不是领先指标**：它通常用于确认，而 Market Clearing / Forward Commitment 更早；
3. **需要增加 Segment Breadth 维度**：否则 2018 与 2022 的局部 GPU 清算容易被升级为系统性清算；
4. **Demand Quality / Financing 的历史可观测性不稳定**：2001 很强，2018 很难按当前定义观测。这意味着第五信号在不同产业结构中需要 proxy hierarchy，而不能假装始终有同样的数据；
5. **Accounting 不应成为硬门槛**：2008–2009 显示金融条件主导的系统性清算可以在卖方并无巨额 write-down 时发生；
6. **相关样本不能重复计数**：2000–2002 telecom 与 2001–2003 semiconductor 属于同一宏观 episode 的不同 physical layers；
7. **目前仍不能称为“验证过的预测系统”**：已经有 5 个 layer/cycle observations，但宏观独立 episode 更少，其中两个案例与 NVIDIA/GPU 有关；不存在盲测，也没有 prospective validation。

因此，当前最准确的表述是：

> **Chapter 24 五信号系统已完成第一轮 retrospective falsification check；它在当前历史样本中尚未出现明显逻辑失效，并已暴露出 Accounting 非硬门槛、Segment Breadth 与样本相关性等重要限制，但仍未达到统计验证或前瞻验证标准。**

---

# 8. 下一步：P0-1 v0.4

下一版继续增加**独立周期**与 timing 数据，不再改变本版的 proxy / breadth / false-positive 规则：

1. **2014–2016 commodity / datacenter-adjacent capex slowdown** 或其他独立资本周期 — 检验非科技泡沫型清算；
2. 至少加入一个“高估值/高 CapEx 但最终没有 system-wide hard landing”的额外负对照；
3. 为每个信号建立 **proxy hierarchy**：A 级一手指标 > B 级机构指标 > C 级市场代理；
4. 记录 **first-deterioration date / confirmation date / trough date**，估计不同信号的领先/滞后关系；
5. 至少加入一个“看起来很危险但最后没有 hard landing”的额外负对照；
6. 在样本扩充前，不优化 0/1/2 的权重，不把任何阈值写回正式 Chapter 24。

---

# 9. Sources

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
