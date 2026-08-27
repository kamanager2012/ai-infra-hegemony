# 第十六卷：AI 基础设施量化框架——Compute、Memory、Packaging 与 Capacity

## 1. 量化的目标不是“算出唯一未来”

AI infrastructure 的量化分析最容易犯的错误，是把不同物理池和不同证据等级的数字连成一个看似精确、实际不可验证的总模型。

本卷只做四类可审计量化：

1. compute / memory intensity；
2. rack-scale material demand；
3. packaging geometry stress test；
4. capacity / commitment indicators。

任何无法由公开数据闭合的环节，都保持为参数，而不是填入虚构点值。

## 2. Roofline：为什么推理经常首先受 memory bandwidth 限制

Roofline model 的基本关系：

```text
Performance
=
minleft(
Peak Compute,;
Memory Bandwidth 	imes Arithmetic Intensity
ight)
```

临界算术强度：

```text
I_{critical}
=
rac{Peak Compute}{Memory Bandwidth}
```

当 workload 的 arithmetic intensity 低于临界值时，系统处于 memory-bound 区域。

自回归推理每一步都需要读取大量 model state 与 KV cache，因此即使 peak FLOPS 很高，实际 token throughput 仍可能由 HBM bandwidth 和 memory movement 限制。

这解释了为什么 frontier inference 的竞争不能只看 FLOPS。

## 3. MLA：算法如何直接改变 memory demand

DeepSeek-V3 技术报告披露：

- 671B total parameters；
- 37B activated parameters；
- 14.8T pre-training tokens；
- 2.788M H800 GPU-hours；
- MLA compressed KV dimension (d_c=512)。

DeepSeek-V2 技术报告则明确给出相对 DeepSeek 67B：

- KV cache reduction：约 **93.3%**
- maximum generation throughput：约 **5.76×**

这两个数字属于不同模型版本，不能混写。

其方法意义是：

> algorithmic architecture 可以直接减少 bytes/token，从而改变同一 HBM capacity 下的并发与 serving cost。

但这不会使 memory bandwidth 失效，只会改变 demand function。

## 4. DeepSeek 的训练成本应该如何理解

DeepSeek-V3 报告给出完整训练约 **2.788M H800 GPU-hours**。

如果按报告侧假设的 **$2/GPU-hour** 进行租金换算：

```text
2.788M 	imes $2 ≈ $5.576M
```

这不是企业完整现金成本。

它不包含：

- research iteration；
- failed runs；
- data collection/cleaning；
- engineering payroll；
- infrastructure depreciation；
- networking；
- storage；
- post-training ecosystem。

因此，这个数字适合用于比较**有效训练计算量级**，不适合直接写成“训练一个 frontier model 只需要 $5.6M”。

## 5. Rack-scale memory demand

GB200 NVL72 官方配置：

- 72 Blackwell GPU
- 36 Grace CPU
- 13.4 TB HBM3E
- 17 TB LPDDR5X

因此：

```text
HBM(R)=13.4 	ext{TB} 	imes R
```

```text
LPDDR(R)=17 	ext{TB} 	imes R
```

其中 (R) 是 rack 数。

| Rack 数 | HBM3E | LPDDR5X |
|---:|---:|---:|
| 1,000 | 13.4 PB | 17 PB |
| 10,000 | 134 PB | 170 PB |
| 30,000 | 402 PB | 510 PB |
| 50,000 | 670 PB | 850 PB |

这些是情景需求，不是 shipment estimate。

## 6. HBM wafer-supply trade ratio

Micron FY24 Q3 prepared remarks：

```text
HBM3E wafer supply
≈
3 	imes DDR5 wafer supply
```

条件是：

- same technology node；
- same number of bits。

因此，若 HBM bit demand 上升，DRAM wafer pressure 会被 trade ratio 放大。

该比率属于 **A 级一手公司证据**，但不能机械外推到所有未来 HBM generation。

## 7. Packaging geometry stress test

报告采用 **5.39 CoWoS wafers/rack** 作为 D 级 geometry stress test。

其几何来源为：

```text
72 	ext{packages}
÷
13.4 	ext{packages/wafer}
≈
5.39 	ext{wafers/rack}
```

其中 13.4 packages/wafer 是几何假设，不是 TSMC 官方 yield。

因此该模型只能用于：

- packaging demand order-of-magnitude；
- scenario comparison；
- bottleneck sensitivity。

不能用于：

- 除 TSMC annual wafer shipments；
- 推导实际 Blackwell shipment；
- 推导 customer allocation。

## 8. 为什么 shipment 在公开数据中无法直接闭合

目前缺少至少三个关键分项：

- actual rack shipments；
- customer-level HBM bits；
- customer-level CoWoS allocation。

因此，从 Data Center revenue 直接反推 rack 数会引入一个未知 system ASP。

再从 rack 数继续推 HBM / CoWoS，则会把一个未知量传播成多个伪精确结果。

正式量化框架因此采用：

> **可观察需求锚 + 情景 rack 数 + 物理 BOM**

而不是“收入÷自拟柜价”。

## 9. Capacity commitment 是更可靠的前向指标

当 shipment 分项缺失时，supply commitment 比自拟出货模型更有价值。

NVIDIA：

- FY26 year-end supply-related commitments：**$95.2B**
- FY27 Q1：**$119.0B**

这类指标反映：

- inventory reservation；
- manufacturing capacity；
- future product supply。

它仍不能告诉我们每一家 supplier 的金额，但可以作为未来资源锁定强度的可观察 proxy。

## 10. AHICR：增量先进产能捕获率

报告引入：

```text
AHICR
=
rac{	ext{某买方获得的新增先进 AI/HPC 资源}}
{	ext{全行业新增先进 AI/HPC 资源}}
```

这里的“资源”可以分别计算：

- advanced logic；
- HBM；
- CoWoS；
- power。

AHICR 不要求把不同单位强行相加，而是分别观察每个 scarce layer 的 incremental capture。

这比历史 revenue share 更适合分析未来资源竞争。

## 11. Quantitative guardrails

全书所有定量模型遵循以下禁区：

- revenue share ≠ wafer share；
- contracted MW ≠ energized MW；
- rack spec × hypothetical racks ≠ shipment；
- CoWoS geometry ≠ fab yield；
- CapEx guidance ≠ actual CapEx；
- AI exposure ≠ job loss；
- model rental conversion ≠ full company cash cost。

## 12. 当前结论

AI infrastructure 可以量化，但必须保持维度一致。

最可靠的分析顺序是：

**official system spec**
→ **material identity**
→ **scenario demand**
→ **supply constraint**
→ **financial commitment**
→ **falsification**

而不是先设一个宏大结论，再反向寻找数字填满它。
