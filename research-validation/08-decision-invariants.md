# Phase II · Decision Invariants v0.3

> **Status:** Research-side strategic layer; not part of the frozen 32-chapter formal report.  
> **Goal:** identify low-regret principles that remain valid across S1–S4, rather than giving one strategy per scenario.

## 0. Decision-rule ownership contract v0.3

This file owns:
- cross-scenario decision rules;
- actor-specific implementation burden;
- low-regret / falsification logic.

It does **not** own:
- evidence state;
- scenario probability;
- live clearing adjudication;
- geopolitical / financing / technical-closure facts.

Authoritative inputs come from the relevant evidence/state layers (`01A`, `03`, `04A–04D`, `05`, `09`, `10`, `12`, `13`).

Hard rule:

> **Decision invariants may tell an actor how to react to a state; they may not create or upgrade that state.**

Formal Chapter 31 remains frozen unless explicitly reopened.

## 1. What counts as a decision invariant

A decision invariant must satisfy all four conditions:

1. **Cross-scenario robustness** — it remains directionally useful under S1, S2, S3 and S4;
2. **Observable implementation** — an organization can tell whether it is actually following the principle;
3. **No hidden point forecast** — it does not require knowing the 2030/2036 winner in advance;
4. **Reversibility / optionality** — it reduces the cost of being wrong when the scenario changes.

Canonical numbering rule:

> **The hard-invariant number refers only to the final ten-item hard set.**

Historical candidates that were demoted during v0.2 falsification are labeled **Conditional Strategy A/B** and do not consume hard-invariant numbers. Section numbers are retained only for document structure.

An invariant is not:

- “buy more GPUs”;
- “multi-cloud everything”;
- “assume AI demand keeps growing”;
- “avoid long-duration assets”;
- “diversify every supplier.”

Those are scenario-dependent choices.

---

# 2. Hard Invariant 1 — Verify economics at the decision-relevant outcome, not the input-unit price

Across every scenario, the economic unit must be the **decision-relevant verified outcome**, not an input-unit price.

For an enterprise workflow, the preferred unit is:

> **cost per verified successful workflow outcome (VSWO)**

Why it survives S1–S4:

- **S1:** cheaper/more portable compute still has to produce accepted outcomes;
- **S2:** platform concentration does not remove the need for workload ROI;
- **S3:** scarce capacity makes outcome-level allocation even more important;
- **S4:** cheap clearing compute is only valuable if real workflows can absorb it.

Decision rule:

> Do not increase long-duration compute commitment faster than verified workflow demand and accepted-outcome economics can justify.

Observable implementation depends on actor:
- enterprise/application buyer → VSWO, cost/VSWO, human review, retry/remediation, realized business value;
- hyperscaler → workload utilization, contracted demand, cloud/AI monetization, contribution economics;
- supplier → repeat/qualified end demand, customer concentration, cancellation/commitment quality;
- infrastructure developer → contracted → energized → utilized capacity, tenant cash-flow coverage;
- capital provider → DSCR, contracted cash flow, refinancing state, residual value;
- policymaker → operational capacity, continuity, qualification and realized—not announced—industrial output.

---

# 3. Conditional Strategy A — Preserve an executable second path

The primary stack can be highly concentrated for efficiency.

**v0.2 status:** this is no longer a hard invariant. The invariant is to **price executable optionality**; continuously maintaining a second production path is conditional on continuity / bargaining / recovery value exceeding carrying cost.

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

# 4. Hard Invariant 2 — Match commitment duration to demand certainty

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

# 5. Hard Invariant 3 — Separate asset clocks

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

# 6. Hard Invariant 4 — Stage-gate irreversible commitments

For every major irreversible commitment, release capital / organizational commitment against observable state transitions.

For physical infrastructure use:

> **Announced → Contracted/Secured → Permitted → Construction → Energized → Utilized**

Never collapse those states.

Why it survives S1–S4:
- prevents false abundance in S1/S2;
- prevents false scarcity certainty in S3;
- prevents overstating stranded assets in S4 before physical delivery.

Capital should be released against state transitions where possible.

---

# 7. Hard Invariant 5 — Measure scarce layers separately

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

# 8. Hard Invariant 6 — Track buyer economics separately from seller economics

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

# 9. Hard Invariant 7 — Separate financing identity / quality from financing quantity

More capital is not automatically stronger demand.

Always distinguish:
- customer operating cash flow;
- third-party risk capital;
- debt;
- supplier equity;
- guarantees;
- credit enhancement;
- refinancing dependency.

The hard invariant:

> **separate independent workload economics from financing amplification, and identify who ultimately bears the loss.**

The older preference for self-financing demand is retained only as a conditional warning when sponsor/supplier support rises while utilization, monetization, refinancing terms, or third-party risk appetite deteriorate.

Why it survives S1–S4:
- healthy financing improves expansion in S1–S3;
- deteriorating financing independence is an early S4 warning.

---

# 10. Hard Invariant 8 — Trigger decisions by state changes, not calendar dates

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

# 11. Hard Invariant 9 — Build resilience where the cost of failure justifies it

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

# 12. Hard Invariant 10 — Keep falsification variables next to every major commitment

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

# 13. Conditional Strategy B — Prefer transferability over perfect optimization

When uncertainty is high, an asset/system that is slightly less optimized but:
- portable;
- redeployable;
- resaleable;
- compatible;
- multi-customer capable

can have higher strategic value.

When uncertainty is low and demand is durable, optimization can dominate.

The hard relationship is:

> **the value of transferability rises with uncertainty, commitment duration, and residual-value risk.**

The action “prefer transferability” remains conditional rather than invariant.

This applies to:
- compute contracts;
- data centers;
- power;
- software architecture;
- financing structures.

---

# 13A. Cross-S1–S4 falsification test

v0.2 applies the file's own standard literally:

> **if a recommendation fails in any scenario, it is not a hard invariant.**

The result is stricter than v0.1.

| Principle | S1 | S2 | S3 | S4 | v0.2 classification |
|---|---|---|---|---|---|
| Measure verified workflow economics | Pass | Pass | Pass | Pass | **Hard invariant** |
| Maintain a production-like second path | Conditional | Pass | Pass | Conditional | **Demote** |
| Match commitment duration to demand certainty | Pass | Pass | Pass | Pass | **Hard invariant** |
| Separate asset clocks | Pass | Pass | Pass | Pass | **Hard invariant** |
| Stage-gate physical capacity | Pass | Pass | Pass | Pass | **Hard invariant** |
| Measure scarce layers separately | Pass | Pass | Pass | Pass | **Hard invariant** |
| Separate buyer economics from seller economics | Pass | Pass | Pass | Pass | **Hard invariant** |
| Classify financing quality separately from quantity | Pass | Pass | Pass | Pass | **Hard invariant** |
| Prefer independently self-funded demand | Conditional | Usually | Usually | Conditional | **Demote preference** |
| Trigger by state changes, not calendar dates | Pass | Pass | Pass | Pass | **Hard invariant** |
| Price resilience rather than maximize redundancy | Pass | Pass | Pass | Pass | **Hard invariant** |
| Keep falsification variables beside commitments | Pass | Pass | Pass | Pass | **Hard invariant** |
| Prefer transferability over optimization | Conditional | Conditional | Usually | Usually | **Demote** |

## 13A.1 Why executable second path is not a hard invariant

The underlying value is **optionality**, not necessarily a permanently maintained second production stack.

In S1:
- supply may be abundant;
- switching cost may be low;
- standardized interfaces may make fallback cheap to recreate;
- a low-criticality workload may not justify continuous duplicate validation.

In S4:
- maintaining two full paths can destroy economics when utilization is weak.

Therefore the hard principle becomes:

> **Price the value of executable optionality; maintain a second path only when continuity / bargaining / recovery value exceeds carrying cost.**

This is consistent with Hard Invariant 9's priced-resilience logic.

## 13A.2 Why “prefer self-financing demand” is too strong

Financing **identity and loss absorption** must always be measured.

But a project does not become low quality merely because it uses:
- external equity;
- project debt;
- infrastructure funds;
- private credit.

A young but economically sound infrastructure asset may rationally use outside capital.

The hard invariant is therefore:

> **separate independent workload economics from financing amplification and identify who absorbs losses.**

The conditional warning is:

> rising sponsor / supplier support becomes negative evidence only when utilization, monetization, refinancing terms, or independent third-party risk appetite also deteriorate.

## 13A.3 Why transferability is a conditional strategy

Transferability has option value, but perfect portability is not free.

In a stable S1 or S2 workload with:
- high utilization;
- durable demand;
- low migration risk;
- strong asset-specific efficiency;

a highly optimized non-transferable design can be economically superior.

The robust relationship is:

> **the value of transferability rises with uncertainty, commitment duration, and residual-value risk.**

That relationship is invariant.

The action “prefer transferability” is not.

## 13A.4 v0.2 hard-invariant set

After falsification, the cleaner hard set is:

1. **Verify economics at the decision-relevant outcome.**
2. **Match commitment duration to demand certainty.**
3. **Separate asset clocks.**
4. **Stage-gate irreversible commitments.**
5. **Measure scarce layers separately.**
6. **Separate buyer economics from seller economics.**
7. **Separate financing quality / identity from financing quantity.**
8. **Trigger decisions by state changes, not calendar dates.**
9. **Price resilience rather than maximize redundancy.**
10. **Attach falsification variables to major commitments.**

Conditional strategies:
- maintain an executable second path;
- prefer independently financed demand;
- prefer transferability over optimization.

This reduction is a feature, not a loss.

A smaller invariant set is more credible because every item has survived an explicit contrary-state test.

---

# 14. Actor-specific implementation-cost test v0.3

v0.3 asks a stricter question than cross-scenario falsification:

> **Can each hard invariant be implemented by the actor who is supposed to use it, at an identifiable operational cost?**

A principle that is directionally true but has no observable owner, data field, review cadence, or decision consequence is only a **meta-principle**, not yet an operational invariant.

## 14.1 Implementation-cost scale

The cost labels below measure **implementation burden**, not economic desirability.

- **L — Low:** can usually be implemented with existing finance / procurement / operations data and a management review rule.
- **M — Medium:** requires cross-functional data joins, new governance, periodic testing, or additional contractual / operational telemetry.
- **H — High:** requires new qualification, duplicated capability, contractual data rights, capital re-architecture, or difficult external data collection.

A high-cost invariant can remain hard if the **measurement / decision rule** is still mandatory. The invariant does not require buying every hedge.

## 14.2 Six core actors

The test uses the six actors most relevant to the report's capital-allocation decisions:

1. Enterprise / AI application buyer
2. Hyperscaler / large platform buyer
3. Semiconductor / system supplier
4. Data-center / power / infrastructure developer
5. Capital provider
6. Policymaker

A frontier-model company can be mapped onto one or more of these roles depending on the decision:
- enterprise/workload owner;
- hyperscale compute buyer;
- infrastructure sponsor / borrower.

## 14.3 Ten-invariant × six-actor implementation matrix

| Hard invariant | Enterprise | Hyperscaler | Supplier | Infra developer | Capital provider | Policymaker | Operational verdict |
|---|---|---|---|---|---|---|---|
| 1. Verify economics at decision-relevant outcome | **M** — VSWO + realized value | **M/H** — workload utilization + monetization + customer demand | **M/H** — end-demand quality often outside own boundary | **M** — contracted→utilized + tenant economics | **M** — DSCR / cash-flow coverage / residual value | **H** — realized industrial output / continuity across firms | **Hard, but actor-specific denominator required** |
| 2. Match commitment duration to demand certainty | **L/M** | **M** | **M** | **M/H** | **M** | **M/H** | **Hard and directly operational** |
| 3. Separate asset clocks | **L/M** | **H** | **M/H** | **H** | **M/H** | **H** | **Hard; data architecture burden can be high** |
| 4. Stage-gate irreversible commitments | **L/M** | **M/H** | **M** | **H** | **M** | **M/H** | **Hard; physical-state version only when relevant** |
| 5. Measure scarce layers separately | **M** | **H** | **H** | **M/H** | **H** | **H** | **Hard meta-relationship; implementation requires actor-specific layer map** |
| 6. Separate buyer economics from seller economics | **M** | **M/H** | **H** | **M/H** | **M** | **H** | **Hard; external-side visibility is the main burden** |
| 7. Separate financing identity/quality from quantity | **L/M** | **M** | **M** | **M/H** | **L/M** | **M/H** | **Hard and measurable** |
| 8. Trigger decisions by state changes, not calendar dates | **L** | **L/M** | **L/M** | **L/M** | **L** | **M** | **Hard; lowest-cost invariant** |
| 9. Price resilience rather than maximize redundancy | **M** | **H** | **M/H** | **H** | **M** | **H** | **Hard decision rule; actual redundancy remains conditional** |
| 10. Attach falsification variables to major commitments | **L/M** | **M** | **M** | **M** | **L/M** | **M** | **Hard and broadly executable** |

### 14.3A First result: none of the ten fails the actor test, but two need explicit actor-specific instantiation

The test does **not** demote another invariant.

However, it exposes two principles that are too abstract if left uninstantiated:

1. **Invariant 1** cannot mean VSWO for every actor.  
   It is now:
   > verify economics at the actor's decision-relevant outcome.

2. **Invariant 5** cannot mean every actor directly measures every wafer/HBM/packaging/power denominator.  
   It means:
   > build the layer map relevant to the commitment, preserve denominator identity, and identify which layer is currently binding.

These are hard relationships, but their observables differ by actor.

## 14.4 Actor implementation cards

### 14.4.1 Enterprise / AI application buyer

**Minimum operating set**

| Invariant | Minimum implementation |
|---|---|
| Outcome economics | workflow_id, VSWO, human minutes, AI/tool cost, persistence, realized value where observable |
| Duration matching | contract / reservation tenor tied to verified workflow demand horizon |
| Asset clocks | separate model/API, software integration, hardware/cloud commitment and data-governance lives |
| Stage-gating | pilot → verified production → scaled deployment; do not jump directly from demo to long-duration commitment |
| Scarce layers | provider/model/runtime/data dependency map rather than semiconductor-layer reconstruction |
| Buyer/seller economics | own ROI separately from vendor growth / benchmark claims |
| Financing identity | distinguish normal Opex/CapEx from vendor credits / subsidized adoption |
| State triggers | scale / cut based on VSWO, reopen, utilization and value thresholds |
| Priced resilience | second provider / exportability only when continuity value exceeds carrying cost |
| Falsification | predefine rollback / expansion triggers |

**Main burden:** workflow telemetry and joining business value to technical usage.

### 14.4.2 Hyperscaler / large platform buyer

**Minimum operating set**

- workload-level utilization and monetization by infrastructure cohort;
- cash PP&E vs finance leases vs contracted capacity;
- accelerator/network/shell/power asset clocks;
- capacity state gates through energized/utilized;
- HBM/packaging/network/power bottlenecks as separate denominators;
- buyer ROI separately from seller/vendor economics;
- debt/equity/lease/contract-backed financing identity;
- RPO/bookings/customer-concentration state triggers;
- priced multi-stack / geographic / power resilience;
- explicit falsification around utilization, RPO, margin and capacity cuts.

**Main burden:** cross-layer telemetry and organizational ownership across cloud, finance, procurement and infrastructure.

### 14.4.3 Semiconductor / system supplier

**Minimum operating set**

- qualify end-demand quality rather than only orders / prepayments;
- match capacity commitments to customer demand duration;
- separate fab/tooling/packaging/inventory/product-cycle clocks;
- stage capital release across qualification and capacity milestones;
- keep wafer / packaging / memory / power / customer concentration denominators separate;
- seller revenue/margin separately from customer utilization / ROI;
- supplier equity / guarantees / financing support separately from organic demand;
- trigger capacity changes from allocation, cancellation, lead-time and utilization states;
- price customer/product/geographic resilience rather than maximize duplication;
- define falsification variables for every major capacity commitment.

**Main burden:** customer-side economic visibility. This is why supplier-assisted financing must not be mistaken for independent demand.

### 14.4.4 Data-center / power / infrastructure developer

**Minimum operating set**

- contracted capacity must progress to energized and utilized capacity;
- tenant demand duration must match lease / debt / power / land duration;
- shell, electrical, cooling, GPU/server and grid clocks remain separate;
- capital draw is stage-gated against permits, construction, power and tenant milestones;
- power, networking, compute and customer concentration are separate bottlenecks;
- landlord economics are separated from tenant workload economics;
- sponsor support / guarantee / project debt / prepayment identities remain separate;
- refinance and delivery triggers are state-based;
- redundancy / alternative tenants are priced against carrying cost;
- DSCR, customer renewal, construction delay and utilization are falsification variables.

**Main burden:** long-duration commitments create the highest duration-mismatch and refinancing implementation cost.

### 14.4.5 Capital provider

**Minimum operating set**

- underwrite cash-flow / DSCR / residual-value outcome rather than headline AI demand;
- match debt maturity and amortization to contracted demand / asset life;
- separate GPU, shell, power and contract clocks;
- release capital against project milestones and collateral state;
- model each collateral / supply / customer bottleneck separately;
- distinguish borrower revenue from end-customer economics;
- classify customer prepayment, sponsor equity, guarantees, debt and third-party risk capital separately;
- use covenant / liquidity / refinancing states rather than calendar forecasts;
- price collateral / guarantor / customer diversification rather than require maximal diversification;
- define covenant, DSCR, utilization and refinancing falsification triggers at underwriting.

**Main burden:** obtaining enough project/customer data rights to monitor after close.

### 14.4.6 Policymaker

**Minimum operating set**

- measure realized production/continuity outcomes, not subsidy announcements;
- match policy commitment duration to strategic need and technology cycle;
- separate fab/equipment/material/HBM/packaging/power/workforce clocks;
- stage public support against qualification, construction and operational milestones;
- preserve denominator identity across capacity, revenue, wafers, bits, MW and utilization;
- distinguish company revenue/market capitalization from buyer/system welfare;
- separate private risk capital from guarantees/subsidies/state-supported finance;
- trigger policy changes from operational state changes rather than target-year slogans;
- price resilience against fiscal / efficiency cost;
- attach sunset / scale-up / rollback criteria to major industrial-policy commitments.

**Main burden:** cross-firm observability and political difficulty of stopping programs after sunk cost.

## 14.5 Which invariants are cheapest and hardest to operationalize

### Lowest implementation burden

Across most actors:

1. **State-triggered decisions**
2. **Falsification variables beside commitments**
3. **Commitment-duration matching**

These mainly require governance discipline and explicit decision rules.

### Highest implementation burden

Across most actors:

1. **Separate asset clocks**
2. **Measure scarce layers separately**
3. **Price resilience**
4. **Separate buyer and seller economics**

These often require:
- cross-organization data;
- third-party/customer information;
- qualification/testing;
- contractual rights;
- capital or architecture changes.

The implication is important:

> **hard invariant does not mean cheap invariant.**

A principle can be robust across scenarios while still being expensive to execute.

## 14.6 Hard invariant vs hard action

v0.3 clarifies one final distinction:

> **the invariant is the decision rule, not the maximum-action version of that rule.**

Examples:

- Hard invariant: **price resilience**  
  Conditional action: maintain two fully production-qualified stacks.

- Hard invariant: **stage-gate commitment**  
  Conditional action: stop a project at a specific gate.

- Hard invariant: **measure financing quality**  
  Conditional action: reject debt-funded demand.

- Hard invariant: **measure transferability / residual-value sensitivity through asset clocks and resilience economics**  
  Conditional action: choose the more portable asset.

This prevents conditional strategies from re-entering the hard set through implementation language.

## 14.7 v0.3 operational verdict

After:
1. cross-S1–S4 falsification; and
2. six-actor implementation-cost testing,

the ten hard invariants still survive.

But the formulation is now cleaner:

1. **Verify economics at the decision-relevant outcome.**
2. **Match commitment duration to demand certainty.**
3. **Separate asset clocks.**
4. **Stage-gate irreversible commitments.**
5. **Measure scarce layers separately.**
6. **Separate buyer economics from seller economics.**
7. **Separate financing identity / quality from quantity.**
8. **Trigger decisions by state changes, not calendar dates.**
9. **Price resilience rather than maximize redundancy.**
10. **Attach falsification variables to major commitments.**

Conditional strategies remain:
- maintain an executable second path;
- prefer independently financed demand;
- prefer transferability over optimization.

No additional invariant is promoted.

No conditional strategy is promoted back into the hard set.

---

# 15. What is genuinely scenario-invariant vs. scenario-dependent

| Decision | Invariant? | Why |
|---|---|---|
| Verify decision-relevant outcome economics | Yes | every actor needs a verified outcome denominator, though VSWO is enterprise-specific |
| Preserve executable optionality | Conditional | option value can be positive while a continuously maintained second production path is not worth its carrying cost |
| Match duration to demand certainty | Yes | protects both upside and downside |
| Lock maximum capacity early | No | only rational under strong scarcity/demand certainty |
| Always multi-source equally | No | can destroy efficiency |
| Avoid debt | No | capital structure is scenario/project dependent |
| Build geographic redundancy everywhere | No | resilience has a cost |
| Bet on one 2036 winner | No | violates updateability |
| Use state triggers and falsification | Yes | required under uncertainty |

---

# 16. The highest-level decision judgment

After cross-scenario falsification, the report’s most robust strategic conclusion is not:

> who wins AI infrastructure.

It is:

> **organizations should maximize the quality of future choices by tying irreversible commitments to verified economic outcomes, matching asset/financing duration to demand duration, pricing resilience and optionality explicitly, and defining in advance the evidence that would force them to change course.**

This is stronger than a point forecast because it remains useful when the forecast is wrong.

---

# 17. Relationship to Chapter 31

Chapter 31 already contains several of these principles in scenario-specific form.

Phase II now applies the stricter test explicitly:

> **Which recommendations survive all four scenarios?**

v0.3 keeps the hard set at ten after six-actor implementation-cost testing. Executable second paths, self-financing preference, and transferability remain valuable only under observable cost / uncertainty / continuity conditions. The actor test does not add new invariants; it makes the existing ten operational.
