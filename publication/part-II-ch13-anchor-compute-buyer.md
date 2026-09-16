# Part II · 第13章：Anchor Compute Buyers——Long-Duration Demand 如何提前拉动 Infrastructure

## 1. Frontier Model Demand 可以提前拉动 Infrastructure

在较小规模下，model company 是 compute tenant；到了 frontier scale，durable demand 本身可以成为 chip、data center、land 与 power 的 financing input。

关系从：

> model company → rent existing compute

逐步转向：

> **model-company commitment → revenue visibility → financing certainty → earlier cloud / data-center / power / chip buildout**

真正需要判断的不是 model company 是否“拥有整个 stack”，而是它的 demand 是否足够大、足够长期，从而改变上游 capacity 被 financing、reservation 与 buildout 的时间。

---

## 2. Demand Certainty 成为 Capital-Formation Input

传导链可以写成：

> **long-duration model demand → revenue visibility → financing certainty → earlier infrastructure buildout → earlier resource reservation → priority capacity for anchor workload**

关键变化在于：需求本身开始推动供给提前建设。

这与传统“先建云，再等客户租用”的模式不同。

如果 buyer commitment 足够长、足够大，供应商与资本市场会更愿意：

- 提前建 data center；
- 提前签 power contract；
- 提前锁定 chip / HBM / packaging；
- 提前部署 custom silicon；
- 提前配置项目融资。

model-company demand 已经成为上游 capital formation 的重要 signal。

---

## 3. OpenAI / Stargate：Delivery State 比 Headline Scale 更重要

OpenAI 在 2025-01 宣布 Stargate，计划未来四年在美国投资 **US$500B** 建设 AI infrastructure。[^1]

随后官方把长期目标描述为到 2029 年确保 **10 GW** 美国 AI infrastructure。[^2]

状态继续前移：

- **2026-04-29**：OpenAI 表示已超过 **10 GW secured-capacity milestone**，并称此前 90 天新增超过 3 GW；[^2]
- **2026-06-01**：Michigan 的 **1 GW The Barn** data-center campus 正式破土。[^3]

这些状态不能混写。

必须区分：

> **Announced / Committed → Contracted / Secured → Permitted → Construction / Transition → Energized → Utilized**

因此：

- US$500B 是长期计划，不是已投入 actual；
- >10 GW secured 不等于 >10 GW 已经 permitted、constructed 或 energized；
- 1 GW groundbreaking 不等于 1 GW 已经 online；
- energized capacity 也不等于满负荷 utilization；
- IT-GW、PPA GW 与 generation GW 不能机械互换。

这套状态机与[第7章](part-I-ch07-power-constraint.md) Power 分析保持一致。

### 3.1 PORTS-Pike：Anchor Demand 已进入 LPS 与 Credit Support

2026-08-17，NVIDIA 披露与 SB Energy 在 Ohio PORTS-Pike Technology Campus 的合作：NVIDIA 通过 credit support 锁定 land、power 与 shell（LPS）capacity，初始部署设计支持 **4.25 IT-GW** AI factory capacity；OpenAI 将作为客户，SB Energy 负责建设、持有并运营 data center，项目采用对 OpenAI 的 **20 年 lease**。announcement-stage 口径是从 **calendar 2028** 开始分阶段上线；NVIDIA 后续 FY27 Q2 Form 10-Q 则把第一 guarantee/service phase 写为预计在 **fiscal 2029** 开始。两者属于可兼容的 time identity，不是两个可以加总的交付节点。[^5]

该项目的重要性不只是规模，而是交易结构发生了变化：

> **Anchor model demand + system-platform credit support + infrastructure developer + long-duration lease**

这说明 system seller 已开始参与解决 model-company balance-sheet / credit profile 与长期基础设施融资之间的缺口。

但必须严格保留状态边界：

- 4.25 IT-GW 是 initial deployment design capacity，不是 2026 已 energized load；
- PORTS-Pike 的后续容量是 future buildout，不是当前 active compute；
- 20 年 lease 提高 revenue visibility，也提高 customer concentration 与 duration risk；
- land / power / shell 已被锁定，不等于最终 compute utilization 已经实现。

NVIDIA 在 2026-08-26 FY27 Q2 earnings call 进一步表示，OpenAI 现有与计划中的 NVIDIA Compute commitments 合计约 **12 GW**。[^6] 这是 NVIDIA management commentary，应作为 platform-side demand visibility 读取，不能改写成 OpenAI 已有 12 GW energized capacity。

PORTS-Pike 的 **4.25 IT-GW** 与 OpenAI 此前披露的 **>10 GW secured capacity** 之间的口径关系，公开材料未说明；本报告不将两者相加，也不假定其从属关系。

---

## 4. Anthropic / AWS：Anchor Workload 可以加速 Second Stack

Anthropic 2026-04 官方披露：[^4]

- 对 AWS technologies 的未来十年 commitment **>US$100B**；
- 可获得 **up to 5 GW** capacity；
- 已使用 **>1M Trainium2 chips**；
- 到 2026 年底预计接近 **1 GW Trainium2/3 capacity**。

这说明 model-company demand 不只是购买 GPU，也可以成为 hyperscaler custom silicon 的长期 anchor workload。

这会形成一条新的反馈链：

> **large model workload → custom-silicon deployment → production feedback → system optimization → lower TCO → more anchor workload**

因此，Anchor Buyer 与 cloud system-stack substitution 不是两条彼此独立的机制，而是可以相互强化。

### 4.1 xAI / Colossus：Self-Built Variant

xAI 是模型公司直接进入基础设施建设的案例。xAI 在 2024-12 的一手更新中披露，**Colossus** 使用 **100,000 颗 NVIDIA Hopper GPU**，并在 **122 天**内达到 fully operational；公司同时表示计划把集群扩展到合计 **200,000 颗 Hopper GPU**。[^7]这一案例能够直接证明的是：模型公司开始自行组织大规模 compute infrastructure，而不再只依赖既有 cloud capacity。

xAI 的路径比 Stargate 与 Anthropic/AWS 更直接：它不是通过 cloud 或合资项目租用 capacity，而是作为 model company 直接驱动 land、power 与 chip 的前置资本形成。这说明 Anchor Buyer 对上游资本形成的引导并非单一模式——长期租用型 commitment 与自建型 buildout 可以并存。

但 xAI 案例同样受状态边界约束：Colossus 上线不等于满负荷 utilization；扩产计划不等于已装机容量。

---

## 5. Anchor Buyer 获得的是 Coordination Power，不是 Ownership

模型公司可以影响：

- demand certainty；
- chip / system selection；
- cloud roadmap；
- rack deployment；
- power planning；
- financing schedule。

但它们通常并不直接拥有：

- leading-edge foundry；
- HBM fab；
- advanced-packaging fab；
- transmission grid；
- generation fleet。

Anchor Buyer 增强的是：

> **demand-side bargaining + coordination + financing power**

而不是 supply-chain ownership。

这一区分很重要。

一个 buyer 可以通过长期 commitment 显著影响上游资本形成，但仍然受 advanced logic、HBM、packaging、power 与 permitting 的物理约束。

---

## 6. Long-Duration Commitment 会形成 Switching Cost

模型公司采购的不是一张 accelerator card，而是一套完整 system：

- accelerator；
- HBM；
- interconnect；
- compiler/runtime；
- scheduler；
- rack/pod；
- cloud operations；
- observability；
- failure recovery。

因此，“换云”往往不是简单更换账单。

迁移可能需要：

- kernel adaptation；
- distributed-training changes；
- performance tuning；
- data-pipeline changes；
- observability rework；
- operational revalidation。

这意味着长期 commitment 的退出成本可能显著高于普通 SaaS contract。

同时，这也解释了为什么 hyperscaler custom stack 一旦获得大型 anchor workload，就可能形成更强学习效应与 lock-in。

---

## 7. Anchor Demand 最终仍取决于 Workload Economics

长期 compute demand 会被两组相反力量同时影响。

**降低单位需求的因素**

- algorithmic efficiency；
- quantization；
- sparse architecture；
- better scheduling；
- higher utilization；
- lower bytes/token；
- faster hardware。

**扩大总需求的因素**

- model capability expansion；
- inference adoption；
- agent workflows；
- longer context；
- multimodality；
- lower unit cost stimulating more usage。

因此：

> **unit compute demand can fall while total infrastructure demand rises**

anchor-buyer demand 是动态 demand function，不能用固定指数曲线外推。

真正需要跟踪的是：

- workload volume；
- utilization；
- unit cost；
- monetization；
- commitment renewal；
- project delivery。

---

## 8. Anchor Demand 沿 Infrastructure Chain 传播

大规模模型需求可以沿完整产业链传播：

> **model demand → cloud CapEx / custom silicon → accelerator / HBM / packaging → data center → power → grid / generation**

这意味着 AI infrastructure cycle 不能只观察：

- NVIDIA revenue；
- hyperscaler CapEx；
- TSMC / memory CapEx。

还必须独立观察：

- model-company long-duration contract；
- secured capacity；
- project construction；
- utilization；
- commitment rescheduling。

如果 Anchor Buyer commitment 继续扩张并被真实 workload 吸收，S2/S3 的资本扩张动力会增强。

如果 commitment 改期、缩减或利用不足，则 S4 risk 上升。

---

## 9. Risk：Concentration 与 Duration Mismatch

Anchor Buyer 能提高融资确定性，也会提高集中度风险。

如果一个大型 infrastructure project 主要依赖少数 model-company workload，其资本回收就更依赖这些客户未来的：

- revenue；
- financing；
- technical roadmap；
- workload growth；
- contract performance。

与此同时，AI hardware 的技术周期短，而：

- data-center shell；
- power contract；
- grid connection；
- generation asset；

具有更长经济寿命。

于是会形成：

> **shorter-cycle AI workload / compute technology vs longer-cycle infrastructure obligation**

如果模型公司增长假设失效，长期 commitment 可能从“融资锚”转化为 stranded-capacity risk。

---

## 10. Monitoring Anchor-Buyer Strength

### 强化信号

- long-duration compute commitments 继续扩大；
- secured capacity 增长；
- dedicated campus / power projects 进入 construction；
- custom silicon 获得更多 anchor workload；
- utilization 与 workload revenue 同步增长；
- commitment 续签或延长。

### 弱化信号

- project rescheduling；
- commitment renegotiation；
- cancellation；
- utilization 低于预期；
- model-company financing / revenue 压力；
- capacity delivery 明显领先于 workload growth。

headline commitment 不是分析终点。

真正重要的是：

> **长期需求是否最终转化成高利用率、可货币化的真实 workload。**

---

## 11. Current Read

截至 2026 年 8 月，大型 model companies 已经构成 AI infrastructure 中一个独立的 Anchor Buyer category。

OpenAI Stargate 的 secured-capacity 与 construction milestones、Anthropic/AWS 的十年 compute commitment 与 Trainium deployment、xAI 的 self-built Colossus buildout，以及 PORTS-Pike 的 LPS / credit-support structure，都表明 model workload 正在塑造：

> **cloud architecture、custom silicon、data-center buildout、power procurement 与 infrastructure finance**

anchor-buyer commitments 是连接 **S2/S3 expansion** 与 **S4 capital clearing** 的关键 leading indicator。这个信号的 leading-indicator value 目前由 Stargate、Anthropic/AWS 与 xAI Colossus 三个 documented cases 支持，仍需要在更多完整周期中重新检验。

它们可以加速 AI-infrastructure capital formation；在 utilization 走弱时，也可能放大 stranded-capacity 与 duration-mismatch risk。

## 12. 什么事实会改变当前判断

anchor-buyer mechanism 应在以下情况下被下调：

- long-duration commitments 大规模改期、缩减或重谈；
- secured capacity 长期无法转化为 energized / utilized capacity；
- anchor workload utilization 持续不足；
- model-company monetization 无法覆盖长期 infrastructure obligation；
- project finance increasingly 依赖更强 seller support 而非 customer / third-party cash flow。

相反，合同金额或 secured GW 继续增加，如果没有 delivery 与 utilization 验证，也不能单独强化本章结论。

## References

[^1]: OpenAI, “Announcing The Stargate Project,” 2025-01, https://openai.com/index/announcing-the-stargate-project/
[^2]: OpenAI, “Building the compute infrastructure for the Intelligence Age,” 2026-04-29, surpassed 10 GW secured-capacity milestone, https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/
[^3]: OpenAI, “Stargate Michigan Data Center,” 2026-06-01, 1 GW The Barn campus groundbreaking, https://openai.com/index/stargate-michigan-data-center/
[^4]: Anthropic, “Anthropic and Amazon expand collaboration,” 2026-04, >US$100B over ten years, up to 5 GW and >1M Trainium2 chips, https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
[^5]: NVIDIA, 2026-08-17 PORTS-Pike announcement, initial 4.25 IT-GW design capacity, LPS credit support, 20-year OpenAI lease, and announcement-stage phased capacity beginning in calendar 2028, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx ; NVIDIA Corporation, FY27 Q2 Form 10-Q, guarantees phasing in across nine data centers with the first expected in fiscal 2029, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^6]: NVIDIA, FY27 Q2 Earnings Call transcript, 2026-08-26, OpenAI existing and planned NVIDIA Compute commitments approximately 12 GW, https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf
[^7]: xAI, “xAI raises $6B Series C,” 2024-12-23，一手披露 Colossus 使用 100,000 颗 NVIDIA Hopper GPU、122 天达到 fully operational，并计划扩展到合计 200,000 颗 Hopper GPU，https://x.ai/news/series-c
