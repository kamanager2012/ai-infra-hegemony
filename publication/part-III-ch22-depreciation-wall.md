# Part III · 第22章：折旧墙与 Duration Mismatch

## 1. Depreciation Wall 是 Duration Mismatch，不是 Calendar Event

真正需要观察的条件是：

> **当 hardware refresh / economic obsolescence 快于 workload monetization 时，installed asset base 开始压缩 return，并改变下一轮 capital formation。**

所以折旧墙必须与 utilization、revenue、residual value 和 next-generation investment 一起看。

## 2. Major Cloud 的 Accounting Useful Life 并不统一

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

## 3. Accounting Life 不等于 Economic Life

一个 server 可能会计上还能继续折旧，但新 architecture、memory efficiency、software support 或 power efficiency 已使它在经济上失去竞争力。

这就是 **economic obsolescence**。

反过来，一座 data-center shell、substation 或 PPA 的经济寿命往往远长于一代 accelerator。

因此 AI infrastructure 的根本错配是：

> **short-cycle compute vs long-cycle physical infrastructure**

## 4. Clearing 沿 Asset-Duration Stack 传播

最先调整的通常是：

1. next-generation hardware orders；
2. inventory；
3. used-system / lease price；
4. discretionary expansion。

最慢调整的是 data-center shell、grid asset、generation/PPA 等 long-duration infrastructure。

这也是为什么 Capital Hard Landing 不会在一个季度完成。

## 5. CapEx 必须与 Utilization 一起分析，而不是只看折旧年限

同样规模的基础设施投资，在高利用率和低利用率条件下会产生完全不同的资本回报。

因此必须同时观察：

> **Revenue / Deployed Compute**

以及真实 **Utilization**。

固定折旧年限只能描述会计费用节奏，不能说明资产是否创造了足够现金流。

真正决定“折旧墙”强度的是：**单位已部署资本能够持续产生多少有效 workload 与收入。**

## 6. Market-Clearing Price 可以更早暴露 Economic Depreciation

used accelerator / system price、cloud lease rate 与 delivery lead time 可以早于 impairment 反映 generation obsolescence 和 oversupply。

如果新一代系统上线后旧一代 residual value 快速下跌，买方经济折旧会明显快于 accounting depreciation。

这也是 Ch24 把 Market Clearing 单列为 S4 信号的原因。

## 7. Algorithmic Efficiency 可以加速 Economic Obsolescence

如果新 architecture 能用更少 HBM、compute 或 communication 完成相同 workload，旧系统即使物理可运行，也可能在 cost per task 上迅速失去竞争力。

因此，软件/模型创新会直接改变 hardware economic life。

### 7A. Efficiency–Utilization Break-Even：效率提升必须与 Workload Growth 一起闭合

算法效率与资本回收之间的张力，可以在不预设需求弹性的情况下写成一个最简单的恒等式：

```text
Infrastructure Demand = Unit Resource Intensity × Workload Volume
```

因此：

```text
D1 / D0 = (I1 / I0) × (V1 / V0)
```

其中 (I) 表示可比 workload 的单位资源强度，(V) 表示 workload volume。

要让 aggregate resource demand 保持不变，break-even 条件是：

```text
V1 / V0 = I0 / I1
```

这只是数学恒等式，不是预测。举例说，如果一个**假设性**架构让可比 workload 的资源强度下降 **90%** ((I1/I0 = 0.1))，那么 workload volume 需要增长 **10×**，才能仅仅维持 aggregate resource demand 不变。本报告不预测“90% 效率提升”或“10× workload 一定发生”；这个例子只是 D 级 sensitivity check。

对旧一代资产而言，门槛甚至比 aggregate break-even 更高。新增 workload 可能优先迁移到 cost per task、memory efficiency、power efficiency 或 software support 更好的新系统。因此，即使全行业 compute demand 持平甚至增长，旧 generation 的 utilization 与 residual value 仍可能下降。

所以效率冲击应转化为四个可观察资本变量：

- cost per verified workload 下降速度；
- total workload volume 增长速度；
- workload 在不同 hardware generation 之间的迁移速度；
- 旧系统 utilization / lease rate / resale value 是否比 accounting depreciation 更快恶化。

因此，algorithmic progress 对 infrastructure demand 既不是天然 expansionary，也不是天然 contractionary。它首先是一个**capital-recovery variable**；最终影响取决于 workload growth 与 generation-level allocation。

---

## 8. Power Asset 具有相反的 Duration Profile

在 S2/S3 高需求环境中，long-duration power / grid asset 可能成为 scarce moat。

在 S4 中，同一个 PPA、substation 或 data-center shell 则可能变成长久期低利用率负担。

所以资产价值取决于 demand duration，而不是“电力资产永远安全”。

## 9. Anchor Buyer 降低 Financing Risk，同时集中 Demand Risk

长期 model-company compute contracts 提高 revenue visibility，使基础设施更容易融资。

但如果 anchor buyer 的 revenue、financing 或 architecture assumptions 变化，take-or-pay、renegotiation 与 stranded-capacity risk 会集中爆发。

因此 customer concentration 与 contract duration 必须与 useful life 一起看。

## 9A. Financing Structure 可以移动 Loss，但不能消除它

2026 年以后，越来越多 AI infrastructure 可能通过：

- operating lease；
- project finance；
- third-party infrastructure vehicle；
- long-duration customer contract；
- supplier equity / credit enhancement；

来融资。

这会改变 depreciation、interest、lease expense、residual-value risk 出现在哪一家公司的报表里。

但它不会改变一条基本关系：

> **如果新一代 system 的 cost per task 显著更低，旧资产的 economic value 仍会下降。**

因此：

- lease 可以把 ownership risk 转移给 lessor；
- project finance 可以把部分 risk 隔离到 SPV；
- seller credit 可以降低前期 financing friction；
- long-term contract 可以提高 revenue visibility；

但这些结构都不能让技术过时本身消失。

真正需要问的是：

> **谁最终持有 residual-value risk，以及合同现金流是否足以覆盖这项风险。**

这也是为什么“reported CapEx 较低”或“资产不在 hyperscaler balance sheet”不能自动解释为 infrastructure risk 已经下降。

## 10. 一轮 Depreciation Cycle 不能决定 2036

不同资产在不同日期投入使用、采用不同 useful life，还可能发生 impairment 或 estimate change。

不存在一个统一“2026 CapEx 在某年全部折完”的时间点。

2036 的产业结构取决于第二、第三轮 buildout、workload growth、system substitution、power、China parallel stack 与 regulation，而不是由第一轮会计折旧机械决定。

## 11. Current Read

截至 2026 年 8 月，更准确的解释是：**CapEx expansion 仍在继续，同时 duration 与 utilization risk 正在上升**，而不是已经进入广泛 impairment cycle。

折旧墙真正需要警惕的是：utilization 下滑、residual value 快速下降、CapEx / lease / project commitments 收缩与 refinancing 条件恶化等多类独立信号跨主体/层级相互印证。impairment 出现时会强化严重度判断，但正式 accounting loss 不是 mandatory gate。

## References

[^1]: Microsoft Corporation, FY26 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
[^2]: Alphabet Inc., 2025 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
[^3]: Meta Platforms, Inc., 2025 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
[^4]: Amazon.com, Inc., 2025 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
