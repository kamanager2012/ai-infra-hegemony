# Part III · 第21章：AI 如何重定价消费电子与其他终端系统

## 1. 核心问题是 Transmission，不是 Displacement

AI 不需要和 smartphone、router、game console、汽车或工业控制器采购完全相同的芯片，也可以改变这些终端的经济条件。

真正需要判断的是：**两类 demand 在哪些 physical pool 直接重叠，又在哪些层通过资本、设备、工程能力、qualification 与 supplier economics 间接耦合。**

直接重叠更常见于 advanced logic、DRAM / LPDDR、selected packaging、consumer/workstation GPU resources、storage 与部分 power-management components。对于 long-life、trusted、RF/power、rad-hard 或 special-process systems，真正重要的往往不是“直接抢同一颗 accelerator”，而是供应连续性与小批量 economics。

因此，本章使用的传导链是：

> **AI/server product mix 上升 → shared / adjacent resource pool 的 allocation priority 改变 → Non-AI Residual Capacity 与 Quantity Assurance 改变 → BOM、configuration、promotion、volume 或 replacement-cycle economics 调整**

本章研究的是 **transmission + attribution**。它既不假设所有价格上涨都由 AI 导致，也不要求存在 literal one-for-one component competition 才承认产业传导。

---

## 2. Memory 是当前最清晰的 Transmission Layer

Micron 一手披露，在 same node / same bits 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。[^1]

TrendForce 预计 2026 年 HBM + RDIMM 合计约占 DRAM bit supply **51%**。[^2]

这两条证据说明，consumer DRAM 的压力不能只用 bit share 判断。如果高价值 AI/server memory 同时具有更高 manufacturing input intensity，那么传统 DRAM 所面对的 residual pressure 可能高于表面 bit share 所显示的程度。

但必须保留边界：

- 3× 是 same node / same bits 的 wafer-supply trade ratio；
- 51% 是 2026E institutional forecast；
- 两者都不能直接改写成“H​​BM 占全球 DRAM wafer 的某个固定百分比”。

---

## 2A. Attribution Test：单独 Price 上涨不足以归因

即使 AI/server demand 正在改变 memory 与 advanced-node resource allocation，也不能把 smartphone / PC component price 的全部变化都归因于 AI。

终端价格同时受到：

- supplier inventory policy；
- conventional demand recovery / weakness；
- wafer starts 与 capacity discipline；
- product-transition timing；
- FX；
- channel inventory；
- geopolitics / trade policy；
- supplier-specific yield 与 product mix；

等因素影响。

因此，本报告对“AI 传导”的证据要求是：

> **必须看到 shared physical resource、supplier product-mix reallocation、allocation / quantity-assurance 变化或公司/机构明确把 AI/server demand 与传统市场供给压力联系起来。**

单独出现“memory price 上涨”只能证明价格周期，不足以证明全部涨幅由 AI 导致。

同样，3Q26 mobile DRAM 涨幅预期已经显著低于 2Q26，说明 inventory、终端承受能力与供给调整能够部分抵消 AI Resource Gravity。

所以第21章讨论的是**边际传导机制**，不是一个“AI 解释所有消费电子通胀”的单因果模型。

## 3. Smartphone：最先调整的是 BOM 与 Configuration

TrendForce 2026-02-11 给出的 1Q26 例子显示，主流 **8GB + 256GB** smartphone memory estimated contract prices 同比接近 **+200%**。[^3]

到 2Q26，TrendForce 估计：

- LPDDR4X solution ASP 环比 **+70–75%**；
- LPDDR5X solution ASP 环比 **+78–83%**。[^4]

但到 2026-08-03，TrendForce 的 **3Q26 forecast** 已把 mobile DRAM 涨幅预期明显下调至约 **+8–13% QoQ**。[^5]

这说明价格压力不是永远单边加速。更准确的判断是：

> **结构性 residual pressure 仍在，但 marginal price pressure 会随着库存、终端需求、supplier allocation 与扩产变化而波动。**

与此同时，TSMC 2025 smartphone platform 仍占全年 net revenue **29%**，platform revenue 同比 **+11%**。[^6]

因此，AI/HPC growth 不等于 smartphone demand 消失。

---

## 4. Smartphone 正在 Segmentation，而不是消失

Counterpoint 2026H1 的数据提供了更直接的终端证据：[^7]

- global smartphone SoC shipments 同比 **-15%**；
- MediaTek 与 Qualcomm shipments 均同比下降 **>25%**；
- 2Q26 smartphone memory prices 同比上涨 **>300%**；
- GenAI smartphone SoC shipments 同比 **+24%**；
- UNISOC 在低成本 segment 继续扩大份额。

这意味着同一轮上游压力会产生不同结果：

### Entry / Mid-range

对 memory/BOM inflation 更敏感，品牌更可能通过：

- 降低配置升级速度；
- 延长成熟节点使用；
- 调整产品组合；
- 延长换机周期；
- 转向更低成本 SoC / component combination。

### Premium / GenAI segment

更高 ASP 与更强产品差异化可以吸收部分 BOM pressure，因此对资源涨价的耐受度更高。

所以 AI 对 smartphone 的更准确影响不是“把手机行业挤掉”，而是：

> **提高高端资源的机会成本，并加剧不同价格带之间的配置分化。**

---

## 4A. Routers / Broadband：Buyer Power 决定传导强度

Counterpoint Research 2026-02 报告称，consumer DRAM/NAND 一年内价格上涨超过 **600%**；router / gateway / set-top-box 等 broadband products 使用的 memory price 接近 **7×**，低中端 router 的 memory BOM 占比从约 **3%** 升至 **>20%**。[^16]

这组数据的重要意义不在于“所有终端都涨七倍”，而在于它揭示一个产业机制：

> **Resource crowding-out 的损伤强度，与终端厂商的议价权、库存能力和 supply assurance 高度相关。**

大型客户可以通过 LTA、规模采购与更强资产负债表缓冲冲击；低议价 OEM 更容易同时承受 higher price + lower allocation。


---

## 5. Cross-Market Reordering：Allocation Logic 正在改变

TrendForce 2026-04 指出，AI demand 已造成 **3 nm–2 nm wafers 与 2.5D/3D advanced packaging** bottleneck，并称 NVIDIA 较早预先锁定大量 **4/3 nm wafer capacity、CoWoS、HBM、T-glass、substrates、PCB 与 SSD** 等资源。[^8]

2026-06 的 foundry research 又指出 TSMC **3 nm capacity remains severely constrained**；[^9] 同月 TrendForce 进一步指出，foundries 正把更多 wafer capacity 转向 AI-related products。[^10]

本报告把这一变化定义为：

> **Cross-Market Resource Reordering：当 AI/server workload 提供更高预期回报、更强订单确定性和更长期资源承诺时，多个原本服务不同终端市场的增量资源会被重新排序。**

这不是“过去各类客户平均分配产能、现在某一客户获得全部产能”。

它支持的结论是：

- advanced-node / packaging / memory 的 product mix 正在变化；
- allocation assurance 的重要性上升；
- low-margin / low-bargaining-power customer 更容易承受 price + quantity 双重压力；
- 传统终端的关键变量从 gross supply 变成 Non-AI Residual Capacity。

它**不能**直接推出 Apple、Qualcomm、AMD、Intel 各自少拿了多少 wafer，更不能把机构估计写成单一客户的确定 allocation。

---

## 6. PC：Memory 与 System Pricing 可以相互强化

NVIDIA FY26 10-K 表示 FY26 Gaming revenue 同比 **+41%**，同时预计 supply constraints 会成为 FY27 Q1 及之后 Gaming 的 headwind。[^11]

到 FY27 Q1，公司新的 Edge Computing 口径又指出，consumer PC demand 较慢，部分原因是 **elevated memory and systems prices**。[^12]

因此 PC 面对至少两条独立但可以叠加的压力：

1. **consumer GPU / system availability**；
2. **DDR / LPDDR / system memory cost**。

这类压力往往先影响：

- memory configuration；
- GPU tier；
- system ASP；
- replacement cycle；

而不是直接导致市场停产。

本报告把这种影响称为**升级税**：

> **消费者可能以相同价格获得更慢的规格升级，或者为相同规格支付更高价格。**

---

## 6A. Game Console：长世代使 Residual Pressure 更持久

游戏主机是一个很适合检验 Non-AI Residual Capacity 的整机行业。它与 AI server 并不直接争夺同一颗 accelerator，却真实暴露于 **memory、storage、custom SoC/APU 与部分制造/封测资源**。

当前主机规格能够说明这种物理暴露的边界：

- PlayStation 5 使用 custom AMD Zen 2 / RDNA-based processor、**16 GB GDDR6** 与 custom SSD；[^24]
- Xbox Series X 使用 custom Zen 2 / RDNA 2 processor、**16 GB GDDR6** 与 **1–2 TB custom NVMe SSD**；[^25]
- Nintendo Switch 2 使用 **custom NVIDIA processor** 与 **256 GB UFS storage**。[^26]

这些规格**不能**推出“游戏主机直接与 HBM 抢同一物理池”。

更准确的关系是：

> **console memory / storage / SoC 与 AI/server demand 位于同一个更大的 semiconductor / memory capital system 中，但具体产品池、封装形式与 qualification path 并不相同。**

### 6A.1 Hardware-Economics Pressure 已可直接观察

Sony 在 FY2025 Q4 / FY2026 outlook 中明确表示：

- 截至 2026 年 3 月，PS5 cumulative unit sales 已超过 **93 million**；
- FY26 PS5 hardware sales 将以公司能够按**合理价格采购到的 memory volume**为基础；
- 如果条件变化，公司将通过调整 **unit sales 与 promotional plans** 管理 hardware profitability。[^27]

这是一条强一手传导证据，因为它把：

> **memory procurement → hardware volume / promotion → hardware profitability**

直接连在一起。

Sony 2026 年 20-F 还把自 2025H2 以来的全球 memory semiconductor 涨价与 supply shortage 列为 G&NS 等业务风险，并明确提到 custom parts、limited production capacity 等条件可能导致生产下降或中断。[^29]

TrendForce 对 2026 游戏主机市场的机构预测进一步估计：

- 2026 global game-console shipment forecast 从原先 **-3.5% YoY** 下修到 **-4.4% YoY**；
- 主要主机的 memory cost 占 BOM 比例，从过去约 **15%** 上升到大约 **23%–42%**；
- hardware gross margin 与传统促销空间因此承压。[^28]

这属于 **B 级 institutional estimate**，不能升级成 Sony / Microsoft / Nintendo 已审计的实际 BOM。

但与 Sony 一手采购口径结合后，可以支持一个更窄、更硬的结论：

> **游戏主机已经成为 memory residual pressure 可以直接影响出货节奏、促销能力与 hardware margin 的整机案例。**

### 6A.2 为什么一次 Cost Shock 可以影响整个 Console Generation

游戏主机通常具有：

- 长 hardware generation；
- 相对刚性的 retail price band；
- 高度定制的 SoC/APU；
- 固定 memory / storage architecture；
- 依赖 installed base 扩大后由 software / network / content monetization 回收平台价值。

因此，风险不只是一季 memory price 上升。

如果一个新世代在 architecture freeze / BOM freeze 时遇到更高的 memory、storage 或 advanced-logic opportunity cost，影响可能通过：

- launch configuration；
- SKU segmentation；
- promotion cadence；
- multi-year cost-down curve；

持续更久。

这就是游戏主机版本的 **upgrade tax**：

> **同一价格带下，硬件规格提升变慢；或同一目标规格需要更高 BOM / 更弱促销补贴。**

### 6A.3 Attribution Boundary

本报告不从上述证据推出：

- PlayStation / Xbox / Nintendo 会被 AI 淘汰；
- 游戏主机“缺的是 HBM”；
- NVIDIA / AI server 抢走了某家主机厂确定数量的 wafer；
- 2026 游戏主机出货下滑全部由 AI 导致；
- 下一代主机一定涨价或延期。

主机市场还同时受 generation cycle、content pipeline、installed-base saturation、retail pricing、FX、consumer demand 与 product strategy 影响。

因此，更准确的产业判断是：

> **游戏主机不是 AI 时代的边缘行业，而是一个长世代、hardware-margin 敏感、memory/storage 暴露较高的整机平台；AI/server memory demand 越强，它越需要在 quantity assurance、BOM、promotion 与 hardware cadence 之间做新的权衡。**

---

## 7. Quantity Assurance 与 Price 是两个独立变量

在 severe shortage 中，终端企业面对的不只是 ASP 上涨，还可能面对 allocation fulfillment 不足。

TrendForce 2026-03 指出，allocation 较低的 PC OEM / module maker 需要以更高价格从供应商或模组厂补货。[^13]

因此必须把：

> **Price Pressure**

与

> **Quantity Assurance**

分开分析。

愿意支付更高价格，不代表一定能获得计划数量。

决定终端企业抗冲击能力的变量包括：

- LTA；
- purchase scale；
- balance-sheet strength；
- inventory；
- multi-sourcing；
- supplier relationship；
- end-market pricing power。

这也是为什么同一个 memory shortage 对大型 premium brand 和中小 OEM 的损伤可以完全不同。

---

## 8. Automotive / Industrial：Qualification 会把价格压力放大成 Continuity Risk

汽车与工业设备具有更长 qualification cycle，但这并不意味着它们与 AI 资源重配无关。

TrendForce 2026-06 指出，主要 memory suppliers 继续把 capacity 向 HBM 与高层数 3D NAND 等高价值产品倾斜，挤压 NOR Flash 与 SLC NAND 等成熟存储供给；1H26 两类产品合约价累计涨幅均超过 **100%**。[^14]

到 2026-07，TrendForce 又把 2H26 SLC NAND 相对 1H26 的涨幅预期提高到 **120–170%**。[^15]

这里能够确认的是：

> **具体 mature-memory 品类正在受到 product-mix reallocation 与供需收紧影响。**

不能外推成：

- “所有车规存储涨 180%”；
- “单车成本增加 RMB7,000–10,000”；
- “全年供应满足率低于 50%”。

这些都需要独立的一手或高质量机构证据。

车规电子还多一层 **qualification / product-longevity rigidity**。NXP 对 S32G vehicle network processors 给出至少 **15 年** product support；STMicroelectronics 2025 年把部分 SPC58 automotive MCU 的 availability 从 15 年延长到 **20 年**，部分料号至少供应至 2038–2041。[^19][^20]

这类一手证据说明：

> **汽车电子的难点不仅是“今天贵不贵”，还包括一旦完成认证后，料号能否在整个平台生命周期内继续获得稳定供应。**

因此，MCU、analog、power semiconductor 与多数车规器件并不和 AI server 直接争夺同一物理池；但 supplier CapEx、packaging/test capacity、engineering priority 与 product-longevity economics 仍可能受到更高回报市场的间接影响。没有项目级证据时，本报告不把这种相邻资源压力写成“AI 已导致某车型缺芯”。

### 8.1 Production Line：Lead Time、Redesign 与 Downtime 才是相关传导

PLC、servo control、industrial PC、sensor、MCU、analog/power 与 industrial memory 的共同特点，是：

- qualification / validation 周期长；
- embedded software 与 hardware BOM 绑定；
- 替换器件需要重新测试；
- 很多设备要求多年维护与备件支持。

因此，对 production line / industrial automation 来说，上游压力更可能表现为：

> **lead time 延长 → redesign / requalification 成本上升 → spare-part / maintenance 风险增加**

而不是“工厂买不到训练 GPU”。

这一机制与本章第2A节的归因边界完全一致：**某一工业器件涨价或交期延长，不足以单独证明原因就是 AI。** 只有看到 shared-resource exposure、supplier product-mix shift、capacity/engineering reallocation 或供应商明确归因，才可升级为 AI-era transmission evidence。

### 8.2 Aerospace / Defense：核心暴露是 Low-Volume Continuity

这类系统与 smartphone / PC 的物理暴露不同。

U.S. GAO 对 trusted defense microelectronics 的公开研究指出，商业微电子市场主要面向高量、短生命周期需求，而国防需求往往低量、特殊，对商业市场的影响力较弱；DMEA Trusted Foundry / Trusted Supplier 体系本身就是为了给通常低量的政府需求保留可信 advanced microelectronics access。[^21][^22]

NASA/JPL 对 space electronics 的资料则强调，空间辐射环境会使部分 IC 需要特殊设计、制造、screening 与 radiation assurance。[^23]

因此，最严谨的 AI-era 判断只能写到：

> **当商业半导体资本、设备与工程能力进一步围绕高量高回报市场优化时，小批量、高可靠、长寿命、可信或特殊工艺需求的维持成本可能上升。**

目前公开证据**不足以**进一步写成：

- 航空或航天项目因为 HBM 被订光而延期；
- radar / naval systems 与 AI server 直接争夺同一 GPU pool；
- AI 已造成这类项目某个确定百分比的成本上涨或供应满足率下降。

这些都需要项目级、供应商级或政府采购级证据。

---

## 9. Local Substitution 可以缓冲压力，但不能外推 Frontier Closure

中国在 DDR、LPDDR、NAND、smartphone manufacturing 与终端 supply chain 的能力扩张，可以提高本地 consumer residual capacity。

这可能影响：

- local memory pricing；
- supply diversification；
- smartphone / PC BOM；
- inventory resilience。

但 consumer DRAM / NAND capability 不能自动外推成 HBM-class frontier memory supply。

因此：

> **本地 conventional memory substitution 可以缓冲消费端成本，却不会自动解除 frontier AI 对 HBM、advanced packaging 与 leading-edge logic 的约束。**

---

## 10. Storage：HDD 与 SSD 仍是 Workload-Specific 的替代与互补

AI data-center storage 正在形成分层竞争。

TrendForce 2025–2026 同时观察到 nearline HDD supply shortage 与高容量 QLC nearline SSD 的替代加速；[^17] Seagate FY26 又明确表示，AI 产生的数据增长正在强化 mass-capacity storage demand。[^18]

因此更准确的结构是：

- latency / inference-sensitive workload 提高 SSD / QLC nearline SSD 的吸引力；
- cold / mass-capacity storage 仍然支持 HDD demand；
- HDD supply / HAMR ramp 本身也可能形成新的 bottleneck。

所以不能写成“AI 数据中心正在让机械硬盘失去战略意义”。

---

## 11. 实体企业还面临 AI Adoption Cost

传统企业不仅承受上游硬件成本，还要为使用 AI 支付另一组成本：

- cloud inference；
- software integration；
- data pipeline；
- security / compliance；
- workflow redesign；
- human review；
- organizational change。

因此，AI 对实体企业的净价值不能只看模型调用价格。

> **Net Productivity Value = Productivity Gain − Upstream Input Pressure − Total AI Adoption Cost**

这解释了为什么“模型越来越便宜”并不自动等于“实体企业 ROI 越来越高”。

---

## 12. Current Read

截至 2026 年 8 月，证据支持：

> **AI infrastructure 已经通过 memory、shared leading-edge resources、allocation priority 与 system pricing，把部分成本压力传导到消费电子、汽车/工业以及其他传统整机；越远离共享 advanced layers，传导越需要通过供应连续性、product-mix 与 supplier economics 单独验证。**

但这种传导不是统一、永久、单方向的。

真正决定损伤强度的是：

- shared-resource exposure；
- supplier product mix；
- end-market pricing power；
- inventory；
- supply assurance；
- demand elasticity；
- local substitution；
- capacity expansion。

因此，更准确的长期结论不是“AI 淘汰消费电子”，而是：

> **AI 正在提高传统终端获得上游资源的机会成本，并迫使不同终端重新调整配置、价格、库存和产品周期。**

## References

[^1]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^2]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^3]: TrendForce, 2026-02-11, 1Q26 mainstream smartphone memory contract cost, https://www.trendforce.com/presscenter/news/20260211-12922.html
[^4]: TrendForce, 2026-05-14, 2Q26 LPDDR4X and LPDDR5X ASP changes, https://www.trendforce.com/presscenter/news/20260514-13044.html
[^5]: TrendForce, 2026-08-03, 3Q26 mobile DRAM price outlook, https://www.trendforce.com/research/download/RP260803NC
[^6]: TSMC, 4Q25 Presentation / 2025 full-year platform mix, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
[^7]: Counterpoint Research, 2026-07-28, H1 2026 smartphone SoC shipment and memory-price trends, https://counterpointresearch.com/en/insights/global-smartphone-soc-shipments-fall-15percent-yoy-in-h12026
[^8]: TrendForce, 2026-04-30, AI supply-chain arms race and advanced-node / packaging bottlenecks, https://www.trendforce.com/presscenter/news/20260430-13028.html
[^9]: TrendForce, 2026-06-08, TSMC 3 nm capacity remains severely constrained, https://www.trendforce.com/research/download/RP260608SX3
[^10]: TrendForce, 2026-06-30, foundry capacity reallocation toward AI-related products, https://www.trendforce.com/presscenter/news/20260630-13127.html
[^11]: NVIDIA Corporation, FY26 Form 10-K, Gaming revenue and supply-constraint disclosure, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
[^12]: NVIDIA, FY27 Q1 CFO commentary, consumer PC demand tempered by elevated memory and systems prices, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27cfocommentary.htm
[^13]: TrendForce, 2026-03-31, allocation fulfillment and higher-price procurement, https://www.trendforce.com/presscenter/news/20260331-12995.html
[^14]: TrendForce, 2026-06-16, NOR Flash / SLC NAND mature-capacity squeeze, https://www.trendforce.com/presscenter/news/20260616-13102.html
[^15]: TrendForce, 2026-07-13, SLC NAND 2H26 price forecast, https://www.trendforce.com/presscenter/news/20260713-13142.html
[^16]: Counterpoint Research, 2026-02-11, broadband memory-price surge and router BOM impact, https://counterpointresearch.com/en/insights/7times-memory-price-surge-threatens-telcos-broadband-router-set-topbox-supply
[^17]: TrendForce, 2025-09-15, nearline HDD shortage and QLC SSD substitution, https://www.trendforce.com/presscenter/news/20250915-12714.html
[^18]: Seagate Technology, FY26 results, AI/cloud data generation and mass-capacity storage demand, https://investors.seagate.com/news/news-details/2026/Seagate-Technology-Reports-Fiscal-Fourth-Quarter-and-Fiscal-Year-2026-Financial-Results/default.aspx


[^19]: NXP Semiconductors, S32G Vehicle Network Processors, minimum 15-year product support under the Product Longevity program, https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32g-vehicle-network-processors%3AS32G-PROCESSORS
[^20]: STMicroelectronics, 2025-09-08, selected SPC58 automotive MCUs extended to 20-year availability, https://newsroom.st.com/media-center/press-item.html/n4718.html
[^21]: U.S. GAO, 2015, Trusted Defense Microelectronics: Future Access and Capabilities Are Uncertain, https://www.gao.gov/products/gao-16-185t
[^22]: U.S. DMEA Trusted Access Program Office, Trusted Foundry / Trusted Supplier Program, https://www.acq.osd.mil/asds/dmea/tapo/trusted-supplier-programs.html
[^23]: NASA/JPL, Space Radiation Effects on Integrated Circuits, https://parts.jpl.nasa.gov/asic/Appendix.3.html


[^24]: PlayStation, PS5 official specifications, custom AMD Zen 2 / RDNA-based processor, 16 GB GDDR6 and custom SSD, https://www.playstation.com/content/dam/global_pdc/en-gb/corporate/support/manuals/ps5-docs/2100ab/CFI-21XX_PS5_Instruction_Manual_Web%24en-gb.pdf
[^25]: Xbox, Xbox Series X official technical specifications, custom Zen 2 / RDNA 2 processor, 16 GB GDDR6 and 1–2 TB custom NVMe SSD, https://www.xbox.com/en-US/consoles/xbox-series-x
[^26]: Nintendo, Nintendo Switch 2 official technical specifications, custom NVIDIA processor and 256 GB UFS storage, https://www.nintendo.com/us/gaming-systems/switch-2/tech-specs/
[^27]: Sony Group, FY2025 Q4 earnings speech / FY2026 outlook, PS5 cumulative sales above 93 million and FY26 hardware-sales / promotion management tied to memory procurement at reasonable prices, https://www.sony.com/en/SonyInfo/IR/library/presen/er/pdf/25q4_sonyspeech.pdf
[^28]: TrendForce, 2025-12-02, Memory Price Surge Squeezes Game Console Margins; 2026 Shipment Forecast Revised Downward, https://www.trendforce.com/presscenter/news/20251202-12811.html
[^29]: Sony Group, FY2025 Form 20-F, global memory-semiconductor price increases / shortages and component-capacity risk, https://www.sony.com/en/SonyInfo/IR/library/FY2025_20F_PDF.pdf
