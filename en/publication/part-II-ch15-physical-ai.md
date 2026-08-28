# Part II · Chapter 15: Physical AI and the Real Bottlenecks in Robotics

## 1. The competitive unit in robotics is also the system

Physical AI has to solve perception, planning, control, actuation, power, safety, and mechanical reliability at the same time.

A robot's productive value therefore cannot be judged from the AI model or edge TOPS alone.

A complete system has to close:

> **model capability × sensor quality × control latency × actuator reliability × energy efficiency × manufacturing economics**

## 2. Cloud training and edge control sit under different physical constraints

Large-scale simulation, policy training, and foundation-model training can run in data centers.

Real-time control is constrained by latency, thermals, battery, sensor loops, and safety deadlines.

Many Physical AI systems therefore naturally follow:

> **cloud-side heavy training + edge-side compressed inference/control**

A roughly 120 kW-class data-center rack and a robot's W/Wh-level power budget belong to completely different physical pools.

## 3. Robot BOM cannot be fixed by a universal percentage template

Humanoids, AMRs, industrial arms, autonomous vehicles, and drones have very different actuator, reducer, sensor, compute, and battery cost structures.

This report therefore does not treat fixed templates such as "actuators 35% / sensors 20% / compute 25%" as industry fact.

The real task is to identify the **scarce component** for each robot form factor.

## 4. Actuators and reducers can be harder to commoditize than compute

The software narrative can easily understate mechanical bottlenecks such as:

- frameless torque motors;
- harmonic reducers;
- planetary roller screws;
- bearings;
- precision gearboxes.

The key variables include durability, backlash, repeatability, noise, yield, maintenance, and cost.

The industry can therefore reach a state where:

> **compute gets cheaper while high-precision mechanical components remain system bottlenecks.**

## 5. Sensor quality determines whether model capability becomes reliable control

Robotic systems may require cameras, depth sensing, force/torque sensors, tactile sensors, IMUs, encoders, and other feedback channels.

Model capability becomes stable control only when calibration, latency, robustness, and failure detection are strong enough.

The strategic value of the sensor stack is therefore not just BOM share. It is closed-loop reliability.

## 6. The strategic position of the edge platform

NVIDIA Jetson/Thor, Qualcomm, and other edge accelerators compete across:

- compute;
- software;
- power efficiency;
- developer ecosystem.

An edge system does not need to replicate data-center rack architecture.

But a platform that spans cloud training, simulation, and edge deployment can create cross-layer cloud-to-robot ecosystem lock-in.

## 7. Physical deployment can generate more cloud workload in reverse

Even if one robot uses modest edge compute, a large fleet continuously generates:

- video / sensor data;
- simulation workloads;
- retraining;
- synthetic data;
- fleet analytics;
- model updates.

The feedback loop can be:

> **physical deployment → data generation → retraining → more cloud compute**

Robot adoption therefore does not necessarily reduce data-center demand. It can create new training and inference workloads.

### 7.1 The robot itself can become a new memory / storage demand pool

Micron's June 24, 2026 investor presentation provides a useful quantitative anchor that must retain its identity as a **company forward-looking view**:

- L2+ and above vehicles carry more than **5×** the memory and storage content of an average vehicle;
- Micron states that humanoid robots carry roughly **10×** the memory content of an average L2+ vehicle;
- the company expects a sustained, multi-decade robotics memory-demand cycle to begin in the latter part of this decade.

This is not industry-wide actual shipment data and it does not establish a universal "hundreds of GB of DRAM + several TB of SSD per robot" configuration.

What it supports is the mechanism:

> **Physical AI commercial scale ↑ → edge memory/storage content ↑ + fleet-generated cloud workload ↑**

Robotics can therefore become both a new edge-memory demand pool and a new source of cloud retraining / storage demand.

## 8. The robot-side power wall is battery / thermal

The data-center power bottleneck is grid / interconnection.

The robot-side bottleneck is battery energy density, runtime, charging, thermal constraints, and peak actuator demand.

Physical AI should therefore be evaluated through:

> **Useful task output / Wh**

alongside continuous runtime, recharge time, thermal headroom, maintenance intervals, and field reliability—not TOPS alone.

## 9. The real threshold from demo to mass production is manufacturing

A demo can tolerate expensive parts, manual calibration, low yield, and frequent maintenance.

Mass production cannot.

Scale thresholds include component yield, assembly time, field failure rate, maintenance interval, supply-chain stability, and unit economics.

The industrial inflection point for Physical AI therefore has to be demonstrated through manufacturing and deployment data, not demonstration videos.

## 10. China's capability structure in Physical AI differs from frontier AI

Physical AI depends heavily on motors, batteries, sensors, manufacturing, consumer-electronics supply chains, and system integration.

Those layers do not perfectly overlap with the HBM / advanced-packaging / leading-edge compute closure required for frontier AI infrastructure.

China can therefore have stronger competitiveness in robot systems and mechanical supply chains than in some frontier-AI infrastructure layers.

This is a separate industrial path and should not be reduced to one "AI chip capability" metric.

## 11. Value capture can be distributed across multiple physical layers

Long-run value capture can appear simultaneously in:

- edge compute / software platforms;
- actuators / reducers;
- sensors;
- batteries / power electronics;
- manufacturing / integration;
- cloud simulation / training infrastructure.

The robotics revolution is not fundamentally a contest over which model tops a benchmark.

It is a contest over:

> **who can convert AI capability into reliable, low-cost, mass-producible, maintainable physical work.**

## Key public sources

- NVIDIA Isaac official platform page — GR00T, simulation/training, Jetson Thor inference/control, and DGX/OVX/AGX workflow layers: https://developer.nvidia.com/isaac
- NVIDIA, 2026-06, Isaac GR00T Reference Humanoid Robot — Jetson Thor onboard compute + Isaac GR00T open platform: https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design
- NVIDIA DGX GB200 hardware guide — data-center rack power reference used only for cloud-vs-edge physical contrast: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
- Micron 2026-06-24 investor presentation — humanoid robots ~10× memory content vs average L2+ vehicle; multi-decade demand outlook: https://investors.micron.com/static-files/2354ecda-77a0-4ddd-8462-a631eb491356
