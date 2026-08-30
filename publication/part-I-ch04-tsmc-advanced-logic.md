# Part I · 第4章：Advanced Logic Allocation——TSMC、N2 与下一单位 Qualified Capacity


## 1. 分析单位是 Qualified Incremental Capacity

leading-edge logic 是 frontier AI 的必要条件，但不是充分条件。真正的变量不是“谁能拿到先进节点”，而是：**谁能在需要的时间和规模上持续获得 qualified incremental capacity，并让 HBM、packaging、interconnect、power 与 software 同步完成 system conversion。**

因此先进制造真正需要回答的是：

> **谁能持续、按期获得足够 N2/N2P/A16-class qualified capacity，并避免其他 physical layer 成为新的 binding constraint？**

市场传闻中的 wafer price 回答不了这个问题。真正相关的是 volume、qualification、delivery timing、roadmap continuity 与 cross-layer readiness。

## 2. TSMC Baseline：Capacity、Node Mix 与 Platform Mix

**Table 4.1 — TSMC 2025 产能、技术与平台收入结构**

| 指标 | 2025 |
|---|---:|
| 12-inch-equivalent wafer shipments | ~15.0M |
| annual capacity | >17M |
| 3 nm wafer-revenue share | 24% |
| 5 nm | 36% |
| 7 nm | 14% |
| ≤7 nm | 74% |
| HPC platform | 58% of net revenue; +48% YoY platform growth |
| Smartphone platform | 29%; +11% YoY platform growth |
| largest / second-largest customer | 19% / 17% of annual revenue |

**Source:** TSMC 2025 Annual Report、2025 Form 20-F 与 4Q25 Presentation.[^1][^2][^3]  
**Note:** platform share 与 node share 均为 revenue-based metrics；customer revenue share 不能换算为 wafer、node 或 CoWoS allocation。

这些数字证明 HPC 已成为 TSMC 最大 platform，同时 TSMC 仍服务广泛客户。它们不支持“TSMC 已成为某一家客户专属 fab”。

## 2A. 2026 Q2：HPC 仍是 Advanced-Manufacturing Capital 的核心边际驱动之一

TSMC 2026 Q2 官方结果进一步给出当前截面：[^8]

- HPC platform revenue mix：**66%**；
- smartphone：**22%**；
- advanced technologies（7 nm 及以下）占 wafer revenue：**77%**；
- 2026 capital budget：**US$60B–64B**。

这些仍然是 revenue mix / company CapEx，不是 AI wafer allocation。

它们支持的更窄判断是：

> **HPC 已经成为 TSMC 当前先进制造资本形成的核心边际需求之一，同时公司仍在显著提高先进制程与先进封装投入。**

这强化了对“下一美元资本流向哪里”的关注，但不能被改写成：

- 66% wafer 都是 AI；
- 77% advanced-technology revenue 都属于 NVIDIA；
- US$60–64B CapEx 全部用于 AI；
- smartphone 已失去 leading-edge access。

## 3. Revenue Share 不是 Allocation Denominator

2025 largest customer 19% 与 second-largest customer 17% 是**年度收入排名口径**。[^2]

它们不能换算成 N2 wafer share、3 nm wafer share、CoWoS share、HPC wafer share 或 physical wafer count。

另一张匿名客户表才支持跨年比较：Customer A **12%→19%**、Customer B **22%→17%**（2024→2025）。[^4]annual largest/second-largest ranking 与 anonymized A/B series 回答不同问题，不能拼成同一客户的虚假轨迹。

同样，HPC 58% 是 platform revenue share，不是 wafer shipment share。

## 4. N2 的战略价值来自 Launch Access、Scale 与 Continuity

N2 的意义不只是 transistor density。竞争者真正关心：

- volume production timing；
- available scale；
- yield / delivery stability；
- HBM 与 packaging 配套；
- system-level performance conversion；
- roadmap continuity。

拿到某个 node 并不自动构成 system victory。如果 memory、packaging、interconnect 或 power 缺失，完整交付仍然受限。

## 5. Scarce-Capacity Access 必须保持 Layer-Specific

本报告不使用一个跨层百分比来概括 advanced logic、HBM、packaging、networking 与 power 的 access。

它们是不同 physical pool，必须分别判断。

真正相关的问题包括：

- qualified supplier 有多少；
- buyer 是否能按计划、按时获得数量；
- lead time 与 allocation fulfillment；
- long-term agreement / prepayment；
- delivery schedule；
- buyer credit quality；
- supply elasticity。

如果未来某一个 physical layer 出现可靠的 customer-level allocation data，可以在该层使用 percentage；但不能把这个比例外推成 full-stack “resource capture share”。

## 6. Allocation 是 Multi-Variable，不是 Rank-Deterministic

先进产能 allocation 更可能同时考虑：price、committed volume、contract duration、prepayment、credit quality、utilization certainty、roadmap stability、customer diversification 与 geopolitical risk。

所以不能用“第一客户一定得到全部最好资源”的决定论。

更合理的机制是：订单规模、信用、预付款与 roadmap certainty 提高买方对新增资源的议价能力；供应商同时仍有客户多元化、长期议价权和地缘风险管理的动机。

## 7. Packaging 是独立 Physical Pool

TSMC 一手资料已确认 advanced-packaging tightness，但 customer-level CoWoS allocation 未披露。[^5] TrendForce 对 NVIDIA 2025 CoWoS demand >60% 的估计属于 B 级机构数据。[^6]

因此，前道 logic capacity 与后道 advanced-packaging capacity 必须分别分析，不能把两者放进同一个 wafer 分母，更不能用全厂 front-end wafer shipments 直接推导可交付 AI rack 数量。

这说明“leading-edge logic available”与“complete AI system deliverable”不是同一个问题。

## 8. Foundry Share 不等于 Frontier-System Substitution

TrendForce 2026 Q1 foundry revenue share 约为：TSMC **72%**、Samsung Foundry **6.5%（excluding System LSI）**、SMIC **5.1%**。[^7]

这些是 revenue share，不是 frontier-AI capacity share。形成第二套可替代 supply system 还要同时验证 node performance、yield、advanced packaging、HBM ecosystem、customer qualification 与 software/system integration。

因此，“有第二家 foundry”与“有完整第二套 frontier AI supply stack”是不同命题。

## 9. Current Read

TSMC 当前的 strategic position 建立在三个同时存在的条件上：strong leading-edge logic、HPC 已成为最大 platform、advanced packaging 仍是公开确认的 growth constraint。

真正需要前瞻观察的，不是一季度 customer revenue share，而是：谁能够获得 incremental N2/N2P/A16-class capacity、HBM 与 packaging supply 如何变化、cloud custom silicon 如何竞争新增 capacity，以及第二套 manufacturing system 能否形成可信的 logic + packaging + memory alternative。

## 10. 什么事实会改变当前判断

应下调 TSMC leading-edge strategic leverage 的信号包括：

- 第二家 foundry 在同代节点实现可复核的大规模 external production；
- customer qualification、yield、delivery 与 advanced packaging 能形成真实替代；
- N2/N2P/A16 的 supply elasticity 明显快于需求增长；
- advanced-packaging constraint 持续消失；
- leading-edge workload 明显向其他制造体系迁移。

仅有 foundry revenue share 上升、单个技术 demo 或政策补贴，不足以证明 frontier manufacturing 已形成等价 second source。

## References

[^1]: TSMC, 2025 Annual Report, https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^2]: Taiwan Semiconductor Manufacturing Company Limited, 2025 Form 20-F, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm
[^3]: TSMC, 4Q25 Presentation / 2025 full-year platform and technology mix, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
[^4]: TSMC, 2025 Consolidated Report, anonymized Customer A/B revenue series, https://www.sec.gov/Archives/edgar/data/1046179/000104617926000024/a2025q4consolidatedreport-.htm
[^5]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging tightness, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^6]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^7]: TrendForce, 2026-06-12, 1Q26 foundry revenue shares, https://www.trendforce.com/presscenter/news/20260612-13095.html
[^8]: TSMC, 2Q26 Quarterly Results / Earnings Conference, platform mix, advanced-technology revenue mix and 2026 capital budget, https://investor.tsmc.com/english/quarterly-results/2026/q2
