# 第十七卷：AI 基础设施终极风险——物理、资本、替代与制度约束

## 1. 风险不是一个“泡沫概率”

AI infrastructure 的主要风险来自多条独立链路。

本卷将其分为五类：

1. physical bottleneck；
2. power bottleneck；
3. capital / utilization risk；
4. system substitution；
5. regulatory / geopolitical risk。

这些风险可以单独发生，也可以形成级联。

## 2. Physical risk：logic、HBM 与 packaging 同时受限

frontier AI system 依赖：

- advanced logic；
- HBM；
- advanced packaging；
- interconnect。

其中任何一层失效，都可能成为系统交付上限。

Micron 的 HBM3E ~3× wafer-supply trade ratio 说明 memory demand 会放大 DRAM wafer pressure。

TSMC 对 advanced packaging tightness 的公开表述说明 packaging 不是“配套”，而是增长约束。

因此，physical risk 不是 transistor scaling 单点问题，而是多层集成风险。

## 3. Power risk：硬件可交付但无法上电

当 rack power 进入约 120 kW 级后，power 可能成为 semiconductor 之后的新瓶颈。

主要风险包括：

- grid delay；
- substation shortage；
- transformer shortage；
- permit delay；
- insufficient firm generation；
- cooling constraints。

如果 power 成为主导瓶颈，最先出现的不是 GPU price collapse，而是：

- deployment delay；
- low utilization；
- slower next-generation orders。

## 4. Capital risk：利用率无法覆盖资产负担

AI infrastructure 的资本风险来自：

- rapid hardware iteration；
- large annual CapEx；
- long-duration power/data-center assets；
- uncertain workflow monetization。

真正需要观察的是：

```text
Economic Return
=
Revenue from deployed compute
-
Depreciation
-
Power
-
Operations
-
Financing
```

如果 deployed compute 利用率不足，资本压力会先反映在：

- asset impairment；
- second-hand price；
- CapEx guidance；
- order cancellation；
- supply commitment。

## 5. Model efficiency risk：需求函数可能被技术改变

MLA、MoE、quantization、speculative decoding 等优化可以显著降低单位任务所需：

- compute；
- memory；
- communication。

如果效率提升速度长期高于 workload 增长，infrastructure demand 可能被压低。

如果更低成本带来更高 workload volume，则总需求仍可能上升。

因此，algorithmic efficiency 是最大的不确定需求变量之一。

## 6. Cloud system-stack substitution

Google、AWS、Microsoft、Meta 的自研系统可以：

- 分流 NVIDIA platform profit；
- 降低内部 workload 成本；
- 提高 buyer bargaining power。

但它们同时可能继续使用：

- TSMC advanced logic；
- HBM；
- advanced packaging；
- data-center power。

因此，system substitution 对平台层和上游 physical layer 的影响方向并不相同。

## 7. China parallel stack

如果中国完成：

- advanced logic；
- HBM；
- packaging；
- interconnect；
- software；

的规模闭环，全球 AI infrastructure 将出现第二个强资源重力中心。

这会降低单一全球 system stack 的控制力。

反之，如果关键 advanced layers 长期受限，全球产业仍会保持明显技术分层。

## 8. Regulatory risk

监管最重要的潜在影响不是罚款，而是：

- interface openness；
- tying restriction；
- non-discriminatory supply；
- structural separation。

这些措施可以直接改变 switching cost 和 bargaining power。

但监管无法直接创造 physical capacity，因此 regulatory risk 必须与 manufacturing risk 分开。

## 9. Geopolitical risk

AI infrastructure 已经高度集中于：

- 少数 foundry；
- 少数 HBM vendor；
- 特定 advanced packaging geography；
- 特定 power region。

因此，地缘风险包括：

- export control；
- trade restriction；
- supply interruption；
- regional conflict；
- industrial policy fragmentation。

地缘冲击可能导致：

- capacity duplication；
- lower efficiency；
- higher inventory；
- parallel ecosystem。

## 10. Risk cascade

最危险的状态不是某一个风险单独上升，而是风险串联。

例如：

power delay  
→ utilization 下降  
→ buyer ROI 下降  
→ next CapEx 下调  
→ hardware order 下降  
→ HBM/packaging tightness 松动  
→ supplier CapEx 下调。

这就是 **Rolling Bottleneck Cascade** 的反向版本。

## 11. 当前风险排序

截至 2026 年 8 月：

### 已经存在的高确定性风险

- HBM / packaging tightness；
- rapidly rising CapEx；
- power delivery pressure；
- model/software price competition。

### 中等确定性风险

- cloud system-stack substitution；
- China parallel stack expansion；
- regulatory intervention。

### 尚未被充分证明的系统性风险

- industry-wide chronic low utilization；
- large-scale stranded AI assets；
- broad order cancellation；
- full capital hard landing。

## 12. 证伪框架

任何“AI infrastructure 会持续集中”的判断都必须被以下事实推翻：

- packaging/HBM 长期宽松；
- supply commitments 明显下降；
- cloud frontier training 大规模迁离 NVIDIA；
- power bottleneck 导致持续 deployment failure；
- utilization 下降；
- China parallel stack 完整闭环；
- structural regulatory remedy 落地。

风险分析的价值不在于预测哪一天崩溃，而在于提前定义：**什么事实出现时，原判断必须改变。**

## 本卷关键公开来源

- Micron FY24 Q3 Prepared Remarks（HBM3E ≈ 3× DDR5 wafer supply）： https://investors.micron.com/static-files/4550f98c-1054-4847-a929-c17d520a0564
