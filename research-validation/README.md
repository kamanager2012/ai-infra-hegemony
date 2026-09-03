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

- **P0-1 Historical Clearing Backtest**：v1.0；历史框架保持冻结，`01A` live prospective ledger 已升 **v0.3**。2026-09-03 更新新增 Broadcom Q3 FY26 一手业绩作为第二个独立大型 AI semiconductor/networking supplier 的强反证：AI semiconductor revenue US$16.7B、+221% YoY / +54% QoQ，Q4 guide US$21.7B；同时纳入 NVIDIA 部分 revenue-sharing support arrangement 被报道暂停/重构的 support-architecture observation。当前 composite state 仍为 **NO CLEARING**，WATCH 集中在资本强度、客户集中、financing-quality dispersion 与 seller-support reflexivity；
- **P0-2 AI Demand Elasticity Calibration**：v0.8；30 天 raw panel 已完成目标覆盖审计，Terra/Luna/Sol 均为 **30/30 days observed**，rank 最差分别 30 / 17 / 32，因此 target-model top-50 censoring 已关闭。Sol 2026-08-17 50% discount 的多组 short-window adjusted specifications 给出约 **-0.43 到 -0.55** 的 OpenRouter-visible E1 event-response range；benchmark specification 约 **-0.47**（95% CI 约 **[-0.69, -0.24]**）。其中 `non-Sol market growth` 只能作为 normalization，不能视为完全外生 control；raw pre/post `-1.40` 被证明会明显混入平台整体增长。Terra/Luna 因 raw export 从 7/30 才开始，不能独立识别 7/27/7/30 初始 treatment。另发现周榜最新 bucket 与 8/24–8/28 日榜合计相差 **10.4169T**，因此撤销此前 `96.90T / 5 days` 的错误 normalization；**structural E2/E3/E4 coefficient 仍未估计**；
- **P0-3 Verified Workflow Economics**：v0.7；public Level-3 candidate audit 已完成，并新增 prospective first-party acquisition contract：固定 `workflow_id` 主键，分离 AI/tool/runtime cost、human execution/review/remediation、verification、persistence 与 realized-value ledger，同时明确 `0 ≠ N/A ≠ not measured ≠ not yet observed`。新增 stop rule：以后只有公开 same-`workflow_id` Level-3 closure、一手前瞻数据，或真正改变 verification / persistence / causal attribution 的方法学结果才允许升级；generic productivity studies 不再触发版本升级；
- **P0-4 Macro-Financial Transmission**：方法主文件继续保持 v0.18，不扩张；四个数据附录职责已收口。04A v0.3 负责 public-credit regime 与 CMDI provenance；04B v0.2 负责 hyperscaler corporate capital state；04C v0.2 负责 facility-level delivery / monetization / DSCR / refinancing；**04D 已升 v0.3**，新增 seller-support program `REDESIGNED / PAUSED-PARTIAL` 状态，记录 NVIDIA 部分 revenue-sharing support arrangement 的报道性调整，并继续固定 support redesign ≠ end-demand destruction；
- **P1 Geopolitical Scenario Layer**：v0.2；新增 ownership contract：05 只负责 G1–G5 geopolitical state definitions 与 event→physical/financial transmission；China technical closure 以 09 为准，scenario aggregation 以 10 为准，正式 Chapter 30 只有显式 reopen 后才可吸收；
- **P1 Conditional Timeline**：v0.2；固定为 derived rewrite layer，只负责 `condition → milestone → contrary signal` 的 conditional grammar，不再生成/升级上游事实状态；05/09/04A–04D/10/01A 分别提供权威输入，Chapter 28 仍冻结；
- **P2 Downstream Empirical Chains**：v0.4；Physical AI 已补 production-grade evidence；Labor 新增 Stanford/ADP direct payroll evidence，把 early-career transmission 从 exposure 推进到 reduced-hiring-driven pipeline divergence；Education 新增 18-school Khanmigo two-year cluster RCT 与 6,000+ student NUMI delayed-assessment RCT，把 evidence chain 推进到 school-scale learning + partial delayed retention。三条链均继续保留 causal / persistence / TCO / system-scale boundary；
- **Decision Invariants**：v0.3；十条 hard invariants 保持不变，并已修正标题编号：canonical hard set 统一为 `Hard Invariant 1–10`，历史上被降级的 executable-second-path / transferability 条目改为 `Conditional Strategy A/B`，避免“标题到 11 但总数为 10”的外部可读性歧义；
- **China System-Stack Extension**：v0.3；继续作为 research-side China technical-closure authority；本轮来源审计进一步固定 evidence hierarchy：IDC 2025H1 accelerated-server 数字明确降级为 proprietary tracker 的 secondary relay / directional evidence，不能单独关闭高影响 market-share 结论；海光信息 2025 财务依据已替换为上海证券交易所官方审计财务报表；
- **Public-Proxy Scenario Dashboard**：v0.6；新增 derived-layer ownership contract：Dashboard 只做 scenario aggregation，不再作为 04A/04B/04C/04D 的竞争性事实台账。Dashboard K 的 company/facility factual state 分别以 04B/04C 为准，Dashboard 只负责 cross-confirmation 与 S1–S4 relevance；
- **Financing Reflexivity Map**：v0.3；继续保留 2026 Support Taxonomy 与 anti-double-counting，但新增 scope contract：`11` 只负责 financing taxonomy / causal graph / reflexivity diagnostic；facility state 归 04C，support activation / funded-loss state 归 04D，live clearing adjudication 归 01A；
- **Non-AI End-System Supply Conditions**：v0.4；在 downstream response-only 规则基础上新增 automotive / industrial attribution counterevidence：NXP 2026Q2 automotive/industrial revenue recovery、Infineon AI growth 与 automotive-order recovery / shared-capacity expansion、ST selected tightness + low distribution inventory 共同说明 supplier-side AI growth / tightness 不能替代 OEM response。当前结论仍是 shared-resource exposure credible，但 broad realized AI-attributed automotive/industrial pressure 未建立；
- **Developer Distribution Chokepoint**：**v0.4**；2026-09-03 一手源复核仍未验证 NVIDIA/Hugging Face definitive agreement / approval / closing；新增 pre-control / unverified-control neutrality baseline：Hugging Face 2026-09-02 WebGPU local-AI kernels 与现有 multi-provider inference architecture 作为后续自我优待比较基线。当前仍为 **DDC-A / transaction-status WATCH**，没有 realized foreclosure evidence。

## 文件索引

- [00 · External Reference Landscape](00-external-reference-landscape.md)
- [01 · Clearing Signals Backtest](01-clearing-signals-backtest.md)
  - [01A · Prospective Adjudication Ledger](01a-prospective-adjudication-ledger.md)
- [02 · Demand Elasticity Calibration](02-demand-elasticity-calibration.md)
  - [OpenRouter · 30-day daily raw panel](data/openrouter-rankings-daily-2026-07-30_2026-08-28.csv)
  - [OpenRouter · four-week weekly raw panel](data/openrouter-rankings-weekly-2026-08-03_2026-08-24.csv)
  - [OpenRouter · source / as-of / tokenizer / license note](data/openrouter-rankings-source-note-2026-08-29.txt)
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
| 07 Downstream Empirical Chains | **MATERIAL EVIDENCE-BOUNDARY FIX APPLIED** | Ch15 now records pre-cutoff production-grade Physical AI evidence while retaining reliability/TCO limits. Ch25 now uses the direct Stanford/ADP revision to distinguish reduced hiring from separations and explicitly preserves its descriptive/non-causal identity. Ch26 now records pre-cutoff school-scale Khanmigo and delayed-assessment NUMI evidence while preserving engagement, retention, transfer, teacher-workload and implementation-cost limits. |
| 08 Decision Invariants | **MATERIAL STRATEGY FIX APPLIED** | Ch31 previously overstated a continuously maintained executable second path as a universal rule. It now prices executable optionality and maintains a second path only when continuity / bargaining / recovery value exceeds carrying cost. |
| 09 China System-Stack Extension | **NO FORMAL CHANGE** | Ch17 already separates production-grade substitution, manufacturing closure, and autonomous frontier closure; later source-quality upgrades remain research-side. |
| 10 Scenario Dashboard / 11 Financing Reflexivity | **NO FORMAL CHANGE** | Formal S1–S4 / financing-reflexivity language is consistent after the S4 breadth correction; derived research layers do not own new facts. |
| 12 Non-AI End-System Conditions | **NO FORMAL CHANGE** | Ch21 already requires observed downstream response before attribution. New 2026 NXP / Infineon / ST supplier-side evidence is mixed—automotive/industrial recovery, capacity expansion and selected tightness coexist—so it strengthens the rule that supplier-side AI growth/tightness cannot be promoted into an OEM-level AI crowding claim without a real downstream behavioral response. |
| 13 Developer Distribution Chokepoint | **NO FORMAL CHANGE** | Ch18 already classifies the Hugging Face item as a reported transaction, not a completed acquisition or realized foreclosure. |

Final publication-state result:

> **The August 28, 2026 evidence cutoff is unchanged. The current S2 — Baseline Concentration judgment is unchanged. The four-scenario taxonomy is unchanged. The formal report has been refrozen after correcting only the validated definition / strategy defects above.**

After this adjudication, Phase II moves from framework construction to **state-transition maintenance and unresolved empirical estimation only**.

## 下一阶段

优先继续深化而不是扩题：

1. P0-1 已完成第二个独立 negative control，并进入 live logging 阶段；下一步不再为了样本数量机械增加历史 case，优先维护 `01A`：只有真实新 publication-time evidence 触发 WATCH / CANDIDATE / CONFIRMED / de-escalation 时才更新；历史案例只在出现新的机制缺口时扩充；
2. P0-2 的 30 天 Terra/Luna/Sol common-window panel、target-model censoring audit 与 Sol 8/17 short-window event calibration 已完成；下一步只在获得 **7/8–7/29 更早 machine-readable pre-window** 后尝试独立识别 Terra/Luna 初始 treatment，并继续把 provider/model substitution、share displacement 与 net market expansion 分开。E2/E3/E4 仍需真实 workload / verified-workflow / infrastructure denominator，不用 Sol 的单模型事件系数替代；
3. P0-3 已升 v0.7 并冻结 literature expansion；下一步只接受公开/可审计 same-`workflow_id` Level-3 全链数据、按 §17 acquisition contract 前瞻构造的一手企业数据，或 material methodology change；继续禁止跨研究拼接 ROI；
4. P0-4 继续只维护 04A–04D，不扩张主方法文件；04B 的 corporate-layer scope 已收口，不再重复 04A/04C/04D。后续按季度分别维护 public-credit regime、hyperscaler headroom/commitment/monetization、facility state、support activation；只有真实 state transition 才推动研究判断变化；
5. Decision Invariants 结构已收口；不再扩充 hard-invariant 数量，也不再改 canonical 编号。后续只在真实实施案例出现时验证 L/M/H implementation burden；
6. China extension 已成为技术闭合权威层；后续只补能改变某一 layer closure state 的一手/高质量独立证据，不再为了公司数量扩表；已确认重大口径错误才按冻结规则考虑同步正式 ch17；
7. P2 进入 chain-closure maintenance：Labor 只接受能推进 causal staffing / wage / occupation transmission 的证据；Education 只接受 delayed retention / transfer、teacher workload、implementation cost 或 system-scale outcome；Physical AI 只接受 intervention / uptime / safety denominator / TCO / customer renewal / multi-site fleet economics。Non-AI automotive/industrial 只接受 OEM / equipment-maker procurement、pricing、qualification、lead-time、production/cadence 的真实 response；supplier-side tightness 本身不再触发 attribution。
8. Developer Distribution Chokepoint 已建立 transaction-status gate；后续只有 first-party agreement/approval/closing 或真实 post-control conduct 才推进状态，并继续跟踪 ranking/backend neutrality、multi-vendor parity、deployment friction、model-creator multi-homing 与监管 remedy；
9. 等上述 empirical layers 稳定后，再决定是否明确重开正式 32 章正文。
