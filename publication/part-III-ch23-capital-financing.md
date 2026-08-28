# Part III · 第23章：AI 基础设施资本市场与融资结构

## 1. AI Capital Market 已跨越多种资产类别

AI infrastructure 的资本体系已经不只包括 listed technology equity。

它同时覆盖：

- semiconductor manufacturing；
- private infrastructure；
- data center；
- power / grid；
- project finance；
- long-duration compute contracts；
- private credit / institutional capital。

因此，核心问题不是“还有多少钱愿意投 AI”，而是：

> **哪一种资本承担哪一种久期、现金流和 residual-value risk。**

## 2. Asset-light Platform 与 Heavy Infrastructure 不能用同一估值逻辑

NVIDIA 的典型特征是 high system margin、strong cash generation 与相对较低直接 fixed-asset intensity。

FY26 NVIDIA-defined non-GAAP free cash flow 为 **US$96.575B**；[^1] FY27 Q2 Revenue **US$96.221B**、Data Center **US$89.0B**、GAAP gross margin **75.0%**、GAAP operating income **US$63.734B**。[^2]

相比之下，hyperscaler、foundry、memory vendor、data-center operator 和 power developer 需要承担大量 fixed assets。

所以同样 revenue growth，在 platform 与 infrastructure 层的 capital return 含义完全不同。

## 3. Hyperscaler 风险来自多资产叠加

cloud CapEx 同时进入 servers、custom silicon、network、buildings、cooling、power 和 land。

这意味着 hyperscaler 必须同时管理多个 useful-life clock。

高 utilization 时，这种 CapEx 可以形成 barrier；低 utilization 时，D&A、FCF 与 residual-value pressure 会迅速显现。

因此需要同时看 growth、D&A、FCF、utilization、AI-related monetization 与 next-year CapEx。

## 4. Manufacturing Capital 具有不同的周期性

TSMC、SK hynix、Micron 等制造商承担 fab、equipment、cleanroom、process migration 与 yield learning。

它们的回报取决于 utilization、product mix、technology leadership、customer demand 与 pricing。

HBM boom 可以显著改善 memory-vendor economics，但制造利润仍比 system-platform economics 更受 cycle 与 utilization 影响。

## 5. 2026 年出现了独立 Compute Financing Platform

NVIDIA 2026-08-10 官方宣布，与 Apollo、BlackRock、Blackstone、Brookfield、Goldman Sachs、KKR 建立独立 compute financing platforms，目标是**随时间动员超过 US$500B third-party capital**用于 AI infrastructure buildout。[^3]

这条证据的重要性不在“500B 已到账”，而在于：

> **compute 正被尝试组织成可由长期机构资本独立承销和融资的基础设施资产。**

官方同时明确：相关 partnership **subject to execution of final agreements**。

因此 >US$500B 只能作为 mobilization target，不能写成 committed / funded / deployed capital。

## 6. Compute 为什么能被包装成 Infrastructure Asset

长期资本通常偏好 predictable cash flow、long contract、collateral 与 clear offtaker。

AI compute 正通过 long-term compute commitments、hyperscaler leases、PPA 与 Anchor Compute Buyer demand 尝试创造这种结构。

如果 usage-linked revenue 与 customer transferability 足够稳定，compute asset 可以获得更接近 infrastructure financing 的资本来源。

## 7. 但 Hardware Residual Value 仍是关键风险

compute 与传统 infrastructure 最大差异之一，是 generation obsolescence 更快。

如果下一代 accelerator / system 显著降低 cost per task，旧 hardware 即使仍可工作，也可能快速贬值。

所以融资结构必须回答：

- residual-value risk 谁承担；
- customer contract 是否覆盖 depreciation；
- utilization 是否足够稳定；
- asset 是否可在不同 customers/operators 之间转移；
- leverage 是否建立在过度乐观的 terminal value 上。

## 8. Anchor Buyer 可以降低融资风险，也提高 Customer Concentration

OpenAI、Anthropic 等 long-duration demand 提供 revenue visibility，使 project finance 更容易成立。

但如果 project economics 高度依赖单一 model company，融资风险会从 technology risk 转成 customer-concentration / utilization risk。

因此，Anchor Buyer 既是融资条件，也是风险集中点。

## 9. Sovereign Capital 的意义在 Strategic Capacity

主权基金参与 AI infrastructure 的逻辑通常不仅是财务回报，也包括 domestic compute、data center、power、semiconductor manufacturing 与 strategic autonomy。

所以真正具有战略意义的是对 fab、power、sovereign cloud、compute fund 和 infrastructure project 的直接参与，而不是二手市场股票持仓。

没有官方项目披露时，本书不使用传闻持仓构造“主权资本已经全面入场”的结论。

## 10. Duration Matching 是融资质量核心

**Table 23.1 — AI infrastructure 资产类别与主要融资风险**

| 资产 | 主要风险 |
|---|---|
| GPU/server | technology refresh / residual value |
| Data center | utilization / lease duration |
| Grid/substation | long construction / regulated return |
| PPA | long obligation / demand risk |
| Foundry | utilization / node transition |
| HBM fab | memory cycle / generation timing |

**Source:** 本报告资产久期与融资风险框架。  
**Note:** 表中为机制分类，不代表所有项目具有相同融资结构、杠杆水平或合同条款。

最危险结构是：

> **short-duration demand assumption + long-duration debt / power / real-estate obligation**

## 11. 当前判断

AI infrastructure 正从科技公司内部 CapEx 扩展为：

> **technology capital + infrastructure capital + private capital + sovereign capital**

共同参与的长期资产体系。

这会扩大可获得资本规模，也会把 risk distribution 从单一 corporate balance sheet 扩散到更广的金融体系。

最终决定这类融资是否可持续的，不是 headline target，而是 utilization、cash yield、contract quality 与 hardware residual value。

## References

[^1]: NVIDIA, “NVIDIA Announces Financial Results for Fourth Quarter and Fiscal 2026,” NVIDIA-defined non-GAAP free cash flow, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
[^2]: NVIDIA, “NVIDIA Announces Financial Results for Second Quarter Fiscal 2027,” https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^3]: NVIDIA, 2026-08-10, AI compute infrastructure financing platforms and >US$500B third-party-capital mobilization target, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Partners-With-Apollo-BlackRock-Blackstone-Brookfield-Goldman-Sachs-and-KKR-to-Establish-AI-Compute-Infrastructure-Financing-Platforms-to-Mobilize-Over-500-Billion-of-Third-Party-Capital/default.aspx
