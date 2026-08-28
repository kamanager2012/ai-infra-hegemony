# 第五卷：HBM、存储战争与 AI 供应链重构

## 1. HBM 已从配件变成系统级瓶颈

在 frontier AI system 中，HBM 不再只是 GPU 附属存储，而是决定模型规模、batch、context、并发和系统利用率的核心资源。

GB200 NVL72 官方配置中，单柜包含 **13.4 TB HBM3E**。当采购单位上移到 rack scale，HBM 需求也从“每颗芯片多少 GB”上移到“每个数据中心需要多少 PB”。

这使 HBM 同时影响：

- GPU system performance；
- memory vendor product mix；
- DRAM wafer allocation；
- advanced packaging；
- conventional DRAM residual supply。

## 2. Micron 的约 3× 是一手物理锚

Micron FY24 Q2 prepared remarks 明确披露：

> industry-wide，HBM3E 在相同 technology node、生产相同比特时，约需要 DDR5 **3× 的 wafer supply**。

Micron FY25 10-K 又确认，HBM 为生产相同比特需要更多 wafers 和 cleanroom space。

因此：

- **约 3× = A 级公司一手证据**
- 它描述 HBM3E 相对 DDR5 的 wafer-supply trade ratio
- 它不是每座 fab 固定不变的 manufacturing constant
- 不能机械外推到所有 HBM generation

Micron 同时表示 HBM4 的 trade ratio 预计进一步上升，这意味着未来 HBM 对 DRAM wafer allocation 的影响可能继续加强。

## 3. SK hynix：HBM 已经改变利润结构

SK hynix FY25 官方数据：

- Revenue：**KRW 97.1467T**
- Operating profit：**KRW 47.2063T**
- Operating margin：**49%**
- Net income：**KRW 42.9479T**
- HBM revenue：同比超过一倍

来源：https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/  
中央来源锚见[核心参考文献索引](核心参考文献索引.md)。

这一组数据说明，HBM 需求已经不仅改变产品结构，也显著改变存储厂盈利结构。

与此同时，SK hynix 仍披露 conventional server memory demand 强劲。这意味着 HBM 与 DDR5/RDIMM 并不是两条完全独立的供给链，而是在共享资本、cleanroom 和部分 wafer input 的条件下竞争资源。

## 4. Samsung 与 Micron 共同构成三厂竞争

全球 HBM 高端供给主要集中在：

- SK hynix
- Samsung
- Micron

三家公司在：

- TSV；
- stacking；
- advanced packaging cooperation；
- logic-base integration；
- HBM qualification

上形成寡头竞争。

但公开一手资料不足以支持一张完全可比的“全球 HBM 精确份额表”，因此本报告不把媒体或卖方 estimate 写成公司官方 market share。

真正重要的是：**HBM supply 仍集中在极少数能够同时完成 DRAM manufacturing 与 advanced stacking 的厂商。**

## 5. 51% DRAM bit share 的含义

TrendForce **预计**，2026 年 HBM + RDIMM 约占 **DRAM bit supply 的 51%**。这是 **2026E institutional forecast**，不是已经实现的 full-year actual。 来源：https://www.trendforce.com/presscenter/news/20260825-13198.html

这个数字不能理解成“51% DRAM 都是 HBM”，也不能改写成 wafer share 或 revenue share。

它表示 AI/server-related memory 在 TrendForce 的 2026 预测中已经占到 DRAM bit supply 的重要部分，而 HBM 的 wafer input 又高于同 bit DDR5。

因此，供给压力可以沿以下路径传导：

HBM demand 上升  
→ more wafer supply / cleanroom space  
→ conventional DRAM residual capacity 下降  
→ DDR5/LPDDR 等产品更容易面临供给紧张或价格上行。

这就是 **Non-AI Residual Capacity** 在 memory 行业中的具体形式。

## 5A. 价格反馈：HBM 的资源虹吸不是无限单向过程

资源重分配存在市场反馈，不应写成“H​BM 永远拥有最高单位 wafer 利润，因此 wafer 会无限向 HBM 转移”。

TrendForce 在 2026-06-02 的研究中估算：由于 conventional DRAM 自 2025 年下半年起快速涨价，按 die size、yield 与 per-Gb pricing 推算的 **per-wafer revenue** 比较中，**DDR5 64GB RDIMM 在 2026 Q1 已超过 HBM**；其估算的 HBM profitability 也因此低于 DDR5 64GB RDIMM。来源：https://www.trendforce.com/presscenter/news/20260602-13074.html

这属于 **B 级机构估算**，不是 Samsung、SK hynix 或 Micron 披露的产品级实际毛利率。但它揭示一个重要反馈机制：

```text
HBM / AI demand 上升
→ conventional DRAM residual supply 收紧
→ DDR5 / RDIMM price 上升
→ conventional DRAM per-wafer economics 改善
→ 继续向 HBM 转产的相对激励下降
→ memory vendor 重新平衡 product mix
```

因此，AI Resource Gravity 不是无限的单向抽水机。价格、长期合同、qualification、yield、generation transition 与客户结构会共同决定 memory allocation。真正需要监控的是不同产品的**风险调整后单位稀缺资源回报**，而不是假设 HBM 永久拥有固定利润倍数。

## 6. Rack-scale demand 的数量级

GB200 NVL72：

```text
13.4 TB HBM3E/rack
```

对应情景：

| Rack 数 | HBM3E demand |
|---:|---:|
| 1,000 | 13.4 PB |
| 10,000 | 134 PB |
| 30,000 | 402 PB |
| 50,000 | 670 PB |

这些数字只用于 stress test。

NVIDIA 没有公开全年 rack shipments；SK hynix、Samsung、Micron 也没有披露可直接对应到这些 rack 的全年 customer-level HBM bits，因此不能把情景需求写成实际消耗。

## 7. “推理改用 DDR5”并不是完全逃离内存约束

一种常见观点是：训练需要 HBM，但推理可以大量回到 commodity DDR5，从而绕开 HBM bottleneck。

这个方向在部分 workload 上成立，但不能简单推广到 frontier inference。

原因包括：

- KV cache 对 memory bandwidth 的要求；
- large-batch inference；
- long context；
- mixture-of-experts routing；
- low-latency serving；
- multi-accelerator communication。

更重要的是，DDR5/RDIMM 本身已经处在 AI/server demand 扩大的同一内存供给池中。

因此，推理从 HBM 转向 DDR5 更可能是**降低单位内存成本和带宽要求**，而不是创造一条完全独立的新供给河流。

## 8. 中国 memory supply 的边界

中国在 DRAM 与 NAND 上的本土供给能力持续增强，但需要严格区分产品层级。

CXMT 的公开招股材料披露 DDR 与 LPDDR 产品，但没有披露 HBM 产品线。

这个事实只能表述为：

> **该公开文件未披露 HBM 产品线。**

它不能被延伸为“企业不存在任何 HBM R&D”。

YMTC 属于 NAND 体系，也不能被用来直接替代 HBM/DRAM 的供给约束。

因此，中国 memory supply 对 consumer computing 的替代能力，与 frontier AI 的 HBM-class memory 替代能力必须分开讨论。

## 9. 当前判断

截至 2026 年 8 月，存储行业已经出现三个结构性变化：

1. HBM 成为高利润、高资本强度的核心产品；
2. AI/server memory 对 DRAM 资源的吸收显著提高，TrendForce 的 2026E bit-supply 预测提供了可观察前向锚；
3. HBM 的 wafer-supply trade ratio 放大了对 conventional DRAM residual capacity 的影响。

未来真正决定存储市场是否继续向 AI 倾斜的指标包括：

- HBM bit growth；
- HBM4 trade ratio；
- SK hynix/Samsung/Micron CapEx allocation；
- conventional DRAM price 与 supply；
- cloud custom silicon 的 HBM configuration；
- HBM packaging capacity；
- 中国是否出现可验证规模的 HBM-class product。

HBM 已经从“GPU 边上的高端内存”上升为 AI 基础设施资源竞争的核心层。

## 本卷关键公开来源

- TrendForce（2026E HBM + RDIMM = 51% of DRAM bit supply；2026/2027 CSP memory CapEx forecast）： https://www.trendforce.com/presscenter/news/20260825-13198.html
- Micron FY24 Q2 Prepared Remarks：https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- Micron FY24 Q2 Prepared Remarks（HBM3E ≈ 3× DDR5 wafer supply）： https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- Micron FY25 10-K（HBM requires more wafers / cleanroom space）：https://www.sec.gov/Archives/edgar/data/723125/000072312525000028/mu-20250828.htm
- NVIDIA GB200 NVL72 official product page（13.4 TB HBM3E/rack）：https://www.nvidia.com/en-us/data-center/gb200-nvl72/
- SK hynix FY25 official results：https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
