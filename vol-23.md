# 第二十三卷：HBM4、逻辑底座与存储资本密度

## 1. HBM 为什么具有“新石油”式的稀缺属性

把 HBM 称为“AI 时代新石油”只能作为比喻。

真正可分析的机制是：

- high bandwidth density；
- stacking complexity；
- wafer-supply trade ratio；
- packaging dependency；
- generation-specific qualification。

HBM 的战略价值来自难以快速复制的生产能力，而不是因为它与石油具有相同市场结构。

## 2. ~3× 的真正物理含义

Micron FY24 Q3 prepared remarks：

> HBM3E 在相同 technology node、生产相同比特时，约需要 DDR5 **3× wafer supply**。

Micron FY25 10-K 又确认：

> HBM 为生产相同比特需要更多 wafers 与 cleanroom space。

因此，~3× 的核心含义是：

> 同样 bit demand，HBM 会占用更多 manufacturing input。

它并不是：

> 一片 HBM wafer 永远“等于三片 DDR5 wafer”。

这是一个 industry trade ratio，而不是固定 fab accounting rule。

## 3. 为什么 HBM bit share 会低估制造压力

假设 HBM 的 bit share 为 (x)，而同 bit wafer input 高于 conventional DRAM，那么：

[
Manufacturing share > Bit share
]

因此，即使 HBM 在总 DRAM bits 中不是多数，其对：

- wafer；
- cleanroom；
- CapEx；
- packaging

的影响也可能显著高于 bit share。

这解释了为什么 HBM demand 会压缩 conventional DRAM residual capacity。

## 4. HBM4 可能进一步提高资本密度

Micron 已表示 HBM4 的 trade ratio 预计高于 HBM3E。

这意味着 future HBM generation 可能继续增加：

- logic-base complexity；
- stacking；
- packaging；
- wafer input；
- testing。

但具体 HBM4/HBM4E 不同 configuration 的 trade ratio 必须以未来 vendor disclosure 为准。

不能把 HBM3E 的 3× 直接机械改写成 HBM4 4× 或 5×。

## 5. 16-Hi 不能在缺乏正式规格时写成既定事实

HBM generation 可能向更高 stack count 演进，但具体：

- 12-Hi；
- 16-Hi；
- capacity；
- bandwidth；
- yield；
- production timing

必须按 vendor official specification 逐项确认。

因此，本报告不会因为标题或供应链预测出现“16-Hi”，就把它写成所有 HBM4 的统一量产规格。

## 6. Logic base die 会把存储与先进逻辑进一步绑定

HBM 正在从“纯 DRAM stack”向更复杂的逻辑底座整合演进。

这可能产生新的资源竞争：

HBM vendor  
→ logic base die  
→ advanced foundry  
→ advanced packaging。

如果 logic base 使用 leading-edge process，memory 与 compute 会进一步竞争相同 foundry resource。

这会使 HBM 从 memory bottleneck 进一步升级为跨 memory/foundry 的 system bottleneck。

## 7. 三家供应商的结构优势

SK hynix、Samsung、Micron 的优势来自同时拥有：

- DRAM technology；
- TSV/stacking；
- manufacturing scale；
- HBM qualification；
- customer relationship。

这一能力无法通过普通 DRAM capacity 快速复制。

因此，HBM 市场的进入壁垒不仅来自 CapEx，还来自：

- yield learning；
- packaging know-how；
- customer qualification；
- generation timing。

## 8. HBM 的“库存”属性与石油不同

HBM 与 commodity oil 最大的差异是：

- product generation 快；
- 与 specific accelerator generation 绑定；
- qualification cycle 长；
- obsolete risk 高。

因此，HBM 不能像标准 commodity 一样长期无差别库存。

这意味着：

> HBM scarcity 与 generation mismatch 可以同时存在。

即某一代产品过剩，并不自动解决下一代 frontier HBM 的短缺。

## 9. 当前判断

HBM 的战略价值来自三个同时存在的特征：

1. high bandwidth；
2. high wafer-supply trade ratio；
3. high integration/qualification complexity。

未来如果 HBM4/HBM4E 继续提高 capital intensity，memory 可能长期保持 AI system 的核心 scarce layer。

如果新的 memory architecture 或 algorithmic efficiency 显著降低 bandwidth/memory demand，则这一结构可能被打破。

所以 HBM 的长期价值不是“永远短缺”，而是：

> **只要 frontier system 对 bandwidth 的增长快于 memory supply elasticity，HBM 就会继续拥有高战略价值。**
