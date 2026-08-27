# 第二十八卷：Physical AI 与机器人系统的真正瓶颈

## 1. Physical AI 不是“把大模型装进机器人”

机器人系统需要同时解决：

- perception；
- planning；
- control；
- actuation；
- power；
- safety；
- mechanical reliability。

因此，Physical AI 的竞争单位同样是 system，而不是单一 AI chip。

## 2. Cloud training 与 edge control 是两套不同物理约束

机器人模型的：

- large-scale simulation；
- policy training；
- foundation-model training

可以在 data center 完成。

实时 control 则受到：

- latency；
- power；
- thermal；
- battery；
- sensor loop

约束。

因此，机器人通常需要：

> cloud-side heavy training + edge-side compressed inference/control。

这与 rack-scale AI 的 100 kW 级环境完全不同。

## 3. Robot BOM 不能被一个百分比模板固定

不同机器人形态差异巨大：

- humanoid；
- AMR；
- industrial arm；
- autonomous vehicle；
- drone。

它们的：

- actuator；
- reducer；
- sensor；
- compute；
- battery

成本占比完全不同。

因此，本报告不采用统一“执行器35% / 传感器20% / 计算25%”作为行业事实。

真正需要分析的是每类机器人中的**scarce component**。

## 4. Actuator / reducer 可能比 compute 更难复制

Physical AI 最容易被 AI 叙事忽略的是机械部件。

例如：

- frameless torque motor；
- harmonic reducer；
- planetary roller screw；
- bearing；
- precision gearbox。

这些部件的竞争力来自：

- durability；
- repeatability；
- backlash；
- noise；
- yield；
- cost。

因此，机器人产业完全可能出现：

> compute commoditizes，但高精度 actuator/reducer 仍然稀缺。

## 5. Sensor 是另一类 physical bottleneck

机器人需要：

- camera；
- depth；
- force/torque；
- tactile；
- IMU；
- encoder。

Physical AI 的模型质量只有在 sensor quality 足够高时才能转化为可靠 control。

因此，sensor calibration、latency 和 robustness 可能成为与 AI model 同等重要的系统约束。

## 6. Edge compute 的战略位置

NVIDIA Jetson/Thor、Qualcomm、China domestic accelerator 等 edge platform 的竞争，本质是：

- compute；
- software；
- power efficiency；
- developer ecosystem。

edge platform 不需要复制 data-center GPU 的完整 rack architecture。

但如果同一家平台同时控制：

- cloud training；
- simulation；
- edge deployment；

就可以形成跨 cloud-to-robot 的 ecosystem lock-in。

## 7. Physical AI 对 upstream AI infrastructure 的反向需求

即使 edge robot 单机算力有限，robot fleet 会产生大量：

- simulation；
- training；
- synthetic data；
- video processing；
- model update

需求。

因此，机器人普及可能反过来扩大 data-center workload。

这形成：

physical deployment  
→ data generation  
→ retraining  
→ more cloud compute。

## 8. Power 与 battery 是机器人侧的“第三堵墙”

data center 的 power bottleneck 是 grid。

机器人侧的 power bottleneck 是：

- battery energy density；
- thermal；
- runtime；
- charging。

因此，Physical AI 的 performance 不能只用 TOPS 衡量。

真正需要比较：

```text
Useful task output / Wh
```

以及：

- continuous operating time；
- recharge time；
- heat；
- reliability。

## 9. Manufacturing scale 决定机器人是否从 demo 进入产业

机器人 demo 可以容忍：

- expensive parts；
- manual calibration；
- low yield；
- frequent maintenance。

mass production 不行。

真正的规模化临界点包括：

- component yield；
- assembly time；
- maintenance interval；
- field failure；
- unit economics。

因此，Physical AI 的产业拐点必须由 manufacturing data 证明，而不是由视频 demo 证明。

## 10. China 在 Physical AI 上具有不同于 frontier AI 的机会

Physical AI 的 supply chain 包含大量中国已有优势的领域：

- motors；
- battery；
- sensors；
- manufacturing；
- supply-chain integration；
- consumer electronics。

因此，中国在机器人整机和机械供应链上的竞争力，可能强于其在 frontier AI infrastructure 某些 advanced layer 的竞争力。

这是一条独立产业路线。

## 11. 当前判断

Physical AI 会扩大 AI 的物理边界，但其核心瓶颈不会只在 GPU。

长期价值捕获可能分布在：

- edge compute platform；
- actuator/reducer；
- sensor；
- battery；
- manufacturing；
- cloud simulation/training。

因此，机器人革命真正的竞争不是“谁模型最好”，而是谁能把 AI capability 转化成**可靠、低成本、可量产的物理工作**。
