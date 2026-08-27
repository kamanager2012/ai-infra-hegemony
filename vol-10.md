# 第十卷：未来十年 AI 基础设施四类标准情景

## 1. 情景分析不是点预测

本报告不为 2030 或 2036 给出单一确定答案，也不再使用固定的 40% / 30% / 15% / 15% 权重。

未来结果取决于一组可观察变量，包括：

- advanced-capacity allocation；
- HBM supply；
- packaging；
- cloud system-stack substitution；
- model-company long-duration demand；
- power；
- software migration；
- China parallel stack；
- regulation；
- utilization；
- CapEx discipline。

这些变量统一记录在《核心假设矩阵》中。

本卷采用四类标准情景：**S1–S4**。

## 2. S1 — Competitive Expansion / 竞争性扩容

### 定义

AI demand 继续增长，但供给与系统竞争同步扩张。

主要特征：

- TSMC/Samsung 等 advanced capacity 扩张；
- HBM supply 提升；
- packaging tightness 缓解；
- cloud custom silicon 成熟；
- open software layer 降低 migration cost；
- power supply 跟上 data-center buildout；
- 多套 system stack 并存。

### 经济结果

NVIDIA 仍是重要平台，但无法持续提高对全部稀缺层的控制。

平台利润下降到更正常竞争水平，AI 基础设施总市场继续扩大。

这是“市场做大、集中度下降”的路径。

## 3. S2 — Baseline Concentration / 基准集中

### 定义

当前趋势延续：

- AI demand 高；
- NVIDIA seller-side economics 强；
- HBM 与 packaging 持续紧张；
- cloud custom silicon 持续成长但尚未完全替代 frontier training；
- power 成为新的建设约束；
- 中国平行栈继续发展但尚未完成 frontier AI 全栈闭环。

### 经济结果

市场继续快速扩张，同时价值捕获集中在少数 system platform 与 scarce-layer supplier。

这是截至 2026 年 8 月最接近当前事实的基准情景。

## 4. S3 — Resource Hegemony / 资源霸权

### 定义

稀缺资源进一步集中，替代路线进展慢于 demand growth。

典型条件：

- advanced packaging 长期供不应求；
- HBM trade ratio 继续上升；
- leading-edge logic 增量高度集中；
- CUDA/NVLink migration cost 仍高；
- cloud custom silicon 只能局部分流；
- power access 被少数大型买方提前锁定；
- long-duration compute commitments 继续增加。

### 经济结果

system platform 的利润和资源预订能力形成更强正反馈：

高利润  
→ 更高 prepayment  
→ 更多 future capacity  
→ 更高 delivery certainty  
→ 更强 customer lock-in。

这不是法律意义上的“垄断”，而是一种基础设施资源控制力显著增强的产业状态。

## 5. S4 — Capital Hard Landing / 资本硬着陆

### 定义

AI demand、utilization 与 monetization 无法覆盖快速增长的资本成本。

典型信号：

- token/workflow volume 增长停滞；
- instance price 快速下跌；
- utilization 下降；
- enterprise AI revenue 增速不足；
- hyperscaler CapEx guidance 下调；
- supply commitments 停止增长或取消；
- second-hand GPU/system price 下跌；
- infrastructure impairment 上升。

### 经济结果

首先受冲击的通常不是已经建设完的电网和 data-center shell，而是：

- next-generation server orders；
- inventory；
- short-lived hardware residual value；
- speculative model company financing。

如果下降持续，才会进一步传导到 semiconductor CapEx 与 power buildout。

## 6. 四种情景由哪些变量决定

### 6.1 Supply variables

- leading-edge wafer capacity；
- HBM bits；
- packaging capacity；
- power availability。

### 6.2 Substitution variables

- cloud custom silicon；
- open compiler/runtime；
- alternative interconnect；
- China parallel stack。

### 6.3 Demand variables

- token volume；
- enterprise workflow adoption；
- long-duration model-company commitments；
- sovereign AI demand。

### 6.4 Financial variables

- seller FCF；
- hyperscaler CapEx；
- depreciation；
- utilization；
- financing cost。

### 6.5 Regulatory variables

- export control；
- antitrust remedy；
- interface openness；
- national industrial policy。

## 7. Anchor Compute Buyer 是新的关键变量

过去，模型公司更多被视为 cloud customer。

现在 OpenAI、Anthropic 等开始通过多年、GW 级 compute commitment 影响 infrastructure investment。

因此，《核心假设矩阵》加入 **H17 — Anchor Buyer Demand**。

如果大型模型公司的长期需求持续扩大：

- cloud 更愿意提前建设；
- chip/HBM/power 更容易获得长期合同；
- S2/S3 的相对权重提高。

如果这些长期承诺开始取消或重谈：

- S4 的相对权重显著提高。

## 8. 情景切换的可证伪信号

### S2 → S1

- alternative system stack 在 frontier training 中规模化；
- packaging/HBM lead time 显著下降；
- CUDA migration cost 明显降低；
- 多买方获得稳定 advanced capacity。

### S2 → S3

- supply commitments 继续快速上升；
- HBM/packaging 长期紧张；
- system-stack switching cost 上升；
- scarce power 被少数买方长期锁定。

### S2 → S4

- CapEx guidance 连续下降；
- utilization 下降；
- supply commitments 被取消；
- second-hand hardware clearing price 快速下跌；
- enterprise AI monetization 明显弱于折旧和运营成本。

## 9. 当前判断

截至 2026 年 8 月，正式基准是 **S2 — Baseline Concentration**。

原因是：

- NVIDIA FY27 Q2 seller economics 仍强；
- HBM 与 advanced packaging 仍是关键 bottleneck；
- cloud custom silicon 已形成真实竞争，但尚未完全替代 frontier training；
- AI infrastructure CapEx 继续扩张；
- power 约束上升；
- China parallel stack 尚未在 frontier AI 全部关键层实现等价替代。

但 S2 不是永恒状态。

未来十年真正值得追踪的，不是谁在某一年拥有多少“市场份额”，而是哪一套 system stack 能持续获得：

> logic + HBM + packaging + interconnect + software + rack + data center + power

并把这些资源转化成可持续 utilization 与现金流。
