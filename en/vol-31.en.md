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
| FY26 revenue | **$215.938B** |
| FY26 Data Center revenue | **$193.737B** |
| FY26 free cash flow | **$96.575B** |
| FY27 Q2 revenue | **$96.221B** |
| FY27 Q2 Data Center revenue | **$89.0B** |
| FY27 Q2 GAAP gross margin | **75.0%** |
| FY27 Q2 GAAP operating income | **$63.734B** |
| Rubin | **full production** |

These indicators answer a strategic question:

> **Does the system platform still generate enough profit and cash flow to reserve the next generation of scarce resources?**

High seller economics do not prove permanent monopoly.

They do show the financial ability to make large forward commitments.

### Supply commitments

NVIDIA reported supply-related commitments of:

- **$95.2B** at FY26 year-end;
- **$119.0B** at FY27 Q1.

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
- HPC platform: **58%**;
- Smartphone platform: **29%**;
- largest customer: **19% of annual revenue**;
- second-largest customer: **17%**;
- advanced packaging + testing: slightly above **10%** of revenue.

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

For 2026:

- HBM + RDIMM represent approximately **51% of DRAM bits**.

Together, those observations help monitor conventional-DRAM residual capacity.

### SK hynix

FY25:

- revenue: **KRW 97.1467T**;
- operating profit: **KRW 47.2063T**;
- operating margin: **49%**;
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

Scope consistency matters more than producing one visually impressive four-company total.

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
- Talen / AWS: revised PPA up to **1.92 GW**;
- Google / Kairos: development target up to **500 MW**.

The Talen/AWS front-of-the-meter conversion was completed in **April 2026**.

The next variables are therefore:

- contract ramp;
- energized MW;
- actual data-center load;
- utilization.

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
