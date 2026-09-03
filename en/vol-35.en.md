# Volume 35: AI Power Constraints — 835 MW, 1.92 GW, and 500 MW Across Three Delivery Paths

Chinese source edition: [vol-35.md](../vol-35.md)

> **Publication role:** [Volume 13](vol-13.en.md) explains why power becomes an independent AI-infrastructure quota. This volume is the project-evidence companion, comparing Crane, Talen/AWS, and Kairos/Google across Contracted, Permitted, Energized, and Utilized states.

> Retrieval and revision cutoff: **2026-08-28**. This volume tracks power through five states: Announced, Contracted, Permitted, Energized, and Utilized. Nameplate or contracted capacity is never treated as live AI load.

## 1. Power must be analyzed by project state

AI data-center power discussions often mix three different questions:

- how many MW or GW were announced;
- how many were written into contracts;
- how many are actually operating.

This report uses five states:

1. **Announced**
2. **Contracted**
3. **Permitted**
4. **Energized**
5. **Utilized**

Only by separating those states can power be compared meaningfully with hardware shipments, CapEx, and workload utilization.

## 2. Rack-power input anchor: scale arithmetic only

NVIDIA rack documentation places GB200 NVL72-class full-rack power at roughly **120 kW/rack**. This volume uses that figure only as a scale anchor; the liquid-cooling, busway, transformer, and high-density distribution implications are developed in [Volume 13](vol-13.en.md).

**D-grade scenario arithmetic:** 500 × 120 kW = **60 MW of rack-level full-load power**. It is not evidence that a campus has deployed 500 racks, it excludes full facility overhead, and it does not establish that a 100 MW campus is operating.

## 3. Microsoft / Constellation: approximately 835 MW tied to a restart PPA

Microsoft and Constellation signed a 20-year PPA supporting the restart of the former Three Mile Island Unit 1, renamed the Crane Clean Energy Center.

The public project scale is approximately **835 MW**.

### Current state

- Contract: signed;
- restart project: progressing;
- regulatory process: ongoing;
- commercial operation: still dependent on required approvals and restart execution;
- actual AI load: cannot be inferred from the 835 MW nameplate figure.

The strategic significance is:

> **a hyperscaler is willing to provide long-duration demand support for the return of a large existing nuclear asset.**

The PPA is evidence of infrastructure reservation, not evidence that 835 MW of AI load is already online.

## 4. Talen / AWS: full contract quantity up to 1,920 MW under the revised PPA

The revised Talen/AWS PPA has a **full contract quantity up to 1,920 MW** through 2042.

The important status change is already known:

> **Talen's 2026 Q2 10-Q states that the transition to the revised AWS PPA occurred in April 2026. That later filing supersedes the earlier 2025 10-K's spring-2027 full-transition expectation as the current transition-state marker. The older filing remains useful for delivery-ramp context. April 2026 still does not mean the full 1,920 MW contract quantity had already been physically delivered, energized, or utilized.**

The monitoring questions remain:

- capacity ramp;
- transmission delivery;
- energized load;
- actual AWS data-center demand;
- utilization.

This path represents a long-duration commercial relationship between large data-center demand and existing nuclear generation through the grid/front-of-the-meter structure.

## 5. Google / Kairos: up to 500 MW of SMR development

The Google/Kairos path is more specific: **Hermes 2 is planned for up to 50 MWe in 2030**, followed by a fleet delivering **up to 500 MWe by 2035**.

Its maturity is different from the first two projects:

- it is an advanced-nuclear development path;
- commercial deployment is on a longer clock;
- current energized AI load cannot be inferred from the development target.

The 500 MW figure is therefore best understood as:

> **a future supply option**

rather than current power availability.

## 6. The three project numbers cannot be added into “live AI power”

Adding:

**835 MW + 1.92 GW + 500 MW**

produces a nominal total of **3.255 GW**.

It does **not** produce 3.255 GW of operating AI load.

The projects sit at different stages:

| Project | Nominal scale | Core state |
|---|---:|---|
| Microsoft / Constellation | ~835 MW | restart + regulatory process |
| Talen / AWS | up to 1,920 MW | 2026 Q2 10-Q: transition occurred in April 2026 and supersedes the prior spring-2027 transition expectation; 2025 10-K still provides the original ramp-to-full-volume no-later-than-2032 context |
| Google / Kairos | Hermes 2 up to 50 MWe in 2030; fleet up to 500 MWe by 2035 | long-duration development |

This is why energy analysis has to follow project state instead of adding headline capacity.

### Public sources
- Constellation / Microsoft Crane: https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
- Talen 2026 Q2 10-Q: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
- Google / Kairos: https://www.kairospower.com/google

## 7. Grid queues are not the same as deliverable shortage

Large interconnection queues demonstrate intense demand for grid access.

But queue data can contain:

- generation;
- storage;
- load;
- duplicate applications;
- projects that later withdraw.

Therefore:

```text
Queue MW ≠ Deliverable AI MW
```

The variables that matter for actual AI delivery are:

- time to interconnect;
- transmission;
- transformer availability;
- permitting;
- physical energization.

Queue size is evidence of congestion and demand for access, not a direct measure of executable AI power.

## 8. Time-to-Power is becoming a competitive variable

AI hardware can move through product generations in months or a few years.

Large power infrastructure generally moves more slowly.

Projects that already possess:

- powered land;
- existing grid connection;
- firm generation;
- fast permitting;

can therefore gain a material time advantage.

This is **Time-to-Power**.

Hyperscaler competition increasingly depends not only on:

- compute;
- chips;
- networks;

but also on:

> **how quickly another 100 MW can actually be energized.**

## 9. Semiconductor and power bottlenecks can rotate

When CoWoS or HBM is tight, hardware is the bottleneck.

If hardware supply expands but grid delivery lags, power can become the next bottleneck.

If power catches up but workload demand is insufficient, utilization becomes the constraint.

This is the practical form of the **Rolling Bottleneck Cascade**.

The limiting layer can migrate:

**manufacturing → power → utilization**

and later move again as conditions change.

## 10. Long-duration power contracts are also financial commitments

A PPA is both:

- a supply hedge;
- a financial obligation.

Under high-demand scenarios, secure MW can be a moat.

Under **S4 Capital Hard Landing**, long-duration power commitments can become burdensome if utilization falls.

Power contracts therefore need to be evaluated through:

- duration;
- take-or-pay structure;
- ramp profile;
- utilization;
- underlying project risk.

The nominal GW figure is only the first line of the analysis.

## 11. Current judgment

As of **August 2026**, the evidence supports four conclusions:

- AI racks have reached roughly 120 kW-class power density;
- hyperscalers are signing 500 MW-to-GW-scale long-duration power arrangements;
- the 2026 Q2 10-Q records the revised-PPA transition in April 2026, but that is not treated as proof that every physical transition or delivery step was complete;
- announced and contracted capacity remains much larger than the AI load that can be confirmed as utilized.

Power is therefore already a strategic scarce layer in AI infrastructure.

The most useful metric is not:

> “How many GW have been announced?”

It is:

> **How many MW have been permitted, energized, and then used continuously by high-utilization AI workloads?**


### Key public sources
- NVIDIA GB200/NVL72 rack power (~120 kW/rack): https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
- Constellation / Microsoft Crane restart (~835 MW): https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
- Talen 2026 Q2 10-Q — revised AWS PPA up to 1,920 MW; transition occurred in April 2026: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
- Talen 2025 10-K — prior spring-2027 transition expectation (superseded as current state); full-volume ramp no later than 2032: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
- Kairos / Google — Hermes 2 up to 50 MWe in 2030; fleet up to 500 MWe by 2035: https://www.kairospower.com/google
