# Phase II · Frozen-Text Gate Status v0.1

> **Status:** Research-side validation layer; not part of the frozen 32-chapter formal report, and does not change the formal 2026-08-28 evidence cutoff.  
> **Purpose:** record the coverage status of a test the frozen formal text sets for itself, which the chapter cannot record without breaching the freeze.  
> **Reproducible artifact:** `scripts/recompute_frozen_gate_status.py` over `data/frozen-gate-inputs.json`. Outputs are D-grade report-side tabulations.  
> **Chinese translation (derived):** [21-frozen-text-gate-status.zh.md](21-frozen-text-gate-status.zh.md)

## 0. Ownership contract v0.1

This file owns:

- the **register of tests the frozen formal text sets for itself**, and the coverage status of each;
- the **classification** of a frozen test's required variables into carried / partly observable / not disclosed / not yet observed;
- the **permanent-floor result**: which required variables cannot be observed before the outcome they describe, and what that does and does not imply.

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

Eight items, classified by what the research panels carry:

| # | Required variable (quoted from Ch23 §1B) | Status | Carried by |
|---:|---|---|---|
| 1 | leverage and loan-to-value | **partly observable** | `04C` §11B.5 facility rows |
| 2 | covenant quality and recourse | **carried** | `04C` §11B.5, §11B.5C |
| 3 | take-or-pay / minimum-revenue obligations | **carried** | `11` §2A support taxonomy; `04D` customer-prepayment row |
| 4 | residual-value guarantees or repurchase commitments | **carried** | `04D` support table |
| 5 | senior / junior loss allocation | **partly observable** | `04C` §11B.5 facility rows |
| 6 | refinancing dependence | **carried** | `04C` §11B.5C refinancing-state refresh |
| 7 | default / restructuring behavior | **not yet observed** | — |
| 8 | transferability and secondary-market liquidity of the underlying assets | **not yet observed** | — |

**Carried: 4 of 8. Partly observable: 2. Not yet observed: 2. Not disclosed: 0.**

The two half-observable items fail in the same way: the half that exists is the instrument side, and the half that is missing is the valuation side. Debt principal, coupon, maturity, collateral and non-recourse status are carried per facility, but no facility discloses the asset-side value an LTV needs, so the ratio cannot be formed. Instrument seniority is recorded, but the loss waterfall between tranches — which is what *loss allocation* means — is not. **Neither is a collection gap. Both are disclosure boundaries**, and the panels report them as such rather than substituting a proxy.

## 3. The permanent floor

Items 7 and 8 are not uncovered. They are **unobservable in advance**, and the difference is the result.

A bubble is identified *ex post*: by defaults, and by assets that fail to transfer to a new owner at a defensible value. Both are **outcomes rather than states**. No disclosure can supply a default before it happens, and no reporting supplies secondary-market liquidity for a market that does not yet exist. The adjacent market-structure item — the compute futures announced for 2026-10-05 (still PRE-LAUNCH as of 2026-09-23, with elevated regulatory-calendar risk) — is in exactly this position and is treated that way in `04C`: pending liquidity rather than carrying any.

So the Ch23 §1B test is not "6 of 8 covered, two gaps remaining". It has a **floor that further reporting cannot lift**, because the two decisive variables are the two that only exist after the question is settled. This is a stronger statement than *the evidence is incomplete*, and it is the reason this layer exists rather than a line in a panel.

**What it does not mean.** It does **not** make the analogy wrong, and it does **not** make a bubble less likely. A buildout can be a bubble and default behavior can be the proof — that is precisely why the variable is decisive. What follows is narrower and, for this report's purposes, more useful: **the analogy cannot be promoted to a conclusion by any amount of further disclosure**, so Ch23 §1B's stopping rule is not a temporary state of the evidence. The chapter's own caution and the structural bound agree.

## 4. What would change it

1. **A first default or restructuring in the panel** would convert item 7 from *not yet observed* to an observation — and it would be a genuinely new facility state, not a disclosure. This is the only item here that a future *event* rather than a future *filing* can move.
2. **A secondary transaction in GPU or data-center assets** at a disclosed price would begin item 8, though one transaction is a price, not a market.
3. **A disclosed asset-side valuation attached to a facility** would close items 1 and 5 together, since both wait on the same missing half.
4. **A second enumerated checklist found in the frozen corpus** would add a gate to the register. The §0 scope does not change; the register is additive by construction.

## 5. Falsification conditions

1. **A facility disclosing an asset-side valuation that the panels had missed** would move items 1 and 5 to *carried* and would show this tabulation understating coverage.
2. **A default already recorded somewhere in the repository** would break item 7's *not yet observed* status and would make the permanent-floor argument wrong for the current population.
3. **An operating secondary market in GPU assets with observable pricing** would break item 8, and with it the claim that the floor is structural rather than a 2026 condition.
4. **A frozen-text gate whose variables are all observable in advance** would show the permanent floor to be a property of this gate rather than a general one — which is the correct reading and is stated as such in §0's scope.

## 6. Boundary rules

- **Status, never conclusion.** This layer records what the panels carry. It cannot promote the analogy, reject the analogy, or write anything into a chapter. The formal reopen gate is unchanged and this layer is not a path around it.
- **No new numeric identity.** Every item is quoted from Ch23 §1B; every coverage claim names an existing section. Nothing is estimated.
- **`not yet observed` is not zero and not N/A.** Items 7 and 8 are absences of the *observable* class, which is why they are counted separately from *not disclosed* — a distinction this layer exists to preserve.
- **No proxy substitution.** Where a variable is half-carried, the missing half is stated as missing rather than filled with a substitute, which is what makes items 1 and 5 *partly observable* rather than *carried*.
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
- Guarantee caps and residual value as a tracked field — [`04D`](04d-supplier-support-panel.md) support table
- Take-or-pay and customer-prepayment support forms — [`11`](11-financing-reflexivity-map.md) §2A
- Asset-transfer falsification signal — [`11`](11-financing-reflexivity-map.md) §6
- Evidence hierarchy and report-side calculation labeling — [Research Transparency](../publication/04-research-transparency.md)
