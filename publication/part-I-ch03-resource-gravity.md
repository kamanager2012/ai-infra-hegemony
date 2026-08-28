# Part I · 第3章：AI Resource Gravity 与 Non-AI Residual Capacity


## 1. “AI 虹吸”不是把所有半导体产能一起抽走

AI infrastructure 对供应链的影响具有强烈层级性。真正容易被重排的，是与 frontier AI 共享且短期供给弹性较低的资源：

- advanced logic；
- HBM / RDIMM / selected DRAM；
- advanced packaging；
- high-end substrate / networking；
- power-management components；
- data-center power。

本书将这种高价值 demand 对资本与供给的吸引定义为 **AI Resource Gravity**。

## 2. Resource Gravity 的经济机制

如果一个需求池能够同时提供更高 willingness-to-pay、更长订单、更高利用率确定性和更强信用，供应商有经济动机优先把新增资本和产能投向它。

传导链可写成：

> high-value AI/server demand → higher expected return → product-mix / capacity allocation shift → lower residual capacity for lower-priority demand

这不意味着供应商只服务第一名，也不意味着所有传统市场都被停止供货。它描述的是**边际新增资源的优先级变化**。

### 2.1 价格不是唯一清算机制：Allocation Assurance 比 Spot Price 更关键

在极端紧缺期，市场并不只通过涨价清算。**长期协议、客户信用、预付款、采购规模和供应商给出的 allocation fulfillment** 会先决定谁能拿到足够的量。

TrendForce 2026-01 明确指出，美国 CSP 锁定 capacity 后，其他买家为了确保 supply allocation 被迫接受更高价格；2026-03 又指出，PC OEM / module maker 如果 allocation fulfillment 较低，只能从供应商或模组厂以更高价格补货。

因此：

> **willingness-to-pay ≠ guaranteed quantity**

真正的系统性风险不是“价格涨了多少”，而是 residual capacity 低到使次级买家即使接受更高报价，也无法获得足够、按时、可持续的交付量。

这比“某一家拿走100%产能”的绝对化说法更可验证，也更接近产业现实。

## 3. 为什么 Non-AI Residual Capacity 比总产能更重要

传统市场真正获得的供给可以抽象为：

> **Non-AI Residual Capacity = total effective supply − AI/server absorption − other priority demand**

如果 total supply +20%，但 AI/server demand 同期吸收 +40%，非 AI 市场的有效 residual capacity 仍可能下降。

因此，“全球产能增长”不能自动推出 PC、smartphone、general server 或消费 GPU 的供给恢复宽松。

## 4. Memory 是最清晰的 observed crowding-out 路径

Micron 一手披露 same node / same bits 条件下 HBM3E 约需要 DDR5 **3× wafer supply**；TrendForce 预计 2026 年 HBM + RDIMM 合计约占 DRAM bit supply **51%**。

这使 memory 层出现一条可观察机制：

> HBM/RDIMM demand 上升 → wafer/cleanroom/capital 向高价值 server products 倾斜 → conventional DDR/LPDDR residual supply 改变 → consumer/general-compute price 与 configuration 承压

51% 是 2026E bit-supply forecast，不是 HBM-only share，也不是 wafer share。

## 5. PC 与 Gaming：GPU allocation + memory residual 双重暴露

NVIDIA FY26 10-K 披露 Gaming revenue **US$16.0B、同比 +41%**，同时预计 supply constraints 会成为 FY27 Q1 及之后 Gaming 的 headwind。

这证明消费 GPU 侧存在供应约束，但不能直接推出所有约束都由 Data Center allocation 造成。

PC 还承受第二条链：server/HBM demand 改变 DRAM product mix，进而影响 DDR5/LPDDR residual supply。于是 PC 更容易出现 GPU availability 与 memory pricing 的双重压力。

## 6. General Server：RDIMM 已进入同一高价值 memory pool

general server 不一定使用 HBM，但大量使用 DDR5 RDIMM。TrendForce 把 RDIMM 与 HBM 一起纳入 2026 DRAM bit-supply 前向结构，说明 traditional server memory 并不是完全独立的 commodity river。

所以 AI/server infrastructure expansion 可以通过 memory allocation 间接提高 general-server cost，即使服务器本身没有使用 frontier accelerator。

## 7. Smartphone：没有被 AI 挤掉，但增量资源竞争已改变

TSMC 2025 smartphone platform 占全年 net revenue **29%**，platform revenue 同比增长 **11%**；HPC 占 **58%**，增速更高。

这不能写成“AI 取代 smartphone”。更准确的是：

- smartphone 仍是巨大需求平台；
- HPC 对新增 leading-edge investment 的吸引更强；
- LPDDR / selected packaging / power-management components 可能与 AI/server demand 共享部分资源；
- flagship input cost 与中端 node migration 节奏更容易受到 residual-capacity pressure。

## 8. Automotive：暴露更慢、更选择性

automotive 具有长 qualification cycle、高 reliability requirement 和大量 mature-node usage，因此不会在所有环节与 frontier AI 直接竞争。

其主要共享层更接近 central compute、memory、power management 与 selected advanced packaging。汽车更适合描述为**第二阶段选择性传导**，而不是第一波全面 shortage。

## 9. Residual pressure 通常先表现为升级税，而不是停产

当有效残量下降，企业常见的应对是：

1. 涨价；
2. 降规格；
3. 延后升级；
4. 延长 mature node / alternative supplier 的使用周期。

所以供应链压力更可能先表现为 flagship BOM 上升、replacement cycle 延长、high-end feature 下放变慢和 product segmentation 加剧，而不是整个行业立即停产。

## 10. China parallel supply 会改变本地 residual structure，但不能自动关闭 frontier bottleneck

中国本地 logic、DRAM、NAND 与终端制造能力增强，可以缓解部分 domestic consumer-market pressure。

但替代必须分层：consumer computing 较强，general compute 部分替代，frontier AI 则仍取决于 advanced logic、HBM-class memory、packaging、interconnect 与 software closure。

因此，本地消费供给扩张可以改善国内终端 residual capacity，却不会自动消除全球 frontier AI 的上游瓶颈。

## 11. 实体企业还承担第二层 AI adoption cost

制造企业采用 AI 时，不只面对硬件/input cost，还要支付 cloud inference、software integration、data pipeline、security/compliance 和 workflow redesign。

真正的 productivity return 应按：

> **Net productivity value = productivity gain − total AI adoption cost**

因此，上游 resource inflation 与下游 AI-service cost 可以同时作用于实体企业。

## 12. 当前判断与证伪

截至 2026 年 8 月，证据更支持：

> **选择性传导 + 产品分层 + Non-AI Residual Capacity pressure**

而不是“所有芯片都被 AI 抢走”。

如果 DDR/LPDDR 价格与供给恢复宽松、consumer GPU availability 明显改善、smartphone/general-server upgrade 不再受到 shared-resource pressure，且 memory/packaging product mix 不再持续向 AI/server 倾斜，本章对 crowding-out 的判断应下调。

## 关键公开来源

- NVIDIA FY26 10-K — Gaming +41% and supply-constraint headwind: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
- Micron FY24 Q2 Prepared Remarks — HBM3E ≈3× DDR5 wafer supply: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- TrendForce — 2026E HBM + RDIMM = 51% of DRAM bit supply: https://www.trendforce.com/presscenter/news/20260825-13198.html
- TSMC 4Q25 Presentation — smartphone 29%, HPC 58%: https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
- TrendForce 2026-01-05 — CSPs lock capacity, other buyers accept higher prices to secure allocation: https://www.trendforce.com/presscenter/news/20260105-12860.html
- TrendForce 2026-03-31 — lower allocation fulfillment forces OEMs to procure at higher prices: https://www.trendforce.com/presscenter/news/20260331-12995.html