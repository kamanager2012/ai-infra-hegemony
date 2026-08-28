# 四云 Capex 口径核对

> 核对/更新日期：2026-08-28  
> 目的：统一 Microsoft、Amazon、Alphabet、Meta 的 CapEx / PPE 口径，避免把不同财年、不同会计科目和不同业务范围机械相加。  
> 本核对优先使用公司 IR、Exhibit 99.1、现金流量表与最新公开指引；若后续 10-K/10-Q 对相关数字重述，以最新法定申报为准。

## 结论

1. 历史口径中的 **$215B** 并不是四家公司在同一日历年、同一会计科目下披露的统一 CapEx 总额；它最接近“Microsoft 财年 + 其余三家日历年”的混合口径。
2. 按可复加的 2024 混年设备购置口径，合计约 **$211.9B–$213.9B**。因此历史 **$215B** 量级接近，但会计口径并不严格一致。
3. 这四笔均为 **company-wide CapEx / PPE**，不是“AI server / GPU”分项。Amazon 还包含 fulfillment/network infrastructure，Meta 包含 Reality Labs，Alphabet 包含办公及其他技术设施。
4. 截至 2026 年 8 月，公开规模继续上升，但时间窗和科目仍不统一：Microsoft calendar-2026 报表口径 CapEx expectation 约 **US$175B**（2026-07-29 租赁分类调整后；公司称底层投资预期不变）；Alphabet Q2 earnings-call guidance **US$195–205B**；Meta Q2 guidance **US$130–145B**；Amazon 截至 2026-06-30 的 TTM PPE net purchases actual **US$169.007B**。这些数字可以用于判断资本扩张方向，但**不能机械复加成统一“2026 AI hardware CapEx”**。

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
| Microsoft（FY，至 6/30） | 28,107 | **44,477** | **64,551** | Calendar-2026 报表口径 expectation 约 **US$175B**（租赁分类调整后） |
| Amazon 净额 | — | **77,658** | **128,320** | 截至 2026-06-30，TTM PPE net purchases actual **US$169.007B** |
| Amazon 毛额购置 | — | 82,999 | 131,819 | — |
| Amazon 出售与激励 | — | 5,341 | 3,499 | — |
| Alphabet | 32,251 | **52,535** | **91,447** | Q2 earnings-call guidance **US$195–205B** |
| Meta 设备购置 | — | **37,256** | **69,691** | — |
| Meta 融资租赁本金 | — | 1,969 | 2,524 | — |
| Meta 公司口径 CapEx | — | 39,225 | 72,215 | Q2 guidance **US$130–145B**（含 finance-lease principal） |

* 2026 列混合公司 guidance 与 Amazon TTM actual，且时间窗、租赁分类和会计定义不一致，仅用于观察规模方向，不用于直接加总。

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
| Microsoft | Calendar-2026 reported CapEx expectation 约 **US$175B** |
| Amazon | 截至 2026-06-30，TTM PPE net purchases actual **US$169.007B** |
| Alphabet | Q2 earnings-call guidance **US$195–205B** |
| Meta | Q2 guidance **US$130–145B** |

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
- Microsoft 最新 calendar-2026 口径：https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4 （2026-07-29；约 US$175B，租赁分类调整）
- Amazon 2026 Q2 10-Q：https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm （TTM PPE net purchases US$169.007B）
- Alphabet 最新 guidance：2026 Q2 earnings call，公开报道记录为 US$195–205B；在官方 transcript 可稳定归档前，保留来源身份，不升级为法定申报 actual。
- Meta 2026 Q2 SEC Exhibit 99.1：https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm （guidance US$130–145B）
- Meta 2025 actual：https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx


> 2026 年最新口径的交叉检查见 [《核心证据台账》](核心证据台账.md) 与 [第八卷](vol-08.md)。