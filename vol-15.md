# 第十五卷：2036 年 AI 基础设施终局——系统栈、资源与权力结构

## 1. 2036 不是一个数字预测点

本卷不预测 2036 年某家公司拥有多少市场份额，也不使用固定概率。

它回答的是：

> 如果今天已经观察到的 system-stack competition、HBM/packaging bottleneck、cloud CapEx、power constraint 和 China parallel stack 持续演化，2036 年产业结构可能呈现什么形态？

第十卷定义 S1–S4 四类标准情景，具体输入变量见 [《核心假设矩阵》](核心假设矩阵.md)。

本卷进一步分析每种情景下的**产业结构**。

## 2. 2036 的竞争单位仍然会是系统，而不是单芯片

无论哪种情景成立，frontier AI 的竞争对象都已经不太可能退回“谁有最好的一颗芯片”。

系统栈至少包括：

- logic；
- HBM；
- packaging；
- interconnect；
- software；
- rack/pod；
- data center；
- power。

2036 年最重要的问题是：

> 这些层是被少数平台高度协调，还是由多套可互操作系统共同提供？

## 3. S1 下的 2036：多系统栈共存

如果 Competitive Expansion 成立：

- NVIDIA 仍是主要平台之一；
- Google/AWS/Microsoft/Meta 自研栈成熟；
- open compiler/runtime 降低 migration cost；
- advanced packaging 与 HBM 供给显著扩大；
- 多家供应商可获得 leading-edge capacity；
- China parallel stack 完整度提高。

产业结构更像：

> 多个大型 system platform + 高度专业化上游制造网络。

价值捕获会从单一平台向 cloud、software 和 specialized supplier 更分散。

## 4. S2 下的 2036：高集中但持续竞争

如果 Baseline Concentration 延续：

- NVIDIA 保持领先通用 AI system platform；
- cloud custom silicon 在内部 workload 占比持续提升；
- HBM/packaging 仍周期性紧张；
- power 成为大型 data-center 项目的核心资源；
- China 形成强平行体系，但全球仍存在显著技术与生态分层。

这种格局不是“单一垄断”，而是：

> 少数大型 system stack + 少数核心 scarce-layer supplier。

这是当前最自然的长期延伸路径。

## 5. S3 下的 2036：资源霸权

如果 Resource Hegemony 成立，关键不是一家公司的 chip share，而是多个稀缺层被高度集中协调。

典型结构：

- leading-edge capacity 集中；
- HBM supply 集中；
- packaging 长期 tight；
- high-speed interconnect 强锁定；
- software switching cost 高；
- powered land / firm MW 被提前锁定。

此时后来者面对的不是“做出一颗更快芯片”，而是需要复制完整 infrastructure stack。

这会形成极高的资本进入门槛。

## 6. S4 下的 2036：资本清算后的基础设施公用化

如果 Capital Hard Landing 出现：

- oversupplied compute 被压价；
- hardware residual value 下跌；
- model/application margin 继续压缩；
- hyperscaler 减少下一轮 expansion；
- power/data-center 长资产面临低利用率。

但这不意味着 AI 消失。

更可能出现：

> 已建算力成为低价基础设施，行业从“建设竞赛”转向“利用率和应用现金流竞赛”。

类似历史上的 fiber、cloud、telecom infrastructure，资本清算之后仍可能形成更大规模使用。

## 7. Memory 在 2036 仍可能是关键分水岭

Micron 的 HBM3E ~3× wafer-supply trade ratio 表明，memory scaling 并不是免费的。

Micron 已披露 HBM4 的 trade ratio 预计高于 HBM3E；**HBM5 尚无本报告可核的一手 trade-ratio 披露**。因此，只能把“后续世代若继续提高 trade ratio”作为条件情景，不能把 HBM4 的方向直接外推成 HBM5 事实。

如果新 memory architecture、3D integration 或 algorithmic efficiency 显著降低 bandwidth requirement，则这一瓶颈可能弱化。

因此，2036 年的 AI stack 不一定由 transistor node 主导，memory wall 可能比 logic node 更关键。

## 8. Packaging 可能从“制造配套”变成独立战略层

随着 chiplet、large interposer、3D integration 与 optical/interconnect 发展，advanced packaging 的战略价值可能继续上升。

未来系统性能越来越可能由：

- die-to-die bandwidth；
- HBM integration；
- thermal design；
- package yield；
- system topology

决定。

因此，2036 年的 semiconductor competition 很可能不再适合用“node leadership”单独描述。

## 9. Power 会决定 AI 地理

如果 rack/pod power 继续上升，AI infrastructure 的地理分布将越来越受：

- firm generation；
- grid；
- water/cooling；
- permit；
- political acceptance

影响。

因此，未来的“AI hub”更可能出现在拥有：

> compute supply + power + land + regulatory execution

组合优势的地区。

这会让 energy geography 进入 technology competition。

## 10. China parallel stack 的长期作用

2036 年中国是否形成完整 parallel frontier stack，将决定全球产业是：

- 单一全球 system ecosystem；
- 两大相对独立 system ecosystem；
- 多区域主权 AI stack。

真正需要观察的不是国产化比例总数，而是：

- advanced logic scale；
- HBM scale；
- packaging scale；
- interconnect；
- software migration；
- frontier workload。

如果这些层闭环，全球 AI infrastructure 将形成长期双重或多重资源重力中心。

## 11. 产业终局的真正分水岭

到 2036 年，行业最关键的四个问题可能是：

1. **system stack 是否可互操作？**
2. **scarce manufacturing 是否足够多元？**
3. **power 是否成为长期配额？**
4. **AI workload 是否能够产生足够现金流覆盖基础设施？**

这四个问题比“谁拥有 80% 市占率”更能解释长期产业结构。

## 12. 当前结论

从 2026 年向 2036 年外推，最合理的基准不是永久垄断，也不是算力迅速商品化，而是：

> **高资本、高集中、多系统栈竞争长期并存。**

领先平台会继续争夺 system definition；cloud 会持续内部化更多 stack；上游制造与 power 会保持战略价值；中国 parallel stack 会逐步扩大。

真正决定终局的，是这些力量谁先跨过临界点。

因此，2036 年不是本报告的“答案”，而是检验当前机制是否持续成立的远期截面。

## 本卷关键公开来源

- Micron FY24 Q3 Prepared Remarks（HBM3E ≈ 3× DDR5 wafer supply）： https://investors.micron.com/static-files/4550f98c-1054-4847-a929-c17d520a0564
