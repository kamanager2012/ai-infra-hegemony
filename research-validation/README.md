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

- **P0-1 Historical Clearing Backtest**：v0.9；在 B/D/G/H 四路径 prospective replay 之后，已补完 2013–2014 Solar recovery contemporaneous replay；新增对称规则 **Recovery confirmation inherits the same layer / breadth discipline as clearing**：2013 只能维持 Stabilization Candidate，直到 2014 equipment orders + sales + operating economics 同向改善后才升级 equipment-supplier-layer Recovery Confirmed，同时明确不等于 full industry normalization；
- **P0-2 AI Demand Elasticity Calibration**：v0.5；OpenRouter `GET /api/v1/datasets/rankings-daily` 的模型日数据路径、top-50 + `other`、`as_of/version` 与字段语义已确认，**data path = closed**；但真实 Terra/Luna/Sol extraction 需要有效 API key，当前 **authentication blocked**，因此 **coefficient = not estimated**。不绕过认证、不从图表反推 daily panel，也不把 5.6×/13.8× headline 直接换算成结构弹性；
- **P0-3 Verified Workflow Economics**：v0.6；完成 public Level-3 workflow-ID candidate audit。METR 246 个 OSS issue 是目前最接近公开 task-ID telemetry 的样本，可联结 treatment + implementation time + 部分 review-to-merge time，但仍缺同 ID 的 AI cost / durable persistence / realized business value；Klarna 则公开约 US$40M annualized savings 但只有 aggregate economics。结论保持严格：**跨研究拼接 ≠ workflow-ID closure，目前仍没有在同一 workflow_id 完整关闭 Level-3 的公开生产数据集**；
- **P0-4 Macro-Financial Transmission**：方法主文件继续保持 v0.18，不扩张；数据层继续推进。04C 已升 v0.2，新增 facility-level longitudinal state ledger（committed → drawn → delivery → monetization → refinance/stress）；04D 已升 v0.2，新增 support activation ledger，严格分离 maximum exposure / effective exposure / triggered obligation / funded cash loss；
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

1. P0-1 Solar recovery contemporaneous replay 已完成；下一步仍不拟合 score，优先找 **1 个真正独立 negative control** 验证 de-escalation，并继续测试 recovery 是否能在其他资本周期保持同层级 / 同广度纪律；
2. P0-2 下一步直接按 OpenRouter Rankings Daily API 构建 Terra/Luna/Sol common-window model-day panel；先做 top-50 censoring / slug / `as_of` / price-path 审计，通过后才估 event-time effect，并继续分离 provider/model substitution、share displacement 与 net workflow/market expansion；
3. P0-3 public candidate audit 已完成但 Level-3 仍未关闭；下一步只接受两类升级：公开/可审计的同一 workflow_id 全链数据，或按当前 schema 前瞻构造的一手企业数据；继续禁止把 task-level time 与另一个组织的 aggregate savings 拼成虚假 ROI；
4. P0-4 继续只维护 04A–04D 数据附录，不扩张主方法文件；04C/04D 已建立 facility/support 状态机，下一步按季度追 draw ratio、ready-for-service / commencement、facility-level monetization、DSCR/covenant、refinancing、guarantee phase activation / step-down；04A 继续解析 NY Fed CMDI stable direct-file path，04B 继续维护 hyperscaler capital-intensity panel；
5. Decision Invariants actor-specific implementation-cost test 已完成；下一步只在真实案例出现时验证 implementation burden 是否与 L/M/H 分类一致，不再扩充 hard-invariant 数量；
6. China extension 继续补 server-vendor / accelerator / foundry / policy 的可审计矩阵；已确认的重大口径错误才按冻结规则同步回正式 ch17；
7. 继续补 Non-AI end-system response panel：优先找第二个 console platform、更多 PC OEM、automotive/industrial 的一手 procurement / lead-time / margin / qualification evidence；必须同时保留 cost-down / inventory / substitution 反证；
8. Developer Distribution Chokepoint 后续只跟踪交易正式状态、ranking/backend neutrality、multi-vendor parity、deployment friction、model-creator multi-homing 与监管 remedy；不把单一 UI/default 变化升级成 foreclosure。
9. 等上述 empirical layers 稳定后，再决定是否明确重开正式 32 章正文。
