# 四云 Capex 口径核对

> 核对日期：2026-08-27  
> 目的：统一 Microsoft、Amazon、Alphabet、Meta 的 CapEx / PPE 口径，避免把不同财年、不同会计科目和不同业务范围机械相加。  
> 本核对优先使用公司 IR、Exhibit 99.1、现金流量表与最新公开指引；若后续 10-K/10-Q 对相关数字重述，以最新法定申报为准。

## 结论

1. 历史口径中的 **$215B** 并不是四家公司在同一日历年、同一会计科目下披露的统一 CapEx 总额；它最接近“Microsoft 财年 + 其余三家日历年”的混合口径。
2. 按可复加的 2024 混年设备购置口径，合计约 **$211.9B–$213.9B**。因此历史 **$215B** 量级接近，但会计口径并不严格一致。
3. 这四笔均为 **company-wide CapEx / PPE**，不是“AI server / GPU”分项。Amazon 还包含 fulfillment/network infrastructure，Meta 包含 Reality Labs，Alphabet 包含办公及其他技术设施。
4. 截至 2026 年 8 月，公开规模继续上升，但时间窗和科目仍不统一：Microsoft calendar 2026 CapEx 预期约 **$190B**；Alphabet guidance **$180–190B**；Meta guidance **$125–145B**；Amazon 截至 2026 Q2 的 TTM net PPE purchase 约 **$169B**。这些数字可以用于判断资本扩张方向，但**不能机械复加成统一“2026 AI hardware CapEx”**。

## 可复加用的科目

| 公司 | 财年截止 | 本稿采用的科目 | 不要和它对齐的东西 |
|---|---|---|---|
| Microsoft | 6 月 30 日 | Additions to property and equipment（现金流量表） | PP&E 账面净值、折旧费用 |
| Amazon | 12 月 31 日 | Purchases of property and equipment, net of proceeds from sales and incentives（公司自己的 capex / FCF 定义） | 毛额购置；履约网络 vs AWS 未拆 |
| Alphabet | 12 月 31 日 | Purchases of property and equipment | 2025 年 2 月当时给的「约 $750 亿」指引（实际 2025 是 $914.47 亿） |
| Meta | 12 月 31 日 | 主表用 Purchases of property and equipment；公司口头 capex 还加 Principal payments on finance leases | 两套数不能混进同一列再加总 |

## 已核对数字（百万美元）

| | 2023 | 2024 | 2025 | 2026 最新公开口径* |
|---|---:|---:|---:|---|
| Microsoft（FY，至 6/30） | 28,107 | **44,477** | **64,551** | Calendar 2026 CapEx 预期约 **$190,000** |
| Amazon 净额 | — | **77,658** | **128,320** | 截至 2026 Q2，TTM net PPE purchase 约 **$169,000** |
| Amazon 毛额购置 | — | 82,999 | 131,819 | — |
| Amazon 出售与激励 | — | 5,341 | 3,499 | — |
| Alphabet | 32,251 | **52,535** | **91,447** | Guidance **$180,000–$190,000** |
| Meta 设备购置 | — | **37,256** | **69,691** | — |
| Meta 融资租赁本金 | — | 1,969 | 2,524 | — |
| Meta 公司口径 CapEx | — | 39,225 | 72,215 | Guidance **$125,000–$145,000**（含融资租赁本金） |

* 2026 列的时间窗和会计定义不一致，仅用于观察规模方向，不用于直接加总。

Amazon 2024 净额勾稽：82,999 − 5,341 = 77,658。  
Amazon 2025 净额勾稽：131,819 − 3,499 = 128,320。  
Meta 2024 公司口径：37,256 + 1,969 = 39,225（公司稿写 $39.23 billion）。  
Meta 2025 公司口径：69,691 + 2,524 = 72,215（公司稿写 $72.22 billion）。

## 分析性复加（非四家公司共同披露的合计）

### A. 2024 混年口径（Microsoft FY2024 + 其余 CY2024）

| 口径 | 算式 | 合计 |
|---|---|---|
| 设备购置；亚马逊用净额；Meta 不加租赁 | 44,477 + 77,658 + 52,535 + 37,256 | **211,926（$2,119 亿）** |
| 同上，Meta 用公司口径 | 44,477 + 77,658 + 52,535 + 39,225 | **213,895（$2,139 亿）** |
| 亚马逊改用毛额；Meta 不加租赁 | 44,477 + 82,999 + 52,535 + 37,256 | **217,267（$2,173 亿）** |

历史 **$215B** 口径落在第一、二行附近，说明量级接近，但不能替代逐项勾稽。

### B. 2025 实际（微软仍是 FY2025，其余 CY2025）

| 口径 | 算式 | 合计 |
|---|---|---|
| 设备购置；亚马逊净额；Meta 不加租赁 | 64,551 + 128,320 + 91,447 + 69,691 | **354,009（$3,540 亿）** |
| 同上，Meta 用公司口径 | 64,551 + 128,320 + 91,447 + 72,215 | **356,533（$3,565 亿）** |

2025 实际资本投入已经明显高于 2024 混年水平，因此不能把两个年份的汇总数混写为同一事实。

### C. 2026 最新公开规模：只比较方向，不直接复加

| 公司 | 2026 最新公开口径 |
|---|---:|
| Microsoft | Calendar 2026 CapEx 约 **$190B** |
| Amazon | 截至 2026 Q2，TTM net PPE purchase 约 **$169B** |
| Alphabet | Guidance **$180–190B** |
| Meta | Guidance **$125–145B** |

四家公司当前均处于高强度资本投入区间，但 Microsoft 的 calendar-year expectation、Amazon 的 TTM net PPE，以及 Alphabet/Meta 的 guidance 并不是同一会计量。由此只能推出“资本扩张继续抬升”，不能推出一个官方统一的“2026 四云 AI hardware CapEx”总额。

## 禁止的口径外推

- 「四云 2024 年 AI CapEx = $215B」——不存在统一 AI-specific 分项。
- 「2026 年四云 AI hardware CapEx 已统一确认为 $670–750B」——当前公开口径不足以支持这一统一定义。
- 把 NVIDIA revenue 与四云 CapEx 直接对敲——买卖双方的收入、设备购置和基础设施投资口径不同。
- Microsoft revenue 与 CapEx 属于不同分析维度；本文件仅处理 PPE/CapEx 口径，不以收入区间替代设备购置。

## 主要来源

- Microsoft：https://www.microsoft.com/en-us/investor/earnings/fy-2025-q4/cash-flows （Additions to property and equipment；FY25 / FY24 / FY23）
- Amazon：https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm （Exhibit 99.1，2026-02-05）
- Alphabet 2024：https://www.sec.gov/Archives/edgar/data/1652044/000165204425000010/googexhibit991q42024.htm
- Alphabet 2025：https://www.sec.gov/Archives/edgar/data/1652044/000165204426000012/googexhibit991q42025.htm
- Meta：https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx （2026-01-28）


> 2026 年最新口径的交叉检查见 [《核心证据台账》](核心证据台账.md) 与 [第八卷](vol-08.md)。