# 第八卷：AI 基础设施超级周期、CapEx 与折旧压力

## 1. 本轮资本周期的核心不是“总投资到底是多少”

Microsoft、Amazon、Alphabet、Meta 的 AI/data-center 投资已经进入历史高位。

但分析这一周期最容易犯的错误，是把不同财年、不同 CapEx 科目、不同公司口径机械相加，然后全部命名为“AI hardware CapEx”。

本报告坚持三个分离：

1. company-wide CapEx 与 AI-specific CapEx 分离；
2. IT equipment 与 data-center/power infrastructure 分离；
3. actual CapEx 与 guidance/forecast 分离。

详见《四云Capex口径核对》。

## 2. 2025–2026 的资本扩张现实

2025 混年口径下，Microsoft、Amazon、Alphabet、Meta 的 equipment/PPE purchase 已达到约 **$354B** 量级。

截至 2026 年 8 月：

- Microsoft 已公开给出 calendar 2026 CapEx 约 **$190B** 的预期；
- Alphabet 指引约 **$180–190B**；
- Meta 指引约 **$125–145B**；
- Amazon 截至 2026 Q2 的 TTM net PPE purchase 约 **$169B**。

这些数字已经足以证明 AI infrastructure CapEx cycle 仍在扩张。

但它们并不是同一时间窗、同一会计科目，因此不能直接相加成一个“官方四云 AI CapEx 总额”。

## 3. CapEx 为什么会形成长期锁定

AI infrastructure investment 包含多个不同寿命的资产：

- GPU/accelerator：较短技术周期；
- servers/network：中短周期；
- data-center shell：长周期；
- substations/transmission：更长周期；
- nuclear/PPA：可能达到 10–20 年以上。

这导致一个核心错配：

> **技术迭代速度远快于部分基础设施资产的经济寿命。**

如果模型效率、系统架构或需求在服务器折旧尚未完成前快速变化，就会出现 asset obsolescence risk。

如果服务器需求仍然很强，而 grid connection 迟迟不能完成，则会出现 stranded-infrastructure risk。

## 4. 折旧墙应该怎样分析

不能简单使用：

[
Total CapEx / 4
]

作为“AI 年折旧”。

原因是：

- CapEx 不全是 IT hardware；
- data center 与 power asset 使用寿命更长；
- 各公司折旧政策不同；
- financing lease 与 purchase accounting 不同。

更可靠的方法是观察：

- PPE additions；
- D&A；
- useful-life disclosure；
- AI-related revenue；
- utilization；
- incremental operating cash flow。

因此，本报告把“折旧墙”定义为**经济压力机制**，而不是固定年度美元点预测。

## 5. 什么情况下这是超级周期，而不是泡沫

CapEx 大本身并不能证明泡沫。

如果以下指标同时成立，大规模 CapEx 可以被视为扩张性基础设施投资：

- utilization 高；
- revenue per deployed compute 稳定；
- token/workflow volume 上升；
- customer demand 长期化；
- supply commitments 继续增长；
- next-generation deployment 仍有明确 ROI。

相反，如果出现以下组合，则资本硬着陆风险提高：

- utilization 下降；
- token price 下降但 volume 不增长；
- enterprise workflow monetization 停滞；
- next-year CapEx guidance 下调；
- supply commitments 停止增长或被取消；
- second-hand system residual value 快速下跌。

## 6. Seller 与 buyer 的资本结构不同

NVIDIA 与 hyperscaler 不能只比较“谁更有钱”。

NVIDIA 的高 FCF 主要用于：

- inventory；
- capacity reservation；
- supply commitments；
- system roadmap。

Hyperscaler 的现金则要同时承担：

- land；
- buildings；
- power；
- network；
- custom silicon；
- third-party systems；
- operations。

因此，同样 $1 的现金，在两类公司中的“再生产对象”不同。

这解释了为什么一个 asset-light platform 可以用较少自有 fixed assets，影响远大于自己资产负债表规模的 manufacturing CapEx。

## 7. Power 把资本周期进一步拉长

AI rack power density 上升之后，data-center buildout 不再只是服务器采购。

关键约束逐渐扩展到：

- grid connection；
- substations；
- transformers；
- transmission；
- cooling；
- long-duration power contracts。

这意味着硬件周期和 power/infrastructure cycle 开始叠加。

如果 chip supply 放松而 power 不放松，瓶颈会从 semiconductor 转移到 electricity。

这就是 **Rolling Bottleneck Cascade**。

## 8. 资本周期的四类清算信号

本报告使用四类信号判断资本周期是否恶化：

### 8.1 Accounting

- impairment；
- depreciation acceleration；
- inventory write-down；
- asset disposal。

### 8.2 Utilization / revenue

- deployed compute utilization；
- AI workload revenue；
- revenue per compute unit；
- idle capacity。

### 8.3 Market clearing

- second-hand GPU/system price；
- cloud instance discount；
- lease rate；
- delivery lead time。

### 8.4 Forward commitments

- CapEx guidance；
- supply commitments；
- long-term compute contracts；
- power contracts。

只有多类信号同时恶化，才足以支持“资本硬着陆”。

## 9. 当前判断

截至 2026 年 8 月，AI infrastructure 仍处于资本扩张阶段，而不是已经完成清算。

风险也在同步上升：

- annual CapEx base 快速扩大；
- server generation 更新更快；
- power asset duration 更长；
- model/software price competition 更激烈。

因此，当前更准确的判断是：

> **超级周期仍在延续，但对 utilization、workflow monetization 与 next-generation ROI 的要求越来越高。**

这正是 S2 Baseline Concentration 与 S4 Capital Hard Landing 之间最关键的分界。
