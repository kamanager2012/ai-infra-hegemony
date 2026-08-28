# Part I · 第7章：从 120 kW Rack 到 GW 级电力约束


## 1. 电力为什么从运营成本变成基础设施配额

当 rack-scale AI system 的整柜功耗进入约 **120 kW/rack** 量级，电力不再只是运行费用，而开始决定系统能否按期交付和利用。

NVIDIA 官方 GB200/GB300 NVL72 级机柜文档给出约 **120 kW/rack** 的整柜功耗口径。[^1]用它做一个明确标注的 **D 级情景算术**：500 racks × 120 kW/rack = **60 MW rack-level full-load power**。

这只是数量级，不代表任何园区已经部署 500 柜，也不包含完整 facility overhead。它能说明的是：数百柜部署很快会把局部供电需求推到数十 MW 级，变电站、输电、许可、冷却和 firm power 因而进入交付链。

所以 AI 基础设施的关键物理层不只包括 wafer / HBM / advanced packaging，还包括 **powered land / grid interconnection / substation / firm MW / cooling**。

## 2. 能源分析必须使用状态机，而不是把 GW 相加

电力项目至少要区分五种状态：**Announced → Contracted → Permitted → Energized → Utilized**。

一个 1 GW PPA 不能直接写成“已有 1 GW AI compute online”；一个 500 MW 开发目标也不能直接换算成 active rack count。项目的经济价值和对 AI 供给的现实影响，取决于它从宣布向真正高利用率运行推进了多少，而不是 headline 中的最大 MW/GW。

## 3. 三条代表性路径处在完全不同的时钟

### 3.1 Microsoft / Constellation：约 835 MW 的存量核电重启

Microsoft 与 Constellation 的 **20 年 PPA** 支持原 Three Mile Island Unit 1 以 Crane Clean Energy Center 名义重启，公开机组规模约 **835 MW**。[^2]这一案例说明 hyperscaler 开始用长期需求承诺支持大型电力资产重新进入供给。

但 835 MW 是项目/机组容量锚，不是 835 MW 已经实时送达 AI 数据中心。项目仍受监管、设备修复、重启执行、并网和商业运行时钟约束。Constellation 官方稿只说重启需要 significant investments，**没有披露 US$1.6B restart CapEx**；因此该数字不进入本章事实层。

### 3.2 Talen / AWS：up to 1,920 MW 的 revised PPA

Talen/AWS revised PPA 的 full contract quantity **up to 1,920 MW**，合同延续至 2042。Talen 2026 Q2 10-Q 写明 transition to the revised AWS PPA **occurred in April 2026**；较早的 2025 10-K 又曾写 **full transition expected in spring 2027**。[^3][^4]

因此 April 2026 可以作为 revised-PPA transition 的当前披露状态，**不能被解释成全部物理转换、输电改造和 full delivery 都已经完成**。后续真正需要追踪的是 capacity ramp、energized MW、AWS load 与 utilization。

这一案例说明，监管和商业结构可以改变供电路径，但并不会让大规模 AI 用电需求自动消失。

### 3.3 Google / Kairos：2030 的 50 MWe 与 2035 的 500 MWe

Google/Kairos 的公开时钟更长：**Hermes 2 up to 50 MWe in 2030**，随后 fleet **up to 500 MWe by 2035**。[^5]这更像长期 supply option、industrial learning path 和 capacity hedge，而不是 2026–2028 可以立刻调用的现货电力。

因此，SMR 对当前 AI 扩张的价值主要在未来选择权，不应被拿来抵消眼前的 interconnection / transformer / powered-site 约束。

## 4. 三个项目不能加成“3.255 GW 已运行 AI power”

把约 835 MW、up to 1.92 GW 和 up to 500 MWe 机械相加，会得到一个名义规模，但不会得到一个可用的 AI-load 数字。

**Table 7.1 — 三类 AI 电力项目的名义规模与交付状态**

| 项目 | 名义规模 | 主要状态 |
|---|---:|---|
| Crane / Microsoft | ~835 MW | restart + regulatory process |
| Talen / AWS | up to 1,920 MW | revised-PPA transition / ramp |
| Kairos / Google | 50 MWe in 2030; up to 500 MWe by 2035 | long-duration development |

**Source:** Constellation、Talen Energy、Kairos Power / Google.[^2][^3][^4][^5]  
**Note:** 名义容量处于不同合同、许可、建设、上电与利用状态，严禁机械相加为 active AI load。

这三条路径分别代表重启既有大电源、重构大用户与既有电源的商业/电网关系、以及建设下一代先进核电供给。技术成熟度、许可时钟和可利用时间完全不同。

## 5. Grid queue 是拥堵证据，不是“AI 缺电量”

Berkeley Lab 的 Queued Up 数据显示，美国 active generation/storage interconnection queue 在 **2023 年末**接近 **2,600 GW** 的峰值；到 **2025 年末**约为 **2,061 GW**。[^6]

这个数字不能直接变成“美国缺 2,061 GW 数据中心电力”，因为 queue 主要包含 generation / storage 项目，也包括退出、重复或延迟项目。它能支持的结论更窄：**并网流程和 transmission buildout 可能跨越多年，time-to-power 是一个真实约束。**

真正与 AI system delivery 有关的，是特定区域在特定硬件代际窗口内能真正交付的 MW，而不是全国 queue 的总 GW。

## 6. Time-to-Power：新的系统竞争变量

先进芯片可以按月/季度推进新一代，电力基础设施却常以多年推进。于是出现一个与 chip roadmap 并列的竞争变量：**Time-to-Power**。

拥有 existing grid connection、powered land、substation / transformer capacity、firm generation 与 executable permitting path 的项目会获得时间优势。这意味着 hyperscaler 的竞争不仅是“谁拿到更多 accelerator”，还包括：**谁能让下一批 50 MW / 100 MW / 500 MW 的系统更早真正上电。**

## 7. 电力与 semiconductor bottleneck 会轮换

AI 基础设施没有一个永远固定的唯一瓶颈。一种可能的 Rolling Bottleneck Cascade 是：HBM / advanced packaging 紧张 → hardware delivery 受限 → 制造约束缓解后更多 rack 到达园区 → power / interconnection 成为下一瓶颈 → deployment rate 与 utilization 下降 → 下一轮 hardware order / commitments 增速放缓。

反过来，如果 power 大量提前建设而 workload 不足，约束会从供给不足转向低利用率与资本回报。所以“电力已经成为核心约束”与“电力尚未成为唯一主导瓶颈”可以同时成立。

## 8. Power contract 与 hardware 存在 duration mismatch

AI server 的技术和经济寿命通常短于大型电力资产与长期 PPA。Crane 对应 **20 年 PPA**，而计算硬件会更快迭代。这会产生典型 duration mismatch：**shorter-cycle compute asset vs longer-cycle power/infrastructure asset**。

在高需求情景中，长期电力是护城河；在 S4 Capital Hard Landing 中，长期 obligation 也可能变成负担。因此，评估 power contract 必须同时看 duration、ramp、take-or-pay / cancellation、project execution、utilization 与 residual value。

## 9. 什么证据会证明 power 已经成为主导瓶颈

如果未来出现多项同步信号，才可以把 power 从“核心约束之一”升级成“主导约束”：major buyers 持续明确披露 power/interconnection 是增长上限；delivered hardware 大规模等待上电；energized capacity 长期显著落后于计划；next-generation orders 因 power delay 被推迟；high-value powered sites 的 time-to-power 持续成为项目决定因素；utilization 与资本回报因电力时钟而系统性恶化。

截至 2026 年 8 月，公开事实更支持：**power 已进入与 HBM、advanced packaging 并列的核心物理约束层，但尚不足以证明它已经压倒其他瓶颈、单独决定整个 AI 基础设施扩张速度。**

## References

[^1]: NVIDIA, DGX GB200 Hardware Guide, rack power approximately 120 kW, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
[^2]: Constellation, Crane Clean Energy Center / Microsoft 20-year PPA and approximately 835 MW unit, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
[^3]: Talen Energy, 2026 Q2 Form 10-Q, revised AWS PPA transition and up to 1,920 MW, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
[^4]: Talen Energy, 2025 Form 10-K, expected full transition timing, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
[^5]: Kairos Power / Google partnership, Hermes 2 up to 50 MWe in 2030 and fleet up to 500 MWe by 2035, https://www.kairospower.com/google
[^6]: Lawrence Berkeley National Laboratory, “Queued Up” 2026 update, active interconnection queue, https://emp.lbl.gov/news/backlog-power-plants-seeking-transmission-grid-connection-eased-somewhat-2025-amidst
