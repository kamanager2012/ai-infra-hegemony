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
- 3 nm：晶圆收入 **24%**
- 5 nm：**36%**
- 7 nm：**14%**
- ≤7 nm：**74%**
- HPC platform：**58%**，同比 +48%
- Smartphone：**29%**
- largest customer：**19% of annual revenue**
- second-largest customer：**17%**
- advanced packaging + testing：2024 年约 **8%**，2025 年略高于 **10%**

来源：
- TSMC 2025 Annual Report
- TSMC 4Q25 Management Report
- TSMC investor conference materials

这些数字说明两件事：

第一，HPC 已经成为 TSMC 最大 platform。  
第二，先进制造收入高度集中，但仍然服务大量客户。

因此，“TSMC 已成为某一家客户的专属 fab”不符合公开事实。

## 3. 客户收入份额不能换算成 wafer share

TSMC 的 largest customer 19% 是**年度收入份额**。

它不能直接换算成：

- N2 wafer share；
- 3 nm wafer share；
- CoWoS share；
- HPC wafer share；
- physical wafer count。

原因很简单：不同产品的 node、die size、wafer ASP、packaging intensity 都不同。

同样，HPC revenue share 58% 也不能换算成 58% 的 wafer shipments。

报告因此采用 **AHICR（Advanced HPC Incremental Capacity Capture Ratio）** 来讨论未来竞争：关注下一批新增先进 AI/HPC 资源中，哪些买方获得了更高比例，而不是拿年度历史收入份额替代未来 allocation。

## 4. Advanced packaging 已经成为公开确认的瓶颈

TSMC 管理层已经多次明确描述 advanced packaging tightness。

2024 Q4：
> very tight capacity and cannot even meet customers' need

2026 Q2：
> packaging capacity is so tight that now it limits my customers' growth

这两句比任何“月产 13 万片”“某客户独占 60%”的供应链数字更重要，因为它们属于 TSMC 自己的经营披露。

TSMC 并未公开 CoWoS customer split。

TrendForce 对 NVIDIA 占 2025 CoWoS demand 超过 60% 的估计，应作为 **B 级机构研究**使用，而不是写成 TSMC 官方数据。

## 5. 5.39 wafers/rack 只能作为压力测试

本报告使用 **5.39 CoWoS wafers/rack** 作为 D 级 geometry stress test。

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
