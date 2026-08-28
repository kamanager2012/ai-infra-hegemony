# Part I · 第9章：全球半导体供应链与制造冗余

> **出版层章节。** 以 [vol-34](../vol-34.md) 为主源，并用 ASML、TSMC 与 CHIPS for America 的公开材料限定事实边界。本章不使用未经核验的设备单价或材料份额表，重点解释：为什么“再建一座 fab”不等于复制完整 leading-edge supply chain，以及战略冗余为什么同时提高 resilience 与成本。

## 1. Frontier AI 背后是一条跨企业、跨国家的工业链

一套 frontier AI system 的 physical supply chain 至少涉及：

- lithography / deposition / etch / metrology equipment；
- silicon wafers 与高纯材料；
- leading-edge foundry；
- HBM；
- advanced packaging / substrates；
- testing；
- data-center power / cooling。

因此，accelerator designer 的 supply security 不是由 chip design 单独决定，而取决于多层工业能力是否同时可用。

## 2. ASML 说明设备本身也是 system-level capability

ASML 2025 Annual Report 披露全年销售 **48 台 EUV lithography systems**；其 High-NA TWINSCAN EXE 平台仍在进入高量产前的客户验证阶段。ASML 表示，到 2025 年末客户已在 High-NA systems 上运行超过 400,000 wafers，并继续推进系统向 high-volume manufacturing qualification。

这说明先进光刻的战略约束不是一个“单台机器报价”就能描述。真正重要的是：

- system availability；
- throughput；
- imaging / overlay performance；
- customer qualification；
- field service；
- optics / source / stage / metrology 的长期协同。

所以 High-NA 的关键意义是下一代 process roadmap 与工业化成熟度，而不是媒体上的单机价格。

## 3. 一座 fab 不能脱离 supplier ecosystem 独立存在

leading-edge manufacturing 依赖设备安装、备件、软件、process recipe、materials、metrology 与长期 field service。

即使两个地区都拥有厂房，如果供应商网络、工程人才、qualification cycle、tool service 与材料稳定性不同，effective capacity 也不会完全等价。

因此，本书把 supply-chain independence 定义为 **system-level continuity**，而不是“地图上有一个 fab”。

## 4. Material Qualification 是经常被低估的时间成本

advanced node 对 contamination、particle、uniformity、defect density 与 long-term stability 极为敏感。

材料供应商替换不是普通采购切换。即便化学成分类似，也可能要求重新 qualification，并在 yield、tool recipe 与 reliability 上重新建立生产经验。

所以材料层的风险不需要一个夸张的市场份额数字才能成立。真正的约束是：

> **qualified alternative supplier 是否存在，以及切换需要多长时间。**

## 5. TSMC 的地理扩张证明“冗余正在发生”，也证明核心集群不会瞬间复制

TSMC 2025 Annual Report 显示：

- Arizona 第一座 fab 已在 **4Q24** 进入 4 nm volume production；
- 第二座 Arizona fab 计划生产 3 nm 及更先进技术；
- 2025 年第三座 Arizona fab 已开始建设，并宣布后续更多 fabs、advanced-packaging facilities 与 R&D expansion；
- 日本 Kumamoto 第一座 fab 在 2024 年末进入量产，第二座 fab 规划包含 3 nm；
- Germany Dresden 项目面向 automotive / industrial specialty technologies；
- Taiwan 仍持续建设 Hsinchu / Kaohsiung 2 nm，并继续投入 leading-edge 与 advanced-packaging facilities。

这说明 geographic diversification 是真实趋势，但不是“Taiwan cluster 一夜复制到海外”。

不同地区承担的 node、product mix、packaging、workforce、supplier density 与 power/water 条件仍不同。

## 6. 政府补贴的作用是降低冗余建设成本，而不是创造即时独立

美国 Department of Commerce 对 TSMC Arizona 的 CHIPS final award 包括 up to **US$6.6B direct funding**，支持三座 leading-edge fabs；对 advanced packaging 的 NAPMP final awards 合计 **US$1.4B**，另对 Amkor Arizona advanced-packaging/test facility 提供 up to **US$407M** direct funding。

这些项目直接证明：

> **战略冗余需要额外公共资本来补偿 geographic duplication、cluster formation 与早期利用率风险。**

但补贴无法立即复制 decades of yield learning、supplier qualification 与 engineering density。subsidy 可以加快 capacity formation，却不是 instant supply-chain independence。

## 7. 冗余为什么天然提高成本

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

这不是效率失败，而是安全目标改变后的成本函数变化。

## 8. AI demand 会加速这种地理重构

AI 对 leading-edge logic、HBM、packaging 与 power 的需求使先进制造从商业周期资产进一步变成战略基础设施。

TSMC 2025 年报明确把 Arizona expansion 与 strong multi-year AI-related demand 联系起来；美国 CHIPS awards 也把 AI/HPC 作为 leading-edge 与 advanced-packaging investment 的重要应用背景。

因此，AI infrastructure cycle 与 industrial-policy cycle 已经发生明显叠加。

## 9. Geographic Redundancy 不等于所有层都本地化

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

## 11. 地缘分化可能让全球总投资上升而单一体系效率下降

如果全球形成两套或多套相对独立的 semiconductor / AI system ecosystems，可能出现：

- repeated fab investment；
- repeated packaging investment；
- duplicated software/runtime；
- higher strategic inventory；
- lower cross-region fungibility；
- more policy-driven capacity。

因此，地缘 fragmentation 不一定意味着全球 semiconductor CapEx 下降，反而可能意味着**更多重复建设、较低单一体系利用效率与更高 resilience**。

## 12. 什么才叫真正的 Supply-Chain Resilience

本书不把“完全自主”设为唯一目标。更现实的指标是：

1. single-point failure 是否减少；
2. critical layer 是否存在 qualified second source；
3. disruption 后 system-level recovery 需要多久；
4. regional capacity 是否有足够 power / workforce / supplier support；
5. redundancy cost 是否仍能被最终 workload economics 覆盖。

真正的竞争不是哪个国家在所有环节完全自产，而是：

> **关键中断发生时，谁能以可接受成本维持最高的 system-level continuity。**

## 13. 当前判断

截至 2026 年，公开事实支持一个相对清晰的方向：

- core leading-edge technologies 仍高度集中；
- geographic redundancy 正在加速；
- government participation 明显提高；
- advanced packaging 已被单独列为政策与投资对象；
- 冗余提高 resilience，同时提高资本与运营成本；
- 海外 fab expansion 仍需要时间复制 supplier / workforce / packaging / infrastructure ecosystem。

因此，未来十年的半导体供应链更可能是**高集中核心技术 + 更多区域冗余 + 更高战略库存与公共资本参与**，而不是快速回到完全分散、完全可替代的全球市场。

## 关键公开来源

- ASML 2025 Annual Report: https://www.asml.com/en/investors/annual-report/2025
- ASML 2025 Strategy & Stories — EUV / High-NA roadmap: https://www.asml.com/en/investors/annual-report/2025/strategy-and-stories
- TSMC 2025 Annual Report — Arizona/Japan/Germany/Taiwan footprint: https://investor.tsmc.com/static/annualReports/2025/english/index.html
- U.S. Department of Commerce — TSMC Arizona CHIPS final award: https://www.commerce.gov/news/press-releases/2024/11/biden-harris-administration-announces-chips-incentives-award-tsmc
- U.S. Department of Commerce — US$1.4B NAPMP advanced-packaging awards: https://www.commerce.gov/news/press-releases/2025/01/us-department-commerce-announces-14-billion-final-awards-support-next
- U.S. Department of Commerce — Amkor Arizona advanced-packaging award: https://www.commerce.gov/news/press-releases/2024/12/biden-harris-administration-announces-chips-incentives-award-amkor