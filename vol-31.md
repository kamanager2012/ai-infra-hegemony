# 第三十一卷：核心指标与证据监测框架

## 1. 本卷的作用：让结论能够持续更新

一份长期产业研究报告不能只在发布日成立。

AI infrastructure 的关键变量变化很快：

- seller economics；
- hyperscaler CapEx；
- HBM supply；
- advanced packaging；
- foundry allocation；
- power；
- regulation；
- system-stack substitution。

因此，本卷不是历史数据堆积，而是一套**持续监测框架**：明确哪些指标可以更新主判断，哪些指标只能作为辅助证据。

## 2. Seller Economics

### NVIDIA

当前核心锚：

| 指标 | 数值 |
|---|---:|
| FY26 revenue | **US$215.938B** |
| FY26 Data Center revenue | **US$193.737B** |
| FY26 non-GAAP FCF（NVIDIA 定义） | **US$96.575B** |
| FY27 Q2 revenue | **US$96.221B** |
| FY27 Q2 Data Center revenue | **US$89.0B** |
| FY27 Q2 GAAP gross margin | **75.0%** |
| FY27 Q2 GAAP operating income | **US$63.734B** |
| Rubin | **full production** |

这些指标回答：

> system platform 是否仍拥有足够高的利润与现金流继续预订下一代 scarce resources？

### Supply commitments

- 2026-01-25：**US$95.2B**
- 2026-04-26：**US$119B**
- 2026-07-26：**US$279B**

口径：manufacturing, supply, and capacity commitments；Q2 10-Q 说明最新承诺主要关联 memory 与 manufacturing facilities，不是单一供应商订单。

供应承诺是前向资源锁定的重要 proxy，但不能拆成未披露的供应商金额。

## 3. Foundry / Packaging

### TSMC 2025

- 12-inch equivalent wafer shipments：约 **15.0M**
- annual capacity：超过 **17M**
- 3 nm：**24%** of wafer revenue
- 5 nm：**36%**
- 7 nm：**14%**
- ≤7 nm：**74%**
- HPC：**58%** of revenue；platform revenue YoY **+48%**
- Smartphone：**29%** of revenue；platform revenue YoY **+11%**
- 2025 largest customer：**19% of annual revenue**
- 2025 second-largest customer：**17%**
- advanced packaging + testing：略高于 **10%**

**客户口径硬边界：** annual largest / second-largest ranking 不是同一客户跨年序列。另一张匿名客户表才可直接比较 2024→2025：Customer A **12%→19%**，Customer B **22%→17%**。两套表不得拼接成“某个第一客户”的纵向轨迹。

### Packaging status

TSMC 已明确表示：

- capacity very tight；
- cannot meet customer demand；
- packaging tightness limits customer growth。

因此 advanced packaging tightness 属于 A 级事实。

### CoWoS demand allocation

TrendForce 对 NVIDIA 占 2025 CoWoS demand 超过 60% 的估计属于 **B 级机构研究**。

TSMC 没有披露 customer-level CoWoS allocation。

## 4. Memory

### Micron

核心 A 级物理锚：

> HBM3E 在相同 technology node、生产相同比特时，约需要 DDR5 **3× wafer supply**。

FY25 10-K 进一步确认 HBM 对 wafers 与 cleanroom space 的要求更高。

### TrendForce

**2026E institutional forecast：**

- HBM + RDIMM：约 **51% of DRAM bit supply**。

51% 是预测的 bit share，不是已经实现的 full-year actual，也不是 wafer share 或 revenue share。

这与 Micron 的 3× trade ratio 共同用于监测 conventional DRAM residual capacity。

### SK hynix

FY25：

- Revenue：**KRW 97.1467T**
- Operating profit：**KRW 47.2063T**
- Operating margin：**49%**
- Net income：**KRW 42.9479T**
- HBM revenue：more than doubled YoY

用于判断 HBM product mix 是否继续改善 memory-vendor economics。

## 5. Hyperscaler CapEx

四大云必须逐家公司记录，避免强行合并不同时间窗和科目。

需要持续监测：

- Microsoft CapEx；
- Amazon net PPE purchase；
- Alphabet CapEx；
- Meta CapEx；
- finance-lease treatment；
- AI/data-center specific disclosure。

判断重点不是“总额有没有创新高”，而是：

> 新增 CapEx 是否仍然主要流向 AI server、network、memory、data center 与 power。

同时必须保留 actual / guidance / expectation 的身份，不能把四家不同口径机械复加成“官方 AI hardware CapEx”。

## 6. Power

能源项目统一采用五层状态：

| 状态 | 含义 |
|---|---|
| Announced | 项目/目标已公布 |
| Contracted | 已形成合同 |
| Permitted | 已获得关键许可 |
| Energized | 已实际送电 |
| Utilized | 已形成真实负载 |

当前重要项目：

- Microsoft / Constellation：约 **835 MW** restart PPA；
- Talen / AWS：revised PPA full contract quantity **up to 1,920 MW**，transition occurred in **2026-04**，power delivery ramps to full volume **no later than 2032**；
- Google / Kairos：Hermes 2 **up to 50 MWe in 2030**，fleet **up to 500 MWe by 2035**。

因此后续应监测的是：

- contract ramp；
- energized MW；
- actual data-center load；
- utilization。

合同上限不能写成已经送到 AI racks 的实时功率。

## 7. System-Stack Substitution

持续跟踪：

### Google
- TPU / Ironwood
- compiler/runtime
- pod scale
- external availability

### AWS
- Trainium
- Neuron
- UltraServer
- Anthropic workload

### Microsoft
- Maia
- Azure workload
- software maturity

### Meta
- MTIA
- internal workload
- generative AI expansion

真正的替代指标不是 chip benchmark，而是：

- frontier workload share；
- utilization；
- migration cost；
- system TCO；
- production scale。

## 8. China Parallel Stack

应分别监测：

### Logic
- domestic accelerator；
- foundry scale；
- yield / volume disclosure。

### Memory
- HBM-class product；
- qualification；
- volume production。

### Packaging
- advanced integration；
- scale；
- yield。

### Software
- CANN / compiler/runtime；
- framework compatibility；
- cluster utilization。

### Deployment
- frontier workload；
- data-center power；
- real system scale。

只有这些指标共同改善，才能上调“中国 frontier AI parallel stack 已形成完整闭环”的判断。

## 9. Regulation

法律状态必须按程序记录：

1. inquiry / information request
2. investigation
3. statement of objections / complaint
4. formal proceeding
5. final decision
6. remedy / fine

禁止：

- inquiry → “已经起诉”
- statutory ceiling → “即将罚款”
- merger review → “已经认定垄断”

监管真正影响模型的变量是：

- interface openness；
- tying restriction；
- supply discrimination；
- structural remedy。

## 10. Capital-Clearing Signals

S4 Capital Hard Landing 重点监测四组指标。

### Accounting
- impairment
- inventory write-down
- accelerated depreciation

### Utilization / Revenue
- compute utilization
- AI workflow revenue
- revenue per deployed compute

### Market Clearing
- second-hand system price
- cloud discount
- lead time

### Forward Commitment
- CapEx guidance
- supply commitments
- long-duration compute contracts
- power contracts

只有多组信号同步恶化，才足以把 S4 从压力测试升级为主情景。

## 11. 证据等级快速表

| 证据 | 等级 |
|---|---|
| NVIDIA / TSMC / Micron 官方披露 | A |
| 政府、监管、法院、正式合同 | A |
| TrendForce / OECD / IEA / Stanford HAI | B |
| 投行、供应链、媒体估计 | C |
| 5.39 CoWoS wafers/rack | D |
| hypothetical rack-count demand | D |

## 12. 更新原则

未来每次更新报告时，只问三件事：

1. 哪个事实发生变化？
2. 它改变了哪一个机制变量？
3. 它是否足以改变 S1–S4 的相对判断？

这样可以避免因为一条新闻重新改写整套产业叙事。

本卷的价值不是“拥有最多数字”，而是确保整份报告的判断可以被现实持续校准。

## 本卷关键公开来源

- NVIDIA FY27 Q2 official results：https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- NVIDIA FY27 Q2 10-Q（US$279B commitments）：https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
- TSMC 2025 Annual Report：https://investor.tsmc.com/static/annualReports/2025/english/index.html
- TSMC 2025 20-F（annual customer rankings）：https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm
- TSMC 2025 consolidated report（Customer A/B）：https://www.sec.gov/Archives/edgar/data/1046179/000104617926000024/a2025q4consolidatedreport-.htm
- TrendForce（2026E HBM + RDIMM = 51% of DRAM bit supply）：https://www.trendforce.com/presscenter/news/20260825-13198.html
- Micron FY24 Q3 Prepared Remarks（HBM3E ≈ 3× DDR5 wafer supply）：https://investors.micron.com/static-files/4550f98c-1054-4847-a929-c17d520a0564
- SK hynix FY25 official results：https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
- Constellation / Microsoft Crane restart (~835 MW)：https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
- Talen 2026 Q2 10-Q（up to 1,920 MW; full volume no later than 2032）：https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
- Kairos / Google（50 MWe in 2030; up to 500 MWe by 2035）：https://www.kairospower.com/google
