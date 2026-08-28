# Part III · 第20章：Value Capture Map——资金流、利润池与风险承担

## 1. 同一美元不能在产业链上重复计算

AI infrastructure 的同一笔支出可能同时出现在：

- hyperscaler CapEx；
- system-vendor revenue；
- foundry revenue；
- memory-vendor revenue；
- packaging revenue；
- data-center / power investment。

这些并不是六笔互相独立的钱。买方购入一套 system，卖方确认 revenue；卖方再向 foundry、memory 和 components 采购；cloud 同时建设机房和电力。把各层 headline number 直接相加，会发生严重 double counting。

因此，本章只分析**价值捕获位置**和**风险承担位置**，不制造一个不可审计的全球总利润池。

## 2. Value Capture 由五个维度决定

判断一层产业能留下多少利润，至少要同时看：

1. **Scarcity**：供给能否快速扩张；
2. **Switching cost**：客户迁移到替代方案的工程/组织成本；
3. **Capital intensity**：维持增长需要投入多少固定资本；
4. **Duration**：收入、资产寿命和合同期限是否匹配；
5. **Distribution / workflow control**：是否拥有客户、数据和真实业务入口。

因此，高 revenue share 不自动等于最高 value capture，高 gross margin 也不能跨商业模式直接比较。

## 3. System Platform：把多个 scarce layer 组织成一套高价值产品

NVIDIA 是当前最清晰的 system-platform 案例。FY27 Q2：Revenue **US$96.221B**、Data Center revenue **US$89.0B**、GAAP gross margin **75.0%**、GAAP operating income **US$63.734B**。

这一层的价值不只是 accelerator die，而来自 compute、HBM、interconnect、software/runtime、rack architecture 与 deployment tooling 的系统整合。系统平台的优势在于：

- 可以把多个外部 scarce input 组织成一个采购单元；
- software / fabric / deployment 形成 switching cost；
- 高 cash generation 可以支持下一代 supply commitments；
- roadmap coordination 让客户更容易留在同一平台跨代升级。

但 system platform 也不拥有所有物理投入。foundry、HBM、advanced packaging 和 power 仍是外部边界。

## 4. Foundry / Advanced Packaging：重资产制造可以成为数量闸门

TSMC 2025 gross margin 为 **59.9%**，HPC platform 占全年 revenue **58%**。2025 的公司更正口径为 **advanced packaging slightly over 10% of revenue**，而 2026 Q2 管理层进一步表示 packaging tightness 已经限制客户增长。

这说明制造价值已经从 transistor scaling 扩展到 system integration。但 foundry / packaging 与 system platform 的经济模型不同：

> **manufacturing service + yield + utilization + CapEx execution**

而不是 software switching cost 主导的 asset-light platform economics。

所以一个制造层可以成为物理 bottleneck，却不必拥有全产业最高 margin；**bottleneck location ≠ profit location**。

## 5. HBM / Memory：高制造投入与产品周期共同创造稀缺利润

SK hynix FY25 官方结果为 Revenue **KRW 97.1467T**、Operating profit **KRW 47.2063T**、Operating margin **49%**，HBM revenue 同比超过一倍。

Micron 的一手披露又说明：same node / same bits 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。这使 HBM 的 value capture 同时来自 bandwidth value、制造投入密度、stacking/qualification 与短期 supply scarcity。

但 memory 仍具有明显周期性。如果 HBM capacity 超前扩张、generation mismatch 上升或 demand 增速下降，利润可以快速回吐。因此，memory 更接近**高壁垒的制造稀缺周期**，不是永久平台租金。

## 6. Hyperscaler：既拥有 distribution，也承担最大资产风险之一

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

## 7. Supply commitments 是 system platform 与 manufacturing 之间的资金桥

NVIDIA manufacturing, supply, and capacity commitments 从 2026-01-25 的 **US$95.2B** 上升到 2026-04-26 的 **US$119B**，再到 2026-07-26 的 **US$279B**。

FY27 Q2 10-Q 说明最新 commitments 主要关联 data-center infrastructure systems 所需的 memory 与 manufacturing facilities。它可以作为**未来资源锁定强度的财务 proxy**，但公开文件没有 supplier-level split，因此不能写成 TSMC、SK hynix、Micron 或任何单一供应商“已经收到多少”。

这也是 value capture 的重要动态：高 seller cash flow 可以更早变成下一代 wafer、memory、packaging 和 component commitments。

## 8. Power / Powered Land：价值来自时间稀缺，而不是单纯电价

当 rack power 进入约 **120 kW-class**，数据中心需要更强的 grid connection、substation、transformer、cooling 与 firm generation。拥有 powered land、existing interconnection 和可执行许可路径的资产会获得明显 **Time-to-Power** 价值。

这层资产的特点是：复制慢、地理固定、许可周期长、合同期限往往长于 compute generation。

因此 power 可以成为 scarce layer，但其经济性必须与 utilization 和合同久期一起分析。长期 PPA 在高需求情景中是 hedge / moat，在 S4 中也可能成为 long-duration obligation。

## 9. Model / Application：长期利润取决于 Workflow，而不是模型本身

模型公司与 AI software 拥有 model capability、API、user distribution 和 workflow 入口，但也面对 open-source competition、inference/retrieval/tool cost、cloud bargaining 与快速价格压缩。

传统 SaaS 的高毛利不能直接套到 AI application。正确单位是 **AI Software Unit Economics**：

> Revenue or productivity value − inference − retrieval/storage − tools/APIs − human review − AI-specific cloud cost

真正有防御力的 application layer 需要把模型能力转化成 proprietary workflow、data、distribution、retention 和 measurable business outcome。

## 10. Consumer Electronics：不是“输掉 AI”，而是承受 residual-capacity pressure

smartphone、PC、gaming 与 general server 仍然是大型市场。它们承受的主要不是“被 AI 淘汰”，而是 shared upstream resources 的再分配：advanced logic allocation、DRAM residual supply、consumer-GPU availability 与 component pricing。

所以这一层更准确的角色是 **residual-capacity pressure bearer**。当 AI/server demand 抢占高价值增量资源时，传统终端的升级节奏、配置和成本会发生变化。

## 11. Custom Silicon 会重画资金路径，但不一定减少上游需求

传统路径可以近似写成：

> cloud / model buyer → system platform → foundry / HBM / packaging → equipment/materials → power/data-center

当 hyperscaler 使用 custom silicon 时，部分资金可能绕开 NVIDIA：

> cloud → custom system → foundry / HBM / packaging

这会改变 platform profit 的归属，却未必降低 advanced logic、HBM、packaging 与 power 的总需求。

因此，system-stack substitution 既是利润分配变量，也是上游资源竞争变量。

## 12. 不使用固定“赢家排名”，而使用 Scenario Map

不同情景会改变 value capture：

- **S1 Competitive Expansion**：custom stack、open software 和 supply expansion 降低平台租金，价值更分散；
- **S2 Baseline Concentration**：system platform 与 scarce manufacturing 保持强 value capture，cloud 继续高投入；
- **S3 Resource Hegemony**：logic/HBM/packaging/power 进一步集中，scarce-layer owners 与 dominant system platform 获取更强议价；
- **S4 Capital Hard Landing**：buyer utilization 与 commitments 下滑，长期基础设施首先面临 duration/ROI 压力，上游利润随后传导回落。

这比给 system platform、HBM、foundry、cloud、application 排一个永久名次更可靠。

## 13. 当前判断

截至 2026 年 8 月，AI infrastructure 的高质量 value capture 主要出现在两类位置：

1. **能够组织多个稀缺层并制造 switching cost 的 system platform；**
2. **短期供给弹性低、进入壁垒高的 HBM / leading-edge manufacturing / advanced packaging / powered infrastructure。**

而最大资产风险则更多留在需要提前建设大规模 infrastructure 的 buyer 端。应用层是否形成长期利润池，取决于 workflow economics 和 distribution。

因此，真正应该问的不是“AI 一共花了多少钱”，而是：

> **同一笔资本在每一层留下多少可重复现金流、形成多少不可替代性，又把多少长期风险留在资产负债表上。**

## 关键公开来源

- NVIDIA FY27 Q2 official results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- NVIDIA FY27 Q2 10-Q — US$279B manufacturing, supply, and capacity commitments: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
- TSMC 2025 Annual Report: https://investor.tsmc.com/static/annualReports/2025/english/index.html
- TSMC 4Q25 Transcript — 2025 advanced packaging slightly over 10%, company-corrected: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
- TSMC 2Q26 Earnings Conference Transcript — packaging tightness limits customer growth: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
- SK hynix FY25 official results: https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
- Micron FY24 Q2 Prepared Remarks — HBM3E ≈3× DDR5 wafer supply: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- NVIDIA DGX GB200 hardware guide — ~120 kW/rack: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html