# 第二十一卷：AI 基础设施资金流与利润池结构

## 1. 资金流不能把同一美元重复记三遍

AI infrastructure 的资金流经常同时出现在：

- hyperscaler CapEx；
- system vendor revenue；
- foundry revenue；
- memory vendor revenue；
- power/data-center investment。

如果简单把这些数字相加，就会把同一笔支出在不同公司账上重复计算。

因此，本卷不估算一个“全球 AI 利润池总额”，而是分析：

> 每一层的收入、成本与利润最终停在哪里。

## 2. 四个主要资金节点

### 2.1 Hyperscaler

Microsoft、Amazon、Alphabet、Meta 的 CapEx 是买方资本支出。

其中包含：

- server；
- network；
- custom silicon；
- third-party accelerator；
- data center；
- power；
- land；
- fulfillment/other infrastructure（视公司而定）。

因此，cloud CapEx 不能直接等同于“支付给 NVIDIA 的钱”。

### 2.2 System platform

NVIDIA Data Center revenue 是卖方收入。

关键财务锚如下：

| 指标 | 数值 |
|---|---:|
| FY26 Data Center revenue | **US$193.737B** |
| FY26 non-GAAP free cash flow（NVIDIA 定义） | **US$96.575B** |
| FY27 Q2 Data Center revenue | **US$89.0B** |
| FY27 Q2 GAAP operating income | **US$63.734B** |

这说明 system platform 可以留下非常高比例的价值。

### 2.3 Foundry / packaging

TSMC 收入来自：

- wafer manufacturing；
- advanced packaging；
- testing。

2025：

- gross margin：**59.9%**
- HPC platform：**58% of revenue**
- advanced packaging + testing：略高于 **10%**

TSMC 在系统中承担重资产制造，因此其资本强度与 NVIDIA 完全不同。

### 2.4 Memory

SK hynix、Samsung、Micron 通过 HBM 与 server memory 获得 AI infrastructure 需求。

SK hynix FY25 官方结果：

- Revenue：**KRW 97.1467T**
- Operating profit：**KRW 47.2063T**
- Operating margin：**49%**
- Net income：**KRW 42.9479T**
- HBM revenue：**more than doubled YoY**。

公开来源：https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/

这表明 memory layer 已经成为重要利润池。

## 3. 为什么 platform margin 与 manufacturing margin 不同

NVIDIA 的经济模型更接近：

> system definition + software + integration + supply orchestration。

TSMC 的经济模型更接近：

> manufacturing service + CapEx + yield + capacity utilization。

memory vendor 则处于：

> product cycle + manufacturing scarcity + technology transition。

因此，不能只用一个毛利率表判断“谁更强”。

需要同时看：

- capital intensity；
- switching cost；
- supply scarcity；
- customer concentration；
- ability to reinvest profits。

## 4. Supply commitment 是跨层资金的重要连接点

NVIDIA manufacturing, supply, and capacity commitments：

- 2026-01-25：**US$95.2B**
- 2026-04-26：**US$119B**
- 2026-07-26：**US$279B**

Q2 10-Q 说明，最新承诺主要关联 memory 与 manufacturing facilities；仍不能拆成单一 supplier amount。来源：https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

它说明 system vendor 已经提前将未来现金需求转化为：

- inventory；
- wafer；
- HBM；
- packaging；
- other components。

但公开文件没有 supplier-level split。

因此，这笔钱不能直接写成：

- TSMC 收到多少；
- SK hynix 收到多少；
- Micron 收到多少。

它只能作为**未来资源锁定强度**的财务 proxy。

## 5. Hyperscaler 的钱为什么不等于 system vendor 的钱

hyperscaler 同样拥有极强现金流，但资金用途更加分散。

需要同时承担：

- land；
- building；
- power；
- network；
- cooling；
- silicon；
- third-party systems；
- operations。

因此，system vendor 与 cloud buyer 的现金不能只比较绝对规模。

真正的差异是：

> 谁的资本可以更直接地用于下一代 scarce layer reservation。

## 6. HBM 把资金流从“芯片”扩展到 memory

TrendForce 预计 2026 年 HBM + RDIMM 约占 DRAM bits **51%**。

Micron 的 ~3× wafer-supply trade ratio 又说明 HBM 对 manufacturing input 的消耗高于同 bit DDR5。

因此，AI infrastructure 的资金不只流向 GPU。

它越来越多地流向：

- HBM；
- RDIMM；
- advanced packaging；
- memory fab expansion。

这解释了为什么 consumer DRAM 也会受到 AI demand 的间接影响。

## 7. Power 成为新的资本吸收层

当 rack power 接近 120 kW，hyperscaler 必须提前投入：

- substation；
- transformer；
- grid connection；
- cooling；
- firm power contract。

因此，AI 资金流正在从 semiconductor 向 energy/infrastructure 扩展。

未来 value capture 可能从单纯 chip margin 进一步转移到：

- powered land；
- firm MW；
- grid access；
- long-duration energy asset。

## 8. AI Software 为什么不能直接套传统 SaaS 利润率

应用层会新增：

- inference；
- retrieval；
- storage；
- tool/API；
- human review。

因此，软件公司的利润池必须按 **AI Software Unit Economics** 分析。

一个收入增长很快的 AI software company，未必同时拥有高质量利润。

真正需要观察：

- gross margin after inference；
- cost per workflow；
- retention；
- revenue per task；
- human review cost。

## 9. 资金流的正确读法

从买方到上游，大致形成：

> Hyperscaler / model company  
> → system platform  
> → foundry / memory / packaging  
> → equipment / materials  
> → power / data-center infrastructure。

但这条链不是单向。

cloud custom silicon 会让部分资金绕开 NVIDIA platform，直接流向：

cloud  
→ foundry / HBM / packaging。

因此，system-stack competition 会改变利润分配，但不一定降低上游资源需求。

## 10. 当前判断

AI infrastructure 当前最强的利润池集中在：

1. system platform；
2. HBM；
3. leading-edge foundry / packaging；
4. powered infrastructure。

应用层能否形成长期利润池，则取决于 unit economics 和 distribution。

因此，AI 产业最重要的不是“总共花了多少钱”，而是：

> **同一笔资本在每一层留下多少利润、形成多少长期锁定、产生多少可重复现金流。**

## 本卷关键公开来源

- TrendForce（2026 HBM + RDIMM = 51% of DRAM bit supply）： https://www.trendforce.com/presscenter/news/20260825-13198.html
- Micron FY24 Q3 Prepared Remarks（HBM3E ≈ 3× DDR5 wafer supply）： https://investors.micron.com/static-files/4550f98c-1054-4847-a929-c17d520a0564
