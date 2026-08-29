# Phase II · Empirical Validation & Scenario Calibration

本目录是 32 章正式报告冻结后的**独立验证层**，不属于已冻结正文，也不改变 **2026-08-28** 的正式报告证据截止日。

目标不是继续润色正文，而是检验报告中最关键、但尚未被历史或实证数据校准的机制。

## 工作顺序

1. **P0-1 Historical Clearing Backtest** — 回测 Chapter 24 五类清算信号；
2. **P0-2 AI Demand Elasticity Calibration** — 用真实价格/用量变化估计需求弹性的经验区间；
3. **P0-3 Verified Workflow Economics** — 建立 cost per verified workflow outcome 的可操作度量；
4. **P0-4 Macro-Financial Transmission** — 把利率、信用、股权估值与项目资本成本接入资本周期；
5. **P1 Geopolitical Scenario Layer** — 把台海、出口管制、联盟结构变成显式情景变量；
6. **P1 Conditional Timeline** — 把 Chapter 28 的年份节点改造成条件化里程碑；
7. **P2 Downstream Empirical Chains** — 劳动、教育、Physical AI 的完整传导链。

## 冻结边界

- 本目录允许使用 2026-08-28 之后的研究方法、历史资料整理与后续观测；
- 这些内容默认是 **research-side validation**，不是 formal-report fact；
- 未完成验证前，不把结果写回 32 章正式正文；
- 若未来需要重开正文，必须明确记录重开原因、影响章节与证据边界。

## Research Authority Graph

```text
Primary / auditable evidence
        │
        ├─ 01  Historical clearing backtest
        ├─ 01A Live prospective adjudication
        ├─ 02  Demand-elasticity empirical calibration (Sol event estimated; structural coefficient unresolved)
        ├─ 03  Workflow-economics contract / Level-3 closure
        ├─ 04A Public-credit regime
        ├─ 04B Hyperscaler corporate capital state
        ├─ 04C Facility / project-finance state
        ├─ 04D Seller / sponsor support state
        ├─ 05  Geopolitical G-state classification
        ├─ 07  Downstream Labor / Education / Physical-AI evidence chains
        ├─ 09  China technical system-stack closure
        ├─ 12  Non-AI end-system response evidence
        └─ 13  Developer-distribution / vertical-foreclosure evidence
                 │
                 ├─ 11 Financing taxonomy / causal double-counting map
                 ├─ 10 Scenario aggregation / S1–S4 relevance
                 ├─ 06 Conditional timeline grammar
                 └─ 08 Cross-scenario decision rules
                          │
                          ▼
                 Formal 32-chapter report
                 only after explicit reopen
```

Authority rules:

1. **Evidence/state layers own facts.** Derived layers may summarize or interpret but must not create a competing raw-state ledger.
2. **`10` owns scenario aggregation, not underlying facts.**
3. **`06` owns conditional timeline grammar, not milestone truth.**
4. **`08` owns decision rules, not scenario state.**
5. **`11` owns financing taxonomy / anti-double-counting, while `04C/04D` own borrower/support states.**
6. **Formal-report text remains frozen unless a specific evidence-backed defect or explicit reopen is recorded.**

This graph is the maintenance contract for Phase II. New files should not be added if their role can be expressed as an existing evidence owner, taxonomy layer, aggregation layer, or decision layer.

## 当前状态

- **P0-1 Historical Clearing Backtest**：v1.0；在 B/D/G/H 四路径 + Solar recovery replay 之后，新增第二个真正独立 negative control：2019 Boeing 737 MAX / commercial aerospace。结果证明 dominant supplier 即使同时出现 production cut + delivery collapse + large accounting charge，只要 independent competitor、end demand 与行业 breadth 不同步恶化，也不能升级成 system clearing。v1.0 因此新增 **signal severity cannot substitute for causal breadth** 与 regulatory/operational-shock boundary；同时 `01A` 已升 v0.2，live prospective adjudication ledger 开始对 2026 AI infrastructure 做真正 publication-time logging，并新增 SLOOS `publication_time + survey label + economic period` 时间身份，避免季度错配；
- **P0-2 AI Demand Elasticity Calibration**：v0.8；30 天 raw panel 已完成目标覆盖审计，Terra/Luna/Sol 均为 **30/30 days observed**，rank 最差分别 30 / 17 / 32，因此 target-model top-50 censoring 已关闭。Sol 2026-08-17 50% discount 的多组 short-window adjusted specifications 给出约 **-0.43 到 -0.55** 的 OpenRouter-visible E1 event-response range；benchmark specification 约 **-0.47**（95% CI 约 **[-0.69, -0.24]**）。其中 `non-Sol market growth` 只能作为 normalization，不能视为完全外生 control；raw pre/post `-1.40` 被证明会明显混入平台整体增长。Terra/Luna 因 raw export 从 7/30 才开始，不能独立识别 7/27/7/30 初始 treatment。另发现周榜最新 bucket 与 8/24–8/28 日榜合计相差 **10.4169T**，因此撤销此前 `96.90T / 5 days` 的错误 normalization；**structural E2/E3/E4 coefficient 仍未估计**；
- **P0-3 Verified Workflow Economics**：v0.7；public Level-3 candidate audit 已完成，并新增 prospective first-party acquisition contract：固定 `workflow_id` 主键，分离 AI/tool/runtime cost、human execution/review/remediation、verification、persistence 与 realized-value ledger，同时明确 `0 ≠ N/A ≠ not measured ≠ not yet observed`。新增 stop rule：以后只有公开 same-`workflow_id` Level-3 closure、一手前瞻数据，或真正改变 verification / persistence / causal attribution 的方法学结果才允许升级；generic productivity studies 不再触发版本升级；
- **P0-4 Macro-Financial Transmission**：方法主文件继续保持 v0.18，不扩张；四个数据附录职责已收口。04A v0.3 负责 public-credit regime 与 CMDI canonical retrieval/provenance，并修正 SLOOS survey-label / economic-period 时间语义；04B v0.2 只负责 hyperscaler `Headroom → Commitment → Corporate Financing → Demand Breadth → Monetization`，并新增 longitudinal descriptive states；04C v0.2 负责 facility-level delivery / monetization / DSCR / refinancing；04D v0.2 负责 support activation / step-down。跨附录只引用，不重复维护状态表；
- **P1 Geopolitical Scenario Layer**：v0.2；新增 ownership contract：05 只负责 G1–G5 geopolitical state definitions 与 event→physical/financial transmission；China technical closure 以 09 为准，scenario aggregation 以 10 为准，正式 Chapter 30 只有显式 reopen 后才可吸收；
- **P1 Conditional Timeline**：v0.2；固定为 derived rewrite layer，只负责 `condition → milestone → contrary signal` 的 conditional grammar，不再生成/升级上游事实状态；05/09/04A–04D/10/01A 分别提供权威输入，Chapter 28 仍冻结；
- **P2 Downstream Empirical Chains**：v0.2；固定 Labor / Education / Physical AI 的 domain evidence-chain ownership，并把 P0-3 §17 明确为 workflow-economics 唯一权威 denominator；新增 stop rule，generic capability/demo/productivity evidence 不再自动触发版本升级；
- **Decision Invariants**：v0.3；十条 hard invariants 保持不变，并已修正标题编号：canonical hard set 统一为 `Hard Invariant 1–10`，历史上被降级的 executable-second-path / transferability 条目改为 `Conditional Strategy A/B`，避免“标题到 11 但总数为 10”的外部可读性歧义；
- **China System-Stack Extension**：v0.3；继续作为 research-side China technical-closure authority；本轮来源审计进一步固定 evidence hierarchy：IDC 2025H1 accelerated-server 数字明确降级为 proprietary tracker 的 secondary relay / directional evidence，不能单独关闭高影响 market-share 结论；海光信息 2025 财务依据已替换为上海证券交易所官方审计财务报表；
- **Public-Proxy Scenario Dashboard**：v0.6；新增 derived-layer ownership contract：Dashboard 只做 scenario aggregation，不再作为 04A/04B/04C/04D 的竞争性事实台账。Dashboard K 的 company/facility factual state 分别以 04B/04C 为准，Dashboard 只负责 cross-confirmation 与 S1–S4 relevance；
- **Financing Reflexivity Map**：v0.3；继续保留 2026 Support Taxonomy 与 anti-double-counting，但新增 scope contract：`11` 只负责 financing taxonomy / causal graph / reflexivity diagnostic；facility state 归 04C，support activation / funded-loss state 归 04D，live clearing adjudication 归 01A；
- **Non-AI End-System Supply Conditions**：v0.3；固定为 downstream response-evidence layer：只维护真实 procurement / BOM-margin / lead-time-EOL / qualification / cadence / substitution response，不再把 upstream AI/HPC tightness 本身当作 realized downstream transmission；Chapter 21 继续受 formal-expansion gate 约束。
- **Developer Distribution Chokepoint**：v0.3；在 transaction-status gate 基础上新增 ownership contract：13 只负责 transaction gating 与 DDC-A/B/C distribution-conduct state，`10` 负责 scenario relevance，`01A` 负责 clearing adjudication；不得由本文件单独升级成法律 monopoly/foreclosure 结论或 capital-clearing state。

## 文件索引

- [00 · External Reference Landscape](00-external-reference-landscape.md)
- [01 · Clearing Signals Backtest](01-clearing-signals-backtest.md)
  - [01A · Prospective Adjudication Ledger](01a-prospective-adjudication-ledger.md)
- [02 · Demand Elasticity Calibration](02-demand-elasticity-calibration.md)
- [03 · Verified Workflow Economics](03-verified-workflow-economics.md)
- [04 · Macro-Financial Transmission](04-macro-financial-transmission.md)
  - [04A · Public Credit & Macro-Financial Panel](04a-public-credit-panel.md)
  - [04B · Hyperscaler Quarterly Capital-Intensity Panel](04b-hyperscaler-quarterly-panel.md)
  - [04C · AI Infrastructure Project-Finance Borrower Panel](04c-project-finance-borrower-panel.md)
  - [04D · Supplier / Sponsor Support Panel](04d-supplier-support-panel.md)
- [05 · Geopolitical Scenario Layer](05-geopolitical-scenario-layer.md)
- [06 · Conditional Timeline](06-conditional-timeline.md)
- [07 · Downstream Empirical Chains](07-downstream-empirical-chains.md)
- [08 · Decision Invariants](08-decision-invariants.md)
- [09 · China System-Stack Extension](09-china-system-stack-extension.md)
- [10 · Minimum Public-Proxy Scenario Dashboard](10-public-proxy-scenario-dashboard.md)
- [11 · Financing Reflexivity Map](11-financing-reflexivity-map.md)
- [12 · Non-AI End-System Supply Conditions](12-non-ai-end-system-supply-conditions.md)
- [13 · Developer Distribution Chokepoint](13-developer-distribution-chokepoint.md)

## Phase II Final Adjudication — 2026-08-30

Phase II validation has now been adjudicated against the frozen 32-chapter publication text.

| Validation layer | Formal-text decision | Adjudication |
|---|---|---|
| P0-1 Historical Clearing Backtest | **MATERIAL FIX APPLIED** | Historical replay proved Accounting is confirmation / severity evidence, not a mandatory S4 gate. The correction was propagated to Ch01 / Ch19 / Ch22 / Ch24 / Ch29 / Ch30 / Ch32 in both languages. |
| P0-2 Demand Elasticity | **NO FORMAL CHANGE** | The Sol Aug-17 short-window OpenRouter-visible E1 event response now clusters around roughly **-0.43 to -0.55** across adjusted specifications (benchmark ~**-0.47**), but this is a single-model/platform event and strict structural causal identification remains unresolved. Formal Ch14/Ch24 already preserve the E1 vs workflow/infrastructure distinction, so no scenario parameter is replaced. |
| P0-3 Verified Workflow Economics | **NO FORMAL CHANGE** | Formal chapters already identify verified-workflow economics as a long-run criterion that is not yet empirically calibrated. |
| P0-4 Macro-Financial Transmission | **NO FORMAL CHANGE** | 04A–04D improve research-side state maintenance; post-cutoff SLOOS / financing updates remain outside the August 28 formal evidence snapshot. |
| 05 Geopolitical Scenario Layer | **NO FORMAL CHANGE** | Formal scenario language already remains conditional and does not convert policy headlines into physical-state facts. |
| 06 Conditional Timeline | **NO FORMAL CHANGE** | Ch28 already functions as a conditional milestone map rather than a deterministic calendar forecast. |
| 07 Downstream Empirical Chains | **NO FORMAL CHANGE** | Ch15 / Ch25 / Ch26 already preserve capability → deployment → persistent outcome boundaries. |
| 08 Decision Invariants | **MATERIAL STRATEGY FIX APPLIED** | Ch31 previously overstated a continuously maintained executable second path as a universal rule. It now prices executable optionality and maintains a second path only when continuity / bargaining / recovery value exceeds carrying cost. |
| 09 China System-Stack Extension | **NO FORMAL CHANGE** | Ch17 already separates production-grade substitution, manufacturing closure, and autonomous frontier closure; later source-quality upgrades remain research-side. |
| 10 Scenario Dashboard / 11 Financing Reflexivity | **NO FORMAL CHANGE** | Formal S1–S4 / financing-reflexivity language is consistent after the S4 breadth correction; derived research layers do not own new facts. |
| 12 Non-AI End-System Conditions | **NO FORMAL CHANGE** | Ch21 already requires observed downstream response and preserves alternative explanations / cost-down / substitution counterevidence. |
| 13 Developer Distribution Chokepoint | **NO FORMAL CHANGE** | Ch18 already classifies the Hugging Face item as a reported transaction, not a completed acquisition or realized foreclosure. |

Final publication-state result:

> **The August 28, 2026 evidence cutoff is unchanged. The current S2 — Baseline Concentration judgment is unchanged. The four-scenario taxonomy is unchanged. The formal report has been refrozen after correcting only the validated definition / strategy defects above.**

After this adjudication, Phase II moves from framework construction to **state-transition maintenance and unresolved empirical estimation only**.

## 下一阶段

优先继续深化而不是扩题：

1. P0-1 已完成第二个独立 negative control，并进入 live logging 阶段；下一步不再为了样本数量机械增加历史 case，优先维护 `01A`：只有真实新 publication-time evidence 触发 WATCH / CANDIDATE / CONFIRMED / de-escalation 时才更新；历史案例只在出现新的机制缺口时扩充；
2. P0-2 下一步直接按 OpenRouter Rankings Daily API 构建 Terra/Luna/Sol common-window model-day panel；先做 top-50 censoring / slug / `as_of` / price-path 审计，通过后才估 event-time effect，并继续分离 provider/model substitution、share displacement 与 net workflow/market expansion；
3. P0-3 已升 v0.7 并冻结 literature expansion；下一步只接受公开/可审计 same-`workflow_id` Level-3 全链数据、按 §17 acquisition contract 前瞻构造的一手企业数据，或 material methodology change；继续禁止跨研究拼接 ROI；
4. P0-4 继续只维护 04A–04D，不扩张主方法文件；04B 的 corporate-layer scope 已收口，不再重复 04A/04C/04D。后续按季度分别维护 public-credit regime、hyperscaler headroom/commitment/monetization、facility state、support activation；只有真实 state transition 才推动研究判断变化；
5. Decision Invariants 结构已收口；不再扩充 hard-invariant 数量，也不再改 canonical 编号。后续只在真实实施案例出现时验证 L/M/H implementation burden；
6. China extension 已成为技术闭合权威层；后续只补能改变某一 layer closure state 的一手/高质量独立证据，不再为了公司数量扩表；已确认重大口径错误才按冻结规则考虑同步正式 ch17；
7. Non-AI end-system panel 进入 response-only maintenance：只有真实 procurement / lead-time / margin / qualification / cadence state change 才新增；upstream scarcity headline 本身不再触发更新，并继续强制记录 cost-down / inventory / substitution 反证；
8. Developer Distribution Chokepoint 已建立 transaction-status gate；后续只有 first-party agreement/approval/closing 或真实 post-control conduct 才推进状态，并继续跟踪 ranking/backend neutrality、multi-vendor parity、deployment friction、model-creator multi-homing 与监管 remedy；
9. 等上述 empirical layers 稳定后，再决定是否明确重开正式 32 章正文。
