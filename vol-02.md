# 第二卷：NVIDIA 平台支配力与系统栈护城河

## 1. 竞争单位已经从 GPU 上移到系统栈

NVIDIA 当前最重要的竞争优势，不是某一代 GPU 的单点性能，而是把芯片、HBM、互联、编译器、运行时和 rack-scale system 组织成一个完整采购单元。

GB200 NVL72 官方配置为：

| 项目 | 官方配置 |
|---|---|
| GPU | **72 Blackwell GPU** |
| CPU | **36 Grace CPU** |
| HBM | **13.4 TB HBM3E** |
| CPU memory | **17 TB LPDDR5X** |
| Scale-up domain | 72-GPU NVLink domain |
| Rack design | Liquid-cooled rack-scale system |

来源：https://www.nvidia.com/en-us/data-center/gb200-nvl72/

这意味着客户采购逻辑已经发生变化。单卡时代的比较重点是 FLOPS、显存和单卡价格；rack-scale 时代则必须比较：

1. GPU/accelerator
2. HBM capacity 与 bandwidth
3. scale-up interconnect
4. scale-out networking
5. compiler/runtime
6. distributed training stack
7. rack/power/cooling
8. 实际 workload 迁移成本

因此，“更便宜的一颗 ASIC”并不自动等于“更便宜的一套训练系统”。

## 2. CUDA/NVLink 的作用不是单独收一笔“软件税”

CUDA 的战略价值在于降低 NVIDIA 系统内部的软件迁移成本，同时提高迁往其他系统栈的工程成本。

其作用体现在多个层次：

- kernel 与 operator ecosystem；
- compiler/runtime；
- profiling 与 debugging；
- collective communication；
- inference stack；
- framework integration；
- distributed scheduling；
- 与 NVLink/NVSwitch 的系统级协同。

这种锁定不能简单换算成一个公开不存在的“40%软件溢价”。NVIDIA 没有在财报中单独披露 CUDA 对整柜毛利的贡献比例。

更准确的判断是：**软件栈扩大了硬件系统的可替代成本，从而增强系统级定价权与客户留存。**

开放迁移路线并非不存在。oneAPI、UXL 等多架构方案持续发展，但目前公开资料不足以证明 frontier AI workload 已经能够在无显著迁移成本的情况下，从 CUDA/NVLink 栈大规模迁移到另一套系统。

## 3. NVIDIA 的优势来自“系统定义权”

NVIDIA 的平台控制力可以分成四层。

### 3.1 Compute

GPU 仍然是核心计算单元，但产品形态已经从 accelerator card 上移到 integrated system。

FY26 Data Center revenue 为 **$193.737B**，其中 compute 与 networking 都已经构成重要收入来源。

### 3.2 Interconnect

NVLink/NVSwitch 把多 GPU 系统从“通过外部网络连接的独立加速器”推向“单一大规模计算域”。

这对训练尤其重要，因为 frontier model training 的瓶颈并不只在单卡 FLOPS，还在：

- all-to-all communication；
- model parallelism；
- memory movement；
- synchronization；
- cluster utilization。

### 3.3 Software

CUDA、TensorRT-LLM、NeMo、NIM 等产品共同降低 NVIDIA 系统内部部署成本。

这类软件资产的作用是强化系统可用性和迁移成本，而不是证明 NVIDIA 已经形成一个独立、可审计的“第二软件利润池”。

### 3.4 Roadmap coordination

Hopper → Blackwell → Rubin 的路线图不是单独升级 GPU，而是同时推进：

- logic node；
- HBM generation；
- advanced packaging；
- interconnect；
- rack architecture；
- power/cooling design。

FY27 Q2，NVIDIA 已披露 Rubin 进入 **full production**。这表明竞争单位仍然在向完整系统推进，而不是退回单芯片比较。

## 4. 高利润为何会转化为资源预订能力

NVIDIA 的资源预订能力可由以下财务指标观察：

| 指标 | 数值 |
|---|---:|
| FY26 Free cash flow | **$96.575B** |
| FY26 Operating income | **$130.387B** |
| FY27 Q2 Revenue | **$96.221B** |
| FY27 Q2 Data Center revenue | **$89.0B** |
| FY27 Q2 GAAP gross margin | **75.0%** |
| FY27 Q2 GAAP operating income | **$63.734B** |

FY27 Q1 supply-related commitments 已上升至 **$119.0B**。

这些数字说明，平台利润可以被重新投入到下一代：

- wafers；
- HBM；
- advanced packaging；
- substrates；
- networking components；
- system inventory。

这构成一种跨代强化机制：

**高系统利润 → 更强资源预订能力 → 更高交付确定性 → 更强客户留存 → 下一代更大的系统收入。**

但这不是“自动垄断公式”。供应商仍会考虑客户多元化、信用、利用率、长期合同、地缘政治和议价平衡。

## 5. Cloud custom silicon 正在攻击什么

Google TPU/Ironwood、AWS Trainium、Microsoft Maia、Meta MTIA 不应被理解成“几颗 ASIC 来挑战 NVIDIA GPU”。

真正的替代路径是 **Cloud System-Stack Substitution**。

要形成有效替代，云厂商至少需要同时解决：

- accelerator architecture；
- compiler/runtime；
- framework support；
- HBM；
- scale-up fabric；
- scale-out network；
- rack/pod；
- large internal workload；
- developer migration。

这些系统可以减少 NVIDIA 在芯片、软件与互联层的利润捕获，但它们仍可能需要相同的先进逻辑、HBM、advanced packaging 和 power。

因此存在两个同时成立的效应：

1. **Platform-profit diversion**：云自研系统分流 NVIDIA 平台利润。
2. **Upstream resource competition**：云自研系统增加对先进上游资源的竞争。

这两者并不矛盾。

## 6. 竞争护城河的真正边界

NVIDIA 的护城河最强处，不是任何单一硬件参数，而是系统栈的联动：

> GPU + HBM + NVLink/NVSwitch + CUDA/runtime + rack architecture + deployment tooling

但这个护城河不是不可打破。

以下变化会显著削弱平台支配力：

- cloud custom silicon 在 frontier training 中规模化；
- 开放软件层显著降低 CUDA migration cost；
- alternative scale-up fabric 成熟；
- HBM/packaging 供给显著宽松；
- 大客户把 workload 同时部署在多套系统栈；
- regulatory remedy 强制开放接口或限制 tying。

## 7. 当前判断

截至 2026 年 8 月，NVIDIA 已经形成明显的系统级平台支配力，但尚不足以定义为“竞争已经结束”。

更准确的状态是：

- 单芯片竞争正在转化为系统栈竞争；
- NVIDIA 仍拥有最成熟的商业化通用 AI system stack；
- cloud custom silicon 已经形成真实的第二条技术路线；
- 竞争焦点正在从“谁有更好的芯片”转向“谁能控制完整系统的成本、迁移、供给与利用率”。

这也是后续所有供应链分析的起点。
