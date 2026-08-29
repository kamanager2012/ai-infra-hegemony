# P0-4A · Public Credit & Macro-Financial Panel v0.3

> Initially extracted from P0-4 v0.17 to keep the method file maintainable. The parent method is now v0.18. This appendix preserves the reproducible macro/public-credit data layer; interpretation rules remain governed by `04-macro-financial-transmission.md`.

## 10A. 2022–2026 quarterly macro-financial panel v0.2

The first reproducible quarterly backbone is now populated with four variables:

- **Fed Funds:** effective federal funds rate, quarter-ending month average;
- **10Y:** 10-year Treasury constant-maturity yield, quarter-ending month average;
- **SLOOS standards:** net percentage of domestic banks tightening C&I standards for large / middle-market firms;
- **SLOOS demand:** net percentage reporting stronger C&I demand from large / middle-market firms.

Important temporal-identity rule:

- **Fed Funds / 10Y** use the calendar quarter and the quarter-ending month's average;
- **SLOOS / FRED** observations use the survey-release quarter label, while the survey questions generally describe changes over the preceding three months.

Therefore the row label below is a **monitoring label**, not proof that all four variables describe the exact same economic quarter.

Example:
- FRED `DRTSCILM/DRSDCILM = Q2 2026` corresponds to the spring survey vintage and reports **8.1 / 4.8**;
- the **July 2026 SLOOS**, released on 2026-08-03 and describing lending changes over 2026Q2, appears in FRED as **Q3 2026** and reports **0.0 / 16.1**.

This distinction is mandatory for prospective use.

| Monitoring label | Fed Funds % | 10Y % | SLOOS tightening % | SLOOS stronger demand % | Macro reading |
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

### 10A.0A Latest SLOOS release bridge — published 2026-08-03

The latest completed SLOOS release must be carried separately because 2026Q3 is not yet a completed rates quarter.

| Publication date | FRED survey label | Economic period described | DRTSCILM | DRSDCILM | Read-through |
|---|---|---|---:|---:|---|
| 2026-08-03 | **2026Q3** | predominantly **2026Q2** lending changes | **0.0%** | **16.1%** | domestic C&I standards were basically unchanged on net while demand from large / middle-market firms strengthened |

This is stronger contrary evidence against an economy-wide credit seizure than the prior spring-vintage 8.1 / 4.8 observation.

It does **not** prove easy financing for AI infrastructure borrowers:
- SLOOS is aggregate bank-credit evidence;
- NDFI / private-credit conditions can differ;
- borrower-specific spreads, covenants, concentration and refinancing still require 04C-level evidence.

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

### 10A.6B CMDI ingestion contract v0.2

The New York Fed confirms that the official CMDI product publishes a downloadable data file containing:

- aggregate market CMDI;
- investment-grade CMDI;
- high-yield CMDI.

The public product page is stable:

```text
https://www.newyorkfed.org/research/policy/cmdi
```

The underlying download asset is exposed through a dynamic page component. A durable direct CSV/XLSX asset URL is **not treated as part of the source contract** unless the New York Fed itself publishes one as a documented endpoint.

That changes the maintenance rule.

#### Human-reproducible retrieval path — CLOSED

For a scheduled research update:

1. open the official CMDI product page;
2. use the official **Downloads** control;
3. save the file exactly as delivered;
4. record:
   - retrieval timestamp;
   - source page;
   - original filename;
   - file size;
   - SHA-256;
   - latest observation date;
   - column names;
5. parse only the delivered file;
6. preserve the raw file outside the report text if the repository's source-license policy permits retention;
7. update derived quarterly/monthly state tables from the parsed values.

This is reproducible because the canonical source identity and retrieval action are stable even if the CDN / media asset URL changes.

#### Fully unattended machine path — NOT YET CLOSED

Phase II will **not**:
- guess a hidden `.csv` / `.xlsx` media URL;
- scrape chart pixels;
- treat a transient CDN asset as a permanent API;
- use a third-party mirror as the authoritative refresh path.

If the New York Fed later exposes a documented API or stable direct-file endpoint, that endpoint can replace the interactive-download step.

Therefore the precise status is:

> **canonical official retrieval path = closed**  
> **unattended direct-file automation = unresolved / non-required for current research maintenance**

This removes the earlier false binary of “direct URL found / data unusable.”

### 10A.6B.1 Validation fixtures — independent check against accidental parser drift

A reproducible ingestion process also needs known historical checkpoints.

GAO-23-105629 publishes accessible data for Figure 5 using Federal Reserve Bank of New York CMDI data. It provides market / IG / HY weekly values for January 2019–August 2022.

Three sparse fixtures are enough to detect:
- column swaps;
- date parsing errors;
- percentage-vs-index rescaling;
- accidental use of the wrong series.

| Week ending | Market CMDI | IG CMDI | HY CMDI | Validation role |
|---|---:|---:|---:|---|
| 2019-04-26 | 0.10 | 0.14 | 0.15 | low-distress pre-COVID baseline |
| 2020-03-20 | 0.46 | 0.51 | 0.56 | acute COVID market-dislocation checkpoint |
| 2022-03-18 | 0.13 | 0.30 | 0.13 | rating-level divergence checkpoint |

These values are **validation fixtures**, not the maintenance source.

Hard rule:

> **GAO can validate the parser; it does not replace the NY Fed as the authoritative ongoing CMDI source.**

The parser should fail closed if:
- expected Market / IG / HY columns are absent;
- duplicate dates appear unexpectedly;
- values are nonnumeric;
- the latest observation predates the prior ingested version;
- historical fixtures materially disagree without a documented NY Fed revision.

### 10A.6B.2 Source-version record

Every CMDI refresh should append one provenance row:

| Field | Meaning |
|---|---|
| `retrieved_at` | retrieval timestamp |
| `source_page` | canonical NY Fed CMDI page |
| `source_filename` | filename delivered by NY Fed |
| `sha256` | raw-file checksum |
| `first_observation` | earliest date in delivered file |
| `last_observation` | latest date in delivered file |
| `row_count` | parsed observation rows |
| `columns` | exact delivered column names |
| `parser_version` | local parsing contract version |
| `revision_note` | whether historical values changed vs prior snapshot |

This makes revision history auditable without pretending the New York Fed guarantees a permanent CDN URL.

For NFCI Credit, a small number of cited point observations may be used, but the repository will not dump long third-party-served observation histories merely because FRED exposes them.

The goal remains a **reproducible research state**, not maximum table density.

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


## Sources carried from parent register

## Sources

- FRED / Federal Reserve, FEDFUNDS monthly effective federal funds rate: https://fred.stlouisfed.org/series/FEDFUNDS
- FRED / Federal Reserve, GS10 monthly 10-year Treasury constant maturity: https://fred.stlouisfed.org/series/GS10
- FRED / Federal Reserve, DRTSCILM quarterly net C&I tightening standards: https://fred.stlouisfed.org/series/DRTSCILM
- FRED / Federal Reserve, DRSDCILM quarterly net stronger C&I demand: https://fred.stlouisfed.org/series/DRSDCILM
- Federal Reserve Bank of New York, Corporate Bond Market Distress Index (CMDI): https://www.newyorkfed.org/research/policy/cmdi
- U.S. Government Accountability Office, GAO-23-105629, accessible Figure 5 data — independent historical validation fixture for Market / IG / HY CMDI, 2019–2022: https://www.gao.gov/assets/820/814275.pdf
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


