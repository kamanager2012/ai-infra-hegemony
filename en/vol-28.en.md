# Volume 28: Physical AI and the Real Bottlenecks in Robotics

Chinese source edition: [vol-28.md](../vol-28.md)

> Retrieval and revision cutoff: **2026-08-28**. Physical AI is analyzed here as a complete electromechanical system. No universal robot BOM percentage is treated as an industry fact.

## 1. Physical AI is not “put a large model inside a robot”

A useful robot has to solve several problems at once:

- perception;
- planning;
- control;
- actuation;
- power;
- safety;
- mechanical reliability.

The competitive unit is therefore a **system**, not one AI accelerator.

A stronger model can improve planning while the machine still fails on actuation, battery life, sensing, thermal limits, or field reliability.

## 2. Cloud training and edge control operate under different physical constraints

Robot development can place:

- large-scale simulation;
- policy training;
- foundation-model training;

inside data centers.

Real-time control operates under a different constraint set:

- latency;
- power;
- thermal limits;
- battery capacity;
- sensor-loop timing.

The architecture therefore tends toward:

> **cloud-side heavy training + edge-side compressed inference and control**

A robot cannot carry a GB200 NVL72-style **~120 kW/rack** environment on its body. The ~120 kW figure is a whole-rack power figure, not compute-only IT load. Source: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html .

Cloud compute and edge compute should be modeled as complementary layers rather than one hardware pool.

## 3. There is no universal robot BOM template

Humanoids, AMRs, industrial arms, autonomous vehicles, and drones have very different cost structures.

Their relative spending on:

- actuators;
- reducers;
- sensors;
- compute;
- batteries;

can differ materially.

This report therefore does not use a fixed “35% actuators / 20% sensors / 25% compute” template as an industry fact.

The more useful question is:

> **Which component is scarce for the specific robot architecture and deployment environment?**

## 4. Actuators and reducers can be harder to reproduce than compute

Physical-AI narratives often underweight mechanical components such as:

- frameless torque motors;
- harmonic reducers;
- planetary roller screws;
- bearings;
- precision gearboxes.

Their competitive performance depends on:

- durability;
- repeatability;
- backlash;
- noise;
- manufacturing yield;
- cost.

The industry can therefore reach a state in which compute becomes cheaper while high-precision actuation remains scarce.

Software commoditization does not automatically commoditize the mechanical system.

## 5. Sensors are another physical bottleneck

Robots can depend on combinations of:

- cameras;
- depth sensors;
- force/torque sensing;
- tactile sensing;
- IMUs;
- encoders.

Model quality translates into reliable control only if sensing is sufficiently accurate, low-latency, calibrated, and robust.

Sensor quality, calibration, and failure behavior can therefore be as important as model capability for real-world deployment.

## 6. Strategic position of edge compute

Edge platforms from NVIDIA, Qualcomm, Chinese accelerator suppliers, and others compete across:

- compute;
- software;
- power efficiency;
- developer ecosystems.

An edge platform does not need to reproduce the complete architecture of a data-center GPU rack.

But a platform that spans:

- cloud training;
- simulation;
- edge deployment;

can create a cross-layer ecosystem from model development to field execution.

The strategic question is whether developers can move efficiently from training infrastructure to the deployed robot without incurring high software and validation costs.

## 7. Physical AI can feed demand back into cloud infrastructure

A single robot may use modest edge compute relative to a training cluster.

A large robot fleet can still generate substantial demand for:

- simulation;
- training;
- synthetic data;
- video processing;
- model updates.

That creates a feedback loop:

**physical deployment  
→ more data  
→ retraining  
→ more cloud compute**

Physical AI can therefore become a new source of upstream data-center workload even when the deployed machines themselves operate under tight edge-power limits.

## 8. Power and batteries are the robot-side “third wall”

For a data center, the power bottleneck is primarily grid delivery.

For a robot, the power bottleneck is:

- battery energy density;
- thermal limits;
- runtime;
- charging.

Peak TOPS is therefore an incomplete performance metric.

A more useful engineering relationship is:

```text
Useful Task Output / Wh
```

alongside:

- continuous operating time;
- recharge time;
- heat;
- reliability.

A robot that is faster for ten minutes but cannot complete a shift has not solved the deployment problem.

## 9. Manufacturing scale determines whether a robot moves from demo to industry

A demonstration can tolerate:

- expensive parts;
- manual calibration;
- low yield;
- frequent maintenance.

Mass production cannot.

The industrial threshold depends on variables such as:

- component yield;
- assembly time;
- maintenance interval;
- field failure rate;
- unit economics.

The true inflection point for Physical AI therefore has to be demonstrated by manufacturing and deployment data, not by a polished video alone.

## 10. China has a different opportunity set in Physical AI than in frontier AI infrastructure

The Physical-AI supply chain includes many areas where China already has substantial industrial strength:

- motors;
- batteries;
- sensors;
- manufacturing;
- supply-chain integration;
- consumer electronics.

China's competitive position in robot manufacturing and electromechanical supply can therefore be stronger than its position in some frontier-AI infrastructure layers.

This is a distinct industrial pathway.

It should not be inferred from, or collapsed into, the frontier accelerator comparison.

## 11. Current judgment

Physical AI extends AI into the physical economy, but its durable bottlenecks will not sit only in GPUs.

Long-run value capture can be distributed across:

- edge compute platforms;
- actuators and reducers;
- sensors;
- batteries;
- manufacturing;
- cloud simulation and training.

The real robotics competition is not simply:

> **who has the best model?**

It is:

> **who can convert AI capability into reliable, affordable, manufacturable physical work at scale?**
