# Macro Essay 6: The Energy War and Physical Grid Constraints

Chinese source edition: [part2-06.md](../part2-06.md)

> Retrieval and revision cutoff: **2026-08-28**. Power is now a core AI-infrastructure constraint, but current evidence does not show that it has already become the single dominant bottleneck. Contracted, permitted, energized, and utilized MW remain separate states.

## 1. The macro question

Even if HBM and advanced packaging expand, an AI system cannot produce useful work until the data center can be powered.

The key question is therefore:

> **Has electricity become a third quota alongside advanced packaging and HBM—and if so, how much of the announced or contracted power is actually executable?**

The current judgment is:

- power is already a core constraint;
- it is not yet proven to be the only dominant constraint;
- SMRs are better understood as long-duration supply options than as current power.

## 2. Why rack density changes the problem

NVIDIA's GB200 NVL72 rack-level hardware guidance is approximately **120 kW/rack**. Source: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html

As a **D-grade scenario arithmetic**, 500 × 120 kW ≈ **60 MW of rack-level full-load power**. This is not compute-only IT load, not a shipment count, and not evidence that 500 racks or 60 MW are already deployed or energized.

The constraint therefore moves beyond an electricity bill.

A project needs:

- transmission;
- substations;
- transformers;
- interconnection;
- cooling;
- permits;
- firm generation.

Power becomes a delivery condition.

## 3. Three representative power paths

### Microsoft / Constellation — ~835 MW restart

The 20-year PPA supports the restart of the former Three Mile Island Unit 1, now the Crane Clean Energy Center. Source: https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs

The project remains dependent on regulatory and restart execution.

The ~835 MW figure is a plant/project capacity anchor, not proof of 835 MW of live AI load.

### Talen / AWS — up to 1.92 GW

The revised arrangement can scale to **1.92 GW**. Source: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm

Talen's 2026 Q2 10-Q states that the transition to the revised AWS PPA **occurred in April 2026**. That later filing supersedes the earlier 2025 10-K's **spring-2027 full-transition expectation** as the current transition-state marker. The older filing remains useful for the original delivery-ramp context. April 2026 still does not mean the full **1,920 MW** contract quantity had already been physically delivered, energized, or utilized.

The monitoring question is now:

- how quickly capacity ramps;
- how much is energized;
- how much load appears;
- how highly it is utilized.

### Google / Kairos — up to 500 MW

The published development clock is more specific: **Hermes 2 up to 50 MWe in 2030**, followed by a fleet **up to 500 MWe by 2035**. Source: https://www.kairospower.com/google

This is a longer-duration advanced-nuclear path.

It should be treated as future supply optionality, not as current AI power.

## 4. Why the three numbers cannot be added into live AI capacity

The three projects occupy different states:

- restart + regulatory process;
- commercial structure converted, capacity ramping;
- long-duration advanced-nuclear development.

A **D-grade arithmetic addition** of 835 MW + 1.92 GW + 500 MW can produce a nominal project total, but the terms represent different project states and maturity clocks.

It does not produce an operating AI-load total.

The correct power framework is:

1. Announced
2. Contracted
3. Permitted
4. Energized
5. Utilized

The economic value increases as a project moves down that sequence.

## 5. Grid queues are evidence of congestion, not deliverable compute

Large interconnection queues contain:

- generation;
- storage;
- loads;
- duplicate or speculative applications;
- projects that later withdraw.

Therefore:

```text
Queue MW ≠ Deliverable AI MW
```

What matters to an AI campus is the subset of grid infrastructure that can actually deliver high-voltage power on the required timetable.

The bottleneck is local and temporal.

National installed generation is not a substitute for a missing transformer or interconnection permit at a specific node.

## 6. Power creates a duration mismatch

AI hardware can turn over on a multi-year technology clock.

Power projects and contracts can last much longer.

That creates the risk:

> **short-duration compute demand financed or supported by long-duration infrastructure**

Under sustained growth, secure power is a moat.

Under S4 Capital Hard Landing, the same obligation can become a stranded long-duration asset.

Power therefore belongs in both the physical-bottleneck model and the capital-risk model.

## 7. Rolling Bottleneck Cascade

The system can move through several limiting layers:

**HBM/packaging tight  
→ more supply comes online  
→ more racks seek deployment  
→ grid/interconnection becomes tighter  
→ deployment slows  
→ utilization and next hardware orders weaken**

The bottleneck can rotate.

This is why the report avoids declaring any one scarce layer permanently dominant.

## 8. What would prove that power has become the dominant bottleneck?

The evidence would need to show several of the following:

- widespread deployment delays caused specifically by power;
- persistent energized-capacity shortfalls;
- idle delivered hardware waiting for interconnection;
- next-generation orders delayed because projects cannot be energized;
- power constraints explicitly cited by major buyers as a binding growth limit.

As of August 2026, power is a core constraint but not yet proven to dominate the whole system.

The key metric is not:

> “How many GW have been announced?”

It is:

> **How many MW can be permitted, energized, and continuously used before the hardware generation changes?**


## Key public sources for this essay

- NVIDIA DGX GB200 hardware guide — ~120 kW/rack: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
- Constellation / Microsoft Crane restart — 20-year PPA, ~835 MW; official release says significant investments: https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
- Talen 2026 Q2 10-Q — transition occurred in April 2026; up to 1,920 MW: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
- Talen 2025 10-K — prior spring-2027 transition expectation (superseded as current state); original delivery-ramp context: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
- Kairos / Google — Hermes 2 up to 50 MWe in 2030; fleet up to 500 MWe by 2035: https://www.kairospower.com/google
