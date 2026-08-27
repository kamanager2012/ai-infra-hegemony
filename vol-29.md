# 第二十九卷：中国 Frontier AI Parallel Stack 的系统级评估

## 1. “能跑起来”与“形成等价系统”不是同一个标准

评估中国 AI stack 不能只看某一颗 accelerator 是否能够运行模型。

需要分成：

1. functional availability；
2. performance；
3. scale；
4. software portability；
5. supply sustainability；
6. economics。

只有这些维度同时达到可接受水平，才构成 system-level substitution。

## 2. Ascend + CANN 的价值在于系统完整性

Huawei Ascend 的战略意义来自：

- accelerator；
- CANN；
- communication；
- server/system；
- domestic cloud deployment。

因此，评价它不能只比较 peak FLOPS。

更重要的是：

- large-cluster utilization；
- compiler stability；
- operator coverage；
- framework compatibility；
- failure recovery；
- production deployment。

这是 system-stack 竞争。

## 3. Interconnect 是大集群的关键

frontier training 需要：

- tensor/model parallel；
- expert routing；
- collective communication。

因此，interconnect 决定：

- scaling efficiency；
- cluster utilization；
- usable compute。

即使单卡性能足够，如果 cluster communication 无法有效扩展，大规模训练效率仍会受到限制。

所以国产 stack 的关键测试不是“单卡 benchmark”，而是：

> thousands-of-accelerator cluster 的有效 utilization。

## 4. CANN 与 CUDA 的真正竞争指标

CANN 的竞争目标不只是“支持 PyTorch”。

需要长期观察：

- operator completeness；
- compiler optimization；
- debugging；
- profiler；
- distributed runtime；
- multi-generation compatibility；
- developer tooling。

migration cost 只有在 production workload 中足够低，才能真正削弱 CUDA switching cost。

## 5. Foundry 是必要条件，但不是全部

China frontier AI supply 仍受到 advanced logic 约束。

但即使 logic die 能够稳定生产，完整 system 还需要：

- HBM；
- packaging；
- substrate；
- interconnect；
- power。

因此，foundry progress 必须与整个 stack 同时评估。

## 6. HBM 是最关键的未闭环层之一

CXMT 公开招股材料披露 DDR/LPDDR，但未披露 HBM product line。

这不能证明没有任何 HBM R&D。

但产业层面需要出现：

- official product；
- customer qualification；
- volume production；
- bandwidth/capacity；
- packaging integration。

只有这些出现，才能把国产 HBM 从“研发可能性”升级为“system supply”。

## 7. Algorithmic efficiency 是重要杠杆

受限 supply chain 下，算法优化具有更高价值。

可通过：

- sparse model；
- memory compression；
- quantization；
- communication optimization；
- routing；

提高 effective compute。

因此，中国 stack 不需要在每一个硬件指标上完全复制 NVIDIA，才能形成有价值的 domestic system。

但算法不能替代全部 physical bottleneck。

## 8. Domestic demand 是最大的战略资产之一

中国拥有：

- large cloud market；
- internet platforms；
- manufacturing；
- government/enterprise demand。

这允许国产 stack 在国内 workload 中积累：

- compiler feedback；
- deployment experience；
- software ecosystem；
- scale。

这与 hyperscaler custom silicon 的逻辑类似：

> 自己拥有大 workload，就可以在不先征服全球 developer 的情况下迭代 system。

## 9. Export control 同时强化 parallel-stack incentive

出口限制提高短期成本，但也提高 domestic stack 的战略必要性。

长期影响取决于：

- R&D efficiency；
- capital allocation；
- ecosystem adoption；
- supply scaling。

因此，export control 不是单向变量。

## 10. 什么时候可以说“形成第二系统”

本报告采用七项 gate：

1. advanced accelerator scale；
2. HBM-class memory scale；
3. advanced packaging scale；
4. large-cluster interconnect；
5. mature compiler/runtime；
6. frontier workload migration；
7. sustainable cost/utilization。

七项都达到可验证规模，才是完整 frontier AI parallel stack。

## 11. 当前判断

截至 2026 年，中国已经拥有真实、持续发展的 accelerator/software parallel stack。

但最前沿 system-level substitution 仍需要多个 advanced layer 同时闭环。

因此，最准确的描述是：

> **中国已经跨过“没有替代系统”的阶段，但尚未跨过“所有关键层都实现全球等价规模”的阶段。**

这个中间状态本身就足以改变全球 AI supply-chain strategy。
