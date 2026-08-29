# P0-4 · Macro-Financial Transmission Layer v0.5

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
- historical hyperscaler operating cash flow / CapEx before the current 2026Q2 cross-section;
- neocloud interest expense / maturities;
- supplier-support / guarantee amount by quarter.

Do not fill those columns using incompatible frequencies merely to make the table look complete.

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

## 14. v0.5 conclusion

The capital-cycle framework no longer treats “interest rates” as a side note.

It now has a falsifiable transmission chain:

> **macro rate / credit shock → financing terms → project hurdle rate → capital commitment → real buildout / delay / cancellation → later accounting recognition**

The quarterly macro backbone is now populated for 2022Q1–2026Q2. The next empirical task is to backfill consistent IG/HY credit-spread series and attach operating cash flow, CapEx, maturity and financing-support structure to the largest AI-infrastructure projects and buyers.

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
