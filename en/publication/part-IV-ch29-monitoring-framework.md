# Part IV · Chapter 29: Monitoring Framework — State Variables, Inflection Tests, and Scenario Reweighting

## 1. Monitor variables that can change the view

A long-horizon view is useful only if later evidence can force it to change.

The monitoring framework therefore tracks **state variables, transition rates, and evidence quality — not news volume**. Each new observation must answer three questions:

1. **What changed in the fact layer?**
2. **Which mechanism variable did that change?**
3. **Is the move material and persistent enough to reweight S1–S4?**

This is a structured research-update process, not an automated trading model. The purpose of the dashboard is to prevent one headline, one forecast revision, or one accounting event from being mistaken for a structural regime change.

## 2. Dashboard A — Seller economics / forward reservation

### NVIDIA current anchors

**Table 29.1 — NVIDIA seller economics and forward-reservation baseline**

| Metric | Current public value |
|---|---:|
| FY26 Revenue | US$215.938B |
| FY26 Data Center | US$193.7B |
| FY26 NVIDIA-defined non-GAAP FCF | US$96.575B |
| FY27 Q2 Revenue | US$96.221B |
| FY27 Q2 Data Center | US$89.0B |
| FY27 Q2 GAAP gross margin | 75.0% |
| FY27 Q2 GAAP operating income | US$63.734B |
| Rubin | ramping / in production; production shipments began Q3 FY27 |

**Source:** NVIDIA FY26 results, FY27 Q2 results, and FY27 Q2 Form 10-Q.[^1][^2]  
**Note:** Company-defined non-GAAP FCF and GAAP metrics retain their respective identities; aggregate commitments have no disclosed supplier-level split.

Manufacturing / supply / capacity commitment family:[^2]

- 2026-01-25: US$95.2B;
- 2026-04-26: US$119B;
- 2026-07-26: US$279B.

The underlying mix and duration are not identical across reporting dates, so the sequence is used as a forward-reservation indicator rather than a homogeneous maturity-matched time series.

These metrics test whether the system seller still has sufficient cash generation and forward-commitment capacity to reserve next-generation scarce resources.

The US$279B figure does not contain a supplier-level split and cannot be converted into TSMC or HBM-vendor revenue.[^2]

## 3. Dashboard B — Foundry / packaging

### TSMC 2025

The following baseline combines TSMC's 2025 Annual Report with its 4Q25 presentation / earnings materials.[^3][^16]

- 12-inch-equivalent wafer shipments: ~15.0M;
- annual capacity: >17M;
- 3 nm / 5 nm / 7 nm wafer revenue: 24% / 36% / 14%;
- ≤7 nm: 74%;
- HPC platform: 58%, +48% YoY;
- smartphone platform: 29%, +11% YoY;
- largest / second-largest annual customer: 19% / 17% of revenue.

A separate anonymized customer table in TSMC's annual-report materials supports only the 2024→2025 Customer A 12%→19% and Customer B 22%→17% trajectories.[^3]

The two disclosure types cannot be merged into one customer history.

### Packaging

A-grade signal: TSMC continues to describe packaging capacity as tight / growth-limiting.[^8]

B-grade signal: TrendForce estimates NVIDIA at >60% of 2025 CoWoS demand.[^9]

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

## 5. Dashboard D — Capital formation

For Microsoft, Amazon, Alphabet, and Meta, preserve separately:

- accounting line item;
- fiscal / calendar window;
- actual vs. guidance / expectation;
- finance-lease treatment;
- AI/data-center-specific disclosure.

The key question is not whether the total is a new record.

It is whether new capital continues flowing into servers, networking, memory, custom silicon, data centers, and power.

Non-comparable accounting definitions must not be mechanically added into an official AI-hardware CapEx total.

## 6. Dashboard E — Power delivery state

**Table 29.2 — Power project state machine**

| State | Meaning |
|---|---|
| Announced | project / target announced |
| Contracted / Secured | contract signed or land/power/shell capacity secured |
| Permitted | key permits obtained |
| Construction / Transition | physical buildout or contractual transition underway |
| Energized | actual power delivery |
| Utilized | real sustained load |

**Source:** Report power / LPS state framework.  
**Note:** The state machine prevents headline MW/GW, secured IT-GW, contract quantity, or project targets from being rewritten as active AI load. Generation MW/GW, PPA capacity, and IT-GW must retain their distinct physical identities.

Representative current paths include:

- Microsoft / Constellation: ~835 MW restart PPA;[^10]
- Talen / AWS: up to 1,920 MW revised PPA; the spring-2026 transition plan / subsequent 2026 Q2 status must not be rewritten as full physical delivery complete;[^11]
- Google / Kairos: Hermes 2 up to 50 MWe in 2030; fleet up to 500 MWe by 2035;[^12]
- PORTS-Pike / NVIDIA / SB Energy / OpenAI: initial **4.25 IT-GW design capacity**, representing secured LPS / future phased buildout with planned delivery beginning in 2028.[^13]

The variables to update are each project's transition from secured / contracted status into construction, energized capacity, actual load, and utilization—not headline capacity alone.

Generation MW/GW, PPA capacity, IT-GW, energized facility load, and utilized AI load must remain separate.

## 7. Dashboard F — Second-stack substitution

For Google / AWS / Microsoft / Meta, track:

- production workload share;
- external availability;
- compiler/runtime maturity;
- large-cluster scaling;
- migration cost;
- utilization;
- system TCO.

A single-chip benchmark is not sufficient evidence of system substitution.

## 8. Dashboard G — China closure tests

Track two different levels rather than one localization rate.

### Production-Grade Parallel Stack

Track:

- accelerator / compute delivery;
- HBM-class or equivalent memory subsystem;
- advanced packaging / integration;
- high-speed interconnect;
- compiler/runtime;
- production workload;
- utilization, reliability, and economics.

### Autonomous Frontier Closure

Then separately track:

- advanced-manufacturing continuity;
- equipment / materials / software / service;
- cross-generation process upgrades;
- HBM / packaging / LPS / power continuity;
- long-duration capital and multi-generation scaling.

Production deployment can strengthen the first level without proving the second.

## 9. Dashboard H — Regulatory state

Use one legal-state machine:

> inquiry / RFI → investigation → Statement of Objections / formal complaint → formal proceeding → final decision → remedy / fine

Do not convert:

- inquiry into "already sued";
- statutory ceiling into "fine is imminent";
- merger review into "monopoly already established."

The variables capable of changing the scenario are interface openness, tying restrictions, access / supply remedies, and structural change.

## 10. Dashboard I — Capital clearing / demand quality

### Accounting

Impairment, inventory write-down, accelerated depreciation, asset disposal.

### Utilization / Revenue

Compute utilization, AI-workflow revenue, revenue per deployed compute.

### Market Clearing

Used-system prices, cloud discounts, lease rates, delivery lead times.

### Forward Commitment

CapEx guidance, seller commitments, Anchor Buyer contracts, power contracts.

### Demand Quality / Financing

Customer cash generation, third-party risk capital, supplier equity / credit support, refinancing dependency, asset transferability, and Anchor Buyer utilization.

S4 should move from stress test toward the main scenario only when **multiple causally independent signal families** show broad, persistent, mutually reinforcing deterioration across more than one actor or layer. The five groups are monitoring families, not a mandatory five-of-five gate; Accounting is confirmation / severity evidence, not a prerequisite.

## 10A. Dashboard J — End-system residual pressure

If the report's downstream question is whether important end systems can still obtain enough, stable, affordable resources on their own product cadence, the monitoring framework cannot stop at seller economics, HBM, packaging, and power.

**Table 29.3 — End-system residual-pressure monitoring panel**

| End system | Main public proxies | Question to answer | Must not be inferred |
|---|---|---|---|
| Smartphone / PC | memory contract price, system ASP, allocation fulfillment, configuration change, replacement cycle | is same-price specification progress slowing; is quantity assurance diverging? | AI caused the full price increase; a named buyer lost a known wafer quantity |
| Game console | memory procurement, hardware unit plan, promotion, hardware margin, memory/storage BOM, generation cadence | is memory/storage pressure changing volume, promotion, SKU, or multi-year cost-down? | direct HBM competition; next generation must be delayed/repriced |
| Automotive / industrial | mature-memory price, EOL, lead time, qualified alternates, product-longevity commitments | do long qualification and long lifecycles amplify supply pressure into redesign / continuity risk? | automotive components and AI GPUs share one physical pool |
| Robotics / Physical AI | industrial-electronics lead time + edge-accelerator / memory availability | are industrial and AI-edge constraints appearing together? | every robot requires frontier HBM |
| High-reliability / aerospace / space | trusted access, EOL, qualification capacity, special-process continuity | is the economics of low-volume, long-life, special-process supply deteriorating? | AI caused a specific program delay / cost increase |

**Source:** Chapter 3 layered-exposure framework, Chapter 21 end-system transmission, and Sony / TrendForce game-console evidence.[^14][^15]  
**Note:** This is not a universal shortage index. It tracks **shared-resource exposure, buyer power, qualification rigidity, and quantity assurance** separately. AI-era attribution is strengthened only when upstream resource evidence and downstream outcome evidence align on the same transmission chain.

### Representative first-party anchor: game consoles

Sony's FY2025 Q4 / FY2026 outlook explicitly links FY26 PS5 hardware sales to memory volume procurable at reasonable prices and states that unit sales / promotional plans can be adjusted to manage hardware profitability.[^14]

That creates one of the cleanest current end-system monitoring chains:

> **memory procurement → hardware volume / promotion → profitability**

TrendForce's 2026 console-shipment / memory-BOM estimates remain B-grade quantitative context and do not override Sony's first-party identity.[^15]

### Dashboard J update direction

**Residual pressure strengthening:**

- memory / storage / component contract prices rise;
- allocation fulfillment deteriorates;
- promotion / configuration / SKU plans are adjusted;
- long-life part EOL / lead-time risk rises;
- end-system vendors explicitly link procurement quantity, price, or supply assurance to hardware cadence.

**Residual pressure weakening:**

- allocation fulfillment improves;
- contract price / lead time declines persist;
- same-price configuration progress resumes;
- long-life supply continuity improves;
- supplier product mix rebalances;
- qualified second-source options expand.

Dashboard J does not independently determine S1–S4. It tests whether:

> **upstream scarcity / concentration is actually transmitting into end-system upgrade tax and supply-assurance pressure.**

## 11. Evidence-weighting rules

**Table 29.4 — Default evidence grade for report updates**

| Data type | Default grade |
|---|---|
| company filing / official product / government / court / formal contract | A |
| institutional research | B |
| sell-side / supply-chain / media estimate | C |
| report geometry / stress test / hypothetical rack count | D |

**Source:** Report evidence method (see Chapter 27).  
**Note:** A default grade can move with source quality, but repeated citation does not upgrade it automatically.

Every update must preserve the original evidence grade.

A newer number is not automatically stronger evidence.

## 12. Scenario-reweighting rules

### Move toward S1

System substitution expands, migration cost falls, HBM/packaging/power supply elasticity improves, and multi-buyer access to scarce resources strengthens.

### Move toward S3

Seller commitments keep expanding, multi-layer scarcity persists, switching costs rise, and powered capacity is locked for long periods by a small set of Anchor Buyers.

### Move toward S4

Multiple independent families among utilization/revenue, market clearing, forward commitments, demand-financing quality, and accounting deterioration cross-confirm one another with sufficient causal breadth. Accounting strengthens severity when present but is not required.

### Remain in S2

Dominant-platform economics stay strong while alternative stacks continue developing; scarce layers remain tight but keep expanding; CapEx remains high while ROI is still serviceable.

## 12A. Materiality and persistence follow each variable's clock

The report does **not** impose a universal rule such as "two quarters" or "three months" across all variables.

That would create false precision because semiconductor allocation, memory pricing, power projects, regulatory proceedings, customer contracts, and accounting losses update on different clocks.

Instead, every monitoring variable should specify:

1. **source cadence** — quarterly filing, monthly pricing series, event-driven contract, annual capacity disclosure, etc.;
2. **physical / economic clock** — hardware, fab, data center, grid, contract, or accounting;
3. **comparable baseline** — same denominator, same unit, same evidence identity;
4. **materiality** — large enough to change the relevant mechanism rather than merely create headline volatility;
5. **persistence / confirmation** — supported by comparable follow-up evidence appropriate to that variable;
6. **cross-signal confirmation** — especially for S4, where one weak metric is insufficient.

**Mechanism-break override:** breadth requirements govern **system-level scenario classification**, not whether an underlying mechanism is allowed to survive direct falsification. If a high-quality observation, on the same denominator and time identity, directly breaks a necessary premise of a mechanism, that mechanism must be downgraded, rewritten, or retired immediately even when cross-signal breadth is not yet present. Breadth determines whether the whole S1–S4 state changes; it cannot be used to ignore a broken premise.

### Handling missing data

If a layer does not provide same-unit `AI_Effective_Demand` and `AI_Effective_Capacity`, its Absolute AI Capacity Gap must be labeled **not measurable from public data**.

Growth Gap, lead time, pricing, and allocation fulfillment may be tracked as proxies, but they cannot be renamed as an absolute capacity gap.

### Scenario reweighting

- **Toward S1:** supply elasticity, system substitution, buyer optionality, and portability improve in mutually reinforcing ways;
- **Toward S3:** multi-layer scarcity, switching cost, quantity assurance concentration, and forward reservation strengthen together;
- **Toward S4:** multiple causally independent signal families deteriorate broadly and persistently across actors/layers; at least one real-economy / market / commitment signal must be present, while Accounting is confirmatory rather than mandatory;
- **Otherwise:** keep S2 as the baseline or make only local weighting adjustments rather than changing the main scenario because of one headline.

## 12B. Five headline inflection tests

For readers who want a fast way to judge whether the long-run structure is changing, Dashboards A–J can be compressed into five headline tests. These are not a new model and they do not impose a universal numeric threshold.

1. **Is Non-AI Residual Capacity / Quantity Assurance improving or deteriorating persistently?**  
   Track contract prices, allocation fulfillment, lead times, configuration, promotion, and qualified alternates across smartphones, PCs, game consoles, automotive / industrial systems, rather than relying on gross global wafer or memory capacity.

2. **Has a second System Stack crossed a real production-workload threshold?**  
   Track production-workload share, external availability, migration cost, utilization, and system TCO for Google / AWS / Microsoft / Meta custom systems. A single accelerator benchmark or product launch does not establish system-level substitution.

3. **Is China's Parallel Stack improving both production-grade economics and autonomous closure?**  
   Track real workloads, unit economics, software/runtime, and cluster utilization alongside advanced logic, HBM-class memory, advanced packaging, and equipment / materials / service continuity. A usable production system and a self-sustaining multi-generation frontier stack remain separate tests.

4. **Can utilization, monetization, and independent financing capacity cover the expanding capital base?**  
   Track revenue / utilization, used-system and lease clearing, forward commitments, customer cash generation, third-party risk capital, supplier support, and refinancing dependency. Duration mismatch becomes more dangerous when technical asset life is shorter than financing duration.

5. **Does Power / LPS actually convert from secured to energized and utilized?**  
   The key metric is not headline GW. It is the conversion speed from Contracted / Secured → Permitted → Construction / Transition → Energized → Utilized, and whether Time-to-Power continues to create material delivery differences.

These five tests deliberately avoid arbitrary universal rules such as “eight quarters” or “30%–40%.” A material scenario reweighting requires **comparable continuous observation plus confirmation from at least two independent mechanism dimensions**.

## 13. Evidence-update protocol

No single news item should trigger reclassification of the full report.

Scenario weighting changes only when new evidence changes a core mechanism variable with materiality and persistence appropriate to that variable's own reporting and asset clock.

This keeps the report updateable without reclassifying the industry after every product launch, stock-price move, or rumor.

## References

[^1]: NVIDIA, FY26 and FY27 Q2 official results, seller economics, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026 ; https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027 ; Vera Rubin full-production announcement, https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory ; FY27 Q2 Form 10-Q, production shipments began Q3 FY27, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^2]: NVIDIA Corporation, FY26 Form 10-K, US$95.2B manufacturing / supply / capacity commitments as of 2026-01-25, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm ; FY27 Q2 Form 10-Q, US$119B last quarter and US$279B as of 2026-07-26, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^3]: TSMC, 2025 Annual Report, https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^4]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^5]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E wafer-supply trade ratio, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf ; Micron Technology, FY25 Form 10-K, HBM requires more wafers / cleanroom space for the same bits at the same technology node, https://www.sec.gov/Archives/edgar/data/723125/000072312525000028/mu-20250828.htm
[^6]: SK hynix, FY25 Financial Results, https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/
[^7]: TSMC, 2025 annual-report customer-disclosure materials; see [^3].
[^8]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging tightness limiting customer growth, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^9]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^10]: Constellation, Crane Clean Energy Center / Microsoft 20-year PPA and approximately 835 MW unit, https://investors.constellationenergy.com/news-releases/news-release-details/constellation-launch-crane-clean-energy-center-restoring-jobs
[^11]: Talen Energy, 2026 Q2 Form 10-Q and 2025 Form 10-K, revised AWS PPA state and ramp, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm ; https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
[^12]: Kairos Power / Google partnership, Hermes 2 up to 50 MWe in 2030 and fleet up to 500 MWe by 2035, https://www.kairospower.com/google
[^13]: NVIDIA, PORTS-Pike Technology Campus / SB Energy / OpenAI, 2026-08-17, initial 4.25 IT-GW design capacity and phased online plan beginning in 2028, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx


[^14]: Sony Group, FY2025 Q4 earnings speech / FY2026 outlook, PS5 hardware-sales / promotion management tied to memory procurement at reasonable prices, https://www.sony.com/en/SonyInfo/IR/library/presen/er/pdf/25q4_sonyspeech.pdf
[^15]: TrendForce, 2025-12-02, 2026 game-console shipment forecast and estimated console memory-cost share of BOM, B-grade institutional forecast, https://www.trendforce.com/presscenter/news/20251202-12811.html
[^16]: TSMC, 4Q25 Presentation / Earnings Conference, 5 nm / 7 nm 2025 technology mix and HPC / smartphone YoY platform growth, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf ; https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
