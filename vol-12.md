# 第十二卷：中美 AI 产业链竞争与中国 Parallel Stack

## 1. 中国 AI 供给能力必须分层

讨论“中国能不能替代”如果不先分层，结论几乎一定失真。

至少要区分：

1. smartphone / consumer computing；
2. PC / workstation / general computing；
3. frontier AI system stack。

这三个层级使用的 logic、memory、packaging、software 和 performance requirement 并不相同。

因此，中国在 smartphone supply chain 上的成功不能直接外推成 frontier AI 已经完全替代；反过来，frontier AI 的约束也不能被写成“中国半导体只能做手机”。

## 2. 第一层：smartphone 与 consumer computing

中国在这一层拥有较完整的产业能力，包括：

- SoC design；
- mature / selected advanced foundry；
- LPDDR / NAND；
- packaging；
- device manufacturing；
- operating system / application ecosystem；
- large domestic market。

这一层的核心特点是：

- volume 大；
- supply chain 完整度高；
- domestic demand 能形成规模；
- performance requirement 与 frontier training 不同。

因此，中国 parallel supply 在 smartphone 与部分 consumer computing 上最容易形成。

## 3. 第二层：PC、workstation 与 general computing

这一层更复杂。

关键约束包括：

- high-performance CPU/GPU；
- Windows/x86 ecosystem 或可替代 desktop stack；
- DDR5；
- workstation software compatibility；
- professional graphics；
- developer ecosystem。

中国可以扩大本土 CPU、GPU、OS、memory 与整机供给，但要形成与全球主流 workstation 完全可替换的 experience，还需要更成熟的软件兼容、developer tooling 和 performance scale。

因此，这一层属于“部分替代正在扩大”，而不是“完全闭环”或“完全不可行”。

## 4. 第三层：frontier AI system stack

frontier AI 需要同时解决：

- advanced logic；
- HBM-class memory；
- advanced packaging；
- high-speed interconnect；
- compiler/runtime；
- distributed training；
- rack-scale deployment；
- data-center power。

这也是中国 parallel stack 最难的一层。

任何单点突破都不足以自动形成完整等价替代。

例如：

- 有 accelerator，但没有足够 HBM；
- 有 HBM prototype，但没有规模 packaging；
- 有 hardware，但 software migration cost 很高；
- 有 cluster，但 power / interconnect scaling 不足；

都会限制 system-level competitiveness。

## 5. Huawei Ascend / CANN 的战略意义

Ascend + CANN 的真正意义不是某一代单卡参数，而是中国正在构建一套与 CUDA 不同的完整 accelerator software stack。

关键价值在于：

- compiler/runtime；
- framework adaptation；
- distributed communication；
- model deployment；
- domestic developer ecosystem。

因此，它代表的是“另一套裁判体系”的形成。

衡量其进展，不应只看 peak FLOPS，而应该看：

- frontier model migration cost；
- large-cluster utilization；
- compiler maturity；
- operator coverage；
- deployment stability；
- workload scale。

## 6. Memory 是最容易被低估的约束

CXMT 的公开招股材料披露 DDR 与 LPDDR 产品，但没有披露 HBM 产品线。

这一事实应严格解释为：

> 该公开文件未披露 HBM product line。

它不能证明企业不存在任何 HBM R&D。

但从产业分析角度看，frontier AI parallel stack 是否闭环，必须出现可验证规模的 HBM-class memory。

YMTC 的 NAND 能增强 storage supply，却不能替代 HBM/DRAM。

因此，memory 不能被“国产存储”这个总词覆盖。

## 7. Foundry 与 advanced packaging 必须一起看

TrendForce 2026 Q1 foundry revenue share：

| Foundry | Revenue share |
|---|---:|
| TSMC | 约 **72%** |
| Samsung | 约 **6.5%** |
| SMIC | 约 **5.1%** |

这些是 foundry revenue share，不等于 frontier AI wafer capability。

中国要形成 frontier AI parallel supply，不只需要 logic wafer，还需要：

- advanced packaging；
- substrate；
- HBM integration；
- yield；
- high-volume qualification。

因此，“节点追赶”只是必要条件之一。

## 8. Algorithmic efficiency 是中国的重要非对称杠杆

DeepSeek 等案例说明，算法和 architecture 可以降低单位 capability 对硬件的需求。

这对受限 supply chain 尤其重要。

如果通过：

- sparse architecture；
- memory compression；
- better routing；
- quantization；
- scheduling；

降低单位任务所需 compute，那么有限硬件可以产生更高有效产出。

但算法效率不能被写成“物理供给已经不重要”。

其真正作用是：

> 在供给受限条件下提高 effective compute productivity。

## 9. Export control 的双重作用

Export control 会同时产生两个方向的影响。

### 短期

- 限制先进 hardware access；
- 提高 acquisition cost；
- 降低 frontier cluster deployment speed。

### 长期

- 强化 domestic substitution incentive；
- 提高 parallel ecosystem 的战略价值；
- 促进 local software/hardware integration。

因此，管制既可能扩大短期差距，也可能强化长期平行体系建设。

## 10. 中国 parallel stack 何时算真正闭环

本报告采用以下条件判断：

1. advanced accelerator 可规模化交付；
2. HBM-class memory 可规模化；
3. advanced packaging 可规模化；
4. high-speed interconnect 可支撑大集群；
5. compiler/runtime 迁移成本可接受；
6. frontier model training 可稳定运行；
7. data-center power 与 system deployment 可持续。

只有这些条件同时成立，才可以把中国描述为形成完整 frontier AI parallel stack。

## 11. 当前判断

截至 2026 年 8 月：

- smartphone / consumer computing parallel supply：较强；
- PC/workstation：替代能力扩大但不完全；
- frontier AI：已经形成重要本土技术栈，但关键 advanced layers 尚未全部实现等价规模闭环。

因此，最准确的判断不是“突破”或“封死”，而是：

> 中国正在从产品替代向系统栈替代推进，真正决定全球格局的是 advanced logic、HBM、packaging、interconnect 与 software 能否同时形成规模。
