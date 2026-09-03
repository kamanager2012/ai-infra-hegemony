# P0-1A · Prospective Adjudication Ledger v0.3

> **Status:** Research-side live logging layer; not part of the frozen 32-chapter formal report.  
> **Purpose:** operationalize P0-1 v1.0 as a publication-time disciplined, causality-aware, reversible adjudication process.

## 1. Why this ledger exists

P0-1 v1.0 no longer treats the five signals as a fixed weighted score.

The live research object is:

> **publication-time disciplined cross-signal confirmation with causal breadth, contrary evidence and reversible state transitions.**

The ledger therefore records what was knowable **at the adjudication time**, not what later turned out to be true.

Historical backtests remain in `01-clearing-signals-backtest.md`.

This file is for:
- current / future observations;
- state changes;
- contrary evidence;
- source-time discipline;
- revision history.

---

## 2. Required evidence-row schema

Each evidence row must resolve to these fields:

| Field | Meaning |
|---|---|
| `ledger_id` | unique evidence-row identifier |
| `adjudication_time` | time the research state is being decided |
| `event_time` | underlying economic period |
| `publication_time` | first public availability of the evidence |
| `signal_family` | Accounting / Utilization-Revenue / Market Clearing / Forward Commitment / Demand Quality-Financing |
| `causal_class` | demand destruction / supply interruption / financing shock / overcapacity / inventory / regulatory-operational / other |
| `actor` | company / lender / customer / regulator / industry |
| `layer` | model / compute / system / data center / power / financing / end demand |
| `scope` | company / segment / multi-company / system |
| `evidence_origin_id` | identity used to prevent duplicate counting of the same underlying event |
| `observation` | what was actually observed |
| `contrary_signal` | same-period evidence against escalation |
| `independence_key` | actor + economic layer + evidence origin |
| `state_before` | prior adjudication state |
| `state_after` | revised adjudication state |
| `revision_reason` | why the state changed or stayed unchanged |
| `source_identity` | first-party / regulator / institutional source |
| `unavailable_at_time` | later evidence explicitly excluded from current judgment |

Hard rules:

1. one economic event cannot be multiplied by repeating it across several filings / articles;
2. accounting severity cannot substitute for causal breadth;
3. a regulatory / operational shutdown must be separated from demand destruction;
4. seller support / guarantee caps are not independent end demand;
5. company-level negative cash headroom is not system clearing by itself;
6. future recovery / collapse evidence cannot be backfilled into earlier states.

---

## 3. State vocabulary

### NO CLEARING
Current evidence does not support capital clearing at the adjudicated scope.

### WATCH
A credible deterioration or vulnerability is visible, but breadth / persistence / causal transmission is insufficient.

### CANDIDATE
Multiple independent signal families begin to align.

### CONFIRMED
Cross-actor / cross-layer clearing is supported and major contrary explanations no longer explain the evidence.

### STABILIZATION CANDIDATE
Deterioration has stopped worsening, but a trough cannot yet be declared.

### RECOVERY CONFIRMED
Later independent evidence confirms that stabilization persisted at the same economic layer.

---

# 4. Live baseline — AI Infrastructure · 2026-08-30

> **Research-side adjudication only.**  
> This baseline may use post-2026-08-28 evidence because `research-validation/` is explicitly outside the frozen formal-report evidence cutoff.

## 4.1 Evidence ledger

| ledger_id | publication_time | signal_family | actor / layer | observation | contrary signal / boundary | causal read | state contribution |
|---|---|---|---|---|---|---|---|
| AI26-001 | 2026-08-26 | Utilization / Revenue | NVIDIA / compute supplier | FY27 Q2 revenue **US$96.2B, +106% YoY**; Data Center **US$89.0B, +117% YoY** | revenue concentration remains material; China / export-control uncertainty persists; margins face component-cost pressure | strong current end-demand / shipment evidence, not clearing | **NO CLEARING evidence** |
| AI26-002 | 2026 Q2 filings | Forward Commitment / Financing | Meta + Alphabet + Amazon + Microsoft / hyperscalers | infrastructure capital intensity is extremely high; Meta quarterly cash headroom is near zero, Alphabet and Amazon show negative quarterly OCF-minus-CapEx headroom in Q2, while Microsoft continues very large cash + lease CapEx | all four retain large operating / balance-sheet funding capacity; one-quarter headroom is not debt-service stress | capital-intensity / duration-mismatch vulnerability | **WATCH — capital intensity, not clearing** |
| AI26-003 | 2026-06-01 / 2026-08-27 | Demand Quality / Financing | IREN / GPU project finance + AI cloud | Microsoft-linked GPU financing about **US$3.65B** at blended 6.0%; with prepayments funds about **96% of associated US$5.81B GPU CapEx**. FY26 AI Cloud Services revenue **US$128.8M vs US$16.4M FY25**; first 50MW Microsoft deployment delivered; 2026 capacity described as largely sold out | non-investment-grade customer financings are more expensive; company-level revenue is not facility-level DSCR closure | financing is available and deployment/monetization is occurring | **NO CLEARING evidence; financing-quality WATCH** |
| AI26-004 | 2026 Q2 / Aug filings | Demand Quality / Financing | CoreWeave / project finance | large DDTLs and notes remain available / drawn; additional 2026 financing capacity has been added | leverage and customer concentration remain high; facility draw does not prove utilization | financing channel is open rather than shut | **NO CLEARING evidence; refinancing/concentration WATCH** |
| AI26-005 | 2026-07-26 / 2026-08-17 | Demand Quality / Financing | NVIDIA / seller-support layer | existing AI-cloud LPS guarantee exposure and new conditional PORTS-Pike support show seller balance sheet increasingly involved in infrastructure delivery | maximum guarantee cap ≠ effective exposure ≠ triggered obligation ≠ funded cash loss; support cannot be double-counted as demand | reflexivity / support-dependence vulnerability, not a clearing event | **WATCH — seller-support dependence** |
| AI26-006 | 2026-08-03 | Demand Quality / Financing | U.S. bank credit / macro | July 2026 SLOOS, shown in FRED as **2026Q3 survey label** but describing changes predominantly over **2026Q2**, reports **0.0%** net tightening for large/middle-market C&I standards and **16.1%** net stronger demand | aggregate bank credit can miss NDFI/private-credit and borrower-specific stress; long rates remain restrictive | latest bank-credit evidence is stronger contrary evidence against an economy-wide credit seizure | **NO CLEARING / WATCH — credit selectivity** |

## 4.2 Composite adjudication

### 4.1A Temporal note added in v0.2

SLOOS is now logged by **publication time + FRED survey label + economic period described** rather than by one ambiguous quarter field.

This prevents a July/October/January survey release from being backfilled into the preceding economic quarter without preserving when the information actually became public.

See `04a-public-credit-panel.md` v0.3 for the maintained macro-credit time identity.

### Current research state

> **NO CLEARING — with elevated WATCH flags on capital intensity, customer concentration, seller-support reflexivity and financing-quality dispersion.**

The key reason this does **not** escalate to CANDIDATE / CONFIRMED is breadth.

Current observations contain real vulnerabilities:

```text
Hyperscaler CapEx intensity ↑
+
Seller / sponsor support ↑
+
Project leverage ↑
+
Customer concentration ↑
+
long-duration commitments ↑
```

But current contrary evidence is also broad:

```text
supplier revenue / Data Center demand ↑ sharply
+
major buyer commitments remain high
+
project financing is still closing
+
physical deployments are progressing
+
AI-cloud monetization is increasing
+
aggregate bank credit is not in crisis-tight mode
```

Therefore:

> **high leverage / high capital intensity / circularity risk ≠ current capital clearing.**

P0-1 requires an adverse state transition, not a high absolute level.

## 4.3 What would escalate the live state

A move from **WATCH → CANDIDATE** should require at least two independent mechanisms such as:

1. **Utilization / Revenue**
   - supplier / cloud / project monetization materially weakens;
   - deployed capacity utilization falls;

2. **Market Clearing**
   - secondary GPU / lease / capacity pricing weakens;
   - delivery lead times collapse because demand disappears rather than supply improves;
   - inventory / unused capacity rises;

3. **Forward Commitment**
   - hyperscaler / anchor-buyer CapEx is cancelled rather than rescheduled;
   - contracted data-center / power / GPU capacity is reduced;
   - project construction is deferred after financing / demand deterioration;

4. **Demand Quality / Financing**
   - refinancing terms worsen materially;
   - DDTL availability is cut / not renewed;
   - DSCR or covenant pressure appears;
   - guarantee obligations become triggered;
   - independent financing disappears while seller support substitutes for it.

A move to **CONFIRMED** additionally requires:
- multi-company or multi-layer breadth;
- persistence;
- no stronger regulatory / product-cycle / architecture-transition explanation.

## 4.4 What would de-escalate WATCH flags

Risk weight should fall if:
- quarterly cash headroom improves while capacity remains highly utilized;
- customer concentration falls;
- seller guarantee exposure steps down without activation;
- third-party financing replaces seller support;
- project revenue / cash conversion reaches contractual debt-service coverage;
- booked capacity becomes energized and utilized on schedule;
- refinancing occurs on stable or improving terms.

---

## 4.5 Live update — 2026-09-03

This update preserves the 2026-08-30 baseline and appends only evidence that became public afterward or that materially changes a maintained support-state interpretation.

| ledger_id | publication_time | signal_family | actor / layer | observation | contrary signal / boundary | causal read | state contribution |
|---|---|---|---|---|---|---|---|
| AI26-007 | 2026-09-02 | Utilization / Revenue + Forward Commitment | Broadcom / custom AI accelerator + networking supplier | Q3 FY2026 AI semiconductor revenue **US$16.7B, +221% YoY and +54% QoQ**; Q4 AI semiconductor revenue guidance **US$21.7B** | supplier revenue/guidance is not end-workflow ROI; custom-silicon demand can coexist with weakness elsewhere | independent large-supplier evidence that AI infrastructure demand / shipments remain strongly expansionary | **NO CLEARING evidence — broadens supplier-side contrary evidence beyond NVIDIA** |
| AI26-008 | 2026-08-27, incorporated into live ledger 2026-09-03 | Demand Quality / Financing | NVIDIA / seller-support architecture | Reuters reported certain AI-cloud revenue-sharing support arrangements were paused / redesigned | media-reported, not first-party filing; broader NVIDIA support model reportedly remained in place; no project cancellation or financing seizure established | support architecture is endogenous and can be redesigned; not evidence of end-demand destruction | **WATCH composition change; no escalation** |

### 4.5A State impact

The new Broadcom observation is important because it increases **independence and breadth** of the contrary evidence.

The previous baseline already had:

```text
NVIDIA Data Center revenue ↑
+
hyperscaler commitments remain high
+
project financing still closes
```

The 2026-09-02 Broadcom release adds:

```text
second major AI semiconductor / networking supplier
→ AI revenue growth remains extremely strong
→ near-term AI revenue guidance remains expansionary
```

That makes a supplier-side system-clearing interpretation less plausible at this adjudication time.

### 4.5B Support redesign is not clearing

The NVIDIA revenue-sharing-program report changes the **form** of seller support, not the live clearing state.

The evidence chain needed for escalation would be:

```text
support paused / redesigned
→ independent financing unavailable
→ project commitment reduced
→ deployment / monetization deteriorates
```

That transmission is not established.

Therefore:

> **seller-support redesign is a financing-architecture observation, not a demand-destruction observation.**

The canonical support-state detail remains in `04d-supplier-support-panel.md`.

### 4.5C Updated composite state

As of **2026-09-03**:

> **NO CLEARING — WATCH flags remain elevated for capital intensity, concentration, financing-quality dispersion and seller-support reflexivity.**

No move to CANDIDATE is justified.

The reason is still causal breadth:

- no broad utilization/revenue deterioration;
- no multi-buyer commitment cut;
- no financing seizure;
- no project-level clearing;
- no cross-supplier contraction.

The 9/2 Broadcom evidence strengthens rather than weakens that conclusion.

---

## 5. Evidence-origin map for the baseline

To avoid false breadth:

| origin | Can support | Must not be counted again as |
|---|---|---|
| NVIDIA product revenue | supplier demand / shipment evidence | separate customer financing evidence |
| hyperscaler CapEx | buyer forward commitment | separate end-workflow ROI proof |
| CoreWeave / IREN debt | financing availability | independent demand if debt is contract-backed |
| customer prepayment | contract / funding quality | both demand and financing as two independent confirmations |
| NVIDIA guarantee | seller support / risk distribution | funded CapEx or realized loss before activation |
| project revenue | monetization | facility-level DSCR unless cash-flow mapping exists |

---

## 6. Live-log update policy

Update this ledger only when one of these occurs:

- new quarterly filing / earnings release;
- financing close / refinance / covenant event;
- project ready-for-service / energization / utilization milestone;
- cancellation / deferral;
- guarantee activation / step-down / release;
- material inventory / pricing / secondary-market clearing evidence;
- borrower distress or customer-default transmission;
- public-credit regime shift.

Do **not** update merely because:
- a stock price moves;
- an analyst changes a price target;
- one media narrative becomes popular;
- one supplier announces a large headline commitment with no state transition.

---

## 7. Current source register

- NVIDIA FY27 Q2 results, 2026-08-26 — revenue US$96.2B, Data Center US$89.0B: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx
- NVIDIA FY27 Q2 Form 10-Q — customer concentration, investments / commitments and guarantee disclosures: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
- IREN, 2026-06-01 — US$3.65B investment-grade GPU financing, ~96% Microsoft GPU-CapEx funding with prepayments: https://iren.gcs-web.com/news-releases/news-release-details/iren-closes-365bn-investment-grade-gpu-financing
- IREN FY26 results, 2026-08-27 — AI Cloud revenue, contracted ARR, deployment state and financing-quality dispersion: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000051/irenreportsfy26results.htm
- Hyperscaler cash-flow / CapEx sources: see `04b-hyperscaler-quarterly-panel.md`.
- Project-finance facility sources: see `04c-project-finance-borrower-panel.md`.
- Seller / sponsor support sources: see `04d-supplier-support-panel.md`.
- Public-credit / SLOOS / CMDI sources: see `04a-public-credit-panel.md`.


- Broadcom Q3 FY2026 results, 2026-09-02 — AI semiconductor revenue US$16.7B, +221% YoY / +54% QoQ; Q4 AI semiconductor revenue guidance US$21.7B: https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-third-quarter-fiscal-year-2026-financial
- Reuters, 2026-08-27 — reported pause/redesign of certain NVIDIA AI-cloud revenue-sharing support arrangements; see canonical support treatment in `04d-supplier-support-panel.md`: https://www.reuters.com/business/nvidia-pauses-revenue-sharing-deals-with-ai-cloud-companies-wsj-reports-2026-08-27/
