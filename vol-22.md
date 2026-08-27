# 第二十二卷：消费电子冲击模型——DRAM 残量、PC 与 Smartphone 成本传导

## 1. AI 对消费电子的影响首先来自 memory residual

消费电子并不直接采购 frontier training rack，但会与 AI/server demand 共享部分：

- DRAM wafer；
- leading-edge logic；
- power-management component；
- selected packaging。

因此，AI infrastructure 对 consumer electronics 的主要传导路径之一是：

> HBM / RDIMM demand 上升 → conventional DRAM residual supply 改变 → PC / smartphone memory cost 变化。

## 2. 结构性冲击与周期性涨价要分开

如果 AI demand 下降、memory vendor 将产能重新转回 conventional DRAM，则 consumer price pressure 可能回落。

如果 HBM/RDIMM 长期保持高利润且继续占用更多 wafer input，则 consumer residual supply 可能持续偏紧。

因此，关键不是某一季度内存涨价，而是：

- product mix；
- CapEx allocation；
- wafer-supply trade ratio；
- contract duration。

## 3. HBM 对 residual supply 的放大效应

Micron FY24 Q3 prepared remarks：

> HBM3E 在相同 node、相同比特下约需要 DDR5 **3× wafer supply**。

TrendForce：

> HBM + RDIMM 约占 2026 DRAM bits **51%**。

两个数字结合意味着：

HBM 对 DRAM manufacturing input 的影响，高于单纯 bit share 所显示的比例。

因此，consumer DRAM residual capacity 可能受到更强挤压。

## 4. PC：双重传导

PC 受到两条主要路径影响。

### 4.1 GPU allocation

consumer GPU 与 Data Center accelerator 会共享部分 advanced manufacturing resource。

NVIDIA 曾披露 gaming GPU supply constraints。

### 4.2 DDR5 supply

PC 使用 DDR5/LPDDR。

如果 server/HBM demand 吸收更多 wafer/capacity，PC memory cost 更容易上升。

因此，PC 的压力更可能表现为：

- high-end GPU availability；
- memory price；
- configuration adjustment；
- longer replacement cycle。

## 5. Smartphone：仍是巨大市场，不是被 AI 消灭

TSMC 2025 smartphone platform：

- revenue share：**29%**
-同比仍增长。

因此，AI 并没有“挤掉 smartphone”。

真正发生的是：

- HPC growth 更快；
- advanced capacity 增量更偏向 AI/HPC；
- memory supply 更受 server/HBM 影响。

这可能导致 flagship smartphone：

- SoC cost 上升；
- memory configuration 成本提高；
- price tier 分化。

但在缺乏公开采购合同的情况下，不应把分析师 SoC 报价直接扩展成整个 smartphone BOM inflation。

## 6. Channel price 只能作为温度计

channel DRAM/SSD price 可以反映 consumer residual pressure。

但它不能等同于：

- vendor contract price；
- global ASP；
- long-term supply agreement。

因此，本报告把 channel data 作为 C 级 evidence 使用。

它能说明“终端正在感受到价格”，但不能反推 memory vendor 的完整定价结构。

## 7. China supply 对 consumer market 的缓冲作用

中国在：

- LPDDR；
- DDR；
- NAND；
- smartphone supply chain

上的本地能力提高，可以缓解国内部分 consumer product 的供给压力。

但这种作用不能直接扩展到 HBM-class memory。

因此：

- China consumer supply 可以减轻部分本地 residual pressure；
- 不能直接改变全球 frontier AI HBM allocation。

## 8. Automotive 与 consumer electronics 不应混为一类

Automotive 具有更长 qualification cycle。

其 memory、logic 和 power-management demand 与 smartphone/PC 不完全一致。

因此，汽车更可能表现为：

- selected component price pressure；
- advanced compute adoption cost；
- qualification delay。

而不是与 PC 同步出现相同供给冲击。

## 9. 量化边界

当前可以量化：

- HBM ~3× wafer-supply trade ratio；
- HBM+RDIMM 51% DRAM bits；
- rack-scale HBM demand scenarios；
- TSMC platform revenue mix。

当前不宜直接量化：

- 某 smartphone BOM inflation；
- 某品牌采购合同；
- 某 SoC 的真实大客户价格；
- 全行业 replacement cycle 因 AI 延长多少个月。

## 10. 当前判断

消费电子正在承担 AI infrastructure 的 residual-capacity pressure，但影响具有明显层级。

最有证据支持的是：

- memory；
- consumer GPU；
- leading-edge allocation。

因此，正式结论是：

> **AI infrastructure 正在通过共享的 scarce manufacturing layers，把部分成本压力传导到 PC、smartphone 和其他非 AI 终端。**

这不是“消费电子被 AI 消灭”，而是产品升级速度、配置和成本结构受到新的上游资源竞争影响。
