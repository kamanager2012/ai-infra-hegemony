# 第三十卷：折旧墙、资本清算与长期产业结构

## 1. 折旧不是年份预测，而是资本约束

AI infrastructure 的“折旧墙”经常被误解成：

> 某几年必然出现固定金额的利润冲击。

更准确的定义是：

> 当 hardware refresh 快于 workload monetization 时，资产成本开始压低资本回报率，并迫使买方减少下一轮投资。

因此，折旧墙必须与：

- utilization；
- revenue；
- residual value；
- next-generation CapEx

共同分析。

## 2. Hardware 与 infrastructure 的寿命不同

AI investment 包含：

- accelerator / server；
- network；
- data-center shell；
- cooling；
- grid；
- power contract。

这些资产的经济寿命与会计 useful life 不同。最新一手口径也并不统一：Microsoft FY26 servers/network equipment **2–6 年**；Alphabet 2025 一般 **6 年**；Meta 2025 servers/network assets **5–5.5 年**；Amazon 2025 servers/networking equipment **5–6 年**。各公司还会因技术变化调整估计寿命。

主要来源：
- Microsoft FY26 Form 10-K：https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
- Alphabet 2025 Form 10-K：https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
- Meta 2025 Form 10-K：https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
- Amazon 2025 Form 10-K：https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm

因此，不能统一使用“4年直线折旧”估算整个 AI infrastructure。

真正的风险是 duration mismatch：

短周期 hardware  
vs  
长周期 infrastructure。

## 3. 第一轮资本压力首先打在哪里

当 demand 低于预期时，最先调整的是：

1. next-generation hardware order；
2. inventory；
3. second-hand system price；
4. discretionary expansion。

最晚调整的是：

- power contract；
- data-center shell；
- grid asset。

因此，资本清算具有明显顺序。

## 4. CapEx 不能脱离 utilization

作为 **D 级 sensitivity example**，设定同样 **US$100B CapEx**：

如果 utilization 为 **90%**，它可能代表高回报增长资产。

如果 utilization 为 **30%**，它可能代表过剩资产。

US$100B、90% 与 30% 都是示例输入，不是任何公司或行业的 current actual。

因此，判断 AI infrastructure cycle 必须增加：

```text
Revenue / Deployed Compute
```

和：

```text
Utilization
```

而不是只看 CapEx。

## 5. Second-hand price 是重要市场清算信号

财报可能滞后。

second-hand GPU/system market 能更早反映：

- oversupply；
- generation obsolescence；
- weak demand。

如果新一代 system 上线后，上一代 residual value 快速下降，会直接提高 hyperscaler 的经济折旧压力。

因此，market-clearing price 是 S4 监测的重要指标。

## 6. Algorithmic efficiency 会加快经济折旧

如果新模型架构能在更少：

- HBM；
- FLOPS；
- network

下实现相同 workload，那么旧 system 即使物理上仍能运行，也可能经济上提前过时。

这构成：

> **economic obsolescence**

而不只是 accounting depreciation。

## 7. Power asset 的风险方向相反

power/data-center infrastructure 期限更长。

如果 AI demand 持续增长，它们可能成为 scarce asset。

如果 compute demand 下降，它们可能成为 stranded asset。

因此，同一个长期 PPA：

- 在 S2/S3 中是护城河；
- 在 S4 中可能变成长久期负担。

## 8. 哪些公司最能穿越资本周期

长期更强的主体通常拥有至少一项：

- high utilization；
- diversified workload；
- strong FCF；
- flexible system stack；
- low financing cost；
- scarce asset。

因此，system platform、hyperscaler、power asset owner、foundry 的资本周期表现不会相同。

## 9. Model company 的资本脆弱性

模型公司如果通过长期 compute contract 锁定大量 capacity，却无法形成稳定 revenue，可能面临：

- take-or-pay；
- financing pressure；
- contract renegotiation；
- dilution。

因此，Anchor Buyer Effect 同时带来增长和风险。

## 10. 2036 结构不能由 2026 折旧直接决定

2026 的一轮 CapEx 会按不同资产的 useful life、投入使用时点、减值与后续估计变更逐步进入折旧/摊销；不存在一个统一的“折旧完毕年份”。

2036 的产业结构取决于：

- 是否发生第二、第三轮 buildout；
- workload demand；
- system substitution；
- power；
- China parallel stack；
- regulation。

因此，不能用一轮资产折旧推导十年后公司名单。

## 11. 资本清算后的 AI 不会消失

即使 S4 Capital Hard Landing 出现，大量已建基础设施仍然存在。

历史上 fiber、telecom、cloud 都曾出现：

资本过剩  
→ asset price 下跌  
→ 使用成本下降  
→ 新应用出现。

AI infrastructure 也可能经历类似过程。

因此，资本硬着陆与长期 AI usage 增长并不矛盾。

## 12. 当前判断

截至 2026 年 8 月，尚未看到足够证据证明 AI infrastructure 已进入全面资本清算。

当前更像：

> CapEx expansion + increasing ROI pressure。

真正需要警惕的是以下组合同时出现：

- utilization 下滑；
- CapEx guidance 下调；
- supply commitments 下降；
- second-hand system price 快速下跌；
- impairment 增加；
- enterprise AI monetization 弱化。

只有这些信号同时出现，S4 才从压力测试变成现实主情景。


## 本卷关键公开来源

- Microsoft FY26 10-K（servers/network equipment useful life 2–6 years）：https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
- Alphabet 2025 10-K（servers/network equipment generally 6 years）：https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
- Meta 2025 10-K（servers/network assets 5–5.5 years）：https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
- Amazon 2025 10-K（servers/networking equipment 5–6 years；部分资产 2025 从6年改5年）：https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
