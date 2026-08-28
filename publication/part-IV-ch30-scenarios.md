# Part IV · 第30章：S1–S4 四类标准情景

## 1. Scenario Analysis 不是 Point Forecast

本书不为 2030 或 2036 给出一个唯一答案，也不使用固定 40% / 30% / 15% / 15% 之类权重。

情景由以下变量共同决定：

- advanced-capacity allocation；
- HBM supply；
- advanced packaging；
- cloud system-stack substitution；
- Anchor Buyer long-duration demand；
- power / Time-to-Power；
- software migration；
- China parallel stack；
- regulation；
- utilization；
- CapEx / financing discipline。

## 2. S1 — Competitive Expansion / 竞争性扩容

### 定义

AI demand 继续增长，但供给扩张与替代系统成熟速度足以降低 concentration。

典型条件：

- leading-edge capacity 扩张并有更多 qualified supply；
- HBM supply elasticity 提高；
- advanced-packaging tightness 显著缓解；
- cloud custom systems 承担大量真实 workload；
- open software / interfaces 降低 migration cost；
- power / energized capacity 跟上 buildout；
- 多套 system stacks 在 production 中长期并存。

### 经济结果

dominant platform 仍然很大，但 buyer optionality 和 bargaining power 提高，scarcity premium 下行，value capture 更分散。

这是：

> **market expands + concentration declines**

而不是“AI infrastructure 消失”。

## 3. S2 — Baseline Concentration / 基准集中

### 定义

当前主要趋势延续：

- AI demand 高；
- leading system-platform seller economics 强；
- HBM / advanced packaging 仍周期性 tight；
- cloud custom systems 继续扩大但未全面替代 frontier workload；
- power 进入独立部署约束；
- China parallel stack 持续扩展但 frontier closure 未完全完成；
- CapEx / forward commitments 仍高。

### 经济结果

市场继续高速扩大，同时 value capture 集中在少数 system platforms 与 scarce-layer suppliers。

截至 2026 年 8 月，这是最接近当前事实组合的**基准状态**，不是十年固定预测。

## 4. S3 — Resource Hegemony / 资源霸权

### 定义

demand growth 持续快于 substitution 与 supply expansion，多个 scarce layers 同时集中。

典型条件：

- advanced packaging 长期供不应求；
- HBM manufacturing intensity / generation constraint 持续；
- leading-edge incremental capacity 高度集中；
- proprietary software / interconnect migration cost 仍高；
- cloud custom systems 只能局部分流；
- powered land / firm MW 被少数大型 buyers 长期锁定；
- Anchor Buyer 与 seller forward commitments 持续扩大。

### 机制

> high profit → stronger commitments / prepayment → greater future resource reservation → higher delivery certainty → stronger installed base / workload retention

它描述的是 system-level resource coordination 强化，不是法律意义上的 monopoly verdict。

## 5. S4 — Capital Hard Landing / 资本硬着陆

### 定义

AI workload demand、utilization 与 monetization 无法覆盖快速增长的资本基数。

典型同步信号：

- token / workflow volume 增长不足；
- instance / lease price 快速下跌；
- utilization 下降；
- enterprise AI monetization 弱；
- hyperscaler CapEx guidance 下调；
- seller / Anchor Buyer commitments 缩减或取消；
- used hardware residual value 快速下跌；
- impairment / write-down 上升。

### 清算顺序

首先承压通常是：

- next-generation hardware orders；
- inventory；
- short-lived system residual value；
- speculative / highly concentrated financing。

如果弱势持续，才进一步传导到 semiconductor CapEx、data-center expansion 与 power buildout。

S4 不等于 AI usage 消失；资本清算之后，低价 compute 仍可能刺激新的 application demand。

## 5A. AI Capacity Gap：S1–S4 的跨情景诊断轴

S1–S4 保持为并列条件状态，不新增第二套情景命名。为了判断状态权重如何移动，本书增加一个跨情景诊断变量：

```text
AI_Capacity_Gap_i(t)
= Growth(AI_Demand_i(t))
- Growth(AI_Effective_Capacity_i(t))
```

其中 (i) 分别代表 advanced logic、HBM/DRAM、advanced packaging、networking、power 等物理层。不同层的 Gap 可以方向相反，因此禁止先加总成一个“全球 AI 产能缺口”。

解释规则：

- **多个关键层持续 Gap > 0**：scarcity 延续，S2 / S3 相对权重上升；
- **关键层 Gap 向 0 收敛，同时 multi-sourcing 与 substitution 改善**：S1 相对权重上升；
- **Gap < 0 但 utilization 仍高**：只是供给宽松，不能直接判 S4；
- **Gap < 0 + utilization 下滑 + clearing price 恶化 + commitments 收缩**：才构成 S4 权重显著上升的组合。

AI Capacity Gap 与 Non-AI Residual Capacity 必须同时观察。前者回答“AI 自己还缺多少新增供给”，后者回答“优先分配之后，非 AI 市场还剩多少有效供给”。

## 6. 五类决定情景的变量

### Supply

leading-edge wafers、HBM、advanced packaging、power。

### Substitution

cloud custom systems、open compiler/runtime、alternative interconnect、China parallel stack。

### Demand

token/workflow volume、enterprise adoption、Anchor Buyer commitments、sovereign demand。

### Finance

seller cash generation、hyperscaler CapEx、depreciation、utilization、financing cost、residual value。

### Regulation / Geopolitics

export control、antitrust remedy、interface openness、industrial policy、regional fragmentation。

## 7. Anchor Compute Buyer 是新的情景变量

大型 model companies 的多年 compute commitments 已经可以影响 infrastructure financing、custom silicon、power 与 data-center buildout。

如果 Anchor Buyer Demand 持续扩大并兑现 utilization，S2/S3 权重提高。

如果长期 commitments 大规模改期、重谈或利用不足，S4 权重明显提高。

所以 model-company contracts 不能再被当作普通 cloud customer spending。

## 8. S2 → S1 的可观察信号

- alternative system stacks 在 frontier / high-value production workload 中规模化；
- HBM / packaging lead time 持续下降；
- advanced capacity access 更分散；
- open software / interfaces 明显降低 migration cost；
- power expansion 缩短 Time-to-Power；
- buyer multi-sourcing 变成生产常态。

## 9. S2 → S3 的可观察信号

- seller forward commitments 持续快速扩大；
- HBM / packaging tightness 跨代持续；
- proprietary system switching cost 上升；
- leading-edge incremental supply 持续高集中；
- scarce power / powered land 被少数 anchor buyers 长期锁定；
- alternative stacks 无法在 production scale 形成足够选择权。

## 10. S2 → S4 的可观察信号

- CapEx guidance 连续下降；
- utilization 下降；
- seller / Anchor Buyer commitments 取消或明显收缩；
- second-hand system clearing price 快速下跌；
- cloud discounts / lease rates 明显恶化；
- impairment 增加；
- enterprise AI monetization 长期弱于 depreciation / operating cost。

## 11. 为什么 S1、S2、S3、S4 不是顺序阶段

它们是并列条件状态。

例如，某些区域可能出现 S3-style power scarcity，同时某些 workload 已进入 S1-style multi-stack competition；memory 可能暂时进入宽松，而 packaging 仍 tight；capital market 可能局部清算，但 productive workload 继续增长。

因此，全书用 scenario weighting 描述**相对结构**，不把产业强行塞进单一路径。

## 12. 当前基准

截至 2026 年 8 月，正式 baseline 是：

> **S2 — Baseline Concentration**

主要原因是：

- NVIDIA / leading platform seller economics 仍强；
- HBM 与 advanced packaging 仍是关键 bottlenecks；
- cloud custom systems 已形成真实竞争，但尚未证明全面替代 frontier workload；
- infrastructure CapEx 与 forward commitments 仍高；
- power constraint 上升；
- China parallel stack 尚未在所有 frontier critical layers 形成等价闭环；
- 全行业 Capital Hard Landing 的同步证据尚不足。

这条 baseline 只在上述事实组合继续成立时有效。

## 13. Scenario Framework 的最终用途

未来每次更新时，不问：

> “哪一个十年预测被证明了？”

而问：

> **“哪些可观察变量改变了，S1–S4 的相对权重应如何调整？”**

这使远期判断可以随产业事实更新，而不依赖一次性押注。

## 核心监测入口

- [第29章：核心指标与证据监测框架](part-IV-ch29-monitoring-framework.md)
- [第32章：总判](part-IV-ch32-master-judgment.md)
- [核心假设矩阵](../核心假设矩阵.md)