# Part II · 第17章：中国 Parallel Stack：Production-Grade Substitution 与 Autonomous Frontier Closure

## 1. 首先必须拆开三个不同 Threshold

中国技术能力不能被压缩成一个“国产化率”。

至少要分别回答三个问题：

1. **consumer computing 能否形成有规模的商业替代？**
2. **PC / workstation 能否同时跨过 software compatibility、performance 与 commercial scale？**
3. **frontier AI stack 能否运行 production workload，并在关键外部输入受限时继续跨代扩张？**

一个层级的证据不能替另一个层级完成 closure。smartphone supply chain 较强，不等于 frontier AI 已闭环；frontier AI 仍有约束，也不等于“中国没有半导体替代能力”。

对于 frontier AI，需要采用两个独立测试：

> **Production-Grade Parallel Stack：** 系统能否在真实 workload 中同时满足 performance、scale、portability、supply continuity、reliability、utilization 与 economics？

> **Autonomous Frontier Closure：** 当关键外部 manufacturing、equipment、materials、software 或 service 受限时，系统能否继续跨代扩张和迭代？

这一区分具有战略意义：**production-grade substitution 可以在 autonomous closure 尚未完成时，就已经产生真实产业与竞争影响。**

## 2. Consumer Computing：商业替代可以先于 Manufacturing Autonomy

smartphone 与部分 consumer computing 更容易形成完整国内链条，因为这一层可以依托本土 SoC、foundry、LPDDR/NAND、packaging、device manufacturing、operating system/application ecosystem 与大型国内需求。

TSMC 2025 platform mix 仍显示 smartphone 占全年 platform revenue **29%**，而 HPC 为 **58%**。[^1]这说明消费计算仍是重要市场，但 frontier AI 与 smartphone 已经在同一先进制造体系中竞争不同资源。

### 2.1 Shipment Scale 已经不是单一厂商问题

Counterpoint Research 的 2026Q1 global smartphone AP-SoC shipment share 显示：[^2]

- UNISOC：**14%**；
- HiSilicon：**4%**。

因此，如果“规模”按实际 smartphone SoC shipment 口径衡量，国产供应并不只有华为一家。

Huawei / HiSilicon 的独特优势更适合描述为：**高端自有终端 + 自研 SoC + 自有软件/生态的 vertical closed loop 更成熟**，而不是“唯一有量”。

Xiaomi 也已经跨过纯 demo 阶段。Xinhua 2025-05 报道 XRing O1 已进入 mass production 并搭载 Xiaomi 15S Pro / Pad 7 Ultra；[^3] Reuters 2026-08 又报道 O1 已覆盖 **超过 1M devices**，新一代 O3 继续采用 TSMC 3 nm，首发产品预计 200k–300k units。[^4]

这意味着“Xiaomi 只有20–30万片边角料、只是品牌秀”不能作为事实层。更准确的判断是：

> **Xiaomi 已经形成真实量产，但 multi-generation scale、modem/system integration、foundry dependency 与长期 shipment share 仍需要继续验证。**

UNISOC 则代表另一种 commercial loop：它在大众/入门与 entry-5G 市场拥有更大的 shipment scale，但不能据此外推为 premium flagship system equivalence。

### 2.2 Design Origin 不等于 Manufacturing Closure

这里还必须增加一个供应链口径约束：

> **“国产设计”不等于“制造自主”，shipment share 也不能替代 foundry continuity。**

UNISOC 是 fabless 设计公司。其公开产品资料能够确认多款当前 5G SoC 使用 **6nm EUV**；其中 UNISOC 官方 M6870 产品页更直接标注为 **TSMC 6nm EUV**。[^19] UNISOC / Spreadtrum 与 TSMC 的代工合作也有长期一手记录：TSMC 2011 年即披露 Spreadtrum 40nm baseband 在其 Fab 12 进入 initial production。[^20]

但这些证据并不支持进一步扩写成“UNISOC 全部产品均由 TSMC 生产”。例如，T9100 官方页面确认的是 **6nm process**，并未在该产品页直接披露 foundry identity。[^21] 因此，当前能够安全写下的判断是：

> **UNISOC 的 14% smartphone AP-SoC shipment share 证明了真实商业设计与出货规模，但不能证明 domestic foundry closure；其公开产品与历史供应链证据显示 TSMC 是重要 manufacturing dependency，foundry continuity 必须作为独立 gate 评估。**

Xiaomi XRing 的情况更直接：本章已经引用的 Reuters 来源明确指出其量产与 TSMC 制造合作。[^4] 因此，Xiaomi 的自研 SoC 同样属于“design capability 已成立，但 manufacturing autonomy 不能由此推出”的案例。

这一修正也改变了消费计算层的判别方式。未来任何“国产 SoC 份额”都至少需要拆成：

1. **design origin**；
2. **foundry identity / process continuity**；
3. **packaging / memory dependency**；
4. **是否受外部许可、服务或设备规则影响**；
5. **multi-generation manufacturing continuity**。

美国 BIS 2025-01 的 foundry due-diligence rule 确实扩大了 front-end foundry / packaging 对**特定 advanced-computing IC** 的许可与尽调要求，并引入 Approved / Authorized IC Designer 机制；规则中的 advanced-node 定义包含 16/14nm 及以下或 non-planar logic。[^22] 但这不能简化成“所有 16/14nm 以下、由中国公司设计的 smartphone SoC 一律需要许可”。是否触发许可取决于 EAR 分类、性能/晶体管等规则条件、设计者身份、目的地与交易结构。

所以对 UNISOC / Xiaomi 最准确的风险表述是：

> **外部 foundry dependence 提高了供应链连续性与政策暴露度，但不能在没有逐产品 EAR classification / licensing evidence 的情况下，把这种依赖直接写成已发生或必然发生的断供。**

因此，消费端的平行供给能力应被评价为一个独立层级，而不是拿来证明或否定 frontier AI closure。

## 3. PC / Workstation：Compatibility 与 Scale 才是 Binding Test

PC、workstation 与 general computing 需要同时解决 CPU/GPU、DDR5、专业软件、driver/tooling、desktop ecosystem 与 developer compatibility。硬件存在替代并不等于使用体验、性能和软件栈已经等价。

把国产 PC CPU/GPU segment 描述成“一片空白”同样不准确。

龙芯当前公开产品线包含面向 desktop/general-purpose 的 3A6000、3B6000 等 CPU；[^5] Moore Threads 公开销售 MTT S80 gaming GPU。[^6]

这些事实证明**产品存在且能形成真实 PC/graphics deployment**。

但它们不能证明：

- mainstream consumer-PC shipment share 已接近 Intel/AMD/NVIDIA；
- professional software / game compatibility 已达到同等级覆盖；
- performance/watt、driver maturity、developer ecosystem 与 supply scale 已全面等价。

更准确的描述是：**真实产品与国内生态已经存在，但主流规模、兼容性和系统经济性仍然是 closure barriers。**

## 4. Frontier AI 是 System-Closure Problem

frontier AI 需要多个 advanced layer 同时成立：

- advanced accelerator；
- HBM-class memory；
- advanced packaging；
- high-speed scale-up / scale-out interconnect；
- compiler/runtime；
- distributed training；
- rack-scale deployment；
- data-center power。

任一单点突破都不足以自动形成等价系统。有 accelerator 但没有 HBM，有 hardware 但 migration cost 很高，有 cluster 但 utilization 与 interconnect scaling 不足，都可能使 system-level competitiveness 显著下降。

因此，“某颗芯片能运行模型”不能作为 frontier substitution 的充分条件。

## 5. Ascend / CANN 应按 System Completeness 而不是单卡 Peak Metric 判断

国内 accelerator stack 的核心价值，不在某一代单卡 peak FLOPS，而在于是否形成 compiler/runtime、framework adaptation、distributed communication、deployment tooling 与 production workload 反馈的闭环。

评估这一层应优先观察：

- large-cluster utilization；
- compiler stability；
- operator completeness；
- framework compatibility；
- failure recovery；
- multi-generation compatibility；
- production deployment scale。

由于部分 Ascend/CANN 具体性能和迁移效率数字目前主要来自二手材料，本章不把未逐项核验的一手缺失参数写成已确认事实。

## 6. Memory：Conventional Scale 与 Frontier HBM 是两个 Threshold

长鑫科技的公开招股/注册材料披露 DDR 与 LPDDR 产品；公司随后已于 **2026-07-27** 在上交所科创板上市交易。[^7][^18] 对相关公开材料检索 `HBM` 与“高带宽内存”未见可用于确认量产产品线的披露，因此现有证据只支持一个窄结论：

> **现有公开发行与产品材料不足以确认已形成可规模交付的 HBM 产品线。**

这不证明企业不存在任何 HBM R&D；但要把 HBM 从研发可能性升级为 frontier system supply，仍必须看到 official product、customer qualification、volume production、bandwidth/capacity 与 packaging integration。上市改变的是资本市场与融资阶段，不会自动跨越 HBM、advanced packaging 或 frontier-system closure 的技术门槛。

同一注册稿还必须严格区分 project investment 与 planned offering proceeds：三项项目总投资与拟使用募集资金不是同一分母；其中 DRAM 技术升级项目 **RMB18.0B 总投资**与 **RMB13.0B 拟使用募集资金**不得混用。

因此，DDR/LPDDR 供给增强与 HBM-class memory closure 必须分开分析。

### 6.1 Conventional DRAM / NAND 可以先于 HBM Closure 改善

长鑫官方当前产品页披露 DDR5 颗粒最高 **8000 Mbps**、16Gb/24Gb，并覆盖 RDIMM/MRDIMM 等 server/workstation/PC 模组；[^8]这确认的是产品规格能力，本身不构成出货规模证据；供给规模判断见 §6.2 的招股书 / Omdia 口径。

长江存储官方则确认自身是 3D NAND IDM，并披露 Gen5/Xtacking 4.0 相关产品体系以及 raw NAND、embedded memory、client SSD 与 enterprise SSD 产品线。[^9]

这两条事实说明：

> **consumer/general-purpose memory resilience 可以提高，而不需要先完成 frontier HBM closure。**

普通 DRAM 与 NAND 的 memory-cell front-end manufacturing 并不等同于台积电 leading-edge logic foundry；但 HBM-class AI system 会重新引入 advanced logic / base logic die、advanced packaging 与 accelerator integration 等更高门槛。Micron 就曾公开披露 HBM4E 的 base logic die 与 TSMC 合作制造。[^10]

所以“普通内存可以绕开台积电”与“frontier AI memory stack 不受台积电影响”是两个完全不同的命题。

### 6.2 Revenue Share 与 Shipment Share 必须保持不同分母

长鑫公开招股材料引用 Omdia 的可审计口径是：按 **2025Q2 DRAM 销售额**测算，长鑫全球市场份额约 **3.97%**，位列全球第四。[^11]

因此，“长鑫已经有 8% 全球 DRAM 份额”不能进入事实层。

长江存储的最新机构口径则不同。Counterpoint Research 2026Q2 Memory & Storage Tracker 给出：YMTC 以约 **14% NAND shipment share** 进入全球前三；[^12] 同一机构 2026Q1 的 **13%** 则是 NAND **revenue share**。[^13]

这两个数字不能拼成同一时间序列，因为分母不同。

它们真正支持的是：

> **中国 conventional DRAM / NAND 的全球供给存在感已经明显上升，但份额增长本身仍不能证明 HBM、leading-edge logic 或 frontier-system closure。**

关于“2027 产能翻倍”“三期明确达到某个月产量”的说法，如果只来自其他公司的招股书转引、媒体或供应链估算，只能放在 B/C 级背景，不进入本章 A 级事实层。

### 6.3 Storage Resilience 不能只看 NAND

AI data-center storage 还包含 nearline HDD。公开产业研究显示，全球 nearline / mass-capacity HDD 仍高度集中于 Seagate、Western Digital 与 Toshiba。

因此，“国产 NAND / SSD 能力增强”不能自动写成“整个 storage stack 已经国产闭环”。

同时，AI 并没有简单淘汰 HDD：mass-capacity / cold-storage demand 仍然存在，只是 QLC nearline SSD 正在部分 workload 上加速替代。

## 7. Foundry Revenue Share 不是 Frontier-AI Capability Metric

TrendForce 2026 Q1 foundry revenue share 约为：[^14]

**Table 17.1 — 2026 Q1 全球 foundry revenue share（TrendForce）**

| Foundry | Revenue share |
|---|---:|
| TSMC | 72% |
| Samsung Foundry (excluding System LSI) | 6.5% |
| SMIC | 5.1% |

**Source:** TrendForce, 2026-06-12.[^14]  
**Note:** 该表为 foundry revenue share，不是 advanced-node yield、AI wafer capacity 或 frontier-system capability。

这些是 foundry **revenue share**，不是先进节点良率、AI wafer capacity 或 frontier-system delivery capability。

中国要形成 frontier AI parallel supply，不只需要 logic die，还需要 advanced packaging、substrate、HBM integration、yield、high-volume qualification 与 power。节点追赶是必要条件之一，不是完整系统本身。

## 8. Algorithmic Efficiency 可以缓解硬件约束，但不能替代 Stack Closure

DeepSeek-V3 Technical Report 说明，算法与架构设计可以显著降低单位 capability 对硬件的需求。论文给出的 **pre-training 为 2.664M H800 GPU-hours**，完整正式训练为 **2.788M H800 GPU-hours**；[^15]按论文采用的 US$2/GPU-hour 假设，**US$5.576M 对应完整正式训练**，不等于完整研发成本。

这一案例支持的机制是：在 supply-constrained environment 中，sparse architecture、memory efficiency、routing、quantization 与 scheduling 可以提高 effective compute productivity。

它不支持“物理供给已经不重要”，也不支持“任何受限系统都能复制同样成本”。算法效率是杠杆，不是对 HBM、packaging、interconnect 和 power 的替代品。

## 8A. System Engineering 可以补偿 Manufacturing Disadvantage，但补偿本身有成本

制造节点上的劣势，并不会一比一转化成 system-output 劣势。

受限技术栈可以通过以下路径做部分补偿：

- sparsity、quantization、routing 与 memory-efficiency；
- 使用更多 die / accelerator；
- chiplet、board-level、rack-level topology；
- 更激进的 compiler / runtime co-design；
- workload-specific scheduling 与 communication optimization；
- 围绕 captive workload 做更窄的 specialization。

这是一个真实竞争轴，因此不能把 process-node position 写成决定 system outcome 的唯一变量。

但 compensation 不是免费的。更多 device、更大 topology 或更复杂软件会把压力转移到其他 denominator：

- logic wafer input；
- package starts / integration complexity；
- memory capacity 与 bandwidth；
- interconnect / switch count；
- power 与 cooling；
- failure domain 与 operations complexity；
- 每单位 delivered workload 所需资本。

所以真正的 Test 不是：

> “谁的节点更先进？”

也不是：

> “软件能不能抹掉制程差距？”

而是：

> **System Engineering 能否把现有制造基础转化为有竞争力的 production-workload economics，而不是仅仅把瓶颈从 logic 移到 memory、packaging、networking、power、reliability 或 capital？**

由于这些资源使用不同物理单位，它们不能被压成一个 synthetic “补偿分数”。更稳健的比较应分别观察 target workload 的 throughput / cost、power per verified output、qualified package availability、memory intensity、utilization 与 multi-generation continuity。

因此，工程补偿应被赋予更高权重，但边界必须保持清楚：

> **它可以压缩 hardware disadvantage，不能替代 system closure。**

---

## 9. Domestic Workload 构成 Parallel Stack 的 Iteration Loop

一个 parallel stack 不必先征服全球 developer 才能产生价值。只要拥有足够大的内部 workload，就可以通过真实生产环境积累 compiler feedback、deployment experience、failure recovery、operator coverage 和 utilization 数据。

这一逻辑与 hyperscaler custom silicon 类似：**大规模 captive workload 可以先支持一套较窄但完整的 system stack，再决定是否向更广泛外部生态扩展。**

因此，判断中国栈长期进展，不能只看 benchmark，还要看 production workload 的规模与持续性。

## 10. Export Control 同时作用于 Manufacturing Continuity

出口限制在短期会提高先进硬件获取成本并降低 frontier cluster deployment speed；长期则会提高 domestic substitution incentive、local software/hardware integration 与 parallel ecosystem 的战略价值。

更上游还要单独看 semiconductor manufacturing equipment / software / service。ASML 的公开说明确认：EUV 对中国已受限制，最先进 immersion DUV 需要出口许可，后续规则还扩大到部分 advanced manufacturing technology、metrology 与 software。[^16][^17]

这不等于“国内所有 memory fab 会因为断供立刻停产”，但它说明：

> **domestic memory capacity growth ≠ upstream manufacturing autonomy**

新增产能能否 ramp、工艺能否升级、既有设备能否长期维护，仍要看关键设备、软件许可、备件、field service 与材料 qualification 的连续性。

因此，export control 不是一个单向变量。它可能同时扩大短期性能/规模差距，并强化长期平行体系建设动机。最终结果取决于 R&D efficiency、capital allocation、ecosystem adoption 与 supply scaling，而不是政策本身自动决定。

## 11. 两级 Closure Test

此前如果把所有关键层都要求“国内完全闭环”之后，才承认存在 frontier parallel stack，会把两个不同问题混在一起：

1. **Production-Grade Parallel Stack**：一套替代系统能否在真实生产环境中稳定运行；
2. **Autonomous Frontier Closure**：这套系统能否在关键外部供给受限时仍持续扩张、升级和迭代。

第一层不要求所有器件、设备和材料都来自国内；第二层才要求更高程度的 upstream continuity。

### 11.1 Production-Grade Parallel Stack 的七个 Gate

1. accelerator / compute 可规模交付；
2. HBM-class 或等价 memory subsystem 能满足目标 workload；
3. advanced packaging / integration 可规模交付；
4. high-speed scale-up / scale-out interconnect 可支撑目标集群；
5. compiler/runtime 与 framework migration cost 可接受；
6. frontier / high-value production workload 能稳定运行并形成持续反馈；
7. system utilization、power、reliability 与 cost economics 可持续。

满足这些条件，才可以把“有国产产品”升级为“存在 production-grade frontier parallel system”。

### 11.2 Autonomous Frontier Closure 还需要两个额外 Gate

8. **advanced manufacturing continuity**：advanced logic、关键 equipment、software、materials、spares、field service 与 process upgrade 能持续获得或替代；
9. **infrastructure / capital continuity**：HBM、packaging、LPS/power 与长期资本能够支持多代规模扩张，而不是只完成一次性 cluster deployment。

因此：

> **production-grade substitution ≠ full technological autonomy**

这一区分可以避免两个相反错误：既不能因为仍有进口依赖就否认真实替代系统，也不能因为系统已经能运行，就宣布所有 frontier critical layers 已经自主闭环。

## 12. 为什么 Partial Closure 已经影响全球竞争

如果中国 parallel stack 在 advanced logic、HBM、packaging、interconnect 与 software 上同时规模化，它不会只是“替代进口”，还会形成第二个大型资源重力中心：新的 foundry demand、memory demand、packaging demand、power demand 与长期资本承诺会进入全球/区域资源分配。

目前公开证据尚不足以证明这一第二个 frontier resource center 已经达到与全球主栈等价的完整规模。长鑫已经进入公开资本市场并扩大 conventional DRAM 产业化能力，但这不能替代 HBM-class memory、advanced packaging 与其他 frontier layers 的独立验证；SMIC 5.1% 也只是 foundry revenue share，而非 frontier capability。

因此，当前更准确的状态是：**中国已经跨过“没有替代系统”的阶段，frontier parallel stack 已出现真实迭代与部分 production deployment；但按本章七个 Production-Grade Gate，公开证据尚不足以确认完整 production-grade frontier parallel stack 已经闭合。Autonomous Frontier Closure 的证据门槛更高，目前同样未满足。**

## 13. Current Read 与 Falsification

截至 2026 年 8 月：

- smartphone / consumer computing：平行供给能力较强；
- PC / workstation：替代能力扩大，但软件与专业 workload 兼容仍决定闭环程度；
- frontier AI：已经存在真实、持续发展的 accelerator/software parallel stack，但 HBM、advanced packaging、interconnect、software migration、power 与 scale 仍需同时验证。

如果未来出现以下一手信号，应上调 **production-grade parallel stack** 判断：公开 HBM-class / equivalent memory subsystem、可复核的大集群 utilization 与 frontier workload、advanced-packaging 规模化交付、多代 compiler/runtime 兼容，以及稳定 system economics。

若同时出现 equipment/material/service continuity、关键制造工艺持续升级和多代基础设施扩张能力，才应进一步上调 **autonomous frontier closure** 判断。

反过来，如果 production workload 仍需要高迁移成本、关键 memory/packaging 不能规模化，或 upstream continuity 长期无法跨代维持，则不应把“有国内技术栈”升级成完整 frontier closure。

## References

[^1]: TSMC, 4Q25 Presentation / 2025 full-year platform mix, HPC 58%, smartphone 29%, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
[^2]: Counterpoint Research, 2026 Q1 smartphone AP-SoC shipment share, UNISOC 14%, HiSilicon 4%, https://counterpointresearch.com/en/insights/global-smartphone-apsoc-market-share-quarterly
[^3]: Xinhua, 2025-05-22, Xiaomi XRing O1 entered mass production, https://english.news.cn/20250522/bca3bd53dab946d88696b0fb1625231d/c.html
[^4]: Reuters, 2026-08-24, XRing O1 device scale and O3 production plan, https://www.reuters.com/world/china/xiaomi-launches-new-xring-chip-partners-with-tsmc-production-sources-say-2026-08-24/
[^5]: Loongson, official CPU product line, https://www.loongson.cn/product/list?id=4
[^6]: Moore Threads, MTT S80 official product page, https://en.mthreads.com/product/S80
[^7]: CXMT, STAR Market registration prospectus, 2026-05-27, Shanghai Stock Exchange, https://static.sse.com.cn/stock/disclosure/announcement/c/202605/002170_20260527_23QQ.pdf ; earlier prospectus / stable fallback, 2025-12-30, https://static.sse.com.cn/stock/disclosure/announcement/c/202512/002170_20251230_B8QS.pdf
[^8]: CXMT, official DDR5 product page, https://www.cxmt.com/en/product.html
[^9]: YMTC, company profile and product portfolio, https://www.ymtc.com/en/aboutus.html ; https://www.ymtc.com/en/buslist.html?cat=35
[^10]: Micron Technology, investor material on HBM4E base logic die partnership with TSMC, https://investors.micron.com/static-files/5ea95475-639b-4cfc-91fd-b9b4a2bb5e63
[^11]: CXMT prospectus / Omdia, 2025 Q2 DRAM revenue share 3.97%, global #4, https://static.sse.com.cn/stock/disclosure/announcement/c/202512/002170_20251230_B8QS.pdf
[^12]: Counterpoint Research, 2026 Q2, YMTC 14% NAND shipment share, https://counterpointresearch.com/en/insights/server-led-essds-hit-48-percent-of-nand-shipments
[^13]: Counterpoint Research, 2026 Q1, YMTC 13% NAND revenue share, https://counterpointresearch.com/en/insights/global-nand-memory-market-share
[^14]: TrendForce, 2026-06-12, 1Q26 foundry revenue shares, https://www.trendforce.com/presscenter/news/20260612-13095.html
[^15]: DeepSeek-AI, “DeepSeek-V3 Technical Report,” https://arxiv.org/abs/2412.19437
[^16]: ASML, 2023 statement on Dutch export-control regulations, https://www.asml.com/en/news/press-releases/2023/statement-regarding-export-control-regulations-dutch-government
[^17]: ASML, 2024 statement on updated export restrictions covering additional advanced manufacturing technologies, metrology and software, https://www.asml.com/en/news/press-releases/2024/asml-expects-impact-of-updated-export-restrictions-to-fall-within-outlook-for-2025

[^18]: Shanghai Stock Exchange, listing announcement for CXMT (688825), 2026-07-24; trading commenced 2026-07-27, https://www.sse.com.cn/disclosure/announcement/listing/ipo/c/c_20260724_10826610.shtml


[^19]: UNISOC, M6870 official product page, explicitly listing TSMC 6nm EUV, https://www.unisoc.com/en/solution/IDMetaverseUS/M6870
[^20]: TSMC / Spreadtrum, 2011-01-27, first commercialized 40nm TD-SCDMA baseband processor produced at TSMC Fab 12, https://pr.tsmc.com/english/news/1655
[^21]: UNISOC, T9100 official product page, 6nm process specification; the page does not itself identify the foundry, https://www.unisoc.com/en/product/SmartPhoneUS/T9100
[^22]: U.S. Bureau of Industry and Security, 2025-01-15, foundry due-diligence / advanced-computing IC controls and Approved / Authorized IC Designer framework, https://www.bis.gov/press-release/commerce-strengthens-restrictions-advanced-computing-semiconductors-enhance-foundry-due-diligence-prevent
