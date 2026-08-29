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

- **P0-1 Historical Clearing Backtest**：v0.7；已恢复 2008–2009 GFC / Enterprise IT 详细案例，把 Case A–H 统一到 first-deterioration / cross-confirmation / accounting-confirmation / trough timing matrix，并进一步收紧 A/B/C/H 的 source-level timing；新增反例显示 inventory-led clearing 中 Accounting 可以与 Market Clearing 几乎同步，因此只能说“多数长周期案例里 Accounting 更常滞后”，不能写成固定顺序；
- **P0-2 AI Demand Elasticity Calibration**：v0.4；除 preferred E1≈-1.11、multi-homing 与 ε/σ_task 边界外，已审计 GPT-5.6 discount event 的公开数据可得性：事件窗口和聚合响应可见，但无可下载 daily raw panel，因此冻结为 Tier B descriptive event-study candidate，不制造回归系数；
- **P0-3 Verified Workflow Economics**：v0.5；新增 515 家 startup 的 Mapping AI into Production firm-performance bridge、Alibaba customer-service persistence counterexample 与 property-tax action-completion case，并把闭环固定为 Productivity → Cost → Economic 三层；完整 Level-3 仍要求同一 workflow_id 联结 AI/tool cost + human time + verification + persistence + realized business value；
- **P0-4 Macro-Financial Transmission**：v0.18；方法层已与可维护数据层分离：04A public-credit/macros、04B hyperscaler quarterly capital intensity、04C project-finance borrowers、04D supplier/sponsor support；主文件只保留 transmission logic 与 S4 cross-confirmation rules；
- **P1 Geopolitical Scenario Layer**：v0.1 已建立；新增 G1–G5：Taiwan continuity、export-control regime、allied coordination、China autonomous closure、bloc fragmentation；
- **P1 Conditional Timeline**：v0.1 已建立；把 2026–2036 时间线改造成 condition → milestone → contrary signal 的 research-side rewrite map；
- **P2 Downstream Empirical Chains**：v0.1 已建立；固定 Labor / Education / Physical AI 的最低实证链与证据边界；
- **Decision Invariants**：v0.2；已完成 S1–S4 cross-scenario falsification，将 hard set 从 12 个候选压缩为 10 条；“持续维护第二生产路径”“偏好自融资需求”“优先 transferability”降为 conditional strategy；
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

1. P0-1 下一步只继续压 Medium-confidence trough / stabilization 边界，并在新增样本时优先找与科技无关、可观测 utilization + financing + residual-value 的周期；
2. P0-2 先寻找 machine-readable OpenRouter daily export / reproducible historical panel；没有原始日度数据就不做 event-time point estimate，继续分离 provider/model substitution、share displacement 与 net workflow/market expansion；
3. P0-3 下一步只追 Level-3 Economic Closure：同一 workflow_id 下连接 AI/tool cost + human time + verification + persistence + realized business value；同时把 use-case mapping/discovery cost 纳入 adoption economics；
4. P0-4 下一步在 04A–04D 附录中维护数据，不再扩张主方法文件；继续解析 NY Fed CMDI stable direct-file path，并优先补 facility-level changes、project monetization/delivery、support drawdown 与 guarantee activation state；
5. Decision Invariants 下一步只验证 actor-specific implementation cost：检查 10 条 hard invariants 是否在 enterprise / hyperscaler / supplier / infrastructure developer / capital provider / policymaker 六类主体上都可操作；
6. China extension 继续补 server-vendor / accelerator / foundry / policy 的可审计矩阵；已确认的重大口径错误才按冻结规则同步回正式 ch17；
7. 继续补 Non-AI end-system response panel：优先找第二个 console platform、更多 PC OEM、automotive/industrial 的一手 procurement / lead-time / margin / qualification evidence；必须同时保留 cost-down / inventory / substitution 反证；
8. Developer Distribution Chokepoint 后续只跟踪交易正式状态、ranking/backend neutrality、multi-vendor parity、deployment friction、model-creator multi-homing 与监管 remedy；不把单一 UI/default 变化升级成 foreclosure。
9. 等上述 empirical layers 稳定后，再决定是否明确重开正式 32 章正文。
