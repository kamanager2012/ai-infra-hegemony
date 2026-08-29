# Phase II · Minimum Public-Proxy Scenario Dashboard v0.5

> **Status:** Research-side calibration layer; not part of the frozen formal facts.  
> **Purpose:** turn S1–S4 from a narrative scenario set into an updateable public-proxy state machine without inventing precision that public data cannot support.

## 1. Why this dashboard exists

The formal report already defines the relevant state variables, but several of the most important ones are not directly observable:

- customer-level scarce-layer allocation;
- large-cluster utilization;
- workload-level monetization;
- supplier-level commitment splits;
- contract-level cancellation / rescheduling;
- true cost per verified workflow outcome.

Therefore the dashboard does not pretend to observe the latent state directly.

It asks:

> **Which public proxies would have to move, in which direction, before the report should change scenario weight?**

## 2. Hard anti-overfitting rules

1. **No single proxy can switch the scenario.**
2. **One company cannot stand in for the whole system.**
3. **One reporting period cannot establish persistence when the underlying variable is volatile.**
4. **Commitment / secured / design capacity cannot be treated as energized / utilized capacity.**
5. **Revenue mix cannot be treated as physical allocation.**
6. **Seller-supported financing and independently financed demand must be separated.**
7. **A proxy must have a plausible transmission path to the latent variable it represents.**
8. **Counterevidence must be recorded beside supportive evidence.**

This is a qualitative protocol until historical backtesting supports calibrated thresholds.

## 3. Dashboard axes

| Axis | Latent variable | Minimum public proxies | Main false positive | Scenario use |
|---|---|---|---|---|
| A. Scarce-layer tightness | actual quantity assurance | lead time, management tightness commentary, qualification delays, allocation / delivery disclosures | pricing strategy or product transition | S1 ↔ S2 ↔ S3 |
| B. System substitution | executable buyer optionality | production workload adoption, multi-stack deployment, migration benchmark, repeat deployment | product launch / demo without production scale | S1 ↔ S2 |
| C. Forward commitment | future capacity reservation | manufacturing/supply commitments, long-term capacity contracts, project state transitions | timing shift / architecture mix change | S2 ↔ S3 / S4 |
| D. Market clearing | utilization pressure | used-system price, lease rates, cloud discount, delivery lead time, inventory | new-generation price/performance improvement | S4 |
| E. Accounting confirmation | loss recognition | inventory provision, impairment, accelerated depreciation, disposal | isolated product transition | S4 confirmation |
| F. Demand quality | independent ability to pay | customer operating cash flow, third-party financing, debt terms, contract quality | seller-supported circularity | S2/S3 ↔ S4 |
| G. Seller support | financing reflexivity | seller equity, guarantees, credit enhancement, OEM financing | healthy ecosystem investment | S4 risk amplifier only when customer economics weaken |
| H. Power / LPS | deployment availability | interconnection milestone, substation/transformer delivery, permitted/construction/energized MW, Time-to-Power | announced/secured GW treated as online | S1/S2/S3 |
| I. China frontier closure | production-grade alternative stack | seven gate evidence: compute, memory, packaging, interconnect, runtime, production workload, utilization/economics | consumer-scale or product existence extrapolated to frontier closure | S1/S2/S3 geography |
| J. Geopolitical continuity | access continuity | export-control state, licensing, allied coordination, Taiwan continuity, service/equipment access | policy headline without physical transmission | all scenarios |
| K. Hyperscaler capital-cycle transmission | whether infrastructure intensity is outrunning durable monetization / financing quality | within-company headroom, recognized CapEx/leases, debt/equity issuance, RPO/bookings breadth, cloud monetization, clearing/accounting | negative FCF or high CapEx read in isolation | S2/S3 ↔ S4 |

## 4. S2 must have exit tests

### S2 → S1
Required direction:
- substitution becomes production-scale and repeatable;
- migration cost falls;
- at least one currently scarce physical layer shows durable supply elasticity improvement;
- buyer optionality rises without system utilization collapsing.

### S2 → S3
Required direction:
- more than one scarce layer remains tight;
- delivery/access becomes more concentrated;
- switching cost remains high;
- forward reservation / long-duration capacity coordination increases;
- buyer alternatives fail to scale.

### S2 → S4
Required direction:
- utilization / revenue weakens relative to deployed capital;
- clearing price / lease economics deteriorate;
- forward commitments shrink, cancel, or reschedule for economic reasons;
- financing independence weakens;
- accounting losses later confirm the pressure.

## 5. No pseudo-threshold rule

The dashboard deliberately does **not** write:

> “two quarters + three signals = scenario switch”

because that would be a D-grade rule presented as if empirically estimated.

Instead every update records:

- first deterioration / improvement;
- cross-confirmation;
- accounting or utilization confirmation where available;
- segment breadth;
- counterevidence;
- data frequency.

Historical Phase II backtesting will determine whether a more quantitative trigger is defensible.

## 6. Public-proxy update sheet

| Axis | Current signal | Direction | Breadth | Persistence | Counterevidence | Evidence grade | Scenario implication |
|---|---|---|---|---|---|---|---|
| Scarce layer |  | ↑ / → / ↓ | Narrow / Multi / System | one-off / repeated |  | A/B/C |  |
| Substitution |  |  |  |  |  |  |  |
| Forward commitment |  |  |  |  |  |  |  |
| Market clearing |  |  |  |  |  |  |  |
| Accounting |  |  |  |  |  |  |  |
| Demand quality |  |  |  |  |  |  |  |
| Seller support |  |  |  |  |  |  |  |
| Power/LPS |  |  |  |  |  |  |  |
| China closure |  |  |  |  |  |  |  |
| Geopolitics |  |  |  |  |  |  |  |
| Hyperscaler capital cycle |  |  |  |  |  |  |  |

The blank cells are intentional: missingness must remain visible.

## 6.1 Axis G protocol — Seller / Sponsor Support

Axis G is now split into explicit support types.

| Support type | Proxy | S4 relevance |
|---|---|---|
| Equity support | seller / sponsor private placements or strategic equity | raises reflexivity risk only when recipient economics / independent capital access weaken |
| Guarantees | lease, land/power/shell, payment or project guarantees | measures risk transfer; becomes negative when guarantee dependence rises while project economics weaken |
| Vendor / OEM finance | hardware leases, OEM/software-license financing | can accelerate deployment; negative only when independent funding capacity deteriorates |
| Capital mobilization | third-party infrastructure funds / private capital | generally counterevidence to pure seller circularity if third-party risk-bearing is real |
| Customer prepayment | upfront / minimum-payment contract cash | strengthens financeability but increases contract / customer dependence |

### 6.1A Hard no-double-count rule

For any one project:

> **contract value + debt raised against contract + seller equity + guarantee cap + customer prepayment must not be added together as “total demand.”**

They are different balance-sheet expressions of the same underlying infrastructure / workload expectation.

### 6.1B Current 2026 seller-support state

Current public evidence shows substantial support capacity:
- NVIDIA strategic equity and guarantee exposure;
- AMD lease guarantees / investment commitments;
- NVIDIA equity participation in CoreWeave;
- OEM / GPU financing across neocloud deployments.

But the current correct classification is:

> **support intensity is rising; support dependence has not yet been shown to replace weakening end demand at system scale.**

Therefore Axis G remains an **S4 risk amplifier**, not an S4 trigger.

It should move meaningfully toward S4 only when:

```text
Seller / Sponsor Support ↑
+
Independent Third-Party Capital ↓
+
Customer Cash Generation / Monetization ↓
+
Refinancing Terms Worsen
```

---

## 6A. Dashboard K — Hyperscaler Capital-Cycle Transmission

The four hyperscaler quarterly pilots in P0-4 can now be converted into one S4 monitoring protocol.

The dashboard does **not** compare firms by a common synthetic CapEx ratio because the accounting identities differ.

It asks the same six questions within each firm.

| Layer | Question | Strengthens S4 when | Counterevidence / non-S4 interpretation |
|---|---|---|---|
| 1. Headroom | Is OCF covering comparable cash infrastructure / PP&E spend? | headroom compresses for multiple periods because OCF / monetization weakens while fixed commitments remain high | headroom compresses because deliberate buildout accelerates while demand and operating economics remain strong |
| 2. Recognized commitment | Are infrastructure commitments still expanding or being cut? | CapEx / leases / contracted capacity are reduced, delayed, canceled, or renegotiated for economic reasons | CapEx remains high because capacity is still constrained or demand is expanding |
| 3. Financing amplification | Is marginal expansion increasingly dependent on weaker-quality capital? | spreads / coupons rise, maturities shorten, leverage falls involuntarily, supplier support rises, refinancing becomes difficult | debt / equity / leases remain long-tenor and broadly available while third-party risk capital remains willing |
| 4. Demand breadth / quality | Is demand broadening or becoming fragile / concentrated? | bookings / RPO / cloud demand weaken; anchor-customer concentration rises; renewals or commitments deteriorate | ex-anchor demand broadens, RPO/bookings grow, customer mix diversifies |
| 5. Monetization | Is deployed capacity earning enough relative to the asset base? | cloud / AI revenue, operating income, utilization or ROI proxies weaken relative to deployed capital | cloud growth and operating economics remain strong despite high investment |
| 6. Clearing / accounting | Is real clearing visible? | project delay/cancel, capacity resale/discounting, inventory clearing, impairment, accelerated depreciation, distressed refinancing | no clearing, utilization remains strong, commitments stay intact |

### 6A.1 Hard anti-overfit rules

The following statements are **forbidden**:

> negative free cash flow = S4

> external debt / equity issuance = weak demand

> high CapEx = bubble confirmation

> one hyperscaler = system-wide state

The correct rule is:

> **S4 weight rises materially only when financing / headroom deterioration aligns with weaker demand or monetization and then begins to affect forward commitments, clearing, or accounting.**

Prefer:
- multi-quarter persistence;
- more than one hyperscaler / infrastructure layer;
- borrower/project transmission;
- explicit counterevidence.

### 6A.2 2026 four-company research-side state

The current four-company evidence is better described as **high-intensity expansion with increasing financing amplification**, not cross-company S4 confirmation.

| Company | Headroom / capital signal | Financing signal | Demand / monetization counterevidence | Current research-side interpretation |
|---|---|---|---|---|
| Meta | 2026Q2 company-defined FCF/headroom compressed to about US$0.8B as CapEx rose sharply | long-term debt issuance / balance-sheet capacity more relevant | 2026 operating-income guidance remained above 2025 while CapEx guide increased | expansion intensity; no S4 confirmation |
| Alphabet | 2026Q2 company-defined FCF about -US$5.9B as CapEx reached about US$44.9B | large 2026 debt and equity issuance | continued strong cloud / AI demand and very high operating cash generation | Layer-1 compression + Layer-2 amplification; not distress by itself |
| Microsoft | cash PP&E and total CapEx both rose; FY26Q2 cash FCF compressed | finance leases materially affect recognized infrastructure commitment | FY26Q4 commercial RPO broadened outside frontier-model companies; ex-OpenAI RPO remained strong | high capital intensity with improving demand breadth |
| Amazon | company-level cash headroom was negative in several 2025–2026 quarters | material debt issuance and strategic AI investment in 2026 | denominator includes fulfillment-network spend as well as AWS; AWS economics / demand remain separate variables | company-level capital intensity; cannot infer AWS S4 |

This table is **not** a ranking.

It exists to demonstrate the protocol:

> **same headroom signal, different transmission state.**

### 6A.3 Cross-confirmation states for Dashboard K

Use three research-side labels only:

**K-A — Expansion / absorption**
- headroom may compress;
- commitments remain strong;
- financing remains available;
- demand breadth / monetization remain healthy;
- no real clearing.

**K-B — Financing sensitivity / watch**
- headroom compresses;
- financing amplification rises;
- customer concentration or refinancing dependence becomes material;
- demand / monetization still mixed rather than clearly weak;
- no broad clearing yet.

**K-C — Clearing confirmation**
- headroom / OCF weaken;
- financing terms deteriorate;
- demand / monetization weaken;
- commitments shrink or reschedule for economic reasons;
- clearing / accounting evidence appears;
- breadth extends beyond one borrower or one accounting period.

These are **ordinal research states**, not calibrated S4 thresholds.

### 6A.4 Relationship to P0-1 historical timing

P0-1 shows that Accounting often confirms rather than leads a long-duration capital clearing, while inventory-led corrections can produce near-synchronous Accounting and Market Clearing.

Dashboard K therefore should monitor in this order:

```text
Demand / monetization
→ headroom / financing sensitivity
→ forward commitment
→ market clearing
→ accounting / refinancing confirmation
```

but the order is not mandatory.

The key is **cross-signal confirmation and breadth**, not a fixed clock.

---

## 6B. Dashboard K borrower extension — project-financed infrastructure

Dashboard K now distinguishes cash-rich hyperscalers from project-financed / neocloud infrastructure.

The latter requires an additional borrower layer:

| Variable | Why it matters | Current public examples |
|---|---|---|
| Contract-backed debt | turns customer credit quality into financing capacity | CoreWeave, Nebius, IREN |
| Customer prepayment / minimum payment | reduces sponsor equity need but can concentrate dependency | IREN |
| Coupon / floating-rate exposure | determines sensitivity to public/private credit conditions | Nebius SOFR-linked; Applied Digital fixed-rate secured notes |
| Maturity concentration | creates refinancing exposure, but not realized stress by itself | CoreWeave near-term principal load; Applied Digital FY31 wall |
| Bridge / short-dated debt | increases near-term refinancing dependence | Applied Digital bridge facility |
| Asset collateral | determines lender recovery / residual-value sensitivity | GPU / infrastructure-backed facilities |
| Customer concentration | can strengthen financeability and increase single-name dependency at the same time | CoreWeave/Core Scientific chains |
| Asset-identity of impairment | prevents false S4 classification | IREN legacy Bitcoin-mining hardware impairment |

### 6B.1 Borrower-level S4 rule

A leveraged AI-infrastructure borrower is **not** S4 simply because:
- debt is large;
- coupons are high;
- customer prepayments are used;
- GPUs are collateral;
- one customer is important.

S4 evidence strengthens when:

> **financing dependence + weaker contract / customer economics + maturity/refinancing pressure + delivery/utilization weakness begin to cross-confirm.**

This is the project-finance equivalent of the hyperscaler six-layer protocol.

### 6B.2 Refinancing exposure vs realized refinancing stress

Dashboard K now separates two states that must not be conflated.

**Refinancing exposure**
- large debt balance;
- near-term maturity;
- floating-rate debt;
- bridge financing;
- concentrated maturity wall;
- high coupon;
- customer concentration.

These variables raise sensitivity.

They do **not** prove distress.

**Realized refinancing stress**
- committed liquidity disappears or draw availability falls;
- refinancing fails, is materially delayed, or closes on much worse terms;
- maturity is extended under pressure;
- covenant / DSCR headroom deteriorates or breaches;
- required collateral / guarantee burden rises materially;
- project delivery slows because financing cannot close;
- asset sale / impairment / distressed restructuring follows.

Current counterexamples matter:

- Core Scientific replaced a SOFR-linked US$1.0B term loan with long-duration fixed-rate 7.75% secured notes;
- Applied Digital refinanced its short bridge after fiscal year-end into longer-dated 2031 notes;
- Nebius disclosed a 1.15× DSCR covenant on a 2030 contract-backed facility;
- CoreWeave still reported substantial undrawn committed liquidity and covenant compliance at June 2026.

Therefore:

> **maturity wall = exposure; adverse rollover = event.**

### 6B.3 Current research-side borrower state

Current public evidence across CoreWeave, Core Scientific, Nebius, Applied Digital and IREN shows a rapid expansion of financing structures, but not one uniform stress state.

- some facilities are supported by investment-grade customer contracts and long-duration pledged cash flows;
- some borrowers carry materially higher coupons / concentrated maturities;
- customer prepayments materially reduce sponsor funding need in some GPU deployments;
- supplier / financing structure is increasingly part of how physical AI capacity is brought online.

Therefore:

> **financing amplification is observable; system-wide refinancing stress is not established.**

The monitoring task is now to detect the transition from **financeable leverage** to **fragile leverage**, not to treat leverage itself as the event.

---

## 7. Formal-report interaction

This dashboard does **not** overwrite the frozen S1–S4 framework.

It supplies the missing operational layer:

> formal scenario definitions → public proxies → historical validation → eventual calibrated transition rules.

Until calibration is strong enough, the formal report should continue to state that S1–S4 are conditional structural states, not a mechanical classifier.
