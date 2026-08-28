# 第四卷：TSMC、N2 与先进制造资源分配

## 1. 真正的竞争对象不是“2 nm 报价”

先进制造竞争经常被简化为“谁拿到 2 nm”“一片 wafer 多少钱”。这种表达忽略了 AI system 的真正交付条件。

frontier AI system 同时需要：

- leading-edge logic；
- HBM；
- advanced packaging；
- substrates；
- high-speed interconnect；
- power。

因此，先进制造竞争的核心不是单一 node price，而是**下一代增量资源的获得顺序与确定性**。

## 2. TSMC 2025 的事实底座

TSMC 2025 年公开数据：

- 12-inch equivalent wafer shipments：约 **15.0M**
- annual capacity：超过 **17M wafers**
- 3 nm：wafer revenue **24%**
- 5 nm：**36%**
- 7 nm：**14%**
- ≤7 nm：**74%**
- HPC platform：**58%**，platform revenue 同比 +48%
- Smartphone platform：**29%**，platform revenue 同比 +11%
- largest customer：**19% of annual revenue**
- second-largest customer：**17%**
- 2024 Q4 transcript：**advanced packaging and testing >8% of revenue**；
- 2025 Q4 transcript（公司会后更正）：**advanced packaging slightly over 10% of revenue**。两年标签并不完全相同，因此不把 8%→10% 写成严格同口径时间序列。

来源：
- TSMC 2025 Annual Report
- TSMC 4Q25 Management Report
- TSMC investor conference materials

这些数字说明两件事：

第一，HPC 已经成为 TSMC 最大 platform。  
第二，先进制造收入高度集中，但仍然服务大量客户。

因此，“TSMC 已成为某一家客户的专属 fab”不符合公开事实。

## 3. 客户收入份额既不能换算成 wafer share，也不能拼成虚假跨年轨迹

TSMC 的 2025 largest customer **19%** 与 second-largest customer **17%** 都是**年度收入排名口径**。

它们不能直接换算成：

- N2 wafer share；
- 3 nm wafer share；
- CoWoS share；
- HPC wafer share；
- physical wafer count。

同样重要的是，**annual largest / second-largest ranking 不能被当成同一个客户的跨年序列**。TSMC 另一张匿名客户表才提供可直接跨年比较的数据：

- Customer A：2024→2025 **12%→19%**；
- Customer B：2024→2025 **22%→17%**。

因此，不能把某一年的 “largest customer 22%” 与下一年的 Customer A 19% 拼接后解释成同一个客户“份额下降”。两套披露回答不同问题，必须分开。

原因也包括：不同产品的 node、die size、wafer ASP、packaging intensity 都不同。

同样，HPC revenue share 58% 也不能换算成 58% 的 wafer shipments。

报告因此采用 **AHICR（Advanced/HPC Incremental Capacity Capture Ratio）** 来讨论未来竞争：关注下一批新增先进 AI/HPC 资源中，哪些买方获得了更高比例，而不是拿年度历史收入份额替代未来 allocation。

## 4. Advanced packaging 已经成为公开确认的瓶颈

TSMC 管理层已经多次明确描述 advanced packaging tightness。

2024 Q4：
> very tight capacity and cannot even meet customers' need

2026 Q2：
> packaging capacity is so tight that now it limits my customers' growth

这两句比任何“月产 13 万片”“某客户独占 60%”的供应链数字更重要，因为它们属于 TSMC 自己的经营披露。

TSMC 并未公开 CoWoS customer split。

TrendForce 对 NVIDIA 占 2025 CoWoS demand 超过 60% 的估计，应作为 **B 级机构研究**使用，而不是写成 TSMC 官方数据。

## 5. 5.37 wafers/rack 只能作为压力测试

本报告使用 **5.37 CoWoS wafers/rack** 作为 D 级 geometry stress test。

其意义是估算 rack-scale deployment 对 advanced packaging 的数量级压力，而不是推导 TSMC 全厂产能。

它不能用于：

- 除 TSMC 全年约 15M wafer shipments；
- 推导 Blackwell 实际出货；
- 推导 CoWoS yield；
- 推导客户实际 allocation。

这种严格的物理池区分，是避免供应链分析出现数量级错误的关键。

## 6. N2 的战略价值来自“增量首发资源”

N2 的重要性不只是 transistor density，而是它代表下一轮 frontier system 的 leading-edge logic resource。

竞争者真正关心的是：

- 谁更早进入 volume production；
- 谁能拿到足够规模；
- 谁能同时匹配 HBM 与 packaging；
- 谁能维持稳定良率和交期；
- 谁能把 node migration 转化为 system performance。

因此，“拿到 N2”本身不是胜利。一个系统如果缺 HBM、CoWoS、interconnect 或 power，同样无法形成有效交付。

## 7. TSMC 如何进行资源分配

供应商不可能只看一个变量。

先进产能 allocation 更可能同时受以下因素影响：

- price；
- committed volume；
- contract duration；
- prepayment；
- credit quality；
- utilization certainty；
- roadmap stability；
- customer diversification；
- geopolitical risk。

因此，本报告不采用“TSMC 没有理由得罪第一客户”这种决定论。

更合理的机制是：

> 当某买方拥有更大长期订单、更强信用、更高预付款能力和更确定的 roadmap 时，它在下一批增量资源中的议价能力提高；但 TSMC 同时仍有维护客户多元化与降低地缘风险的商业动机。

## 8. Samsung 与其他代工厂的意义

TrendForce 2026 Q1 foundry revenue share：

- TSMC：约 **72%**
- Samsung：约 **6.5%**
- SMIC：约 **5.1%**

这是 foundry revenue share，不是 frontier AI capacity share。

Samsung 的存在意味着 leading-edge supply 并非理论上只有一家，但实际竞争力必须同时考虑：

- node performance；
- yield；
- packaging；
- HBM ecosystem；
- customer qualification；
- software/system integration。

因此，“有第二家先进代工厂”与“形成可完全替代的第二套 frontier AI supply stack”是两个不同命题。

## 9. 当前判断

TSMC 的战略地位来自三个同时存在的事实：

1. leading-edge logic 份额高；
2. HPC 已成为最大 platform；
3. advanced packaging 仍是公开确认的增长约束。

未来真正需要观察的不是某一季 customer revenue share，而是：

- N2/N2P/A16 等新增资源的客户结构；
- advanced packaging 扩产速度；
- HBM supply；
- cloud custom silicon 对新增资源的争夺；
- 第二代工体系能否在 logic + packaging + HBM 上形成组合替代。

先进制造竞争正在从“谁拥有最先进 node”转变为“谁能稳定获得完整 frontier system 所需的全部 scarce layers”。

## 本篇关键公开来源

- TSMC 2025 Annual Report: https://investor.tsmc.com/static/annualReports/2025/english/index.html
- TSMC 2025 20-F（annual largest / second-largest customer ranking）: https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm
- TSMC 2025 consolidated report（Customer A/B 2024→2025）: https://www.sec.gov/Archives/edgar/data/1046179/000104617926000024/a2025q4consolidatedreport-.htm

- TSMC 4Q24 Transcript（advanced packaging and testing >8%）：https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf
- TSMC 4Q25 Transcript（2025 advanced packaging slightly over 10%，company-corrected）：https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
- TSMC 2Q26 Earnings Conference Transcript（packaging capacity limits customers' growth）：https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
- TrendForce 2025 CoWoS demand structure（NVIDIA >60%，B 级机构估计）：https://www.trendforce.com/research/download/RP250314ZJ
- TrendForce 2026-06-12（1Q26 foundry revenue shares：TSMC ~72%、Samsung ~6.5%、SMIC ~5.1%）：https://www.trendforce.com/presscenter/news/20260612-13095.html
