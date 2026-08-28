# 竞争集、替代路径与反方证据矩阵

> 本矩阵用于防止“霸权”主命题只由单一平台的强项材料支撑。它不把所有公司视为同一市场的直接可比对象，而是按物理层、系统层和终端层分别定义竞争问题。

| 分析层 | 主要观察对象 | 主要替代 / 竞争集合 | 核心比较指标 | 必须保留的反方证据 / 边界 | 主章节 |
|---|---|---|---|---|---|
| General-purpose AI system stack | NVIDIA | Google TPU/Ironwood、AWS Trainium、Microsoft Maia、Meta MTIA、AMD Instinct/ROCm | production workload、external availability、migration cost、system utilization、TCO、supply assurance | custom silicon 已是第二路线；不能用单芯片 benchmark 证明完整 system substitution | [Ch02](part-I-ch02-nvidia-system-stack.md), [Ch12](part-II-ch12-hyperscaler-system-stack.md), [Ch16](part-II-ch16-differentiated-competitors.md) |
| Advanced logic | TSMC | Samsung Foundry、Intel Foundry、SMIC，以及未来 qualified second source | qualified node、volume、yield disclosure、customer diversity、time-to-capacity | foundry revenue share ≠ frontier yield / node capacity；HPC share ≠ AI share | [Ch04](part-I-ch04-tsmc-advanced-logic.md), [Ch09](part-I-ch09-semiconductor-redundancy.md), [Ch17](part-II-ch17-china-parallel-stack.md) |
| HBM / DRAM | SK hynix、Samsung、Micron | conventional DRAM economics、CXMT conventional DRAM、future HBM entrants | HBM qualification、bits/wafer input、product mix、contract pricing、allocation fulfillment | DDR/RDIMM per-wafer economics 可反向改善；HBM 资源拉力不是无限单向 | [Ch05](part-I-ch05-hbm-memory.md), [Ch21](part-III-ch21-consumer-transmission.md) |
| Advanced packaging | TSMC CoWoS | Samsung/Intel packaging、OSAT expansion、alternative integration architectures | qualified capacity、lead time、yield/throughput disclosure、customer access | customer-level CoWoS allocation 未公开；B-grade demand share 不能升级为 TSMC fact | [Ch06](part-I-ch06-advanced-packaging.md) |
| Interconnect / software | CUDA/NVLink/NVSwitch ecosystem | ROCm、XLA/TPU stack、AWS Neuron、open compiler/runtime、alternative fabrics | migration cost、framework coverage、cluster scale、debuggability、production uptime | proprietary stack 可被部分 workload 绕开；“可运行”不等于低迁移成本 | [Ch02](part-I-ch02-nvidia-system-stack.md), [Ch12](part-II-ch12-hyperscaler-system-stack.md), [Ch16](part-II-ch16-differentiated-competitors.md) |
| Power / LPS / powered land | hyperscaler / AI-campus demand | utility expansion、restart projects、SMR / nuclear、grid/transmission buildout、LPS development | Announced→Contracted/Secured→Permitted→Construction→Energized→Utilized、Time-to-Power | generation GW、PPA GW 与 IT-GW 不能机械互换；headline capacity 不能相加成 active AI load | [Ch07](part-I-ch07-power-constraint.md) |
| Model-company demand | OpenAI、Anthropic 等 Anchor Buyers | hyperscaler internal workloads、enterprise demand、sovereign demand | contract duration、delivered capacity、utilization、monetization、financing support | long-duration commitment 既提高 buildout certainty，也放大 duration mismatch | [Ch13](part-II-ch13-anchor-compute-buyer.md), [Ch23](part-III-ch23-capital-financing.md) |
| China frontier stack | domestic accelerator/software/memory/foundry ecosystem | global frontier stack、domestic consumer/general-compute substitutes | advanced logic、HBM、packaging、interconnect、compiler/runtime、frontier workload、power closure | conventional DRAM/NAND 或 smartphone substitution 不等于 frontier-AI closure；出口限制也不等于“完全无替代” | [Ch17](part-II-ch17-china-parallel-stack.md) |
| Client / edge AI | Apple、Qualcomm、AMD、Intel | local inference、hybrid cloud-edge、NVIDIA edge products | performance/W、memory footprint、OS integration、distribution、privacy / latency | data-center system economics 不能直接外推到 battery/power-constrained edge | [Ch15](part-II-ch15-physical-ai.md), [Ch16](part-II-ch16-differentiated-competitors.md) |
| Capital cycle | hyperscalers、system sellers、memory/foundry/power projects | capacity overshoot / ROI shock as counter-scenarios | utilization、D&A、FCF、clearing price、commitments、asset duration、supplier-assisted financing | 高 CapEx 既可能是 moat 也可能是 future write-down source；需要区分独立终端需求与 supplier equity / credit support | [Ch19](part-III-ch19-capex-supercycle.md), [Ch22](part-III-ch22-depreciation-wall.md), [Ch23](part-III-ch23-capital-financing.md), [Ch24](part-III-ch24-capital-clearing.md) |

## 使用规则

1. 任何“dominance / hegemony”判断都必须至少同时回答：**替代是否存在、迁移成本多高、稀缺资源是否可多源、反向价格反馈是否正在工作。**
2. 竞争集合按 layer 定义，不把 smartphone SoC、frontier training accelerator、foundry、HBM vendor 强行放进同一个 market-share 表。
3. “没有等价替代”与“没有任何替代”必须分开。
4. 每次 major update 至少检查一条会**削弱**主论点的证据，而不只增加支持性证据。
5. 如果反方证据获得持续、可比且足够独立的支持，并改变核心机制变量，应调整 S1–S4 weighting，而不是仅放在脚注中。