# Part IV · 第31章：2036 终局与战略选择

## 1. 2036 不是市场份额预测点，而是战略时间尺度

本报告不预测 2036 年某家公司拥有多少市场份额，也不为 S1–S4 分配固定概率。

2036 的意义是把当前机制拉到更长时间尺度，回答一个更重要的问题：

> **当 compute、memory、packaging、software、power 与 capital 继续演化十年后，产业的选择权会变多还是变少？**

竞争单位已经从单颗芯片上移到 system stack。

因此，长期竞争不再只是：

> 谁拥有更快 accelerator

而是：

> **谁能够持续获得关键物理资源、组织完整系统、降低迁移成本，并把基础设施转化为高利用率 workload。**

---

## 2. 2036 的五个真正分水岭

长期产业结构主要取决于五个问题。

### 2.1 System Portability

不同 system stack 之间的 workload 能否以可接受成本迁移？

如果 compiler/runtime、model format、networking 与 orchestration 更开放，buyer optionality 会提高。

如果 proprietary interfaces 与 platform-specific engineering 继续强化，switching cost 会成为更大的产业壁垒。

### 2.2 Scarce-Layer Supply Elasticity

advanced logic、HBM、advanced packaging 是否出现更多 qualified supply？

如果 supply elasticity 提高，资源集中度下降。

如果多个 scarce layers 长期同时紧张，system platform 与大型 anchor buyer 的 supply coordination advantage 会增强。

### 2.3 Time-to-Power

powered land、grid connection、substation 与 firm power 是否持续成为 deployment quota？

如果 Time-to-Power 长期无法缩短，AI competition 会越来越具有基础设施和地理属性。

### 2.4 Workload Monetization

AI workload 是否能够产生足够现金流覆盖：

- compute depreciation；
- data-center cost；
- power；
- operations；
- financing。

这是决定资本扩张最终可持续性的根本变量。

### 2.5 Financing Independence / Demand Quality

长期 compute demand 是由谁的资产负债表承担？

2026 年 8 月的新结构已经显示，compute financing 正从单一 corporate CapEx 扩展到 third-party capital、LPS credit support 与 seller-assisted financing。[^4][^5]

需要区分：

- independently financed customer demand；
- long-duration Anchor Buyer commitment；
- third-party infrastructure capital；
- supplier equity / credit enhancement。

如果 utilization 与 monetization 健康，seller-assisted financing 可以降低资本形成摩擦；如果 customer cash generation 走弱，而 supplier support 与 refinancing dependency 持续上升，则产业对少数 balance sheets 的依赖反而增强。

因此，2036 的一个关键问题是：

> **AI infrastructure 能否从“需要持续 seller / sponsor support 的扩张”演化成能够由独立 workload cash flow 和长期资本自我承销的资产体系。**

S1–S4 的完整定义见[第30章：S1–S4 四类标准情景](part-IV-ch30-scenarios.md)。

---

## 3. 当前战略基准：高增长、高集中、替代路径同时存在

截至 2026 年 8 月，当前事实组合仍最接近 **S2 — Baseline Concentration**。

主要原因包括：

- leading system-platform economics 仍强；[^1]
- advanced packaging 仍是公开确认的增长约束；[^2]
- HBM / server memory 对制造资源的影响仍强；[^3]
- cloud custom systems 已形成真实第二路线，但尚未证明全面替代 frontier workload；
- power 已进入独立 physical constraint；
- China production-grade parallel stack 持续发展，但 autonomous frontier closure 尚未在所有 critical layers 得到规模化证明；
- 全行业 Capital Hard Landing 的同步证据仍不足。

这不是十年固定预测。

它只是当前战略选择的起点。

---

## 4. 企业：先证明 Workflow Economics，再锁长期 Compute

企业部署 AI 的合理顺序是：

1. 找到可量化的真实 workflow；
2. 建立 evaluation / verification；
3. 计算 cost per completed task 与业务价值；
4. 测量 human review、failure 与 retry；
5. 保留 model / cloud / data portability；
6. 根据需求确定性决定长期 compute commitment。

高确定性的 production workload 可以使用较长期 reservation。

不确定的实验、模型快速变化领域，则应保留 flexible / multi-provider 路径。

最危险的顺序是：

> **先锁定大量长期 capacity，再寻找足以填满它的业务需求。**

---

## 5. 企业：主栈可以集中，但第二路径必须真实可执行

portability 不意味着所有供应商平均采购。

更有效的策略是：

> **主栈追求效率，第二路径追求选择权。**

第二路径至少应验证：

- model portability；
- data portability；
- cloud portability；
- accelerator / runtime optionality；
- open interfaces；
- workload benchmark；
- cost observability；
- operational recovery。

如果第二路径只存在于采购 PPT，而没有真实 production validation，就不能提供有效 bargaining power 或 resilience。

---

## 6. 资本：必须先区分资产类型，再谈“AI 估值”

AI 相关资产至少可以分成四类：

**Table 31.1 — AI 相关资产的主要价值来源与风险**

| 资产 | 主要价值来源 | 主要风险 |
|---|---|---|
| System Platform | switching cost / system definition / ecosystem | substitution / regulation |
| Manufacturing | scarcity / yield / technology / capacity | cycle / CapEx / utilization |
| Infrastructure | powered land / grid / data center / duration | utilization / duration mismatch |
| Application | workflow / distribution / data | commoditization / unit economics |

**Source:** 本报告 Value Capture / Duration framework。  
**Note:** 该分类用于产业战略分析，不构成证券估值或投资建议。

同样的 revenue growth，在不同资产类型上具有完全不同的资本回报含义。

因此，资本判断不能只看：

- revenue growth；
- CapEx；
- valuation multiple。

还必须同时看：

- utilization；
- FCF；
- forward commitments；
- residual value；
- asset duration；
- customer concentration；
- third-party risk capital；
- supplier equity / credit support；
- refinancing dependency。

---

## 7. 资本：最大结构风险是 Duration Mismatch

AI infrastructure 同时包含：

- 短周期 accelerator / server；
- 中周期 network / cooling；
- 长周期 data-center shell；
- 更长周期 grid / generation / PPA。

如果短周期 workload demand 与 long-duration debt、PPA、data-center assets 绑定，一旦 demand 不及预期，清算不会同步发生。

因此，核心问题不是：

> “AI CapEx 是否太高？”

而是：

> **demand duration 是否与 asset duration 匹配？**

高需求环境中，长久期资产可以形成 moat。

在 S4 中，同一资产会转化成 stranded-capacity 与 refinancing risk。

---

## 8. 国家：竞争单位已经不是一座 Fab

完整 frontier AI industrial capability 至少需要：

- equipment / materials；
- advanced logic；
- HBM；
- advanced packaging；
- interconnect；
- compiler/runtime；
- data center；
- power / grid；
- engineering talent；
- production operations。

因此，单纯补贴一座先进 fab 不等于形成 frontier AI industrial capability。

国家层面真正需要的是：

> **system-level continuity**

即关键环节发生外部中断时，整个 system 能否继续以可接受成本运行、扩张和迭代。

---

## 9. 国家：Power Policy 已经成为 Compute Policy

高功率 AI system 已经把：

- generation；
- transmission；
- grid interconnection；
- substation；
- transformer；
- cooling；
- permitting；

拉入算力竞争。

如果 semiconductor supply 增长，而 Time-to-Power 不改善，就会形成：

> **hardware available + deployment unavailable**

因此，国家 AI infrastructure strategy 必须同时处理：

> **semiconductor clock + power clock + capital clock**

Power 不能再被当成数据中心建设完成后的运营问题。

---

## 10. 国家：Interoperability 是战略选择权，而不是平均市场份额

系统韧性并不要求拒绝领先平台。

真正需要避免的是：

> **所有关键 workload 同时依赖一条不可替代技术路径。**

长期应提高：

- open compiler/runtime；
- portable model / data formats；
- interoperable networking；
- multi-architecture engineering capability；
- cross-stack production benchmarking。

目标不是人为平均市场份额，而是保证：

> **供应中断、价格失衡、政策变化或平台条件变化时，替代路径可以真正执行。**

---

## 11. 中国：长期核心指标不是“国产化率”，而是两级 Closure

China parallel stack 是否改变全球产业结构，不取决于一个总国产化率。

第一层应验证 **Production-Grade Parallel Stack**：

- accelerator / compute；
- HBM-class 或 equivalent memory subsystem；
- advanced packaging；
- high-speed interconnect；
- compiler/runtime；
- production workload；
- utilization / reliability / system economics。

第二层再验证 **Autonomous Frontier Closure**：

- advanced manufacturing continuity；
- equipment / materials / software / service；
- cross-generation process upgrade；
- long-duration HBM / packaging / LPS / power / capital continuity。

consumer / smartphone supply success 不能直接证明 autonomous frontier closure。

但同样，存在进口依赖也不能否定已经形成的 production-grade substitution。

如果 production-grade stack 持续扩大，中国会形成更强的第二资源重力中心；如果 upstream continuity 也跨代闭环，则其战略意义将从 domestic resilience / selected substitution 上升到更高程度的 autonomous frontier competition。

---

## 12. 劳动与人才：价值从“会用工具”转向“能对结果负责”

模型、IDE、agent 与生成工具会快速商品化。

因此，长期更耐久的能力不是绑定某一个 AI product，而是：

- domain knowledge；
- problem decomposition；
- system / workflow design；
- verification；
- cross-stack portability；
- risk judgment；
- 对最终结果负责。

这与产业结构变化是一致的：

> **当执行成本下降，定义问题、组合系统、验证结果和承担责任的价值会上升。**

劳动和教育的完整分析见第25、26章。

---

## 13. 什么事实会改变战略方向

未来最重要的更新变量包括：

- leading system seller commitments 是否持续扩大或开始收缩；
- cloud custom stacks 的 production workload share；
- migration cost 是否下降；
- HBM / advanced-packaging tightness 是否缓解；
- leading-edge capacity access 是否更分散；
- energized MW / Time-to-Power 是否改善；
- Anchor Compute Buyer commitments 是否兑现；
- AI monetization 是否覆盖资本基数；
- China production-grade parallel stack / autonomous frontier closure 是否获得更多一手规模化证据；
- supplier-assisted financing 是否仍由独立 workload cash flow、third-party capital 与高 utilization 支撑；
- regulation 是否真实降低 interface / tying / switching barriers。

这些变量的变化决定 S1–S4 的相对权重，而不是一个固定十年预测。

---

## 14. 最终战略判断

截至 2026 年 8 月，AI infrastructure 仍处在：

> **高速扩张 + 高集中 + 替代系统加速形成**

同时存在的阶段。

未来十年的真正竞争，不是简单判断“谁会赢”，而是持续围绕：

- system substitution；
- scarce-layer supply；
- power；
- Anchor Buyer demand；
- workload monetization；
- capital duration / financing quality；
- regulation；
- geopolitical redundancy；

重新分配产业权力和资本回报。

对企业、资本和国家，最重要的共同原则可以压缩成一句：

> **不要押注一个永远不变的终局；建立在终局变化时仍然可执行的选择权。**

## 15. 什么事实会迫使本章改判

长期战略选择应随以下变量改变：

- multi-stack portability 是否从“备选”变成 production 常态；
- scarce-layer supply 是否出现 durable abundance；
- Time-to-Power 是否显著缩短；
- workload monetization 是否能够独立覆盖 capital cost；
- supplier-assisted financing 是否下降、独立长期资本是否上升；
- China production-grade stack / autonomous closure 是否跨越更多关键层。

因此，本章给出的不是固定十年终局，而是一组在这些变量变化时必须重新排序的战略优先级。

## References

[^1]: NVIDIA, FY27 Q2 official results, current system-platform economics, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^2]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging supply constraint, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^3]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^4]: NVIDIA, 2026-08-10, AI compute infrastructure financing platforms and >US$500B third-party-capital mobilization target, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Partners-With-Apollo-BlackRock-Blackstone-Brookfield-Goldman-Sachs-and-KKR-to-Establish-AI-Compute-Infrastructure-Financing-Platforms-to-Mobilize-Over-500-Billion-of-Third-Party-Capital/default.aspx
[^5]: NVIDIA, 2026-08-17, PORTS-Pike / SB Energy / OpenAI, LPS credit support and initial 4.25 IT-GW design capacity, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx

## 交叉引用

- [第25章：AI 与劳动市场](part-III-ch25-labor-market.md)
- [第26章：AI 时代教育与人才体系](part-III-ch26-education-talent.md)
- [第30章：S1–S4 四类标准情景](part-IV-ch30-scenarios.md)
- [第32章：总判](part-IV-ch32-master-judgment.md)
