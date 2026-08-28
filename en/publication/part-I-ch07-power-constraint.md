# Part I · Chapter 7: From 120 kW Racks to GW-Scale Power Constraints

> **Publication-layer chapter.** Recompiled from [Volume 13](../vol-13.en.md), [Volume 35](../vol-35.en.md), and [Macro Essay 06](../part2-06.en.md). This chapter compresses the power argument into one chain: **rack power density → project state → Time-to-Power → utilization / capital consequences**.

## 1. Why power has moved from operating cost to infrastructure quota

Once rack-scale AI systems reach roughly **120 kW/rack**, electricity is no longer merely an operating expense. It becomes a constraint on whether systems can be deployed and utilized on schedule.

NVIDIA's official documentation for GB200/GB300 NVL72-class racks gives an approximately **120 kW/rack** full-rack power figure. A clearly labeled **D-grade scenario calculation** is therefore:

> 500 racks × 120 kW/rack = **60 MW of rack-level full-load power**

This is an order-of-magnitude calculation. It does not mean any specific campus has deployed 500 racks, and it does not include complete facility overhead. What it demonstrates is that deployments measured in hundreds of racks quickly create local loads measured in tens of MW, pulling substations, transmission, permitting, cooling, and firm generation into the delivery chain.

The critical physical layers of AI infrastructure therefore extend beyond wafers, HBM, and advanced packaging to include **powered land / grid interconnection / substations / firm MW / cooling**.

## 2. Power analysis requires a state machine, not headline-GW addition

Power projects should be separated into at least five states:

> **Announced → Contracted → Permitted → Energized → Utilized**

A 1 GW PPA cannot be rewritten as "1 GW of AI compute online." A 500 MW development target cannot be converted directly into an active rack count. The real economic value of a project depends on how far it has advanced from announcement toward high-utilization delivery—not on the maximum MW/GW in a headline.

## 3. Three representative paths operate on very different clocks

### 3.1 Microsoft / Constellation: restarting an existing ~835 MW nuclear asset

Microsoft and Constellation entered a **20-year PPA** supporting the restart of the former Three Mile Island Unit 1 as the Crane Clean Energy Center, with an approximately **835 MW** public capacity anchor.

The case shows how hyperscaler demand can support a large existing power asset returning to service.

But 835 MW is a project / unit-capacity anchor, not evidence that 835 MW is already being delivered in real time to AI data centers. The project still sits on regulatory, repair, restart, interconnection, and commercial-operation clocks.

Constellation's official release states that the restart requires significant investment but does **not** disclose a US$1.6B restart CapEx figure. That number therefore does not enter this chapter's fact layer.

### 3.2 Talen / AWS: a revised PPA of up to 1,920 MW

The Talen/AWS revised PPA has a full contract quantity of **up to 1,920 MW** and runs through 2042.

Talen's 2026 Q2 10-Q states that the transition to the revised AWS PPA **occurred in April 2026**. An earlier 2025 10-K had stated that **full transition was expected in spring 2027**.

April 2026 can therefore be used as the current disclosed status of the revised-PPA transition. It **cannot** be interpreted as proof that every physical conversion, transmission modification, and full-delivery step had already been completed.

The relevant forward indicators are the capacity ramp, energized MW, AWS load, and utilization.

This case shows that regulation and commercial structure can change the delivery path for power without making large-scale AI electricity demand disappear.

### 3.3 Google / Kairos: 50 MWe in 2030 and up to 500 MWe by 2035

The Google/Kairos public timeline is much longer: **Hermes 2 up to 50 MWe in 2030**, followed by a fleet of **up to 500 MWe by 2035**.

This is better understood as a long-duration supply option, industrial-learning path, and capacity hedge than as spot power that can be called on in 2026–2028.

The near-term value of SMRs therefore lies mainly in future optionality; they should not be used to erase today's interconnection, transformer, and powered-site constraints.

## 4. These three projects cannot be added into "3.255 GW of active AI power"

Mechanically adding approximately 835 MW, up to 1.92 GW, and up to 500 MWe produces a nominal total but not a usable AI-load number.

| Project | Nominal scale | Primary status |
|---|---:|---|
| Crane / Microsoft | ~835 MW | restart + regulatory process |
| Talen / AWS | up to 1,920 MW | revised-PPA transition / ramp |
| Kairos / Google | 50 MWe in 2030; up to 500 MWe by 2035 | long-duration development |

The three paths represent restarting an existing large generator, restructuring the commercial/grid relationship between a large load and existing generation, and developing next-generation nuclear supply. Their technology maturity, permitting clocks, and utilization dates are not comparable.

## 5. Grid queues are evidence of congestion, not a measure of "AI power shortage"

Berkeley Lab's Queued Up data show that active U.S. generation/storage interconnection requests peaked near **2,600 GW at the end of 2023** and stood at approximately **2,061 GW at the end of 2025**.

These numbers cannot be converted into "the United States lacks 2,061 GW of data-center power." The queue is primarily generation/storage projects and includes projects that may withdraw, duplicate one another, or experience long delays.

The narrower supported conclusion is that **interconnection and transmission buildout can take years, making Time-to-Power a real constraint.**

What matters for AI system delivery is how many MW a specific region can actually deliver inside a specific hardware-generation window—not the total GW sitting in a national queue.

## 6. Time-to-Power is becoming a system-competition variable

Advanced chips can advance on monthly and quarterly product clocks. Power infrastructure often advances on multi-year clocks.

That creates a variable comparable in importance to the chip roadmap:

> **Time-to-Power**

Projects with existing grid interconnection, powered land, substation / transformer capacity, firm generation, and executable permitting paths gain a timing advantage.

Hyperscaler competition is therefore not only about who acquires more accelerators. It is also about:

> **who can energize the next 50 MW / 100 MW / 500 MW of systems sooner.**

## 7. Power and semiconductor bottlenecks can rotate

AI infrastructure does not have one permanent bottleneck.

One possible **Rolling Bottleneck Cascade** is:

> HBM / advanced packaging tight → hardware delivery constrained → manufacturing supply expands → more racks reach sites → power / interconnection becomes binding → deployment and utilization slow → next-cycle hardware orders / commitments decelerate

The reverse is also possible. If power infrastructure is built far ahead of workload demand, the problem can shift from scarcity to low utilization and weak capital returns.

"Power is now a core constraint" and "power is not yet the sole dominant bottleneck" can therefore both be true.

## 8. Power contracts and hardware operate on mismatched durations

AI servers have shorter technological and economic lives than major power assets and long-duration PPAs.

Crane involves a **20-year PPA**, while compute hardware will turn over much faster. This creates a classic duration mismatch:

> **shorter-cycle compute asset vs. longer-cycle power / infrastructure asset**

In high-demand scenarios, long-duration power access can be a moat. In S4 Capital Hard Landing, the same long-duration obligation can become a burden.

Power contracts therefore need to be evaluated through duration, ramp, take-or-pay / cancellation terms, project execution, utilization, and residual value.

## 9. What evidence would show that power has become the dominant bottleneck

Power should be upgraded from "one of the core constraints" to "the dominant constraint" only if several signals appear together:

- major buyers repeatedly disclose power/interconnection as the binding growth ceiling;
- delivered hardware sits idle waiting to be energized;
- energized capacity persistently lags deployment plans;
- next-generation orders are delayed by power constraints;
- Time-to-Power remains a decisive differentiator for high-value powered sites;
- utilization and capital returns deteriorate systematically because of power-delivery timing.

As of August 2026, public evidence supports a narrower conclusion:

> **Power has joined HBM and advanced packaging as a core physical constraint, but the evidence is not yet sufficient to show that power alone dominates the entire AI-infrastructure expansion rate.**

## Key public sources

- NVIDIA DGX GB200 hardware guide — ~120 kW/rack: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
- Constellation / Microsoft Crane restart — 20-year PPA, ~835 MW: https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
- NRC — Crane / former Three Mile Island Unit 1 regulatory information: https://www.nrc.gov/info-finder/reactors/ccec
- Talen 2026 Q2 10-Q — revised AWS PPA transition occurred in April 2026; up to 1,920 MW: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
- Talen 2025 10-K — full transition expected spring 2027: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
- Kairos / Google — Hermes 2 up to 50 MWe in 2030; fleet up to 500 MWe by 2035: https://www.kairospower.com/google
- Berkeley Lab, Queued Up 2026 — end-2025 active queue ~2,061 GW; end-2023 peak near 2,600 GW: https://emp.lbl.gov/news/backlog-power-plants-seeking-transmission-grid-connection-eased-somewhat-2025-amidst
