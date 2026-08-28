# 第十九卷：2026–2036 AI 基础设施时间线与阶段性里程碑

## 1. 时间线应该按条件推进，而不是按年份编故事

未来十年无法用一张精确年份表预测。

更可靠的方法是把时间线分成阶段，并定义每个阶段需要观察的可验证里程碑。

本卷采用四阶段：

- Phase I：2026–2027
- Phase II：2028–2030
- Phase III：2031–2033
- Phase IV：2034–2036

年份只是观察窗口，不代表事件必然在该年发生。各阶段的情景变量统一回溯至 [《核心假设矩阵》](核心假设矩阵.md)。

## 2. Phase I：2026–2027 —— system race 与基础设施锁定

当前已经确认的状态包括：

- NVIDIA FY27 Q2 Data Center revenue：$89.0B；
- GAAP gross margin：75.0%；
- Rubin：full production；
- manufacturing, supply, and capacity commitments：2026-04-26 **US$119B**；2026-07-26 **US$279B**（Q2 10-Q，最新承诺主要关联 memory 与 manufacturing facilities）；
- TSMC packaging tightness 仍限制客户增长；
- HBM + RDIMM 约占 2026 DRAM bits 的 51%；
- cloud CapEx 继续扩大；
- hyperscaler power contract 进入 835 MW、1.92 GW、500 MW 等级。

这一阶段的核心问题：

> demand 是否继续快于 scarce-layer supply expansion？

关键里程碑：

- Rubin volume deployment；
- HBM4 ramp；
- advanced packaging expansion；
- cloud custom silicon 新一代部署；
- power project actual energization；
- supply commitments 是否继续增长。来源：https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm 。

## 3. Phase II：2028–2030 —— substitution 是否形成规模

这一阶段决定 S1 与 S2/S3 的分叉。

需要观察：

### Cloud

- TPU/Trainium/Maia/MTIA 是否在 frontier training 中形成大规模占比；
- internal workload 是否持续迁移；
- external customer adoption 是否提高。

### Software

- CUDA migration cost 是否下降；
- open compiler/runtime 是否形成真实 production alternative；
- multi-stack deployment 是否成为企业常态。

### Memory / packaging

- HBM supply 是否显著宽松；
- packaging 是否仍被描述为 growth constraint；
- new packaging architecture 是否提高供给弹性。

### Power

- contracted GW 是否真正变成 energized GW；
- powered land 是否仍然稀缺。

## 4. Phase III：2031–2033 —— 地理与产业结构固化

如果 AI infrastructure 继续扩大，到这一阶段竞争会从“产品路线”进一步上升到“区域基础设施体系”。

需要观察：

- 哪些地区形成 power + data center + chip access 的组合优势；
- China parallel stack 是否完成 frontier-layer 闭环；
- sovereign AI 是否形成多个区域 system ecosystem；
- global supply chain 是否继续一体化，还是长期分区。

这一阶段的核心指标不再只是 chip benchmark，而是：

- total deployable compute；
- system utilization；
- powered capacity；
- cross-stack portability；
- regional supply resilience。

## 5. Phase IV：2034–2036 —— 产业进入成熟、集中或清算

到 2034–2036，四类结构将逐步清晰：

### Competitive Expansion

多套 system stack 成熟，成本下降，市场继续扩大。

### Baseline Concentration

少数大型平台长期并存，scarce-layer supplier 保持高战略价值。

### Resource Hegemony

少数平台对 logic/HBM/packaging/software/power 的协调能力进一步集中。

### Capital Hard Landing

已建基础设施供过于求，行业从建设竞赛转向利用率与现金流清算。

## 6. 哪些技术节点不应预写死

本报告不为未来年份预设：

- wafer price；
- exact node ASP；
- exact CoWoS wafers/month；
- exact GW/rack count；
- exact company market share。

原因是这些变量高度依赖：

- yield；
- product mix；
- architecture；
- demand；
- regulation；
- capital cycle。

时间线只记录**条件里程碑**。

## 7. Algorithmic milestones

未来十年需要持续跟踪：

- memory compression；
- sparse architecture；
- quantization；
- inference scheduling；
- model routing；
- on-device capability。

如果 algorithmic efficiency 显著降低 frontier workload 的 compute intensity，基础设施需求路径会改变。

但只有在**总 workload demand 也下降**时，才会真正削弱 aggregate infrastructure demand。

## 8. Capital milestones

每个阶段都应同时观察：

- hyperscaler CapEx；
- depreciation；
- supply commitments；
- utilization；
- second-hand hardware price；
- enterprise AI monetization。

技术路线和资本周期必须放在同一时间轴上。

## 9. Power milestones

power timeline 需要记录：

- permit；
- interconnect；
- energization；
- utilization。

而不是只记录“签了多少 GW”。

Crane、Talen/AWS、Kairos 等项目应持续按成熟度更新，而不能在合同签署时直接标记为“AI power online”。

## 10. 当前判断

未来十年最重要的不是预测某一年谁赢，而是识别三个临界点：

1. **system substitution 是否跨过 frontier training 临界点；**
2. **scarce-layer supply 是否跨过长期宽松临界点；**
3. **AI workload monetization 是否跨过覆盖资本成本的临界点。**

这三个临界点决定 2026–2036 最终走向 S1、S2、S3 还是 S4。
