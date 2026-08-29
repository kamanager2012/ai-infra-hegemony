# Part I · 第1章：执行摘要与未来十年核心判断

## 1. 执行判断：AI 正在重构产业资源配置，而不只是扩大算力市场

截至 **2026 年 8 月 28 日**，AI 产业最重要的变化已经不再只是 GPU 销量增长，而是**全球先进半导体、存储、封装、数据中心、电力与资本的边际配置逻辑正在被重新排序**。

本报告的核心判断可以压缩为六点：

1. **竞争单位已经从单颗芯片上移到完整 system stack。** 决定竞争力的不再只是 accelerator 性能，而是 advanced logic、HBM、advanced packaging、interconnect、compiler/runtime、rack/pod、data center、power 与真实 workload 能否形成稳定闭环。
2. **AI/HPC 正在改变“下一美元资本投向哪里”。** 当 AI workload 具有更高支付能力、更长订单周期和更强资本回报预期时，新增投资与稀缺资源更容易向 AI infrastructure 倾斜。
3. **传统终端承受的不是“全球总产能”变化，而是优先分配后的 residual capacity。** 因此，总供给增长与 smartphone、PC、汽车、工业等市场继续承受价格或配置压力可以同时成立。
4. **NVIDIA 的优势仍然很强，但竞争已经从“GPU vs ASIC”升级为“system stack vs system stack”。** Google、AWS、Microsoft、Meta 的 custom systems 正在形成第二类完整路线。
5. **基础设施的长期价值最终必须由可验证工作流产出完成需求侧闭环。** Agent-Native Software、Physical AI 与企业自动化能否把 Compute 转化为稳定、可验收、可收费的经济结果，将决定 utilization、monetization 与资本回收。
6. **未来并不是单一的“继续繁荣”或“泡沫破裂”。** 真正决定 2026–2036 产业路径的是 supply elasticity、system substitution、utilization、power、capital discipline、workload economics 与中国 parallel stack 的 frontier closure。

截至当前，公开事实更符合 **S2 — Baseline Concentration**：少数 system platform 与 scarce-layer supplier 保持强经济性，替代路线正在发展，但尚未消除 HBM、advanced packaging、power 与迁移成本等关键约束。

---

## 2. 第一层变化：AI 基础设施已经从“芯片采购”变成“系统工程”

NVIDIA GB200 NVL72 官方规格包含 **72 Blackwell GPU、36 Grace CPU、13.4 TB HBM3E 与 17 TB LPDDR5X**。高端 AI infrastructure 的商业交付对象已经从 accelerator card 上移到 compute、memory、interconnect、software 与 rack architecture 的组合。[^1]

这一变化解释了为什么单颗芯片 benchmark 越来越不足以解释产业竞争。真正决定 system economics 的，是：

- 单位 workload 的有效吞吐与成本；
- software / runtime 的迁移成本；
- memory 与 interconnect 的系统效率；
- rack-level deployment 与 power density；
- 供应链能否稳定获得 advanced logic、HBM 与 packaging；
- 最终 utilization 是否足以覆盖资本成本。

NVIDIA FY27 Q2 披露 Revenue **US$96.221B**、Data Center revenue **US$89.0B**、GAAP gross margin **75.0%**、GAAP operating income **US$63.734B**，并表示 Vera Rubin 已进入 full production。[^2] 这些数据说明当前领先平台仍具有极强 seller-side economics，但高利润本身并不能证明永久垄断；真正需要判断的是这些利润能否持续转化为下一代 system、supply 与 installed-base 优势。

与此同时，NVIDIA manufacturing, supply and capacity commitments 从 2026-01-25 的 **US$95.2B** 增至 2026-07-26 的 **US$279B**。[^3] 这说明前置供应承诺显著扩大，但公开文件没有披露 supplier-level split，因此不能把 US$279B 直接解释成 TSMC、CoWoS 或某一家 HBM supplier 的确定订单。

---

## 3. 第二层变化：半导体正在形成 Two-Speed Semiconductor Economy

AI infrastructure 与传统终端仍然共享大量上游资源，但两类需求的经济属性已经明显分化。

AI/HPC 的典型特征是：

- 更高的价格承受能力；
- 更长的订单与 capacity-commitment 周期；
- 更高的单机与单柜 BOM；
- 更强的融资与预付款能力；
- 对先进制程、HBM、advanced packaging 与 power 的集中需求。

传统 smartphone、PC、汽车与工业终端则更受零售价格、BOM、换机周期和终端需求弹性约束。

TSMC 2025 年 HPC platform 占全年 net revenue **58%**，smartphone 占 **29%**；到 2026 Q2，HPC platform revenue 占季度营收 **66%**，smartphone 为 **22%**，advanced technologies（7 nm 及以下）占 wafer revenue **77%**。[^4][^5] 这些是 revenue mix，不能直接换算成 customer-level wafer allocation，但它们足以说明：HPC 已成为先进制造资本形成的重要边际驱动力之一。

因此，本报告把这一结构称为 **Two-Speed Semiconductor Economy**：

> **AI Infrastructure Economy 与 Traditional Device Economy 共享部分上游资源，却具有不同的价格承受能力、订单期限与资本形成能力。真正改变产业的，不只是“谁买了更多芯片”，而是谁更能决定新增产能为了什么需求而建设。**

---

## 4. 第三层变化：稀缺正在从单一芯片扩展为多个独立物理池

### 4.1 HBM：bit share 低估了制造资源占用

Micron 一手披露，在 **same technology node / same number of bits** 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。[^6]

TrendForce 预计 HBM + RDIMM 约占 **2026 年 DRAM bit supply 的 51%**。[^7] 该数字是机构预测，不是 full-year actual。两条证据联合起来的重要含义不是“H​​BM 占了多少市场份额”，而是：

> **高价值 AI/server memory 对制造资源的吸收强度，可能显著高于单纯 bit share 所显示的程度。**

### 4.2 Advanced Packaging：先进逻辑有产能并不等于系统能够交付

TSMC 在 4Q24 表示 advanced packaging capacity “very tight”，2026 Q2 又明确表示 packaging tightness 正在限制客户增长。[^8]

因此，先进节点 wafer capacity 与可交付 AI system capacity 不能画等号。即使某一层扩产，bottleneck 也可能转移到 packaging、memory、networking 或 power。

### 4.3 Power：从设备约束升级为基础设施约束

NVIDIA DGX GB200 hardware guide 给出的 rack power 约为 **120 kW**。与此同时，835 MW 级核电重启、最高 1.92 GW 的长期 PPA，以及数百 MW 级长期电源开发计划，说明 Time-to-Power、grid connection、substation、firm power 与 permitting 已经进入 AI system delivery 的核心约束集合。[^9]

分析中必须严格区分 **Contracted / Secured / Permitted / Construction / Energized / Utilized**。合同或 secured capacity 不能写成已经上电，更不能写成已经被有效 workload 使用。

2026-08-17 的 PORTS-Pike 项目进一步说明，稀缺正在从单纯“电力容量”上移到 **land + power + shell（LPS）** 的组合交付。NVIDIA 披露通过对 SB Energy 提供 credit support 锁定初始 **4.25 IT-GW** 设计容量，OpenAI 为客户，项目计划从 2028 年开始分阶段上线。[^12] 这不是当前 energized load，但它证明 system platform 已开始把资源协调能力延伸到数据中心物理基础设施。

---

## 5. 第四层变化：真正值得观察的是 Non-AI Residual Capacity，而不是总产能

传统行业能够获得多少资源，不取决于全球总供给本身，而取决于优先需求吸收之后剩余多少有效供给：

```text
NonAI_Residual(t)
= Effective_Supply(t)
- AI_Absorption(t)
- Other_Priority_Demand(t)
```

这个框架能够解释一个看似矛盾的现象：

> **全球 wafer、DRAM 或 packaging capacity 可以继续增长，但 smartphone、PC、汽车或工业客户仍然可能面对更高价格、更低 allocation 或更慢规格升级。**

因此，AI 对传统产业的影响通常不是“直接全面占用产能”，而是通过 **product-mix reallocation、quantity assurance、pricing power 与 capital priority** 改变边际供给。

这也是为什么低利润、低议价、短订单客户通常比大型 anchor buyer 更容易承受压力。

---

## 6. 第五层变化：Hyperscaler 正在从芯片自研走向第二类 System Stack

Google Ironwood、AWS Trainium3 UltraServers、Microsoft Maia 200 与 Meta MTIA 300 显示，hyperscaler 的竞争已经从“有没有自研 ASIC”上移到 accelerator、compiler/runtime、interconnect、rack/pod 与 captive workload 的 system-stack competition。[^10]

这会产生两个同时存在、方向不同的效果：

1. **Platform-profit diversion**：部分 workload 不再支付完整的外部平台 economics；
2. **Upstream resource competition**：custom systems 自身仍然需要 advanced logic、HBM、packaging 与 power。

因此，“custom silicon 增长”并不自动意味着 NVIDIA 失去产业地位，也不自动意味着上游资源宽松。真正需要观察的是：

- production workload share；
- migration cost；
- system utilization；
- external adoption；
- software portability；
- 是否减少对同一批 scarce layers 的竞争。

---

## 7. 中国：已经形成真实 Parallel Stack，但不能用一个“国产化率”判断

中国已经形成持续发展的 accelerator/software parallel stack，并在 consumer computing、DRAM/NAND、部分通用计算与本土软件生态上形成更强的平行供给能力。[^11]

但 frontier AI 的等价闭环需要多个层级同时成立：

- advanced logic；
- HBM-class memory；
- advanced packaging；
- high-speed interconnect；
- compiler/runtime；
- frontier workload；
- large-scale system operation；
- power；
- equipment / materials / software continuity。

因此，本报告既不采用“已经全面追平”，也不采用“完全没有替代能力”的极端叙述。

更准确的判断需要分成两个层级：

> **中国已经跨过“没有替代系统”的阶段，正在形成 production-grade parallel stack；但公开证据尚不足以证明所有关键 upstream / infrastructure layers 都已经实现 autonomous frontier closure。**

前者回答“系统能不能在真实 production workload 中稳定运行”，后者回答“在关键外部供给受限时，能否跨代持续扩张和迭代”。

因此，中国 AI infrastructure 的核心问题不再只是“有没有一颗国产 GPU”，而是 production-grade system、upstream manufacturing continuity 与 multi-generation scaling 能否同时成立。

---

## 8. 资本周期：真正的风险不是 CapEx 大，而是资产久期与利用率错配

Cloud CapEx、system-vendor revenue、foundry revenue、memory revenue 与 power/data-center investment 会在产业链不同账本中重复出现，因此不能机械相加成“全球 AI 总投入”。

AI infrastructure 的资本周期存在明显的 **duration mismatch**：

- accelerator / server：技术周期短；
- network / cooling：中周期；
- data-center shell：长周期；
- grid / substation / generation：更长周期；
- workload monetization：不确定且取决于真实业务采用。

因此，判断是否进入 **S4 — Capital Hard Landing**，不能只看 CapEx 绝对规模，而应同时观察五类信号：

- **Accounting**：impairment、write-down、accelerated depreciation；
- **Utilization / Revenue**：有效利用率、单位收入、workflow monetization；
- **Market Clearing**：lease rate、二手价格、lead time、inventory；
- **Forward Commitment**：CapEx guidance、supply commitments、Anchor Buyer contracts；
- **Demand Quality / Financing**：customer cash generation、third-party risk capital、supplier equity / credit support 与 refinancing dependency。

截至 2026 年 8 月，公开事实更符合：

> **高强度资本扩张仍在持续，但对 utilization 与 monetization 的要求正在明显提高。**

资本来源也在变化。NVIDIA 2026-08-10 宣布与 Apollo、BlackRock、Blackstone、Brookfield、Goldman Sachs、KKR 建立独立 compute financing platforms，目标是**随时间动员超过 US$500B third-party capital**；公司同时明确这些合作仍取决于 final agreements。[^13] 因此，这一数字应作为 capital-mobilization target，而不是已经 funded / deployed 的资本。

这与“全行业资本硬着陆已经发生”是两个不同判断。

---

## 9. 2026–2036：未来由四种结构状态而不是一个单点预测描述

**Table 1.1 — AI 基础设施四类标准情景**

| 情景 | 核心结构 |
|---|---|
| S1 — Competitive Expansion | supply elasticity 与 interoperability 上升，多 system stack 共存，value capture 更分散 |
| S2 — Baseline Concentration | 少数 system platform 与 scarce-layer supplier 保持强经济性，同时替代路线持续发展 |
| S3 — Resource Hegemony | 多个 scarce layers 与 switching cost 同时强化，后来者复制完整 infrastructure stack 的门槛上升 |
| S4 — Capital Hard Landing | utilization、clearing price、CapEx/commitments、accounting losses 与 demand-financing quality 同步恶化 |

**Source:** 本报告情景框架。  
**Note:** S1–S4 是并列条件状态，不赋固定概率，也不是必然连续阶段。

截至 2026 年 8 月，**S2 — Baseline Concentration** 是最接近当前事实组合的基准状态。

决定未来向哪一侧移动的核心变量不是一个“2036 市场份额预测”，而是：

- supply elasticity 是否改善；
- HBM / packaging / power 是否继续构成跨代约束；
- hyperscaler custom systems 是否承担更大比例的真实 production workload；
- software migration cost 是否下降；
- AI workload monetization 是否足以覆盖资本基数；
- Anchor Compute Buyer commitments 是否兑现；
- 中国 production-grade parallel stack 是否扩大，以及 autonomous frontier closure 是否跨越更多关键层；
- supplier-assisted financing 是否仍由真实 utilization / monetization 支撑。

---

## 10. 哪些事实会迫使本报告改判

以下变化应显著降低 S2/S3 的相对权重：

- leading system-platform commitments 持续下降或大规模取消；
- advanced packaging 不再被主要供应商描述为 growth constraint；
- HBM / DRAM residual supply 长期显著宽松；
- cloud custom systems 在 frontier workload 上形成低迁移成本的大规模替代；
- energized power 与 grid interconnection 大幅改善，Time-to-Power 不再造成项目差异；
- Anchor Compute Buyer commitments 大规模改期或利用不足；
- China frontier-system closure 在多个关键层获得规模化一手证据；
- formal regulatory remedy 实质性降低 proprietary-interface switching cost。

反过来，如果多个关键物理层持续短缺、Non-AI Residual Capacity 继续下降、migration cost 仍高、forward commitments 继续扩大，则 S3 — Resource Hegemony 的相对权重会上升。

---

## 11. 阅读本报告时最重要的边界

本报告所有判断始终区分：

- **Fact**：已经发生并可公开验证；
- **Institutional Forecast**：机构预测；
- **Company Guidance**：公司前瞻指引；
- **Hypothesis / Scenario**：本报告条件假设；
- **Model / Stress Test**：本报告计算与压力测试。

未来判断可以明确，但不能伪装成已经发生的事实；历史事实必须保留时间、分母、单位与来源身份。

如果只阅读一章，应以本章作为本报告入口；如果需要理解任一结论的证据链、反方条件与量化边界，应继续进入对应主题章与 References。

## References

[^1]: NVIDIA, “GB200 NVL72,” official product page, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^2]: NVIDIA, “NVIDIA Announces Financial Results for Second Quarter Fiscal 2027,” 2026, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^3]: NVIDIA Corporation, Form 10-Q for quarter ended 2026-07-26, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm ; NVIDIA Corporation, FY26 Form 10-K, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
[^4]: TSMC, 4Q25 Presentation / 2025 full-year platform and technology mix, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
[^5]: TSMC, “2Q26 Quarterly Results,” platform and technology revenue mix, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^6]: Micron Technology, FY24 Q2 Prepared Remarks, 2024-03-20, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^7]: TrendForce, 2026-08-25, HBM + RDIMM 2026E DRAM bit-supply structure, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^8]: TSMC, 4Q24 Earnings Conference Transcript, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf ; TSMC, 2Q26 Earnings Conference Transcript, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^9]: NVIDIA, DGX GB200 Hardware Guide, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html ; Constellation, Crane Clean Energy Center announcement, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs ; Talen Energy, 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm ; Kairos Power / Google partnership, https://www.kairospower.com/google
[^10]: Google, “Ironwood TPU,” https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; AWS, “Amazon EC2 Trn3 UltraServers,” https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ ; Microsoft, “Maia 200,” https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ ; Meta, “MTIA 300,” https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
[^11]: CXMT public offering materials, Shanghai Stock Exchange, https://static.sse.com.cn/stock/disclosure/announcement/c/202512/002170_20251230_B8QS.pdf ; Shanghai Stock Exchange, CXMT (688825) listing announcement, trading began 2026-07-27, https://www.sse.com.cn/disclosure/announcement/listing/ipo/c/c_20260724_10826610.shtml ; Moore Threads, MTT S80 official product page, https://en.mthreads.com/product/S80 ; DeepSeek, “DeepSeek-V3 Technical Report,” https://arxiv.org/abs/2412.19437 ; TrendForce, 2026-06-12, 1Q26 foundry revenue shares, https://www.trendforce.com/presscenter/news/20260612-13095.html
[^12]: NVIDIA, “NVIDIA Guarantees SB Energy's PORTS-Pike Technology Campus in Ohio to Exclusively Host NVIDIA AI Compute,” 2026-08-17, initial 4.25 IT-GW design capacity and phased online plan beginning in 2028, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx
[^13]: NVIDIA, 2026-08-10, AI compute infrastructure financing platforms and >US$500B third-party-capital mobilization target, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Partners-With-Apollo-BlackRock-Blackstone-Brookfield-Goldman-Sachs-and-KKR-to-Establish-AI-Compute-Infrastructure-Financing-Platforms-to-Mobilize-Over-500-Billion-of-Third-Party-Capital/default.aspx
