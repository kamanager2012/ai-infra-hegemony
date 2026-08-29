# Phase II · Decision Invariants v0.1

> **Status:** Research-side strategic layer; not part of the frozen 32-chapter formal report.  
> **Goal:** identify low-regret principles that remain valid across S1–S4, rather than giving one strategy per scenario.

## 1. What counts as a decision invariant

A decision invariant must satisfy all four conditions:

1. **Cross-scenario robustness** — it remains directionally useful under S1, S2, S3 and S4;
2. **Observable implementation** — an organization can tell whether it is actually following the principle;
3. **No hidden point forecast** — it does not require knowing the 2030/2036 winner in advance;
4. **Reversibility / optionality** — it reduces the cost of being wrong when the scenario changes.

An invariant is not:

- “buy more GPUs”;
- “multi-cloud everything”;
- “assume AI demand keeps growing”;
- “avoid long-duration assets”;
- “diversify every supplier.”

Those are scenario-dependent choices.

---

# 2. Invariant 1 — Optimize verified workflow economics, not model-unit price

Across every scenario, the economic unit that matters is:

> **cost per verified successful workflow outcome**

Why it survives S1–S4:

- **S1:** cheaper/more portable compute still has to produce accepted outcomes;
- **S2:** platform concentration does not remove the need for workload ROI;
- **S3:** scarce capacity makes outcome-level allocation even more important;
- **S4:** cheap clearing compute is only valuable if real workflows can absorb it.

Decision rule:

> Do not increase long-duration compute commitment faster than verified workflow demand and accepted-outcome economics can justify.

Observable implementation:
- VSWO count;
- cost per VSWO;
- human review minutes;
- retry/remediation;
- cycle time;
- utilization.

---

# 3. Invariant 2 — Preserve an executable second path

The primary stack can be highly concentrated for efficiency.

The invariant is not “split spend evenly.”

It is:

> **maintain at least one second path that has been tested in production or production-like conditions.**

This can mean:
- alternative model/provider;
- alternative cloud;
- alternative accelerator/runtime;
- portable data/model formats;
- open interfaces;
- validated recovery path.

Why it survives S1–S4:

- **S1:** second paths create bargaining power and exploit competition;
- **S2:** they prevent dependence from becoming irreversible;
- **S3:** they reduce scarcity/lock-in exposure even if the main stack dominates;
- **S4:** they improve access to cheaper/repriced capacity after clearing.

A second path that exists only in procurement slides is not optionality.

---

# 4. Invariant 3 — Match commitment duration to demand certainty

The report’s most durable capital principle is:

> **the less certain the workload, the shorter and more reversible the commitment should be.**

Long-duration reservation is rational only when:
- workload is production-grade;
- utilization is observable;
- demand duration is credible;
- capital cost can be covered.

This applies to:
- accelerators;
- data-center leases;
- power contracts;
- capacity reservations;
- project finance.

Why it survives S1–S4:

- S1/S2 may reward long commitments for highly certain workloads;
- S3 can make early reservation strategically valuable;
- S4 punishes overcommitment.

The invariant is **duration matching**, not “always stay flexible.”

---

# 5. Invariant 4 — Separate asset clocks

AI infrastructure contains different economic lives:

> accelerator/server → network/cooling → data-center shell → grid/generation/PPA

Never evaluate them as one homogeneous “AI asset.”

Required questions:
- demand duration;
- accounting life;
- economic life;
- refinancing maturity;
- transferability;
- residual value.

Why it survives S1–S4:
- the relative attractiveness changes by scenario;
- duration mismatch remains dangerous in all scenarios.

This is especially important when short-lived compute demand is financed with long-lived fixed obligations.

---

# 6. Invariant 5 — Stage-gate physical capacity

For every major infrastructure commitment use:

> **Announced → Contracted/Secured → Permitted → Construction → Energized → Utilized**

Never collapse those states.

Why it survives S1–S4:
- prevents false abundance in S1/S2;
- prevents false scarcity certainty in S3;
- prevents overstating stranded assets in S4 before physical delivery.

Capital should be released against state transitions where possible.

---

# 7. Invariant 6 — Measure scarce layers separately

Do not infer:

> revenue share → wafer share → packaging allocation → HBM share → power access

Each physical layer has:
- its own denominator;
- its own elasticity;
- its own customer concentration;
- its own lead time;
- its own substitution path.

Why it survives S1–S4:
- the bottleneck can migrate;
- one layer can clear while another remains scarce.

Decision consequence:

> allocate engineering and capital attention to the currently binding layer, not to an inherited narrative about “the AI bottleneck.”

---

# 8. Invariant 7 — Track buyer economics separately from seller economics

A seller can recognize strong revenue while the buyer carries years of utilization and depreciation risk.

Therefore always maintain two clocks:

> **seller economics**  
> vs.  
> **buyer ROI / utilization economics**

Why it survives S1–S4:
- S1/S2 can sustain both;
- S3 can strengthen sellers while stressing buyers;
- S4 often begins with buyer ROI deterioration before seller revenue collapses.

Do not use high seller margin as proof of healthy buyer-side return.

---

# 9. Invariant 8 — Financing quality matters as much as financing quantity

More capital is not automatically stronger demand.

Always distinguish:
- customer operating cash flow;
- third-party risk capital;
- debt;
- supplier equity;
- guarantees;
- credit enhancement;
- refinancing dependency.

The invariant:

> **prefer demand that can increasingly finance itself from independent workload cash flow over demand that requires rising sponsor/supplier support.**

Why it survives S1–S4:
- healthy financing improves expansion in S1–S3;
- deteriorating financing independence is an early S4 warning.

---

# 10. Invariant 9 — Trigger decisions by state changes, not calendar dates

Do not act because “it is 2030.”

Act because observable thresholds changed:

- production substitution;
- durable abundance;
- capital-cost coverage;
- financing independence;
- Time-to-Power;
- geopolitical continuity;
- clearing signals.

Why it survives S1–S4:
- scenario transitions rarely align with round years;
- calendar-based decisions create false precision.

This is the operational form of the report’s conditional timeline.

---

# 11. Invariant 10 — Build resilience where the cost of failure justifies it

Redundancy is not automatically efficient.

The decision rule is:

> **buy redundancy when expected continuity value exceeds redundancy cost.**

Apply to:
- supplier qualification;
- geographic distribution;
- power;
- cloud/runtime;
- data formats;
- critical maintenance/service.

Why it survives S1–S4:
- S1 can make redundancy cheaper;
- S2/S3 can make it strategically valuable;
- S4 can make excessive duplication expensive.

The invariant is **priced resilience**, not maximal redundancy.

---

# 12. Invariant 11 — Keep falsification variables next to every major commitment

Every strategic commitment should define, before deployment:

- what would confirm the thesis;
- what would weaken it;
- what would trigger reduction;
- what would trigger expansion.

Examples:
- utilization floor;
- VSWO economics;
- lead-time normalization;
- financing-cost threshold;
- customer renewal;
- second-path performance;
- project state transition.

Why it survives S1–S4:

> decisions become updateable without requiring the original narrative to remain true.

This is the operational use of F→H→M→S→X.

---

# 13. Invariant 12 — Prefer transferability over perfect optimization when uncertainty is high

When uncertainty is high, an asset/system that is slightly less optimized but:
- portable;
- redeployable;
- resaleable;
- compatible;
- multi-customer capable

can have higher strategic value.

When uncertainty is low and demand is durable, optimization can dominate.

The invariant:

> **the value of transferability rises with uncertainty and duration.**

This applies to:
- compute contracts;
- data centers;
- power;
- software architecture;
- financing structures.

---

# 14. Actor map

## Enterprise / AI application buyer

Highest-value invariants:
1. VSWO economics;
2. executable second path;
3. commitment-duration matching;
4. trigger-based decisions.

## Model company / Anchor Compute Buyer

Highest-value invariants:
1. verified workload growth;
2. commitment-duration matching;
3. financing independence;
4. power/compute state-gating;
5. transferability.

## Hyperscaler

Highest-value invariants:
1. buyer ROI separated from seller economics;
2. portfolio of system stacks;
3. utilization before next capital step;
4. physical-layer bottleneck measurement;
5. asset-clock matching.

## Semiconductor / system supplier

Highest-value invariants:
1. track end-demand quality;
2. avoid treating prepayment/financing support as identical to organic demand;
3. preserve product/customer optionality;
4. distinguish short-cycle clearing from structural demand loss.

## Data-center / power / infrastructure developer

Highest-value invariants:
1. state-gated capital release;
2. duration matching;
3. transferability;
4. financing independence;
5. customer concentration control.

## Capital provider

Highest-value invariants:
1. buyer economics;
2. residual value;
3. refinancing dependence;
4. asset duration;
5. independent third-party risk bearing.

## Policymaker

Highest-value invariants:
1. system-level continuity rather than one-fab metrics;
2. priced resilience;
3. qualified second sources;
4. power + semiconductor + capital clocks;
5. avoid confusing announced capacity with operational capability.

---

# 15. What is genuinely scenario-invariant vs. scenario-dependent

| Decision | Invariant? | Why |
|---|---|---|
| Measure cost per VSWO | Yes | needed in every demand state |
| Preserve executable optionality | Yes | value changes, but never becomes zero |
| Match duration to demand certainty | Yes | protects both upside and downside |
| Lock maximum capacity early | No | only rational under strong scarcity/demand certainty |
| Always multi-source equally | No | can destroy efficiency |
| Avoid debt | No | capital structure is scenario/project dependent |
| Build geographic redundancy everywhere | No | resilience has a cost |
| Bet on one 2036 winner | No | violates updateability |
| Use state triggers and falsification | Yes | required under uncertainty |

---

# 16. The highest-level decision judgment

The report’s most robust strategic conclusion is not:

> who wins AI infrastructure.

It is:

> **organizations should maximize the quality of their future choices by tying irreversible commitments to verified demand, preserving executable alternatives, matching asset/financing duration to demand duration, and defining in advance the evidence that would force them to change course.**

This is stronger than a point forecast because it remains useful when the forecast is wrong.

---

# 17. Relationship to Chapter 31

Chapter 31 already contains several of these principles in scenario-specific form.

Phase II adds one stricter test:

> **Which recommendations survive all four scenarios?**

Only those should be promoted to “decision invariants.”

Everything else remains conditional strategy.
