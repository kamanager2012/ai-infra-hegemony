# Part I · 第9章：Semiconductor Supply-Chain Resilience——Equipment、Materials 与 Geographic Redundancy


## 1. Resilience 本质上是 System-Continuity Problem

Frontier AI 的 supply security 不能从一张 fab 地图或相关企业的国籍直接推断。真正需要测试的是：**整个工业链在关键 disruption 下，能否继续生产、qualification、service、repair 与跨代扩张。**

一套 frontier AI system 的 physical supply chain 至少涉及：

- lithography / deposition / etch / metrology equipment；
- silicon wafers 与高纯材料；
- leading-edge foundry；
- HBM；
- advanced packaging / substrates；
- testing；
- data-center power / cooling。

因此，accelerator designer 的 supply security 不是由 chip design 单独决定，而取决于多层工业能力是否同时可用。

## 2. Equipment 本身就是 System-Level Capability

ASML 2025 Annual Report 披露全年销售 **48 台 EUV lithography systems**；截至 2025 年末，High-NA TWINSCAN EXE 仍主要处在客户 qualification 与 production-readiness 推进阶段。[^1]

但状态已经在 2026 年进一步前移。2026-07-15，ASML 与 Intel Foundry 官方确认：Intel 已在 **Intel 18A 的特定 layers** 上 dual-qualify High-NA EUV，并使用 High-NA 生产部分 Panther Lake / Intel Core Ultra Series 3 产品；这些产品已经进入 high-volume manufacturing，并以与 NXE platform 匹配的 yield 出货。[^8]

这条证据支持的是：

> **High-NA EUV 已经进入真实 high-volume logic production environment。**

它不能推出所有 Intel 18A layers 都依赖 High-NA，也不能推出 TSMC N2 已经采用 High-NA。

这说明先进光刻的战略约束不是一个“单台机器报价”就能描述。真正重要的是：

- system availability；
- throughput；
- imaging / overlay performance；
- customer qualification；
- field service；
- optics / source / stage / metrology 的长期协同。

所以 High-NA 的关键意义是下一代 process roadmap 与工业化成熟度，而不是媒体上的单机价格。

## 3. Fab 不能脱离 Supplier Ecosystem 独立存在

leading-edge manufacturing 依赖设备安装、备件、软件、process recipe、materials、metrology 与长期 field service。

即使两个地区都拥有厂房，如果供应商网络、工程人才、qualification cycle、tool service 与材料稳定性不同，effective capacity 也不会完全等价。

因此，本报告把 supply-chain independence 定义为 **system-level continuity**，而不是“地图上有一个 fab”。

### 3.1 Upstream Continuity 由多个独立约束组成

“国内有 fab”也不能自动推出“扩产不再受外部供给影响”。

ASML 的公开出口管制说明给出了一个可审计边界：[^2][^3]

- EUV systems 对中国的销售已受限制；
- 最先进 immersion DUV systems 需要荷兰政府 export license；
- 2024 更新后的美国规则进一步扩大到部分 advanced semiconductor manufacturing equipment、metrology 与 software。

这支持的不是“所有中国晶圆厂都会因断供停摆”——ASML 自己也明确指出，限制针对 advanced technologies / specific fabs，其他系统并非全部受同一规则控制。

真正应该监测的是：

> **critical equipment availability + software/license + spare parts/field service + materials qualification**

这些上游变量决定新增产能能否按计划 ramp、既有产线能否长期维持 yield，以及下一代工艺能否持续迭代。

所以“存储产能扩张”与“存储供应链完全自主”也是两个不同命题。

### 3.2 Process Control 是独立设备层，不是 Lithography 的脚注

Lithography 只是 manufacturing-control stack 的一部分。KLA FY2026 Form 10-K 把 inspection、metrology、data analytics、reticle / mask control、chemistry / materials quality control 与 advanced-packaging process control 明确放在从 R&D 到 volume production 的生产链中；同时指出 2 nm 等 leading-edge transition 会提高 process-control intensity。[^10]

### Table 9.1 — 影响 Production Continuity 的 Manufacturing-Control Layers

| Layer | Production role | 为什么会形成 continuity constraint |
|---|---|---|
| Lithography | patterning / critical-dimension formation | tool availability、imaging、overlay、service、qualification |
| Inspection / metrology | defect detection、dimensional control、yield learning | 决定 process 能否 ramp 并维持 target yield |
| Reticle / mask control | pattern-source quality assurance | 缺陷可能跨大量 wafer 放大 |
| Deposition / etch | film formation 与 material removal | recipe stability 与 tool availability 是制程代际输入 |
| Chemical / materials quality control | contamination / composition / incoming-material control | qualified materials 必须在长周期量产中保持稳定 |
| Advanced-packaging process control | substrate / package inspection 与 yield management | packaging complexity 可以形成独立 HVM constraint |

**Source:** ASML 与 KLA first-party disclosures.[^1][^10]  
**Note:** 该表识别的是生产所需的 manufacturing-control functions，不代表某一家 vendor 垄断全部类别，也不把 vendor revenue share 转换成 physical capacity share。

这会改变 resilience 的判断方式：一个地区即使获得 leading-edge lithography，也仍可能因为 inspection、metrology、reticle control、materials quality、etch/deposition、packaging control 或 field service 无法在规模化生产中闭合，而存在 production-continuity risk。

## 4. Material Qualification 是 Hidden Time Cost

advanced node 对 contamination、particle、uniformity、defect density 与 long-term stability 极为敏感。

材料供应商替换不是普通采购切换。即便化学成分类似，也可能要求重新 qualification，并在 yield、tool recipe 与 reliability 上重新建立生产经验。

所以材料层的风险不需要一个夸张的市场份额数字才能成立。真正的约束是：

> **qualified alternative supplier 是否存在，以及切换需要多长时间。**

## 5. Geographic Redundancy 正在发生，但 Cluster Replication 很慢

TSMC 2025 Annual Report 与 2026 年 Arizona 官方更新显示：[^4][^9]

- Arizona 第一座 fab 已在 **4Q24** 进入 N4 high-volume production；
- 第二座 fab 的 fab structure 已完成，目标在 **2027H2** 进入 N3 volume production；
- 第三座 fab 已于 2025 开工，规划 N2 / A16，目标在本十年末进入 volume production；
- 第四座 fab 与首座 advanced-packaging facility 已在 2026 年进入前期建设；
- 当前 Arizona 规划已扩展到 **six logic fabs + two advanced-packaging facilities + R&D center**；
- Japan Kumamoto 第一座 fab 在 2024 年末进入量产，第二座 fab 规划包含 3 nm；
- Germany Dresden 项目面向 automotive / industrial specialty technologies；
- Taiwan 仍持续建设 2 nm 及更先进节点，并扩张 advanced packaging。

这说明 geographic diversification 是真实趋势，而且正在从单一 logic fab 扩展到 packaging 与 R&D。

但它仍不是“Taiwan cluster 一夜复制到海外”。

不同地区承担的 node、product mix、packaging、workforce、supplier density 与 power/water 条件仍不同。

## 5A. Geographic、Supplier 与 Technology Redundancy 必须分开

“美国有 TSMC fab”主要提高的是 **geographic redundancy**。

它并不自动等于：

- foundry supplier redundancy；
- EDA / equipment redundancy；
- HBM supplier redundancy；
- packaging supplier redundancy；
- design portability。

因此至少要区分三类 resilience：

### Geographic Redundancy

同一技术/供应商在多个地区拥有制造能力。

它降低单一区域中断风险，但仍可能依赖同一公司、同一 process ecosystem 或同一关键设备体系。

### Supplier Redundancy

同一 workload / design 可以在两个或更多 qualified suppliers 之间切换。

这要求：

- process portability；
- design requalification；
- packaging compatibility；
- yield / reliability validation；
- software / firmware adaptation。

它比“同一供应商跨地区扩产”更难。

### Technology Redundancy

即使某一种设备、process 或 architecture 受限，仍存在另一条可达到可接受 performance / cost 的技术路径。

因此：

> **geographic diversification ≠ true second source ≠ technology independence**

对 frontier AI supply security，真正高价值的是三种冗余能够同时提高，而不是只看 fab 地图是否变得更分散。

## 6. Subsidy 降低 Redundancy Cost，但不会创造即时独立

美国 Department of Commerce 对 TSMC Arizona 的 CHIPS final award 包括 up to **US$6.6B direct funding**，支持三座 leading-edge fabs；对 advanced packaging 的 NAPMP final awards 合计 **US$1.4B**，另对 Amkor Arizona advanced-packaging/test facility 提供 up to **US$407M** direct funding。[^5][^6][^7]

这些项目直接证明：

> **战略冗余需要额外公共资本来补偿 geographic duplication、cluster formation 与早期利用率风险。**

但补贴无法立即复制 decades of yield learning、supplier qualification 与 engineering density。subsidy 可以加快 capacity formation，却不是 instant supply-chain independence。

## 7. Redundancy 天然带来 Efficiency Cost

更高 resilience 往往要求：

- duplicated fabs / packaging lines；
- duplicated inventories；
- spare / reserve capacity；
- regional supplier qualification；
- lower initial utilization；
- government incentives；
- additional engineering / compliance overhead。

因此，供应链可能从：

> **lowest-cost global optimization**

逐步转向：

> **higher-cost strategic redundancy**

这不只是 efficiency loss，而是在不同 security objective 下运行的另一套 cost function。

## 8. AI demand 会加速这种地理重构

AI 对 leading-edge logic、HBM、packaging 与 power 的需求使先进制造从商业周期资产进一步变成战略基础设施。

TSMC 2025 年报明确把 Arizona expansion 与 strong multi-year AI-related demand 联系起来；美国 CHIPS awards 也把 AI/HPC 作为 leading-edge 与 advanced-packaging investment 的重要应用背景。[^4][^5][^6]

因此，AI infrastructure cycle 与 industrial-policy cycle 已经发生明显叠加。

## 9. Geographic Redundancy 不等于 Full Localization

一套区域 supply stack 需要分别验证：

- equipment / service；
- materials；
- foundry；
- HBM；
- packaging / substrate；
- testing；
- power / water；
- workforce；
- customer qualification。

某一层完成本地化，只能降低该层 dependency，不能自动关闭其他层风险。

这也是为什么 China、US、EU、Japan 的“本地化率”不能用一个总百分比描述 frontier system resilience。

## 10. China localization 与 Western reshoring 本质上面对相同系统问题

中国推动 equipment、materials、foundry、memory、packaging localization，美国/欧洲/日本推动 reshoring / friend-shoring，目标方向不同，但都面对同一工程现实：

> **performance + yield + scale + qualification + cost 必须同时成立。**

单点产品存在不是 system closure；真实替代需要在生产规模、稳定性与长期 service 上达到可持续水平。

## 11. Fragmentation 可以提高总投资，同时降低单一体系效率

如果全球形成两套或多套相对独立的 semiconductor / AI system ecosystems，可能出现：

- repeated fab investment；
- repeated packaging investment；
- duplicated software/runtime；
- higher strategic inventory；
- lower cross-region fungibility；
- more policy-driven capacity。

因此，地缘 fragmentation 不一定意味着全球 semiconductor CapEx 下降，反而可能意味着**更多重复建设、较低单一体系利用效率与更高 resilience**。

## 12. Supply-Chain Resilience 的 Evidence Standard

本报告不把“完全自主”设为唯一目标。更现实的指标是：

1. single-point failure 是否减少；
2. critical layer 是否存在 qualified second source；
3. disruption 后 system-level recovery 需要多久；
4. regional capacity 是否有足够 power / workforce / supplier support；
5. redundancy cost 是否仍能被最终 workload economics 覆盖。

真正的竞争不是哪个国家在所有环节完全自产，而是：

> **关键中断发生时，谁能以可接受成本维持最高的 system-level continuity。**

## 13. Current Read

截至 2026 年，公开事实支持一个相对清晰的方向：

- core leading-edge technologies 仍高度集中；
- High-NA EUV 已从 qualification 推进到真实 HVM logic production；
- geographic redundancy 正在加速，并开始覆盖 logic + packaging + R&D；
- supplier redundancy 的提升速度明显慢于 geographic redundancy；
- government participation 明显提高；
- advanced packaging 已被单独列为政策与投资对象；
- 冗余提高 resilience，同时提高资本与运营成本；
- 海外 fab expansion 仍需要时间复制 supplier / workforce / packaging / infrastructure ecosystem。

因此，未来十年的半导体供应链更可能是**高集中核心技术 + 更多区域冗余 + 更高战略库存与公共资本参与**，而不是快速回到完全分散、完全可替代的全球市场。

## References

[^1]: ASML, 2025 Annual Report and Strategy & Stories, EUV / High-NA roadmap and system shipments, https://www.asml.com/en/investors/annual-report/2025
[^2]: ASML, 2023 statement on Dutch export-control regulations, EUV and advanced immersion DUV licensing, https://www.asml.com/en/news/press-releases/2023/statement-regarding-export-control-regulations-dutch-government
[^3]: ASML, 2024 statement on updated export restrictions covering additional advanced manufacturing technologies, metrology and software, https://www.asml.com/en/news/press-releases/2024/asml-expects-impact-of-updated-export-restrictions-to-fall-within-outlook-for-2025
[^4]: TSMC, 2025 Annual Report, Arizona/Japan/Germany/Taiwan manufacturing footprint and AI-related demand context, https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^5]: U.S. Department of Commerce, TSMC Arizona CHIPS final award, 2024-11, https://www.commerce.gov/news/press-releases/2024/11/biden-harris-administration-announces-chips-incentives-award-tsmc
[^6]: U.S. Department of Commerce, US$1.4B NAPMP advanced-packaging final awards, 2025-01, https://www.commerce.gov/news/press-releases/2025/01/us-department-commerce-announces-14-billion-final-awards-support-next
[^7]: U.S. Department of Commerce, Amkor Arizona advanced-packaging and test award, 2024-12, https://www.commerce.gov/news/press-releases/2024/12/biden-harris-administration-announces-chips-incentives-award-amkor
[^8]: ASML, “High NA EUV reaches new readiness milestone with first high-volume Logic product,” 2026-07-15, Intel 18A select layers / Panther Lake HVM, https://www.asml.com/en/news/press-releases/2026/high-na-euv-reaches-new-readiness-milestone
[^9]: TSMC Arizona, current project milestones and planned manufacturing footprint, 2026, https://www.tsmc.com/static/abouttsmcaz/index.htm ; TSMC 2026 AGM minutes, second-fab HVM timing and Arizona expansion context, https://investor.tsmc.com/sites/ir/shareholders-meeting/2026-06-04/2026AGM_Minutes_wmn.pdf

[^10]: KLA Corporation, FY2026 Form 10-K, semiconductor process control, inspection, metrology, reticle/mask, chemistry/materials quality control, advanced packaging, and 2 nm process-control intensity, https://ir.kla.com/sec-filings/all-sec-filings/content/0000319201-26-000027/klac-20260630.htm
