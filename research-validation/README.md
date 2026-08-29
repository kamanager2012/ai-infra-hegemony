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

- **P0-1 Historical Clearing Backtest**：v0.5；已包含 7 个 layer/cycle observations；新增 2018–2019 hyperscale cloud CapEx digestion 独立负对照，进一步验证“单点 CapEx 减速 ≠ system-wide clearing”；固定 proxy hierarchy、segment breadth、lead/lag 与 false-positive constraints；
- **P0-2 AI Demand Elasticity Calibration**：v0.3；除 preferred E1≈-1.11 与 GPT-5.6 event catalog 外，新增 firm multi-homing / concentration 约束，并明确 ε（price-demand elasticity）与 σ_task（task substitution elasticity）不可混用；
- **P0-3 Verified Workflow Economics**：v0.3；ledger 新增 66 firms / 7,137 knowledge workers、P&G 776 professionals、online-retail randomized field experiments；进一步区分 individual time saving、organization throughput、team-substitution 与 business value；
- **P0-4 Macro-Financial Transmission**：v0.2；已把 2026 Fed SLOOS / Financial Stability Report 与 CoreWeave / Core Scientific 真实债务、合同现金流、客户集中度接入 project-level transmission chain；
- **P1 Geopolitical Scenario Layer**：v0.1 已建立；新增 G1–G5：Taiwan continuity、export-control regime、allied coordination、China autonomous closure、bloc fragmentation；
- **P1 Conditional Timeline**：v0.1 已建立；把 2026–2036 时间线改造成 condition → milestone → contrary signal 的 research-side rewrite map；
- **P2 Downstream Empirical Chains**：v0.1 已建立；固定 Labor / Education / Physical AI 的最低实证链与证据边界；
- **Decision Invariants**：v0.1 已建立；从 Chapter 31 的条件化战略中提炼跨 S1–S4 都成立的低后悔决策原则；
- **China System-Stack Extension**：v0.1 已建立；补服务器/整机交付、Huawei full stack、上市公司证据地图、产业政策政治经济学，并把 design origin / foundry closure / autonomous closure 分开；
- **Public-Proxy Scenario Dashboard**：v0.1 已建立；把 S1–S4 的 latent variables 映射到公开代理、反证、breadth 与 persistence，不制造伪阈值；
- **Financing Reflexivity Map**：v0.1 已建立；拆分 end-demand origin、seller support、contract-backed leverage 与 downstream balance-sheet transmission，防止把同一需求链重复当成多源确认；
- **Non-AI End-System Supply Conditions**：v0.1 已建立；把 smartphone/PC、automotive/industrial、robotics、defense/aerospace/space 分成直接共享、相邻重配与高可靠小批量三类暴露。

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

1. P0-1 把 Case A–G 全部统一填入 first-deterioration / cross-confirmation / accounting-confirmation / trough timing，并继续增加跨行业独立周期；
2. P0-2 对 GPT-5.6 Terra/Luna/Sol 做 event-time 重估，分离 provider/model substitution、share displacement 与 net workflow/market expansion；
3. P0-3 优先寻找能够在同一 workflow_id 下连接 AI cost + human time + verification + persistence + business value 的真实数据；
4. P0-4 建季度 macro-financial panel，继续映射 CoreWeave / Core Scientific / hyperscaler / supplier-supported projects 的融资结构、客户集中与 contract-backed debt；
5. 对 Decision Invariants 做 cross-scenario falsification：凡是只在某一情景成立的原则降回 conditional strategy；
6. China extension 继续补 server-vendor / accelerator / foundry / policy 的可审计矩阵；已确认的重大口径错误才按冻结规则同步回正式 ch17；
7. 继续补 Non-AI end-system exposure 的可审计证据，尤其是 automotive qualification、industrial longevity、trusted/space electronics 的供应连续性；只有当 AI-era transmission 能被直接观测时，才考虑把相应行业扩入正式第21章；
8. 等上述 empirical layers 稳定后，再决定是否明确重开正式 32 章正文。
