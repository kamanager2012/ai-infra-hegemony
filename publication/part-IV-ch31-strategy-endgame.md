# Part IV · 第31章：2036 终局与战略选择

## 1. 2036 不是一个市场份额预测点

本书不预测 2036 年某家公司拥有多少市场份额，也不赋固定情景概率。2036 的作用是把当前机制拉到更长时间尺度，观察哪些变量如果持续成立，会把产业带向不同结构。

竞争单位已经从单颗芯片上移到 system stack。frontier AI system 同时依赖 advanced logic、HBM、advanced packaging、interconnect、compiler/runtime、rack/pod、data center、power、capital 与可持续 workload demand。

因此，2036 真正的问题不是“谁有最好的一颗芯片”，而是：

> **这些层最终由少数平台高度协调，还是由多套可互操作系统共同提供？**

## 2. 本章使用的事实锚与对应章节

**Table 31.1 — 长期战略判断所依赖的核心结构变量**

| 结构变量 | 对应章节 |
|---|---|
| NVIDIA system stack / switching cost | [Part I · Ch02](part-I-ch02-nvidia-system-stack.md) |
| HBM / memory resource intensity | [Part I · Ch05](part-I-ch05-hbm-memory.md) |
| Advanced Packaging / CoWoS | [Part I · Ch06](part-I-ch06-advanced-packaging.md) |
| Power / Time-to-Power | [Part I · Ch07](part-I-ch07-power-constraint.md) |
| Hyperscaler second system stack | [Part II · Ch12](part-II-ch12-hyperscaler-system-stack.md) |
| China frontier-system closure | [Part II · Ch17](part-II-ch17-china-parallel-stack.md) |
| Value Capture Map | [Part III · Ch20](part-III-ch20-value-capture-map.md) |
| Capital clearing / S4 signals | [Part III · Ch24](part-III-ch24-capital-clearing.md) |

**Source:** 本报告章节体系。  
**Note:** 本章只承接前文章节已经建立的事实与机制，不重复复制高影响数据表。

终局章不复制这些章节的财务表和物理公式，只使用已经建立的变量进行情景与行动分析。

## 3. S1 — Competitive Expansion：多系统栈共存

如果 advanced manufacturing、HBM、packaging 与 power 供给弹性提高，同时 cloud custom systems、open compiler/runtime 和 interoperability 显著降低迁移成本，产业会更接近 S1。

可能的结构是：

- NVIDIA 仍是主要通用平台之一；
- Google/AWS/Microsoft/Meta system stacks 在大量 workload 中成熟；
- 多家买方能稳定获得 leading-edge manufacturing；
- open software / interfaces 降低跨栈迁移摩擦；
- China parallel stack 的 system closure 提高；
- value capture 从单一 dominant platform 向 cloud、specialized supplier 与 application/workflow 更分散。

S1 不是“所有硬件商品化”，而是**替代路径足够真实，买方拥有可执行选择权**。

## 4. S2 — Baseline Concentration：高集中与持续竞争并存

S2 的结构是：少数大型 system platform 和 scarce-layer supplier 保持强 value capture，同时 cloud custom silicon、中国平行栈和开放软件持续形成竞争压力。

这意味着：

- 通用 frontier workload 仍高度依赖成熟 system platform；
- cloud 自研在内部 workload 持续扩大；
- HBM / packaging / power 仍周期性形成物理约束；
- buyer 会主动保留第二系统，但不会立即放弃主栈；
- 上游资源分配仍受长期订单、现金流、roadmap certainty 和客户多元化共同影响。

截至 2026 年 8 月，本报告把 S2 作为最接近当前事实组合的**基准状态**，不是不可改变的十年预测。[^1][^2][^3]

## 5. S3 — Resource Hegemony：真正的门槛是复制整套基础设施

S3 不要求某家公司拥有一个夸张的单点市场份额。它的核心是多个 scarce layer 同时高度集中：

- leading-edge capacity；
- HBM；
- advanced packaging；
- scale-up / software interfaces；
- powered land / firm MW；
- long-duration supply commitments。

在这种状态下，后来者面对的不是“设计出更快 accelerator”，而是需要同时复制 manufacturing、memory、packaging、software、power 与 customer migration path。

资本进入门槛会显著上升，Non-AI Residual Capacity 也更容易受到挤压。

## 6. S4 — Capital Hard Landing：资本清算不等于 AI 消失

如果 utilization、effective revenue、market-clearing price 和 forward commitments 同步恶化，产业会进入 S4。

此时可能出现：

- hardware residual value 下跌；
- next-generation orders 放缓；
- hyperscaler / model-company commitments 改期；
- data-center / power 长资产面临低利用率；
- model/application margin 继续压缩；
- 过剩 compute 的使用价格显著下降。

但资本清算与技术扩散可以同时发生。历史上的 fiber、telecom 与 cloud 都显示：**overbuild → asset-price decline → cheaper access → new applications** 是一种可能路径。

所以 S4 的长期结果未必是“AI 失败”，也可能是从建设竞赛转向利用率、workflow 和现金流竞赛。

## 7. 2036 的四个真正分水岭

到更长期，以下四个问题比任何单一市场份额更重要：

1. **System stacks 是否可互操作？**
2. **Scarce manufacturing / memory / packaging 是否足够多元？**
3. **Power / powered land 是否长期成为配额？**
4. **AI workload 是否产生足够现金流覆盖基础设施与资本成本？**

它们分别决定 switching cost、supply elasticity、deployment geography 和资本可持续性。

## 8. 企业：先证明 Workflow Economics，再锁长期 Compute

企业部署 AI 的顺序应当是：

1. 找到可量化的真实 workflow；
2. 建立 evaluation / verification；
3. 计算 cost per completed task 与业务价值；
4. 保留 model / cloud / data portability；
5. 根据需求确定性再决定长期 compute commitment。

高确定性的 workload 可以使用较长期 reservation；不确定的实验和快速变化模型则应保留 flexible / multi-provider 路径。

最危险的顺序是先锁大量长期 capacity，再寻找足以填满它的业务场景。

## 9. 企业：主栈可以集中，但第二路径必须可执行

portability 不意味着所有供应商平均采购。更有效的策略是：

> **主栈追求效率，第二路径追求可执行性。**

至少要保留：

- model portability；
- data portability；
- cloud portability；
- accelerator / runtime optionality；
- open interface；
- workload benchmark 与 cost observability。

第二路径的价值在于降低供应、价格、政策和迁移的单点风险。

## 10. 资本：先区分资产类型，再谈“AI 估值”

至少要把四类资产分开：

**Table 31.2 — AI 相关资产的主要价值来源与风险**

| 资产 | 主要价值 | 主要风险 |
|---|---|---|
| Platform | switching cost / system definition / ecosystem | substitution / regulation |
| Manufacturing | scarcity / yield / technology / capacity | cycle / CapEx / utilization |
| Infrastructure | powered land / grid / data center / duration | utilization / duration mismatch |
| Application | workflow / distribution / data | commoditization / unit economics |

**Source:** 本报告 Value Capture / Duration framework。  
**Note:** 分类用于战略分析，不构成证券估值、评级或投资建议。

高 CapEx 既可能是进入壁垒和增长准备，也可能是未来 depreciation 与 stranded asset。资本判断必须同时看 CapEx、utilization、revenue、FCF、forward commitments 与 clearing price。

## 11. 资本：最危险的不是高估值，而是 Duration Mismatch

短周期 compute demand 如果匹配 long-duration debt、PPA、data-center shells 与 transmission assets，一旦 workload 不及预期，清算会比硬件库存慢得多。

因此，资本配置的核心问题是：

> **demand duration 是否与 asset duration 匹配？**

高需求情景下，长资产是 moat；S4 下，同一资产可能成为长期负担。

## 12. 国家：竞争单位已经不是一座 Fab

完整 frontier AI industrial capability 至少需要：

- equipment / materials；
- advanced logic；
- HBM；
- advanced packaging；
- interconnect；
- compiler/runtime；
- data center；
- power / grid；
- talent / production operations。

因此，单纯补贴先进 fab 无法形成 system closure。制造、memory、packaging、software 与 power 必须在同一产业政策框架中。

## 13. 国家：Power Policy 已经是 Compute Policy

高功率 rack 将 grid planning、generation、interconnection、substation、cooling 和 permit 拉进技术竞争。

如果 chip supply 增长而 time-to-power 不改善，就会形成“有 hardware、无法按期上电”的资产错配。

国家层面的 AI infrastructure strategy 因而需要同时管理：

> **semiconductor clock + power-permitting clock + capital clock**。

## 14. 国家：Interoperability 是战略选择权

系统韧性并不要求拒绝领先平台，而要求避免所有关键层同时依赖一个不可替代入口。

长期应提高：

- open compiler/runtime；
- portable model / data formats；
- interoperable networking；
- multi-architecture engineering education；
- cross-stack production benchmarking。

其目标不是人为平均市场份额，而是让替代路径在供应中断、政策变化或价格失衡时真正可执行。

## 15. 中国：长期关键不是“国产化率”，而是 Frontier System Closure

China parallel stack 是否改变全球资源结构，不取决于一个总国产化率，而取决于 advanced logic、HBM、packaging、interconnect、compiler/runtime、frontier workload 与 power 是否同时达到可验证规模。

smartphone / consumer supply success 不能直接证明 frontier AI closure；同样，frontier AI 的高级约束也不能否定中国在消费、制造与国内 workload 上已经存在的大规模产业基础。

如果七个 closure gate 逐步跨越，中国将形成第二个更强的资源重力中心；如果多个关键 advanced layer 长期未闭环，则 parallel stack 的价值更多体现为 domestic resilience 和部分 workload substitution。

## 16. 个人：长期价值来自对结果负责，而不是绑定某一个工具

当模型、IDE、agent 与生成工具快速商品化，最脆弱的个人定位是把职业价值完全绑定到某一个具体工具的操作方法。

更耐久的能力包括：

- domain knowledge；
- problem decomposition；
- workflow / system design；
- verification；
- cross-stack portability；
- 对结果、风险和质量负责的能力。

工具降低执行门槛后，能够定义问题、验证结果和承担交付责任的能力反而更重要。

## 17. 监测框架：什么会让我们改判

未来不靠“十年后必然如此”维持观点，而靠公开信号持续校准：

- NVIDIA / major system seller commitments 是否持续扩大或开始收缩；
- cloud custom stacks 的 production workload share 与迁移成本；
- HBM / advanced-packaging tightness 是否显著缓解；
- leading-edge capacity 是否更分散；
- energized MW / time-to-power 是否改善；
- Anchor Compute Buyer commitments 是否兑现；
- hyperscaler utilization / AI monetization 是否覆盖资本基数；
- China frontier-system closure gates 是否出现一手规模化证据；
- regulation 是否真正降低 interface / tying / switching barriers。

如果供给弹性和 interoperability 同时提高，权重向 S1 移动；如果 multiple scarce layers 与 switching cost 同时强化，向 S3 移动；如果 utilization、clearing price、CapEx 与 commitments 同步转弱，向 S4 移动。

## 18. 最终战略判断

截至 2026 年 8 月，本报告最合理的总体描述是：

> **AI infrastructure 仍处于高速扩张与高集中并存阶段，竞争单位正在从单颗芯片上移到完整 system stack 与基础设施。**

这不是“永久垄断”判断，也不是“算力迅速商品化”判断。它意味着未来十年的竞争会围绕 system substitution、scarce-layer supply、Anchor Buyer demand、power、utilization、capital duration 与 regulation 反复重新分配。

对所有主体，最重要的共同策略可以压缩成一句：

> **不要押注一个不可改变的终局；建立能够在终局改变时仍然可执行的选择权。**

## References

[^1]: NVIDIA, FY27 Q2 official results, current system-platform economics, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^2]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging supply constraint, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^3]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html

## 交叉引用

- [核心证据台账](../核心证据台账.md)
- [核心参考文献索引](../核心参考文献索引.md)
- [Part I · Ch02 NVIDIA System Stack](part-I-ch02-nvidia-system-stack.md)
- [Part I · Ch05 HBM](part-I-ch05-hbm-memory.md)
- [Part I · Ch06 Advanced Packaging](part-I-ch06-advanced-packaging.md)
- [Part I · Ch07 Power](part-I-ch07-power-constraint.md)
- [Part II · Ch12 Hyperscaler System Stack](part-II-ch12-hyperscaler-system-stack.md)
- [Part II · Ch17 China Parallel Stack](part-II-ch17-china-parallel-stack.md)
- [Part III · Ch20 Value Capture Map](part-III-ch20-value-capture-map.md)
- [Part III · Ch24 Capital Clearing](part-III-ch24-capital-clearing.md)