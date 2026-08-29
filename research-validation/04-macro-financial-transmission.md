# P0-4 · Macro-Financial Transmission Layer v0.1

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

## 8. Macro-Financial Stress Matrix

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

## 9. S4 integration rule

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

## 10. New forward-monitoring panel

Phase II should maintain a quarterly panel:

| Layer | Metric |
|---|---|
| Rates | policy rate, 2Y, 10Y, term premium |
| Public credit | IG / HY yields and spreads |
| Bank credit | SLOOS standards and C&I demand |
| Private credit | fundraising, spreads where available, redemptions, covenant stress |
| Equity | AI-infrastructure valuation / equity risk premium proxies |
| Hyperscalers | operating cash flow, CapEx, net cash/debt, finance leases |
| Neocloud / developers | debt, lease obligations, maturities, interest expense |
| Project finance | leverage, maturity, guarantees, fixed/floating cost |
| Supplier support | equity, guarantees, credit enhancement |
| Clearing outcome | delay, cancel, renegotiate, impairment, asset sale |

The panel is valuable even when data are incomplete because missingness itself should be explicit.

---

## 11. Relationship to the five clearing signals

Macro-financial variables do not become a sixth independent S4 signal.

They primarily strengthen:

- **Forward Commitment** — financing changes future buildout;
- **Demand Quality / Financing** — identifies independent vs assisted demand;
- **Accounting** — later impairment/refinancing consequences.

This avoids double counting.

---

## 12. Relationship to scenarios

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

## 13. v0.1 conclusion

The capital-cycle framework no longer treats “interest rates” as a side note.

It now has a falsifiable transmission chain:

> **macro rate / credit shock → financing terms → project hurdle rate → capital commitment → real buildout / delay / cancellation → later accounting recognition**

The next empirical task is to build the quarterly panel and attach financing structure to the largest AI-infrastructure projects and buyers.

## Sources

- Federal Reserve, January 2026 SLOOS: https://www.federalreserve.gov/data/sloos/sloos-202601.htm
- Federal Reserve, April 2026 SLOOS: https://www.federalreserve.gov/data/sloos/sloos-202604.htm
- Federal Reserve, July 2026 SLOOS: https://www.federalreserve.gov/data/sloos/sloos-202607.htm
- Federal Reserve, Financial Stability Report, May 2026: https://www.federalreserve.gov/publications/2026-may-financial-stability-report-overview.htm
- Federal Reserve, Funding Risks / Private Credit, May 2026: https://www.federalreserve.gov/publications/2026-may-financial-stability-report-funding-risks.htm
- Goldman Sachs, “The AI Investment Boom: When Will It Pay Off?”, 2026-06-02: https://www.goldmansachs.com/insights/goldman-sachs-exchanges/the-ai-investment-boom-when-will-it-pay-off
- Goldman Sachs, “Why AI Companies May Invest More than $500 Billion in 2026”, 2025-12-18: https://www.goldmansachs.com/insights/articles/why-ai-companies-may-invest-more-than-500-billion-in-2026
- Goldman Sachs, “What the Capex Boom Means for Stock Investors”, 2026: https://www.goldmansachs.com/insights/articles/what-the-capex-boom-means-for-stock-investors
