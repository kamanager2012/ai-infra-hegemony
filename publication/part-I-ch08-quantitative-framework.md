# Part I · 第8章：AI 基础设施量化框架与 Rolling Bottleneck Cascade

## 1. 核心原则：量化不是把所有数字塞进一个总模型

AI infrastructure 最容易出现的分析错误，是把不同物理池、不同会计科目、不同时间窗口和不同证据等级的数字串成一个看似完整的总量模型。

本报告只允许能够保持量纲和证据身份的量化进入主链。

核心原则是：

> **先确认物理对象和分母，再做计算；无法公开闭合的变量保留为参数，不用“合理猜测”补齐。**

量化主要服务四类问题：

1. workload 对 compute / memory / interconnect 的需求强度；
2. system spec 如何转化成 material / power requirement；
3. 某一 scarce layer 是否存在有效供给缺口；
4. bottleneck、utilization 与 capital return 如何随时间变化。

---

## 2. Roofline：为什么不能只用 FLOPS 衡量 AI System

Roofline model 的基本关系是：

> **Performance = min(Peak Compute, Memory Bandwidth × Arithmetic Intensity)**

临界算术强度：

> **I_critical = Peak Compute / Memory Bandwidth**

当 workload 的 arithmetic intensity 低于临界值时，系统进入 memory-bound 区域。

这解释了为什么 frontier inference / training 不能只比较 peak FLOPS。

真实 workload 还会受到：

- HBM bandwidth；
- model state movement；
- KV cache；
- MoE routing；
- collective communication；
- interconnect；
- synchronization；

等因素影响。

因此，本报告把 compute、memory 与 interconnect 放在同一 system unit 中分析。

---

## 3. Algorithmic Efficiency 会改变需求函数，但不会自动删除物理约束

算法与架构可以改变：

- activated compute；
- bytes/token；
- KV-cache requirement；
- communication pattern；
- batch / concurrency；
- serving efficiency。

DeepSeek-V3 / V2 等公开案例说明，architecture improvement 可以显著改变单位 capability 所需的硬件资源。[^1][^2]

但量化时必须区分：

> **unit-resource demand**

与

> **total infrastructure demand**

如果单位 workload 成本下降，而 workload volume 增长得更快，总基础设施需求仍然可能继续上升。

因此：

> **Efficiency gain ≠ infrastructure demand decline**

真正需要计算的是 demand elasticity，而不是只计算单位成本下降。

---

## 4. System Spec 可以用于 Material Identity，但不能凭空制造 Shipment

GB200 NVL72 官方规格包括：

- 72 Blackwell GPU；
- 36 Grace CPU；
- 13.4 TB HBM3E；
- 17 TB LPDDR5X。[^3]

这类公开规格可以回答：

> **一套 system 需要什么、需要多少。**

但如果没有公开 shipment / deployment count，就不能回答：

> **全行业实际消耗了多少。**

因此：

> **official system spec × hypothetical deployment count = scenario arithmetic**

而不是 actual shipment。

同理，不能通过：

> Data Center revenue ÷ 自拟 system ASP

反推出“实际 rack 数”，再继续传播成 HBM、packaging 和 power 的事实数字。

---

## 5. HBM：Bit Demand 与 Manufacturing Input 不是一一对应

Micron FY24 Q2 prepared remarks 给出一个重要一手边界：

> 在 same technology node / same number of bits 条件下，HBM3E 约需要 DDR5 **3× wafer supply**。[^4]

因此：

> **same bits ≠ same wafer input**

这说明 HBM bit share 上升时，对 DRAM wafer / cleanroom input 的压力可能高于 bit share 本身。

但 3× 必须保留适用条件：

- same technology node；
- same number of bits；
- HBM3E vs DDR5；
- 不是售价倍数；
- 不是未来所有 HBM generation 的永久常数。

---

## 6. AI Capacity Gap：先判断“现在缺不缺”，再判断“缺口在扩大还是收敛”

对每个物理层 (i)，定义：

```text
AI_Capacity_Gap_i(t)
= AI_Effective_Demand_i(t)
- AI_Effective_Capacity_i(t)
```

其中 (i) 可以分别代表：

- advanced logic；
- HBM / DRAM；
- advanced packaging；
- networking；
- power。

Demand 与 Capacity 必须使用：

- 同一 physical layer；
- 同一 delivery window；
- 同一 qualification / quality boundary；
- 同一 physical unit。

例如：

- wafers/month；
- qualified package starts/month；
- bits/year；
- MW。

解释：

- **Gap > 0**：当前有效供给不足；
- **Gap ≈ 0**：当前接近平衡；
- **Gap < 0**：当前存在有效余量。

---

## 7. Capacity Growth Gap：只描述方向，不能代替当前缺口

再定义：

```text
AI_Capacity_Growth_Gap_i(t)
= Growth(AI_Effective_Demand_i)
- Growth(AI_Effective_Capacity_i)
```

它回答的是：

> **当前供需缺口更可能扩大还是收敛？**

- **Growth Gap > 0**：短缺压力可能加剧，或既有余量缩小；
- **Growth Gap < 0**：供给在追赶，短缺可能收敛；
- **Growth Gap = 0**：只表示增长速度相同，不表示当前没有短缺。

因此：

> **Absolute Gap 与 Growth Gap 必须同时看。**

一个市场可以仍然短缺，但供给正在快速追赶；也可以当前还有余量，但需求增长速度正在迅速侵蚀余量。

---

## 8. Non-AI Residual Capacity 回答的是另一类问题

AI Capacity Gap 观察 AI 侧。

传统市场则需要看：

```text
NonAI_Residual(t)
= Effective_Supply(t)
- AI_Server_Absorption(t)
- Other_Priority_Demand(t)
```

它回答：

> **AI 和其他高优先需求吸收之后，非 AI 市场还能获得多少有效供给。**

因此：

- AI Capacity Gap；
- AI Capacity Growth Gap；
- Non-AI Residual Capacity；

不能互相替代。

前两者看 AI 自身，后者看传统市场 residual access。

---

## 9. Power 必须同时保留 Physical Quantity 与 Delivery State

约 **120 kW/rack** 可以作为 rack-level power-density input。[^5]

但 system power 计算必须同时保留两个维度：

### Physical Quantity

- kW；
- MW；
- GW。

### Delivery State

- Announced；
- Contracted / Secured；
- Permitted；
- Construction / Transition；
- Energized；
- Utilized。

因此：

> **contracted / secured capacity ≠ energized capacity ≠ utilized AI load**

同时，generation MW/GW、PPA capacity 与 IT-GW 必须保持各自物理身份，不能因为都服务 AI project 就直接相加。

一个正确的 power model 必须同时说明“多少”和“处于什么状态”。

---

## 10. Forward Commitment 是 Supply Reservation Intensity 的 Proxy，而不是 Shipment

NVIDIA manufacturing, supply and capacity commitments 的公开轨迹为：[^6]

- 2026-01-25：**US$95.2B**；
- 2026-04-26：**US$119B**；
- 2026-07-26：**US$279B**。

FY27 Q2 10-Q 说明，最新 commitments 主要涉及 data-center infrastructure systems 所需的 memory 与 manufacturing facilities。

这可以用来观察：

> **future resource reservation intensity**

但不能告诉我们：

- 某一家 supplier 获得多少；
- customer-level HBM bits；
- CoWoS allocation；
- rack shipments。

因此：

> **commitment ≠ shipment**

它是领先指标，而不是实际交付量。

---

## 11. Rolling Bottleneck Cascade：约束会在不同物理层之间迁移

AI infrastructure 没有一个永久固定的唯一瓶颈。

一种扩张链可能是：

> HBM / packaging tight  
> → hardware delivery constrained  
> → supply expands  
> → more systems reach sites  
> → power / interconnection becomes binding  
> → utilization becomes next constraint

反向资本链可能是：

> power delay / low utilization  
> → buyer ROI declines  
> → CapEx slows  
> → hardware orders slow  
> → HBM / packaging tightness eases  
> → upstream CapEx slows

这就是 **Rolling Bottleneck Cascade**。

它说明：

> **一个瓶颈缓解，不代表系统约束消失；约束可能只是转移到了下一层。**

---

## 12. Capital Return 必须把不同现金时钟放进同一经济框架

AI infrastructure 的最基本经济关系可以写成：

> **Economic Return = Revenue from Productive Workload − Depreciation − Power − Operations − Financing**

这里的核心问题是 duration mismatch：

- hardware 技术周期短；
- network / cooling 中周期；
- data-center shell 长周期；
- grid / PPA / generation 更长周期。

因此，一个 system 即使技术上可运行，也可能因为：

- utilization 低；
- workload monetization 弱；
- capital cost 高；
- long-duration obligation 重；

而形成较差资本回报。

---

## 13. Quantitative Guardrails

本报告量化必须遵守以下边界：

- revenue share ≠ wafer share；
- platform revenue share ≠ physical shipment share；
- demand share ≠ allocation share；
- contracted MW ≠ energized MW；
- energized MW ≠ utilized AI load；
- system spec × hypothetical count ≠ actual shipment；
- front-end wafer pool ≠ advanced-packaging wafer pool；
- CapEx guidance ≠ actual CapEx；
- institutional forecast ≠ company actual；
- model compute conversion ≠ full R&D cost；
- exposure ≠ realized outcome。

这些不是文字上的谨慎，而是防止模型在量纲上失真。

---

## 14. 最可靠的量化顺序

本报告采用：

> **official fact → physical identity → denominator → scenario input → supply constraint → utilization → capital return → falsification**

而不是：

> **先设定一个终局 → 再寻找数字填满模型。**

量化框架的价值不是制造伪精确，而是让未来情景可以大胆，同时让事实层、物理量纲和证据身份始终保持可审计。

## References

[^1]: DeepSeek-AI, “DeepSeek-V3 Technical Report,” https://arxiv.org/abs/2412.19437
[^2]: DeepSeek-AI, “DeepSeek-V2,” repository and technical report, https://github.com/deepseek-ai/DeepSeek-V2
[^3]: NVIDIA, “GB200 NVL72,” official product page, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^4]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^5]: NVIDIA, DGX GB200 Hardware Guide, rack power approximately 120 kW, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
[^6]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
