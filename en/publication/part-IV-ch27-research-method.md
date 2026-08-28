# Part IV · Chapter 27: Research Method and Evidence Architecture

> **Publication-layer methodology chapter.** Based primarily on [Volume 18](../vol-18.en.md). This chapter defines the common grammar for facts, hypotheses, mechanisms, scenarios, falsification, and evidence grades so that financial, semiconductor, energy, regulatory, and labor-market material can enter one auditable framework.

## 1. AI-infrastructure research needs a unified evidence language

AI infrastructure spans finance, semiconductors, memory, advanced packaging, cloud, power, regulation, and labor markets.

The numbers in these fields carry different physical units, accounting definitions, time windows, and evidence strengths.

Without one common discipline, recurring errors include:

- mixing company disclosures with institutional forecasts;
- converting revenue share into wafer share;
- rewriting contracted MW as energized / utilized load;
- presenting engineering estimates as vendor disclosures;
- treating guidance as actuals;
- presenting future scenarios as current facts;
- repeating one secondary-source number across chapters until it appears to become multi-source confirmation.

This book therefore uses two complementary frameworks:

> **F → H → M → S → X**

and:

> **A / B / C / D evidence grades**

The first determines the identity of a claim; the second determines evidence strength.

## 2. F — Fact

A Fact must describe something that has already occurred and can be traced to a clear public source.

Preferred sources include:

- 10-K / 20-F / annual reports;
- official earnings materials;
- official product specifications;
- regulator / government documents;
- court filings;
- formal contracts / official project disclosures.

Fact does not mean "many media outlets reported the same thing."

Multiple media reports citing the same origin do not create independent multi-source confirmation.

## 3. H — Hypothesis

A Hypothesis is a future input condition inferred from facts but not fully confirmed by reality.

Example:

> **If a system platform continues to combine stronger cash flow, long-duration orders, prepayment capacity, and roadmap certainty, its bargaining power for next-generation scarce capacity may increase.**

That is not a fact contained in a company filing.

It is a testable hypothesis that can later be checked against allocation, commitment, and delivery data.

## 4. M — Mechanism

A Mechanism must explain the intermediate variables connecting facts and future states.

Example:

> high system margin → higher cash generation → larger forward commitments → stronger capacity reservation → higher delivery certainty → stronger customer retention

A mechanism cannot collapse into "it is strong, therefore it will become stronger."

It has to identify what changes, how the constraint transmits, and which evidence would show that the chain has broken.

## 5. S — Scenario

A Scenario is a conditional state created by multiple hypotheses and mechanisms.

The book uses four standard scenarios:

- **S1 — Competitive Expansion**;
- **S2 — Baseline Concentration**;
- **S3 — Resource Hegemony**;
- **S4 — Capital Hard Landing**.

The objective is not to assign fixed world probabilities.

It is to ask:

> **If a set of observable conditions holds together, which structural state does the industry resemble most closely?**

## 6. X — Falsification

Every strong judgment requires reverse signals.

For example, the thesis that scarce-layer value capture continues strengthening must be weakened if several of the following reverse persistently:

- supply commitments fall;
- advanced packaging stops being tight;
- HBM / DRAM residual supply loosens materially;
- cloud frontier workloads migrate at scale away from the dominant stack;
- open interfaces materially reduce migration costs;
- utilization and forward commitments weaken together.

A long-run narrative without falsification conditions does not enter the book's formal judgment layer.

## 7. A / B / C / D Evidence Grades

| Grade | Definition | Typical source |
|---|---|---|
| A | First-party / formal evidence | filing, official product page, regulator, government, court, formal contract |
| B | Institutional research | TrendForce, ILO, IMF, Stanford HAI, academic / industry research |
| C | Sell-side / supply-chain / media estimate | investment bank, channel, supply-chain source, media estimate |
| D | Report model / stress test | geometry, arithmetic, sensitivity, scenario assumption |

Examples:

- Micron HBM3E same-node/same-bits ≈ **3× DDR5 wafer supply**: **A**;
- TrendForce estimate that NVIDIA represented >60% of 2025 CoWoS demand: **B**;
- a sell-side estimate of one customer's monthly CoWoS wafer count: **C**;
- 72 ÷ 13.4 ≈ **5.37 CoWoS wafers/rack** as report-side geometry: **D**.

Repeating the same number across multiple chapters does not automatically upgrade its evidence grade.

## 8. Dimensional consistency outranks narrative convenience

The book prohibits the following conversions:

### Revenue share ≠ wafer share

TSMC customer revenue share cannot be converted directly into N2, 3 nm, HPC, or CoWoS physical share.

### Contracted MW ≠ Energized MW ≠ Utilized AI Load

An up-to-1.92-GW revised PPA cannot be rewritten as 1.92 GW of active AI load.

### Product specification × hypothetical quantity ≠ shipment

13.4 TB HBM3E/rack × 50,000 hypothetical racks creates D-grade scenario demand, not actual HBM shipment.

### Engineering geometry ≠ fab yield

5.37 CoWoS wafers/rack is a geometry stress test, not TSMC-disclosed yield.

### Guidance / expectation ≠ actual

Company guidance must retain its guidance identity and cannot be combined with another company's TTM actuals into a single "already occurred" total.

## 9. The boundary of negative evidence

"Not disclosed in this document" proves only that the document does not disclose it.

For example, if CXMT's registration prospectus does not disclose an HBM product line, the supported statement is:

> **The registration prospectus does not disclose an HBM product line.**

It cannot be expanded into "the company has no HBM R&D."

Negative evidence limits what can be confirmed. It does not prove absolute non-existence.

## 10. Forecasts, guidance, and scenarios must retain time identity

Institutional forecasts must preserve:

- source identity;
- publication date;
- forecast window.

For example, TrendForce's "HBM + RDIMM ≈51% of 2026 DRAM bit supply" must remain a **2026E institutional forecast**, not become a 2026 actual through repeated citation.

Likewise, 2030/2036 node prices, monthly packaging capacity, or GW campus estimates can only appear as explicitly conditioned assumptions.

## 11. Where the book's core mechanism models fit

The primary models include:

- **AI Resource Gravity**;
- **Scarce-layer Value Capture**;
- **AHICR — Advanced/HPC Incremental Capacity Capture Ratio**;
- **Non-AI Residual Capacity**;
- **Cloud System-Stack Substitution**;
- **Anchor Compute Buyer Effect**;
- **Rolling Bottleneck Cascade**;
- **AI Software Unit Economics**;
- **Task-to-Job Translation Layer**.

These models organize causal relationships.

They do not replace source facts.

Their validity must ultimately be tested by new F and X evidence.

## 12. Publication-layer deduplication rules

The research layer can retain multiple independent modules for evidence tracing.

The publication layer must satisfy stricter rules:

1. one factual table has one canonical home;
2. a mechanism is fully defined once;
3. later chapters add evidence, boundaries, counterarguments, or falsification;
4. unique formulas / cross-volume reasoning from macro essays move into the relevant canonical chapter;
5. sources move with the claims they support;
6. internal revision history does not enter public-facing text.

The publication layer is therefore not a mechanical merger of 40 research volumes.

It is a reorganization of evidence and argument.

## 13. Formal release standard

Each chapter should satisfy:

- factual claims have sources;
- forecasts / institutional numbers retain their identities;
- sell-side estimates do not masquerade as first-party facts;
- D-grade models state assumptions;
- future claims are conditional;
- falsification conditions exist;
- technical units use standard notation;
- accounting and physical units remain separate;
- public text carries no internal revision metadata, process notes, or self-justification.

This method does not exist to make scenarios timid.

It allows scenarios to be bold while the fact layer remains auditable, falsifiable, and updateable.

## Key public sources

- Micron FY24 Q2 Prepared Remarks: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- TSMC 2025 20-F: https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm
- NVIDIA GB200 NVL72 product page: https://www.nvidia.com/en-us/data-center/gb200-nvl72/
- Talen 2026 Q2 10-Q: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
- TrendForce, 2025 CoWoS demand structure: https://www.trendforce.com/research/download/RP250314ZJ
