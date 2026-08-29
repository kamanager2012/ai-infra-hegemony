# Part II · 第15章：Physical AI 与机器人系统的真正瓶颈

## 1. 机器人竞争单位同样是 System

Physical AI 需要同时解决 perception、planning、control、actuation、power、safety 与 mechanical reliability。

所以一台机器人能否形成生产力，不能只由 AI model 或 edge TOPS 判断。

完整系统至少要把：

> **model capability × sensor quality × control latency × actuator reliability × energy efficiency × manufacturing economics**

同时闭合。

## 2. Cloud Training 与 Edge Control 是两套物理约束

large-scale simulation、policy training 与 foundation-model training 可以在 data center 完成。

实时 control 则受到 latency、thermal、battery、sensor loop 与 safety deadline 约束。

所以很多 Physical AI 系统天然呈现：

> **cloud-side heavy training + edge-side compressed inference/control**

data-center 的约 **120 kW-class rack**[^4] 与机器人本体的 W/Wh 级 power budget 属于完全不同的物理池。

## 3. Robot BOM 不能套统一百分比模板

humanoid、AMR、industrial arm、autonomous vehicle、drone 的 actuator、reducer、sensor、compute 与 battery 成本结构差异巨大。

因此，本报告不采用固定“执行器35% / 传感器20% / 计算25%”之类行业模板。

真正需要识别的是不同机器人形态中的 **scarce component**。

## 4. Actuator / Reducer 可能比 Compute 更难商品化

Physical AI 最容易被软件叙事低估的，是 frameless torque motor、harmonic reducer、planetary roller screw、bearing 与 precision gearbox 等机械部件。

它们的竞争变量包括 durability、backlash、repeatability、noise、yield、maintenance 与 cost。

于是完全可能出现：

> **compute 更便宜，但高精度机械部件仍是系统瓶颈。**

## 5. Sensor Quality 决定模型能否转化成可靠 Control

robot system 需要 camera、depth、force/torque、tactile、IMU、encoder 等多种 sensing。

模型能力只有在 calibration、latency、robustness 与 failure detection 足够好时，才能转化成稳定 control。

因此 sensor stack 的价值不只是 BOM，而是 closed-loop reliability。

## 6. Edge Platform 的战略位置

NVIDIA Jetson Thor、Qualcomm 与其他 edge accelerators 的竞争维度是 compute、software、power efficiency 与 developer ecosystem。NVIDIA Isaac/GR00T 将 simulation/training、robot model 与 Jetson Thor onboard compute 组织成跨 cloud-to-edge workflow。[^1][^2]

edge system 不需要复制 data-center rack architecture。

但如果同一平台同时覆盖 cloud training / simulation / edge deployment，就可能形成 cloud-to-robot 的跨层 ecosystem lock-in。

## 7. Physical Deployment 会反向制造更多 Cloud Workload

即使单台 robot 的 edge compute 很有限，大规模 fleet 会持续产生：

- video / sensor data；
- simulation；
- retraining；
- synthetic data；
- fleet analytics；
- model updates。

因此可形成：

> **physical deployment → data generation → retraining → more cloud compute**

机器人普及不一定减少 data-center demand，反而可能扩大新的训练/推理 workload。

### 7.1 机器人本体也可能成为新的 Memory / Storage Demand Pool

Micron 在 2026-06-24 investor presentation 中给出一个值得跟踪、但必须保留“公司前瞻判断”身份的量化锚：[^3]

- L2+ 及以上车辆的 memory + storage content 已超过 average vehicle 的 **5×**；
- Micron 称 humanoid robots 的 memory content 约为 average L2+ vehicle 的 **10×**；
- 公司预计本十年后段开始形成持续、多十年的 robotics memory demand cycle。

这不是全行业 actual shipment，也不是“每台机器人固定需要数百 GB DRAM + 数 TB SSD”的统一规格。

它真正支持的机制是：

> **Physical AI commercial scale ↑ → edge memory/storage content ↑ + fleet-generated cloud workload ↑**

所以机器人可能同时成为 edge memory 的新需求池和 cloud retraining / storage 的新需求源。

### 7.2 机器人具有双重身份：AI 需求方，也是工业电子的残量承压方

Physical AI 不只是新的 AI compute demand。

机器人本体同时依赖：

- MCU / control electronics；
- sensors；
- motor drive / power electronics；
- industrial memory / storage；
- edge accelerator；
- networking。

因此它可能同时受到两类上游约束：

> **industrial-electronics supply pressure + edge-AI compute / memory pressure**

这也是为什么机器人不能只按“AI 模型能力”判断产业速度。即使 cloud training 与 edge model 进步很快，MCU、sensor、actuator electronics、qualified memory 或其他工业器件的交期与供应连续性仍可能限制 mass deployment。

反过来，也不能把任何工业器件短缺都归因于 AI。具体归因仍需满足第3、21章的 shared-resource / product-mix / allocation evidence 要求。

---

## 8. 机器人侧的 Power Wall 是 Battery / Thermal

data center 的 power bottleneck 是 grid / interconnection；机器人侧则是 battery energy density、runtime、charging、thermal 与 peak actuator demand。作为量纲对照，NVIDIA DGX GB200 rack 的官方功耗约为 120 kW，但该数据只用于说明 cloud 与 edge 属于不同物理池。[^4]

因此 Physical AI 应比较：

> **Useful task output / Wh**

以及 continuous runtime、recharge time、thermal headroom、maintenance interval 与 field reliability，而不是只比较 TOPS。

## 9. Demo 到 Mass Production 的真正门槛是 Manufacturing

demo 可以容忍 expensive parts、manual calibration、low yield 和 frequent maintenance。

mass production 不行。

规模化临界点包括 component yield、assembly time、field failure rate、maintenance interval、supply-chain stability 与 unit economics。

因此 Physical AI 的产业拐点必须由 manufacturing / deployment data 证明，而不能由演示视频证明。

## 9A. Physical AI 的商业临界点不是“能完成任务”，而是 Capital Payback

机器人从 demo 进入 production 后，真正需要比较的不是单次任务成功率，而是：

```text
Economic Output
≈ Useful Tasks per Hour
× Uptime
× Deployment Scale
- Energy
- Maintenance
- Human Supervision
- Financing / Depreciation
```

因此，一台机器人即使技术上可以完成某项工作，如果：

- utilization 低；
- downtime 高；
- maintenance interval 短；
- human supervision 仍重；
- replacement / component failure 快；
- upfront CapEx 过高；

仍然可能无法形成可持续 ROI。

这使 Physical AI 与 data-center AI 共享一个资本规律：

> **能力必须最终通过 utilization 与现金流证明。**

区别只是 data-center 的 bottleneck 更多在 compute / HBM / power，机器人则多出 actuator、battery、mechanical reliability、field service 与 safety。

## 10. 中国在 Physical AI 上的能力结构与 Frontier AI 不同

Physical AI 大量依赖 motors、battery、sensors、manufacturing、consumer-electronics supply chain 与 system integration。

这些层与 frontier AI 的 HBM / advanced-packaging / leading-edge compute 闭环并不完全重合。

所以中国在机器人整机和机械供应链上的竞争力，可以与其在 frontier AI infrastructure advanced layers 的状态不同。

这是独立产业路径，不应被一个“AI 芯片能力”指标覆盖。

## 11. 当前判断：Value Capture 可能分布在多个物理层

长期 value capture 可能同时出现在：

- edge compute / software platform；
- actuator / reducer；
- sensor；
- battery / power electronics；
- manufacturing / integration；
- cloud simulation / training infrastructure。

机器人革命的真正竞争不是“谁模型 benchmark 最好”，而是：

> **谁能把 AI capability 转化成可靠、低成本、可量产、可维护，而且能够以足够高 utilization 回收资本的物理工作。**

## References

[^1]: NVIDIA Developer, Isaac platform, simulation/training and robotics workflow, https://developer.nvidia.com/isaac
[^2]: NVIDIA, 2026-06, Isaac GR00T Reference Humanoid Robot, Jetson Thor onboard compute and Isaac GR00T platform, https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design
[^3]: Micron Technology, investor presentation, 2026-06-24, humanoid-robot memory-content outlook, https://s25.q4cdn.com/621799436/files/doc_financials/2026/q3/Micron_Q3_26_Earnings_Deck.pdf
[^4]: NVIDIA, DGX GB200 Hardware Guide, rack power approximately 120 kW, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
