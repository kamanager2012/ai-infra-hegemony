# Volume 31: Core Indicators and Evidence-Monitoring Framework

Chinese source edition: [vol-31.md](../vol-31.md)

> Retrieval and revision cutoff: **2026-08-27**. The purpose of this volume is to make the report continuously updateable. It defines which observations can change the main judgment and which should remain supporting evidence.

## 1. Why the report needs a monitoring framework

A long-horizon industry report cannot be valid only on the day it is published.

The key variables in AI infrastructure move quickly:

- seller economics;
- hyperscaler CapEx;
- HBM supply;
- advanced packaging;
- foundry allocation;
- power;
- regulation;
- system-stack substitution.

This volume is therefore not a historical-data appendix.

It is a **monitoring framework** for updating the report's mechanisms and scenarios as new evidence arrives.

## 2. Seller economics

### NVIDIA

Current core anchors:

| Indicator | Value |
|---|---:|
| FY26 revenue | **US$215.938B** |
| FY26 Data Center revenue | **US$193.737B** |
| FY26 non-GAAP free cash flow (NVIDIA definition) | **US$96.575B** |
| FY27 Q2 revenue | **US$96.221B** |
| FY27 Q2 Data Center revenue | **US$89.0B** |
| FY27 Q2 GAAP gross margin | **75.0%** |
| FY27 Q2 GAAP operating income | **US$63.734B** |
| Rubin | **full production** |

These indicators answer a strategic question:

> **Does the system platform still generate enough profit and cash flow to reserve the next generation of scarce resources?**

High seller economics do not prove permanent monopoly.

They do show the financial ability to make large forward commitments.

### Supply commitments

NVIDIA reported manufacturing, supply, and capacity commitments of:

- **US$95.2B** as of 2026-01-25;
- **US$119B** as of 2026-04-26;
- **US$279B** as of 2026-07-26.

Scope: the FY27 Q2 10-Q says the latest commitments are primarily tied to memory and manufacturing facilities. These remain aggregate commitments, not a disclosed single-supplier order.

These commitments are useful as a forward proxy for resource reservation.

They should not be decomposed into supplier-level amounts that the company has not disclosed.

## 3. Foundry and advanced packaging

### TSMC 2025

Key public anchors include:

- approximately **15.0M** 12-inch-equivalent wafer shipments;
- annual capacity above **17M** wafers;
- 3 nm: **24%** of wafer revenue;
- 5 nm: **36%**;
- 7 nm: **14%**;
- 7 nm and below: **74%**;
- HPC platform: **58%** of revenue, with platform revenue up **48% YoY**;
- Smartphone platform: **29%** of revenue, with platform revenue up **11% YoY**;
- 2025 largest customer: **19% of annual revenue**;
- 2025 second-largest customer: **17%**;
- 2025 advanced packaging: slightly above **10%** under the company-corrected 4Q25 wording; the 2024 >8% disclosure used the distinct label “advanced packaging and testing.”

**Customer-scope hard boundary:** annual largest / second-largest rankings are not a same-customer time series. A separate anonymized table provides the directly comparable 2024→2025 series: Customer A **12%→19%**, Customer B **22%→17%**. The two disclosure formats must not be stitched together into one customer's longitudinal trajectory.

### Packaging status

TSMC has directly described advanced-packaging capacity as:

- very tight;
- unable to meet all customer demand;
- tight enough to limit customers' growth.

That makes packaging tightness **A-grade first-party evidence**.

### CoWoS demand allocation

TrendForce's estimate that NVIDIA represented more than **60% of 2025 CoWoS demand** is **B-grade institutional research**.

TSMC does not publish customer-level CoWoS allocation.

The two evidence types should remain separate.

## 4. Memory

### Micron

The core A-grade physical anchor is:

> **HBM3E requires roughly 3× the wafer supply of DDR5 to produce the same number of bits at the same technology node.**

Micron's FY25 10-K further confirms that HBM requires more wafers and cleanroom space for the same bit output.

### TrendForce

**2026E institutional forecast:**

- HBM + RDIMM represent approximately **51% of DRAM bit supply**.

The 51% figure is a forecast bit share, not an observed full-year actual, wafer share, or revenue share.

Together with Micron's 3× trade-ratio disclosure, it helps monitor conventional-DRAM residual capacity.

### SK hynix

FY25:

- revenue: **KRW 97.1467T**;
- operating profit: **KRW 47.2063T**;
- operating margin: **49%**;
- net income: **KRW 42.9479T**;
- HBM revenue: more than doubled year over year.

These indicators help determine whether the HBM product mix continues to support unusually strong memory-vendor economics.

## 5. Hyperscaler CapEx

The four major cloud companies should be tracked individually.

Their accounting windows and definitions differ, so the report should monitor:

- Microsoft CapEx;
- Amazon net PPE purchases;
- Alphabet CapEx;
- Meta CapEx;
- finance-lease treatment;
- AI/data-center-specific disclosures.

The important question is not only whether the aggregate headline reaches a new record.

It is:

> **Is incremental capital still flowing primarily into AI servers, networking, memory, data centers, and power?**

Scope consistency matters more than producing one visually impressive four-company total. Actuals, guidance, and expectations must retain their separate identities.

## 6. Power

Energy projects are tracked through five states:

| State | Meaning |
|---|---|
| Announced | project or target has been announced |
| Contracted | a binding commercial agreement exists |
| Permitted | key approvals have been obtained |
| Energized | power is physically delivered |
| Utilized | real workload is drawing the power |

Current important projects include:

- Microsoft / Constellation: approximately **835 MW** restart PPA;
- Talen / AWS: revised-PPA full contract quantity **up to 1,920 MW**. The 2026 Q2 10-Q states that the transition occurred in **April 2026**, while the 2025 10-K had expected full transition in **spring 2027**. April 2026 is not evidence that all physical delivery was complete;
- Google / Kairos: Hermes 2 **up to 50 MWe in 2030**, followed by a fleet **up to 500 MWe by 2035**.

The next variables are therefore:

- contract ramp;
- energized MW;
- actual data-center load;
- utilization.

A contracted maximum must not be restated as real-time AI-rack load.

## 7. System-stack substitution

The monitoring framework follows the major alternative stacks separately.

### Google
- TPU / Ironwood;
- compiler/runtime;
- pod scale;
- external availability.

### AWS
- Trainium;
- Neuron;
- UltraServer;
- Anthropic workload.

### Microsoft
- Maia;
- Azure workloads;
- software maturity.

### Meta
- MTIA;
- internal workloads;
- generative-AI expansion.

The meaningful substitution indicators are not isolated chip benchmarks.

They are:

- frontier-workload share;
- utilization;
- migration cost;
- system TCO;
- production scale.

A custom chip matters strategically when it changes deployed system economics.

## 8. China's parallel stack

Progress should be tracked separately by layer.

### Logic
- domestic accelerators;
- foundry scale;
- yield and volume disclosures.

### Memory
- HBM-class products;
- qualification;
- volume production.

### Packaging
- advanced integration;
- scale;
- yield.

### Software
- CANN and other compiler/runtime systems;
- framework compatibility;
- cluster utilization.

### Deployment
- frontier workloads;
- data-center power;
- real system scale.

Only broad improvement across these layers should justify upgrading the judgment that China has closed a complete frontier-AI parallel stack.

## 9. Regulation

Legal state should be tracked procedurally:

1. inquiry / information request;
2. investigation;
3. statement of objections / complaint;
4. formal proceeding;
5. final decision;
6. remedy / fine.

The following shortcuts are invalid:

- inquiry → “already sued”;
- statutory ceiling → “fine is imminent”;
- merger review → “monopoly already established.”

The regulatory variables that can materially change the industrial model are:

- interface openness;
- tying restrictions;
- supply-discrimination rules;
- structural remedies.

## 10. Capital-clearing signals

For **S4 Capital Hard Landing**, the report monitors four groups.

### Accounting
- impairments;
- inventory write-downs;
- accelerated depreciation.

### Utilization / Revenue
- compute utilization;
- AI-workflow revenue;
- revenue per unit of deployed compute.

### Market Clearing
- second-hand system prices;
- cloud discounts;
- delivery lead times.

### Forward Commitments
- CapEx guidance;
- supply commitments;
- long-duration compute contracts;
- power contracts.

S4 should become the dominant interpretation only when several groups deteriorate together.

## 11. Evidence-grade quick reference

| Evidence | Grade |
|---|---|
| NVIDIA / TSMC / Micron official disclosures | A |
| Government, regulator, court, formal contract | A |
| TrendForce / OECD / IEA / Stanford HAI | B |
| Investment-bank, supply-chain, or media estimate | C |
| 5.39 CoWoS wafers/rack | D |
| Hypothetical rack-count demand | D |

The grade describes the evidentiary basis of a claim, not whether the mechanism itself is economically important.

## 12. Update rule

Every future update should ask three questions:

1. **Which fact changed?**
2. **Which mechanism variable does that fact change?**
3. **Is the change large enough to alter the relative interpretation of S1–S4?**

This prevents one news item from forcing an unnecessary rewrite of the entire industrial narrative.

The value of the monitoring framework is not that it contains the most numbers.

It is that it keeps the report **continuously calibratable to reality**.

## Key public sources for this volume

- NVIDIA FY27 Q2 official results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- NVIDIA FY27 Q2 10-Q — US$279B commitments: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
- TSMC 2025 Annual Report: https://investor.tsmc.com/static/annualReports/2025/english/index.html
- TSMC 2025 20-F — annual customer rankings: https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm
- TSMC 2025 consolidated report — Customer A/B: https://www.sec.gov/Archives/edgar/data/1046179/000104617926000024/a2025q4consolidatedreport-.htm
- TrendForce — 2026E HBM + RDIMM = 51% of DRAM bit supply: https://www.trendforce.com/presscenter/news/20260825-13198.html
- Micron FY24 Q3 prepared remarks — HBM3E ≈ 3× DDR5 wafer supply: https://investors.micron.com/static-files/4550f98c-1054-4847-a929-c17d520a0564
- SK hynix FY25 official results: https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
- Constellation / Microsoft Crane restart (~835 MW): https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
- Talen 2026 Q2 10-Q — up to 1,920 MW; full volume no later than 2032: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
- Kairos / Google — 50 MWe in 2030; up to 500 MWe by 2035: https://www.kairospower.com/google

- TSMC 4Q24 Transcript — 2024 advanced packaging and testing >8%: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf
- TSMC 4Q25 Transcript — 2025 advanced packaging slightly above 10%, company-corrected: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
