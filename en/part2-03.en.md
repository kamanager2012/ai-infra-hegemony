# Macro Essay 3: Physical Manufacturing Limits and the Global Semiconductor Supply Contest


> **Audit boundary for retired research calculations.** The Chinese research source retains several historical CoWoS/supply-chain stress calculations to document denominator and physical-pool errors. Those retired C/D-grade calculations are **not imported into this English publication-facing research essay as observed facts**. Current conclusions rely on first-party TSMC/Micron evidence, explicitly graded institutional research, and versioned D-grade models.

Chinese source edition: [part2-03.md](../part2-03.md)

> Retrieval and revision cutoff: **2026-08-28**. Advanced logic, advanced packaging, and HBM are different physical pools. Their metrics cannot be substituted for one another, and the shortest layer determines system delivery.

## 1. The core question

Around 2026, which physical layer most directly limits rack-scale AI-system delivery?

The answer cannot be derived from one number such as:

- TSMC's largest-customer revenue share;
- HPC revenue share;
- packaging revenue share;
- an estimated CoWoS monthly capacity;
- an HBM bit share.

These quantities measure different objects.

The correct framework separates three ceilings:

1. **leading-edge logic**;
2. **advanced packaging**;
3. **HBM / DRAM manufacturing input**.

All three must be satisfied at the same time.

## 2. Leading-edge logic: an entry ticket, not the full delivery system

TSMC's 2025 public disclosures show:

- 3 nm at **24% of wafer revenue**;
- 5 nm at **36%**;
- 7 nm at **14%**;
- 7 nm and below at **74%**;
- HPC at **58% of revenue**;
- N2 entering volume production in **4Q25**.

Primary sources:
- TSMC 2025 Annual Report: https://investor.tsmc.com/static/annualReports/2025/english/index.html
- TSMC 4Q25 Presentation (2025 platform mix / growth): https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf

These are strong indicators of leading-edge concentration and HPC demand.

They do not disclose:

- physical wafers by customer;
- N2 customer allocation;
- N2 revenue share;
- customer-level frontier-AI capacity.

A node is therefore the **entry ticket**.

It is not the complete system-delivery constraint.

## 3. Advanced packaging: the clearest first-party short-term bottleneck

TSMC has repeatedly described advanced-packaging capacity as very tight.

The company said in 2024 Q4 that it could not meet all customer needs.

By 2026 Q2, management said packaging capacity was tight enough to **limit customers' growth**.

TSMC's disclosures use different labels by year:

- 4Q24 transcript: **advanced packaging and testing >8% of 2024 revenue**;
- 4Q25 transcript, after company correction: **advanced packaging slightly above 10% of 2025 revenue**.

These are not treated as a perfectly like-for-like time series.

The key evidence boundary is:

> **Packaging tightness is first-party fact. Customer-level CoWoS allocation is not publicly disclosed by TSMC.**

That makes advanced packaging one of the clearest observable short-term delivery constraints.

## 4. The 5.37 wafers-per-rack coefficient is a geometry stress test

The report's working relation is:

```text
72 GPU packages
÷ 13.4 packages per CoWoS wafer
≈ 5.37 CoWoS wafers per rack
```

The **72** is tied to the official NVL72 configuration.

The **13.4 packages per wafer** term is a geometry assumption.

The resulting **5.37** is therefore **D-grade engineering geometry**.

It is not:

- a TSMC-disclosed yield;
- a front-end logic-wafer coefficient;
- a customer-allocation disclosure.

The coefficient is useful for scenario stress tests.

It is not valid to divide TSMC's full annual wafer shipments by 5.37 and claim a global rack-production limit.

That mixes different physical pools.

## 5. Why the “an invalid six-figure rack-count extrapolation” style calculation fails

TSMC's full-fab wafer shipments include:

- smartphones;
- automotive;
- IoT;
- mature-node products;
- many non-CoWoS flows.

CoWoS is a back-end advanced-packaging pool.

Front-end logic wafers are another pool.

A rack can consume both, but their coefficients cannot be added or applied to the same denominator.

This is the central quantitative discipline:

> **Do not divide a packaging coefficient into a foundry-wide front-end wafer total.**

A model can look arithmetically clean while being physically meaningless.

## 6. HBM: manufacturing pressure exceeds simple bit share

Micron disclosed that HBM3E requires roughly **3× the wafer supply of DDR5** for the same number of bits at the same technology node.

This is **A-grade first-party evidence**.

TrendForce estimates that HBM + RDIMM represent about **51% of 2026 DRAM bits**.

Together, these observations show why AI/server memory can consume a disproportionate share of manufacturing input.

The ~3× figure is not:

- a price multiple;
- a permanent universal constant;
- a fab-accounting identity.

It is a defined industry trade ratio.

## 7. Scarcity moves across the three ceilings

The binding constraint can migrate.

### If packaging is tight

Logic exists, but complete systems cannot be assembled fast enough.

### If packaging loosens

HBM or power may become the next bottleneck.

### If HBM expands

Leading-edge logic, power, or utilization can become more important.

This is why the report uses the **Rolling Bottleneck Cascade** rather than declaring one layer permanently dominant.

## 8. Customer concentration must be read carefully

TSMC's **largest / second-largest customer shares were 19% / 17% of 2025 annual revenue**. Those annual rank statistics are not a same-customer longitudinal series. A separate anonymized table shows **Customer A at 12%→19%** and **Customer B at 22%→17%** from 2024 to 2025. The two disclosures must not be stitched together as if the annual largest or second-largest customer were necessarily the same entity each year.

These figures are not:

- CoWoS share;
- N2 share;
- frontier-AI wafer share.

TSMC does not publicly identify the customers in those tables. The forward strategic question is therefore not a fabricated customer trajectory.

It is **incremental scarce-capacity capture** across each physical layer.

## 9. Current macro judgment

As of August 2026:

- advanced logic remains highly concentrated;
- N2 has entered production but customer allocation remains undisclosed;
- advanced packaging is explicitly described by TSMC as growth-limiting;
- HBM's manufacturing-input intensity is confirmed by Micron;
- cloud custom systems continue to bid for the same upstream resources.

The correct macro picture is:

> **process is the entry ticket, packaging is a quantity gate, and HBM is a manufacturing-input multiplier.**

The shortest of the three determines how many complete frontier systems can actually leave the line.

## Key public sources for this essay

- TSMC 4Q25 Presentation — 2025 platform mix / growth: https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
- TSMC 4Q24 Transcript — advanced packaging and testing >8%: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf
- TSMC 4Q25 Transcript — 2025 advanced packaging slightly above 10%, company-corrected: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
- TSMC 2Q26 Earnings Conference Transcript — packaging capacity limits customers' growth: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
- TrendForce — 2026E HBM + RDIMM = 51% of DRAM bit supply: https://www.trendforce.com/presscenter/news/20260825-13198.html
- Micron FY24 Q2 event page: https://investors.micron.com/events/event-details/microns-second-quarter-2024-financial-call
- Micron FY24 Q2 prepared remarks — HBM3E ≈ 3× DDR5 wafer supply: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- TSMC 2025 20-F — annual largest / second-largest customer concentration: https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm
- TSMC 2025 consolidated report — anonymized Customer A/B comparison: https://www.sec.gov/Archives/edgar/data/1046179/000104617926000024/a2025q4consolidatedreport-.htm
