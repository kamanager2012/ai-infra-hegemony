# Part IV · 第30章：S1–S4 四类标准情景

## 1. Scenario Analysis 不是 Point Forecast

本报告不为 2030 或 2036 给出一个唯一答案，也不使用固定 40% / 30% / 15% / 15% 之类权重。

情景由以下变量共同决定：

- layer-specific scarce-capacity access；
- HBM supply；
- advanced packaging；
- cloud system-stack substitution；
- Anchor Buyer long-duration demand；
- power / Time-to-Power；
- software migration；
- China parallel stack；
- regulation；
- utilization；
- CapEx / financing discipline；
- demand financing quality / supplier-assisted financing。

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
- advanced logic、HBM、packaging、LPS/power 等多个关键层的 quantity assurance / delivery access 持续向少数买方集中；
- proprietary software / interconnect migration cost 仍高；
- cloud custom systems 只能局部分流；
- powered land / firm MW 被少数大型 buyers 长期锁定；
- Anchor Buyer 与 seller forward commitments 持续扩大；
- infrastructure finance 能持续吸收长期资本，且 workload monetization 足以支撑相关承诺。

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
- impairment / write-down 上升；
- customer financing capacity 走弱，同时 supplier equity / credit support 或 refinancing dependency 上升。

### 清算顺序

首先承压通常是：

- next-generation hardware orders；
- inventory；
- short-lived system residual value；
- speculative / highly concentrated financing。

如果弱势持续，才进一步传导到 semiconductor CapEx、data-center expansion 与 power buildout。

S4 不等于 AI usage 消失；资本清算之后，低价 compute 仍可能刺激新的 application demand。

## 5.1 四类标准情景的比较框架

**Table 30.1 — S1–S4 的核心驱动、主要结果与反向信号**

| 情景 | 核心驱动 | 主要产业结果 | 关键反向信号 |
|---|---|---|---|
| S1 — Competitive Expansion | supply elasticity、multi-sourcing、portability 上升 | value capture 更分散，buyer optionality 提高 | scarce-layer tightness 重新强化、migration cost 回升 |
| S2 — Baseline Concentration | demand 强、dominant platforms 强、替代持续但不完全 | 高增长与集中并存 | supply/substitution 明显改善或 ROI/commitments 同步恶化 |
| S3 — Resource Hegemony | 多层 scarcity + switching cost + forward reservation / financing coordination 强化 | layer-specific capacity access 更集中，后来者复制成本提高 | capacity access 分散、open interfaces 显著降低迁移成本 |
| S4 — Capital Hard Landing | utilization / monetization 弱于资本基数，且 demand financing quality 恶化 | clearing、orders、CapEx 与资产价值下行，refinancing pressure 上升 | utilization、clearing price、financing independence 和 forward commitments 恢复 |

**Source:** 本报告 S1–S4 scenario framework。  
**Note:** 四类情景是并列条件状态，不赋固定概率，也不是必然连续阶段。

## 5A. Capacity Gap 是诊断轴，不是第二套情景体系

AI Capacity Gap、AI Capacity Growth Gap 与 Non-AI Residual Capacity 的定义和量纲规则已经在第8章完整给出，本章不再重复公式。

在情景分析中，它们只承担诊断作用：

- **AI Capacity Gap 持续为正且供给追赶不足**：S2 / S3 权重上升；
- **AI 仍短缺但 supply elasticity 明显改善**：S1 权重上升；
- **出现有效余量但 utilization 仍健康**：不等于 S4；
- **有效余量扩大，同时 utilization、clearing price 与 commitments 恶化**：S4 权重上升；
- **Non-AI Residual Capacity 继续下降**：说明 AI / priority demand 的资源吸收仍在向传统市场传导。

详细计算边界见[第8章：AI 基础设施量化框架与 Rolling Bottleneck Cascade](part-I-ch08-quantitative-framework.md)。

## 6. 六类决定情景的变量

### Supply

leading-edge wafers、HBM、advanced packaging、power。

### Substitution

cloud custom systems、open compiler/runtime、alternative interconnect、China parallel stack。

### Demand

token/workflow volume、enterprise adoption、Anchor Buyer commitments、sovereign demand。

### Capital / Monetization

seller cash generation、hyperscaler CapEx、depreciation、utilization、workload revenue、residual value。

### Financing Quality

Anchor Buyer credit quality、third-party risk capital、supplier equity / credit support、refinancing dependency、asset transferability。

### Regulation / Geopolitics

export control、antitrust remedy、interface openness、industrial policy、regional fragmentation。

## 7. Anchor Compute Buyer 与 Financing Reflexivity 是新的情景变量

大型 model companies 的多年 compute commitments 已经可以影响 infrastructure financing、custom silicon、power 与 data-center buildout。

但 2026 年的新变化是，system seller 也开始通过 equity、credit enhancement、LPS support 与 compute-financing platforms 参与资本形成。[^7][^8]

因此需要同时观察两个方向：

- **健康扩张**：Anchor Buyer demand、third-party capital、seller support 与真实 utilization / monetization 同步增长；
- **融资反身性恶化**：customer cash generation 走弱，但 seller equity / credit support 与 refinancing dependency 持续上升。

前者可以强化 S2/S3 的 infrastructure coordination；后者则提高 S4 风险。

所以 model-company contracts 与 seller-supported financing 都不能被当作普通 cloud customer spending。

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
- 多个关键 scarce layers 的 quantity assurance / delivery access 持续向少数买方集中；
- scarce power / powered land 被少数 anchor buyers 长期锁定；
- alternative stacks 无法在 production scale 形成足够选择权。

## 10. S2 → S4 的可观察信号

- CapEx guidance 连续下降；
- utilization 下降；
- seller / Anchor Buyer commitments 取消或明显收缩；
- second-hand system clearing price 快速下跌；
- cloud discounts / lease rates 明显恶化；
- impairment 增加；
- enterprise AI monetization 长期弱于 depreciation / operating cost；
- supplier equity / credit support 占比上升，而独立 customer financing / third-party risk-taking 走弱。

## 11. 为什么 S1、S2、S3、S4 不是顺序阶段

它们是并列条件状态。

例如，某些区域可能出现 S3-style power scarcity，同时某些 workload 已进入 S1-style multi-stack competition；memory 可能暂时进入宽松，而 packaging 仍 tight；capital market 可能局部清算，但 productive workload 继续增长。

因此，本报告用 scenario weighting 描述**相对结构**，不将产业演化简化为单一路径。

## 12. 当前基准

截至 2026 年 8 月，本报告的 baseline 是：

> **S2 — Baseline Concentration**

主要原因是：

- NVIDIA / leading platform seller economics 仍强；[^1]
- HBM 与 advanced packaging 仍是关键 bottlenecks；[^2][^3]
- cloud custom systems 已形成真实竞争，但尚未证明全面替代 frontier workload；[^4]
- infrastructure CapEx 与 forward commitments 仍高；[^5]
- power constraint 上升；[^6]
- China 已形成真实 production-grade substitution 路径，但 autonomous frontier closure 尚未在所有 critical layers 得到规模化证明；
- 全行业 Capital Hard Landing 的同步证据尚不足。

这条 baseline 只在上述事实组合继续成立时有效；判别方法见 §12A。

## 12A. 判别规则：S1–S4 之间如何用公开证据区分

情景之间按以下判别轴区分，而不是用单一总量指标：

- **S1 ↔ S2**：替代系统在 frontier / high-value production workload 中的规模化程度，以及 HBM / packaging lead time 是否持续下降；
- **S2 ↔ S3**：scarce-layer allocation 的集中度变化方向、seller forward commitments 增速、proprietary switching cost 与 powered-land 锁定程度；
- **S3 ↔ S4**：utilization / monetization 与资本基数之比——该变量不公开披露，因此使用公开代理：clearing price（二手系统价、lease rate、cloud discount）、commitments 增速、seller equity / credit support 占比、third-party capital 的 risk premium 与 refinancing dependency。

同一批资本证据（如 **>US$500B** mobilization target、**US$50B** frontier-lab 投资、**2 GW** credit support）[^7][^8][^9]在代理信号健康时支持 S2/S3 的 infrastructure coordination，在代理信号广泛、持续恶化时支持 S4 权重上升；判别不依赖任何单点数据。

边界情形：若需求增速显著放缓但不触发五类 S4 信号，则按 substitution 强度归属——替代规模化扩大则 S1 权重上升；scarce-layer 仍紧则归入 S2（此时"需求高"应读作"需求增速仍高于有效供给增速"）。

## 13. Scenario Framework 的最终用途

未来每次更新时，不问：

> “哪一个十年预测被证明了？”

而问：

> **“哪些可观察变量改变了，S1–S4 的相对权重应如何调整？”**

这使远期判断可以随产业事实更新，而不依赖一次性押注。

## References

[^1]: NVIDIA, FY27 Q2 official results, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^2]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E wafer-supply trade ratio, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^3]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging tightness limiting customer growth, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^4]: Google Ironwood TPU, https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; AWS Trainium3 UltraServers, https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ ; Microsoft Maia 200, https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ ; Meta MTIA 300, https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
[^5]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^6]: NVIDIA, DGX GB200 Hardware Guide, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html ; Talen Energy, 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
[^7]: NVIDIA, 2026-08-10, AI compute infrastructure financing platforms and >US$500B third-party-capital mobilization target, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Partners-With-Apollo-BlackRock-Blackstone-Brookfield-Goldman-Sachs-and-KKR-to-Establish-AI-Compute-Infrastructure-Financing-Platforms-to-Mobilize-Over-500-Billion-of-Third-Party-Capital/default.aspx
[^8]: NVIDIA, 2026-08-17, PORTS-Pike / SB Energy / OpenAI, LPS credit support and initial 4.25 IT-GW design capacity, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx
[^9]: NVIDIA, FY27 Q2 Earnings Call transcript, 2026-08-26, frontier-lab investment close to US$50B and selective credit enhancement for close to 2 GW of compute, https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf

## 交叉引用

- [第29章：核心指标与证据监测框架](part-IV-ch29-monitoring-framework.md)
- [第32章：总判](part-IV-ch32-master-judgment.md)
- [核心假设矩阵](../核心假设矩阵.md)