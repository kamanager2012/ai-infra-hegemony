# Part II · 第11章：NVIDIA 从 Accelerator Vendor 向 AI Factory 扩张

## 1. NVIDIA 的扩张方式不是传统 IDM 式纵向整合

NVIDIA 并不通过拥有 leading-edge fabs、HBM fabs 或整个 data-center real estate 来控制系统。

它的扩张更接近：

> **interface control + reference architecture + software/runtime + supply orchestration**

系统边界已经覆盖 GPU / CPU、NVLink / NVSwitch、networking、rack-scale design、liquid-cooling requirements、CUDA/runtime、AI Enterprise、NIM / NeMo、DGX 与 cloud-service extensions。[^1][^2][^3]

## 2. Rack-scale sales unit 会重新定义 OEM / ODM 的角色

在 accelerator-card 时代，OEM 可以围绕 GPU 定义大量 server architecture。

进入 rack-scale system 后，power delivery、cooling、fabric、cable topology、firmware、rack layout 和 software validation 被更强地绑定到 reference architecture。

这不意味着 Dell、HPE、Lenovo、ODM 等失去产品能力，而是 system-platform owner 对整机设计和 qualification 的约束增强。

## 3. Networking 已经成为 Compute Platform 的一部分

大模型 training/inference 的性能越来越依赖 multi-GPU scaling 与 collective communication。

当 accelerator、NVLink/NVSwitch、InfiniBand/Ethernet networking 与 software communication stack 被一起设计时，network 不再只是第三方附属品，而成为 system performance 与 switching cost 的组成部分。

所以平台竞争逐渐从“GPU + 任意网络”变成一套更统一的 AI Factory architecture。

## 4. DGX Cloud 的价值主要在 Platform Extension

在没有独立大规模收入分项的情况下，不应把 DGX Cloud 写成已经取代 hyperscaler 的第二主业。

更可靠的战略功能是：

1. 展示完整 NVIDIA architecture；
2. 获得真实 workload / deployment feedback；
3. 降低客户首次使用全栈系统的门槛；
4. 增加与 hyperscaler 之间的渠道与议价选择。

它更接近 platform extension 与 reference deployment channel。

## 5. AI Enterprise / NIM / NeMo 的核心作用是强化部署与迁移成本

软件产品让 system platform 从 hardware purchase 延伸到 model serving、deployment、optimization、enterprise support 与 lifecycle management。

在未披露独立软件收入之前，本报告不把这些产品的贡献估算成固定“软件税”或单独利润池。

更准确的作用是：

> **降低 platform 内部部署摩擦，提高 platform 外部迁移成本。**

## 6. Asset-light Orchestration 为什么重要

NVIDIA 把大量 manufacturing CapEx 留在 TSMC、memory vendors、packaging ecosystem 与 infrastructure providers，同时用 long-term commitments、prepayments、roadmap coordination 和 volume certainty 影响这些供应商扩产。FY26 10-K 的 manufacturing, supply and capacity commitments 为这一 supply-orchestration 模式提供了公司层事实锚。[^4]

这形成典型：

> system definition / cash generation 留在平台 → 重资产扩产留在供应链 → 平台用订单和承诺锁定未来资源

它提高了平台资本效率，也把外部 supply elasticity 变成平台战略的一部分。

## 6A. Asset-light 是相对概念，不等于零 Balance-Sheet Exposure

2026 年 8 月的新交易结构表明，NVIDIA 的 supply orchestration 正在部分延伸到 infrastructure capital。

- 公司宣布与大型长期资本提供方建立 compute-financing platforms，目标是随时间动员 **>US$500B third-party capital**；[^5]
- PORTS-Pike 中，NVIDIA 为 land + power + shell buildout 提供 credit support，并投资 **US$1.5B** 于 SB Energy。[^6]

因此，NVIDIA 仍然没有变成拥有所有 fab、data center 与 power assets 的传统重资产运营商，但“asset-light platform”也不能再理解为完全不承担 infrastructure financing risk。

更准确的描述是：

> **平台尽量让 fab / data center / power 资产留在外部主体，同时选择性使用 cash、equity、credit support 和 long-duration coordination 去加速关键基础设施形成。**

这可以提高 Time-to-Capacity，也可能把 customer concentration、credit 与 duration risk 部分拉回平台自身。

## 7. Physical AI 是系统平台的外延，但不属于本章主证据链

Automotive、robotics、simulation 与 edge deployment 延续同一种 system-platform 逻辑：hardware、runtime、simulation、developer tooling 与 deployment 被组织成一套工作流。

但 Physical AI 的产业门槛还包括 actuator、sensor、battery、safety、manufacturing 与 field reliability，不能由 Data Center 平台优势直接外推。

因此，本章只把 Physical AI 视为 NVIDIA system architecture 的潜在外延；其独立产业逻辑见[第15章：Physical AI 与机器人系统的真正瓶颈](part-II-ch15-physical-ai.md)。

## 8. 纵向扩张的六个边界

NVIDIA 的系统扩张并非没有制衡：

- hyperscaler custom system stack；
- open compiler/runtime / portability；
- alternative networking；
- customer multi-sourcing；
- regulation / interface remedy；
- physical power and supply constraints；
- China parallel stack。

如果这些变量同时增强，NVIDIA 仍可能是最强 system platform，但 system definition 的议价能力会下降。

## 9. “AI Factory” 的正确含义

AI Factory 不应被当成“每个数据中心都是 NVIDIA 工厂”的所有权叙事。

更准确地说，它代表一个设计哲学：compute、memory、networking、software、rack、cooling 与 deployment 被当成统一生产系统优化。

这一思想的产业影响在于销售单位、qualification、supply commitments 与 data-center engineering 都被拉进同一个 roadmap。

## 10. 当前判断

截至 2026 年，最确定的变化是 NVIDIA 已经明显从 accelerator vendor 向 system-platform / AI-Factory architecture 扩张。

但“纵向扩张”与“产业完全被一个平台控制”仍是两个不同命题。下一阶段真正需要观察的是：system definition 能否继续转化成长期 workload、supply commitments 和低迁移成本的跨代客户留存。


## References

[^1]: NVIDIA, NIM official product page, optimized inference microservices across cloud, data center, workstation and edge, https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/
[^2]: NVIDIA, AI Foundation Models / NeMo, NVIDIA AI Foundry architecture, https://www.nvidia.com/en-us/ai-data-science/foundation-models/
[^3]: NVIDIA, “Introducing NVIDIA DGX Cloud Lepton,” unified AI platform and compute marketplace, https://developer.nvidia.com/blog/introducing-nvidia-dgx-cloud-lepton-a-unified-ai-platform-built-for-developers/
[^4]: NVIDIA Corporation, FY26 Form 10-K, U.S. SEC, Data Center, networking, platform and supply-chain disclosures, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
[^5]: NVIDIA, 2026-08-10, AI compute infrastructure financing platforms and >US$500B third-party-capital mobilization target, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Partners-With-Apollo-BlackRock-Blackstone-Brookfield-Goldman-Sachs-and-KKR-to-Establish-AI-Compute-Infrastructure-Financing-Platforms-to-Mobilize-Over-500-Billion-of-Third-Party-Capital/default.aspx
[^6]: NVIDIA, 2026-08-17, PORTS-Pike / SB Energy / OpenAI, LPS credit support and US$1.5B SB Energy investment, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx
