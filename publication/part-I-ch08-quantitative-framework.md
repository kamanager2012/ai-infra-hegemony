# Part I · 第8章：Quantitative Framework——什么可以量化，什么不能，以及为什么

## 1. Quantification 必须从 Denominator Closure 开始

量化的第一问不是“数字是多少”，而是：**这个数字是否具备可审计的存在条件。**

只有 numerator、denominator、physical unit、delivery window、qualification boundary 与 evidence identity 能够一致闭合，point estimate 才有资格进入主链。front-end wafer、HBM bits、package starts、energized MW、accounting CapEx 与 seller commitments 不能被拼成一个 synthetic total。

因此，本报告只允许四类量化进入主链：

1. **compute / memory intensity**；
2. **rack-scale material / power intensity**；
3. **layer-specific stress test**；
4. **capacity / commitment / utilization indicator**。

如果公开 denominator 不能闭合，变量就保留为 parameter 或 proxy。**不会为了让模型“看起来完整”而用一个 point estimate 填空。**

---

## 2. Peak FLOPS 不是 Workload Denominator

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

## 3. Efficiency 改变 Demand Function，不改变 Measurement Standard

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

## 4. Training-Run Arithmetic 只是有边界的 Cost Conversion

DeepSeek-V3 Technical Report 披露 full formal training 使用 **2.788M H800 GPU-hours**，并使用 **US$2/GPU-hour** 的租赁成本假设。[^1]

因此可以得到一个明确标记为 **D 级算术换算**的结果：

> **2.788M × US$2 ≈ US$5.576M**

这个数字只代表 formal-training compute conversion，不包含 research iteration、failed runs、data engineering、engineering payroll、cluster depreciation、networking、storage 与 post-training ecosystem。

因此，US$5.576M 可以作为公开训练运行规模的量化锚，但不能写成“一个 frontier model 的完整公司研发成本”。

---

## 5. System Spec 可以支持 Intensity Analysis，不能反推 Deployment

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

## 6. HBM：Bits 与 Wafer Input 是两个 Denominator

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

## 7. Advanced Packaging 必须使用独立 Physical Denominator

advanced-packaging 分析应优先使用可观察或有来源边界的变量，例如：

- qualified capacity；
- lead time；
- allocation fulfillment；
- package starts；
- supplier guidance。

本报告不使用合成的“CoWoS wafers per rack”系数反推实际 shipment。

front-end wafers、back-end packaging capacity、HBM bits 与 energized MW 属于不同 physical pools，必须保持量纲分离。

---

## 8. Absolute Capacity Gap：Current Balance

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

## 9. Capacity Growth Gap：Direction of Travel

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

## 10. Non-AI Residual Capacity 回答的是另一个问题

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

## 11. Power 必须同时保留 Physical Quantity 与 Delivery State

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

### Table 8.1 — NVL72 Rack-to-MW D 级强度换算

| 项目 | 官方 / 已知输入 | 1 MW rack IT load 的机械换算 |
|---|---:|---:|
| Rack power | ≈120 kW / rack | ≈8.33 racks |
| GPU | 72 / rack | ≈600 GPUs |
| HBM3E | 13.4 TB / rack | ≈111.7 TB |
| LPDDR5X | 17 TB / rack | ≈141.7 TB |

**Source:** NVIDIA GB200 NVL72 official specification and DGX GB200 Hardware Guide.[^3][^5]  
**Note:** 该表是 **D 级机械强度换算**，仅回答“如果 1 MW IT rack load 全部由该 rack configuration 构成，物料强度是多少”。它**不是 shipment、deployment、energized-facility capacity 或全行业需求估计**，且不包含 PUE、network/storage、power-conversion、redundancy 与 facility overhead。

这类换算的价值在于把 system spec 变成可审计的 engineering intensity，同时保留“spec ≠ deployment”的边界。

---

## 12. Shipment 不可观察时，使用有边界的 Forward Indicator

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

## 13. Scarce-Capacity Access 必须 Layer-Specific

本报告不把 advanced logic、HBM、advanced packaging、networking 与 power 压缩成一个综合“capture ratio”。

每个 physical layer 分别观察：

- qualified supplier count；
- lead time；
- allocation fulfillment；
- long-term agreements / prepayments；
- delivery timing；
- buyer credit quality；
- supply elasticity。

只有当某一具体 physical pool 的 customer-level allocation 可观察时，才使用可审计的百分比。

### Table 8.2 — 2026 Public-Data Quantification Readiness by Layer

| Physical layer | 当前公开可观察输入 | Absolute Gap 能否闭合 | 2026 更可靠的输出 |
|---|---|---|---|
| Advanced logic | node / platform revenue mix、CapEx、supplier guidance、部分 roadmap | **不能**：缺 customer-level qualified wafer demand / allocation | direction、access proxy、node mix；不造 wafer-share gap |
| HBM / DRAM | vendor supply guidance、same-bits wafer trade ratio、institutional bit forecast | **部分可量化，不能闭合全球 gap**：缺 customer-level bits / wafer allocation | manufacturing intensity、tightness、product-mix shift |
| Advanced packaging | supplier guidance、tightness statement、部分 institutional demand estimate | **不能**：缺统一 qualified package-start denominator 与 customer allocation | lead time、qualification、allocation proxy |
| Networking | system spec、公开 topology / deployment、vendor product data | **部分**：缺统一 workload-level topology / utilization denominator | workload-specific bandwidth / latency / TCO |
| Power / LPS | project-level contracted / secured / permitted / construction / energized states | **项目级部分可闭合，全球不能** | Time-to-Power、state conversion、project delivery gap |
| Capital / Utilization | CapEx、supply commitments、financing structure、部分 revenue disclosure | **资本基数可观察，真实 utilization 不完全公开** | capital-base growth vs utilization / monetization proxy |

**Source:** 本报告根据公开证据可闭合程度整理。  
**Note:** “不能闭合”不是数据空白的借口，而是明确指出**缺失的分母是什么**。未来只有当 demand 与 capacity 在同一 physical unit、delivery window 与 qualification boundary 下同时可观察时，才把该层升级为可审计的 Absolute Gap。

这张表给出 Ch08 的量化边界：

> **能算的，明确计算；只能部分闭合的，明确 proxy；分母缺失的，不用 point estimate 填空。**

---

## 14. 先拆开 Risk Class，再判断 Cascade

AI infrastructure 的 system risk 至少分成五类：

1. **Physical bottleneck：** logic / HBM / packaging / interconnect；
2. **Power bottleneck：** grid / substation / permit / cooling；
3. **Capital / utilization risk：** asset utilization 无法覆盖 depreciation、power、operations 与 financing；
4. **System-substitution risk：** cloud custom stacks / open software 改变 platform economics；
5. **Regulatory / geopolitical risk：** export controls、supply interruption、interface remedies 与 regional fragmentation。

单一风险不等于全行业危机。更危险的状态是多个时钟开始相互强化。

---

## 15. Rolling Bottleneck Cascade 是 State-Transition Model

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

## 16. Capital Return 必须统一不同 Asset Clock

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

## 17. False-Precision Guardrails

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

## 18. Preferred Quantitative Workflow

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
