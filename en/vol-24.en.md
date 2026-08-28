# Volume 24: Advanced Packaging, CoWoS, and AI-System Delivery Bottlenecks

Chinese source edition: [vol-24.md](../vol-24.md)

> Retrieval and revision cutoff: **2026-08-27**. This volume keeps three evidence levels separate: TSMC's first-party statements on packaging tightness, institutional estimates of customer demand, and the report's own geometry stress tests.

## 1. Advanced packaging has become a system constraint

Frontier AI accelerators increasingly depend on:

- multi-die integration;
- HBM;
- large interposers;
- high-speed die-to-die connections.

Advanced packaging is therefore no longer just the final manufacturing step.

It has become:

> **a scarce manufacturing layer that can determine whether a frontier AI system can actually be delivered.**

A logic die that exists without the packaging capacity required to combine logic, HBM, and interconnect is not yet a deliverable rack-scale system.

## 2. TSMC's first-party evidence is already sufficient to establish tightness

TSMC described advanced-packaging capacity as **very tight** in its 2024 Q4 discussion and said it could not meet all customer demand.

By 2026 Q2, management said packaging capacity was tight enough to **limit customers' growth**.

TSMC's year-specific wording must be preserved:

- 4Q24 transcript: **advanced packaging and testing >8% of 2024 revenue**;
- 4Q25 transcript, after company correction: **advanced packaging slightly above 10% of 2025 revenue**.

The labels differ, so the two numbers are not treated as a perfectly like-for-like time series.

The company does not publicly provide a customer-level CoWoS allocation table.

The evidence boundary is therefore clear:

> **CoWoS / advanced-packaging tightness is an A-grade fact. Customer-level allocation is not.**

## 3. NVIDIA's >60% share of CoWoS demand is B-grade institutional research

TrendForce estimates that NVIDIA represented more than **60% of 2025 CoWoS demand**.

That estimate is important because it indicates how strongly one platform can influence the packaging market.

But it remains **B-grade institutional research**.

It should not be restated as:

- a TSMC official disclosure;
- actual customer wafer allocation;
- a guaranteed future share.

Its correct use is scenario analysis: if one buyer continues to represent a very large share of demand, residual packaging capacity available to competitors can become strategically important.

## 4. 5.39 CoWoS wafers per rack is a D-grade geometry stress test

The report uses the following geometry stress test:

```text
72 packages
÷ 13.4 packages per wafer
≈ 5.39 CoWoS wafers per rack
```

The coefficient is designed only to illustrate the order of magnitude of packaging pressure created by rack-scale systems.

It is **not**:

- a TSMC yield;
- observed wafer starts;
- logic-wafer demand;
- customer allocation.

The **13.4 packages per wafer** term is itself a geometry assumption, not a TSMC manufacturing disclosure.

The 5.39 coefficient therefore must not be combined with TSMC's roughly 15 million annual 12-inch-equivalent wafer shipments as though both figures described the same production pool.

## 5. Why packaging can become a shorter-term quota than the node itself

Leading-edge logic supply can expand through:

- new fabs;
- process migration;
- capacity additions.

Advanced packaging has a different constraint set.

It depends simultaneously on:

- tools;
- interposers;
- substrates;
- testing;
- process flow;
- HBM integration.

This creates periods in which:

> **logic wafers are available, but complete systems still cannot be delivered at the desired rate.**

Packaging therefore acts as a delivery gate between semiconductor production and usable AI infrastructure.

## 6. Incremental-capacity capture matters more than one monthly capacity estimate

Let new CoWoS capacity be (C), and let one platform capture a fraction (s).

Residual capacity for other buyers is:

```text
Residual = (1 - s) × C
```

| Increment captured by one buyer | Residual for others |
|---:|---:|
| 50% | 50% |
| 60% | 40% |
| 70% | 30% |
| 80% | 20% |

This table is a scenario model, not a forecast of the real customer split.

Its purpose is to show a simple mechanism:

> **As one buyer captures a larger share of incremental scarce capacity, the residual available to second and third buyers falls rapidly.**

That mechanism is more durable than debating an unverified monthly capacity number.

## 7. Cloud custom silicon does not automatically escape CoWoS and HBM

Google, AWS, Microsoft, and Meta are building increasingly complete custom AI systems.

But new generations still rely heavily on combinations of:

- advanced logic;
- HBM;
- advanced packaging.

Custom silicon can change:

- who defines the accelerator;
- who captures software and platform economics.

It does not automatically reduce demand for the same upstream scarce layers.

In some cases, successful custom silicon can increase upstream competition by adding another large buyer of leading-edge logic, HBM, packaging, and power.

## 8. Bottleneck location is not the same as profit-pool location

Advanced packaging can be a system bottleneck without becoming the industry's largest profit pool.

TSMC's 2Q24 management commentary was more specific and time-bounded: advanced-packaging gross margin had historically been **well below** the corporate average and was **approaching** it, but had **not yet reached** the company average at that time. This should not be frozen into a timeless claim that advanced-packaging margins always remain below the corporate average. Source: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2024-08/5122725a56670882d777a8e8bfe0ed247cc55330/TSMC%202Q24%20Transcript.pdf .

A system platform can capture value through a different combination:

- software;
- interconnect;
- integration;
- switching cost;
- customer lock-in.

The distinction is fundamental:

> **bottleneck location ≠ profit location**

A scarce manufacturing step can control delivery while another layer captures more of the economic surplus.

## 9. Advanced packaging is also central to China's frontier-stack closure

A complete China frontier-AI parallel stack requires more than a competitive logic die.

It also requires scalable capability in:

- advanced packaging;
- HBM integration;
- substrates;
- testing;
- high-volume yield.

Logic-node progress without packaging scale cannot deliver a stable large-system supply chain.

Advanced packaging must therefore be analyzed as its own layer rather than hidden inside the broad label “domestic chips.”

## 10. Current judgment

As of **August 2026**:

- TSMC has directly confirmed advanced-packaging tightness;
- institutional research supports the view that NVIDIA has an unusually large influence on CoWoS demand;
- TSMC still does not disclose a customer-level CoWoS split;
- **5.39 wafers per rack** remains a **D-grade geometry stress test**;
- cloud custom silicon continues to compete for many of the same upstream scarce resources.

CoWoS and advanced packaging are therefore among the most important physical quotas in AI infrastructure today.

The analytical discipline is equally important: **first-party tightness, institutional customer-share estimates, and internal geometry stress tests must remain separate evidence classes.**


## Key public sources

- TSMC 4Q24 Transcript — advanced packaging and testing >8%: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf
- TSMC 4Q25 Transcript — 2025 advanced packaging slightly above 10%, company-corrected: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
- TrendForce, 2025 CoWoS demand structure (NVIDIA estimated >60%, B-grade institutional estimate): https://www.trendforce.com/research/download/RP250314ZJ
