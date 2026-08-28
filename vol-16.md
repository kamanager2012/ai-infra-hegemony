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
Performance = min(Peak Compute, Memory Bandwidth × Arithmetic Intensity)
```

临界算术强度：

```text
I_critical = Peak Compute / Memory Bandwidth
```

当 workload 的 arithmetic intensity 低于临界值时，系统处于 memory-bound 区域。

自回归推理每一步都需要读取大量 model state 与 KV cache，因此即使 peak FLOPS 很高，实际 token throughput 仍可能由 HBM bandwidth 和 memory movement 限制。

这解释了为什么 frontier inference 的竞争不能只看 FLOPS。

## 3. MLA：算法如何直接改变 memory demand

DeepSeek-V3 Technical Report 披露：

- 671B total parameters；
- 37B activated parameters；
- 14.8T pre-training tokens；
- pre-training compute：**2.664M H800 GPU-hours**；
- full training compute：**2.788M H800 GPU-hours**；
- MLA compressed KV dimension (d_c=512)。

DeepSeek-V2 技术报告则明确给出相对 DeepSeek 67B：

- KV cache reduction：约 **93.3%**
- maximum generation throughput：约 **5.76×**

这两个数字属于不同模型版本，不能混写。

来源：
- DeepSeek-V3：https://arxiv.org/abs/2412.19437
- DeepSeek-V2：https://github.com/deepseek-ai/DeepSeek-V2

其方法意义是：

> algorithmic architecture 可以直接减少 bytes/token，从而改变同一 HBM capacity 下的并发与 serving cost。

但这不会使 memory bandwidth 失效，只会改变 demand function。

## 4. DeepSeek 的训练成本应该如何理解

DeepSeek-V3 报告给出 **full training 2.788M H800 GPU-hours**；其中 **pre-training 为 2.664M H800 GPU-hours**。

如果按论文采用的 **US$2/GPU-hour** 口径对 full-training compute 做租金换算：

```text
2.788M × US$2 ≈ US$5.576M
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

因此，这个数字适合用于比较**formal full-training compute 量级**，不适合直接写成“训练一个 frontier model 只需要 US$5.576M”。

## 5. Rack-scale memory demand

GB200 NVL72 官方配置：

- 72 Blackwell GPU
- 36 Grace CPU
- 13.4 TB HBM3E
- 17 TB LPDDR5X

因此：

```text
HBM(R) = 13.4 TB × R
```

```text
LPDDR(R) = 17 TB × R
```

其中 R 是 rack 数。

| Rack 数 | HBM3E | LPDDR5X |
|---:|---:|---:|
| 1,000 | 13.4 PB | 17 PB |
| 10,000 | 134 PB | 170 PB |
| 30,000 | 402 PB | 510 PB |
| 50,000 | 670 PB | 850 PB |

这些是情景需求，不是 shipment estimate。

## 6. HBM wafer-supply trade ratio

Micron FY24 Q3 prepared remarks 披露，**industry-wide**，HBM3E 在 same technology node、生产 same number of bits 时约需要 DDR5 **3× wafer supply**。

因此，若 HBM bit demand 上升，DRAM wafer pressure 会被 trade ratio 放大。

该比率属于 **A 级一手公司披露的 industry-wide estimate / observation**，不是 Micron 单厂固定制造常数，也不能机械外推到所有未来 HBM generation。

公开来源：https://investors.micron.com/static-files/4550f98c-1054-4847-a929-c17d520a0564

## 7. Packaging geometry stress test

报告采用 **约 5.37 CoWoS wafers/rack** 作为 D 级 geometry stress test。

其几何来源为：

```text
72 packages ÷ 13.4 packages/wafer ≈ 5.373 wafers/rack
```

取两位小数为 **5.37**。

其中 **13.4 packages/wafer 是报告几何工作假设**，不是 TSMC 官方 yield、官方 packages-per-wafer 指标，也不是一手历史事实。

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

NVIDIA manufacturing, supply, and capacity commitments：

- 2026-01-25：**US$95.2B**
- 2026-04-26：**US$119B**
- 2026-07-26：**US$279B**

Q2 10-Q 说明，US$279B 主要对应 data-center infrastructure systems 所需的 memory 和 manufacturing facilities，用于 current / future architectures 的长期需求。来源：https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

这类指标反映：

- inventory reservation；
- manufacturing capacity；
- future product supply。

它仍不能告诉我们每一家 supplier 的金额，但可以作为未来资源锁定强度的可观察 proxy。

## 10. AHICR：增量先进产能捕获率

```text
AHICR = 某买方获得的新增先进 AI/HPC 资源
        / 全行业新增先进 AI/HPC 资源
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

## 本卷关键公开来源

- DeepSeek-V3 Technical Report（pre-training 2.664M；full training 2.788M H800 GPU-hours）：https://arxiv.org/abs/2412.19437
- DeepSeek-V2（93.3% KV-cache reduction；5.76× maximum generation throughput，relative to DeepSeek 67B）：https://github.com/deepseek-ai/DeepSeek-V2
- NVIDIA GB200 NVL72 product page（72 GPU、36 Grace、13.4 TB HBM3E、17 TB LPDDR5X）：https://www.nvidia.com/en-us/data-center/gb200-nvl72/
- Micron FY24 Q3 event page：https://investors.micron.com/events/event-details/microns-third-quarter-2024-financial-call
- Micron FY24 Q3 prepared remarks（industry-wide HBM3E ≈ 3× DDR5 wafer supply at same node / same bits）：https://investors.micron.com/static-files/4550f98c-1054-4847-a929-c17d520a0564
- NVIDIA FY26 10-K（2026-01-25 supply/capacity commitments baseline）：https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
- NVIDIA FY27 Q2 10-Q（US$279B commitments）：https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
