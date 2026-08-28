# 第十四卷：AI 基础设施价值捕获地图——谁获得利润，谁承担残量压力

## 1. “赢家与输家”不能按行业标签粗暴划分

AI infrastructure 的价值重新分配不是“半导体赢、软件输”这么简单。

真正决定利润归属的是：

- 是否控制 scarce layer；
- 是否拥有 switching cost；
- 是否能锁定长期 demand；
- 是否承担重资产；
- 是否拥有定价权。

因此，本卷采用 **Value Capture Map**，而不是简单赢家/输家名单。

## 2. 第一类：System Platform

代表性角色是拥有：

- accelerator；
- interconnect；
- software/runtime；
- rack architecture；
- customer ecosystem

的系统平台。

这类公司的优势来自：

> 将多个独立稀缺环节组织成一个高价值系统，并获得系统级毛利。

NVIDIA 当前是最典型案例。

FY27 Q2：

| 指标 | 数值 |
|---|---:|
| Revenue | **US$96.221B** |
| Data Center revenue | **US$89.0B** |
| GAAP gross margin | **75.0%** |
| GAAP operating income | **US$63.734B** |

来源：https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027

这是当前 AI infrastructure 中最强的 seller-side value capture 之一。

## 3. 第二类：HBM / Memory Supplier

SK hynix、Samsung、Micron 获益于 HBM product mix 上移。

HBM 的价值来自：

- high bandwidth；
- high stacking complexity；
- advanced packaging integration；
- high wafer-supply trade ratio。

SK hynix FY25 Operating margin 达到 **49%**，HBM revenue more than doubled YoY。

来源：https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/

但 memory supplier 的利润仍具有周期性。

如果 HBM supply 过度扩张、需求下降或 conventional DRAM 恢复宽松，利润率可以快速回落。

因此，它们是**稀缺周期赢家**，但不等于拥有永久平台控制权。

## 4. 第三类：Advanced Foundry / Packaging

TSMC 是典型的 manufacturing bottleneck owner。

其价值来自：

- leading-edge process；
- yield；
- customer trust；
- advanced packaging；
- roadmap execution。

TSMC 2025 gross margin **59.9%**，HPC platform 占全年 revenue **58%**。TSMC 4Q25 transcript 的公司会后更正口径是 **advanced packaging slightly over 10% of 2025 revenue**；这不能扩写成 2025 “advanced packaging + testing”。管理层在 2026 Q2 又明确表示 packaging tightness 已经限制客户增长。

来源：
- https://investor.tsmc.com/static/annualReports/2025/english/index.html
- https://investor.tsmc.com/english/quarterly-results/2026/q2

这些事实说明制造价值正在从单纯 transistor scaling 向 system integration 扩展。

但 TSMC 的商业模式仍是 manufacturing service，平台利润和制造利润不能混为一谈。

## 5. 第四类：Power / Powered Land

随着 rack density 上升，拥有：

- powered land；
- grid connection；
- firm generation；
- long-duration PPA；
- substation capacity

的资产开始获得更高战略价值。

这类资产的特点是：

- 复制慢；
- 地理固定；
- 许可周期长；
- 与 AI data center deployment 直接绑定。

如果 power bottleneck 持续，价值捕获可能进一步向 energy/infrastructure 迁移。

## 6. Hyperscaler：既是赢家，也是最大的资本承担者

Microsoft、Amazon、Alphabet、Meta 既拥有：

- cloud distribution；
- customer base；
- internal workload；
- custom silicon；

又承担巨额：

- CapEx；
- depreciation；
- power；
- data center；
- network investment。

因此，它们不能简单归类为“输家”。

更准确的判断是：

> hyperscaler 通过规模和自研系统争夺 platform profit，但同时承担整个 AI infrastructure cycle 最大的资产负债表风险之一。

## 7. Model Company：利润池最不稳定的一层

模型公司拥有：

- model capability；
- brand；
- API；
- workflow；
- user distribution。

但它们面临：

- model commoditization；
- open-source competition；
- inference cost；
- cloud bargaining；
- customer switching；
- rapid price compression。

因此，模型层利润能否长期存在取决于 **AI Software Unit Economics**。

最有价值的模型公司需要把“模型能力”转化为：

- workflow lock-in；
- proprietary data；
- user distribution；
- measurable business outcome。

## 8. Traditional SaaS：不是必然输，而是成本结构被改变

AI 功能进入 SaaS 后，软件公司会新增：

- inference；
- retrieval；
- storage；
- tool/API；
- human review

成本。

因此，传统“新增一个用户几乎没有边际成本”的模型受到挑战。

但这不意味着 SaaS gross margin 必然降到某个固定数字。

真正需要观察的是：

- AI gross margin；
- cost per completed workflow；
- price uplift；
- retention；
- productivity gain。

## 9. Consumer electronics：承受 residual-capacity pressure

Smartphone、PC、gaming、general server 并没有消失。

它们受到的主要影响是：

- advanced logic allocation；
- DRAM residual supply；
- consumer GPU supply；
- component price。

因此，它们更像**残量压力承担者**，而不是“被 AI 淘汰的行业”。

## 10. 当前价值捕获排序

截至 2026 年 8 月，AI infrastructure 的价值捕获大致呈现：

> **System platform**  
> → **HBM / advanced packaging / leading-edge manufacturing**  
> → **powered infrastructure**  
> → **hyperscaler platform**  
> → **model / application layer**

这不是固定排名。

如果 custom silicon、open software 与 power expansion 成功，价值可能向 cloud 和 application layer 回流。

如果 physical bottleneck 继续强化，则更多利润会留在 scarce infrastructure layer。

## 11. 当前判断

AI 时代真正的“赢家”不是某个行业，而是能够控制以下至少一种资源的主体：

- system definition；
- scarce manufacturing；
- memory bandwidth；
- migration cost；
- power；
- distribution；
- proprietary workflow。

因此，本报告后续不使用简单“谁赢谁输”的静态表，而使用 **Value Capture Map + Scenario Matrix** 判断利润如何在不同情景下迁移。

## 本卷关键公开来源

- NVIDIA FY27 Q2 official results：https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- TSMC 2025 Annual Report：https://investor.tsmc.com/static/annualReports/2025/english/index.html
- TSMC 2026 Q2 IR / transcript（packaging tightness limits customer growth）：https://investor.tsmc.com/english/quarterly-results/2026/q2
- SK hynix FY25 official results（Operating margin 49%; HBM revenue more than doubled YoY）：https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/

- TSMC 4Q25 Transcript（2025 advanced packaging slightly over 10%，company-corrected）：https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
