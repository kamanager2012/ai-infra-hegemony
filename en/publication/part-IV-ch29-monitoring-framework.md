# Part IV · Chapter 29: Core Metrics and Evidence-Monitoring Framework

## 1. Long-run research has to be designed as an updateable system

Seller economics, CapEx, HBM, packaging, foundry allocation, power, regulation, and system substitution all change quickly.

The report's conclusions therefore have to be designed for continuous updating rather than being valid only on the publication date.

Every update should answer only three questions:

1. **Which fact changed?**
2. **Which mechanism variable did it change?**
3. **Is the change large enough to alter S1–S4 weighting?**

## 2. Dashboard A — Seller Economics / Forward Reservation

### NVIDIA current anchors

**Table 29.1 — NVIDIA seller economics and forward-reservation baseline**

| Metric | Current public value |
|---|---:|
| FY26 Revenue | US$215.938B |
| FY26 Data Center | US$193.737B |
| FY26 NVIDIA-defined non-GAAP FCF | US$96.575B |
| FY27 Q2 Revenue | US$96.221B |
| FY27 Q2 Data Center | US$89.0B |
| FY27 Q2 GAAP gross margin | 75.0% |
| FY27 Q2 GAAP operating income | US$63.734B |
| Rubin | full production |

**Source:** NVIDIA FY26 results, FY27 Q2 results, and FY27 Q2 Form 10-Q.[^1][^2]  
**Note:** Company-defined non-GAAP FCF and GAAP metrics retain their respective identities; aggregate commitments have no disclosed supplier-level split.

Supply / capacity commitments:

- 2026-01-25: US$95.2B;
- 2026-04-26: US$119B;
- 2026-07-26: US$279B.

These metrics ask whether the system seller still has enough cash generation and forward-commitment capacity to reserve next-generation scarce resources.

The US$279B figure does not contain a supplier-level split and cannot be converted into TSMC or HBM-vendor revenue.

## 3. Dashboard B — Foundry / Packaging

### TSMC 2025

The following baseline is drawn from TSMC's 2025 Annual Report.[^3]

- 12-inch-equivalent wafer shipments: ~15.0M;
- annual capacity: >17M;
- 3 nm / 5 nm / 7 nm wafer revenue: 24% / 36% / 14%;
- ≤7 nm: 74%;
- HPC platform: 58%, +48% YoY;
- smartphone platform: 29%, +11% YoY;
- largest / second-largest annual customer: 19% / 17% of revenue.

A separate anonymized customer table supports only the 2024→2025 Customer A 12%→19% and Customer B 22%→17% trajectories.

The two disclosure types cannot be merged into one customer history.

### Packaging

A-grade signal: TSMC continues to describe packaging capacity as tight / growth-limiting.

B-grade signal: TrendForce estimates NVIDIA at >60% of 2025 CoWoS demand.

TSMC does not disclose customer-level CoWoS allocation.

## 4. Dashboard C — Memory

### A-grade manufacturing anchor

Micron: HBM3E same-node / same-bits ≈ **3× DDR5 wafer supply**; the FY25 10-K further confirms that HBM requires more wafers / cleanroom space.[^5]

### B-grade forward structure

TrendForce: **2026E HBM + RDIMM ≈51% of DRAM bit supply**.[^4]

### Vendor economics

SK hynix FY25:[^6]

- Revenue KRW97.1467T;
- Operating profit KRW47.2063T;
- Operating margin 49%;
- Net income KRW42.9479T;
- HBM revenue more than doubled YoY.

These indicators help test whether HBM product mix continues to absorb DRAM manufacturing input and whether conventional-DRAM residual capacity is loosening.

## 5. Dashboard D — Hyperscaler CapEx

For Microsoft, Amazon, Alphabet, and Meta, preserve separately:

- accounting line item;
- fiscal / calendar window;
- actual vs. guidance / expectation;
- finance-lease treatment;
- AI/data-center-specific disclosure.

The key question is not whether the total is a new record.

It is whether new capital continues flowing into servers, networking, memory, custom silicon, data centers, and power.

Non-comparable accounting definitions must not be mechanically added into an official AI-hardware CapEx total.

## 6. Dashboard E — Power State Machine

**Table 29.2 — Power project state machine**

| State | Meaning |
|---|---|
| Announced | project / target announced |
| Contracted | contract signed |
| Permitted | key permits obtained |
| Energized | actual power delivery |
| Utilized | real sustained load |

**Source:** Report power-state framework.  
**Note:** The state machine prevents headline MW/GW, contract quantity, or project targets from being rewritten as active AI load.

Representative current paths include:

- Microsoft / Constellation: ~835 MW restart PPA;
- Talen / AWS: up to 1.92 GW revised PPA; April-2026 transition status must not be rewritten as full physical delivery complete;
- Google / Kairos: Hermes 2 up to 50 MWe in 2030; fleet up to 500 MWe by 2035.

The variables that need updating are ramp, energized MW, actual load, and utilization.

## 7. Dashboard F — System-Stack Substitution

For Google / AWS / Microsoft / Meta, track:

- production workload share;
- external availability;
- compiler/runtime maturity;
- large-cluster scaling;
- migration cost;
- utilization;
- system TCO.

A single-chip benchmark is not sufficient evidence of system substitution.

## 8. Dashboard G — China's Parallel Stack

Track each layer independently.

### Logic

Domestic accelerators, foundry scale, yield / volume disclosures.

### Memory

HBM-class products, qualification, volume production.

### Packaging

Advanced integration, yield, scale.

### Software

Compiler/runtime, framework compatibility, cluster utilization.

### Deployment

Frontier workloads, data-center power, real system scale.

Frontier-system closure should be upgraded only when several closure gates improve together.

## 9. Dashboard H — Regulation

Use one legal-state machine:

> inquiry / RFI → investigation → Statement of Objections / formal complaint → formal proceeding → final decision → remedy / fine

Do not convert:

- inquiry into "already sued";
- statutory ceiling into "fine is imminent";
- merger review into "monopoly already established."

The variables capable of changing the scenario are interface openness, tying restrictions, access / supply remedies, and structural change.

## 10. Dashboard I — Capital Clearing

### Accounting

Impairment, inventory write-down, accelerated depreciation, asset disposal.

### Utilization / Revenue

Compute utilization, AI-workflow revenue, revenue per deployed compute.

### Market Clearing

Used-system prices, cloud discounts, lease rates, delivery lead times.

### Forward Commitment

CapEx guidance, seller commitments, Anchor Buyer contracts, power contracts.

S4 should move from stress test toward main scenario only when multiple signal groups deteriorate together.

## 11. Evidence-grade quick rules

**Table 29.3 — Default evidence grade for report updates**

| Data type | Default grade |
|---|---|
| company filing / official product / government / court / formal contract | A |
| institutional research | B |
| sell-side / supply-chain / media estimate | C |
| report geometry / stress test / hypothetical rack count | D |

**Source:** Report evidence method (see Chapter 27).  
**Note:** A default grade can move with source quality, but repeated citation does not upgrade it automatically.

Every update preserves the original evidence grade.

A newer number does not automatically become stronger evidence.

## 12. Scenario-weighting update rules

### Move toward S1

System substitution expands, migration cost falls, HBM/packaging/power supply elasticity improves, and multi-buyer access to scarce resources strengthens.

### Move toward S3

Seller commitments keep expanding, multi-layer scarcity persists, switching costs rise, and powered capacity is locked for long periods by a small set of Anchor Buyers.

### Move toward S4

Utilization, market-clearing prices, CapEx / commitments, and accounting losses deteriorate together.

### Remain in S2

Dominant-platform economics stay strong while alternative stacks continue developing; scarce layers remain tight but keep expanding; CapEx remains high while ROI is still serviceable.

## 13. Update discipline

One news item should not rewrite the entire book.

Scenario weighting changes only when a new fact changes a core mechanism variable and crosses a pre-defined threshold.

This keeps the report updateable without rewriting the industry narrative after every product launch, stock-price move, or rumor.

## References

[^1]: NVIDIA, FY26 and FY27 Q2 official results, seller economics and Rubin status, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026 ; https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^2]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^3]: TSMC, 2025 Annual Report, https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^4]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^5]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E wafer-supply trade ratio, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^6]: SK hynix, FY25 Financial Results, https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
