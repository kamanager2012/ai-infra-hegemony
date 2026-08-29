# P1-2 · Conditional Timeline Rewrite Map v0.2

> **Status:** Research-side rewrite map; not part of the frozen formal report.  

## 0. Derived-layer contract v0.2

This file owns **conditional grammar and milestone dependency**, not underlying factual state.

Authoritative inputs:
- geopolitical state → `05`;
- China technical closure → `09`;
- macro/public/project financing → `04A–04D`;
- scenario aggregation → `10`;
- live clearing state → `01A`.

Hard rule:

> **A timeline milestone may reference an upstream state, but must not create, upgrade or duplicate that state.**

Formal-report gate:

> **No Chapter 28 rewrite occurs from this file unless the frozen formal report is explicitly reopened.**
> **Goal:** prevent Chapter 28’s year windows from being read as a point forecast by expressing every major milestone as **condition → observable milestone → contrary signal**.

## 1. Rewrite rule

A future-year statement is acceptable only if it fits one of these forms:

```text
If [condition],
then by/within [window] we should observe [milestone].
If [contrary observable],
the milestone is delayed, weakened, or invalidated.
```

or:

```text
[Company/project] publicly targets [date].
This is a target/contractual plan, not a forecast by the report.
The report will treat [observable state transition] as confirmation.
```

Forbidden form:

> “In 2030, X happens.”

---

## 2. Phase I · 2026–2027

### T1 — Rubin / next-generation system deployment

**Condition**
- production remains on schedule;
- HBM / packaging / networking supply supports system delivery;
- customer demand remains strong.

**Milestone**
- volume deployment broadens across major customers;
- utilization and follow-on orders remain strong.

**Contrary signal**
- material shipment deferral;
- customer order reductions;
- utilization weakness;
- packaging/HBM constraints prevent expected system delivery.

### T2 — HBM4 / memory transition

**Condition**
- qualified yields and packaging integration improve;
- customer demand persists.

**Milestone**
- HBM4 moves from qualification/ramp into meaningful production deployment.

**Contrary signal**
- qualification delay;
- persistent yield limitation;
- architecture changes reduce expected HBM intensity.

### T3 — Advanced packaging constraint

**Condition**
- announced capacity actually qualifies and ramps faster than demand.

**Milestone**
- suppliers stop describing advanced packaging as a material growth constraint across multiple reporting periods.

**Contrary signal**
- lead time / allocation remains tight;
- new architectures shift rather than eliminate the bottleneck.

### T4 — Anchor Buyer delivery

**Condition**
- financing, land, power, shell and accelerator supply all progress.

**Milestone**
- contracted capacity moves through:
  secured → construction → energized → utilized.

**Contrary signal**
- schedule slip;
- financing renegotiation;
- underutilization;
- contract reduction/cancellation.

---

## 3. Phase II · 2028–2030

### T5 — Hyperscaler system-stack substitution

**Condition**
- TPU / Trainium / Maia / MTIA-class systems achieve stable production economics;
- software migration cost declines;
- workloads can move without unacceptable quality/reliability loss.

**Milestone**
- sustained share of high-value production inference and/or frontier training runs on alternative stacks;
- external customer adoption expands where applicable;
- utilization and TCO remain competitive.

**Contrary signal**
- custom systems remain narrow internal accelerators;
- migration cost remains high;
- frontier workloads stay concentrated on the dominant external stack.

### T6 — Durable HBM / packaging abundance

**Condition**
- supply expansion and architecture efficiency outrun demand growth for several periods.

**Milestone**
- lead times normalize;
- allocation pressure falls;
- pricing/contract terms become structurally less scarcity-driven.

**Contrary signal**
- new model/agent demand absorbs added capacity;
- bottleneck migrates to a new packaging/memory generation.

### T7 — Power conversion

For projects with public 2028–2030 targets:

**Condition**
- permitting, grid, generation, construction and equipment proceed.

**Milestone**
- announced/secured capacity reaches **energized and utilized** state.

**Contrary signal**
- contracted capacity remains unelectrified;
- schedule slips;
- transmission/generation bottlenecks persist.

The target date itself is never counted as confirmation.

---

## 4. Phase III · 2031–2033

### T8 — Regional system capability

**Condition**
- power + data center + chip access + software + talent remain jointly available in a region.

**Milestone**
- the region can repeatedly deploy large production systems without one critical external gate dominating delivery.

**Contrary signal**
- one or more gates remain externally binding;
- qualified second sources fail to scale.

### T9 — China production-grade parallel stack

**Condition**
- domestic/accessible compute, memory, packaging, interconnect, software and upstream continuity improve together.

**Milestone**
- multiple important production workloads run at sustained scale with acceptable utilization, reliability and economics.

**Contrary signal**
- substitution remains workload-narrow;
- key upstream service/equipment/material dependencies remain generation-binding.

### T10 — Autonomous frontier closure

**Condition**
- China crosses multiple upstream equipment/material/service gates, not just accelerator availability.

**Milestone**
- cross-generation expansion remains possible despite tighter external access.

**Contrary signal**
- leading-generation scale still depends materially on external tools/materials/services.

### T11 — Supply-chain regionalization

**Condition**
- geopolitical fragmentation persists and governments/firms pay for redundancy.

**Milestone**
- qualified regional second-source capacity becomes operational rather than merely announced.

**Contrary signal**
- global specialization remains economically dominant;
- announced redundancy stays subscale/unqualified.

---

## 5. Phase IV · 2034–2036

This window must not list four futures as if one will mechanically arrive by 2036.

Instead, 2034–2036 is a **classification window**.

### S1 classification

**If**
- supply elasticity rises;
- multi-stack production substitution scales;
- migration cost falls;
- power expansion keeps pace;
- financing remains sustainable;

**then**
- classify the observed structure closer to **Competitive Expansion**.

### S2 classification

**If**
- demand remains strong;
- dominant stacks retain advantage;
- substitution exists but remains incomplete;
- bottlenecks rotate rather than disappear;

**then**
- classify closer to **Baseline Concentration**.

### S3 classification

**If**
- multi-layer scarcity persists;
- access/quantity assurance becomes more concentrated;
- switching costs remain high;
- long-duration reservations and scarcity rents remain economically supported;

**then**
- classify closer to **Resource Hegemony**.

### S4 classification

**If**
- utilization/monetization underperforms the capital base;
- clearing prices fall;
- commitments shrink;
- financing quality deteriorates;
- impairments/refinancing stress follow;

**then**
- classify closer to **Capital Hard Landing**.

No 2036 state is preselected.

---

## 6. Cross-cutting threshold milestones

The formal Chapter 28 already names four thresholds. Phase II makes their confirmation rules explicit.

### C1 — Production substitution threshold

Confirmed only when:
- alternative stack runs important production workloads;
- at meaningful scale;
- over multiple periods;
- with acceptable utilization/reliability/economics.

A benchmark win is insufficient.

### C2 — Durable abundance threshold

Confirmed only when:
- effective supply persistently outruns priority demand;
- lead time/allocation improves;
- scarcity pricing weakens;
- the improvement survives at least one major product cycle.

A single capacity announcement is insufficient.

### C3 — Capital-cost coverage threshold

Confirmed only when:
- verified workflow economics and enterprise monetization support depreciation, operating cost and financing cost;
- not merely revenue growth without return evidence.

### C4 — Independent financing threshold

Confirmed only when:
- projects attract durable third-party capital;
- without continuously increasing supplier/sponsor support;
- while utilization and cash generation remain healthy.

---

## 7. Geopolitical conditions added to the timeline

If the frozen formal report is explicitly reopened, any Chapter 28 revision should incorporate the G1–G5 states from Phase II:

- Taiwan continuity;
- export-control regime;
- allied coordination;
- China autonomous closure;
- bloc fragmentation.

Example:

> If G2/G3 restrictions tighten while G4 closure remains incomplete, then 2028–2033 China frontier deployment milestones should be delayed/down-weighted; if G4 improves across equipment, memory, packaging and production workload simultaneously, the same milestones should be brought forward.

This is a conditional update rule, not a geopolitical forecast.

---

## 8. Macro-financial conditions added to the timeline

Every capital milestone should also carry:

- financing state;
- WACC / credit condition direction;
- sponsor balance-sheet capacity;
- refinancing dependency.

Example:

> A 2029 data-center build target remains valid only if construction progress and financing remain intact; higher rates alone do not invalidate it, but refinancing stress + schedule slippage + weak utilization do.

---

## 9. v0.2 conclusion

The main issue with a ten-year timeline is not the use of dates.

It is **dates without conditional grammar**.

Phase II therefore treats:
- 2026–2027;
- 2028–2030;
- 2031–2033;
- 2034–2036

as observation windows, while every substantive milestone is tied to:
- enabling conditions;
- observable confirmation;
- contrary evidence.

This removes the visual impression of a deterministic forecast without discarding the usefulness of a timeline.
