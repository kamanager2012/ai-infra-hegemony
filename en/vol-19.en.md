# Volume 19: 2026–2036 AI-Infrastructure Timeline and Milestones

Chinese source edition: [vol-19.md](../vol-19.md)

> Retrieval and revision cutoff: **2026-08-27**. The timeline advances by observable conditions, not by assuming that specific events must happen in specific years. The dates below are monitoring windows, not deterministic forecasts.

## 1. A ten-year timeline should be milestone-driven

A precise year-by-year forecast for AI infrastructure would create false certainty.

This volume therefore divides 2026–2036 into four observation phases:

- **Phase I: 2026–2027**
- **Phase II: 2028–2030**
- **Phase III: 2031–2033**
- **Phase IV: 2034–2036**

Each phase is defined by conditions that can be checked against public evidence.

The scenario variables remain anchored to the [Core Hypothesis Matrix](核心假设矩阵.en.md).

## 2. Phase I: 2026–2027 — system race and infrastructure locking

The current factual base includes:

- NVIDIA FY27 Q2 Data Center revenue: **$89.0B**;
- GAAP gross margin: **75.0%**;
- Rubin: **full production**;
- manufacturing, supply, and capacity commitments: **US$119B** as of 2026-04-26 and **US$279B** as of 2026-07-26; the Q2 filing says the latest amount is primarily tied to memory and manufacturing facilities;
- TSMC advanced-packaging tightness still limiting customer growth;
- HBM + RDIMM representing approximately **51% of 2026 DRAM bits**;
- continued hyperscaler CapEx expansion;
- power arrangements reaching the **835 MW, 1.92 GW, and 500 MW** scale.

The central question for this phase is:

> **Does demand continue to grow faster than scarce-layer supply?**

Key milestones include:

- Rubin volume deployment;
- HBM4 ramp;
- advanced-packaging expansion;
- next-generation cloud custom-silicon deployment;
- actual energization of power projects;
- whether supply commitments continue to rise. Source: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm .

## 3. Phase II: 2028–2030 — does substitution reach scale?

This phase is likely to determine the main fork between **S1 Competitive Expansion** and the more concentrated **S2/S3** paths.

### Cloud

Watch whether:

- TPU, Trainium, Maia, and MTIA gain material share in frontier training;
- internal workloads continue migrating;
- external customer adoption increases.

### Software

Watch whether:

- CUDA migration cost falls materially;
- open compiler/runtime systems become credible production alternatives;
- multi-stack deployment becomes normal for enterprises.

### Memory and packaging

Watch whether:

- HBM supply becomes materially more elastic;
- packaging is still described as a growth constraint;
- new packaging architectures increase supply flexibility.

### Power

Watch whether:

- contracted GW actually becomes energized GW;
- powered land remains scarce;
- time-to-power continues to determine deployment speed.

The critical variable is not whether alternatives exist in demos.

It is whether they operate reliably at production scale.

## 4. Phase III: 2031–2033 — geographic and industrial structure hardens

If AI infrastructure keeps expanding, competition can move upward from product roadmaps into regional infrastructure systems.

Key questions include:

- which regions combine power, data centers, and chip access most effectively;
- whether China's parallel stack closes at the frontier layer;
- whether sovereign AI creates multiple regional system ecosystems;
- whether the global supply chain remains integrated or becomes durably segmented.

At this stage, chip benchmarks become less informative than:

- total deployable compute;
- system utilization;
- energized capacity;
- cross-stack portability;
- regional supply resilience.

The competitive unit becomes an infrastructure geography, not only a chip company.

## 5. Phase IV: 2034–2036 — maturity, concentration, or clearing

By 2034–2036, the industry should provide clearer evidence for one or more of the four formal structures.

### S1 — Competitive Expansion

Multiple system stacks mature, switching costs fall, supply broadens, and the market continues expanding.

### S2 — Baseline Concentration

A small number of large platforms coexist, while scarce-layer suppliers retain high strategic value.

### S3 — Resource Hegemony

Coordination over logic, HBM, packaging, software, and power becomes more concentrated.

### S4 — Capital Hard Landing

Installed infrastructure exceeds productive demand, shifting the industry from construction competition toward utilization and cash-flow clearing.

These states can coexist by region or workload.

The timeline is therefore a monitoring structure, not a claim that the industry flips into one global state on one date.

## 6. Technology variables that should not be hard-coded by year

This report does not preassign exact future values for:

- wafer prices;
- node ASPs;
- CoWoS wafers per month;
- GW or rack counts;
- company market shares.

Those variables depend heavily on:

- yield;
- product mix;
- architecture;
- demand;
- regulation;
- capital cycles.

The timeline records **conditions and milestones**, not fake precision.

## 7. Algorithmic milestones

The next decade requires continuous monitoring of:

- memory compression;
- sparse architectures;
- quantization;
- inference scheduling;
- model routing;
- on-device capability.

If algorithmic efficiency materially lowers compute intensity, the infrastructure-demand curve changes.

But aggregate infrastructure demand weakens only if efficiency gains are not offset by greater total workload volume.

The relevant relationship remains:

> **efficiency × demand elasticity**

rather than “better algorithms automatically reduce infrastructure.”

## 8. Capital milestones

Every phase should also track:

- hyperscaler CapEx;
- depreciation;
- supply commitments;
- utilization;
- second-hand hardware prices;
- enterprise AI monetization.

The technology roadmap and the capital cycle belong on the same timeline.

A technically successful system can still fail economically if utilization and monetization lag the asset base.

## 9. Power milestones

Power should be tracked through:

- permitting;
- interconnection;
- energization;
- utilization.

The relevant question is not how many GW have been signed.

Projects such as Crane, Talen/AWS, and Kairos should move through the monitoring framework only as their physical maturity changes.

A contract should not be labeled “AI power online” before power is actually delivered and used.

## 10. Current judgment

The most important task for 2026–2036 is not predicting who wins in a particular year.

It is identifying three thresholds:

1. **Does system substitution cross the frontier-training threshold?**
2. **Does scarce-layer supply cross into durable abundance?**
3. **Does AI workload monetization cover the capital cost of the installed infrastructure base?**

Those three thresholds will do more than any fixed calendar to determine whether the industry moves toward S1, S2, S3, or S4.
