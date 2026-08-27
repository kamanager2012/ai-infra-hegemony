# 第三十七卷：AI 基础设施资本风险——折旧、利用率、价格与去库存

## 1. 核心判断

AI 基础设施是否形成泡沫，不能由股价、舆论或单一 CapEx 数字判断。

真正需要观察的是四类信号是否同时出现：

1. **会计信号**：折旧与基础设施运营成本持续上升；
2. **利用率 / 收入信号**：AI 相关增量收入、调用量或机时利用率不足以覆盖新增成本；
3. **市场清算信号**：GPU/整柜现货折价、交期缩短、HBM/CoWoS 由配额转向宽松供应；
4. **前瞻承诺信号**：Cloud CapEx 指引下调，或供应承诺、预付款出现显著放缓、改期或取消。

只有第一类信号，代表资本密集化；第一、二类同时出现，代表 ROI 压力；四类信号共同出现，才接近本卷定义的 **Infrastructure Hard Landing（基础设施硬着陆）**。

因此，本报告不采用“CapEx 很大 = 泡沫”或“CapEx 仍在增长 = 没有泡沫”这两种简单判断。

## 2. 资本开支必须先统一口径

Microsoft、Amazon、Alphabet、Meta 的 CapEx 口径并不完全一致。

不同公司存在：

- 财年与日历年差异；
- PPE 与 net PPE 差异；
- fulfillment/network infrastructure 等非 AI 项目；
- office 与其他技术设施；
- data center、server、network、power 等多类资产。

因此，不能把四家公司全部 CapEx 直接相加后称为“AI hardware CapEx”。

更有意义的观察对象是：

- AI server / accelerator investment；
- network；
- memory；
- data-center construction；
- power；
- custom silicon；

在各家公司投资结构中的占比是否持续提高。

2025–2026 年公开数据已经说明一件事：资本基数仍在快速上升。真正的风险并不是“资本投入太大”本身，而是这些资产未来能否形成足够 utilization 与 cash return。

## 3. 折旧墙：费用出现晚于采购决定

AI infrastructure investment 具有明显的时间错配。

采购决定发生在第一年，但 hardware depreciation 会在后续多个会计年度持续进入费用。

因此，卖方可以在设备交付时确认收入，而买方需要在未来数年内持续承担：

- depreciation；
- power；
- cooling；
- networking；
- software；
- operations。

这意味着“卖方高利润”和“买方 ROI 压力”完全可以同时存在。

本报告不把“四年折旧”写成所有公司的统一会计规则。服务器、accelerator、network equipment 与 data-center building 的使用寿命存在公司差异。

但机制不会改变：

> **一旦大规模 CapEx 转化为 PPE，未来几个会计年度就会出现持续成本；是否继续扩张，则取决于下一轮 utilization、收入和新增订单。**

## 4. Token 价格下降不是泡沫，价格下降与用量不足才是

AI 软件和模型价格持续下降是正常技术进步的一部分。

价格下降本身甚至可能扩大需求。

真正危险的组合是：

- token / inference price 快速下降；
- 但调用量增长不足；
- enterprise workflow 没有形成足够新增收入；
- infrastructure utilization 因此下降。

这也是为什么“DeepSeek 训练成本下降”不能直接推出“AI infrastructure 已经过剩”。

算法效率提高可以降低单位训练或推理需求，但同时也可能：

- 扩大模型使用范围；
- 增加并发；
- 增加 Agent workflow；
- 扩大长上下文与多模态需求。

最终结果取决于**效率提升是否带来足够的需求弹性**。

## 5. AI Software Unit Economics 是需求侧核心

判断 infrastructure demand 是否可持续，必须进一步看应用层单位经济。

AI Software Unit Economics 至少包括：

- inference cost；
- retrieval / storage；
- tool / API cost；
- human review；
- AI-specific cloud cost；
- reliability / observability；
- workflow orchestration。

如果应用公司无法把 AI 转化为可重复的 workflow revenue，那么成本会持续存在，但收入不会同步增长。

这种情况下，风险会从应用层向上游传导：

应用 ROI 下降  
→ cloud workload growth 放缓  
→ utilization 下降  
→ next-round CapEx 放缓  
→ hardware order growth 放缓。

因此，真正的基础设施风险不是“模型公司烧钱”，而是**整个 workload monetization chain 无法覆盖不断扩大的固定资产成本**。

## 6. 去库存不是一个动作，而是四层资产依次出清

AI infrastructure 去库存具有明显层次。

### 6.1 第一层：GPU / Rack Inventory

最容易看到市场变化。

典型信号包括：

- 现货相对合同价折让；
- 交期显著缩短；
- 预付款条款变弱；
- 二手系统出现稳定成交市场。

这是最接近“短周期库存”的部分。

### 6.2 第二层：HBM / Advanced Packaging

这类产能物理黏性更强。

Micron 已明确披露 HBM3E 相同 bit、相同 node 下约需要 DDR5 **3× wafer supply**；TSMC 也持续确认 advanced packaging tightness。

因此，HBM 和 CoWoS 不会因为一个季度订单下滑就立即恢复成普通 DRAM 或消费逻辑产线。

### 6.3 第三层：Installed Compute

已经安装并开始折旧的 server / rack 无法“取消订单”。

如果 utilization 下降，只能通过：

- 降价；
- 转售；
- 改用途；
- 延长使用周期；
- impairment。

这一层会直接影响新设备价格和下一轮采购。

### 6.4 第四层：Data Center / Power

土建、substation、PPA、nuclear contract 等资产期限更长。

在需求强劲时，它们是 scarce asset；在硬着陆时，它们可能成为长期负担。

因此，AI 泡沫如果真正破裂，不会表现为“所有资产一起归零”，更可能表现为：

> **短周期硬件先降价，制造追加产能随后放缓，已安装资产 utilization 下降，而长久期电力与土建继续留在资产负债表上。**

## 7. 卖方与买方的风险不同

NVIDIA、TSMC、memory suppliers 与 cloud buyers 并不处于同一会计位置。

卖方主要面对：

- order growth；
- pricing；
- capacity commitments；
- inventory；
- margin。

买方主要面对：

- depreciation；
- utilization；
- power cost；
- workload revenue；
- return on invested capital。

因此，卖方高利润与买方投资回报压力并不矛盾。

如果需求在高位放缓，最先出现风险的可能是：

1. workload ROI；
2. utilization；
3. next-generation procurement；
4. seller order growth；
5. upstream capacity expansion。

而不是卖方已经确认的历史收入立即消失。

## 8. 监管不能消除折旧墙

反垄断政策可能改变 system-stack competition，但不会自动取消已经投入的 PPE。

罚款属于卖方成本。

折旧属于买方费用。

Token cost 属于应用层单位成本。

这三者位于不同主体的财务报表中。

真正可能影响未来投资回报的监管措施，是能够显著降低 migration cost 的结构性措施，例如：

- interoperability；
- anti-tying；
- portability；
- interface openness；
- structural separation。

即使这些措施发生，它们也只能改变未来 workload allocation，不能追溯性消除已经发生的折旧。

## 9. 四类风险状态

### 9.1 Healthy Expansion

CapEx 高增长，但 utilization、workflow revenue 与 seller orders 同步增长。

结果：高投入属于理性扩容，而不是泡沫。

### 9.2 ROI Pressure

折旧持续上升，但应用层收入和 utilization 开始落后。

结果：投资回报下降，但供给仍然紧张，市场尚未进入真正清算。

### 9.3 Soft Landing

Cloud CapEx 增速下降，硬件价格和交期趋于正常，但 utilization 仍然较高。

结果：行业从极端紧缺转向正常资本周期。

### 9.4 Hard Landing

四类风险信号同时出现：

- utilization 显著下降；
- workflow revenue 不足；
- hardware / HBM / packaging market 明显转松；
- next-round commitments 大幅减速或取消。

这才是本报告定义的基础设施硬着陆。

## 10. 当前状态：尚未出现完整硬着陆信号

截至 2026 年 8 月，当前公开事实仍显示：

- NVIDIA FY27 Q2 Data Center revenue：**$89.0B**；
- GAAP gross margin：**75.0%**；
- Rubin 已进入 full production；
- supply commitments 仍处于高位；
- HBM demand 仍然强；
- TSMC 仍将 advanced packaging 描述为限制客户增长的瓶颈；
- hyperscaler CapEx 仍然处于高位。

这说明“收入失速 + 毛利塌陷 + 供给宽松 + 承诺收缩”的完整硬着陆组合尚未出现。

但这并不意味着风险不存在。

CapEx 是领先指标，折旧和 utilization 验证具有滞后性。当前最值得关注的是未来几个季度是否出现：

- workload revenue 增速放缓；
- utilization 下滑；
- GPU/rack lead time 大幅缩短；
- HBM/CoWoS tightness 缓解；
- supply commitments 改期或取消；
- cloud CapEx 指引系统性下调。

## 11. 可验证指标

### Buyer Side

- CapEx growth；
- PPE growth；
- D&A；
- utilization；
- AI revenue disclosure；
- workflow monetization。

### Seller Side

- Data Center revenue；
- gross margin；
- supply commitments；
- inventory；
- order lead time。

### Market Clearing

- rack / GPU spot pricing；
- secondary-market liquidity；
- HBM lead time；
- CoWoS availability；
- cloud instance pricing。

### Long-duration Assets

- data-center cancellations；
- power contract changes；
- energized MW versus contracted MW；
- impairment。

## 12. 最终判断

AI 基础设施风险的本质，不是“AI 有没有价值”，而是：

> **未来 workload 产生的现金流，能否覆盖今天正在形成的 hardware depreciation、data-center cost、power commitment 和 upstream capacity investment。**

只要 utilization 与 workflow revenue 能够跟上，大规模 CapEx 仍然可能是合理扩张。

如果收入和利用率长期落后，而供给、价格和下一轮承诺同时转弱，AI 基础设施才会真正进入去库存和资本硬着陆。

因此，本卷反对两种极端叙事：

- “CapEx 越大，泡沫越大”；
- “CapEx 还在增长，所以不存在泡沫”。

真正的判断标准始终是：**会计、利用率、市场清算和未来承诺是否同时发生变化。**