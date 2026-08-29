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

- **P0-1 Historical Clearing Backtest**：v0.4；已包含 6 个 layer/cycle observations，并新增 2014–2016 Oil & Gas 独立跨行业资本周期；固定 proxy hierarchy、segment breadth、lead/lag 与 false-positive constraints，且相关宏观 episode 不重复计数；
- **P0-2 AI Demand Elasticity Calibration**：v0.2；将 ε*=0.737 明确为 D-grade geometry break-even；复核 NBER provider-model-day 识别式与 preferred E1≈-1.11，并加入 2026-08 GPT-5.6 discount event catalog；E1 / E2 / E3 / E4 继续严格分层；
- **P0-3 Verified Workflow Economics**：v0.2；除 VSWO / Cost-per-VSWO 定义外，已建立 customer support / METR / CodeFuse evidence-completeness ledger，明确现有研究尚未完整覆盖 cost + human time + verification + persistence；
- **P0-4 Macro-Financial Transmission**：v0.1 已建立；把 rates / spreads / SLOOS / WACC / project finance / refinancing 接入资本周期与 S4；
- **P1 Geopolitical Scenario Layer**：v0.1 已建立；新增 G1–G5：Taiwan continuity、export-control regime、allied coordination、China autonomous closure、bloc fragmentation；
- **P1 Conditional Timeline**：v0.1 已建立；把 2026–2036 时间线改造成 condition → milestone → contrary signal 的 research-side rewrite map；
- **P2 Downstream Empirical Chains**：v0.1 已建立；固定 Labor / Education / Physical AI 的最低实证链与证据边界；
- **Decision Invariants**：v0.1 已建立；从 Chapter 31 的条件化战略中提炼跨 S1–S4 都成立的低后悔决策原则；
- **China System-Stack Extension**：v0.1 已建立；补服务器/整机交付、Huawei full stack、上市公司证据地图、产业政策政治经济学，并把 design origin / foundry closure / autonomous closure 分开。

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

## 下一阶段

优先继续深化而不是扩题：

1. P0-1 增加一个独立负对照，并把 Case A–F 全部统一填入 first-deterioration / cross-confirmation / accounting-confirmation / trough timing；
2. P0-2 对 GPT-5.6 Terra/Luna/Sol 做 event-time 重估，分离 share displacement 与 net market expansion；
3. P0-3 寻找能够在同一 workflow_id 下连接 cost + human time + verification + persistence 的真实数据；
4. P0-4 建季度 macro-financial panel，并映射主要 AI-infrastructure 项目的融资结构；
5. 对 Decision Invariants 做 cross-scenario falsification：凡是只在某一情景成立的原则降回 conditional strategy；
6. China extension 继续补 server-vendor / accelerator / foundry / policy 的可审计矩阵；已确认的重大口径错误才按冻结规则同步回正式 ch17；
7. 等上述 empirical layers 稳定后，再决定是否明确重开正式 32 章正文。
