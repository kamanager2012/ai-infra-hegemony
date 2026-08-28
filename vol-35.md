# 第三十五卷：AI 电力约束实证——835 MW、1.92 GW 与 500 MW 三条路径

> **出版定位：**[第十三卷](vol-13.md)定义为什么 power 会成为 AI infrastructure 的独立物理配额；本卷只做项目级实证，重点比较 Crane、Talen/AWS 与 Kairos/Google 在 Contracted / Permitted / Energized / Utilized 状态上的差异。

## 1. 本卷只分析可验证的电力状态

AI data center power 经常出现三个数字混在一起：

- 项目宣布多少 MW/GW；
- 合同写多少 MW/GW；
- 实际已经运行多少 MW/GW。

本卷统一使用五层状态：

1. Announced
2. Contracted
3. Permitted
4. Energized
5. Utilized

只有这样，电力才可以与 hardware shipment、CapEx 和 utilization 放在同一个分析框架中。

## 2. Rack-power 输入锚：只用于数量级换算

NVIDIA 官方机柜文档给出的 GB200 NVL72 级整柜功耗约为 **120 kW/rack**。本卷只把它作为项目尺度的输入锚；液冷、busway、transformer 与高密度配电的工程含义已在[第十三卷](vol-13.md)展开。

**D 级情景算术：**500 × 120 kW = **60 MW rack-level full-load power**。它不是某个园区已经部署 500 柜的事实，也不包含完整 facility overhead，更不能据此宣布“100 MW campus 已运行”。

## 3. Microsoft / Constellation：约 835 MW restart PPA

Microsoft 与 Constellation 签署 20 年 PPA，支持重启原 Three Mile Island Unit 1，并更名为 Crane Clean Energy Center。

公开项目容量约 **835 MW**。

### 当前状态

- Contract：已签
- Restart project：推进中
- Regulatory process：进行中
- Commercial operation：尚需完成许可与重启
- Actual AI load：不能由 835 MW 名义容量直接推导

该项目的意义是：

> hyperscaler 愿意用长期需求支持一座大型现有核电资产重新投入。

## 4. Talen / AWS：revised PPA full contract quantity up to 1,920 MW

Talen 与 AWS 的 revised PPA full contract quantity 最高为 **1,920 MW**，合同延续至 2042。

关键状态变化：

> Talen 2026 Q2 10-Q 写明 transition to the revised AWS PPA **occurred in 2026-04**；较早 2025 10-K 则写过 **full transition expected in spring 2027**。因此 April 2026 不能等同于全部物理转换或 full power delivery 已完成。

分析重点仍是：

- capacity ramp；
- transmission delivery；
- energized load；
- actual AWS data-center demand；
- utilization。

这条路径代表：

> 大型 data-center demand 与既有核电站之间通过 grid/front-of-meter 结构建立长期商业关系。

## 5. Google / Kairos：最高 500 MW SMR development

Google / Kairos 的项目路径更具体：**Hermes 2 up to 50 MWe in 2030**，随后扩展为 fleet，**up to 500 MWe by 2035**。

其状态与前两项不同：

- 属于 advanced nuclear development；
- commercial deployment timeline 更长；
- current energized AI load 不能由开发目标推导。

因此，500 MW 更适合作为：

> future supply option

而不是当期 power availability。

## 6. 三个项目不能直接相加

835 MW + 1.92 GW + 500 MW

并不等于：

> 3.255 GW 已经运行的 AI power。

原因是三者处于不同阶段：

| 项目 | 名义规模 | 核心状态 |
|---|---:|---|
| Microsoft / Constellation | ~835 MW | restart + regulatory |
| Talen / AWS | up to 1,920 MW | 2026 Q2 10-Q: transition occurred 2026-04; 2025 10-K: full transition expected spring 2027 and ramp to full volume no later than 2032 |
| Google / Kairos | Hermes 2 up to 50 MWe in 2030; fleet up to 500 MWe by 2035 | long-term development |

这就是为什么能源分析必须按状态，而不是按新闻 headline 加总。

### 公开来源
- Constellation / Microsoft Crane: https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
- Talen 2026 Q2 10-Q（transition occurred 2026-04；up to 1,920 MW）：https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
- Talen 2025 10-K（full transition expected spring 2027；full-volume ramp no later than 2032）：https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
- Google / Kairos: https://www.kairospower.com/google

## 7. Grid queue 也不能等同于 shortage

大规模 interconnection queue 可以说明电网连接需求很大。

但 queue 包含：

- generation；
- storage；
- load；
- duplicate application；
- withdrawn project。

因此：

```text
Queue MW ≠ Deliverable AI MW
```

真正需要观察的是：

- time-to-interconnect；
- transmission；
- transformer；
- permit；
- actual energization。

## 8. Time-to-Power 是新的竞争变量

AI chip 可以在数月内完成新一代迭代。

大型 power infrastructure 往往需要更长时间。

因此，拥有：

- powered land；
- existing grid connection；
- firm generation；
- fast permitting

的项目可以获得明显时间优势。

这就是 **Time-to-Power**。

未来 hyperscaler 竞争很可能不仅比较：

- compute；
- chip；
- network；

还比较：

> 新增 100 MW 能多快真正上电。

## 9. Power 与 semiconductor bottleneck 会轮换

如果 CoWoS/HBM 紧张，hardware 是瓶颈。

如果 hardware supply 缓解，但 grid 迟迟不能交付，power 会成为下一瓶颈。

如果 power 扩张完成，但 workload 不够，utilization 又成为瓶颈。

这正是：

**Rolling Bottleneck Cascade**

的现实表现。

## 10. Power contract 的金融属性

长期 PPA 既是 supply hedge，也是 financial commitment。

在高需求情景中：

- secure MW 是护城河。

在 S4 Capital Hard Landing 中：

- long-duration power obligation 可能成为负担。

因此，分析 PPA 必须同时看：

- duration；
- take-or-pay；
- ramp；
- utilization；
- underlying project risk。

## 11. 当前判断

截至 2026 年 8 月，可以确认：

- AI rack 已进入约 120 kW 级功率密度；
- hyperscaler 正在签署 500 MW–GW 级长期 power arrangements；
- Talen 2026 Q2 10-Q 记载 revised-PPA transition occurred in 2026-04；较早 2025 10-K 曾预计 full transition in spring 2027，因此不能把 April 2026 写成全部物理转换或 full delivery 已完成；
- contracted/announced capacity 远大于可直接确认的 utilized AI load。

因此，电力已经成为 AI infrastructure 的战略 scarce layer。

但最有意义的指标不是“签了多少 GW”，而是：

> **多少 MW 已获许可、实际送电，并被高利用率 AI workload 持续使用。**

## 本卷关键公开来源

- NVIDIA DGX GB200/NVL72 official hardware guide（~120 kW/rack）： https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
- Constellation / Microsoft Crane Clean Energy Center（20-year PPA; ~835 MW unit）：https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
- Talen 2026 Q2 Form 10-Q（revised AWS PPA up to 1,920 MW; transition occurred in April 2026）：https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
- Talen 2025 Form 10-K（full transition expected spring 2027; full-volume ramp no later than 2032）：https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
- Kairos Power / Google（Hermes 2 up to 50 MWe in 2030; fleet up to 500 MWe by 2035）：https://www.kairospower.com/google
