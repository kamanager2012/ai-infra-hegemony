# Part II · 第13章：Anchor Compute Buyer Effect——模型公司如何重塑基础设施

> **出版层章节。** 以 [vol-26](../vol-26.md) 为主源，并更新到 2026 年 8 月公开状态。本章把 OpenAI / Anthropic 等模型公司从普通 cloud tenant 中单独抽出，分析长期 workload commitment 如何影响 data center、custom silicon、HBM、packaging 与 power。

## 1. 模型公司正在从“算力租户”升级为 Infrastructure Anchor Buyer

传统关系是：

> model company → rent cloud compute

超大模型公司正在把关系改成：

> **model-company demand ↔ cloud / data-center / power buildout**

它们通过 multi-year compute commitments、dedicated campuses、chip selection 与 capacity reservation 给基础设施供应商更高 revenue visibility。

## 2. Anchor Compute Buyer Effect

机制可以写成：

> **long-duration model demand → infrastructure financing certainty → earlier data-center/power buildout → earlier chip/HBM/packaging reservation → priority capacity for anchor workload**

所以模型公司本身已经成为上游资本形成的重要需求信号，而不是仅仅接受 hyperscaler 的投资结果。

## 3. OpenAI Stargate：从 nominal commitment 到 secured / construction state

OpenAI 在 2025-01 宣布 Stargate，计划未来四年在美国投资 **US$500B** 建设 AI infrastructure。

随后官方把长期目标描述为到 2029 年确保 10 GW 美国 AI infrastructure。

状态继续前移：OpenAI 在 **2026-04-29** 表示已**超过 10 GW secured-capacity milestone**，并称此前 90 天新增超过 3 GW；**2026-06-01**，Michigan 的 **1 GW The Barn** data-center campus 正式破土。

这些状态必须区分：commitment / secured capacity / construction / energized capacity / utilization。超过 10 GW secured 不等于 10 GW 已全部上电运行。

## 4. Anthropic / AWS：Anchor Workload 也能推动 Custom Silicon

Anthropic 在 2026-04 官方披露：

- 对 AWS technologies 的未来十年 commitment **>US$100B**；
- 可获得 **up to 5 GW** capacity；
- 已使用 **>1M Trainium2 chips**；
- 到 2026 年底预计接近 **1 GW Trainium2/3 capacity**。

这说明 model-company demand 可以成为 cloud custom silicon 的重要 anchor workload。

但公开披露只能证明规模大，不能在缺乏 workload-share 排名时写成“第一大用户”。

## 5. Anchor Buyer 增强的是需求侧权力，不是物理所有权

模型公司可以影响：

- demand certainty；
- chip / system selection；
- cloud roadmap；
- rack deployment；
- power planning；
- infrastructure financing。

但通常并不直接拥有 leading-edge foundry、HBM fab、advanced-packaging fab 或 transmission grid。

所以 Anchor Buyer 是需求侧 bargaining / coordination power 的上升，而不是完整 supply-chain ownership。

## 6. 为什么换云不是简单换账单

模型公司选择的是 accelerator、HBM、interconnect、compiler/runtime、scheduler、rack/pod 与 cloud operations 的完整 system。

迁移可能需要 kernel adaptation、distributed-training changes、performance tuning、observability rework 与 operational revalidation。

这形成 infrastructure switching cost，也解释了为什么长期 commitment 的退出成本可能高于普通 SaaS contract。

## 7. Algorithmic Efficiency 会直接改变 Anchor Demand

如果 architecture 大幅降低同一 capability 的 compute requirement，model company 可以减少长期 capacity commitment，提高 buyer bargaining power，并提高 infrastructure provider 的 utilization risk。

如果 unit cost 下降反而刺激 workload volume 更快增长，长期 commitment 仍可能继续扩大。

所以 Anchor Buyer Demand 是动态需求函数，不是固定指数增长曲线。

## 8. Anchor Buyer 的产业链传导

大规模模型需求可以沿链条传播：

> model demand → cloud CapEx / custom silicon → accelerator/HBM/packaging → data-center power → grid/generation

因此，评估 AI infrastructure cycle 不能只看 hyperscaler CapEx 和 system-vendor commitments，还要独立看 model-company long-duration contracts 是否扩张、改期或利用不足。

## 9. 风险：Anchor Buyer 也会放大 Stranded-Capacity Risk

如果 model-company revenue、financing、workload growth 或 architecture assumptions 发生逆转，long-duration infrastructure commitments 可能变成低利用率资产。

需要持续观察：

- cancellation / rescheduling；
- take-or-pay / minimum commitments；
- utilization；
- project financing；
- customer concentration；
- power and data-center delivery state。

## 10. 当前判断

截至 2026 年 8 月，模型公司已经成为 AI infrastructure 的独立 Anchor Buyer category。

OpenAI Stargate 的 secured-capacity 与 construction 状态、Anthropic/AWS 的十年 compute commitment 和 Trainium deployment 都说明：模型 workload 正在影响 data-center、power 与 custom-silicon buildout。

这使 Anchor Buyer commitments 成为 S2/S3 expansion 与 S4 capital clearing 之间的重要 leading indicator。

## 关键公开来源

- OpenAI — Announcing The Stargate Project: https://openai.com/index/announcing-the-stargate-project/
- OpenAI — Building the compute infrastructure for the Intelligence Age（2026-04-29；surpassed 10 GW milestone）: https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/
- OpenAI — Michigan 1 GW The Barn groundbreaking（2026-06-01）: https://openai.com/index/stargate-michigan-data-center/
- Anthropic / AWS — >US$100B over ten years; up to 5 GW; >1M Trainium2: https://www.anthropic.com/news/anthropic-amazon-compute?lang=us