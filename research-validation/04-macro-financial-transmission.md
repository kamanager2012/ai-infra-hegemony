# P0-4 · Macro-Financial Transmission Layer v0.11

> **Status:** Research-side validation; not part of the frozen formal report.  
> **Goal:** make interest rates, credit conditions, valuation, financing structure and refinancing explicit state variables in the AI-infrastructure capital cycle.

## 1. The missing chain

The report already models:

> CapEx → asset deployment → utilization / monetization → depreciation → capital clearing

The missing macro-financial chain is:

> **Risk-free rate → credit spread / lending standards → cost of debt & equity → WACC / hurdle rate → project NPV / financing capacity → CapEx timing → refinancing / impairment risk**

S4 is not simply “rates rise.”

The relevant question is:

> **Do financing conditions become restrictive enough, relative to project cash generation and sponsor balance-sheet strength, to delay/cancel buildout or make refinancing uneconomic?**

---

## 2. Six observable macro-financial state variables

### MF1 — Risk-free rate / term structure

Observe:
- policy rate;
- 2Y / 10Y Treasury yields;
- term premium where available.

Role:
- raises the base discount rate;
- affects long-duration project NPV;
- affects lease / debt refinancing economics.

### MF2 — Credit spread

Observe separately:
- investment-grade spread;
- high-yield spread;
- leveraged-loan spread;
- private-credit pricing where observable.

Role:
- identifies whether the market is repricing borrower/project risk beyond the risk-free move.

### MF3 — Lending standards / credit availability

Primary U.S. public proxy:
- Federal Reserve **Senior Loan Officer Opinion Survey (SLOOS)**.

Role:
- captures non-price rationing;
- matters when a project cannot obtain the same leverage or maturity even if nominal rates appear manageable.

### MF4 — Equity cost / valuation support

Observe:
- sector valuation;
- equity risk premium;
- ability to issue equity without severe dilution;
- sponsor stock-price / earnings sensitivity.

Role:
- high valuations can lower effective equity financing cost and support aggressive CapEx;
- valuation compression can raise hurdle rates even before bank credit disappears.

### MF5 — Project-finance structure

Observe:
- corporate balance-sheet funding;
- project debt;
- lease / synthetic lease;
- SPV;
- private credit;
- supplier credit enhancement;
- third-party infrastructure capital;
- guarantees / minimum payments.

Role:
- determines who actually bears demand, residual-value and duration risk.

### MF6 — Refinancing / maturity wall

Observe:
- debt maturities;
- floating vs fixed rate;
- covenant headroom;
- refinancing spread;
- DSCR / interest coverage where available;
- extension / amend-and-extend behavior.

Role:
- turns a valuation problem into a cash-flow problem.

---

## 3. Project-level transmission

A minimum project model should represent:

```text
Project Value
=
PV(Expected Operating Cash Flow, WACC)
- Initial CapEx
- Required Future CapEx
```

with:

```text
WACC
=
Debt Weight × After-tax Cost of Debt
+
Equity Weight × Cost of Equity
```

The research layer does **not** need one universal WACC for AI infrastructure.

It needs to track whether:
- WACC rises;
- expected utilization/revenue falls;
- construction cost rises;
- schedule slips;
- residual value falls

at the same time.

That combination can flip marginal projects from expansion to deferral/cancellation.

---

## 4. Why hyperscalers and project-financed AI assets must be separated

Cash-rich hyperscalers can self-finance large CapEx and may remain relatively insensitive to ordinary bank tightening.

A highly leveraged:
- data-center developer;
- SPV;
- neocloud;
- power project;
- supplier-supported customer

can be much more rate-sensitive.

Therefore the report should never use:

> “Fed tightened”

as a direct proxy for:

> “hyperscaler AI CapEx must fall.”

The correct state variable is **financing sensitivity by capital structure**.

---

## 5. Historical lesson from P0-1

The 2008–2009 enterprise-IT backtest already showed:

- investment collapsed;
- firms postponed/abandoned expansion;
- credit availability and cost deteriorated;
- yet Cisco did not need a 2001-style giant write-down for the macro clearing to be real.

This means **Accounting cannot be the only hard confirmation** when the shock enters through financing conditions.

Macro-financial variables can lead the accounting signal.

---

## 6. Current 2026 baseline

The correct 2026 reading is mixed rather than “credit is tight” or “money is easy.”

Federal Reserve 2026 SLOOS:
- January: banks reported tighter C&I standards on balance;
- April: standards again tightened on balance;
- July: C&I standards were basically unchanged on balance.

Federal Reserve May 2026 Financial Stability Report:
- corporate bond spreads remained low by historical standards;
- investment-grade corporate credit quality remained robust;
- some riskier firms, especially those relying on floating-rate leveraged loans/private credit, faced debt-servicing pressure;
- bank commitments to nonbank financial institutions remained large and private-credit exposures continued growing.

This combination implies:

> **there is no economy-wide credit seizure, but borrower sensitivity is increasingly heterogeneous.**

That is exactly why AI infrastructure needs a borrower/project-level financing map.

---

## 7. Current AI-infrastructure financing transition

Goldman Sachs’ 2026 public research emphasizes two simultaneous facts:

1. AI/hyperscaler CapEx estimates remain extremely high;
2. investors are becoming more selective about businesses where CapEx is debt-funded or where operating-earnings growth does not clearly justify the investment.

The report’s existing NVIDIA financing evidence adds a third development:
- supplier / ecosystem balance sheets are increasingly participating through equity, credit support, guarantees and third-party capital-mobilization structures.

Therefore the financing question is no longer only:

> “How much CapEx can hyperscalers fund from cash flow?”

It is also:

> **“How much long-duration AI infrastructure risk is migrating into debt, SPVs, private credit, guarantees and third-party infrastructure capital?”**

---

## 8. 2026 empirical transmission panel: from bank standards to AI infrastructure debt

The 2026 data now allow the framework to move from generic macro variables into observable transmission.

### 8.1 Bank credit is not uniformly tight — but AI exposure is already affecting credit allocation

Federal Reserve SLOOS:

- **January 2026:** banks reported tighter C&I standards on balance;
- **April 2026:** C&I standards again tightened, and banks reported tighter standards across all queried categories of loans to nondepository financial institutions (NDFIs);
- **July 2026:** C&I standards were basically unchanged, while current standards for many NDFI loan categories remained toward the tighter end of their historical ranges.

The January survey added an unusually relevant AI-specific special question.

The January special question provides an unusually concrete cross-section.

Among the **17 responding banks**:

- for firms **benefiting from high AI exposure**, **35.3%** were more likely to approve C&I loans than in January 2025, while **64.7%** were about as likely and none were less likely;
- for firms **adversely affected by high AI exposure**, **70.6%** were less likely to approve, **23.5%** were about as likely, and **5.9%** were more likely;
- for firms with **little AI exposure**, **94.1%** reported no change in approval likelihood.

These are survey responses, not realized loan-flow shares, and the sample is small.

But they are direct evidence that AI is beginning to enter credit allocation not only through borrower growth, but through lenders' assessment of business-model exposure.

The implication is:

> **AI can simultaneously loosen financing for perceived winners and tighten it for perceived losers.**

So “AI boom” does not imply a uniform reduction in cost of capital.

### 8.1A A useful asymmetry: AI exposure is becoming a credit-screening variable

The SLOOS result is more informative as an **asymmetry** than as a bullish macro signal.

The same technology shock can produce:

```text
perceived AI beneficiary
→ easier marginal credit approval

perceived AI loser
→ tighter marginal credit approval
```

while aggregate C&I standards remain tight or unchanged.

This means Phase II should not model “AI” as one common financing factor.

A more useful borrower panel is:

| Borrower class | Operating exposure | Financing channel | Expected transmission |
|---|---|---|---|
| cash-rich hyperscaler | AI beneficiary | retained cash + public debt | weak bank-credit sensitivity |
| neocloud / AI infra developer | AI beneficiary but capital intensive | project debt / private credit / contract-backed debt | high financing-structure sensitivity |
| supplier | AI beneficiary | operating cash + customer commitments | working-capital / capacity-finance sensitivity |
| traditional firm benefiting from AI | positive | C&I / public credit | potentially easier marginal approval |
| firm judged adversely exposed to AI | negative | C&I / leveraged credit | potentially tighter approval / refinancing |

The scenario implication is not “credit flows to AI.”

It is:

> **credit allocation is beginning to differentiate by perceived AI exposure, which can amplify the Two-Speed economy outside semiconductor allocation itself.**

This should remain a macro-financial amplifier, not a new standalone S1–S4 signal.

### 8.2 Public credit remains open while risk migration grows

The Federal Reserve May 2026 Financial Stability Report states:

- corporate bond spreads remained low by historical standards;
- overall business/household debt vulnerabilities remained moderate;
- private credit had grown to roughly **US$1.4T**, about **10% of U.S. nonfinancial corporate debt** and roughly one-third of below-investment-grade debt excluding bank loans;
- some nontraded BDCs experienced increased redemption pressure;
- private-credit and AI risks were increasingly cited in market outreach.

This supports the current baseline:

> **no system-wide credit seizure, but more risk is being intermediated outside traditional bank balance sheets.**

That is especially relevant to neoclouds, SPVs and data-center developers.

### 8.3 CoreWeave: project finance has become a first-order AI-infrastructure variable

CoreWeave's 2026 filings provide a concrete borrower-level case.

As of **June 30, 2026**:

- delayed-draw term loan facilities outstanding: about **US$13.6B**;
- aggregate principal amount of notes outstanding: about **US$16.6B**;
- delayed-draw facilities are collateralized by assets and pledged contractual cash flows, generally from investment-grade counterparties;
- the company also uses OEM / software-license financing;
- a revolver provided another **US$2.0B** of remaining capacity.

A March 2026 financing announcement also disclosed an **US$8.5B** delayed-draw facility rated A3 / A(low), described as the first investment-grade rated financing of its type backed by HPC infrastructure and an associated customer contract.

This demonstrates a real transmission chain:

```text
long-duration customer contract
→ pledged contractual cash flow
→ asset-level / non-recourse debt
→ infrastructure construction
→ deployed AI capacity
```

This is materially different from hyperscaler self-financing.

### 8.4 Counterparty concentration can transmit through the stack

Core Scientific provides the opposite side of the same chain.

In its 2026 Q2 filing:

- CoreWeave represented about **77% of total revenue** for the first half of 2026;
- colocation revenue was entirely derived from CoreWeave;
- the company explicitly states that financial results, liquidity and cash flows depend on CoreWeave's performance.

Its investor materials further describe:

- about **590 MW** of infrastructure tied to CoreWeave contracts;
- revenues from those contracts flowing into a lockbox associated with **US$3.3B senior secured notes**.

This creates a visible dependency graph:

> **AI lab / end customer → CoreWeave contract → CoreWeave debt → Core Scientific lease/cash flow → Core Scientific debt**

A weakening at the top of the chain can therefore propagate before any industry-wide impairment appears.

### 8.5 What this changes in the S4 monitor

The macro panel should now add four project-level quantities:

1. **Contract-backed debt / total debt**;
2. **single-customer or anchor-customer revenue concentration**;
3. **debt service supported by pledged customer cash flows**;
4. **supplier / sponsor / OEM financing share**.

These variables make Demand Quality / Financing more operational.

---

## 9. Macro-Financial Stress Matrix

| State | Risk-free / spreads | Lending / refinancing | Utilization / monetization | Interpretation |
|---|---|---|---|---|
| MF-A | benign | available | strong | expansion can remain durable |
| MF-B | higher base rates | available but pricier | strong | margin/NPV compression; not S4 |
| MF-C | higher rates + wider spreads | tighter | mixed | marginal projects delay; S4 risk rises |
| MF-D | wide spreads / rationing | refinancing impaired | weak | strong S4 confirmation |
| MF-E | rates fall because growth collapses | credit still tight | weak | easing policy does not imply recovery |

This prevents one common error:

> lower policy rates after a downturn are not evidence that financing stress has ended.

---

## 10. S4 integration rule

Macro-financial conditions should increase S4 weight only when at least one capital-market deterioration **transmits into a real project or buyer variable**, such as:

- CapEx guidance reduction attributable to financing/ROI;
- project delay/cancellation;
- covenant/refinancing stress;
- rising supplier support needed to close financing;
- lower leverage / shorter maturity / higher spread;
- equity issuance at materially worse terms;
- asset sale / distressed refinancing;
- utilization weakness combined with higher financing cost.

Rates/spreads without project transmission remain **context**, not S4 evidence.

---

## 10A. 2022–2026 quarterly macro-financial panel v0.1

The first reproducible quarterly backbone is now populated with four variables:

- **Fed Funds:** effective federal funds rate, quarter-ending month average;
- **10Y:** 10-year Treasury constant-maturity yield, quarter-ending month average;
- **SLOOS standards:** net percentage of domestic banks tightening C&I standards for large / middle-market firms;
- **SLOOS demand:** net percentage reporting stronger C&I demand from large / middle-market firms.

Important frequency rule:

> **Fed Funds / 10Y are monthly averages from the quarter-ending month. SLOOS uses the survey-quarter label and generally describes changes over the preceding three months.**

The table therefore aligns monitoring windows; it does **not** claim same-day observation.

| Quarter | Fed Funds % | 10Y % | SLOOS tightening % | SLOOS stronger demand % | Macro reading |
|---|---:|---:|---:|---:|---|
| 2022Q1 | 0.20 | 2.13 | -14.5 | 21.7 | easy bank standards, strong demand; hiking cycle begins |
| 2022Q2 | 1.21 | 3.14 | -1.5 | 12.3 | rates rise sharply; standards near neutral |
| 2022Q3 | 2.56 | 3.52 | 24.2 | 24.2 | tightening begins while reported demand remains positive |
| 2022Q4 | 4.10 | 3.62 | 39.1 | -8.8 | monetary tightening and bank standards now align; demand turns weaker |
| 2023Q1 | 4.65 | 3.66 | 44.8 | -31.3 | tighter credit + weaker demand |
| 2023Q2 | 5.08 | 3.75 | 46.0 | -55.6 | peak broad credit restraint in this panel |
| 2023Q3 | 5.33 | 4.38 | 50.8 | -51.6 | standards remain very tight; long rates rise |
| 2023Q4 | 5.33 | 4.02 | 33.9 | -30.5 | still restrictive, but standards begin easing from peak |
| 2024Q1 | 5.33 | 4.21 | 14.5 | -25.0 | policy rate high; bank tightening materially less severe |
| 2024Q2 | 5.33 | 4.31 | 15.6 | -26.6 | restrictive but no renewed broad tightening wave |
| 2024Q3 | 5.13 | 3.72 | 7.9 | 0.0 | rates begin easing; C&I demand stabilizes |
| 2024Q4 | 4.48 | 4.39 | 0.0 | -21.3 | standards neutral on net; long yield rebounds |
| 2025Q1 | 4.33 | 4.28 | 6.2 | 9.4 | mild tightening, positive demand |
| 2025Q2 | 4.33 | 4.38 | 18.5 | -20.3 | bank standards tighten again despite stable policy rate |
| 2025Q3 | 4.22 | 4.12 | 9.5 | -28.6 | credit still selective; demand weak |
| 2025Q4 | 3.72 | 4.14 | 6.5 | 11.5 | policy easing with improving demand |
| 2026Q1 | 3.64 | 4.25 | 5.3 | 16.1 | aggregate bank credit no longer crisis-tight; demand positive |
| 2026Q2 | 3.63 | 4.47 | 8.1 | 4.8 | modest tightening persists while long rates remain elevated |

**Sources:** Federal Reserve / FRED series FEDFUNDS, GS10, DRTSCILM and DRSDCILM.

### 10A.1 What the panel already falsifies

This backbone rejects two simplistic narratives.

**Narrative A — “Higher rates automatically cause AI hard landing.”**

False in the observed 2023–2026 window:
- rates remained high;
- C&I standards were restrictive;
- yet AI infrastructure commitments and project financing continued expanding.

Therefore higher rates alone remain **MF context**, not S4 confirmation.

**Narrative B — “Policy easing means financing stress is gone.”**

Also false:
- Fed Funds fell from the 2023–2024 peak;
- but long yields remained around / above 4%;
- SLOOS standards repeatedly stayed positive;
- private-credit / NDFI conditions remained selective.

So financing conditions are multidimensional.

### 10A.2 AI-specific overlay

The aggregate panel must be read beside AI-specific financing evidence:

| Window | AI-specific observation | Interpretation |
|---|---|---|
| 2025Q4 / Jan-2026 survey | 35.3% of 17 responding banks more willing to approve firms benefiting from high AI exposure; 70.6% less willing for firms adversely affected | AI exposure enters credit screening as a two-speed allocator |
| 2026Q1 | CoreWeave announces US$8.5B investment-grade delayed-draw term-loan facility backed by HPC infrastructure / customer contract | long-duration customer contracts are being transformed into debt capacity |
| 2026Q2 | CoreWeave reports ~US$13.6B DDTLs and ~US$16.6B notes outstanding; contractual cash flows are pledged in parts of the structure | financing quantity has scaled; contract quality / concentration become first-order variables |
| 2026Q2 | Core Scientific reports CoreWeave ~77% of H1 revenue, with contract cash flows supporting a debt lockbox structure | counterparty risk can propagate downstream before aggregate credit markets seize |

This produces a more precise interpretation:

> **2022–2023 was a broad macro-credit tightening cycle; by 2025–2026 the aggregate system is less uniformly restrictive, while AI-linked capital allocation becomes more borrower- and contract-specific.**

That is closer to a Two-Speed financing regime than to an economy-wide credit seizure.

### 10A.3 Public-credit proxy rule: observable is not the same as republishable

The initial worklist called for a quarterly IG / HY OAS backfill.

A source-governance audit changes that plan.

The commonly used ICE BofA OAS series surfaced through FRED are third-party licensed data. FRED's series notes explicitly state that the underlying ICE index data are proprietary and restrict redistribution of the top-level observations.

Therefore Phase II will **not** copy a historical IG / HY OAS time series into this repository merely because it is viewable online.

Instead:

- ICE BofA IG / HY OAS remain **external cross-check variables**;
- the reproducible public panel uses Federal Reserve-produced / Federal Reserve Bank research indicators where possible;
- source-license identity is now part of the data-quality protocol.

Preferred public credit-state proxies:

1. **NY Fed Corporate Bond Market Distress Index (CMDI)**  
   - combines primary issuance/pricing, secondary-market pricing/liquidity, and relative traded/nontraded bond pricing;
   - provides aggregate as well as investment-grade / high-yield segment readings;
   - is specifically designed to identify widespread corporate-bond-market distress.

2. **Chicago Fed NFCI Credit Subindex**  
   - weekly credit-conditions subindex;
   - positive values indicate tighter-than-average credit conditions; negative values indicate looser-than-average conditions.

This changes the research objective from:

> “republish an IG/HY spread table”

to:

> **maintain a legally reproducible public-credit state panel, while using proprietary spread indices only as external validation.**

The distinction matters for a publication-grade repository.

### 10A.4 2026Q2 hyperscaler self-financing cross-section

A second financing layer is now observable directly from company filings / earnings disclosures.

The comparison must keep each company's CapEx definition intact rather than forcing one false common denominator.

| Company / period | Operating cash flow | CapEx / infrastructure spend | External financing / balance-sheet observation | Research interpretation |
|---|---:|---:|---|---|
| Microsoft FY26 Q4 | US$55.4B | US$41.0B total CapEx; cash paid for PP&E US$35.8B; ~2/3 short-lived assets | finance leases US$5.6B, mainly large data-center sites | OCF still exceeds current-quarter investment, but leases and long-lived sites remain a material financing layer |
| Alphabet 2026Q2 | US$39.1B | US$44.9B CapEx, primarily technical infrastructure | ~US$49.6B net equity raise + US$20.3B senior notes in Q2 | even a cash-rich platform can combine internal cash generation with large external capital raises when infrastructure intensity jumps |
| Meta 2026Q2 | US$31.86B | US$31.08B CapEx including finance-lease principal | US$90.26B cash/securities; US$83.66B long-term debt | current-quarter OCF and CapEx are nearly matched; self-financing capacity exists, but balance-sheet leverage is no longer irrelevant |
| Amazon 2026Q2 | US$45.4B | US$53.1B cash CapEx; majority supports technology infrastructure / AWS growth | TTM FCF -US$7.6B; PP&E purchases rose sharply YoY | infrastructure growth can outrun current-quarter OCF even while AWS operating income remains strong |

**Definition warning:** these rows are **not** one harmonized accounting ratio.

- Microsoft total CapEx includes finance-lease effects while separately reporting cash PP&E;
- Meta CapEx includes principal payments on finance leases;
- Amazon reports cash capital expenditures;
- Alphabet reports conventional CapEx.

Therefore Phase II does **not** rank companies by a synthetic “OCF/CapEx league table.”

The robust result is directional:

> **hyperscaler AI infrastructure is still supported by very large operating cash flows, but external equity, public debt, finance leases and negative/near-zero free-cash-flow outcomes are becoming more visible as infrastructure intensity rises.**

This weakens two simplistic statements at once:

- “hyperscalers are self-funded, therefore financing does not matter”;
- “external financing proves AI demand is weak.”

The relevant state variables are:
- operating cash generation;
- cash vs non-cash / lease CapEx;
- incremental debt/equity issuance;
- asset life;
- customer commitments;
- refinancing need.

### 10A.5 2022–2025 hyperscaler annual self-funding history

The 2026Q2 cross-section is useful, but one quarter can mislead.

Phase II therefore adds a first annual history using each company's own disclosed accounting identity.

**Do not compare the CapEx columns as if they were one standardized denominator.**

| Company | 2022 | 2023 | 2024 | 2025 | Read-through |
|---|---|---|---|---|---|
| Microsoft | OCF **US$89.0B**; PP&E additions **US$23.9B** | OCF **US$87.6B**; PP&E additions **US$28.1B** | OCF **US$118.5B**; PP&E additions **US$44.5B** | OCF **US$136.2B**; PP&E additions **US$64.6B** | OCF grew materially while infrastructure investment accelerated; debt issuance is available but operating self-funding remains large |
| Alphabet | OCF **US$91.5B**; CapEx **US$31.5B** | OCF **US$101.7B**; CapEx **US$32.3B** | OCF **US$125.3B**; CapEx **US$52.5B** | OCF **US$164.7B**; CapEx **US$91.4B** | investment intensity rises faster after 2023; company still generates very large OCF while also using external debt/equity capacity |
| Meta | OCF **US$50.5B**; PP&E **US$31.4B** (+ finance-lease principal **US$0.85B**) | OCF **US$71.1B**; PP&E **US$27.0B** (+ lease principal **US$1.06B**) | OCF **US$91.3B**; PP&E **US$37.3B** (+ lease principal **US$1.97B**) | OCF **US$115.8B**; PP&E **US$69.7B** (+ lease principal **US$2.52B**) | operating cash generation expanded, but AI/infrastructure investment and long-term debt / future lease commitments also expanded sharply |
| Amazon | OCF **US$46.8B**; PP&E purchases **US$63.6B** | OCF **US$84.9B**; PP&E purchases **US$52.7B** | OCF **US$115.9B**; PP&E purchases **US$83.0B** | OCF **US$139.5B**; PP&E purchases **US$131.8B** | OCF recovered strongly after 2022, but infrastructure / PP&E intensity accelerated again and 2025 gross PP&E purchases approached annual OCF |

### 10A.5A Definition controls

The annual history is **not** a synthetic four-company cash-coverage league table.

- **Microsoft:** uses cash-flow-statement additions to property and equipment; quarterly total CapEx can additionally include finance leases.
- **Alphabet:** uses reported capital expenditures, primarily technical infrastructure in the current AI build cycle.
- **Meta:** cash-flow-statement PP&E purchases are shown separately from finance-lease principal; Meta's headline CapEx guidance/results often include both.
- **Amazon:** cash-flow statement reports gross PP&E purchases, while Amazon's free-cash-flow reconciliation uses PP&E net of asset-sale proceeds / incentives.

Therefore:

> **A cross-company ratio should not be calculated unless the denominator is explicitly harmonized.**

The useful signal is the **trajectory within each company**.

### 10A.5B What the annual panel shows

The 2022–2025 history weakens two opposite narratives.

**“The AI build is simply debt-funded.”**

Not supported:
- operating cash generation expanded substantially at all four platforms by 2025;
- Microsoft, Alphabet, Meta and Amazon all retained very large internal funding capacity.

**“Because OCF is large, financing structure no longer matters.”**

Also not supported:
- CapEx / infrastructure spend accelerated materially;
- Meta increased long-term debt and accumulated large not-yet-commenced data-center / network lease obligations;
- Alphabet explicitly uses debt/equity issuance alongside cash generation;
- Microsoft uses finance leases for large data-center sites;
- Amazon's 2025 PP&E investment increased much faster than its OCF and financing inflows turned positive.

The correct interpretation is:

> **the hyperscaler build remains fundamentally cash-generative, but the marginal infrastructure dollar is increasingly financed through a broader mix of retained cash, debt, equity, leases and long-duration contractual commitments.**

That is not an S4 signal.

It becomes an S4-relevant signal only if:
- OCF growth weakens;
- CapEx remains rigid;
- external financing becomes more expensive / dilutive;
- utilization or monetization weakens;
- commitments cannot be resized.

### 10A.5C A first self-funding stress variable

Phase II can now define a non-ranking monitor:

```text
Self_Funding_Headroom
=
Operating Cash Flow
-
Comparable Cash Infrastructure / PP&E Spend
```

But this variable is valid **only within a company and within a stable accounting definition**.

It must not be compared mechanically across firms.

The direction is useful:

- rising headroom → more internal capacity to absorb buildout;
- falling headroom → greater sensitivity to debt/equity/lease amplification;
- negative headroom → not automatically distress, but external financing / balance-sheet support becomes more economically relevant.

---

### 10A.5D Quarterly pilot — Meta 2024Q1–2026Q2

Meta provides one of the cleanest public quarterly histories because its earnings materials report, for the same quarter:

- operating cash flow;
- purchases of property and equipment;
- principal payments on finance leases;
- company-defined free cash flow.

That allows a within-company quarterly pilot without denominator reconstruction.

| Quarter | OCF US$B | PP&E US$B | Finance-lease principal US$B | Company-defined CapEx US$B | Self-funding headroom / FCF US$B |
|---|---:|---:|---:|---:|---:|
| 2024Q1 | 19.246 | 6.400 | 0.315 | 6.715 | 12.531 |
| 2024Q2 | 19.370 | 8.173 | 0.299 | 8.472 | 10.898 |
| 2024Q3 | 24.724 | 8.258 | 0.944 | 9.202 | 15.522 |
| 2024Q4 | 27.988 | 14.425 | 0.411 | 14.836 | 13.152 |
| 2025Q1 | 24.026 | 12.941 | 0.751 | 13.692 | 10.334 |
| 2025Q2 | 25.561 | 16.538 | 0.474 | 17.012 | 8.549 |
| 2025Q3 | 29.999 | 18.829 | 0.545 | 19.374 | 10.625 |
| 2025Q4 | 36.214 | 21.383 | 0.754 | 22.137 | 14.077 |
| 2026Q1 | 32.226 | 18.997 | 0.843 | 19.840 | 12.386 |
| 2026Q2 | 31.862 | 30.116 | 0.962 | 31.078 | 0.784 |

**Identity rule:** for this Meta pilot only:

```text
Company-defined CapEx
=
PP&E purchases
+
finance-lease principal
```

and:

```text
Self-funding headroom
=
OCF
-
Company-defined CapEx
=
Meta-reported FCF
```

### What the pilot shows

The important signal is not that Meta's 2026Q2 free cash flow is “low.”

The important signal is the **compression in headroom while investment is still being expanded**:

- 2024Q1–2025Q4: quarterly headroom remains strongly positive;
- 2026Q1: still US$12.4B;
- 2026Q2: falls to only about **US$0.8B** as quarterly CapEx rises to about **US$31.1B**;
- at the same time Meta raises 2026 CapEx guidance to **US$130–145B** and continues to expect 2026 operating income above 2025.

This is **not S4 confirmation**.

It is an example of a transition from:

> **high internal cash generation + moderate infrastructure intensity**

toward:

> **high internal cash generation + much higher infrastructure intensity + greater relevance of balance-sheet / debt capacity**

The correct monitor is therefore:

> **Does self-funding headroom compress because infrastructure investment is accelerating into still-strong monetization, or because operating cash generation / utilization is deteriorating?**

Those are economically opposite states.

### 10A.5E Quarterly pilot — Alphabet 2024Q1–2026Q2

Alphabet is the second clean quarterly case because its filings report quarter-specific:

- operating cash flow;
- capital expenditures;
- company-defined free cash flow = OCF − CapEx.

| Quarter | OCF US$B | CapEx US$B | Self-funding headroom / FCF US$B |
|---|---:|---:|---:|
| 2024Q1 | 28.8 | 12.0 | 16.8 |
| 2024Q2 | 26.6 | 13.2 | 13.4 |
| 2024Q3 | 30.7 | 13.1 | 17.6 |
| 2024Q4 | 39.1 | 14.3 | 24.8 |
| 2025Q1 | 36.2 | 17.2 | 19.0 |
| 2025Q2 | 27.7 | 22.4 | 5.3 |
| 2025Q3 | 48.4 | 24.0 | 24.4 |
| 2025Q4 | 52.4 | 27.9 | 24.6 |
| 2026Q1 | 45.8 | 35.7 | 10.1 |
| 2026Q2 | 39.1 | 44.9 | **-5.9** |

### What the Alphabet pilot shows

The sequence is not monotonic.

- 2024: headroom remains strongly positive while technical-infrastructure CapEx rises.
- 2025Q2: headroom compresses sharply as CapEx steps up.
- 2025H2: OCF rebounds strongly and headroom widens again.
- 2026Q1: CapEx rises to roughly US$35.7B while headroom remains positive.
- 2026Q2: CapEx reaches roughly **US$44.9B**, exceeding quarterly OCF of roughly **US$39.1B** and producing company-defined FCF of about **-US$5.9B**.

At the same time:

- Alphabet had guided 2026 CapEx to **US$175–185B**;
- Q2 2026 financing included roughly **US$49.6B** of net equity proceeds explicitly available for general corporate purposes including scaling AI infrastructure / global compute;
- Q1 2026 also included **US$31.1B** of senior-note net proceeds.

This is a clean example of **Layer 1 self-funding compression being offset by Layer 2 balance-sheet amplification**.

It is not, by itself, a distress event.

### 10A.5F Meta vs Alphabet: same headroom signal, different financing state

Both Meta and Alphabet show rapid 2026 infrastructure-intensity increases.

But the signal must be decomposed:

| 2026Q2 | Meta | Alphabet |
|---|---:|---:|
| OCF | US$31.9B | US$39.1B |
| Company-comparable infrastructure CapEx | US$31.1B | US$44.9B |
| Headroom / FCF | US$0.8B | **-US$5.9B** |
| Balance-sheet financing observation | US$24.9B long-term debt issuance in Q2 | ~US$49.6B equity raise in Q2; US$31.1B senior notes in Q1 |

The correct read is not:

> “Alphabet is in worse shape than Meta.”

The correct read is:

> **both firms are moving from abundant self-funding headroom toward a regime where corporate financing structure becomes more relevant to marginal infrastructure expansion.**

To turn this into S4 evidence, the panel would still need deterioration in:
- cloud / AI monetization;
- utilization;
- financing terms;
- forward commitments;
- or asset impairment / retrenchment.

Without those, the current state is better described as **high-intensity expansion with balance-sheet amplification**.

---

### 10A.5G Quarterly pilot — Microsoft FY24Q1–FY26Q4

Microsoft should retain its own fiscal-quarter labels.

Its disclosures distinguish:

- operating cash flow;
- cash paid for PP&E;
- total CapEx including finance leases;
- free cash flow = OCF − cash PP&E.

This is useful because **cash infrastructure spend and recognized CapEx can diverge materially**.

| Microsoft fiscal quarter | OCF US$B | Cash PP&E US$B | Free cash flow US$B | Total CapEx incl. finance leases US$B |
|---|---:|---:|---:|---:|
| FY24Q1 | 30.6 | 9.9 | 20.7 | 11.2 |
| FY24Q2 | 18.9 | 9.7 | 9.1 | 11.5 |
| FY24Q3 | 31.9 | 11.0 | 21.0 | 14.0 |
| FY24Q4 | 37.2 | 13.9 | 23.3 | 19.0 |
| FY25Q1 | 34.2 | 14.9 | 19.3 | 20.0 |
| FY25Q2 | 22.3 | 15.8 | 6.5 | 22.6 |
| FY25Q3 | 37.0 | 16.7 | 20.3 | 21.4 |
| FY25Q4 | 42.6 | 17.1 | 25.6 | 24.2 |
| FY26Q1 | 45.1 | 19.4 | 25.7 | 34.9 |
| FY26Q2 | 35.8 | 29.9 | 5.9 | 37.5 |
| FY26Q3 | 46.7 | 30.9 | 15.8 | 31.9 |
| FY26Q4 | 55.4 | 35.8 | 19.6 | 41.0 |

### 10A.5H Why Microsoft needs two capital clocks

For Microsoft:

```text
Cash self-funding clock
=
OCF - cash PP&E

Recognized infrastructure-commitment clock
=
total CapEx including finance leases
```

These clocks can move differently.

Examples:

- FY26Q1 total CapEx was **US$34.9B**, but cash PP&E was **US$19.4B**; roughly US$11.1B of finance leases were primarily large data-center sites.
- FY26Q2 total CapEx was **US$37.5B**, cash PP&E **US$29.9B**, and finance leases **US$6.7B**.
- FY26Q3 total CapEx fell to **US$31.9B**, while cash PP&E stayed high at **US$30.9B** because finance-lease timing shifted.
- FY26Q4 total CapEx rose to **US$41.0B**, cash PP&E **US$35.8B**, with finance leases **US$5.6B**.

Therefore:

> **cash FCF alone understates some long-duration infrastructure commitments, while total CapEx alone can overstate current-period cash drain.**

Both clocks must be monitored.

### 10A.5I Headroom compression is not enough: demand breadth matters

Microsoft provides a useful demand-quality overlay.

FY26Q2:
- free cash flow compressed to about **US$5.9B**;
- commercial RPO reached about **US$625B**;
- approximately **45%** of RPO was from OpenAI.

That means strong contracted demand coexisted with a meaningful concentration variable.

By FY26Q4:
- commercial RPO rose to about **US$678B**;
- Microsoft stated that **all sequential commercial RPO growth was driven by customers outside frontier model companies**;
- RPO growth excluding OpenAI was **25%**;
- nearly **90% of full-year Microsoft Cloud revenue** came from customers outside frontier model companies.

This is important counterevidence against a simple:

> “frontier-model financing is the only demand engine”

narrative.

The S4 monitor should therefore pair:

```text
Self-funding headroom
+
recognized CapEx
+
customer concentration
+
broad-customer RPO growth
```

A headroom squeeze with broadening contracted demand is structurally different from a headroom squeeze caused by weak monetization and shrinking commitments.

### 10A.5J Cross-company lesson after Meta + Alphabet + Microsoft

Three quarterly pilots now show why the same FCF signal can mean different things:

| Pattern | Possible interpretation |
|---|---|
| FCF compresses + CapEx rises + demand broadens | high-intensity expansion |
| FCF compresses + external financing rises + demand remains strong | balance-sheet amplification |
| FCF compresses + customer concentration rises | financing / demand-quality sensitivity increases |
| FCF compresses + utilization / bookings / RPO weaken | S4 weight rises |
| FCF improves because CapEx is cut while demand weakens | not automatically recovery |

Therefore the quarterly panel should never classify S4 from free cash flow alone.

---

### 10A.5K Quarterly pilot — Amazon 2024Q1–2026Q2

Amazon's quarterly pilot requires a different denominator warning.

Its disclosed **cash capital expenditures** primarily reflect:

- technology infrastructure, the majority of which supports AWS growth;
- fulfillment-network capacity.

Therefore Amazon is a **company-level capital-intensity case**, not a pure AWS infrastructure denominator.

Using Amazon's own quarter / YTD cash-capex disclosures:

| Quarter | OCF US$B | Amazon cash CapEx US$B | Company-level cash headroom US$B |
|---|---:|---:|---:|
| 2024Q1 | 19.0 | 13.9 | 5.1 |
| 2024Q2 | 25.3 | 16.4 | 8.9 |
| 2024Q3 | 26.0 | 21.3 | 4.7 |
| 2024Q4 | 45.7 | 26.1 | 19.6 |
| 2025Q1 | 17.0 | 24.2 | **-7.2** |
| 2025Q2 | 32.5 | 31.4 | 1.1 |
| 2025Q3 | 35.5 | 34.2 | 1.3 |
| 2025Q4 | 54.5 | 38.4 | 16.0 |
| 2026Q1 | 26.0 | 43.2 | **-17.2** |
| 2026Q2 | 45.4 | 53.1 | **-7.7** |

**Derivation rule:** Q1 values are directly disclosed; Q2/Q3 are directly disclosed by quarter; Q4 and some Q1 cash-CapEx values are derived only from company-reported full-year / YTD cash-capex identities. Values are rounded to one decimal and should not be treated as higher-precision observations.

### 10A.5L Amazon shows why company-level headroom needs business-mix controls

Amazon differs from Meta / Alphabet / Microsoft in two ways.

First, company cash CapEx is not an AI-only denominator.

A large majority of technology-infrastructure investment supports AWS growth, but fulfillment-network expansion is also included.

Second, Amazon's cash headroom is more volatile:

- 2025Q1 turns negative;
- 2025Q2–Q3 remain close to zero;
- 2025Q4 widens again;
- 2026Q1 falls to roughly **-US$17B**;
- 2026Q2 remains negative at roughly **-US$8B**.

This does **not** imply AWS distress.

The correct decomposition is:

```text
Amazon company headroom
=
retail / marketplace / advertising / AWS operating cash generation
-
AWS-oriented technology infrastructure
-
fulfillment-network cash capital expenditure
```

Therefore a company-level headroom deterioration must be paired with:

- AWS revenue / operating income;
- AWS capacity / demand commentary;
- fulfillment-network investment;
- acquisition / strategic-investment cash uses;
- debt issuance.

### 10A.5M 2026 financing amplification is directly observable

Amazon's 2026Q1 filing adds a clear Layer-2 financing signal:

- Q1 2026 operating cash flow: about **US$26.0B**;
- financing cash inflow: about **US$52.8B**;
- proceeds from short-term and long-term debt: about **US$59.5B**;
- cash investment of **US$15.0B** in OpenAI Series C Preferred Stock;
- an additional **US$35.0B** equity commitment subject to conditions;
- Amazon stated that it expected to undertake additional financing activities in 2026.

This means the 2026 capital state cannot be described simply as:

> “Amazon's infrastructure build is internally funded.”

Nor can external financing be treated as evidence of weakness.

The more precise identity is:

> **strong operating cash generation + very high company-level CapEx + large strategic AI investment + material external financing.**

### 10A.5N Four-hyperscaler quarterly monitor is now structurally complete

Meta, Alphabet, Microsoft and Amazon now cover four distinct financing identities:

| Company | Main quarterly strength | Main denominator warning |
|---|---|---|
| Meta | clean OCF + PP&E + finance-lease principal identity | headline CapEx includes lease principal |
| Alphabet | clean OCF − CapEx FCF identity | 2026 external equity/debt amplification must be tracked separately |
| Microsoft | cash PP&E and total CapEx including finance leases both disclosed | fiscal-quarter calendar; total CapEx and cash drain are different clocks |
| Amazon | quarterly OCF + cash CapEx + financing flows | cash CapEx mixes AWS technology infrastructure with fulfillment network |

The common S4 protocol can now be:

1. **Headroom:** is within-company OCF minus comparable cash infrastructure spend compressing?
2. **Commitment:** is total recognized / contracted infrastructure commitment still rising?
3. **Financing:** is debt/equity/lease amplification rising?
4. **Demand breadth:** are bookings / RPO / cloud revenue / customer concentration improving or worsening?
5. **Monetization:** is cloud / AI operating economics weakening?
6. **Clearing:** are projects delayed, commitments cut, assets impaired, or financing terms deteriorating?

Only a multi-layer deterioration should raise S4 materially.

---

### 10A.5O Quarterly expansion protocol

The Meta pilot defines the template for Microsoft / Alphabet / Amazon.

For each company:

1. use the company's own stable quarter-level cash-flow identity;
2. preserve fiscal-vs-calendar labels;
3. separate cash PP&E from finance leases where disclosed;
4. do not calculate a synthetic cross-company ratio unless the denominator is harmonized;
5. flag quarters where OCF–comparable-infrastructure-spend compresses;
6. then inspect whether the compression reflects:
   - accelerated buildout;
   - weaker OCF;
   - external financing;
   - asset acquisition;
   - lease-financing changes.

A headroom decline is therefore a **trigger for decomposition**, not a distress label.

---

### 10A.5 Financing structure now separates into three layers

The panel should therefore track:

```text
Layer 1 — Operating self-funding
  OCF / retained cash generation

Layer 2 — Corporate balance-sheet amplification
  public debt / equity / finance leases

Layer 3 — Project / contract-backed amplification
  private credit / SPV / customer-contract-backed debt / supplier support
```

Microsoft / Alphabet / Meta / Amazon primarily illuminate Layers 1–2.

CoreWeave / Core Scientific illuminate Layer 3.

S4 risk rises when:
- Layer 1 weakens;
- Layer 2 becomes more expensive or dilutive;
- Layer 3 becomes more concentrated or refinancing-dependent;
- utilization / monetization weakens at the same time.

This structure is more informative than a single “AI CapEx funded by cash or debt” binary.

### 10A.3 What remains missing

The panel is deliberately incomplete.

Still to backfill:
- NY Fed CMDI / IG / HY segment state on a reproducible quarterly aggregation basis;
- Chicago Fed NFCI Credit Subindex on a reproducible quarterly aggregation basis;
- private-credit spreads / covenants where public;
- AI-infrastructure equity risk-premium proxy;
- quarterly—not only annual—hyperscaler OCF / CapEx / debt-equity issuance on a stable within-company definition;
- neocloud interest expense / maturities;
- supplier-support / guarantee amount by quarter.

Do not fill those columns using incompatible frequencies merely to make the table look complete.

---

## 10A.6 Public-credit state layer: CMDI + NFCI Credit

The public-credit layer now has an explicit two-indicator design.

### A. NY Fed CMDI — market-functioning distress

CMDI is a monthly summary of corporate-bond market functioning built from weekly primary- and secondary-market metrics, including:

- issuance / primary pricing;
- secondary pricing;
- liquidity;
- duration-matched / default-adjusted spread measures;
- quoted-vs-traded pricing;
- primary-vs-secondary pricing.

The New York Fed also publishes rating-level readings for investment-grade and high-yield segments.

Role in Phase II:

> **CMDI answers whether corporate-bond-market functioning is becoming broadly distressed, not merely whether a spread moved.**

This makes it a natural MF2 public-credit proxy and a useful cross-check against SLOOS.

### B. Chicago Fed NFCI Credit — broad credit-condition direction

The NFCI Credit Subindex isolates the credit component of the Chicago Fed National Financial Conditions Index.

Interpretation rule:

- **positive** → credit conditions tighter than the long-run average;
- **negative** → credit conditions looser than the long-run average.

The latest publicly visible observation reviewed in this pass, **2026-08-21**, was **-0.086**.

That single point is not enough to claim “credit is easy.”

It only says the broad credit subindex was modestly on the looser-than-average side at that date.

### 10A.6A Why two public-credit indicators are better than one spread

CMDI and NFCI Credit measure different things:

| Indicator | Primary question | Best use |
|---|---|---|
| CMDI | is corporate-bond market functioning broadly distressed? | market-clearing / issuance / liquidity stress |
| NFCI Credit | are aggregate credit conditions tighter or looser than historical average? | broad credit-state direction |
| SLOOS | are banks tightening standards and is borrower demand changing? | non-price rationing / bank credit |
| Project filings | can a specific AI borrower actually finance / refinance? | real transmission |

The hierarchy becomes:

```text
Public market functioning
    CMDI
        ↓
Broad credit state
    NFCI Credit
        ↓
Bank rationing
    SLOOS
        ↓
Borrower/project transmission
    debt terms / maturities / covenant / issuance / cancellation
```

No single layer is allowed to stand in for the others.

### 10A.6B Reproducibility rule

The New York Fed confirms that a downloadable CMDI data file exists and includes:

- aggregate market CMDI;
- investment-grade CMDI;
- high-yield CMDI.

However, the current public page exposes the download through a dynamic component, and the stable underlying file URL was **not resolved in this audit pass**.

Therefore the repository records the state as:

> **official downloadable data exists; stable direct-file URL not yet captured.**

Until the direct path is reproducibly resolved:

- cite the official CMDI product page;
- do not invent a CSV/XLSX path;
- do not hand-copy chart values;
- do not digitize interactive graphics;
- do not substitute ICE OAS observations for CMDI.

This is a source-provenance limitation, not an evidence failure.



The New York Fed states that a downloadable CMDI data file includes aggregate and rating-level values.

Phase II should ingest that file only through an explicit, reproducible data path.

Until that path is captured in the repository:

- do not hand-copy chart values;
- do not digitize interactive graphics;
- do not reconstruct a synthetic series from screenshots;
- do not substitute ICE OAS observations for CMDI.

For NFCI Credit, a small number of cited point observations may be used, but the repository will not dump long third-party-served observation histories merely because FRED exposes them.

The goal is a **reproducible research state**, not maximum table density.

### 10A.6C Public-credit S4 rule

Public-credit deterioration raises S4 weight only when at least two layers align:

1. CMDI / public-market functioning deteriorates materially;
2. NFCI Credit / SLOOS also tightens;
3. and preferably one real AI borrower / project shows transmission:
   - spread / coupon increase;
   - shorter maturity;
   - lower leverage;
   - covenant tightening;
   - refinancing difficulty;
   - delay / cancellation.

Therefore:

> **credit-market stress without project transmission is context; project stress without broader credit deterioration is borrower-specific; both together are macro-financial S4 confirmation.**

---

## 10B. New public monitoring instrument: private-credit direct-lending survey

On **August 5, 2026**, the Federal Reserve Banks of New York and Dallas announced a pilot survey of the U.S. private-credit direct-lending market.

The announcement matters because it directly addresses one of the largest visibility gaps in this research layer:

- the U.S. direct-lending market is estimated by the Fed announcement at more than **US$1.3T**;
- visibility into new private-credit lending activity is materially weaker than in public bond markets;
- the survey is intended to cover credit availability, lending standards and market evolution;
- borrower size will be segmented into upper-middle, middle and lower-middle market categories;
- launch is expected after **2026Q3**;
- first aggregate findings are expected in **2027Q1**.

No result exists yet.

Therefore this is not evidence that private credit is tightening or easing.

It is a **future observability upgrade**.

Once published, Phase II should map the survey into:

> **MF3 Lending Standards / Credit Availability**

and compare it with:
- bank SLOOS;
- NY Fed CMDI;
- CoreWeave / project-level financing terms;
- refinancing / covenant changes.

This will help answer whether stress is migrating from public/bank credit into private-credit channels rather than disappearing.

---

## 11. New forward-monitoring panel

Phase II should maintain a quarterly panel:

| Layer | Metric |
|---|---|
| Rates | policy rate, 2Y, 10Y, term premium |
| Public credit | NY Fed CMDI / rating-level CMDI; ICE IG/HY OAS as external cross-check only |
| Bank credit | SLOOS standards and C&I demand |
| Private credit | fundraising, spreads where available, redemptions, covenant stress |
| Equity | AI-infrastructure valuation / equity risk premium proxies |
| Hyperscalers | operating cash flow, CapEx, net cash/debt, finance leases |
| Neocloud / developers | debt, lease obligations, maturities, interest expense, contract-backed debt |
| Counterparty chain | anchor-customer concentration, pledged cash flows, downstream landlord/developer exposure |
| Project finance | leverage, maturity, guarantees, fixed/floating cost |
| Supplier support | equity, guarantees, credit enhancement |
| Clearing outcome | delay, cancel, renegotiate, impairment, asset sale |

The panel is valuable even when data are incomplete because missingness itself should be explicit.

---

## 12. Relationship to the five clearing signals

Macro-financial variables do not become a sixth independent S4 signal.

They primarily strengthen:

- **Forward Commitment** — financing changes future buildout;
- **Demand Quality / Financing** — identifies independent vs assisted demand;
- **Accounting** — later impairment/refinancing consequences.

This avoids double counting.

---

## 13. Relationship to scenarios

### S1 / S2 can survive higher rates when:
- utilization and monetization remain strong;
- sponsors self-fund;
- credit spreads remain contained;
- project return exceeds the higher hurdle rate.

### S3 can coexist with expensive capital when:
- scarcity rents and buyer willingness-to-pay remain high enough;
- anchor buyers lock capacity;
- financing structures successfully transfer risk.

### S4 becomes more likely when:
- utilization/monetization weakens;
- WACC rises or refinancing tightens;
- forward commitments slow;
- independent risk capital retreats;
- supplier support rises to preserve projects.

So the macro layer changes **scenario weights through transmission**, not through a standalone rate threshold.

---

## 14. v0.11 conclusion

The capital-cycle framework no longer treats “interest rates” as a side note.

It now has a falsifiable transmission chain:

> **macro rate / credit shock → financing terms → project hurdle rate → capital commitment → real buildout / delay / cancellation → later accounting recognition**

The quarterly macro backbone is populated for 2022Q1–2026Q2; all four hyperscalers now have quarter-level capital-intensity pilots with company-specific denominator controls; Microsoft separates cash PP&E from total CapEx, and Amazon explicitly carries an AWS-plus-fulfillment denominator warning. The next empirical task is to resolve the stable CMDI direct-file path and connect the four-company headroom / financing / demand-breadth variables into one S4 monitoring table.

## Sources

- FRED / Federal Reserve, FEDFUNDS monthly effective federal funds rate: https://fred.stlouisfed.org/series/FEDFUNDS
- FRED / Federal Reserve, GS10 monthly 10-year Treasury constant maturity: https://fred.stlouisfed.org/series/GS10
- FRED / Federal Reserve, DRTSCILM quarterly net C&I tightening standards: https://fred.stlouisfed.org/series/DRTSCILM
- FRED / Federal Reserve, DRSDCILM quarterly net stronger C&I demand: https://fred.stlouisfed.org/series/DRSDCILM
- Federal Reserve Bank of New York, Corporate Bond Market Distress Index (CMDI): https://www.newyorkfed.org/research/policy/cmdi
- Federal Reserve Bank of Chicago / FRED, NFCICREDIT: https://fred.stlouisfed.org/series/NFCICREDIT
- ICE BofA US Corporate / High Yield OAS via FRED — external cross-check only; repository does not reproduce the licensed observation history: https://fred.stlouisfed.org/series/BAMLC0A0CM ; https://fred.stlouisfed.org/series/BAMLH0A0HYM2
- Federal Reserve, January 2026 SLOOS: https://www.federalreserve.gov/data/sloos/sloos-202601.htm
- Federal Reserve, April 2026 SLOOS: https://www.federalreserve.gov/data/sloos/sloos-202604.htm
- Federal Reserve, July 2026 SLOOS: https://www.federalreserve.gov/data/sloos/sloos-202607.htm
- Federal Reserve, Financial Stability Report, May 2026: https://www.federalreserve.gov/publications/2026-may-financial-stability-report-overview.htm
- Federal Reserve, Funding Risks / Private Credit, May 2026: https://www.federalreserve.gov/publications/2026-may-financial-stability-report-funding-risks.htm
- Goldman Sachs, “The AI Investment Boom: When Will It Pay Off?”, 2026-06-02: https://www.goldmansachs.com/insights/goldman-sachs-exchanges/the-ai-investment-boom-when-will-it-pay-off
- Goldman Sachs, “Why AI Companies May Invest More than $500 Billion in 2026”, 2025-12-18: https://www.goldmansachs.com/insights/articles/why-ai-companies-may-invest-more-than-500-billion-in-2026
- Goldman Sachs, “What the Capex Boom Means for Stock Investors”, 2026: https://www.goldmansachs.com/insights/articles/what-the-capex-boom-means-for-stock-investors
- CoreWeave, Q2 2026 Form 10-Q — delayed-draw term loans, notes, revolver and collateral structure: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm
- CoreWeave, 2026-03-31 — US$8.5B investment-grade GPU/HPC-backed financing facility: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000129/ex991.htm
- Core Scientific, Q2 2026 Form 10-Q — CoreWeave customer concentration and counterparty dependence: https://www.sec.gov/Archives/edgar/data/1839341/000183934126000014/core-20260630.htm
- Core Scientific, Q2 2026 earnings materials — contract cash-flow lockbox and US$3.3B senior secured notes: https://www.sec.gov/Archives/edgar/data/1839341/000183934126000012/q2fy26earningsdeck728am.htm


## Hyperscaler 2026Q2 / FY26Q4 financing sources

- Microsoft FY2026 Q4 earnings — OCF US$55.4B; total CapEx US$41B; cash PP&E US$35.8B; finance leases US$5.6B: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4
- Alphabet Q2 2026 Form 10-Q — OCF US$39.1B; CapEx US$44.9B: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm
- Alphabet Q2 2026 earnings exhibit — ~US$49.6B net equity raise and US$20.3B senior-note proceeds: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
- Meta Q2 2026 results — OCF US$31.86B; CapEx US$31.08B; cash/securities US$90.26B; long-term debt US$83.66B: https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/default.aspx
- Amazon Q2 2026 Form 10-Q — OCF US$45.4B; cash CapEx US$53.1B; technology infrastructure / AWS investment: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm


## Hyperscaler annual-history sources

- Microsoft FY2024 cash flows — 2022–2024 OCF and PP&E additions: https://www.microsoft.com/en-us/investor/earnings/fy-2024-q4/cash-flows
- Microsoft FY2025 annual report / cash flows — 2023–2025 OCF and PP&E additions: https://www.microsoft.com/investor/reports/ar25/
- Alphabet 2024 Form 10-K — 2022–2024 OCF and CapEx: https://www.sec.gov/Archives/edgar/data/1652044/000165204425000014/goog-20241231.htm
- Alphabet 2025 Form 10-K / Q4 earnings — 2025 OCF US$164.7B; CapEx US$91.4B: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
- Meta FY2022 results — 2022 OCF / PP&E / finance-lease principal: https://investor.atmeta.com/investor-news/press-release-details/2023/Meta-Reports-Fourth-Quarter-and-Full-Year-2022-Results/default.aspx
- Meta FY2023 results — 2023 OCF / PP&E / finance-lease principal: https://investor.atmeta.com/investor-news/press-release-details/2024/Meta-Reports-Fourth-Quarter-and-Full-Year-2023-Results-Initiates-Quarterly-Dividend/default.aspx
- Meta FY2024 results — 2024 OCF / PP&E / finance-lease principal: https://investor.atmeta.com/investor-news/press-release-details/2025/Meta-Reports-Fourth-Quarter-and-Full-Year-2024-Results/default.aspx
- Meta FY2025 results / 10-K — 2025 OCF / PP&E / finance-lease principal and future lease obligations: https://www.sec.gov/Archives/edgar/data/1326801/000162828026025534/meta-12312025x10kars.htm
- Amazon 2024 Form 10-K — 2022–2024 OCF / PP&E purchases: https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm
- Amazon 2025 Form 10-K — 2023–2025 OCF / PP&E purchases and FCF reconciliation: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm


## Alphabet quarterly-pilot sources

- Alphabet 2024Q1 Form 10-Q — OCF US$28.8B; CapEx US$12.0B: https://www.sec.gov/Archives/edgar/data/1652044/000165204424000053/goog-20240331.htm
- Alphabet 2024Q2 Form 10-Q — OCF US$26.6B; CapEx US$13.2B: https://www.sec.gov/Archives/edgar/data/1652044/000165204424000079/goog-20240630.htm
- Alphabet 2024Q3 Form 10-Q — OCF US$30.7B; CapEx US$13.1B: https://www.sec.gov/Archives/edgar/data/1652044/000165204424000118/goog-20240930.htm
- Alphabet Q4 2024 earnings release — OCF US$39.1B; CapEx US$14.3B: https://abc.xyz/assets/a3/91/6d1950c148fa84c7d699abe05284/2024q4-alphabet-earnings-release.pdf
- Alphabet 2025Q1 Form 10-Q — OCF US$36.2B; CapEx US$17.2B: https://www.sec.gov/Archives/edgar/data/1652044/000165204425000043/goog-20250331.htm
- Alphabet 2025Q2 Form 10-Q — OCF US$27.7B; CapEx US$22.4B: https://www.sec.gov/Archives/edgar/data/1652044/000165204425000062/goog-20250630.htm
- Alphabet 2025Q3 Form 10-Q — OCF US$48.4B; CapEx US$24.0B: https://www.sec.gov/Archives/edgar/data/1652044/000165204425000091/goog-20250930.htm
- Alphabet Q4 2025 earnings call / release — OCF US$52.4B; CapEx US$27.9B; 2026 CapEx guide US$175–185B: https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx
- Alphabet 2026Q1 Form 10-Q — OCF US$45.8B; CapEx US$35.7B; senior-note proceeds US$31.1B: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm
- Alphabet 2026Q2 earnings exhibit — OCF US$39.1B; CapEx US$44.9B; FCF -US$5.9B; ~US$49.6B equity proceeds: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm


## Microsoft quarterly-pilot sources

- Microsoft FY24Q1 earnings call — OCF US$30.6B; cash PP&E US$9.9B; total CapEx US$11.2B: https://www.microsoft.com/en-us/investor/events/fy-2024/earnings-fy-2024-q1
- Microsoft FY24Q2 earnings call — OCF US$18.9B; cash PP&E US$9.7B; total CapEx US$11.5B: https://www.microsoft.com/en-us/investor/events/fy-2024/earnings-fy-2024-q2
- Microsoft FY24Q3 earnings call — OCF US$31.9B; cash PP&E US$11.0B; total CapEx US$14.0B: https://www.microsoft.com/en-us/investor/events/fy-2024/earnings-fy-2024-q3
- Microsoft FY24Q4 earnings call — OCF US$37.2B; cash PP&E US$13.9B; total CapEx US$19.0B: https://www.microsoft.com/en-us/investor/events/fy-2024/earnings-fy-2024-q4
- Microsoft FY25Q1 earnings call — OCF US$34.2B; cash PP&E US$14.9B; total CapEx US$20.0B: https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q1
- Microsoft FY25Q2 earnings call — OCF US$22.3B; cash PP&E US$15.8B; total CapEx US$22.6B: https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q2
- Microsoft FY25Q3 earnings call — OCF US$37.0B; cash PP&E US$16.7B; total CapEx US$21.4B: https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q3
- Microsoft FY25Q4 earnings call — OCF US$42.6B; cash PP&E US$17.1B; total CapEx US$24.2B: https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q4
- Microsoft FY26Q1 earnings call — OCF US$45.1B; cash PP&E US$19.4B; total CapEx US$34.9B; finance leases US$11.1B: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q1
- Microsoft FY26Q2 earnings call — OCF US$35.8B; cash PP&E US$29.9B; total CapEx US$37.5B; finance leases US$6.7B; ~45% of commercial RPO from OpenAI: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2
- Microsoft FY26Q3 earnings call — OCF US$46.7B; cash PP&E US$30.9B; total CapEx US$31.9B; finance leases US$4.7B: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3
- Microsoft FY26Q4 earnings call — OCF US$55.4B; cash PP&E US$35.8B; total CapEx US$41.0B; finance leases US$5.6B; RPO breadth outside frontier-model companies: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4


## Amazon quarterly-pilot sources

- Amazon 2024Q1 Form 10-Q — OCF US$19.0B; cash CapEx US$13.9B: https://www.sec.gov/Archives/edgar/data/1018724/000101872424000083/amzn-20240331.htm
- Amazon 2024Q2 Form 10-Q — OCF US$25.3B; cash CapEx US$16.4B; H1 cash CapEx US$30.3B: https://www.sec.gov/Archives/edgar/data/1018724/000101872424000130/amzn-20240630.htm
- Amazon 2024Q3 Form 10-Q — OCF US$26.0B; cash CapEx US$21.3B; 9M cash CapEx US$51.6B: https://www.sec.gov/Archives/edgar/data/1018724/000101872424000161/amzn-20240930.htm
- Amazon 2024 Form 10-K — annual OCF US$115.9B; net PP&E / FCF denominator US$77.7B; Q4 derived from annual minus 9M: https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm
- Amazon 2025Q1 Form 10-Q — OCF US$17.0B; Q1 cash CapEx derived from H1 minus Q2 company cash-capex disclosure: https://www.sec.gov/Archives/edgar/data/1018724/000101872425000036/amzn-20250331.htm
- Amazon 2025Q2 Form 10-Q — OCF US$32.5B; cash CapEx US$31.4B; H1 cash CapEx US$55.6B: https://www.sec.gov/Archives/edgar/data/1018724/000101872425000086/amzn-20250630.htm
- Amazon 2025Q3 Form 10-Q — OCF US$35.5B; cash CapEx US$34.2B; 9M cash CapEx US$89.9B: https://www.sec.gov/Archives/edgar/data/1018724/000101872425000123/amzn-20250930.htm
- Amazon 2025 Q4 earnings exhibit / 10-K — annual OCF US$139.5B; net PP&E / FCF denominator about US$128.3B; Q4 derived from annual minus 9M: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm
- Amazon 2026Q1 Form 10-Q — OCF US$26.0B; US$59.5B debt proceeds; US$15B OpenAI investment + US$35B conditional commitment: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000014/amzn-20260331.htm
- Amazon 2026Q2 Form 10-Q — OCF US$45.4B; cash CapEx US$53.1B; H1 cash CapEx about US$96.3B: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
