# Part II · 第13章：Anchor Compute Buyer Effect——模型公司如何重塑基础设施

## 1. 核心判断：头部模型公司正在从“算力租户”升级为基础设施资本形成的锚定买方

传统关系更接近：

> model company → rent cloud compute

但超大模型公司的关系正在演化为：

> **model-company demand ↔ cloud / data-center / power / chip buildout**

当模型公司通过 multi-year compute commitments、dedicated campuses、chip selection、capacity reservation 与长期 cloud agreement 提供更高 revenue visibility 时，它们已经不只是“购买现成算力”。

它们开始影响：

- data-center investment timing；
- cloud custom-silicon roadmap；
- accelerator / HBM / packaging reservation；
- power procurement；
- project financing；
- infrastructure geography。

因此，本报告把这类需求定义为 **Anchor Compute Buyer**。

---

## 2. Anchor Compute Buyer Effect 的核心机制

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

因此，模型公司正在成为上游资本形成的重要 leading indicator。

---

## 3. OpenAI Stargate：必须严格区分 Commitment、Secured、Construction 与 Energized

OpenAI 在 2025-01 宣布 Stargate，计划未来四年在美国投资 **US$500B** 建设 AI infrastructure。[^1]

随后官方把长期目标描述为到 2029 年确保 **10 GW** 美国 AI infrastructure。[^2]

状态继续前移：

- **2026-04-29**：OpenAI 表示已超过 **10 GW secured-capacity milestone**，并称此前 90 天新增超过 3 GW；[^2]
- **2026-06-01**：Michigan 的 **1 GW The Barn** data-center campus 正式破土。[^3]

这些状态不能混写。

必须区分：

> **Announced / Committed → Secured → Construction → Energized → Utilized**

因此：

- US$500B 是长期计划，不是已投入 actual；
- >10 GW secured 不等于 >10 GW 已经 energized；
- 1 GW groundbreaking 不等于 1 GW 已经 online；
- energized capacity 也不等于满负荷 utilization。

这套状态机与第7章 Power 分析保持一致。

### 3.1 PORTS-Pike：Anchor Demand 正在进一步进入 Land + Power + Shell 与信用支持层

2026-08-17，NVIDIA 披露与 SB Energy 在 Ohio PORTS-Pike Technology Campus 的合作：NVIDIA 通过 credit support 锁定 land、power 与 shell（LPS）capacity，初始部署设计支持 **4.25 IT-GW** AI factory capacity；OpenAI 将作为客户，SB Energy 负责建设、持有并运营 data center，项目采用对 OpenAI 的 **20 年 lease**。NVIDIA 同时披露，项目计划容量预计从 **2028 年开始分阶段上线**。[^5]

该项目的重要性不只是规模，而是交易结构发生了变化：

> **Anchor model demand + system-platform credit support + infrastructure developer + long-duration lease**

这说明 system seller 已开始参与解决 model-company balance-sheet / credit profile 与长期基础设施融资之间的缺口。

但必须严格保留状态边界：

- 4.25 IT-GW 是 initial deployment design capacity，不是 2026 已 energized load；
- PORTS-Pike 的后续容量是 future buildout，不是当前 active compute；
- 20 年 lease 提高 revenue visibility，也提高 customer concentration 与 duration risk；
- land / power / shell 已被锁定，不等于最终 compute utilization 已经实现。

NVIDIA 在 2026-08-26 FY27 Q2 earnings call 进一步表示，OpenAI 现有与计划中的 NVIDIA Compute commitments 合计约 **12 GW**。[^6] 这是 NVIDIA management commentary，应作为 platform-side demand visibility 读取，不能改写成 OpenAI 已有 12 GW energized capacity。

---

## 4. Anthropic / AWS：Anchor Workload 可以反向推动 Custom Silicon

Anthropic 2026-04 官方披露：[^4]

- 对 AWS technologies 的未来十年 commitment **>US$100B**；
- 可获得 **up to 5 GW** capacity；
- 已使用 **>1M Trainium2 chips**；
- 到 2026 年底预计接近 **1 GW Trainium2/3 capacity**。

这说明 model-company demand 不只是购买 GPU，也可以成为 hyperscaler custom silicon 的长期 anchor workload。

这会形成一条新的反馈链：

> **large model workload → custom-silicon deployment → production feedback → system optimization → lower TCO → more anchor workload**

因此，Anchor Buyer 与 Cloud System-Stack Substitution 不是两条独立故事，而是可以相互强化。

---

## 5. Anchor Buyer 增强的是 Demand-Side Coordination Power，而不是完整物理所有权

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

所以 Anchor Buyer 增强的是：

> **demand-side bargaining + coordination + financing power**

而不是 supply-chain ownership。

这一区分很重要。

一个 buyer 可以通过长期 commitment 显著影响上游资本形成，但仍然受 advanced logic、HBM、packaging、power 与 permitting 的物理约束。

---

## 6. 长期 Compute Commitment 也会提高 Switching Cost

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

## 7. Anchor Buyer Demand 不是固定指数增长函数

长期 compute demand 会被两组相反力量同时影响。

### 降低单位需求的因素

- algorithmic efficiency；
- quantization；
- sparse architecture；
- better scheduling；
- higher utilization；
- lower bytes/token；
- faster hardware。

### 扩大总需求的因素

- model capability expansion；
- inference adoption；
- agent workflows；
- longer context；
- multimodality；
- lower unit cost stimulating more usage。

因此：

> **unit compute demand can fall while total infrastructure demand rises**

Anchor Buyer Demand 不能用简单“每年固定翻倍”外推。

真正需要跟踪的是：

- workload volume；
- utilization；
- unit cost；
- monetization；
- commitment renewal；
- project delivery。

---

## 8. Anchor Buyer 如何沿产业链传导

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

## 9. Anchor Buyer 的最大风险：Customer Concentration + Duration Mismatch

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

## 10. 判断 Anchor Buyer 是否正在强化，应看什么

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

因此，Headline commitment 本身不是终点。

真正重要的是：

> **长期需求是否最终转化成高利用率、可货币化的真实 workload。**

---

## 11. 当前判断

截至 2026 年 8 月，模型公司已经可以被视为 AI infrastructure 的独立 Anchor Buyer category。

OpenAI Stargate 的 secured-capacity 与 construction 状态、Anthropic/AWS 的十年 compute commitment 与 Trainium deployment，都说明：

> **model workload 已经开始影响 cloud architecture、custom silicon、data-center buildout、power procurement 与基础设施融资。**

因此，Anchor Buyer commitments 是连接 **S2/S3 expansion** 与 **S4 capital clearing** 的关键 leading indicator。

它既可以加速 AI infrastructure 的资本形成，也可以在 utilization 不足时放大 stranded-capacity 与 duration-mismatch risk。

## References

[^1]: OpenAI, “Announcing The Stargate Project,” 2025-01, https://openai.com/index/announcing-the-stargate-project/
[^2]: OpenAI, “Building the compute infrastructure for the Intelligence Age,” 2026-04-29, surpassed 10 GW secured-capacity milestone, https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/
[^3]: OpenAI, “Stargate Michigan Data Center,” 2026-06-01, 1 GW The Barn campus groundbreaking, https://openai.com/index/stargate-michigan-data-center/
[^4]: Anthropic, “Anthropic and Amazon expand collaboration,” 2026-04, >US$100B over ten years, up to 5 GW and >1M Trainium2 chips, https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
[^5]: NVIDIA, “NVIDIA Guarantees SB Energy's PORTS-Pike Technology Campus in Ohio to Exclusively Host NVIDIA AI Compute,” 2026-08-17, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx
[^6]: NVIDIA, FY27 Q2 Earnings Call transcript, 2026-08-26, OpenAI existing and planned NVIDIA Compute commitments approximately 12 GW, https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf
