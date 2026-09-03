# Part III · 第20章：AI Infrastructure Stack 的 Value Capture 与 Risk Bearing

## 1. Value Capture 与 Risk Bearing 是两张不同的 Map

同一美元 AI infrastructure spending 可以在产业链不同位置表现为 hyperscaler CapEx、system-vendor revenue、foundry revenue、memory revenue、packaging revenue 与 data-center / power investment。它们是同一资本流在不同账本上的 accounting view，不是互相独立的多笔资金。

因此真正需要回答的不是“全球利润池到底多大”，而是：

> **哪一层捕获 economic rent，哪一层承担 asset risk；当 scarcity、switching cost、utilization 或 financing condition 改变时，两者如何重新分配？**

本章把 value capture 与 risk bearing 分开分析，避免 double counting，也避免固定 winner / loser ranking。

## 2. 六个变量决定 Economic Rent

判断一层产业能留下多少利润，至少要同时看：

1. **Scarcity**：供给能否快速扩张；
2. **Switching cost**：客户迁移到替代方案的工程/组织成本；
3. **Capital intensity**：维持增长需要投入多少固定资本；
4. **Duration**：收入、资产寿命和合同期限是否匹配；
5. **Distribution / workflow control**：是否拥有客户、数据和真实业务入口；
6. **Financing / risk-transfer capacity**：是否能够降低项目资本成本、提高 revenue visibility，并把 residual-value / duration risk 转移给愿意承担它的资本。

因此，高 revenue share 不自动等于最高 value capture，高 gross margin 也不能跨商业模式直接比较。

## 2A. 经营价值捕获与资本市场估值运行在不同 Clock

一家企业可以已经形成很强的经营利润，却未必获得最高估值倍数；也可以先获得极高资本市场估值，而经营经济性尚未完全兑现。

因此，本报告必须把三层分开：

- **Operating Value Capture：** revenue、gross / operating profit、free cash flow、unit economics 与 cash conversion；
- **Market Position：** scarcity、switching cost、distribution、supply access 与 bargaining power；
- **Capital-Market Valuation：** market cap、equity multiple、debt pricing 与 financing flexibility。

三者会互相影响，但不能互相替代。

更强的市场地位可以支持 margin 与 cash flow；更强 cash flow 又能提高融资能力；更高 market valuation 则可能降低 equity financing friction、提高并购货币价值、强化人才激励，并扩大供应链预付款与 strategic investment 的可执行空间。

但必须始终保留：

> **market cap ≠ cash flow ≠ economic rent ≠ physical resource control**

只有当估值能够被转化成真实 financing capacity，而且底层 operating economics 仍然可信时，这个反馈才真正具有产业战略意义。

这也是本章 Value Capture Map 与第23章“五维资本观察框架”之间的连接点。

---

## 3. System Platform 通过 Coordination 与 Switching Cost 变现

NVIDIA 是当前最清晰的 system-platform 案例。FY27 Q2：Revenue **US$96.221B**、Data Center revenue **US$89.0B**、GAAP gross margin **75.0%**、GAAP operating income **US$63.734B**。[^1]

这一层的价值不只是 accelerator die，而来自 compute、HBM、interconnect、software/runtime、rack architecture 与 deployment tooling 的系统整合。系统平台的优势在于：

- 可以把多个外部 scarce input 组织成一个采购单元；
- software / fabric / deployment 形成 switching cost；
- 高 cash generation 可以支持下一代 supply commitments；
- roadmap coordination 让客户更容易留在同一平台跨代升级。

但 system platform 也不拥有所有物理投入。foundry、HBM、advanced packaging 和 power 仍是外部边界。

## 4. Foundry / Packaging 可以控制 Quantity，但不一定拥有最高 Margin

TSMC 2025 gross margin 为 **59.9%**，HPC platform 占全年 revenue **58%**。[^2] 2025 的公司更正口径为 **advanced packaging slightly over 10% of revenue**，[^3] 而 2026 Q2 管理层进一步表示 packaging tightness 已经限制客户增长。[^4]

这说明制造价值已经从 transistor scaling 扩展到 system integration。但 foundry / packaging 与 system platform 的经济模型不同：

> **manufacturing service + yield + utilization + CapEx execution**

而不是 software switching cost 主导的 asset-light platform economics。

所以一个制造层可以成为物理 bottleneck，却不必拥有全产业最高 margin；**bottleneck location ≠ profit location**。

## 5. Memory 捕获 Scarcity Rent，但仍然具有周期性

SK hynix FY25 官方结果为 Revenue **KRW 97.1467T**、Operating profit **KRW 47.2063T**、Operating margin **49%**，HBM revenue 同比超过一倍。[^5]

Micron 的一手披露又说明：same node / same bits 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。[^6] 这使 HBM 的 value capture 同时来自 bandwidth value、制造投入密度、stacking/qualification 与短期 supply scarcity。

但 memory 仍具有明显周期性。如果 HBM capacity 超前扩张、generation mismatch 上升或 demand 增速下降，利润可以快速回吐。因此，memory 更接近**高壁垒的制造稀缺周期**，不是永久平台租金。

## 6. Hyperscaler 同时拥有 Distribution Power 与 Duration Risk

Microsoft、Amazon、Alphabet、Meta 同时拥有 cloud distribution、internal workload、customer base、custom silicon 和 data-center scale。这让它们有能力把一部分 platform economics 内部化。

但 cloud buyer 同时承担：

- server / accelerator；
- network；
- data-center shell；
- cooling；
- power / land；
- depreciation；
- utilization risk。

所以 hyperscaler 不能简单归为“赢家”或“输家”。它们最强的资产是 distribution + workload + capital；最危险的资产是长期 infrastructure 先建设、workflow revenue 后兑现所形成的 duration mismatch。

## 7. Supply Commitments 把 Platform Cash Flow 连接到 Manufacturing Capacity

NVIDIA 披露的 **forward supply / capacity commitment family** 从 2026-01-25 的 **US$95.2B** 上升到 2026-04-26 的 **US$119B**，再到 2026-07-26 的 **US$279B**。[^7]

FY27 Q2 10-Q 说明最新 commitments 主要关联 data-center infrastructure systems 所需的 memory 与 manufacturing facilities。它可以作为**未来资源锁定强度的财务 proxy**，但公开文件没有 supplier-level split，因此不能写成 TSMC、SK hynix、Micron 或任何单一供应商“已经收到多少”。

这也是 value capture 的重要动态：高 seller cash flow 可以更早变成下一代 wafer、memory、packaging 和 component commitments。

## 7A. Financing Coordination 正成为 System Capability

2026 年 8 月的两项披露说明，system-platform coordination 已经从 supply commitments 延伸到 infrastructure finance：

- NVIDIA 与 Apollo、BlackRock、Blackstone、Brookfield、Goldman Sachs、KKR 宣布建立 compute-financing platforms，目标是随时间动员 **>US$500B third-party capital**；相关合作仍 subject to final agreements。[^9]
- PORTS-Pike 中，NVIDIA 为 land + power + shell 提供 credit support，并投资 **US$1.5B** 于 SB Energy；OpenAI 为客户，SB Energy build / own / operate data center。[^10]

这意味着 value capture 不再只取决于“谁控制技术”和“谁控制物理稀缺”，还取决于：

> **谁能够把长期 workload、基础设施资产与长期资本匹配起来，并降低项目的 financing friction。**

但融资协调能力同时会改变风险承担位置。

如果 seller 通过 equity / credit support 帮助客户和基础设施项目融资，则：

- project formation 加快；
- seller 对 future workload 的影响力上升；
- customer concentration 与 financing reflexivity 也上升。

因此：

> **financing coordination 可以强化 platform advantage，但必须与 risk transfer 和 workload monetization 一起判断。**

完整机制见第23、24章。

## 8. Powered Land 捕获 Time-to-Power Scarcity

当 rack power 进入约 **120 kW-class**，[^8]数据中心需要更强的 grid connection、substation、transformer、cooling 与 firm generation。拥有 powered land、existing interconnection 和可执行许可路径的资产会获得明显 **Time-to-Power** 价值。

这层资产的特点是：复制慢、地理固定、许可周期长、合同期限往往长于 compute generation。

因此 power 可以成为 scarce layer，但其经济性必须与 utilization 和合同久期一起分析。长期 PPA 在高需求情景中是 hedge / moat，在 S4 中也可能成为 long-duration obligation。

## 9. Model / Application 的价值取决于 Workflow Economics

模型公司与 AI software 拥有 model capability、API、user distribution 和 workflow 入口，但也面对 open-source competition、inference/retrieval/tool cost、cloud bargaining 与快速价格压缩。

传统 SaaS 的高毛利不能直接套到 AI application。正确单位是 **AI Software Unit Economics**：

> Revenue or productivity value − inference − retrieval/storage − tools/APIs − human review − AI-specific cloud cost

真正有防御力的 application layer 需要把模型能力转化成 proprietary workflow、data、distribution、retention 和 measurable business outcome。

## 10. End Systems 吸收 Residual-Capacity 与 Quantity-Assurance Pressure

smartphone、PC、game consoles、automotive、industrial systems、robotics 与部分 high-reliability electronics 仍然是重要的终端和战略系统。它们承受的主要不是“被 AI 淘汰”，而是共享或相邻上游资源的再排序。

对 end system，更相关的暴露变量是 **residual capacity 与 supply assurance**，而具体 physical channel 并不相同：

- smartphone / PC 更直接暴露于 selected leading-edge logic、DRAM/LPDDR/NAND、consumer GPU 与 selected packaging；
- game consoles 暴露于 custom SoC/APU、GDDR/DRAM、NAND/SSD 与 long-generation hardware economics，memory procurement 可以直接传导到 promotion、unit volume 与 hardware margin；
- automotive / industrial 更受 mature memory、MCU/analog、power、qualification 与 long-life supply 影响；
- robotics 同时连接 industrial electronics 与 edge/cloud AI；
- defense / aerospace / space electronics 的核心约束更多是 trusted、qualified、low-volume、long-life、RF/power、rad-hard 与 special-process continuity，而不是直接争夺同一批 HBM。

因此，不能给“整机层”排一个统一利润名次，也不能把所有下游压力归因于 AI。真正需要观察的是：

> **shared-resource exposure + buyer power + qualification rigidity + supply assurance + product-mix reallocation**

第3章定义资源机制，第21章讨论已经能够观测到的 price / configuration / longevity / allocation 传导。

## 11. Custom Silicon 会先重新分配 Platform Rent，再影响 Upstream Demand

传统路径可以近似写成：

> cloud / model buyer → system platform → foundry / HBM / packaging → equipment/materials → power/data-center

当 hyperscaler 使用 custom silicon 时，部分资金可能绕开 NVIDIA：

> cloud → custom system → foundry / HBM / packaging

这会改变 platform profit 的归属，却未必降低 advanced logic、HBM、packaging 与 power 的总需求。

因此，system-stack substitution 既是利润分配变量，也是上游资源竞争变量。

## 12. Value Capture 取决于 Scenario

不同情景会改变 value capture：

- **S1 Competitive Expansion**：custom stack、open software 和 supply expansion 降低平台租金，价值更分散；
- **S2 Baseline Concentration**：system platform 与 scarce manufacturing 保持强 value capture，cloud 继续高投入；
- **S3 Resource Hegemony**：logic/HBM/packaging/power 进一步集中，scarce-layer owners 与 dominant system platform 获取更强议价；
- **S4 Capital Hard Landing**：buyer utilization 与 commitments 下滑，长期基础设施首先面临 duration/ROI 压力，上游利润随后传导回落。

这比给 system platform、HBM、foundry、cloud、application 排一个永久名次更可靠。

## 13. Current Read

截至 2026 年 8 月，AI infrastructure 中最有力的 durable value-capture evidence 主要集中在三类位置：

1. **能够组织多个稀缺层并制造 switching cost 的 system platform；**
2. **短期供给弹性低、进入壁垒高的 HBM / leading-edge manufacturing / advanced packaging / powered infrastructure；**
3. **能够把长期 workload、LPS / compute assets 与长期资本组织起来的 financing / coordination layer。**

但第三类的 value capture 与 risk transfer 必须一起看：如果 platform 同时提供 equity / credit support，它获得更多 infrastructure influence 的同时，也可能重新吸收部分 customer / duration / residual-value risk。

应用层是否形成长期利润池，仍取决于 workflow economics 和 distribution。

因此，真正应该问的不是“AI 一共花了多少钱”，而是：

> **同一笔资本在每一层留下多少可重复现金流、形成多少不可替代性，又把多少长期风险留在资产负债表上。**

## 14. 什么事实会改变当前判断

当前 value-capture map 应在以下变化下重估：

- system portability 显著提高、switching cost 下行；
- HBM / packaging / power scarcity premium 持续消失；
- financing coordination 无法带来更低资本成本或更高 utilization；
- supplier-assisted financing 开始造成明显 credit / impairment loss；
- application-layer workflow economics 显著改善并形成更稳定利润池；
- upstream manufacturing 的竞争格局出现真实 second source。

value capture 不是永久排名，而是 scarcity、switching cost、capital intensity 与 risk transfer 的动态结果。

## References

[^1]: NVIDIA, “NVIDIA Announces Financial Results for Second Quarter Fiscal 2027,” https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^2]: TSMC, 2025 Annual Report, gross margin and platform mix, https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^3]: TSMC, 4Q25 Earnings Conference Transcript, advanced packaging slightly over 10% of 2025 revenue, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
[^4]: TSMC, 2Q26 Earnings Conference Transcript, packaging tightness limiting customer growth, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/547d1696765e05ce3adb81c108ce1c8c1682b80c/TSMC%202Q26%20Transcript.pdf
[^5]: SK hynix, FY25 Financial Results, https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
[^6]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^7]: NVIDIA Corporation, FY26 Form 10-K, US$95.2B manufacturing / supply / capacity commitments as of 2026-01-25, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm ; FY27 Q2 Form 10-Q, US$119B last quarter and US$279B as of 2026-07-26, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^8]: NVIDIA, DGX GB200 Hardware Guide, rack power approximately 120 kW, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
[^9]: NVIDIA, 2026-08-10, AI compute infrastructure financing platforms and >US$500B third-party-capital mobilization target, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Partners-With-Apollo-BlackRock-Blackstone-Brookfield-Goldman-Sachs-and-KKR-to-Establish-AI-Compute-Infrastructure-Financing-Platforms-to-Mobilize-Over-500-Billion-of-Third-Party-Capital/default.aspx
[^10]: NVIDIA, 2026-08-17, PORTS-Pike / SB Energy / OpenAI, LPS credit support, US$1.5B SB Energy investment and initial 4.25 IT-GW design capacity, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx
