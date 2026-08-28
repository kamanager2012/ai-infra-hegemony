# Part III · 第22章：折旧墙与 Duration Mismatch

## 1. 折旧墙不是某一年必然出现的固定美元冲击

更准确的定义是：

> **当 hardware refresh / economic obsolescence 快于 workload monetization 时，已形成资产成本开始压低资本回报，并改变下一轮 CapEx。**

所以折旧墙必须与 utilization、revenue、residual value 和 next-generation investment 一起看。

## 2. 四家主要 Cloud 的 Server Useful Life 并不统一

最新公司披露大致显示：

**Table 22.1 — 主要 Cloud 公司 server / network equipment useful-life disclosure**

| 公司 | server / network equipment useful-life disclosure |
|---|---|
| Microsoft FY26 | 2–6 years |
| Alphabet 2025 | generally 6 years |
| Meta 2025 | 5–5.5 years |
| Amazon 2025 | 5–6 years；部分资产 2025 从 6 年调整到 5 年 |

**Source:** Microsoft FY26 10-K、Alphabet 2025 10-K、Meta 2025 10-K、Amazon 2025 10-K.[^1][^2][^3][^4]  
**Note:** accounting useful life 不是 economic life；不同公司资产类别与折旧估计不可机械视为同口径。

这已经足以证明：不能用一个统一“4 年直线折旧”去估算整个 AI infrastructure。

## 3. Accounting Useful Life 与 Economic Life 不相同

一个 server 可能会计上还能继续折旧，但新 architecture、memory efficiency、software support 或 power efficiency 已使它在经济上失去竞争力。

这就是 **economic obsolescence**。

反过来，一座 data-center shell、substation 或 PPA 的经济寿命往往远长于一代 accelerator。

因此 AI infrastructure 的根本错配是：

> **short-cycle compute vs long-cycle physical infrastructure**

## 4. Demand 转弱时，清算有明确顺序

最先调整的通常是：

1. next-generation hardware orders；
2. inventory；
3. used-system / lease price；
4. discretionary expansion。

最慢调整的是 data-center shell、grid asset、generation/PPA 等 long-duration infrastructure。

这也是为什么 Capital Hard Landing 不会在一个季度完成。

## 5. CapEx 必须除以 Utilization，而不是只除以年份

作为 **D 级 sensitivity example**，同样 **US$100B** investment 在 **90%** 与 **30%** utilization 下会代表完全不同的经济结果；US$100B、90% 和 30% 都是示例输入，不是行业 actual。

因此必须同时看：

> **Revenue / Deployed Compute**

以及真实 **Utilization**。

固定折旧年限只能描述会计费用节奏，不能描述资产是否在创造足够现金流。

## 6. Market-clearing Price 是比财报更快的 Economic Depreciation 信号

used accelerator / system price、cloud lease rate 与 delivery lead time 可以早于 impairment 反映 generation obsolescence 和 oversupply。

如果新一代系统上线后旧一代 residual value 快速下跌，买方经济折旧会明显快于 accounting depreciation。

这也是 Ch24 把 Market Clearing 单列为 S4 信号的原因。

## 7. Algorithmic Efficiency 也会制造 Economic Obsolescence

如果新 architecture 能用更少 HBM、compute 或 communication 完成相同 workload，旧系统即使物理可运行，也可能在 cost per task 上迅速失去竞争力。

因此，软件/模型创新会直接改变 hardware economic life。

## 8. Power Asset 的风险方向恰好相反

在 S2/S3 高需求环境中，long-duration power / grid asset 可能成为 scarce moat。

在 S4 中，同一个 PPA、substation 或 data-center shell 则可能变成长久期低利用率负担。

所以资产价值取决于 demand duration，而不是“电力资产永远安全”。

## 9. Anchor Buyer 能降低融资风险，也会集中 Demand Risk

长期 model-company compute contracts 提高 revenue visibility，使基础设施更容易融资。

但如果 anchor buyer 的 revenue、financing 或 architecture assumptions 变化，take-or-pay、renegotiation 与 stranded-capacity risk 会集中爆发。

因此 customer concentration 与 contract duration 必须与 useful life 一起看。

## 10. 2036 不能由 2026 一轮折旧直接推出

不同资产在不同日期投入使用、采用不同 useful life，还可能发生 impairment 或 estimate change。

不存在一个统一“2026 CapEx 在某年全部折完”的时间点。

2036 的产业结构取决于第二、第三轮 buildout、workload growth、system substitution、power、China parallel stack 与 regulation，而不是由第一轮会计折旧机械决定。

## 11. 当前判断

截至 2026 年 8 月，更准确的状态是：

> **CapEx expansion + rising duration / utilization risk**

而不是已经确认的大规模 impairment cycle。

折旧墙真正需要警惕的组合是：utilization 下滑、residual value 快速下降、CapEx guidance 下调、commitments 收缩和 impairment 增加同时出现。

## References

[^1]: Microsoft Corporation, FY26 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
[^2]: Alphabet Inc., 2025 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
[^3]: Meta Platforms, Inc., 2025 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
[^4]: Amazon.com, Inc., 2025 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
