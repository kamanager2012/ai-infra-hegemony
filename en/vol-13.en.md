# Volume 13: The AI Energy War — From 120 kW Racks to GW-Scale Power Commitments

Chinese source edition: [vol-13.md](../vol-13.md)

> Retrieval and revision cutoff: **2026-08-28**. This volume separates announced, contracted, permitted, energized, and utilized power. The size of a PPA is not the same thing as live AI load.

## 1. Why power is becoming an infrastructure quota rather than only an operating cost

Once AI rack power density reaches roughly **120 kW per rack**, data-center construction changes qualitatively.

**D-grade scenario arithmetic:** about 500 racks at **120 kW per rack** represent approximately **60 MW of rack-level full-load power**. This is a scale test, not evidence that 500 racks or 60 MW are already deployed or energized. The 120 kW figure is an NVIDIA rack-power figure that includes compute nodes and rack components; it should not be relabeled as compute-only IT load.

AI-infrastructure delivery therefore depends not only on:

- GPUs;
- HBM;
- advanced packaging;

but also on:

- grid connection;
- substations;
- transformers;
- transmission;
- cooling;
- firm power;
- permits.

Power is becoming a core scarce layer in the AI infrastructure system.

## 2. Contracted MW is not energized load

Power analysis has to distinguish at least five states:

1. announced capacity;
2. contracted capacity;
3. permitted capacity;
4. energized capacity;
5. utilized load.

These states are not interchangeable.

A 1 GW PPA cannot be restated as “1 GW of AI compute already online.”

Likewise, planned data-center power cannot be mechanically converted into active GPU counts.

The relevant question is always: **how far has the project moved from contract to executable load?**

## 3. Microsoft / Constellation: approximately 835 MW tied to a nuclear restart

Microsoft and Constellation's long-term PPA is associated with the restart of an approximately **835 MW** nuclear unit.

The strategic significance is not that Microsoft already has 835 MW of live AI load.

It is that a hyperscaler is willing to use long-duration demand to support the return of an existing nuclear asset.

The mechanism is:

> **large compute demand → long-duration offtake → financeable power asset → dedicated capacity path**

Actual delivery still depends on:

- regulatory approval;
- restart schedule;
- grid delivery;
- commercial operation;
- realized utilization.

The contract therefore represents a power-supply strategy, not a completed data-center load measurement.

## 4. Talen / AWS: a long-duration arrangement expandable to 1.92 GW

The revised Talen/AWS PPA can expand to as much as **1.92 GW**. Source: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm

Talen's 2026 Q2 10-Q states that the transition to the revised AWS PPA **occurred in April 2026**. Its earlier 2025 10-K had described the process as beginning in spring 2026 with **full transition expected in spring 2027**. April 2026 should therefore be treated as a revised-PPA transition status update, not as proof that every physical conversion and power-delivery step was complete.

The relevant monitoring questions remain:

It is no longer whether the conversion will occur. It is:

- how the contract ramps;
- how many megawatts become energized;
- how much data-center load actually appears;
- how highly that capacity is utilized.

This distinction is central to the report's power framework: legal structure can be complete while physical load is still ramping.

## 5. Google / Kairos: up to 50 MWe in 2030, then up to 500 MWe by 2035

The public Google/Kairos path is **Hermes 2 up to 50 MWe in 2030**, followed by a fleet **up to 500 MWe by 2035**.

This path differs fundamentally from restarting an existing nuclear plant.

SMRs are a longer-duration supply option with:

- development risk;
- regulatory risk;
- first-of-a-kind execution risk;
- a later delivery clock.

Their strategic value is closer to:

- a future option;
- a long-duration capacity hedge;
- an industrial-learning path.

SMR capacity should therefore not be used to “solve” 2026–2028 rack-deployment pressure on paper.

## 6. Why power creates a new form of resource lock-in

Semiconductor scarcity is tied to technology generations.

Power scarcity is tied to geography, permitting, and executable infrastructure.

When a hyperscaler secures:

- powered land;
- grid interconnection;
- firm generation;
- substation capacity;

those assets are difficult for a competitor to reproduce quickly in the same location.

AI resource competition is therefore expanding from:

> **wafer / HBM / packaging**

to:

> **powered site / grid / firm MW**.

This is a distinct form of capacity reservation with a different time constant.

### Key public sources
- NVIDIA GB200/NVL72 rack power (~120 kW/rack): https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
- Constellation / Microsoft Crane restart (~835 MW): https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
- Talen 2026 Q2 10-Q — revised AWS PPA up to 1,920 MW; transition occurred in April 2026: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
- Talen 2025 10-K — full transition expected in spring 2027; delivery ramp to full volume no later than 2032: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
- Kairos / Google — Hermes 2 up to 50 MWe in 2030; fleet up to 500 MWe by 2035: https://www.kairospower.com/google

## 7. How power can interrupt semiconductor expansion

If semiconductor supply continues to expand but data centers cannot be energized on schedule, the system can move through the following sequence:

1. delivered hardware waits for deployment;
2. utilization weakens;
3. depreciation begins before matching revenue appears;
4. next-generation orders are delayed;
5. supply-commitment growth slows.

This is a **Rolling Bottleneck Cascade**:

**packaging bottleneck eases  
→ power bottleneck rises  
→ deployment rate slows  
→ hardware-order growth slows**

The limiting constraint can therefore migrate over time.

More chips do not guarantee more usable compute if power-on becomes the next gate.

## 8. National electricity supply is not the same as locally usable AI power

The binding constraint for an AI data center is often a local node rather than a national energy total.

A country can have ample installed generation while a specific campus still lacks deliverable power on the required schedule. For example, a **100 MW-class** requirement still has to be verified project by project through interconnection, substation, transmission, permitting, and construction milestones.

The critical variables are local:

- transformer capacity;
- transmission corridors;
- interconnection queues;
- permits;
- construction;
- firm generation.

AI power constraints are therefore primarily **node and time problems**, not simple national installed-capacity problems.

## 9. Power contracts and hardware depreciation run on different clocks

AI servers can turn over rapidly over a period of several years.

Large power infrastructure and long-duration PPAs can outlast fast-turnover compute assets; the Microsoft/Constellation Crane arrangement, for example, is a **20-year PPA**.

That creates a duration mismatch:

> **shorter-lived compute assets vs. longer-lived power and infrastructure obligations**

Under sustained demand growth, long-duration power access can be a moat.

Under S4 Capital Hard Landing, the same asset can become a long-duration liability.

The value of a power contract therefore depends on utilization over time, not only on the nominal number of megawatts reserved.

## 10. Current judgment

As of **August 2026**:

- power is already a core AI-infrastructure constraint;
- large hyperscalers are using long-duration contracts to reserve future MW;
- contracted capacity is much larger than the AI load that can be confirmed as energized and utilized;
- nuclear restarts, front-of-the-meter PPAs, and SMR development sit on different maturity clocks;
- the evidence is not yet sufficient to conclude that power has already stopped AI expansion.

The most important forward indicators are:

- energized MW;
- time to power;
- rack utilization;
- power-related deployment delays;
- next-round hardware commitments.

The energy contest is not about who announces the largest GW number.

It is about:

> **who can convert contracted capacity into sustained, highly utilized compute on an executable timetable.**
