# Phase II · Frozen-Text Gate Status v0.2

> **Status:** Research-side validation layer; not part of the frozen 32-chapter formal report, and does not change the formal 2026-08-28 evidence cutoff.  
> **Purpose:** record the coverage status of a test the frozen formal text sets for itself, which the chapter cannot record without breaching the freeze.  
> **Reproducible artifact:** `scripts/recompute_frozen_gate_status.py` over `data/frozen-gate-inputs.json`. Outputs are D-grade report-side tabulations.  
> **Chinese translation (derived):** [21-frozen-text-gate-status.zh.md](21-frozen-text-gate-status.zh.md)

## 0. Ownership contract v0.1

This file owns:

- the **register of tests the frozen formal text sets for itself**, and the coverage status of each;
- the **classification** of a frozen test's required variables into carried / partly observable / not disclosed / not yet observed;
- the **observation-boundary result**: which required variables are absent from the sampled panel, which may be observed before a default, and which require an event to have occurred.

It does **not** own: any chapter's text or conclusion (the frozen 32 chapters), any facility, borrower or support fact (`04C`/`04D`/`11`), the historical-analogy question itself (Ch23 §1B), scenario aggregation (`10`), or clearing adjudication (`01A`). It creates **no anchors** — every item is quoted from the chapter and every coverage claim points at a section of a layer that already exists.

**Why a new owner.** The layer system reads the frozen text and cannot write to it. That asymmetry is deliberate and correct, but it left one thing with no home: when the research panels come to carry variables a frozen chapter names as required, **nothing records it**, and a reader of the chapter has no way to learn the status of the test it states. No existing layer can hold this. The panels own facts, not the status of another document's tests; `10` aggregates evidence into scenario relevance, not into chapter-gate coverage; and `03`'s ledger is scoped to workflow economics. The gap is structural rather than accidental, so the layer is stated as a register with an explicit scope rather than as a general-purpose chapter audit.

## 1. The gate

The register's one entry is **CH23-1B**. Ch23 §1B is the chapter's own gate on its most rhetorically loaded comparison:

> Vendor assistance, SPVs, private credit, or off-balance-sheet structures can resemble features seen in previous infrastructure cycles. That resemblance is not enough to classify the current AI buildout as a replay of the telecom bubble or the 2008 securitization cycle.

It then names the eight contract-level variables a defensible comparison would require, and closes the loop itself:

> Without those contract-level variables, the analogy remains a **research heuristic**, not a formal report conclusion.

That is a test the report sets for itself, with its own stopping rule. What the chapter cannot say is which of the eight variables now exist — because saying so would mean editing a frozen chapter to report on the research side.

**The register has one entry, and that is stated rather than implied.** The frozen corpus was searched in both editions for enumerated evidence-requirement checklists of the form *"a defensible X would require evidence on: [list]"*. Ch23 §1B is the only one found; the Chinese edition is also searched for the corresponding 需要看到 / 需要证据 forms, which return this checklist plus one non-enumerated rule at Ch21. This file therefore does not present itself as a survey of the report's gates. It presents one gate, fully.

## 2. The tabulation

Eight items, classified by **exact variable identity** and by what the tracked research panels actually carry. A lease-payment backstop is not automatically a residual-value guarantee; generic support categories are not substitutes for contract terms.

| # | Required variable (quoted from Ch23 §1B) | Status | Evidence owner / boundary |
|---:|---|---|---|
| 1 | leverage and loan-to-value | **partly observable** | `04C` §11B.5: debt/collateral terms exist; facility-matched collateral valuation is missing |
| 2 | covenant quality and recourse | **carried** | `04C` §11B.5, §11B.5C |
| 3 | take-or-pay / minimum-revenue obligations | **carried** | `11` §2A support taxonomy; `04D` customer-prepayment row; coverage is not a complete facility census |
| 4 | residual-value guarantees or repurchase commitments | **not disclosed** | `04D` tracks lease/payment and completion guarantees, but these do not themselves establish a residual-value floor or repurchase obligation |
| 5 | senior / junior loss allocation | **partly observable** | `04C` §11B.5: instrument ranking exists; intercreditor waterfall and tranche-level recovery allocation are missing |
| 6 | refinancing dependence | **carried** | `04C` §11B.5C refinancing-state refresh |
| 7 | default / restructuring behavior | **not yet observed** | No such event recorded in the tracked current borrower panel; not a prediction about future events |
| 8 | transferability and secondary-market liquidity of the underlying assets | **not disclosed** | The tracked panels lack comparable facility-asset transaction, realized-price, depth, spread, transfer-restriction and recovery observations |

**Carried: 3 of 8. Partly observable: 2. Not disclosed: 2. Not yet observed: 1.** These are *panel coverage counts*, not percentages of a market, causal confidence weights, or evidence that the eight variables have been resolved at the level needed for the historical analogy.

The two partly observable items have **different missing contracts**. Item 1 needs facility-matched asset valuation to calculate LTV. Item 5 needs the priority, intercreditor, subordination and loss-waterfall terms to trace senior/junior allocation; a valuation by itself cannot supply that legal allocation. Item 4 is not carried merely because `04D` tracks guarantee caps: payment/lease-performance guarantees, project-completion backstops, residual-value protection, and repurchase undertakings answer different questions.

## 3. Observation boundaries, not an irreversible floor

The former v0.1 claim that *both* items 7 and 8 are structurally unobservable before distress was too strong.

**Item 7 is event-contingent in the observed cohort.** Default or restructuring behavior for a given borrower cannot be recorded as an occurred event before it occurs. Nevertheless, a panel can observe *other* borrowers' defaults and restructurings, analyze contractual recovery rights in advance, and update this item's status if a tracked borrower has an event. The current label is a bounded absence in this cohort, not a theorem that the historical comparison can never be evaluated.

**Item 8 is potentially observable before default.** Used GPUs, servers and data-center assets may have resale prices, transfers, bids, depth and restrictions before any distressed sale. The relevant research gap is narrower: `04C` / `11` do not yet carry a reliable matched series of realized transfers, prices, depth, transferability restrictions and recoveries for the *pledged assets* in the borrower sample. The existence of a resale quote would not by itself demonstrate scalable liquidity, distressed recovery value or transferable customer contracts.

**Do not substitute a compute-price derivative for physical collateral liquidity.** A contract or index concerning the price of computing capacity is a distinct object from a sale of financed GPUs or data-center assets; its launch or trading activity cannot close item 8.

The historical telecom/securitization analogy **remains a research heuristic under Ch23 §1B** because material evidence is not yet closed, not because a permanent logical barrier forbids its reassessment. Future verified disclosures and actual transactions could change coverage without automatically proving or disproving the analogy. No S1–S4 state or frozen chapter changes here.

## 4. What would change it

1. **A documented default or restructuring within the sampled cohort** moves item 7 from *not yet observed* to an observed event only after `04C` records the borrower, date, obligation and resolution.
2. **Auditable asset-sale, bid/ask and transfer records** with model/condition, transaction size, dates and asset/legal perimeter could move item 8 toward *partly observable* or *carried*. A single indicative quote is neither an executed sale nor a liquid market; evidence must match the pledged-asset scope.
3. **Facility-matched collateral valuation** can advance item 1, but only if the debt and asset units and valuation date close.
4. **Intercreditor and priority-of-payments documentation** can advance item 5. Collateral valuation alone cannot resolve it.
5. **A contractual residual-value floor or repurchase undertaking, including triggers and obligor**, can advance item 4. An ordinary rent/lease-payment guarantee cannot.
6. **A second enumerated checklist from the frozen corpus** adds a registered gate, not an inferred one.

## 5. Falsification / correction conditions

1. Evidence of a facility-matched valuation the panel missed challenges item 1; an actual intercreditor loss waterfall challenges item 5. Neither automatically changes the other.
2. A verified residual-value guarantee or repurchase obligation attached to a named asset/facility challenges item 4. A capped performance or payment guarantee is insufficient.
3. Evidence of actual matched secondary-market transfers and transaction depth for pledged assets challenges item 8. Listing prices alone do not.
4. A default/restructuring already recorded in `04C` challenges item 7 and requires correction of the sample status.
5. If the assumed source owners change their observations, update them first and rerun this classification. Do not turn a coverage change into a conclusion about an asset-price bubble.

## 6. Boundary rules

- **Status, never conclusion.** This layer records what the panels carry. It cannot promote the analogy, reject the analogy, or write anything into a chapter. The formal reopen gate is unchanged and this layer is not a path around it.
- **No new numeric identity.** Every item is quoted from Ch23 §1B; every coverage claim names an existing section. Nothing is estimated.
- **`not yet observed` is not zero and not N/A.** Item 7 means no event is recorded in the sampled cohort. Item 8 is *not disclosed* in the tracked facility-asset data, not inherently impossible to observe before default. Missing does not mean nonexistent.
- **No proxy substitution.** Keep legal waterfalls distinct from collateral valuation, residual-value support distinct from payment guarantees, and physical asset resale distinct from compute-price contracts. Partial inputs do not complete the variable.
- **The register is not a survey.** One gate, stated as one gate. Adding a second requires finding one, not inferring one.
- **No double-counting with `04C`/`04D`/`11`.** Those layers own the facts; this one owns only their coverage of a chapter's list. A fact that changes here changes them first.
- **No scenario switch, no S4, no composite index.** This layer cannot change `10`'s scenario relevance, confirm S4, or enter the frozen chapters, and its counts must never be netted into a score.
- **D-grade labeling is mandatory** wherever an output is reused, under `04-research-transparency`'s hierarchy.

## 7. Integration

1. Re-run `scripts/recompute_frozen_gate_status.py` when a panel's coverage changes, and update the table rather than appending narrative. The script asserts the classification, so a silent re-classification fails rather than propagating.
2. **Feeds nothing automatically.** `04C`, `04D` and `11` continue to own every fact; `10` continues to own scenario relevance. This layer adds no row to the dashboard and no input to any surface.
3. **A default is a `04C` event first.** If item 7 moves, the facility-state change belongs to `04C` and is recorded there; this layer re-runs afterwards.
4. `01A` adjudication: a default in the panel would be a financing-family contribution — recorded as one family among several, never as a standalone S4 confirmation and never multiplied into one index.

## Sources

No new external source. Every item is quoted from the frozen chapter and every coverage claim points at an existing layer section.

- The eight required contract-level variables, the analogy test, and the stopping rule — Ch23 §1B: [`publication/part-III-ch23-capital-financing.md`](../publication/part-III-ch23-capital-financing.md) / [`en/publication/part-III-ch23-capital-financing.md`](../en/publication/part-III-ch23-capital-financing.md)
- Facility debt, covenant, recourse, refinancing state — [`04C`](04c-project-finance-borrower-panel.md) §11B.5, §11B.5C
- Lease/payment and completion guarantee categories, **not** evidence of a contractual residual-value floor — [`04D`](04d-supplier-support-panel.md) §11C.3 support table
- Take-or-pay and customer-prepayment support forms — [`11`](11-financing-reflexivity-map.md) §2A
- Asset-transfer falsification signal — [`11`](11-financing-reflexivity-map.md) §6
- Evidence hierarchy and report-side calculation labeling — [Research Transparency](../publication/04-research-transparency.md)
