# P0-1 · Chapter 24 Historical Backtest of Five Capital-Clearing Signal Families v1.0

> **Status:** Research-side validation; not part of the formal 32-chapter publication.  
> **Purpose:** test whether Chapter 24's five signal families can distinguish systemic capital clearing, segment-level clearing, and severe inventory/capacity corrections that do not become system-wide S4.  
> This file does not create a formal trigger threshold and does not change Chapter 24 by itself.

## 1. Signal families under test

The five Chapter 24 signal families are:

1. **Accounting** — impairment, inventory write-down, accelerated depreciation, asset disposal;
2. **Utilization / Revenue** — whether deployed assets, utilization, revenue, or monetization deteriorate relative to the installed asset base;
3. **Market Clearing** — inventory, channel/resale pricing, discounting, lead time, resale liquidity, lease clearing;
4. **Forward Commitment** — CapEx guidance, orders, supply commitments, long-duration capacity reservations, project delays/cancellations;
5. **Demand Quality / Financing** — customer cash flow, financing availability, supplier support, refinancing dependence, willingness of independent third-party risk capital.

The objective is not to make every case fit all five families. A missing or structurally unobservable family remains **N/A**.

## 2. Pre-registered-style backtest rules

To reduce hindsight freedom:

- use contemporaneous or later formal disclosures that describe the period being evaluated;
- do not infer an earlier signal merely because the cycle later crashed;
- score each signal family independently;
- do not substitute equity-price declines for operating or financing evidence;
- preserve contrary evidence explicitly;
- do not require all five families to appear in the same quarter because accounting, clearing, financing, and commitment signals have different clocks;
- do not optimize weights or thresholds on the current sample;
- record **N/A** instead of force-mapping a missing signal.

### 2.1 Research-side ordinal score

For cross-case comparison only:

- **0** — no deterioration or strong contrary evidence;
- **1** — credible deterioration exists but persistence/breadth is weak;
- **2** — formal confirmation, repeated deterioration, or multiple independent observations;
- **N/A** — the variable cannot be observed reliably in that case.

Research-side labels:

- **Broad clearing:** at least four signal families deteriorate, with at least two strong real-economy/commitment/accounting confirmations;
- **Partial clearing:** two to three signal families deteriorate strongly, or deterioration is confined to one demand segment;
- **No systemic clearing:** key demand, utilization, financing, or forward-commitment evidence remains strongly contrary.

These are calibration aids, not production thresholds.

### 2.2 Proxy hierarchy

| Signal | Tier 1 — preferred | Tier 2 — secondary | Tier 3 — auxiliary only |
|---|---|---|---|
| Accounting | 10-K/10-Q/annual-report impairment, inventory provision, write-down, disposal, accelerated depreciation | official earnings/CFO commentary | media or analyst estimate |
| Utilization / Revenue | disclosed utilization, segment revenue, revenue per deployed asset, monetization | institutional shipment/order/usage statistics | single-channel survey, equity price |
| Market Clearing | official/company channel inventory, pricing programs, lead time, resale/lease clearing | high-quality industry pricing/inventory databases | scattered secondary-market quotes |
| Forward Commitment | first-party CapEx guidance, supply/purchase commitments, contract capacity, project delay/cancel | regulatory/project-finance filings, institutional aggregation | rumor |
| Demand Quality / Financing | customer cash flow, credit conditions, formal financing, supplier equity/credit support, refinancing | central-bank/regulatory credit evidence, high-quality financing data | valuation/risk-appetite proxy |

Hard rules:

- equity prices, valuation, or media sentiment cannot independently move a signal from 0 to 2;
- repeated sentences from one company disclosure remain one evidence origin;
- a price decline caused by technology migration is not automatically Market Clearing;
- a CapEx reduction caused by timing/mix/architecture migration is at most weak evidence unless cancellation, renegotiation, utilization, or demand deterioration confirms it.

### 2.3 Segment breadth

Every case also records **Segment Breadth**, outside the 10-point score:

- **Narrow** — one demand source, generation, product, or downstream segment;
- **Multi-segment** — at least two economically distinct segments deteriorate;
- **System-wide** — supplier, buyer, commitment, and financing layers deteriorate across the system.

A Narrow case cannot be promoted to system-wide S4 merely because the observable signals are severe.

### 2.4 Lead / lag fields

Each case records:

1. **First deterioration**
2. **Cross-confirmation**
3. **Accounting confirmation**
4. **Trough / stabilization** — ex post only unless explicitly relabeled as a prospective stabilization candidate

When source precision is quarterly or semiannual, the backtest preserves that range rather than inventing monthly precision.

### 2.5 False-positive constraint

Every candidate clearing event must actively search for contrary evidence such as:

- core segment revenue/utilization still expanding;
- forward commitment delayed rather than cancelled;
- capital migrating from legacy/non-AI assets into a new architecture rather than disappearing;
- inventory clearing explained by product transition;
- financing tightening not transmitting into actual project cuts.

Contrary evidence belongs in the main table, not in a footnote.

---

# 3. Case A — 2000–2002 Internet / Telecom Capital Bust

## 3.1 Why this is a positive systemic case

Communications and network-equipment investment expanded rapidly through 1999–2000 and entered a severe capital clearing in 2001.

Federal Reserve data later summarized that U.S. real spending on communications equipment shifted from more than 20% average annual growth in 1998–2000 to a decline of more than **30% in 2001**.

## 3.2 Signal replay

| Signal | Contemporaneous evidence | Score |
|---|---|---:|
| Accounting | Cisco FY2001 provision of **US$2.77B** for inventory/purchase commitments plus roughly **US$1.17B** restructuring/impairment/excess-facility charges | 2 |
| Utilization / Revenue | Cisco on 2001-04-16 expected fiscal Q3 revenue to fall about **30% q/q**; Fed later recorded >30% decline in communications-equipment investment for 2001 | 2 |
| Market Clearing | March-2001 Beige Book reported high telecom-equipment inventories; Cisco inventory turns fell sharply as demand weakened against long-lead procurement | 2 |
| Forward Commitment | Cisco expected capital-spending slowdown to persist; carriers slowed network deployment and CapEx; telecom/high-tech orders and plans remained weak | 2 |
| Demand Quality / Financing | constrained capital markets, high debt, carrier bankruptcies, difficult financing, and excess network capacity jointly reduced CapEx | 2 |

**Research result: 10/10 — Broad clearing.**

## 3.3 Timing

- **2000 Q4:** high-tech investment growth decelerates;
- **2001 Mar:** high telecom inventories, corporate CapEx cuts, Cisco cost reduction;
- **2001 Apr:** Cisco discloses sudden demand decline and ~30% q/q revenue guidance drop; FY2001 later confirms a roughly **US$2.25B** fiscal-Q3 excess-inventory charge and **US$2.77B** full-year inventory/purchase-commitment provision;
- **2001 H2:** carrier financing constraints, excess capacity, bankruptcies, and CapEx cuts broaden;
- **early 2002:** Fed confirms >30% 2001 communications-equipment investment decline and continued excess-capacity pressure.

### 3.4 Implication

A real capital clearing is not "technology stocks fell."

It is a cross-confirmation of:

> **Accounting + Utilization/Revenue + Market Clearing + Forward Commitment + Financing**

with several leading signals visible before annual accounting/statistical confirmation.

---

# 4. Case B — 2018–2019 Cryptocurrency / GPU Channel Unwind

This is a genuine clearing event with much narrower breadth than the 2001 telecom bust.

## 4.1 Signal replay

| Signal | Contemporaneous evidence | Score |
|---|---|---:|
| Accounting | NVIDIA FY2019 Q3 recorded about **US$57M** charge after crypto-mining demand fell sharply; Q4 added roughly **US$128M** excess DRAM/component charges | 2 |
| Utilization / Revenue | FY2019 Q4 revenue **US$2.21B, -31% q/q**; Gaming **US$954M, -46% q/q**; Data Center **-14% q/q** | 2 |
| Market Clearing | NVIDIA disclosed post-crypto **excess channel inventory**, reduced shipments, and delayed planned ramps to clear Pascal mid-range inventory over one to two quarters | 2 |
| Forward Commitment | 2019-01-28 Q4 revenue guidance cut from **US$2.70B to US$2.20B**; production ramp delayed; crypto-specific revenue expected to become negligible | 2 |
| Demand Quality / Financing | crypto-linked demand disappeared, but the case lacks a clean customer-cash-flow / supplier-finance / refinancing analogue | N/A |

**Research result: 8/8 observable points — Strong Partial / segment clearing, not five-family broad clearing.**

## 4.2 Contrary evidence

FY2019 full-year NVIDIA revenue still rose 21% and Data Center revenue rose 52%.

A Q4 Gaming/channel collapse therefore cannot be promoted into a whole-platform or whole-accelerated-compute system collapse.

## 4.3 Timing tightening

- **2018 Aug (FY2019 Q2):** NVIDIA still reported record platform revenue — strong evidence against backdating the clearing;
- **2018 Nov (FY2019 Q3):** excess channel inventory post crypto boom becomes public;
- **2019 Jan 28:** guidance is cut sharply and production ramps are delayed to clear inventory;
- **FY2019 Q3–Q4:** inventory/component charges confirm the accounting impact;
- **2019 H1:** channel normalization expected over roughly one to two quarters.

| Timing field | Case B |
|---|---|
| First public deterioration | 2018 Q4 / Nov disclosure |
| Cross-confirmation | 2019 Jan |
| Accounting confirmation | FY2019 Q3–Q4 |
| Trough / stabilization | 2019 H1 |
| Confidence | Medium–High |

### 4.4 Implication

The protocol needs both **signal breadth** and **segment breadth**.

A single demand source can produce severe Accounting, Revenue, Market Clearing, and Forward Commitment deterioration without becoming system-wide S4.

---

# 5. Case C — 2022–2023 GPU / Channel Correction + Cloud Optimization

This is a negative/partial-control case.

## 5.1 Signal replay

| Signal | Contemporaneous evidence | Score |
|---|---|---:|
| Accounting | NVIDIA FY2023 recorded **US$2.17B** inventory charges tied mainly to excess Ampere Gaming/Data Center supply and purchase obligations | 2 |
| Utilization / Revenue | Gaming FY2023 revenue **-27% YoY**, but Data Center **+41% YoY** | 1 |
| Market Clearing | NVIDIA Q2 FY2023 Gaming revenue **-44% q/q** with channel pricing programs and intentional under-shipping | 2 |
| Forward Commitment | Meta reduced 2023 CapEx guidance from US$34–37B to US$30–33B and later US$27–30B, but explicitly attributed part to non-AI server savings and project timing; 2024 CapEx was then expected to re-accelerate with AI/data-center investment | 1 |
| Demand Quality / Financing | no telecom-style financing break; AI demand/commitment strengthened again in 2023 | 0 |

**Research result: 6/10 — Partial / sector clearing; no system-wide S4.**

## 5.2 Why the negative control matters

Accounting and Market Clearing looked severe in isolation, but cross-segment evidence remained contrary:

- Data Center continued growing;
- Meta did not cancel AI capacity — it changed mix/timing;
- 2024 forward commitment re-accelerated;
- no system-wide financing break appeared.

## 5.3 Timing tightening

On **2022-08-08**, NVIDIA disclosed:
- revenue ~US$6.70B vs US$8.10B outlook;
- Gaming -44% q/q;
- lower sell-in after weaker channel-partner sales;
- channel pricing programs;
- about **US$1.32B** inventory/related charges based on revised demand expectations.

On **2022-08-24**, NVIDIA said OEM/channel inventory reduction would continue into Q3 while Data Center was expected to grow sequentially.

| Timing field | Case C |
|---|---|
| First public deterioration | 2022 Aug 8 |
| Cross-confirmation | 2022 Aug 8–24, segment-level only |
| Accounting confirmation | 2022 Aug — nearly synchronous |
| Trough / stabilization | 2022 H2–2023 H1; AI/Data Center reversed earlier |
| Confidence | High for first signal; Medium for trough |

**Counterexample:** inventory-led clearing can produce Accounting confirmation almost simultaneously with market clearing.

---

# 5A. Case D — 2008–2009 GFC / Enterprise IT

This case tests whether broad clearing can be confirmed without a 2001-style seller impairment.

## 5A.1 Evidence

Federal Reserve contemporaneous material shows:

- **2008 H1:** sales, profits, and credit conditions deteriorated; firms postponed/abandoned expansion;
- **2008 Q4:** real equipment & software investment fell about **28% annualized**;
- **2008 H2:** real IT investment fell about **12.5% annualized on average**;
- **2009 Q1:** real equipment & software fell about **34% annualized**;
- credit availability remained tight and borrowing costs increased;
- Cisco FY2009 revenue fell **9% YoY**, product revenue roughly **12%**.

Cisco did not record a telecom-bust-scale seller impairment.

## 5A.2 Signal replay

| Signal | Contemporaneous evidence | Score |
|---|---|---:|
| Accounting | no 2001-scale enterprise-IT seller write-down | 0 |
| Utilization / Revenue | 2008Q4 E&S ~-28% annualized; 2009Q1 ~-34%; 2008H2 IT ~-12.5%; Cisco FY2009 revenue -9% | 2 |
| Market Clearing | broad business inventory liquidation; enterprise-IT-specific resale/channel evidence weaker | 1 |
| Forward Commitment | firms postponed/abandoned expansion; 2008Q4–2009H1 investment collapsed | 2 |
| Demand Quality / Financing | reduced credit availability / higher cost; conditions remained tight into 2009H1 | 2 |

**Research result: 7/10 — Broad / macro-systemic clearing.**

## 5A.3 Timing

- **First deterioration:** 2007 Q4–2008 H1;
- **Cross-confirmation:** 2008 Q4;
- **Accounting confirmation:** no qualifying hard accounting signal;
- **Trough / stabilization:** 2009 H1 trough ex post; H2 stabilization/recovery evidence.

### 5A.4 Implication

> **Accounting is a confirmation/severity channel, not a mandatory S4 gate.**

Financing + Forward Commitment + Utilization/Revenue can confirm broad clearing even without a giant seller impairment.

---

# 6. Case E — 2001–2003 Semiconductor Downcycle

Case E belongs to the same macro episode as Case A and must not be double-counted as an independent crisis.

## 6.1 Signal replay

| Signal | Contemporaneous evidence | Score |
|---|---|---:|
| Accounting | Micron memory-inventory write-downs of about **US$727M** in 2001 and **US$376M** in 2002; Intel flash-memory results also hit by inventory write-down and under-utilization | 2 |
| Utilization / Revenue | U.S. semiconductor/electronic-component capacity utilization fell from about **93.2%** in Jul-2000 to **58.8%** in Nov-2001; 2001 industry sales fell >30% | 2 |
| Market Clearing | Micron ASP about **-60%** in 2001 and **-53%** in 2002; customer inventory-reduction programs and excess capacity sustained pricing pressure | 2 |
| Forward Commitment | STMicroelectronics closed/selectively idled fabs; Fed revised semiconductor/computer capacity-growth estimates down | 2 |
| Demand Quality / Financing | not independently observable at telecom/GFC strength | N/A |

**Research result: 8/8 observable points — Broad semiconductor-layer clearing.**

## 6.2 Timing

- **2000 H2:** utilization starts falling;
- **2001 H1:** utilization, orders, inventories, pricing deteriorate together;
- **2001 H2:** utilization approaches ~60%; shutdowns and write-downs appear;
- **2002:** ASP remains under severe pressure;
- **2003:** utilization recovers into roughly the 70–80% range.

Typical sequence:

> **Utilization / Market Clearing → Accounting / Capacity Retrenchment → Recovery**

## 6.3 Implication

Market Clearing and Utilization are often earlier than Accounting, and Financing is not mandatory for a physical manufacturing clearing.

### 6.4 Correlation warning

Cases A and E are two layer observations of one 2000–2002 macro episode, not two independent validations.

---

# 7. Case F — 2014–2016 Oil & Gas Upstream Capital Clearing

This is the strongest non-technology cross-industry positive case.

## 7.1 Signal replay

| Signal | Contemporaneous evidence | Score |
|---|---|---:|
| Accounting | Halliburton 2015 ~**US$2.2B** impairments/other charges; Apache 2015 ~**US$9.47B** impairments | 2 |
| Utilization / Revenue | U.S. land rig count fell about **64%** from Nov-2014 peak to Dec-2015; Halliburton 2015 revenue **-28% YoY**; 2016 average U.S. rig count nearly **75% below** Nov-2014 peak | 2 |
| Market Clearing | widespread service pricing pressure; offshore dayrate/utilization declines and fleet impairment | 2 |
| Forward Commitment | U.S. mining/exploration investment fell about **35% in 2015**; ConocoPhillips 2015 CapEx **-41% vs 2014**; major producers reduced plans | 2 |
| Demand Quality / Financing | operating cash flow compressed; firms cut CapEx and used more debt/equity; banks tightened oil/gas underwriting/credit lines; classified commitments increased | 2 |

**Research result: 10/10 — Multi-segment / industry-wide broad clearing.**

## 7.2 Timing

- **2014 H2:** commodity-price collapse;
- **2014 Q4–2015 Q1:** rig count, activity, CapEx plans fall;
- **2015 Q2:** bank underwriting/credit-line tightening becomes visible;
- **2015 H2:** cash-flow, debt-service, pricing, utilization, and CapEx deterioration cross-confirm;
- **2015–2016:** large impairments/accounting confirmation;
- **2016 Q2–Q4:** stabilization/recovery evidence emerges.

## 7.3 Implications

1. The framework is not technology-bubble-specific.
2. Financing can act as a mid-cycle amplifier rather than the initial trigger.
3. Lower prices can both signal clearing and create conditions for later rebalance.

---

# 8. Case G — 2018–2019 Hyperscale Cloud CapEx Digestion

Independent negative control.

Alphabet CapEx rose from roughly **US$13.2B in 2017** to **US$25.1B in 2018**, then fell modestly to about **US$23.5B in 2019**.

That alone could be misread as a cloud-infrastructure clearing.

Contrary cross-company evidence:

- AWS 2019 revenue **+37%**, from US$25.7B to US$35.0B;
- AWS PP&E additions rose from roughly **US$9.8B to US$13.1B**;
- Facebook 2019 CapEx rose from roughly **US$13.9B to US$15.1B**, with 2020 guidance **US$17–19B**;
- Google Cloud revenue rose from roughly **US$5.84B to US$8.92B**.

## 8.1 Signal replay

| Signal | Evidence | Score |
|---|---|---:|
| Accounting | no broad cloud-overbuild impairment | 0 |
| Utilization / Revenue | AWS +37%; Google Cloud high growth | 0 |
| Market Clearing | no cross-hyperscaler resale/inventory clearing | 0 |
| Forward Commitment | Alphabet CapEx down modestly, but AWS asset additions and Facebook CapEx increased | 1 |
| Demand Quality / Financing | strong operating cash flow, no broad financing break | 0 |

**Research result: 1/10 — Narrow/company-specific; No systemic clearing.**

## 8.2 Implication

> **CapEx growth deceleration ≠ CapEx contraction ≠ system-wide clearing.**

Forward Commitment must be read with revenue/utilization and cross-company breadth.

---

# 9. Case H — 2011–2013 Solar PV Manufacturing Overcapacity

Independent manufacturing-capital-cycle positive case.

The mechanism:

> **policy-supported demand + rapid upstream expansion → excess capacity → price clearing → utilization decline → capacity restructuring / impairment → financing pressure**

Evidence included:
- sector-wide excess manufacturing capacity and falling module/wafer/polysilicon prices;
- Suntech cell utilization around **60%** with annualized cell capacity reduced to about **1.8 GW**;
- First Solar 2012 restructuring of roughly **US$127M**, including about **US$99.2M** tied to cancellation of the Vietnam four-line plant;
- Applied Materials solar-equipment order/revenue collapse plus impairment/inventory/restructuring;
- project-financing constraints causing cancellations, postponements, or scale-backs.

## 9.1 Signal replay

| Signal | Evidence | Score |
|---|---|---:|
| Accounting | First Solar / Applied Materials / other manufacturer impairments, write-downs, restructuring | 2 |
| Utilization / Revenue | Suntech cell utilization ~60%; solar-equipment orders/revenue fell sharply | 2 |
| Market Clearing | polysilicon/wafer/module prices fell sharply, sometimes below production cost | 2 |
| Forward Commitment | cancelled expansion, idled lines, capacity rationalization | 2 |
| Demand Quality / Financing | project financing tightened; projects were cancelled/delayed/scaled back; some manufacturers faced liquidity/going-concern pressure | 2 |

**Research result: 10/10 — Multi-segment / system-wide manufacturing clearing.**

## 9.2 Timing

- **First deterioration:** mid-2011 / Q3;
- **Cross-confirmation:** 2011 Q3–Q4;
- **Accounting confirmation:** 2012 reporting cycle;
- **Stabilization:** late-2012 / early-2013 candidate;
- **Recovery confirmation:** 2014 at the solar-equipment-supplier layer; full industry normalization not claimed.

### 9.3 Implication

Forward Commitment includes expansion cancellation, idle lines, and capacity rationalization — not only company CapEx guidance.

Project-financing availability belongs inside Demand Quality / Financing because end demand can exist while financing blocks project conversion.

---

# 10. A–I Unified Timing Matrix v1.0

| Case | First deterioration | Cross-confirmation | Accounting confirmation | Trough / stabilization | Confidence |
|---|---|---|---|---|---|
| A · Internet/Telecom | 2000 Q4 | 2001 Mar–Apr | FY2001 Q3, annual confirmation later | 2002 H1–H2, boundary broad | High confirmation; Medium trough |
| B · Crypto/GPU | 2018 Q4 / Nov disclosure | 2019 Jan | FY2019 Q3–Q4 | 2019 H1 | Medium–High |
| C · GPU + Cloud Optimization | 2022 Aug 8 | 2022 Aug 8–24, segment breadth fails | 2022 Aug, near-synchronous | 2022 H2–2023 H1; AI side reversed earlier | High first signal; Medium trough |
| D · GFC / Enterprise IT | 2007 Q4–2008 H1 | 2008 Q4 | **No qualifying hard accounting signal** | 2009 H1 ex-post trough / H2 stabilization | High |
| E · Semiconductor | 2000 H2 | 2001 H1 | 2001 H2–2002 | 2003 recovery | High |
| F · Oil & Gas Upstream | 2014 H2 | 2015 H1–H2 | 2015–2016 | 2016 Q2–Q4 | High |
| G · Hyperscale Cloud Digestion | 2019 CapEx deceleration | **No systemic cross-confirmation** | None | N/A — negative control | High |
| H · Solar PV Manufacturing | mid-2011 / Q3 | 2011 Q3–Q4 | 2012 | late-2012/early-2013 stabilization candidate; 2014 equipment-layer recovery confirmed | High / Medium–High |
| I · Boeing 737 MAX / Commercial Aerospace | 2019 Mar–Apr | **No system-wide cross-confirmation** | Boeing-specific Q2-2019 accounting | N/A — negative control; pre-COVID system clearing never confirmed | High |

### 10.1 Lead / lag results

The most stable result is directional, not a precise number of months:

1. **Market Clearing / Utilization often lead or coincide with Accounting, but not always.**
2. **Forward Commitment often deteriorates before Accounting.**
3. **Financing timing depends on the shock-entry path.**
4. **Absence of hard Accounting does not veto a systemic clearing.**
5. **Failure to reach cross-confirmation is itself informative.**

### 10.2 What this sample cannot support

Nine observations are still too few; A/E are correlated and B/C both involve NVIDIA/GPU exposure. G/I are independent negative controls.

v1.0 therefore does **not**:
- estimate an average lead time and present it as a forecast horizon;
- report p-values/regressions;
- optimize signal weights;
- turn "Accounting often lags" into a fixed law;
- count A and E as two independent crises.

The current empirical interpretation is:

> **The five-signal framework is better treated as a cross-signal confirmation protocol than a fixed-threshold score. Market Clearing, Utilization, and Forward Commitment are often better leading observation layers; Accounting is common but non-mandatory confirmation; Financing can lead, amplify, or remain secondary depending on shock origin.**

---

# 11. v1.0 Backtest Conclusion

| Historical case | Accounting | Util./Revenue | Clearing | Forward | Demand Quality | Research classification |
|---|---:|---:|---:|---:|---:|---|
| Internet/Telecom | 2 | 2 | 2 | 2 | 2 | Broad clearing |
| Crypto/GPU | 2 | 2 | 2 | 2 | N/A | Strong partial / segment clearing |
| GPU + Cloud optimization | 2 | 1 | 2 | 1 | 0 | Partial / no system-wide S4 |
| GFC / Enterprise IT | 0 | 2 | 1 | 2 | 2 | Broad clearing |
| Semiconductor | 2 | 2 | 2 | 2 | N/A | Broad layer clearing* |
| Oil & Gas Upstream | 2 | 2 | 2 | 2 | 2 | Broad clearing |
| Hyperscale Cloud Digestion | 0 | 0 | 0 | 1 | 0 | No systemic clearing |
| Solar PV Manufacturing | 2 | 2 | 2 | 2 | 2 | Broad multi-segment clearing |
| Boeing 737 MAX / Commercial Aerospace | 2 | 2 | N/A / idiosyncratic | 2 | 0 | Severe company/program disruption; **No system-wide clearing** |

Current findings:

1. The framework has basic face validity across positive, partial, and negative-control cases.
2. Accounting is usually confirmation/severity evidence, not the earliest signal.
3. Segment Breadth is necessary to prevent local GPU/channel corrections from being promoted into system-wide S4.
4. Demand Quality / Financing observability varies by industry and therefore needs a proxy hierarchy.
5. Accounting cannot be a mandatory gate.
6. Correlated samples cannot be double-counted.
7. Oil & Gas provides preliminary cross-industry external validity.
8. Hyperscale cloud digestion provides an independent negative control against CapEx-decay overinterpretation.
9. Solar adds another independent manufacturing-capital-cycle positive case.
10. The sample is still not a statistically validated prediction system.
11. Boeing MAX provides a second independent negative control: severe focal-company disruption does not become system clearing without independent competitor/end-demand/industry breadth.

The correct status is:

> **Chapter 24's five-signal system has passed a first retrospective falsification check and exposed important constraints—Accounting is not a hard gate, breadth matters, and correlated samples must not be double-counted—but it is not a statistically validated or prospectively calibrated classifier.**

---

# 12. Prospective Adjudication Protocol v1.0

The central methodological problem is **look-ahead bias**.

A 2011 economic event that is only revealed in a 2012 filing cannot be treated as if it were known to an outside observer in 2011.

Every evidence item therefore needs two clocks:

```text
event_time
=
when the underlying economic event occurred

publication_time
=
when an external observer could first reasonably access the evidence
```

A prospective replay may use only:

> **publication_time ≤ adjudication_time**

Later filings or retrospective explanations may validate an earlier state ex post, but they cannot be injected backward into the earlier information set.

## 12.1 Prospective research states

These labels are research adjudication states, not new S1–S4 scenarios and not a calibrated classifier.

### NO CLEARING — current evidence does not support clearing

Use when:
- isolated deterioration is absent or contradicted;
- broad revenue/utilization/commitment evidence remains expansionary;
- a suspected signal is better explained by timing, mix shift, product transition, or idiosyncratic shock.

### WATCH — isolated deterioration without cross-confirmation

Examples:
- one guidance cut;
- one inventory event;
- one price collapse;
- one financing tightening;
- one impairment.

Do not promote a point shock into system clearing.

### CANDIDATE — cross-signal deterioration begins

Require at least:
- one real economic/capital signal from Utilization/Revenue, Market Clearing, or Forward Commitment;
- plus an independent signal family;
- without double-counting the same underlying event through multiple documents.

This is an evidence floor, not a calibrated threshold.

### CONFIRMED — multi-actor / multi-layer clearing

Require:
- breadth beyond one company/idiosyncratic event;
- persistence in at least one quantity/utilization/clearing/commitment signal;
- later Accounting, Financing, or second real-economy confirmation;
- insufficient contrary evidence to explain the whole pattern.

Accounting is not mandatory.

### STABILIZATION CANDIDATE — deterioration stops worsening

Real-time research is not allowed to announce "the trough is in."

Use this label when:
- inventory deterioration stops accelerating;
- utilization stops falling;
- cancellation/CapEx cuts stop worsening;
- financing terms stop deteriorating;
- clearing prices stop making new lows.

The label remains reversible.

### RECOVERY CONFIRMED — later evidence validates stabilization

Examples:
- utilization/revenue recovery;
- inventory normalization;
- forward commitments rebuild;
- financing/credit reopens;
- sustained pricing normalization.

No universal "two quarters" rule is imposed across industries.

## 12.2 Trough / stabilization anti-look-ahead rule

**Trough** is an ex-post local minimum and requires future data.

**Stabilization Candidate** is a prospective state: leading deterioration is no longer worsening.

The real-time question is not:

> "Do we know this is the absolute bottom?"

It is:

> **"Is there enough evidence to stop increasing clearing severity or to start testing a recovery hypothesis?"**

## 12.3 Source-time ledger

Each prospective evidence item should contain:

| Field | Required meaning |
|---|---|
| case_id | A–I / future case |
| signal_family | Accounting / Utilization-Revenue / Market Clearing / Forward Commitment / Demand Quality-Financing |
| event_time | underlying economic period |
| publication_time | first externally observable date |
| source_identity | filing / IR / regulator / market data / institutional source |
| actor / layer | company / industry / bank / capital market / supply layer |
| observation | what was actually observed |
| contrary_signal | same-period evidence against clearing |
| status_at_time | NO CLEARING / WATCH / CANDIDATE / CONFIRMED / STABILIZATION CANDIDATE / RECOVERY CONFIRMED |
| revision_reason | why the state changed later |

Hard rule:

> **One underlying event cannot create multiple independent confirmations merely because it appears in multiple documents.**

## 12.4 Breadth protocol

Strong breadth can come from:
- multiple firms;
- multiple customer groups;
- multiple financing channels;
- multiple supply-chain layers;
- utilization + project/capacity decisions;
- market clearing + lender behavior.

Weak breadth:

```text
one company revenue ↓
+
same company gross margin ↓
+
same company inventory charge
```

That can be severe company distress without system clearing.

## 12.5 Accounting rule

Accounting is explicitly:

> **confirmation / severity evidence, not a mandatory gate**

Observed timing patterns:

1. lagging Accounting — semiconductor, solar, oil;
2. near-synchronous Accounting — inventory-led GPU/channel correction;
3. no qualifying hard Accounting — financing-led broad contraction such as GFC enterprise IT.

## 12.6 Financing rule

Financing timing depends on shock entry:

- **GFC:** financing can lead;
- **Oil & Gas:** financing can amplify after price/commitment deterioration;
- **Semiconductor / GPU inventory:** financing may be secondary or unobservable.

Therefore:
- absence of financing stress cannot veto real clearing;
- higher rates/spreads without project/demand transmission remain macro context rather than clearing confirmation.

## 12.7 Prospective replay procedure

For each historical case:

1. choose adjudication dates at the information frequency actually available;
2. hide every source published after that date;
3. assign a research state;
4. record contrary evidence;
5. advance one information period;
6. update only when new independent evidence arrives;
7. compare the first prospective state change with the ex-post timing matrix.

Do not optimize the protocol separately by case.

## 12.8 Descriptive prospective metrics

With the current small sample, do not report p-values, ROC curves, or optimized weights.

Allowed process metrics:

### Adjudication latency

```text
Latency
=
first CONFIRMED publication_time
-
first credible deterioration publication_time
```

Use ranges for quarterly/semiannual evidence.

### Candidate resolution

Track:

```text
CANDIDATE
→ CONFIRMED
or
→ RETRACTED / SEGMENT-ONLY
```

### Evidence breadth

Record independent actors, independent signal families, and economic layers without collapsing them into a fitted score.

### Revision count

Frequent state reversals can indicate noisy signals or insufficient breadth.

## 12.9 Prospective output table

| adjudication date | known evidence | contrary evidence | breadth | research state | why state changed | evidence unavailable at that time |
|---|---|---|---|---|---|---|

The final column makes look-ahead contamination visible.

## 12.10 Interpretation change

The five signals should no longer be read as five equally weighted boxes.

The better interpretation is:

> **a cross-signal confirmation protocol with publication-time discipline, breadth requirements, contrary evidence, and reversible adjudication states**

---

## 12A. Prospective Replay 1 — Case B: Crypto/GPU

Key publication-time sequence:

| Adjudication time | Evidence available then | Contrary evidence | Breadth | State |
|---|---|---|---|---|
| 2018-08-16 | NVIDIA reports record revenue across major platforms | all major platforms still strong | no clearing breadth | **NO CLEARING** |
| 2018-11-15 | excess post-crypto channel inventory publicly identified | annual/platform growth still strong | company/segment | **WATCH** |
| 2019-01-28 | guidance cut US$2.70B → US$2.20B; production ramps delayed; channel clearing persists; Gaming/Data Center weakness broadens | full-year platform strength still matters | multiple signal families, still company-level | **CANDIDATE — segment/company clearing** |
| 2019 Feb | Q4 results confirm severe Gaming/channel weakness and charges | no evidence of whole accelerated-compute system collapse | company/segment | **CONFIRMED — segment/company clearing; NOT system clearing** |
| 2019 May–Aug | sequential growth/stabilization resumes | — | company-level recovery | **RECOVERY CONFIRMED — segment/company scope** |

Prospective replay materially corrects the earlier temptation to date clearing to "2018 H2" broadly.

The August-2018 state was **NO CLEARING**.

The first defensible CANDIDATE state is closer to Jan-2019, and even then the classification remains segment/company rather than system-wide.

---

## 12B. Prospective Replay 2 — Case G: Hyperscale Cloud Digestion Negative Control

| Adjudication time | Evidence available then | Contrary evidence | Breadth | State |
|---|---|---|---|---|
| 2019 Apr | Alphabet Q1 CapEx ~US$4.64B vs ~US$7.30B prior year | Alphabet revenue +17%, OCF ~US$12.0B; AWS Q1 sales +41%; Facebook still guides US$17–19B 2019 CapEx | one company | **WATCH → NO CLEARING** |
| 2019 Jul | Alphabet Q2 CapEx ~US$6.13B vs ~US$5.48B prior year; H1 still below prior-year H1 | AWS Q2 sales +37%; Google Cloud hiring; Facebook infrastructure investment continues | breadth argues against clearing | **NO CLEARING** |
| 2020 Feb | Alphabet 2019 CapEx ~US$23.5B vs ~US$25.1B | AWS revenue +37%, PP&E additions rise; Facebook CapEx rises and guides higher 2020 spend | multi-company counterevidence | **NEGATIVE CONTROL CONFIRMED** |

Lesson:

> **the protocol must be able to de-escalate a WATCH state when independent evidence contradicts the clearing hypothesis.**

---

## 12C. Prospective Replay 3 — Case D: GFC / Enterprise IT

| Adjudication time | Evidence available then | Contrary evidence | Breadth | State |
|---|---|---|---|---|
| 2008-07 | business fixed investment slows; sales/profits/credit deteriorate; firms postpone/abandon expansion; E&S indicators turn down; banks tighten C&I | profits not yet at historical trough; some financing markets improve temporarily | macro + financing + forward commitment | **CANDIDATE — broad macro/business** |
| 2009-02 | E&S ~-7.5% Q3 / **-28% Q4 annualized**; H2 IT ~-12.5%; sales/production/profits down; credit reduced/more expensive | no telecom-style enterprise-IT seller write-down | financing + utilization/investment + forward commitment | **CONFIRMED — broad systemic clearing** |
| 2009-07 | Q1 E&S ~**-34% annualized**; credit still tight; declines "may be abating" | rate of deterioration slows | broad macro | **STABILIZATION CANDIDATE** |
| 2010-02 | E&S expands in 2009H2; IT capital accelerates; some financing improves | structures/labor remain weak | business-investment/finance reversal | **RECOVERY CONFIRMED — E&S / IT scope** |

Core falsification:

> **A giant seller impairment is not required to confirm broad clearing when financing, investment, and utilization evidence already cross-confirm.**

---

## 12D. Prospective Replay 4 — Solar PV Manufacturing Overcapacity

| Adjudication time | Evidence available then | Contrary evidence | Breadth | State |
|---|---|---|---|---|
| 2011 Q3 filing window | worldwide panel overcapacity/inventory; project financing very challenging; panel prices falling for several quarters; customers defer investment | 2011H1 remained strong; one main source does not establish independent breadth | clearing + financing + forward commitment | **CANDIDATE — mechanism visible, breadth incomplete** |
| 2012 H1 | Applied Materials describes excess manufacturing capacity and deferred capacity purchases; restructuring begins; First Solar adjusts footprint/capacity | some hard accounting impairment not yet fully synchronized | multiple firms + capacity deferral/restructuring | **CONFIRMED — multi-actor manufacturing clearing** |
| 2012 H2 | First Solar cancels Vietnam plant with ~US$99M impairment; Applied orders/sales collapse plus impairment/restructuring; Suntech utilization ~60% and capacity cut | end demand not zero; technology/company dispersion remains | accounting + utilization + forward + clearing | **CONFIRMED — severity broadens** |
| late-2012 / early-2013 | new orders rebound from extremely low levels but excess capacity remains | weak sales, impairment, overcapacity persist | deterioration slows | **STABILIZATION CANDIDATE** |

### 12D.1 Recovery must close at the same economic layer

End-market solar deployment growth alone is not sufficient to declare manufacturing-equipment recovery.

Contemporaneous recovery replay:

| Adjudication time | Evidence | Contrary evidence | Layer | State |
|---|---|---|---|---|
| 2013-12-04 · Applied Materials FY2013 | end demand robust; EES book-to-bill improves toward ~1.0 | capital-equipment investment still depressed; global production capacity exceeds demand; orders -15%, sales -59%, large operating loss | end demand improving, equipment still weak | **STABILIZATION CANDIDATE** |
| 2014-02-12 · Q1 FY2014 | operating loss narrows | excess capacity, tight capital, weak orders/sales persist | equipment layer | **STABILIZATION CANDIDATE** |
| 2014 Q3 filing | equipment environment improves slightly; end demand grows | capital investment remains low; excess capacity persists | demand recovery stronger than equipment recovery | **STABILIZATION CANDIDATE — recovery hypothesis strengthened** |
| FY2014 results | EES orders ~US$238M vs US$166M (+43%); sales ~US$279M vs US$173M (+61%); operating income ~US$15M vs -US$433M | excess capacity still exists; not full industry normalization | equipment orders + sales + operating result improve together | **RECOVERY CONFIRMED — supplier layer only** |

Rule:

> **Do not use a later industry-recovery narrative to backdate recovery, just as later crash evidence cannot be used to backdate clearing.**

---

## 12E. Four-Path Prospective Validation Result

The B / D / G / H subset covers four different shock-entry paths:

- inventory/channel;
- financing-led macro contraction;
- negative-control CapEx digestion;
- long-duration manufacturing overcapacity.

What survives:

1. publication-time discipline materially changes some dates;
2. breadth prevents false system-wide promotion;
3. Accounting can lag, coincide, or remain absent;
4. candidate states can de-escalate;
5. stabilization must remain distinct from ex-post trough.

What is not proven:

- statistical false-positive rate;
- optimized weights;
- universal lead time;
- calibrated state-transition probability.

---

## 12F. Prospective Replay 5 — Case I: 2019 Boeing 737 MAX / Commercial Aerospace Negative Control

This is a stronger negative control than a simple company-specific CapEx miss because Boeing experienced severe clearing-like signals while the underlying industry demand remained robust.

Shock origin:

> **certification / regulatory / operational disruption**

not:

> **system-wide end-demand / financing / overcapacity clearing**

| Adjudication time | Evidence available then | Contrary evidence | Breadth | State |
|---|---|---|---|---|
| 2019-04-05 / 04-24 | Boeing cuts 737 monthly production 52 → 42; Q1 revenue ~US$22.9B; backlog >5,600; guidance suspended | 737 employment maintained; no passenger-demand collapse | single company/program | **WATCH — Boeing/MAX-specific** |
| 2019-07-18 / 07-24 | ~US$5.61B customer-concession charge; ~US$1.7B higher 737 production cost; Commercial Airplanes margin deeply negative | Airbus H1 calls environment robust, deliveries 389 vs 303, revenue +24%, guidance maintained; passenger traffic still grows | strong focal-company distress, independent competitor/end-demand counterevidence | **CONFIRMED — Boeing/MAX disruption; NO SYSTEM CLEARING** |
| late 2019 | grounding continues; inventory/delivery/cash-flow pressure persists | Airbus ramp/backlog strong; passenger demand slows but remains positive | supplier-specific distress | **NO SYSTEM CLEARING** |
| 2020-01, before COVID dominates | Boeing 2019 Commercial Airplanes deliveries 380 vs 806; revenue US$32.3B vs US$57.5B; operating loss ~US$6.66B; company OCF ~-US$2.45B | Airbus 863 deliveries (+8%), 1,131 gross / 768 net orders, backlog 7,482; IATA 2019 RPK +4.2%, load factor record 82.6% | cross-company/end-demand evidence directly rejects system clearing | **NEGATIVE CONTROL CONFIRMED** |

### 12F.1 Regulatory / operational shock rule

A focal company can show:

- production cuts;
- delivery collapse;
- large accounting charges;
- cash-flow deterioration;

without system-wide capital clearing.

The protocol must ask:

1. Did the shock originate in end demand / capital-cycle economics?
2. Did independent competitors deteriorate?
3. Did customer/end-user demand deteriorate?
4. Did backlog/production breadth turn down across the industry?
5. Did financing stress propagate?

If not, the correct state can be severe company/program disruption while the system remains outside clearing.

### 12F.2 COVID boundary

The Case I observation window ends with 2019 data / early-2020 publication, before the later COVID shock becomes dominant.

The 2020 global aviation demand shock is a different event and cannot be injected backward to prove that the 2019 MAX grounding was already system-wide clearing.

---

## 12G. Negative-Control Pair Result v1.0

The framework now has two mechanism-independent negative controls:

1. **Case G — hyperscale cloud digestion:** apparent forward-commitment weakness without broad deterioration;
2. **Case I — Boeing/MAX:** severe dominant-supplier operational/accounting distress without broad end-demand/competitor/financing deterioration.

Together they harden the specificity rule:

> **A large focal-company signal is not enough. System clearing requires causal breadth across independent actors and economic layers.**

At v1.0 the framework has evolved from a historical scorecard into:

> **a publication-time, contrary-evidence, breadth-aware adjudication protocol**

It is still not a statistical classifier.

The next priority is therefore no longer mechanical case accumulation.

It is:
1. maintain a repeatable adjudication ledger;
2. log future AI-infrastructure evidence prospectively;
3. add historical cases only when they expose a genuinely new mechanism gap.

---


# 13. Sources

## 2000–2002 Internet / Telecom

- Cisco Systems, FY2001 Annual Report — inventory provision US$2.77B; restructuring / impairment / excess-facility charges; inventory turns and demand decline:  
  https://www.cisco.com/c/dam/en_us/about/ac49/ac20/downloads/annualreport/ar2001/pdf/AR.pdf
- Cisco Systems, 2001-04-16 Business and Financial Update — expected fiscal Q3 revenue approximately 30% below Q2 amid sudden demand decline:  
  https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2001/m04/cisco-systems-offers-business-and-financial-update.html
- Cisco Systems, 2001-03-09 cost-cutting announcement — capital-spending slowdown expected to extend beyond two quarters:  
  https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2001/m03/cisco-systems-inc-announces-cost-cutting-measures.html
- Federal Reserve, Monetary Policy Report / 2001–early 2002 — communications-equipment spending fell more than 30% in 2001; capital overhang and excess capacity:  
  https://www.federalreserve.gov/boarddocs/hh/2002/february/reportsection2.htm
- Federal Reserve Beige Book, 2001-03-07 — high telecommunications-equipment inventories and firms trimming capital spending:  
  https://www.federalreserve.gov/fomc/beigebook/2001/20010307/default.htm
- Nortel Networks / SEC filing — constrained capital markets, high debt, bankruptcies, excess network capacity and lower carrier CapEx:  
  https://www.sec.gov/Archives/edgar/data/1119664/000113031902000166/t06647e10-k405.htm

## 2018–2019 Crypto / GPU

- NVIDIA FY2019 Form 10-K — crypto after-effects, channel inventory, Q3/Q4 component charges and crypto-specific revenue expected to become negligible:  
  https://www.sec.gov/Archives/edgar/data/1045810/000104581019000023/nvda-2019x10k.htm
- NVIDIA, 2018 Q3 FY2019 Form 10-Q — US$57M charge after sharp fall-off in cryptocurrency mining demand:  
  https://www.sec.gov/Archives/edgar/data/1045810/000104581018000150/nvda2019q310q.htm
- NVIDIA, 2019-01-28 guidance update — Q4 revenue guidance cut from US$2.70B to US$2.20B; excess post-crypto channel inventory:  
  https://nvidianews.nvidia.com/news/nvidia-updates-financial-guidance-for-fourth-quarter-of-fiscal-year-2019
- NVIDIA FY2019 Q4 results — Q4 revenue -31% q/q; Gaming -46% q/q; post-crypto excess inventory:  
  https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2019

## 2022–2023 GPU / Cloud Optimization

- NVIDIA FY2023 Form 10-K — US$2.17B inventory provisions; Gaming -27% y/y; Data Center +41% y/y; channel undershipping:  
  https://www.sec.gov/Archives/edgar/data/1045810/000104581023000017/nvda-20230129.htm
- NVIDIA Q2 FY2023 Form 10-Q — Gaming -44% q/q; US$1.22B inventory-related charge; pricing programs and channel adjustment:  
  https://www.sec.gov/Archives/edgar/data/1045810/000104581022000147/nvda-20220731.htm
- Meta FY2022 Q4 results — 2023 CapEx guidance lowered to US$30–33B from US$34–37B due to lower data-center construction spend:  
  https://investor.atmeta.com/investor-news/press-release-details/2023/Meta-Reports-Fourth-Quarter-and-Full-Year-2022-Results/default.aspx
- Meta 2023 Q2 results — CapEx lowered again to US$27–30B, but reduction attributed to non-AI server savings and project/equipment timing; AI investment remained a priority:  
  https://investor.atmeta.com/investor-news/press-release-details/2023/Meta-Reports-Second-Quarter-2023-Results/default.aspx
- Meta 2023 Q3 results — preliminary 2024 CapEx US$30–35B, with growth driven by AI/non-AI servers and data-center construction:  
  https://investor.atmeta.com/investor-news/press-release-details/2023/Meta-Reports-Third-Quarter-2023-Results/default.aspx

## 2008–2009 Global Financial Crisis / Enterprise IT

- Federal Reserve, Monetary Policy Report, 2009-02-24 — Q4 2008 equipment/software investment collapse; reduced credit availability and higher cost of credit; IT investment contraction:  
  https://www.federalreserve.gov/monetarypolicy/mpr_20090224_part2.htm
- Federal Reserve, Monetary Policy Report, 2009-07-21 — 2009 Q1 equipment/software investment about -34% annualized; high-tech capital spending more than -20% annualized; credit availability remained tight:  
  https://www.federalreserve.gov/monetarypolicy/mpr_20090721_part2.htm
- Federal Reserve, accessible Figure 13/14 — high-tech investment and business-inventory liquidation series for 2008–2009:  
  https://www.federalreserve.gov/monetarypolicy/mpr_20090721_part2_accessible.htm
- Cisco Systems FY2009 Annual Report — FY2009 revenue -9%, product revenue approximately -12% amid reduced enterprise/service-provider spending; inventory and purchase-commitment provisions:  
  https://www.cisco.com/assets/cdc_content_elements/docs/annualreports/media/2009-ar.pdf


## 2001–2003 Semiconductor Downcycle

- Federal Reserve G.17, 2001-05-14 — high-technology capacity utilization fell for the ninth consecutive month; semiconductor/computer capacity growth estimates revised downward:  
  https://www.federalreserve.gov/releases/g17/20010514/
- Federal Reserve / FRED, semiconductor and electronic-component capacity-utilization series — utilization fell from roughly 93% in mid-2000 to roughly 60% by late 2001, then recovered through 2003:  
  https://fred.stlouisfed.org/data/CAPUTLG3344S
- Micron Technology FY2002 Form 10-K — semiconductor-memory ASP declined approximately 60% in 2001 and 53% in 2002; inventory write-downs approximately US$727M in 2001 and US$376M in 2002:  
  https://www.sec.gov/Archives/edgar/data/723125/000091205702038669/a2091284z10-k.htm
- Intel 2001 Annual Report — flash-memory results hurt by lower volume, decreased factory capacity utilization and higher inventory write-downs:  
  https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-05/history-2001-annual-report.pdf
- STMicroelectronics 2001 Form 20-F — 2001 semiconductor TAM down approximately 32%; customer inventory reductions drove lower utilization and fab closures/selective shutdowns:  
  https://www.sec.gov/Archives/edgar/data/932787/000102140802007666/d20f.htm


## 2014–2016 Oil & Gas Upstream

- Halliburton FY2015 Form 10-K — U.S. land rig count down approximately 64% from Nov. 2014 peak through Dec. 2015, 2015 revenue -28%, widespread pricing pressure, and approximately US$2.2B impairments / other charges:  
  https://www.sec.gov/Archives/edgar/data/45012/000004501216000272/hal_12312015-10k.htm
- Halliburton FY2016 Form 10-K — 2016 described as the sharpest/deepest industry decline; average U.S. rig count nearly 75% below Nov. 2014 peak, with recovery signals later in 2016:  
  https://www.sec.gov/Archives/edgar/data/45012/000004501217000047/hal_12312016-10k.htm
- Apache FY2016 Form 10-K — 2014–2016 impairment table, including approximately US$9.47B total impairments in 2015:  
  https://www.sec.gov/Archives/edgar/data/6769/000167337917000004/apa10-k2016.htm
- U.S. EIA, 2016-03-04 — U.S. mining/exploration investment declined about 35% in 2015 and companies planned further CapEx reductions:  
  https://www.eia.gov/todayinenergy/detail.php?id=24912
- U.S. EIA, 2015-09-18 — low oil prices reduced operating cash flow; producers cut CapEx, raised debt/equity, and debt service consumed a larger share of cash flow:  
  https://www.eia.gov/todayinenergy/detail.php?id=22992
- Federal Reserve SLOOS, April 2015 — banks expected oil/gas loan quality to deteriorate and reported tighter underwriting, reduced credit lines and additional collateral requirements:  
  https://www.federalreserve.gov/boarddocs/snloansurvey/201505/default.htm
- Federal Reserve / FDIC / OCC Shared National Credits review, 2015-11-05 — sharp increase in classified oil/gas commitments following the commodity-price collapse:  
  https://www.federalreserve.gov/newsevents/pressreleases/bcreg20151105a.htm
- ConocoPhillips 2016 proxy / 2015 review — 2015 capital expenditures reduced 41% vs. 2014:  
  https://www.sec.gov/Archives/edgar/data/1163165/000104746916011624/a2227560zdef14a.htm


## 2018–2019 Hyperscale Cloud CapEx Digestion

- Alphabet FY2019 Form 10-K — total CapEx approximately US$25.1B in 2018 and US$23.5B in 2019; Google Cloud revenue US$5.84B in 2018 and US$8.92B in 2019:  
  https://www.sec.gov/Archives/edgar/data/1652044/000165204420000008/goog10-k2019.htm
- Amazon FY2019 Form 10-K — AWS sales +37% in 2019; AWS net additions to property and equipment increased from approximately US$9.8B to US$13.1B:  
  https://www.sec.gov/Archives/edgar/data/1018724/000101872420000004/amzn-20191231x10k.htm
- Facebook FY2019 Form 10-K — 2019 CapEx approximately US$15.1B versus US$13.9B in 2018; 2020 CapEx expected at US$17–19B:  
  https://www.sec.gov/Archives/edgar/data/1326801/000132680120000013/fb-12312019x10k.htm


## 2011–2013 Solar PV Manufacturing

- First Solar FY2012 Form 10-K — 2012 manufacturing restructuring, approximately US$127M charges, cancellation of Vietnam 4-line plant, idle/closed manufacturing capacity:  
  https://www.sec.gov/Archives/edgar/data/1274494/000127449413000006/fslrdec1210k.htm
- Suntech 2012 investor materials — industry cell capacity utilization around 60% and capacity rationalization / reduction:  
  https://www.sec.gov/Archives/edgar/data/1342803/000110465912077662/a12-26837_1ex99d1.htm
- Applied Materials FY2012 Form 10-K — solar excess manufacturing capacity, sharp equipment-demand decline, impairment / inventory / restructuring charges:  
  https://www.sec.gov/Archives/edgar/data/6951/000000695112000018/amat10282012-10kdoc.htm
- Solar-industry SEC filing — excess module capacity, polysilicon price down to approximately US$18/kg in 2012, below production cost in some markets:  
  https://www.sec.gov/Archives/edgar/data/1594124/000104746914009214/a2222165z424b4.htm
- JA Solar / industry filing — module ASP fell sharply into 2012; inventory write-downs followed market-price decline below carrying cost:  
  https://www.sec.gov/Archives/edgar/data/1375877/000104746914000764/a2218242z424b5.htm
- Solar financing disclosure — credit-market contraction and higher financing costs caused project cancellations, postponements, and scale-backs:  
  https://www.sec.gov/Archives/edgar/data/1481513/000119312510120053/d424b4.htm


## Timing-tightening sources added in v0.7

- Cisco FY2001 Annual Report — fiscal Q3 excess inventory charge US$2.25B; FY2001 inventory / purchase-commitment provision US$2.77B: https://www.cisco.com/c/dam/en_us/about/ac49/ac20/downloads/annualreport/ar2001/pdf/AR.pdf
- NVIDIA 2018 Q2 FY2019 results — record platform revenues in August 2018, used as contrary evidence against backdating the crypto clearing: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2019
- NVIDIA 2018 Q3 FY2019 results — excess channel inventory post crypto boom publicly identified: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2019
- NVIDIA 2019-01-28 shareholder letter / guidance update — production-ramp delay and 1–2 quarter channel-inventory depletion expectation: https://www.sec.gov/Archives/edgar/data/1045810/000104581019000004/shareholderletter.htm
- NVIDIA 2022-08-08 preliminary Q2 FY2023 results — Gaming -44% q/q, channel pricing programs and ~US$1.32B inventory-related charges disclosed together: https://nvidianews.nvidia.com/news/nvidia-announces-preliminary-financial-resultsfor-second-quarter-fiscal-2023
- NVIDIA 2022-08-24 Q2 FY2023 results — ongoing OEM/channel inventory reduction into Q3 with Data Center growth counterevidence: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2023
- 2011 solar-equipment filing — mid-year deterioration, Q3–Q4 order slowdown after Q2 peak: https://www.sec.gov/Archives/edgar/data/103145/000104746913010200/a2217194z10-k.htm
- 2011 solar-industry filing — worldwide panel overcapacity/inventory, difficult project financing, multi-quarter panel-price decline by Q3 2011: https://www.sec.gov/Archives/edgar/data/927003/000095012311096521/c23205e10vq.htm


## Prospective-replay sources added in v0.8

- NVIDIA FY2019 Q2 results, 2018-08-16 — record revenue across Datacenter, Gaming, Professional Visualization and Automotive: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2019
- NVIDIA FY2019 Q3 results, 2018-11-15 — excess channel inventory post crypto boom disclosed: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2019-6747552
- NVIDIA guidance update, 2019-01-28 — Q4 guidance US$2.70B → US$2.20B; production ramps delayed to deplete excess channel inventory: https://www.sec.gov/Archives/edgar/data/1045810/000104581019000004/shareholderletter.htm
- NVIDIA FY2020 Q1 results — May 16, 2019, sequential stabilization / gaming growth resumed: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2020
- NVIDIA FY2020 Q2 results — Aug 15, 2019, sequential growth across platforms: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2020
- Alphabet 2019 Q1 Form 10-Q — Q1 CapEx US$4.638B vs US$7.299B prior year; revenue +17%; OCF US$12.0B; liquidity statement: https://www.sec.gov/Archives/edgar/data/1652044/000165204419000015/goog10-qq12019.htm
- Alphabet 2019 Q2 Form 10-Q — Q2 CapEx US$6.126B vs US$5.477B prior year; H1 CapEx US$10.764B vs US$12.776B: https://www.sec.gov/Archives/edgar/data/1652044/000165204419000023/goog10-qq22019.htm
- Amazon 2019 Q1 Form 10-Q — AWS sales +41% YoY: https://www.sec.gov/Archives/edgar/data/1018724/000101872419000043/amzn-2019331x10q.htm
- Amazon 2019 Q2 Form 10-Q — AWS sales +37% YoY: https://www.sec.gov/Archives/edgar/data/1018724/000101872419000071/amzn-2019630x10q.htm
- Amazon 2019 Form 10-K — AWS revenue US$35.026B vs US$25.655B; AWS PP&E additions US$13.058B vs US$9.783B: https://www.sec.gov/Archives/edgar/data/1018724/000101872420000004/amzn-20191231x10k.htm
- Facebook 2019 Q1 Form 10-Q — continued infrastructure investment; 2019 CapEx outlook US$17–19B: https://www.sec.gov/Archives/edgar/data/1326801/000132680119000037/fb-03312019x10q.htm
- Facebook 2019 Form 10-K — 2019 PP&E purchases US$15.10B vs US$13.92B in 2018; 2020 CapEx outlook US$17–19B: https://www.sec.gov/Archives/edgar/data/1326801/000132680120000013/fb-12312019x10k.htm


## Prospective D/H source register added in v0.8

- Federal Reserve, July 15, 2008 Monetary Policy Report — business fixed-investment slowdown, tightened credit, postponed/abandoned expansion plans: https://www.federalreserve.gov/monetarypolicy/mpr_20080715_part2.htm
- Federal Reserve, Feb 24, 2009 Monetary Policy Report — E&S -7.5% Q3 / -28% Q4 annualized; H2 IT investment -12.5%; reduced / higher-cost credit: https://www.federalreserve.gov/monetarypolicy/mpr_20090224_part2.htm
- Federal Reserve, July 21, 2009 Monetary Policy Report — Q1 E&S -34%, credit still tight, declines may be abating: https://www.federalreserve.gov/monetarypolicy/mpr_20090721_part2.htm
- Federal Reserve, Feb 24, 2010 Monetary Policy Report — E&S began expanding in H2 2009; IT capital accelerated: https://www.federalreserve.gov/monetarypolicy/mpr_20100224_part2.htm
- Advanced Energy Industries Q3 2011 Form 10-Q — worldwide panel overcapacity/inventory, difficult project financing, multi-quarter panel-price decline and customer investment pause: https://www.sec.gov/Archives/edgar/data/927003/000095012311096521/c23205e10vq.htm
- Applied Materials Q2 FY2012 Form 10-Q — first-half solar excess manufacturing capacity, deferred capacity purchases, May-2012 restructuring: https://www.sec.gov/Archives/edgar/data/6951/000144530512001872/amat-042912x10qxdoc.htm
- First Solar 2012 filing — Feb-2012 capacity restructuring; Vietnam 4-line plant cancellation / impairment: https://www.sec.gov/Archives/edgar/data/1274494/000127449412000048/fslrsep1210qdraft.htm
- Applied Materials FY2012 Form 10-K — solar excess capacity, lower orders/sales, US$421M goodwill impairment, inventory/restructuring charges: https://www.sec.gov/Archives/edgar/data/6951/000000695112000018/amat10282012-10kdoc.htm
- Suntech 2012 investor filing — cell utilization ~60% and annualized cell capacity reduced to ~1.8GW: https://www.sec.gov/Archives/edgar/data/1342803/000110465912077662/a12-26837_1ex99d1.htm


## Solar recovery source register added in v0.9

- Applied Materials FY2013 Form 10-K — robust PV end-demand but depressed capital-equipment investment; EES orders / sales / operating-loss state: https://www.sec.gov/Archives/edgar/data/6951/000000695113000044/amat10272013-10kdoc.htm
- Applied Materials Q1 FY2014 Form 10-Q — continued excess manufacturing capacity, tightened capital access, deferred equipment purchases; EES orders / sales / loss: https://www.sec.gov/Archives/edgar/data/6951/000000695114000007/amat-form10xqq12014.htm
- Applied Materials Q3 FY2014 Form 10-Q — solar equipment environment improved slightly while capital-equipment investment remained low: https://www.sec.gov/Archives/edgar/data/6951/000000695114000028/amat-form10xqq32014.htm
- Applied Materials FY2014 Form 10-K — EES orders US$238M vs US$166M; sales US$279M vs US$173M; operating income US$15M vs loss US$433M; overcapacity still present: https://www.sec.gov/Archives/edgar/data/6951/000000695114000037/amat10262014-10kdoc.htm
- IEA PVPS, *A Snapshot of Global PV 1992–2013* — contemporaneous end-market deployment context; used only as demand-layer evidence, not as manufacturing-recovery proof: https://iea-pvps.org/wp-content/uploads/2020/01/PVPS_report_-_A_Snapshot_of_Global_PV_-_1992-2013_-_final_3.pdf


## Independent negative-control sources added in v1.0

- Boeing, 2019-04-05 — 737 monthly production rate temporarily reduced from 52 to 42 following MAX delivery pause: https://boeing.mediaroom.com/2019-04-05-Statement-from-Boeing-CEO-Dennis-Muilenburg-We-Own-Safety-737-MAX-Software-Production-and-Process-Update
- Boeing Q1 2019 results, 2019-04-24 — revenue, operating cash flow, commercial backlog >5,600 aircraft and withdrawal of guidance pending MAX impact assessment: https://investors.boeing.com/investors/news/press-release-details/2019/Boeing-Reports-First-Quarter-Results/default.aspx
- Boeing, 2019-07-18 — approximately US$5.61B net customer-concession charge and US$1.7B increase in estimated 737 production costs: https://investors.boeing.com/investors/news/press-release-details/2019/Boeing-to-Recognize-Charge-and-Increased-Costs-in-Second-Quarter-Due-to-737-MAX-Grounding/default.aspx
- Boeing Q2 2019 results — severe Commercial Airplanes margin impact / lower deliveries, while backlog remained >5,500 aircraft: https://investors.boeing.com/investors/news/press-release-details/2019/Boeing-Reports-Second-Quarter-Results/default.aspx
- Airbus H1 2019 results — robust commercial environment, 389 deliveries vs 303, consolidated revenue +24%, guidance maintained and backlog 7,276 aircraft: https://www.airbus.com/en/newsroom/press-releases/2019-07-airbus-reports-half-year-h1-2019-results
- Airbus 2019 commercial performance — 863 deliveries (+8%), 1,131 gross / 768 net orders, backlog 7,482 aircraft: https://www.airbus.com/en/newsroom/press-releases/2020-01-airbus-delivers-strong-2019-commercial-aircraft-performance
- IATA Air Passenger Market Analysis, June 2019 — passenger demand remained positive across major markets during the MAX grounding: https://www.iata.org/contentassets/08ea7f485007409d998575257c822ee9/passenger-analysis-jun-2019.pdf
- IATA Air Passenger Market Analysis, December 2019 — 2019 global RPK +4.2%, capacity +3.4%, load factor record 82.6%: https://www.iata.org/en/iata-repository/publications/economic-reports/air-passenger-monthly---dec-2019/
- Boeing FY2019 results, 2020-01-29 — Commercial Airplanes deliveries 380 vs 806, revenue US$32.255B vs US$57.499B, operating loss US$6.657B, commercial backlog >5,400 aircraft: https://investors.boeing.com/investors/news/press-release-details/2020/Boeing-Reports-Fourth-Quarter-Results/default.aspx
