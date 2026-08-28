# Part I · 第4章：TSMC、N2 与先进制造资源分配


## 1. 真正的竞争对象不是一个“2 nm wafer price”

frontier AI system 同时需要 leading-edge logic、HBM、advanced packaging、substrate、interconnect 与 power。node leadership 只是进入下一代 system 的必要条件之一。

所以先进制造竞争的核心不是某个市场传闻报价，而是：

> **谁能在 N2/N2P/A16 等下一代资源进入 volume production 时，稳定获得足够规模，并同时匹配 memory、packaging 与 system roadmap。**

## 2. TSMC 2025 的关键事实

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

## 3. Customer revenue share 不能换算成 wafer / node / CoWoS share

2025 largest customer 19% 与 second-largest customer 17% 是**年度收入排名口径**。[^2]

它们不能换算成 N2 wafer share、3 nm wafer share、CoWoS share、HPC wafer share 或 physical wafer count。

另一张匿名客户表才支持跨年比较：Customer A **12%→19%**、Customer B **22%→17%**（2024→2025）。[^4]annual largest/second-largest ranking 与 anonymized A/B series 回答不同问题，不能拼成同一客户的虚假轨迹。

同样，HPC 58% 是 platform revenue share，不是 wafer shipment share。

## 4. N2 的战略价值来自“增量首发资源”

N2 的意义不只是 transistor density。竞争者真正关心：

- volume production timing；
- available scale；
- yield / delivery stability；
- HBM 与 packaging 配套；
- system-level performance conversion；
- roadmap continuity。

拿到某个 node 并不自动构成 system victory。如果 memory、packaging、interconnect 或 power 缺失，完整交付仍然受限。

## 5. 真正值得跟踪的是 Incremental Capacity Access，而不是创造一个综合份额

历史 revenue share 只能说明过去收入集中度，不能直接回答下一代资源如何分配。对 N2/N2P/A16 更有价值的问题是：**哪些客户能够在量产初期持续获得足够、稳定、经过验证的增量供给。**

但这种分析必须逐层进行。advanced logic、HBM、advanced packaging 与 power 使用不同物理单位、不同供应商和不同扩产时钟，因此不应被压缩成一个综合“资源捕获率”。

更稳健的跟踪方式是分别观察：

- leading-edge node 的量产节奏与客户需求强度；
- HBM qualification 与 supply；
- advanced-packaging capacity；
- system delivery 与 utilization；
- 客户长期承诺、预付款与 roadmap visibility。

这比用 50/60/70/80% 的假设比例模拟“谁拿走多少未来产能”更适合作为正文分析。

## 6. TSMC 的资源分配不是单变量决定

先进产能 allocation 更可能同时考虑：price、committed volume、contract duration、prepayment、credit quality、utilization certainty、roadmap stability、customer diversification 与 geopolitical risk。

所以不能用“第一客户一定得到全部最好资源”的决定论。

更合理的机制是：订单规模、信用、预付款与 roadmap certainty 提高买方对新增资源的议价能力；供应商同时仍有客户多元化、长期议价权和地缘风险管理的动机。

## 7. Advanced Packaging 必须与 logic pool 分开

TSMC 一手资料已确认 advanced-packaging tightness，但 customer-level CoWoS allocation 未披露。[^5] TrendForce 对 NVIDIA 2025 CoWoS demand >60% 的估计属于 B 级机构数据。[^6]

因此，前道 logic capacity 与后道 advanced-packaging capacity 必须分别分析，不能把两者放进同一个 wafer 分母，更不能用全厂 front-end wafer shipments 直接推导可交付 AI rack 数量。

这说明“leading-edge logic available”与“complete AI system deliverable”不是同一个问题。

## 8. Samsung / SMIC 的 foundry share 不能直接等同于 frontier substitution

TrendForce 2026 Q1 foundry revenue share 约为：TSMC **72%**、Samsung Foundry **6.5%（excluding System LSI）**、SMIC **5.1%**。[^7]

这些是 revenue share，不是 frontier-AI capacity share。形成第二套可替代 supply system 还要同时验证 node performance、yield、advanced packaging、HBM ecosystem、customer qualification 与 software/system integration。

因此，“有第二家 foundry”与“有完整第二套 frontier AI supply stack”是不同命题。

## 9. 当前判断

TSMC 的战略地位来自三个同时存在的条件：leading-edge logic 领先、HPC 已成为最大 platform、advanced packaging 仍是公开确认的增长约束。

但这并不意味着 TSMC 已成为某一家 AI 客户的“专属 fab”。对未来最有解释力的变量不是某一季 customer revenue share，而是：

- N2/N2P/A16 的量产节奏与有效供给；
- 大型 AI 与 cloud-custom-system 客户对新增 leading-edge capacity 的需求强度；
- HBM / packaging 是否同步扩张；
- 第二制造体系能否在 logic + memory + packaging 上形成组合替代。

因此，先进制程的长期竞争核心不是一个“2 nm wafer price”，而是**下一代 system 所需多层资源能否在同一时间窗口内形成可交付组合。**

## References

[^1]: TSMC, 2025 Annual Report, https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^2]: Taiwan Semiconductor Manufacturing Company Limited, 2025 Form 20-F, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm
[^3]: TSMC, 4Q25 Presentation / 2025 full-year platform and technology mix, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
[^4]: TSMC, 2025 Consolidated Report, anonymized Customer A/B revenue series, https://www.sec.gov/Archives/edgar/data/1046179/000104617926000024/a2025q4consolidatedreport-.htm
[^5]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging tightness, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^6]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^7]: TrendForce, 2026-06-12, 1Q26 foundry revenue shares, https://www.trendforce.com/presscenter/news/20260612-13095.html
