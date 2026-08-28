# Part IV · Chapter 27: Research Method and Evidence Architecture

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

**Table 27.1 — Evidence-grade system used in this report**

| Grade | Definition | Typical source |
|---|---|---|
| A | First-party / formal evidence | filing, official product page, regulator, government, court, formal contract |
| B | Institutional research | TrendForce, ILO, IMF, Stanford HAI, academic / industry research |
| C | Sell-side / supply-chain / media estimate | investment bank, channel, supply-chain source, media estimate |
| D | Report model / stress test | geometry, arithmetic, sensitivity, scenario assumption |

**Source:** Report research method.  
**Note:** Evidence grade measures source strength, not analytical importance. D-grade models can support scenarios and sensitivity analysis but cannot be presented as observed facts.

Examples:

- Micron HBM3E same-node/same-bits ≈ **3× DDR5 wafer supply**: **A**;[^1]
- TrendForce estimate that NVIDIA represented >60% of 2025 CoWoS demand: **B**;[^2]
- a sell-side estimate of one customer's monthly CoWoS wafer count: **C**;
- 72 ÷ 13.4 ≈ **5.37 CoWoS wafers/rack** as report-side geometry: **D**.

Repeating the same number across multiple chapters does not automatically upgrade its evidence grade.

## 8. Dimensional consistency outranks narrative convenience

The book prohibits the following conversions:

### Revenue share ≠ wafer share

TSMC customer revenue share cannot be converted directly into N2, 3 nm, HPC, or CoWoS physical share.

### Contracted MW ≠ Energized MW ≠ Utilized AI Load

An up-to-1.92-GW revised PPA cannot be rewritten as 1.92 GW of active AI load.[^3]

### Product specification × hypothetical quantity ≠ shipment

13.4 TB HBM3E/rack × 50,000 hypothetical racks creates D-grade scenario demand, not actual HBM shipment.[^4]

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

## 12. Full-report deduplication and cross-reference rules

A formal report should not repeatedly rewrite the same facts and mechanisms across chapters.

The publication rules are:

1. one high-impact factual table has one primary location;
2. a mechanism is fully defined once and later chapters inherit it through cross-reference;
3. later chapters add only new evidence, boundaries, counterarguments, or falsification conditions;
4. when one number appears across chapters, its original denominator, time window, and evidence grade remain unchanged;
5. sources move with the claims they support;
6. revision history, editorial process, and construction metadata do not enter public-facing text.

The purpose is not to reduce information. It is to let readers distinguish first definition, incremental evidence, and cross-chapter inference.

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

## References

[^1]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^2]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^3]: Talen Energy, 2026 Q2 Form 10-Q, revised AWS PPA up to 1,920 MW, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
[^4]: NVIDIA, “GB200 NVL72,” official product page, 13.4 TB HBM3E per rack, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
