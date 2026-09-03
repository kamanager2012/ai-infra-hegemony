# P0-4D · Supplier / Sponsor Support Panel v0.3

> Initially extracted from P0-4 v0.17; the parent method is now v0.18. Support is a risk-distribution layer, not an independent copy of end demand.

## 11C. Supplier / Sponsor Support overlay

The project-finance layer now needs an explicit support overlay.

Support is classified separately from borrower debt:

| Support channel | Examples | What to monitor |
|---|---|---|
| Strategic equity | NVIDIA → CoreWeave | recipient liquidity, dilution, whether support substitutes for weaker independent capital |
| Lease / payment guarantee | NVIDIA AI-cloud / LPS guarantees; AMD data-center lease guarantees | maximum exposure, activation conditions, step-down / termination terms |
| Vendor / OEM financing | CoreWeave OEM/software financing; IREN Dell GPU leases | tenor, guarantee, residual value, dependence on vendor credit |
| Third-party capital mobilization | seller-coordinated infrastructure financing platforms | actual third-party risk bearing vs announced capacity |
| Customer prepayment | Microsoft / IREN; take-or-pay colocation | prepayment share, customer concentration, performance obligations |

### 11C.1 Current rule

Seller / sponsor support is **not** negative evidence by itself.

It becomes S4-relevant only when:

```text
Support Dependence ↑
+
Independent Capital Access ↓
+
Customer / Workload Economics ↓
+
Refinancing Terms Worsen
```

Likewise, a guarantee cap is not a funded cash loss.

The overlay therefore records:

- maximum support amount;
- funded vs unfunded;
- conditional vs currently effective;
- guaranteed obligation identity;
- who bears first loss;
- whether support declines as project cash flow matures.

### 11C.2 No-double-counting rule

Do not sum:

```text
customer contract
+ debt raised against contract
+ seller equity
+ guarantee cap
+ customer prepayment
```

as independent demand.

They are separate financing / risk-distribution layers around the same underlying infrastructure expectation.

This overlay is maintained jointly with `11-financing-reflexivity-map.md`.

---


## 11C.3 Support Activation / Drawdown Ledger v0.2

The support overlay now uses four separate states:

```text
Maximum Exposure
≠
Effective Exposure
≠
Triggered Obligation
≠
Funded Cash Loss
```

This is required because a large guarantee cap can exist years before:
- a facility is ready for service;
- the covered lease starts;
- a customer defaults;
- the guarantor makes any cash payment.

### 11C.3A Current support-state panel

| Support / sponsor | Maximum / stated support | Activation mechanics | Current observable state | Funded-loss / draw state | Research treatment |
|---|---:|---|---|---|---|
| **NVIDIA · existing AI-cloud LPS guarantees** | about **US$3.529B** notional / maximum gross exposure at 2026-07-26 | cover selected AI-cloud partners' land / power / shell lease obligations upon default | guarantees are recognized as credit derivatives; fair values were not significant; partner escrow of about **US$712M** partially mitigates exposure | no separate funded-loss amount disclosed in the Q2 filing used here | **Effective support exists; do not treat notional as cash loss or demand** |
| **NVIDIA · SB Energy PORTS-Pike** | aggregate obligation capped at **US$105B** for initial ~4.25 IT-GW | each guarantee generally becomes effective when the applicable lease commences / ready-for-service conditions are satisfied; nine phases; first service expected beginning in NVIDIA FY2029; exposure declines as OpenAI makes lease payments | signed August-2026; conditions and future service milestones remain ahead | **not a current US$105B funded outflow**; no triggered payment state is established by the filing | **Conditional future credit support; track phase activation, lease commencement, tenant performance and step-down** |
| **AMD · partner data-center lease guarantees** | maximum potential future payments about **US$4.1B** at 2026-06-27 | tied to certain commercial-partner data-center lease obligations, terms up to 15 years | guarantee capacity disclosed alongside commenced / not-yet-commenced lease commitments | public filing used here does not identify a realized guarantee payment | **Risk-support exposure; not independent demand and not funded CapEx** |
| **Applied Digital · project completion guarantees** | amount is not a single headline cap in the FY2026 filing | sponsor must provide project entity funds if note proceeds / available funds are insufficient to achieve specified lease commencement milestones | guarantee obligation exists for identified financed data-center projects | no activation / shortfall draw is identified in the FY2026 filing used here | **Delivery-risk backstop; activation would be a new adverse facility-state signal** |
| **IREN · customer prepayments** | tranche-linked prepayments; Microsoft-linked structure plus financing funds about **96% of associated GPU CapEx** according to FY2026 materials | prepayment occurs before delivery and is credited against later service fees | funded customer support is economically different from a guarantee because cash is received before service | **funded**, but it creates future performance obligations rather than free revenue | **Funding support + contract evidence; do not double count as both demand and financing** |

### 11C.3B Activation-state vocabulary

Future quarterly maintenance should use one of:

- **UNCOMMITTED** — no binding support;
- **COMMITTED-CONDITIONAL** — signed but future conditions remain;
- **EFFECTIVE-UNTRIGGERED** — guarantee / backstop is in force, no default-triggered payment;
- **TRIGGERED-UNFUNDED** — contractual trigger occurred but cash loss not yet settled;
- **FUNDED** — cash / equity / prepayment / guarantee payment has actually moved;
- **STEPPING-DOWN** — exposure declines as project/customer obligations are performed;
- **TERMINATED / RELEASED** — support no longer applies.

These are financing-state labels, not S1–S4 states.

### 11C.3C Hard accounting rule for guarantees

For every guarantee, the panel must separately maintain:

```text
Notional / Maximum Gross Exposure
Current Fair Value / Provision
Escrow / Collateral / Indemnity
Effective Amount
Triggered Amount
Cash Paid
Remaining Exposure
```

If one of these fields is not disclosed, record:

> **not publicly disclosed**

Do not infer it from the headline guarantee cap.

### 11C.3D What would constitute deterioration

Guarantee / support dependence becomes an S4 amplifier only if state transitions move adversely, for example:

```text
COMMITTED-CONDITIONAL
→ EFFECTIVE
→ TRIGGERED
→ FUNDED LOSS
```

while independent customer economics / refinancing are also weakening.

The opposite path is contrary evidence:

```text
EFFECTIVE
→ customer performs
→ exposure steps down
→ guarantee released
```

For PORTS-Pike, the next high-information observations are therefore:
- each ready-for-service / lease-commencement phase;
- guarantee amount becoming effective by phase;
- OpenAI lease performance;
- any replacement-tenant / assumption mechanics;
- exposure step-down;
- whether additional ~3.8 GW credit support is exercised.

The **US$105B cap itself is not a clearing signal**.

---

## 11C.4 Reported support-program redesign — NVIDIA revenue-sharing arrangements

On **2026-08-27**, Reuters reported, citing the Wall Street Journal, that NVIDIA had paused certain revenue-sharing arrangements with AI-cloud companies under a recently launched financing/support program.

The reported program design had included combinations of:
- credit / support for AI-cloud operators;
- revenue-sharing tied to NVIDIA-hardware-generated cloud revenue;
- capacity-repurchase / backstop concepts.

Reuters also reported NVIDIA's position that the broader business model remained in place and was evolving amid strong demand.

### 11C.4A Evidence identity

This item is **media-reported support-structure evidence**, not a first-party filing.

Research treatment:

> **C-grade support-program transition — useful for monitoring support architecture, insufficient to infer funded loss, financing shutdown, or end-demand deterioration.**

### 11C.4B Why this matters

The support ledger previously focused heavily on:

```text
COMMITTED
→ EFFECTIVE
→ TRIGGERED
→ FUNDED
```

This event proves the opposite direction also matters:

```text
ANNOUNCED / PILOTED SUPPORT
→ TERMS REDESIGNED
→ PARTIALLY PAUSED
→ REPLACED / TERMINATED / RESUMED
```

Therefore support monitoring must track **program design changes**, not only guarantee activation.

### 11C.4C New support-state labels

Add two operational labels:

- **REDESIGNED** — support remains conceptually available, but economics / eligibility / revenue-sharing / backstop terms change;
- **PAUSED-PARTIAL** — a defined subset of a support program is paused without evidence that the entire financing channel has shut.

These are not S4 states.

### 11C.4D Current adjudication

The reported pause does **not** establish:

- AI-cloud financing seizure;
- NVIDIA withdrawal from infrastructure support;
- triggered guarantee losses;
- weakening customer demand.

It does establish:

> **seller-support architecture is endogenous and can be revised when governance, economics, antitrust exposure, or partner incentives change.**

This improves the anti-circularity test.

If support is later replaced by:
- independent third-party credit;
- customer cash flow;
- long-duration normal project debt,

that is contrary evidence to seller-dependent circularity.

If instead seller support repeatedly returns in larger forms as independent capital weakens, S4 / reflexivity weight rises.

### 11C.4E No-double-counting implication

A paused or redesigned support program must not be treated as a fall in end demand unless:

```text
support reduction
→ financing access worsens
→ project delivery / capacity commitment falls
→ customer demand / monetization weakens
```

Without that transmission, the observation belongs only to the **support architecture** layer.

---

## Related evidence layer

See also [11 · Financing Reflexivity Map](11-financing-reflexivity-map.md), which maintains the 2026 support taxonomy and source-level evidence for strategic equity, guarantees, vendor/OEM finance, third-party capital mobilization, and customer prepayments.


## Support-activation sources added in v0.2

- NVIDIA FY27 Q2 Form 10-Q — existing ~US$3.529B AI-cloud LPS guarantees, ~US$712M partner escrow, PORTS-Pike phased US$105B cap and activation mechanics: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
- NVIDIA FY27 Q2 CFO commentary — existing AI-cloud guarantees, PORTS-Pike ready-for-service / phase mechanics and maximum exposure: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm
- NVIDIA 2026-08-17 Form 8-K — residual-value guarantee agreements and conditional commencement / ready-for-service structure: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm
- AMD Q2 2026 Form 10-Q — approximately US$4.1B maximum potential future payments under partner data-center lease guarantees: https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm
- Applied Digital FY2026 Form 10-K — project completion guarantees tied to lease commencement milestones: https://www.sec.gov/Archives/edgar/data/1144879/000114487926000048/apld-20260531.htm
- IREN FY2026 results — customer prepayments and financing coverage of Microsoft-linked GPU CapEx: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000051/irenreportsfy26results.htm


- Reuters, 2026-08-27, “Nvidia pauses revenue-sharing deals with AI cloud companies, WSJ reports” — media-reported support-program redesign; not first-party filing evidence: https://www.reuters.com/business/nvidia-pauses-revenue-sharing-deals-with-ai-cloud-companies-wsj-reports-2026-08-27/
