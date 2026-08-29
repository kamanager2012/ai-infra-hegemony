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
- **P0-3 Verified Workflow Economics**：v0.4；在企业 RCT ledger 上新增 1,174 人 randomized problem-solving + non-AI follow-up，开始把 assisted output 与 persistence / retained human capability 分开；完整 Cost/VSWO 仍缺 cost + human time + verification + persistence + business value 同 workflow_id 联结；
- **P0-4 Macro-Financial Transmission**：v0.8；在 macro backbone、四大 hyperscaler 年度 self-funding history 与 2026Q2 cross-section 上，新增 Meta 2024Q1–2026Q2 quarter-level OCF / PP&E / finance-lease pilot；CMDI 官方确认存在 aggregate/IG/HY downloadable file，但动态页面尚未解析出稳定 direct-file URL，因此记录为 provenance limitation，不伪造下载路径；
- **P1 Geopolitical Scenario Layer**：v0.1 已建立；新增 G1–G5：Taiwan continuity、export-control regime、allied coordination、China autonomous closure、bloc fragmentation；
- **P1 Conditional Timeline**：v0.1 已建立；把 2026–2036 时间线改造成 condition → milestone → contrary signal 的 research-side rewrite map；
- **P2 Downstream Empirical Chains**：v0.1 已建立；固定 Labor / Education / Physical AI 的最低实证链与证据边界；
- **Decision Invariants**：v0.2；已完成 S1–S4 cross-scenario falsification，将 hard set 从 12 个候选压缩为 10 条；“持续维护第二生产路径”“偏好自融资需求”“优先 transferability”降为 conditional strategy；
- **China System-Stack Extension**：v0.1 已建立；补服务器/整机交付、Huawei full stack、上市公司证据地图、产业政策政治经济学，并把 design origin / foundry closure / autonomous closure 分开；
- **Public-Proxy Scenario Dashboard**：v0.1 已建立；把 S1–S4 的 latent variables 映射到公开代理、反证、breadth 与 persistence，不制造伪阈值；
- **Financing Reflexivity Map**：v0.1 已建立；拆分 end-demand origin、seller support、contract-backed leverage 与 downstream balance-sheet transmission，防止把同一需求链重复当成多源确认；
- **Non-AI End-System Supply Conditions**：v0.2；新增 Sony / Microsoft / Nintendo 三个 2025–2026 end-system response anchors，形成 quantity-assurance pressure、PC inventory/device-price transmission 与 cost-down absorption 的正反样本。

## 文件索引

- [00 · External Reference Landscape](00-external-reference-landscape.md)
- [01 · Clearing Signals Backtest](01-clearing-signals-backtest.md)
- [02 · Demand Elasticity Calibration](02-demand-elasticity-calibration.md)
- [03 · Verified Workflow Economics](03-verified-workflow-economics.md)
- [04 · Macro-Financial Transmission](04-macro-financial-transmission.md)
- [05 · Geopolitical Scenario Layer](05-geopolitical-scenario-layer.md)
- [06 · Conditional Timeline](06-conditional-timeline.md)
- [07 · Downstream Empirical Chains](07-downstream-empirical-chains.md)
- [08 · Decision Invariants](08-decision-invariants.md)
- [09 · China System-Stack Extension](09-china-system-stack-extension.md)
- [10 · Minimum Public-Proxy Scenario Dashboard](10-public-proxy-scenario-dashboard.md)
- [11 · Financing Reflexivity Map](11-financing-reflexivity-map.md)
- [12 · Non-AI End-System Supply Conditions](12-non-ai-end-system-supply-conditions.md)

## 下一阶段

优先继续深化而不是扩题：

1. P0-1 下一步只继续压 Medium-confidence trough / stabilization 边界，并在新增样本时优先找与科技无关、可观测 utilization + financing + residual-value 的周期；
2. P0-2 先寻找 machine-readable OpenRouter daily export / reproducible historical panel；没有原始日度数据就不做 event-time point estimate，继续分离 provider/model substitution、share displacement 与 net workflow/market expansion；
3. P0-3 优先寻找能够在同一 workflow_id 下连接 AI cost + human time + verification + persistence + business value 的生产数据，并区分 rented capability 与 retained capability；
4. P0-4 下一步继续解析 NY Fed CMDI stable direct-file path，并按 Meta 模板把 Microsoft / Alphabet / Amazon 展开成稳定口径季度表；随后接入 neocloud interest expense / maturities 与 supplier-support amounts；
5. Decision Invariants 下一步只验证 actor-specific implementation cost：检查 10 条 hard invariants 是否在 enterprise / hyperscaler / supplier / infrastructure developer / capital provider / policymaker 六类主体上都可操作；
6. China extension 继续补 server-vendor / accelerator / foundry / policy 的可审计矩阵；已确认的重大口径错误才按冻结规则同步回正式 ch17；
7. 继续补 Non-AI end-system response panel：优先找第二个 console platform、更多 PC OEM、automotive/industrial 的一手 procurement / lead-time / margin / qualification evidence；必须同时保留 cost-down / inventory / substitution 反证；
8. 等上述 empirical layers 稳定后，再决定是否明确重开正式 32 章正文。
