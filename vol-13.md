# 第十三卷：AI 时代能源战争——从 120 kW Rack 到 GW 级电力锁定

## 1. 电力为什么从运营成本变成基础设施配额

当 AI rack power density 进入约 **120 kW/rack** 级别后，data center 建设逻辑发生变化。

**D 级情景算术：**约 500 个按 **120 kW/rack** 设计的 GB200 NVL72 rack，对应约 **60 MW 的 rack-level full-load power**。该乘算只说明数量级压力，不代表实际已部署 500 柜或 60 MW 已上电。这里的 120 kW 是 NVIDIA 对整柜功耗的官方口径，包含 compute nodes 与 rack components（如 switches / interconnects），不能写成纯 IT compute load。来源：https://docs.nvidia.com/mission-control/docs/systems-administration-guide/2.0.0/prs/faq.html 。

这意味着 AI infrastructure 的交付不再只取决于：

- GPU；
- HBM；
- advanced packaging；

还取决于：

- grid connection；
- substation；
- transformer；
- transmission；
- cooling；
- firm power；
- permit。

因此，电力正在成为 AI 基础设施的第三类核心稀缺资源。

## 2. Contracted MW 不等于 energized load

能源分析必须严格区分五种状态：

1. announced capacity；
2. contracted capacity；
3. permitted capacity；
4. energized capacity；
5. utilized load。

这五者不能互换。

例如，一个 1 GW PPA 不能直接写成“已有 1 GW AI compute online”。

同样，planned data center power 也不能直接换算成 active GPU count。

## 3. Microsoft / Constellation：约 835 MW 核电重启

Microsoft 与 Constellation 的长期 PPA 对应约 **835 MW** 核电机组重启。

这一案例说明，hyperscaler 已经愿意用长期需求锚定既有 nuclear asset 的重新投入。

它的战略意义不是“Microsoft 已经得到 835 MW AI 实时负荷”，而是：

> 超大 AI 买方开始通过长期合同把 power supply 从公共市场采购转变为专用基础设施安排。

实际效果仍取决于：

- regulatory approval；
- restart schedule；
- grid delivery；
- commercial operation；
- actual utilization。

## 4. Talen / AWS：最高 1.92 GW 的长期电力安排

Talen/AWS 新版 PPA 最高可扩展至 **1.92 GW**。

Talen 2026 Q2 10-Q 写明，向 revised AWS PPA 的 transition **occurred in April 2026**；较早的 2025 10-K 则曾描述为 spring 2026 开始 transitioning、**full transition expected in spring 2027**。因此，April 2026 应理解为 revised-PPA transition 状态更新，不能写成全部物理转换与供电交付已经完成。

后续关键变量仍是：

- contract ramp；
- energized MW；
- actual data-center load；
- utilization。

这也是报告在能源分析中最重要的状态更新之一。

## 5. Google / Kairos：2030 首个 50 MWe、2035 fleet up to 500 MWe

Google 与 Kairos 的公开路径是：**Hermes 2 up to 50 MWe in 2030**，随后 fleet **up to 500 MWe by 2035**。

与既有核电站重启不同，SMR 属于更长期的供给路线。

其价值更像：

- future option；
- long-duration capacity hedge；
- industrial learning path。

因此，SMR capacity 不应被拿来平衡 2026–2028 年已经存在的短期 rack deployment pressure。

## 6. 为什么 power 会形成新的“资源锁定”

半导体供给具有代际属性。

电力供给具有地理和许可属性。

一旦 hyperscaler 提前锁定：

- powered land；
- grid interconnect；
- firm generation；
- substation capacity；

这些资源很难在短期内被其他竞争者复制。

因此，AI resource competition 正在从：

> wafer / HBM / packaging

扩展到：

> **powered site / grid / firm MW**。

### 本卷关键公开来源
- NVIDIA GB200/NVL72 rack power (~120 kW/rack): https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
- Constellation / Microsoft Crane restart (~835 MW): https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
- Talen 2026 Q2 10-Q — revised AWS PPA, up to 1,920 MW, ramp to full volume no later than 2032: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
- Kairos / Google — Hermes 2 up to 50 MWe in 2030; fleet up to 500 MWe by 2035: https://www.kairospower.com/google

## 7. 电力如何打断 semiconductor expansion

如果 semiconductor supply 持续增加，但 data center 无法按时上电，则会出现：

1. delivered hardware 等待部署；
2. utilization 下降；
3. depreciation 开始但 revenue 未同步；
4. next-generation orders 推迟；
5. supply commitments 增长放缓。

这就是电力能够触发的 **Rolling Bottleneck Cascade**：

packaging bottleneck 缓解  
→ power bottleneck 上升  
→ deployment rate 下降  
→ hardware order growth 下降。

## 8. 不能把全国电力总量当成 AI 可用电力

AI data center 的核心约束通常是局部节点。

全国发电装机充足，并不意味着某个园区能够在任意给定的短期窗口内获得 **100 MW 级**可交付电力；具体 time-to-power 必须由当地 interconnection、变电站、输电和许可进度逐项目核验。

真正重要的是：

- local transformer；
- transmission corridor；
- interconnection queue；
- permit；
- construction；
- firm generation。

因此，AI power constraint 是**节点问题和时间问题**，不是简单的国家总装机问题。

## 9. Power contract 与 hardware depreciation 的期限错配

AI server 可能在数年内快速迭代，而大型 power infrastructure 与长期 PPA 的期限往往更长；例如 Microsoft / Constellation 的 Crane 安排公开为 **20 年 PPA**。

因此存在 duration mismatch：

短寿命 compute asset  
vs  
长寿命 power/infrastructure asset。

在需求持续增长时，这种长期电力资产是护城河。

在资本硬着陆时，它也可能变成长久期负担。

## 10. 当前判断

截至 2026 年 8 月：

- power 已经成为 AI infrastructure 的核心约束；
- 大型 hyperscaler 正在用长期合同提前锁定 MW；
- contracted capacity 远大于可直接确认的 energized AI load；
- nuclear restart、front-of-meter PPA 与 SMR development 处于不同成熟度；
- 目前尚不足以断言“电力已经终止 AI 扩张”。

未来最重要的指标是：

- energized MW；
- time-to-power；
- rack utilization；
- power-related deployment delay；
- next-round hardware commitments。

真正的能源战争不是“谁签了最大 GW”，而是谁能把合同容量转化为可持续运行的高利用率 compute。
