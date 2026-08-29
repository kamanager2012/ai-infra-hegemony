# Part I · 第6章：Advanced Packaging、CoWoS 与系统交付瓶颈

## 1. 核心判断：Advanced Packaging 已从“后段工序”升级为系统交付层

frontier AI accelerator 越来越依赖 multi-die integration、HBM、large interposer 与 high-speed die-to-die connection。

因此，advanced packaging 不再只是芯片完成前道制造后的配套环节，而是：

> **决定一个 frontier AI system 能否按计划、按数量交付的独立制造层。**

这解释了一个重要现象：

> **leading-edge logic capacity 增加，并不必然等于可交付 AI system capacity 同比例增加。**

如果 HBM integration、interposer、substrate、testing 或 packaging capacity 不足，前道逻辑晶圆已经完成，完整系统仍可能无法按期交付。

---

## 2. TSMC 已经一手确认 Advanced Packaging Tightness

TSMC 的公开表述已经足以确认 advanced-packaging tightness：[^1][^2]

- 2024 Q4：管理层称相关 capacity **very tight**，无法满足全部客户需求；
- 2026 Q2：管理层进一步表示 packaging capacity **so tight that now it limits my customers' growth**。

这使 advanced packaging 从“可能的供应瓶颈”升级为**公司公开确认的 growth constraint**。

收入数据也说明其经济重要性上升，但年份口径必须保持原样：

- 4Q24 transcript：**advanced packaging and testing >8% of revenue**；
- 4Q25 transcript 公司更正口径：**advanced packaging slightly over 10% of 2025 revenue**。[^5]

两者标签不同，因此不能把 >8% → >10% 直接当作严格同口径连续序列。

---

## 3. Tightness 是事实，Customer Allocation 不是公开事实

TSMC 公开资料可以支持：

- advanced packaging 很紧；
- CoWoS 是 AI system delivery 的重要环节；
- packaging tightness 已经限制客户增长。

但公开资料没有给出一张 customer-level CoWoS allocation table。

因此必须区分：

- **A 级事实**：packaging / CoWoS tightness；
- **未公开**：每个客户实际获得多少 CoWoS capacity；
- **机构估计**：不同客户需求占比。

同样，TSMC customer revenue share、wafer revenue share 与 CoWoS demand/allocation share 不能互换。

---

## 4. NVIDIA 高 CoWoS Demand Concentration 有机构证据，但不能升级成官方 Allocation

TrendForce 对 2025 CoWoS demand 的研究将 NVIDIA 列为最大需求客户，并估计其需求占比 **超过 60%**。[^3]

这条信息可以作为 B 级 institutional estimate，用于说明：

> **AI advanced-packaging demand 存在较高客户集中度。**

但它不能被改写成：

- TSMC 官方确认 NVIDIA 获得 >60% allocation；
- >60% 是 2026 actual；
- NVIDIA 对 CoWoS 拥有排他权利。

Demand concentration 与 actual allocation 是两个不同问题。

---

## 5. Packaging Capacity 必须保持为独立 Physical Pool

advanced-packaging capacity 由 packaging flow、interposer / substrate、HBM integration、tool capacity、testing、yield 与 qualification 共同决定，不能与 TSMC front-end wafer capacity 互换。

因此：

- front-end logic wafers 不能除以一个 packaging geometry factor 后直接推导 rack output；
- packaging demand share 不能转换成 customer allocation；
- HBM bits、logic wafers、package starts 与 energized MW 必须保留各自物理身份。

因此，本报告不将多个 scarce layer 压缩成一个“综合产能占有率”。

## 6. 为什么 Packaging 可能比 Node 更早成为“数量闸门”

leading-edge logic 的扩产路径主要围绕：

- fab construction；
- process migration；
- equipment installation；
- yield ramp。

advanced packaging 则同时依赖：

- packaging tools；
- interposer；
- substrate；
- HBM integration；
- testing；
- process flow；
- qualification；
- high-volume yield。

因此，完整 AI system 的交付需要多个环节同时成熟。

这使 advanced packaging 更容易成为一种**数量闸门**：

> **有足够先进逻辑芯片，不代表能在同一时间窗口内组装出足够数量的完整 AI systems。**

所以分析 AI system supply 时，不能把 front-end wafer capacity 与 back-end packaging capacity 放进同一个分母。

---

## 7. Incremental Packaging Access 必须直接测量

前瞻问题不是构造一个跨层 capture ratio，而是竞争 buyer 能否持续获得 qualified advanced-packaging supply。

应直接观察：

- lead time；
- allocation fulfillment；
- delivery stability；
- supplier diversification；
- generation transition；
- integration yield。

只有 packaging layer 自身存在可核验 customer-level allocation 时，才使用该层的份额数据。

因此：

> **packaging access 必须在 packaging 自己的物理池中判断，不能由 foundry revenue share、HBM demand share 或 system revenue 反推。**

## 8. Cloud Custom Silicon 不会自动绕开 Packaging

Google、AWS、Microsoft、Meta 的 custom accelerator system 能够分流 NVIDIA platform profit，但它们自身仍需要：

- advanced logic；
- HBM；
- high-density integration；
- advanced packaging；
- networking；
- power。

因此两个效应可以同时成立：

1. **Platform substitution**：hyperscaler 自研系统降低对 NVIDIA 完整平台的依赖；
2. **Upstream competition**：这些系统继续竞争相同或相近的 scarce manufacturing layers。

所以“更多 custom silicon”不自动等于“CoWoS/HBM pressure 下降”。

---

## 9. Bottleneck Location 不等于 Profit Location

advanced packaging 可以是系统交付瓶颈，但不代表它一定拥有整个价值链最高 margin。

TSMC 2Q24 管理层曾表示，advanced-packaging gross margin 过去显著低于 corporate average，当时正在接近但尚未达到公司平均。[^4]

因此：

> **bottleneck location ≠ profit location**

这是 AI infrastructure 价值链分析中非常重要的区分。

- packaging 可能决定“能不能交付”；
- HBM 可能决定 memory bandwidth 与 system configuration；
- system platform 则可能通过 software、interconnect、integration 与 switching cost 捕获更高 system-level economics。

物理稀缺与利润捕获不能自动画等号。

---

## 10. Packaging 是 China Production-Grade Parallel Stack 的独立 Gate

frontier AI parallel stack 不能只用 logic node 判断。

即使 accelerator die 可以生产，如果以下环节不足：

- advanced packaging；
- substrate；
- HBM integration；
- testing；
- high-volume yield；
- qualification；

仍然无法稳定交付大规模 production system。

因此，“有国产 accelerator”与“形成 production-grade frontier system”不是同一个命题。

在 **Production-Grade Parallel Stack** 层，必须验证 packaging 是否能支撑真实 workload 的规模化交付；在更高一层的 **Autonomous Frontier Closure** 中，还需要继续验证 packaging equipment、materials、service、process upgrade 与跨代 capacity expansion 的 continuity。

这两个层级不能混写。

---

## 11. 当前判断与证伪条件

截至 2026 年 8 月，最稳健的结论是：

- TSMC 已一手确认 advanced-packaging tightness；
- packaging tightness 已成为 customer growth constraint；
- NVIDIA 高 CoWoS demand concentration 有 B 级机构锚；
- customer-level actual allocation 仍未公开；
- cloud custom systems 仍会竞争相同上游资源；
- packaging 是独立于 leading-edge logic 的 frontier-system closure gate。

因此，advanced packaging 当前应被视为 AI infrastructure 的核心 scarce layer 之一。

如果未来出现以下变化，本章判断应下调：

- TSMC 不再把 packaging 描述为增长约束；
- lead time 持续显著缩短；
- capacity expansion 明显快于需求增长；
- customer access 更分散；
- HBM / substrate / packaging integration 的 supply elasticity 显著提高。

## References

[^1]: TSMC, 4Q24 Earnings Conference Transcript, advanced packaging and testing >8% of revenue; capacity “very tight,” https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf
[^2]: TSMC, 2Q26 Earnings Conference Transcript, packaging capacity limiting customer growth, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^3]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^4]: TSMC, 2Q24 Earnings Conference Transcript, advanced-packaging margin relative to corporate average, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2024-08/5122725a56670882d777a8e8bfe0ed247cc55330/TSMC%202Q24%20Transcript.pdf
[^5]: TSMC, 4Q25 Earnings Conference Transcript, corrected 2025 advanced-packaging revenue identity, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
