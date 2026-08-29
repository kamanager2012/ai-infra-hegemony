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

## 当前状态

- **P0-1 Historical Clearing Backtest**：v1.0；在 B/D/G/H 四路径 + Solar recovery replay 之后，新增第二个真正独立 negative control：2019 Boeing 737 MAX / commercial aerospace。结果证明 dominant supplier 即使同时出现 production cut + delivery collapse + large accounting charge，只要 independent competitor、end demand 与行业 breadth 不同步恶化，也不能升级成 system clearing。v1.0 因此新增 **signal severity cannot substitute for causal breadth** 与 regulatory/operational-shock boundary；同时新增 `01A` live prospective adjudication ledger，开始对 2026 AI infrastructure 做真正 publication-time logging；
- **P0-2 AI Demand Elasticity Calibration**：v0.5；OpenRouter `GET /api/v1/datasets/rankings-daily` 的模型日数据路径、top-50 + `other`、`as_of/version` 与字段语义已确认，**data path = closed**；但真实 Terra/Luna/Sol extraction 需要有效 API key，当前 **authentication blocked**，因此 **coefficient = not estimated**。不绕过认证、不从图表反推 daily panel，也不把 5.6×/13.8× headline 直接换算成结构弹性；
- **P0-3 Verified Workflow Economics**：v0.7；public Level-3 candidate audit 已完成，并新增 prospective first-party acquisition contract：固定 `workflow_id` 主键，分离 AI/tool/runtime cost、human execution/review/remediation、verification、persistence 与 realized-value ledger，同时明确 `0 ≠ N/A ≠ not measured ≠ not yet observed`。新增 stop rule：以后只有公开 same-`workflow_id` Level-3 closure、一手前瞻数据，或真正改变 verification / persistence / causal attribution 的方法学结果才允许升级；generic productivity studies 不再触发版本升级；
- **P0-4 Macro-Financial Transmission**：方法主文件继续保持 v0.18，不扩张；四个数据附录职责已收口。04A v0.2 负责 public-credit regime 与 CMDI canonical retrieval/provenance；04B v0.2 只负责 hyperscaler `Headroom → Commitment → Corporate Financing → Demand Breadth → Monetization`，并新增 longitudinal descriptive states；04C v0.2 负责 facility-level delivery / monetization / DSCR / refinancing；04D v0.2 负责 support activation / step-down。跨附录只引用，不重复维护状态表；
- **P1 Geopolitical Scenario Layer**：v0.1 已建立；新增 G1–G5：Taiwan continuity、export-control regime、allied coordination、China autonomous closure、bloc fragmentation；
- **P1 Conditional Timeline**：v0.1 已建立；把 2026–2036 时间线改造成 condition → milestone → contrary signal 的 research-side rewrite map；
- **P2 Downstream Empirical Chains**：v0.1 已建立；固定 Labor / Education / Physical AI 的最低实证链与证据边界；
- **Decision Invariants**：v0.3；在 S1–S4 falsification 之后完成 enterprise / hyperscaler / supplier / infrastructure developer / capital provider / policymaker 六类主体 implementation-cost test；10 条 hard invariants 全部保留，但 Invariant 1 改为 decision-relevant verified outcome、Invariant 5 改为 stage-gate irreversible commitments，并明确 hard invariant ≠ high-cost action；
- **China System-Stack Extension**：v0.1 已建立；补服务器/整机交付、Huawei full stack、上市公司证据地图、产业政策政治经济学，并把 design origin / foundry closure / autonomous closure 分开；
- **Public-Proxy Scenario Dashboard**：v0.5；在 refinancing exposure / realized stress 分离基础上，Axis G 已新增 Seller / Sponsor Support protocol；支持强度上升只在独立资本、客户经济性与 refinancing 同时恶化时才成为 S4 amplifier；
- **Financing Reflexivity Map**：v0.2；新增 2026 Support Taxonomy，把 seller equity、lease/payment guarantees、vendor/OEM finance、third-party capital mobilization 与 customer prepayment 分开，并固定 guarantee cap / support commitment ≠ funded CapEx ≠ independent demand；
- **Non-AI End-System Supply Conditions**：v0.2；新增 Sony / Microsoft / Nintendo 三个 2025–2026 end-system response anchors，形成 quantity-assurance pressure、PC inventory/device-price transmission 与 cost-down absorption 的正反样本。
- **Developer Distribution Chokepoint**：v0.1；由 2026-08-27 NVIDIA/Hugging Face reported transaction 触发，建立 model discovery / distribution / runtime / deployment 的 vertical-foreclosure 监测协议；当前只判定为潜在高影响纵向整合风险，不判定已完成 software monopoly。

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

## 下一阶段

优先继续深化而不是扩题：

1. P0-1 已完成第二个独立 negative control，并进入 live logging 阶段；下一步不再为了样本数量机械增加历史 case，优先维护 `01A`：只有真实新 publication-time evidence 触发 WATCH / CANDIDATE / CONFIRMED / de-escalation 时才更新；历史案例只在出现新的机制缺口时扩充；
2. P0-2 下一步直接按 OpenRouter Rankings Daily API 构建 Terra/Luna/Sol common-window model-day panel；先做 top-50 censoring / slug / `as_of` / price-path 审计，通过后才估 event-time effect，并继续分离 provider/model substitution、share displacement 与 net workflow/market expansion；
3. P0-3 已升 v0.7 并冻结 literature expansion；下一步只接受公开/可审计 same-`workflow_id` Level-3 全链数据、按 §17 acquisition contract 前瞻构造的一手企业数据，或 material methodology change；继续禁止跨研究拼接 ROI；
4. P0-4 继续只维护 04A–04D，不扩张主方法文件；04B 的 corporate-layer scope 已收口，不再重复 04A/04C/04D。后续按季度分别维护 public-credit regime、hyperscaler headroom/commitment/monetization、facility state、support activation；只有真实 state transition 才推动研究判断变化；
5. Decision Invariants actor-specific implementation-cost test 已完成；下一步只在真实案例出现时验证 implementation burden 是否与 L/M/H 分类一致，不再扩充 hard-invariant 数量；
6. China extension 继续补 server-vendor / accelerator / foundry / policy 的可审计矩阵；已确认的重大口径错误才按冻结规则同步回正式 ch17；
7. 继续补 Non-AI end-system response panel：优先找第二个 console platform、更多 PC OEM、automotive/industrial 的一手 procurement / lead-time / margin / qualification evidence；必须同时保留 cost-down / inventory / substitution 反证；
8. Developer Distribution Chokepoint 后续只跟踪交易正式状态、ranking/backend neutrality、multi-vendor parity、deployment friction、model-creator multi-homing 与监管 remedy；不把单一 UI/default 变化升级成 foreclosure。
9. 等上述 empirical layers 稳定后，再决定是否明确重开正式 32 章正文。
