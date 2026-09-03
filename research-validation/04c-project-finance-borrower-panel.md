# P0-4C · AI Infrastructure Project-Finance Borrower Panel v0.3

> Initially extracted from P0-4 v0.17; the parent method is now v0.18. The panel separates financing exposure from realized refinancing stress and keeps facility-level identity.

## 11B. Project-finance borrower panel v0.1 — beyond CoreWeave

CoreWeave / Core Scientific are no longer the only project-finance chain in the research layer.

Three additional borrowers now provide different financing identities.

| Borrower | Financing structure | Maturity / pricing / coverage | What it demonstrates | What must not be inferred |
|---|---|---|---|---|
| Nebius | GPU-infrastructure / contracted-cash-flow senior secured debt + corporate convertibles | first secured facility ~US$775M, SOFR + 2.50%, matures 2030; together with customer cash flows covers >100% of underlying GPU CapEx | investment-grade customer contracts can be transformed directly into asset-backed debt capacity | secured financing proves utilization; debt growth proves distress |
| Applied Digital | senior secured notes + convertible debt + bridge / term facilities | US$2.35B 9.25% notes due 2030; US$2.15B 6.75% notes due 2031; US$300M bridge due 2027; weighted-average term-loan rate ~7.1%; ~US$4.19B principal scheduled in FY31 | maturity concentration and coupon structure make refinancing / completion risk materially more important than for cash-rich hyperscalers | higher coupon alone means project failure |
| IREN | customer prepayments + convertible notes + GPU leasing + GPU financing | Microsoft-linked ~US$3.6B GPU financing around 6%; separate ~US$2.8B GPU financings including 9% fixed-rate financing; prepayments cover a meaningful share of GPU CapEx | customer contracts / prepayments can materially reduce equity funding need, while borrower risk varies by counterparty quality and financing price | customer prepayment is organic cash flow; all impairment is AI clearing |

### 11B.1 Nebius — contract-backed debt as repeatable growth framework

In July 2026 Nebius entered its first senior secured facility of approximately **US$775M**.

The facility:
- is backed by deployed GPU infrastructure;
- is supported by contracted cash flows from an investment-grade customer;
- bears interest at **SOFR + 2.50%**;
- matures **October 31, 2030**;
- together with the customer cash-flow structure, covers more than 100% of the capital expenditure required for the underlying GPU deployment.

Nebius subsequently continued to use corporate convertible-note financing for broader data-center / GPU expansion.

Research implication:

> **contract quality can be converted into financing capacity before the infrastructure has generated a long public operating history.**

That is a financing-strength signal.

It also creates a future dependency:

> **contract performance → pledged cash flow → debt service.**

### 11B.2 Applied Digital — maturity wall and coupon sensitivity

Applied Digital's FY2026 filing shows a more maturity-sensitive structure.

As of May 31, 2026, major debt included:

- **US$2.35B** 9.25% senior secured notes due December 2030;
- **US$2.15B** 6.75% senior secured notes due March 2031;
- **US$450M** 2.75% convertible notes due June 2030;
- **US$300M** bridge facility due April 2027;
- additional term / other debt.

The filing reports:
- weighted-average term-loan interest rate around **7.1%**;
- remaining principal payments of about **US$4.19B in FY31**.

This creates a clear MF6 / maturity-wall monitor.

The S4-relevant variables are not the coupon in isolation.

They are:

```text
construction / lease cash flow
+
debt-service coverage
+
refinancing terms
+
maturity concentration
+
project delivery
```

A refinancing problem becomes system evidence only if it coincides with weaker project economics / demand and extends beyond one borrower.

### 11B.3 IREN — prepayment + GPU financing + counterparty-quality differentiation

IREN provides a different structure.

By early 2026 it had assembled financing across:
- customer prepayments;
- convertible notes;
- GPU leasing;
- GPU financing.

For its Microsoft-linked deployment:
- GPU financing was approximately **US$3.6B**;
- reported pricing was about / below **6%**;
- together with a **US$1.9B Microsoft prepayment**, the structure was expected to cover roughly **95%** of associated GPU CapEx.

By August 2026 IREN also described:
- approximately **US$2.8B** of additional GPU financings for other customer deployments;
- a large financing tranche at around **9% fixed**;
- customer prepayments covering roughly **45–55%** of GPU CapEx in recent contracts.

This shows why project finance must classify **counterparty and contract quality**, not just financing amount.

A useful monitor is:

```text
Net sponsor funding need
=
GPU / infrastructure CapEx
-
customer prepayment
-
asset-backed / GPU financing
```

but this is not the same as project profitability.

### 11B.4 Accounting-identity warning from IREN

IREN's FY26 results also include a strong accounting counterexample.

The company reported large non-cash impairments primarily associated with **decommissioning Bitcoin-mining hardware while sites were converted toward AI Cloud growth**.

Therefore:

> **an impairment inside an AI-transitioning company is not automatically an AI-infrastructure clearing signal.**

Before assigning the Accounting signal to AI S4, identify:

- which asset was impaired;
- which business generated the impairment;
- whether the impaired asset is legacy / displaced by AI or is itself AI infrastructure;
- whether the loss reflects demand clearing, technology migration, or strategic conversion.

This rule should be applied to every mixed-business infrastructure company.

### 11B.5 Standardized borrower maturity / pricing / concentration matrix

The project-finance panel is now normalized into one update table.

| Borrower / reference | Financing amount / structure | Pricing | Maturity / wall | Cash-flow / collateral support | Concentration / prepayment | Current research read |
|---|---|---|---|---|---|---|
| CoreWeave · 2026Q2 | ~US$13.6B DDTLs + ~US$16.6B notes outstanding; ~US$10.0B availability under existing facilities | DDTL 4.0 floating: SOFR + 2.25%; DDTL 5.0: SOFR + 4.50%; Apr-2026 senior notes: 9.75% | Q1 debt schedule: ~US$6.1B remainder-2026, US$5.7B 2027, US$3.8B 2028, US$2.9B 2029, US$2.3B 2030; DDTL 4.0 matures Mar-2032; DDTL 5.0 final payment May/Nov-2031 depending facility terms | asset collateral + pledged contractual cash flows; several SPV structures; DDTL 4.0 largely non-recourse | Q1 2026 total debt interest expense ~US$427M after capitalization; all disclosed DDTL covenants in compliance at Jun-2026 | very large financing scale plus near-term principal load; still financeable, but refinancing and customer-contract quality are first-order variables |
| Core Scientific · 2026Q2 | US$3.3B senior secured notes + US$460M 2029 convertibles + US$625M 2031 convertibles; prior US$1.0B SOFR+2.50% term loan repaid May-2026 | 7.75% fixed on senior secured notes; 3.00% on 2029 convertibles; 0% stated on 2031 convertibles | no principal due 2026–2028 on current notes; US$649.8M due 2029 incl. secured-note amortization/convertibles; remaining secured notes largely thereafter | CoreWeave contract revenues feed a lockbox supporting debt; no variable-rate debt outstanding at Jun-2026 | CoreWeave ~77% of H1 revenue; Q2 interest incurred ~US$52.4M, interest expense after capitalization ~US$40.6M | refinancing action reduced floating-rate exposure, but concentration risk remains very high |
| Nebius · Jul-2026 | ~US$775M first senior secured facility; separate corporate convertibles for broader expansion | SOFR + 2.50% on secured facility | Oct-2030 on secured facility | deployed GPUs + contracted cash flows from investment-grade customer | DSCR covenant 1.15× plus minimum-liquidity covenant; customer contract plus facility covers >100% of underlying deployment CapEx | financeable contract-backed expansion with explicit covenant discipline; future dependency on contract performance |
| Applied Digital · FY2026 | US$2.35B 2030 secured notes + US$2.15B 2031 secured notes + US$450M convertibles + US$300M bridge + other debt | 9.25%, 6.75%, 2.75% on major notes; bridge: SOFR + 2.75%; weighted-average term-loan rate ~7.1% | bridge originally Apr-2027 but refinanced after year-end into 2031 notes; ~US$4.19B principal scheduled FY31 | project / secured-note structure; DSCR covenants disclosed and in compliance at May-2026 | FY26 gross interest expense ~US$85.3M; ~US$39.6M interest capitalized; net interest expense ~US$29.5M | maturity wall remains material, but successful bridge refinancing is counterevidence against near-term refinancing stress |
| IREN · 2026 | Microsoft-linked ~US$3.6B GPU financing + ~US$2.8B additional GPU financings + US$3.0B 1.00% 2033 convertibles + equipment leases | Microsoft-linked notes 5.96% / ~6%; one large additional financing ~9% fixed; convertibles 1.00% | Microsoft financing matures Dec-2031; convertibles Dec-2033; legacy GPU leases 24–36 months | GPUs + Microsoft contract cash flows; customer prepayments reduce sponsor funding need; parent guarantees on several equipment leases | Microsoft contract ~US$9.7B through 2031 with 20% tranche prepayments; recent contracts prepay ~45–55% of GPU CapEx | long-duration contract-backed expansion plus low-coupon corporate convertibles; financing quality differs sharply by customer/collateral structure |

### 11B.5A Update fields

Every future borrower update should capture the same minimum fields:

1. **Reference date**
2. **Gross debt / facility size**
3. **Cash drawn vs committed-but-undrawn**
4. **Fixed / floating pricing**
5. **Maturity**
6. **Collateral**
7. **Pledged customer cash flow**
8. **Customer concentration**
9. **Prepayment / minimum payment**
10. **Interest expense / capitalized interest**
11. **Covenant / DSCR**
12. **Refinancing / extension**
13. **Project delivery state**
14. **Impairment identity**

Missing values remain N/A.

Do not infer a value from another borrower merely to complete the matrix.

### 11B.5C Refinancing-state refresh — drawn, pricing, covenant and rollover

The standardized borrower panel now contains enough hard data to distinguish **financing scale** from **refinancing state**.

#### CoreWeave

CoreWeave's 2026 filings show:

- March 31, 2026 total debt of about **US$25.1B**;
- future principal payments of about **US$6.1B** for the remainder of 2026 and **US$5.7B** in 2027;
- Q1 contractual interest expense of about **US$483M**, with about **US$97M** capitalized and total reported debt interest expense about **US$427M**;
- DDTL 4.0 floating-rate pricing at **SOFR + 2.25%**, maturity March 2032;
- DDTL 5.0 pricing at **SOFR + 4.50%**, with a 0.50% undrawn fee;
- as of June 30, 2026, about **US$10.0B** availability under existing facilities;
- disclosed compliance with DDTL covenants as of June 30, 2026.

This is not a simple distress profile.

It is:

> **high leverage + high interest burden + substantial near-term principal + still-large undrawn committed liquidity + covenant compliance.**

The S4-relevant change would be deterioration in refinancing terms, draw availability, covenant headroom, or customer-contract performance.

#### Core Scientific

Core Scientific provides an actual refinancing-state transition rather than merely a debt snapshot:

- a fully drawn **US$1.0B** term loan at Term SOFR + 2.50% was repaid and terminated in May 2026;
- proceeds from **US$3.3B 7.75% senior secured notes due 2031** replaced that floating-rate exposure;
- as of June 30, 2026 the company reported **no variable-rate debt outstanding**;
- Q2 interest incurred was about **US$52.4M**, with about **US$11.7M** capitalized and reported interest expense about **US$40.6M**.

This is a useful counterexample:

> **large debt can coexist with an improvement in refinancing / rate-risk structure.**

Debt quantity alone would miss that.

#### Nebius

Nebius's July 2026 secured facility adds a clean covenant datapoint:

- approximately **US$775M** facility;
- **SOFR + 2.50%**;
- maturity October 2030;
- **1.15× DSCR covenant**;
- minimum-liquidity covenant;
- GPU assets + investment-grade customer contractual cash flows.

That makes DSCR a directly observable project-finance state variable rather than a conceptual placeholder.

#### Applied Digital

Applied Digital's FY2026 filing adds both an interest-cost and refinancing counterexample:

- FY26 gross interest expense about **US$85.3M**;
- about **US$39.6M** of interest capitalized;
- net interest expense about **US$29.5M**;
- the US$300M bridge facility carried **SOFR + 2.75%** and originally matured April 2027;
- after fiscal year-end, the bridge was refinanced with long-term 2031 notes;
- disclosed DSCR covenants were in compliance at May 31, 2026.

Therefore:

> **a near-term maturity is a risk state; successful refinancing is contrary evidence and must be recorded symmetrically.**

### 11B.5D New borrower-state fields that now become mandatory

The borrower table should no longer stop at gross debt.

For every borrower, the minimum quarterly / filing-date update now requires:

```text
Gross Debt
Drawn Debt
Undrawn Committed Liquidity
Cash Interest / Interest Incurred
Capitalized Interest
Fixed vs Floating
Next 24M Principal
Weighted / Facility Pricing
DSCR / Covenant State
Refinancing Completed / Pending
Customer Concentration
Pledged Customer Cash Flow
Project Delivery State
```

The most important new distinction is:

> **scheduled maturity risk ≠ realized refinancing stress.**

Realized stress requires adverse refinancing terms, failed access, covenant pressure, or project/economic deterioration.


### 11B.5E IREN maturity / capital-stack completion

IREN's Microsoft-linked financing moved from a commitment letter into executed financing in May 2026.

The executed structure includes:

- approximately **US$1.5B** delayed-draw term loan;
- approximately **US$2.1B** senior notes at **5.96%**;
- aggregate Microsoft-linked GPU financing of roughly **US$3.6B**;
- availability in tranches through May 2027;
- maturity on **December 31, 2031**;
- GPU collateral and Microsoft-contract cash flows supporting the structure.

At the customer-contract layer:

- Microsoft contract value is approximately **US$9.7B through 2031**;
- roughly **20% of each tranche's contract value** is prepaid before delivery and credited against later service fees.

At the corporate layer:

- IREN issued **US$3.0B** of **1.00% convertible senior notes due December 1, 2033** in May 2026;
- additional GPU financings for non-investment-grade customer deployments include a large **9.0% fixed-rate** tranche;
- older GPU equipment financings include 24–36 month leases with parent guarantees.

This creates a layered capital stack:

```text
Customer prepayment
+
GPU / contract-backed secured financing
+
equipment leases
+
corporate convertible debt
```

The financing should therefore be monitored by **layer**, not by one blended debt number.

### 11B.5F Financing-quality dispersion inside one borrower

IREN also shows that one borrower can contain very different financing quality.

Microsoft-linked deployment:
- investment-grade counterparty;
- ~6% financing;
- meaningful prepayment;
- 2031 maturity.

Other deployments:
- non-investment-grade counterparties;
- at least one large financing around **9% fixed**;
- prepayments still reduce sponsor equity need.

Therefore:

> **borrower-level average financing cost can hide material project-level dispersion.**

The correct S4 monitor is contract / facility specific:
- counterparty quality;
- pricing;
- tenor;
- prepayment;
- collateral;
- project delivery;
- renewal / utilization.

This is particularly important when one company spans hyperscaler and frontier-lab / startup customers.


### 11B.5B First cross-borrower lesson

The current five-borrower panel already shows that “AI debt” is not one asset class.

It contains at least:

- investment-grade-customer-backed GPU facilities;
- high-coupon project secured notes;
- customer-prepayment structures;
- corporate convertibles;
- finance leases;
- landlord / colocation cash-flow securitization;
- bridge facilities.

Therefore:

> **gross debt / AI CapEx is too crude to function as an S4 metric.**

A better financing-risk decomposition is:

```text
Refinancing Risk
=
Maturity Concentration
× Funding-Cost Sensitivity
× Contract / Customer Fragility
× Residual-Value Risk
× Delivery Risk
```

This is a conceptual multiplicative map, not an estimated formula.

---

### 11B.6 Borrower-level watch states

For project-financed AI infrastructure, use:

**PF-A — Contract-backed expansion**
- long-duration contracts / prepayments;
- financing closes on acceptable terms;
- project delivery progresses;
- customer concentration may be high, but counterparty quality / cash flow is strong.

**PF-B — Financing sensitivity**
- coupons / leverage / maturity dependence rise;
- sponsor funding need increases;
- bridge / refinancing reliance grows;
- delivery and demand remain intact.

**PF-C — Refinancing / clearing stress**
- financing terms deteriorate materially;
- maturity extension becomes necessary;
- covenant / DSCR pressure appears;
- contract quality weakens;
- project delivery slows or cancels;
- asset impairment / distressed sale follows.

No fixed numeric trigger is assigned in v0.1.

---


## 11B.7 Facility-Level Longitudinal State Ledger v0.2

Borrower-level gross debt is no longer sufficient.

The panel now records facility transitions as:

```text
Announced / Committed
→ Closed
→ Available
→ Drawn
→ Project Delivery
→ Monetization
→ Refinance / Amortize
→ Stress / Cure / Exit
```

The point is to distinguish a financing commitment from:
- actual borrowing;
- physical project delivery;
- revenue generation;
- refinancing stress.

### 11B.7A Current dated facility transitions

| Borrower / facility | Earlier state | Latest observable state | Delivery / monetization linkage | Current research read |
|---|---|---|---|---|
| **CoreWeave DDTL 4.0** | March-2026: **US$8.5B** delayed-draw facility opened | 2026-06-30: about **US$2.9B drawn** — US$1.4B floating + US$1.5B fixed; draw window extends to 2027-06-30 | company-level demand remains strong, but public filing does not map each draw to a separately observed facility-level revenue stream | **Partial draw / expansion financing; not a stress event** |
| **CoreWeave DDTL 5.0** | May-2026: **US$3.1B** delayed-draw facility | 2026-06-30 debt table carries about **US$1.101B** outstanding; amortization begins later in 2026 and expected final payment is May-2031 | facility-level utilization / customer cash flow is not separately disclosed in the public row used here | **Partially drawn; monitor draw pace + monetization + debt service** |
| **CoreWeave DDTL 5.5** | no balance at 2026-06-30 | 2026-08-07: new **US$2.6B** delayed-draw facility, available through Dec-2026; SOFR loans at Term SOFR + **5.5%** | no draw / utilization evidence yet in the entry filing | **New financing capacity; high spread is a financing-quality variable, not realized stress by itself** |
| **Core Scientific March-2026 Term Loan** | March-2026: **US$1.0B fully drawn** senior secured term loan | 2026-05-06: repaid and terminated using proceeds of **US$3.30B 7.75% senior secured notes due 2031**; no remaining term-loan obligation at 2026-06-30 | existing colocation revenue / customer concentration remain separate operating variables | **Refinancing completed; floating / short-term structure replaced rather than failed** |
| **Applied Digital · ELN-02 / ELN-03 financing** | 2025: **US$2.35B 9.25% 2030 notes** issued to fund 100MW ELN-02 + 150MW ELN-03 and related costs | FY2026 filing: notes remain outstanding; issuer has project covenants and sponsor completion guarantee tied to lease commencement milestones | debt is directly connected to identified physical projects; sponsor must fund shortfall if available proceeds are insufficient for commencement | **Project-specific delivery risk is observable; guarantee existence ≠ guarantee activation** |
| **Applied Digital · 2031 notes / bridge** | March-2026 2031 notes + May-2026 **US$300M** bridge | after FY-end the bridge was refinanced into longer-dated 2031 capital; DSCR covenants reported compliant at 2026-05-31 | project commencement / lease covenants provide a physical-state bridge | **Refinancing completed; covenant state currently contrary evidence to realized stress** |
| **IREN · Microsoft-linked GPU financing** | early-2026 commitment structure | FY2026: approximately **US$3.6B** investment-grade GPU financing around 6%; together with customer prepayments, company says **96% of associated GPU CapEx** is funded | FY2026 AI Cloud Services revenue about **US$128.8M vs US$16.4M FY2025**; company targets cumulative IT delivery of ~0.3GW in 2026 and ~0.8GW in 2027 | **Financing → deployment → monetization bridge is forming; still requires contract/facility-level cash-flow follow-through** |
| **Nebius · first secured facility** | no comparable secured-debt state in prior panel | July-2026: approximately **US$775M**, SOFR + 2.50%, Oct-2030 maturity, 1.15× DSCR covenant, GPU / investment-grade customer cash-flow collateral | Q2 materials show signed-contract and capacity growth, but the public evidence used here does not yet isolate cash flow attributable to this facility | **First secured-facility baseline established; longitudinal draw / DSCR path begins here** |

### 11B.7B Draw ratio is a state variable, not demand

For a delayed-draw facility:

```text
Draw Ratio
=
Drawn Principal
/
Committed Borrowing Capacity
```

This can show project funding progression.

It cannot by itself prove:
- workload utilization;
- customer economics;
- project profitability.

For example, CoreWeave DDTL 4.0 moved from **US$8.5B available** to roughly **US$2.9B drawn** by 2026-06-30.

That is a real financing-state transition.

But the correct interpretation is:

> **capital has moved from commitment toward deployment; monetization must still be tested independently.**

### 11B.7C Monetization bridge

The borrower panel now distinguishes:

```text
Financing Closure
→ Physical Delivery
→ Contract Availability
→ Revenue Recognition
→ Cash Conversion
→ Debt Service
```

Evidence can enter at different points.

IREN currently provides a useful partial bridge:
- project / GPU financing is identified;
- customer prepayments reduce equity funding need;
- AI Cloud Services revenue is already scaling;
- physical IT-capacity targets are stated.

But even there:

> **company-level AI revenue is not automatically facility-level debt-service coverage.**

Future updates should connect:
- the financed GPU / data-center tranche;
- ready-for-service / delivery date;
- recognized revenue;
- customer cash receipt;
- DSCR / interest coverage.

### 11B.7D Facility-state stress protocol

A facility is not moved to a stress state merely because:
- coupon is high;
- leverage is large;
- a delayed-draw facility is only partly drawn;
- a sponsor guarantee exists.

Escalation requires an adverse state transition such as:

```text
Draw / construction progress stalls
+
Delivery milestone slips
or
Customer commitment weakens
or
DSCR / covenant headroom deteriorates
or
Refinancing terms worsen / access fails
```

Conversely, successful refinancing, covenant compliance, project delivery and monetization are explicit contrary evidence.

This makes the facility panel consistent with P0-1's reversible adjudication logic.

---


## 11B.8 Compute Financialization — planned GPU rental futures v0.3

A new market-structure development could eventually change how lenders, AI clouds and infrastructure owners manage compute-price risk.

CME Group and Silicon Data have announced two planned futures contracts:

- **Silicon Data H100 Rental Index Futures**
- **Silicon Data B200 Rental Index Futures**

The contracts are scheduled to begin trading on **October 5, 2026**, pending completion of regulatory review.

CME's technical notices define the unit of measure as:

> **GPU-H — GPU Hours**

and state that each futures contract is based on Silicon Data benchmarks for hourly GPU rental costs.

### 11B.8A Current state: announced / testable, not yet a live liquid market

As of the current **2026-09-03** research state:

~~~text
contract specification announced
+
Globex / clearing support prepared
+
customer testing available
but
live trading not yet started
~~~

Therefore the correct research state is:

> **COMPUTE-DERIVATIVES PRE-LAUNCH**

Do not write:

- a liquid compute futures market already exists;
- H100/B200 forward curves already reveal market consensus;
- lenders already hedge project debt with these contracts;
- GPU rental-price risk has become fully hedgeable.

Those claims require post-launch evidence.

### 11B.8B Why this matters for project finance

If these contracts become liquid enough to support real hedging, the capital stack gains a new risk-management layer.

Conceptually:

~~~text
physical GPU capacity
→ spot / contracted rental price
→ benchmark index
→ futures curve
→ hedge / price discovery
→ potentially lower revenue-volatility uncertainty
→ potentially different lender underwriting
~~~

For an AI-cloud borrower, this could make a previously hard-to-observe variable more explicit:

> **forward market expectation for standardized GPU rental prices.**

That could improve:
- revenue-sensitivity analysis;
- collateral/residual-value modeling;
- refinancing scenarios;
- contract-vs-market basis analysis.

But it does not eliminate:
- utilization risk;
- customer-default risk;
- model / hardware obsolescence;
- geography / power constraints;
- basis risk between a specific facility and the index.

### 11B.8C Futures price ≠ facility economics

The benchmark tracks rental pricing for standardized GPU categories.

A real facility's economics also depend on:

- GPU generation / exact SKU;
- cluster size;
- networking;
- location;
- power cost;
- availability / uptime;
- reserved vs on-demand contract;
- software / support;
- customer credit;
- utilization;
- contract duration.

Therefore:

> **H100/B200 futures cannot be treated as a direct mark-to-market of a data-center project.**

The relevant variable is basis:

~~~text
Facility Realized Rental Economics
-
Benchmark Futures / Index Economics
=
Basis
~~~

A hedge is only economically useful if that basis remains manageable.

### 11B.8D New observables after launch

If the contracts go live, 04C should maintain:

| Variable | Why it matters |
|---|---|
| launch / regulatory state | distinguishes announced product from tradable instrument |
| daily volume | whether market is actually used |
| open interest | persistence / risk transfer rather than one-off prints |
| bid-ask / liquidity | practical hedgeability |
| futures curve | expected rental-price term structure |
| spot-futures basis | hedge effectiveness |
| H100 vs B200 spread | generation / obsolescence signal |
| participant adoption | whether AI clouds / lenders / hyperscalers actually use it |
| collateral / margin burden | hedge can itself consume liquidity |
| correlation with facility revenue | whether the index maps to project cash flow |

### 11B.8E S4 boundary

A declining compute futures curve is **not** by itself Market Clearing or S4.

Possible explanations include:
- expected new supply;
- generation transition;
- efficiency gains;
- index methodology changes;
- lower power / operating cost;
- expected weaker demand.

Escalation requires physical / economic cross-confirmation:

~~~text
futures / rental curve weakens
+
spot rental / resale clearing weakens
+
utilization falls
+
forward commitments fall
+
project refinancing / monetization deteriorates
~~~

Conversely, a steep / expensive forward curve can coexist with poor project economics if:
- utilization is weak;
- customer concentration is high;
- financing cost is excessive.

So compute derivatives are a **new price-discovery input**, not a new standalone clearing signal.

### 11B.8F Financialization can improve and amplify the system

Potential stabilizing effect:
- hedging reduces cash-flow uncertainty;
- lenders can model revenue risk more explicitly;
- standardized price discovery may reduce financing friction.

Potential amplification effect:
- mark-to-market changes become visible faster;
- margin requirements can create liquidity needs;
- forward-curve repricing can affect collateral / underwriting expectations;
- a standardized benchmark can synchronize market expectations.

This is a research hypothesis until post-launch data exists.

### 11B.8G Current adjudication

Current conclusion:

> **The institutional infrastructure for treating GPU compute rental cost as a hedgeable, standardized asset is being built, but the market has not yet demonstrated liquidity, adoption, basis quality, or financing transmission.**

No P0-1 / S4 state change follows from the announcement.

---

## Facility-level longitudinal sources added in v0.2

- CoreWeave Q2 2026 Form 10-Q — DDTL 4.0 / 5.0 draw states, debt maturities, interest expense and subsequent DDTL 5.5 disclosure: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm
- CoreWeave 2026-08-07 Form 8-K — US$2.6B DDTL 5.5 facility and pricing: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000357/crwv-20260807.htm
- CoreWeave Q2 2026 results — revenue backlog / customer commitments used only as company-level demand context, not facility-level monetization proof: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000362/coreweave2q26earningspress.htm
- Core Scientific Q2 2026 Form 10-Q — US$1.0B term loan repayment / termination and US$3.30B 7.75% secured-note refinancing: https://www.sec.gov/Archives/edgar/data/1839341/000183934126000014/core-20260630.htm
- Applied Digital FY2026 Form 10-K — ELN-02 / ELN-03 project financing, completion guarantees, bridge / revolver / notes, DSCR state: https://www.sec.gov/Archives/edgar/data/1144879/000114487926000048/apld-20260531.htm
- IREN FY2026 results — Microsoft-linked GPU financing, customer-prepayment funding coverage, AI Cloud Services revenue and IT-capacity delivery targets: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000051/irenreportsfy26results.htm
- Nebius Q2 2026 shareholder materials — first ~US$775M secured facility and operating / contract / capacity context: https://www.sec.gov/Archives/edgar/data/1513845/000110465926094568/tm2622968d1_ex99-2.htm

## Sources carried from parent register

## Project-finance borrower sources added in v0.13

- Nebius, 2026-07-17 — ~US$775M first senior secured facility, SOFR + 2.50%, October-2030 maturity, backed by deployed GPUs and investment-grade customer contracted cash flows: https://nebius.com/newsroom/nebius-raises-775-million-in-first-secured-debt-financing-to-accelerate-global-buildout
- Nebius Q2 2026 filing — secured-facility identity and collateral structure: https://www.sec.gov/Archives/edgar/data/1513845/000110465926094844/nbis-20260812xex99d2.htm
- Applied Digital FY2026 Form 10-K — debt stack, weighted-average rate and principal-payment schedule: https://www.sec.gov/Archives/edgar/data/1144879/000114487926000048/apld-20260531.htm
- IREN, 2026-02-05 — Microsoft GPU financing / prepayment structure: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000014/a991irenreportsq2fy26res.htm
- IREN Q3 FY26 filing — binding ~US$3.6B GPU financing commitment backed by Microsoft-related GPUs / cash flows: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000026/iren-20260331.htm
- IREN FY26 results, 2026-08-27 — additional GPU financings, customer prepayments and legacy Bitcoin-mining impairment identity: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000051/irenreportsfy26results.htm



## Compute-financialization sources added in v0.3

- CME Group, 2026-08-11, “CME Group and Silicon Data to Launch Compute Futures on October 5 to Unlock New Way to Hedge AI Risks”: https://www.cmegroup.com/media-room/press-releases/2026/8/11/cme_group_and_silicondatatolaunchcomputefuturesonoctober5tounloc.html
- CME Group Globex Notice, 2026-08-17 — planned H100/B200 Compute Futures, GPU-H unit-of-measure support and October-5 launch schedule pending regulatory review: https://www.cmegroup.com/notices/electronic-trading/2026/08/20260817.html
- CME Group, Compute Futures product page — benchmark / hedging design and pending-regulatory-review status: https://www.cmegroup.com/markets/energy/power/compute-futures.html
