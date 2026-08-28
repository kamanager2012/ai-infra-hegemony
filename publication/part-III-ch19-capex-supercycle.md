# Part III · 第19章：AI 基础设施 CapEx 超级周期

> **出版层章节。** 以 [vol-08](../vol-08.md) 为主源。资本清算的判据归 Ch24；折旧 useful life 归 Ch22。本章只回答：为什么 AI infrastructure CapEx 仍在扩张、为什么四云数字不能直接相加成“AI hardware CapEx”，以及资本周期何时从扩张转向约束。

## 1. CapEx 大小不是唯一问题，口径一致性才是第一道门

Microsoft、Amazon、Alphabet、Meta 的 infrastructure spending 已处历史高位，但四家公司财年、PPE、finance lease 与 net purchases 定义并不一致。

本书坚持三个分离：

1. company-wide CapEx 与 AI-specific CapEx 分离；
2. IT equipment 与 data-center / power infrastructure 分离；
3. actual CapEx 与 guidance / expectation 分离。

因此不存在一个可以直接从四家公司新闻稿相加得到的“官方四云 AI hardware CapEx”。

## 2. 2026 年当前资本扩张锚

| 公司 | 2026 当前公开口径 | 身份 |
|---|---:|---|
| Microsoft | calendar-2026 reported CapEx expectation ~US$175B | expectation；lease-classification adjustment 后，underlying investment expectation unchanged |
| Alphabet | US$195–205B | Q2 full-year guidance |
| Meta | US$130–145B | Q2 guidance；含 finance-lease principal |
| Amazon | US$169.007B | TTM PPE net purchases actual through 2026-06-30 |

这些数据足以证明 infrastructure investment 仍在高位扩张，但不能机械相加：三家是 guidance/expectation，Amazon 是 TTM actual，时间窗与科目都不同。

## 3. 2025 mixed-window aggregate 只能作为 scale anchor

研究层按公开 PPE/equipment purchase 复加得到的 2025 mixed-window scale 约 **US$354B**。

它的用途仅是说明资本基数已经很大，不是四家公司共同披露的统一 AI subtotal。

如果把 fulfillment、office、network、power、custom silicon、third-party accelerator 等不同资产全部命名为 AI hardware，就会把会计分类问题伪装成产业事实。

## 4. CapEx 为什么形成长期锁定

AI infrastructure 不是单一 server purchase，而是多个久期不同的资产共同建设：

- accelerator / server：较短技术周期；
- network：中短周期；
- data-center shell / cooling：长周期；
- substation / transmission：更长周期；
- long-duration PPA / generation project：可达十年以上。

因此，技术迭代速度与 infrastructure economic life 之间形成 **duration mismatch**。

## 5. Seller 与 Buyer 的资本再生产对象不同

NVIDIA 的 cash generation 更直接用于 inventory、capacity reservation、supply commitments 与 next-generation roadmap。

Hyperscaler 的资本则要同时覆盖 land、building、power、network、custom silicon、third-party systems 与 operations。

所以“谁现金更多”不是正确比较。真正的差异是：

> **每一美元资本能否直接提高下一代 scarce-resource access 与 productive utilization。**

## 6. Power 把资本周期从 Hardware Clock 拉长到 Infrastructure Clock

rack density 上升后，扩张不再只取决于 server procurement，而取决于 grid connection、substation、transformer、transmission、cooling 与 long-duration power contracts。

这使 semiconductor clock 与 power-permitting clock 叠加。

当 chip supply 缓解但 energized capacity 仍不足时，bottleneck 可以从 manufacturing 转向 Time-to-Power。

## 7. 超级周期与泡沫的区别在 Utilization

高 CapEx 可以是高回报扩张，也可以是 overbuild。

如果 utilization、revenue per deployed compute、workflow volume 与 customer commitments 同步增长，大规模 investment 可以持续形成 barrier。

如果出现低 utilization、weak monetization、next-year guidance cuts、commitment cancellation 与 falling residual value，则同一 CapEx base 会变成资本压力。

## 8. 四类领先清算信号

CapEx cycle 的转折不能只看 stock price。本书观察：

- **Accounting**：impairment / accelerated depreciation / write-down；
- **Utilization / Revenue**：deployed compute utilization / AI revenue；
- **Market Clearing**：used-system price / cloud discounts / delivery lead time；
- **Forward Commitment**：CapEx guidance / supply commitments / compute contracts / power contracts。

只有多类信号同步恶化，才足以把“ROI pressure”升级为“Capital Hard Landing”。

## 9. 当前判断

截至 2026 年 8 月，公开数据仍更支持：

> **CapEx supercycle continues + hurdle rate for utilization and monetization is rising**

而不是已经完成资本清算。

资本基数越大，下一阶段越需要证明真实 workflow、revenue 与 utilization，而不能只依赖“未来需求一定更大”的叙事。

## 关键公开来源

- Microsoft FY26 Q4 earnings / call: https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast
- Alphabet 2026 Q2 SEC Exhibit 99.1: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
- Meta 2026 Q2 SEC Exhibit 99.1: https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm
- Amazon 2026 Q2 Form 10-Q: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm