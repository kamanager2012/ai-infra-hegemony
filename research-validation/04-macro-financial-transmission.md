# P0-4 · Macro-Financial Transmission Layer v0.18

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

## 10A. Empirical data appendices

The P0-4 data layer is now separated from the method file.

- [04A · Public Credit & Macro-Financial Panel](04a-public-credit-panel.md) — 2022–2026 rates/SLOOS backbone, CMDI/NFCI protocol, private-credit observability.
- [04B · Hyperscaler Quarterly Capital-Intensity Panel](04b-hyperscaler-quarterly-panel.md) — Meta, Alphabet, Microsoft, Amazon annual/quarterly OCF/CapEx identities and denominator controls.

The method file retains only the interpretation rule:

> **macro credit conditions and hyperscaler free-cash-flow compression are context until they transmit into demand, monetization, commitment, refinancing, or clearing.**

Do not classify S4 from:
- one negative FCF quarter;
- one rate/spread move;
- one large debt/equity issuance;
- one record CapEx print.

The detailed tables are maintained in the appendices so quarterly updates do not continuously expand the transmission-method document.

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

## 11A. Integration into Dashboard K

The four hyperscaler pilots now feed the public-proxy scenario layer through **Dashboard K — Hyperscaler Capital-Cycle Transmission**.

The integration rule is deliberately stricter than a free-cash-flow screen.

For each hyperscaler / major infrastructure buyer, record six layers:

1. **Headroom** — within-company OCF minus comparable cash infrastructure / PP&E spend;
2. **Recognized Commitment** — total CapEx, finance leases, contracted capacity, or other long-duration commitments;
3. **Financing Amplification** — debt, equity, leases, project finance, guarantees, supplier support;
4. **Demand Breadth / Quality** — RPO, bookings, customer concentration, cloud demand, renewal breadth;
5. **Monetization** — cloud / AI revenue growth, operating income, utilization / ROI proxies;
6. **Clearing / Accounting** — project cuts, resale/discounting, impairments, accelerated depreciation, distressed refinancing.

### 11A.1 S4 confirmation rule

Do **not** raise S4 materially because one of the following occurs alone:

- FCF turns negative;
- debt issuance rises;
- equity is issued;
- finance leases rise;
- CapEx reaches a record;
- one anchor customer becomes large.

Those are **state variables**, not conclusions.

S4 weight rises only when a financing / headroom deterioration begins to align with:

- weaker demand breadth or concentration deterioration;
- weaker monetization / utilization;
- forward-commitment cuts or economically driven rescheduling;
- market clearing;
- accounting / refinancing stress.

Cross-company / cross-layer breadth strengthens the signal.

### 11A.2 Current 2026 classification

Using the current quarterly evidence:

- **Meta:** headroom compression is visible, but investment and operating-income expectations remain expansionary;
- **Alphabet:** negative quarterly FCF is accompanied by large external debt/equity capacity and continued infrastructure expansion;
- **Microsoft:** large recognized CapEx / lease commitments coexist with broadening commercial RPO outside frontier-model companies;
- **Amazon:** company-level cash headroom is negative in selected quarters, but the denominator mixes AWS and fulfillment investment and must be paired with AWS monetization.

Therefore the current four-company state is:

> **high-intensity expansion + increasing financing amplification, without cross-company S4 confirmation.**

This is a research-side classification, not a formal-report scenario switch.

### 11A.3 What would change the classification

Upgrade toward S4 only if future quarters show a combination such as:

```text
headroom compression
+
weaker cloud / AI monetization
+
narrower / weaker bookings or RPO
+
more expensive / fragile financing
+
CapEx or project commitment cuts
+
clearing / impairment evidence
```

The sequence need not be identical across firms.

The requirement is **cross-confirmation**, not a fixed threshold count.

---

## 11B. Project-finance borrower integration

Detailed facility-level evidence is maintained in:

- [04C · AI Infrastructure Project-Finance Borrower Panel](04c-project-finance-borrower-panel.md)

The parent method keeps the decision rule:

> **refinancing exposure ≠ realized refinancing stress.**

Exposure variables:
- maturity wall;
- floating-rate debt;
- high coupon;
- bridge financing;
- customer concentration;
- collateral / residual-value sensitivity.

Realized stress requires adverse transmission such as:
- failed / delayed refinancing;
- materially worse rollover terms;
- covenant / DSCR pressure;
- loss of committed liquidity;
- project delay / cancellation;
- distressed asset sale / impairment.

Current borrower evidence remains heterogeneous rather than one uniform stress state.

## 11C. Supplier / Sponsor Support integration

Detailed seller/sponsor support evidence is maintained in:

- [04D · Supplier / Sponsor Support Panel](04d-supplier-support-panel.md)
- [11 · Financing Reflexivity Map](11-financing-reflexivity-map.md)

The parent method retains two hard rules:

> **support intensity is not independent demand.**

and:

> **support becomes S4-relevant only when rising support dependence aligns with weaker independent capital access, weaker customer/workload economics, and worse refinancing conditions.**

Guarantee caps, equity commitments, customer prepayments, and contract-backed debt must not be added together as separate copies of demand.

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

## 14. v0.18 conclusion

The capital-cycle framework no longer treats “interest rates” as a side note.

It now has a falsifiable transmission chain:

> **macro rate / credit shock → financing terms → project hurdle rate → capital commitment → real buildout / delay / cancellation → later accounting recognition**

P0-4 now separates method from maintainable evidence panels: public credit/macros (04A), hyperscaler capital intensity (04B), project-finance borrowers (04C), and supplier/sponsor support (04D). The parent file retains only the transmission logic and S4 cross-confirmation rules. 04A now owns the canonical CMDI retrieval / provenance contract; 04B owns hyperscaler corporate capital-intensity state; 04C owns facility-level delivery / monetization / refinancing transitions; and 04D owns support activation / step-down. The remaining empirical task is maintenance of real state transitions over time, not expansion of the parent method file.

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


## Project-finance borrower sources added in v0.13

- Nebius, 2026-07-17 — ~US$775M first senior secured facility, SOFR + 2.50%, October-2030 maturity, backed by deployed GPUs and investment-grade customer contracted cash flows: https://nebius.com/newsroom/nebius-raises-775-million-in-first-secured-debt-financing-to-accelerate-global-buildout
- Nebius Q2 2026 filing — secured-facility identity and collateral structure: https://www.sec.gov/Archives/edgar/data/1513845/000110465926094844/nbis-20260812xex99d2.htm
- Applied Digital FY2026 Form 10-K — debt stack, weighted-average rate and principal-payment schedule: https://www.sec.gov/Archives/edgar/data/1144879/000114487926000048/apld-20260531.htm
- IREN, 2026-02-05 — Microsoft GPU financing / prepayment structure: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000014/a991irenreportsq2fy26res.htm
- IREN Q3 FY26 filing — binding ~US$3.6B GPU financing commitment backed by Microsoft-related GPUs / cash flows: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000026/iren-20260331.htm
- IREN FY26 results, 2026-08-27 — additional GPU financings, customer prepayments and legacy Bitcoin-mining impairment identity: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000051/irenreportsfy26results.htm
