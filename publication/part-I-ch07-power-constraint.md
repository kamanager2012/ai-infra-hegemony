# Part I · 第7章：从 120 kW Rack 到 GW 级电力约束

## 1. 核心判断：Power 已从运营成本升级为 AI System Delivery 的独立约束

当 rack-scale AI system 的整柜功耗进入约 **120 kW/rack** 量级时，电力不再只是 OpEx，而开始直接影响系统能否按期部署、上电和利用。[^1]

这意味着 AI infrastructure 的关键物理层不再只有：

- advanced logic；
- HBM；
- advanced packaging；

还包括：

- powered land；
- grid interconnection；
- substation / transformer capacity；
- firm MW；
- cooling；
- permitting。

因此，完整 AI system 的交付问题已经从“有没有芯片”扩展为：

> **有没有可以在同一时间窗口内真正上电并高利用率运行的完整基础设施。**

---

## 2. 电力分析必须使用状态机，而不能把公布的 MW/GW 容量直接相加

AI power project 至少要区分：

> **Announced → Contracted → Permitted → Construction / Transition → Energized → Utilized**

这些状态不能互换。

例如：

- 1 GW PPA 不等于 1 GW AI compute 已经 online；
- 500 MW development target 不等于当前已有 500 MW 可调度电力；
- secured capacity 不等于 energized capacity；
- energized capacity 也不等于已经被高利用率 workload 占用。

因此，AI power 研究最重要的不是把所有已公布 MW/GW 容量加总，而是判断：

> **多少容量、在什么地点、什么时间、以什么状态，能够真正服务当前或下一代 AI system。**

---

## 3. 三类代表性路径处在完全不同的交付时钟

### 3.1 Microsoft / Constellation：存量大型电源重启

Microsoft 与 Constellation 的 **20 年 PPA** 支持原 Three Mile Island Unit 1 以 Crane Clean Energy Center 名义重启，公开机组规模约 **835 MW**。[^2]

这一案例说明，大型 AI / cloud demand 已经能够通过长期购电承诺影响大型 generation asset 的资本决策。

但 835 MW 是项目容量锚，不代表 835 MW 已经实时送达 AI data center。

真正决定经济价值的是：

- regulatory approval；
- equipment restoration；
- grid interconnection；
- commercial operation timing；
- delivered MW；
- utilization。

---

### 3.2 Talen / AWS：大负荷客户与既有电源的商业关系重构

Talen/AWS revised PPA 的 full contract quantity 为 **up to 1,920 MW**，合同延续至 2042。Talen 2026 Q2 10-Q 写明 revised-PPA transition **occurred in April 2026**；更早的 2025 Form 10-K 曾披露 full transition expected in spring 2027。[^3][^4]

因此，April 2026 可以作为 revised-PPA transition 的最新公司披露状态，但不能扩写成：

- 全部物理改造已完成；
- 全部 1.92 GW 已经 delivered；
- 全部 capacity 已被 AWS workload 高利用率使用。

这一案例说明，商业合同可以提前锁定长期资源，但物理交付仍有独立时钟。

---

### 3.3 Google / Kairos：长期 Supply Option

Google / Kairos 的公开路径更长：

- Hermes 2：**up to 50 MWe in 2030**；
- fleet target：**up to 500 MWe by 2035**。[^5]

这类 advanced-nuclear agreement 的主要价值是：

- future supply option；
- industrial learning；
- long-duration hedge；
- diversification of firm power。

它不应被当成 2026–2028 的现货电力去抵消当前 interconnection、transformer 或 powered-site constraint。

---

### 3.4 NVIDIA / SB Energy / OpenAI：从购电进一步走向 Land + Power + Shell 锁定

2026-08-17，NVIDIA 披露 PORTS-Pike Technology Campus 的新结构：通过与 SB Energy 合作，NVIDIA 为 land、power 与 shell buildout 提供 credit support，初始部署设计支持 **4.25 IT-GW**；OpenAI 将使用该 site，SB Energy 建设、持有并运营 data center。项目计划容量预计从 **2028 年开始分阶段上线**。[^7]

这条证据把 Time-to-Power 再推进一层：

> **真正稀缺的不是孤立的电力合同，而是 land + power + shell 在可执行时间窗口内的组合。**

因此，LPS secured capacity 比单一 PPA 容量数字更接近 deployable-compute 的前置条件。

但 4.25 IT-GW 仍然是设计/规划容量，不是 2026 energized 或 utilized load。

---

## 4. 不同 Power / LPS Project 不能机械合并成“已运行 AI 电力”

**Table 7.1 — 代表性 AI 电力 / LPS 路径**

| 项目 | 名义规模 | 当前分析身份 |
|---|---:|---|
| Crane / Microsoft | ~835 MW | restart / regulatory / execution path |
| Talen / AWS | up to 1,920 MW | revised PPA / transition / ramp |
| Kairos / Google | up to 50 MWe in 2030; up to 500 MWe by 2035 | long-duration development option |
| PORTS-Pike / NVIDIA / SB Energy / OpenAI | initial 4.25 IT-GW design capacity | LPS secured / future phased buildout from 2028 |

**Source:** Constellation、Talen Energy、Kairos Power / Google、NVIDIA / SB Energy.[^2][^3][^4][^5][^7]  
**Note:** 不同项目处于不同合同、建设、许可、上电与利用状态，且表中的 generation MW/GW、PPA capacity 与 IT-GW 不是同一物理量，不能机械相加为 active AI load。

这些案例分别代表：

1. 重启既有大型电源；
2. 重构大型用户与现有 generation asset 的长期关系；
3. 建设新的未来 generation technology；
4. 通过信用支持提前锁定 land + power + shell 的组合交付能力。

它们说明 AI demand 正在影响 power capital formation，但不能用来证明某个统一 GW 数字已经投入 AI 运行。

---

## 5. Grid Queue 证明的是 Time-to-Power 风险，不是“AI 缺多少电”

Berkeley Lab 的 Queued Up 数据显示，美国 active generation/storage interconnection queue 在 **2023 年末**接近 **2,600 GW** 峰值，到 **2025 年末**约为 **2,061 GW**。[^6]

这个数字不能改写为“美国 AI 缺 2,061 GW 电力”。

它能够支持的更窄结论是：

> **大量 generation / storage project 需要经过漫长 interconnection 流程，grid buildout 与 transmission capacity 会形成多年级时钟。**

真正与 AI system delivery 相关的是：

- specific region；
- specific site；
- specific delivery window；
- executable interconnection path；
- firm delivered MW。

所以 nationwide queue 只是 grid friction 的宏观证据，不是 AI power shortage 的直接数量。

---

## 6. Time-to-Power 正在成为与 Chip Roadmap 并列的竞争变量

先进芯片可以按季度甚至更快迭代，但：

- transmission；
- substation；
- transformer；
- permitting；
- generation；

往往以多年推进。

这意味着 hyperscaler / data-center competition 出现一个新的时间变量：

> **Time-to-Power：从项目决策到可稳定交付、可被 workload 利用的电力需要多久。**

拥有以下条件的项目会获得明显时间优势：

- existing grid connection；
- powered land；
- available transformer / substation capacity；
- firm generation；
- executable permitting path；
- cooling infrastructure。

因此，拥有 accelerator 不代表拥有 deployable compute。

---

## 7. Power 与 Semiconductor Bottleneck 会发生轮换

AI infrastructure 没有一个永久固定的唯一瓶颈。

一种典型路径是：

> HBM / advanced packaging tight → hardware delivery受限 → 制造扩产后更多 racks 到场 → power / interconnection 成为下一瓶颈 → deployment / utilization 受限

也可能反过来：

> power / data-center capacity 提前建设 → workload 或 hardware delivery 不足 → utilization 下降 → capital return 恶化

所以：

> **一个 bottleneck 被解决，不代表整个 system bottleneck 被解决。**

这就是 Rolling Bottleneck Cascade 在电力层的含义。

---

## 8. Power Contract 与 Compute Asset 存在明显 Duration Mismatch

AI server 的技术迭代周期通常远短于：

- data-center shell；
- transmission；
- generation asset；
- long-duration PPA。

Crane 对应 **20 年 PPA**，而 compute hardware 会更快换代。[^2]

因此，长期电力承诺具有双重属性：

### 高需求情景

它是：

- supply assurance；
- deployment advantage；
- financing support；
- barrier to entry。

### 低利用率 / S4 情景

它可能转化为：

- long-duration obligation；
- stranded infrastructure；
- take-or-pay exposure；
- lower capital return。

因此，power asset 不能只按“有没有签合同”评价，还要看：

- duration；
- ramp；
- cancellation / take-or-pay；
- project execution；
- utilization；
- residual economic value。

---

## 9. 当前判断：Power 何时从“核心约束之一”升级为“主导约束”

需要看到多项同步证据，例如：

- major buyers 持续明确披露 power/interconnection 是增长上限；
- delivered hardware 大规模等待上电；
- energized capacity 长期落后于计划；
- next-generation orders 因 power delay 被推迟；
- powered sites 的 Time-to-Power 持续决定项目选址和资本回报；
- utilization 因电力不足系统性下降。

截至 2026 年 8 月，更稳健的判断是：

> **Power 已经进入与 HBM、advanced packaging 并列的核心物理约束层，但公开证据尚不足以证明它已经单独成为整个 AI infrastructure 的唯一主导瓶颈。**

## 10. 证伪边界：什么事实会迫使本章改判

应下调 power / LPS 作为核心约束的判断，如果持续出现：

- Time-to-Power 显著缩短；
- secured / contracted projects 高比例、按期转化为 energized capacity；
- transformer、substation、grid interconnection 与 cooling 不再形成主要 deployment delay；
- energized capacity 增长持续快于 deployable compute demand；
- regional power price / availability 不再显著影响 site selection。

公布的 GW 规模增加本身不足以证明 power bottleneck 已解除，必须看到 state transition 与实际 utilization。

## References

[^1]: NVIDIA, DGX GB200 Hardware Guide, rack power approximately 120 kW, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
[^2]: Constellation, Crane Clean Energy Center / Microsoft 20-year PPA and approximately 835 MW unit, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
[^3]: Talen Energy, 2026 Q2 Form 10-Q, revised AWS PPA transition and up to 1,920 MW, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
[^4]: Talen Energy, 2025 Form 10-K, expected full transition timing, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
[^5]: Kairos Power / Google partnership, Hermes 2 up to 50 MWe in 2030 and fleet up to 500 MWe by 2035, https://www.kairospower.com/google
[^6]: Lawrence Berkeley National Laboratory, “Queued Up” 2026 update, active interconnection queue, https://emp.lbl.gov/news/backlog-power-plants-seeking-transmission-grid-connection-eased-somewhat-2025-amidst
[^7]: NVIDIA, “NVIDIA Guarantees SB Energy's PORTS-Pike Technology Campus in Ohio to Exclusively Host NVIDIA AI Compute,” 2026-08-17, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx
