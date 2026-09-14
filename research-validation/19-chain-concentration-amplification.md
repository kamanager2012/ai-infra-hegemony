# Phase II · Chain Concentration Amplification v0.1

> **Status:** Research-side validation layer; not part of the frozen 32-chapter formal report, and does not change the formal 2026-08-28 evidence cutoff.  
> **Purpose:** quantify the one variable `11` names and cannot compute — how far an origin shock travels down a fixed-obligation financing chain, and how much headroom a link must already hold to survive it — using only concentration and obligation anchors already observed.  
> **Reproducible artifact:** `scripts/recompute_chain_amplification.py` over `data/chain-amplification-inputs.json`. Outputs are D-grade report-side calculations.  
> **Chinese translation (derived):** [19-chain-concentration-amplification.zh.md](19-chain-concentration-amplification.zh.md)

## 0. Ownership contract v0.1

This file owns:

- the **pass-through multiplier** along a financing chain, derived from observed concentration, and its **residual**;
- the **required-headroom and absorbable-decline surfaces** at observed covenant floors;
- the **two transmission channels** — proportional pass-through and counterparty step — the computed difference between them, and the observation that distinguishes which one is operating;
- the **ranking rule** for which link feels a shock first, together with the observed structural facts placed against it.

It does **not** own: financing taxonomy or the causal graph (`11`), the propagation chain itself, which is `11` §2's, borrower / facility state (`04C`), support activation (`04D`), the required-cash floor or the energization schedule (`15`/`17`), or clearing adjudication (`01A`). It creates **no anchors** — every input is read from `11` and `04C`.

**Why a new owner.** `11` §2 draws the propagation chain and §7 names the discriminating variable — *independent cash generation relative to fixed capital obligations* — but `11` is a taxonomy and explicitly declines to put a number on it. `04C` §11B.7C lists "DSCR / interest coverage" among the fields a future bridge should connect, and §11B.7D defines when a facility escalates without defining how far a shock travels to reach it. **Neither owns the transmission arithmetic between links**, which is what turns two observed concentration ratios into a statement about who breaks first.

## 1. The chain, as observed

`11` §2 gives the chain; `04C` §11B.5 gives each link's obligations:

```text
anchor / end-customer economics
  → CoreWeave contract economics
  → CoreWeave debt service          ~US$25.1B debt; US$6.1B due remainder-2026, US$5.7B 2027
  → Core Scientific colocation cash flow   CoreWeave ≈ 77% of H1 2026 revenue
  → Core Scientific debt service    US$4.4B debt; nothing due 2026–2028, US$649.8M in 2029
```

Three observed facts frame everything below:

1. **the concentration is 0.77** — the only observed link ratio carried anywhere in the repository;
2. **the upstream obligation is unbounded and immediate** — US$6.1B of principal falls due in the remainder of 2026;
3. **the downstream obligation is bounded and distant, and its cash is ring-fenced** — no principal due 2026–2028, and CoreWeave contract revenues feed a **lockbox** supporting the debt.

## 2. Pass-through and residual

Let `x` be the fractional decline in what the origin pays its direct counterparty, and `c` the downstream link's revenue concentration from the chain. Under proportional pass-through:

```text
revenue_after  = revenue_before x (1 - c x)
coverage_after = coverage_before x (1 - c x)
```

At the observed `c = 0.77`:

| Origin decline | Revenue retained | Coverage multiplier |
|---:|---:|---:|
| 25% | 80.8% | 0.807× |
| 50% | 61.5% | 0.615× |
| 100% | **23.0%** | **0.230×** |

**The concentration ratio is simultaneously the amplification factor and the residual.** At `c = 0.77` a total shutdown of the origin still leaves the downstream link 23% of its revenue, because 23% came from somewhere else. That single number is the most useful thing the ratio says, and it is the reason a concentration statistic is not by itself a distress statistic.

## 3. Required headroom

Inverting the identity: to sit exactly at a floor `F` after a decline `x`, a link must already hold `F / (1 − c x)`.

| Origin decline | Required at the 1.15× covenant | Required at 1.00× interest cover |
|---:|---:|---:|
| 5% | 1.196× | 1.040× |
| 10% | 1.246× | 1.083× |
| 20% | 1.359× | 1.182× |
| 30% | 1.495× | 1.300× |
| 50% | 1.870× | 1.626× |
| **100%** | **5.000×** | 4.348× |

**A complete shutdown of the origin requires 5.00× current coverage** — exactly `1.15 / 0.23`. A link holding anything less than five times its debt service cannot survive its counterparty going to zero at this concentration.

## 4. Absorbable decline

The same result read from the other side — the largest origin decline a link survives:

| Coverage before | Absorbable decline at the 1.15× covenant |
|---:|---:|
| 1.20× | 5.4% |
| 1.30× | 15.0% |
| 1.50× | 30.3% |
| 1.75× | 44.5% |
| 2.00× | 55.2% |

**A link already sitting at its covenant absorbs 0%**, which is trivial — and the non-trivial version is directly beneath it: **the covenant floor, not the concentration, consumes most of the shock budget.** At 1.50× coverage the link could absorb a 43.3% decline before losing interest cover, but only **30.3%** before breaching the covenant. The 1.15× floor is what converts a 30% shock budget into a 15% one at 1.30×, and into nothing at the floor itself.

That is a computable statement of something the report asserts qualitatively: **a covenant is an amplifier, not a guardrail.**

## 5. Chain depth — the shock attenuates downward

Each additional link multiplies the arriving shock by its own concentration, so the cumulative pass-through is the product. The upstream link's own concentration is **not disclosed in the rows carried here** and enters as a dial:

| Upstream `c₁` | Cumulative | Retained at shutdown | Required coverage |
|---:|---:|---:|---:|
| 0.50 | 0.385 | 61.5% | 1.870× |
| 0.77 | 0.593 | 40.7% | 2.825× |
| 0.90 | 0.693 | 30.7% | 3.746× |

**The shock attenuates as it travels outward.** The link nearest the origin absorbs the largest fraction of any origin shock; position alone predicts consequence backwards. This is worth stating because the intuitive reading — that the most distant link is most exposed — is wrong in this model.

## 6. The two transmission channels

The proportional model above is one of two mechanisms, and the observed structure selects between them.

**Channel A — proportional pass-through.** Applies when the intermediate obligation is variable: revenue-share, cost-plus, renegotiable, or the intermediary absorbs the shock by cutting its own margin. The origin shock arrives as `c x`, continuously.

**Channel B — counterparty step.** Applies when the intermediate obligation is fixed: a take-or-pay lease, or cash that is contractually ring-fenced. The downstream link is **insulated** until the upstream link's own coverage breaches, and then takes a step of size `c` at once.

| Upstream breach at `x*` | A's damage at `x*` | B's damage at `x*` | Step ratio |
|---:|---:|---:|---:|
| 20% | 0.154 | 0.770 | **5.00×** |
| 30% | 0.231 | 0.770 | 3.33× |
| 50% | 0.385 | 0.770 | 2.00× |
| 77% | 0.593 | 0.770 | 1.30× |

**The channels differ in shape, not in expected level: A drifts, B steps.** And B is worse at the moment it matters — if the upstream link breaches at a 30% origin decline, B inflicts the full 0.77 at once where A would have inflicted 0.231, a **3.33× larger instantaneous hit**.

**The observed structure is evidence for Channel B.** `04C` §11B.5 records that CoreWeave contract revenues **feed a lockbox supporting Core Scientific's debt** — i.e. the intermediate obligation is fixed and the cash is ring-fenced. Under Channel B the decisive quantity is therefore **not** Core Scientific's headroom. Core Scientific is insulated until CoreWeave breaches; what determines the downstream link's fate is **CoreWeave's** breach point. CoreWeave's coverage is **not carried in the repository**, so this layer stops at the rule and does not assert the number.

**The distinguishing signature is directly observable and cheap.** Under A, the downstream link's revenue from the chain tracks the origin proportionally. Under B, it stays flat and then moves in a step. **The next Core Scientific filing tests which channel is operating** — and it is the cheapest test this layer has.

**That test now has a runnable form, and one correction.** The observable, the statistic relating the two links' series, its predicted value under each channel, the disclosure granularity a separation needs and the verdicts — fixed before the data rather than after it — are owned by `22`. That layer also records a precondition this section does not state: **at zero upstream decline the two channels predict the same observation**, so a flat downstream series decides nothing without a measured upstream decline. The test is therefore **two series, not one filing**, and the framing above is corrected there rather than left standing here.

## 7. Which link feels it first

`11` §7's discriminating variable is *independent cash generation relative to fixed capital obligations*. Putting the computed pieces against the observed structural facts:

```text
pressure at a link  =  cumulative concentration
                       x obligation due in the window
                       / (headroom above its own floor x revenue)
```

Per-link revenue and coverage are not carried in the repository, so **the rule is stated and no ranking is asserted.** What can be placed against it is observed, and it points somewhere non-obvious:

| | Core Scientific (77% concentrated) | CoreWeave (heaviest wall) |
|---|---|---|
| Principal due in the window | **US$0.0B 2026–2028**; US$649.8M 2029 | **US$6.1B remainder-2026**, US$5.7B 2027, on US$25.1B total debt |
| Committed undrawn liquidity | not carried | US$10.0B at 2026-06-30 |
| Undrawn / 2026 wall | — | **1.64×** |
| Undrawn / 2026+2027 wall | — | **0.85×** |
| Structural | lockbox on CoreWeave revenue; no variable-rate debt | several SPV structures; DDTL 4.0 largely non-recourse |
| Blended reported interest | 3.70% (includes a 0%-stated convertible) | 6.80% |

**Concentration and immediacy point at different links.** The more concentrated link has the milder wall, the ring-fenced cash, and the cheaper blended debt. The link facing the immediate wall is the one the origin pays directly — and **its 2027 wall is not covered by committed liquidity** (0.85×), so it must be refinanced, which makes refinancing access the transmission channel from origin economics to the downstream link.

Two caveats, both stated rather than smoothed: the US$6.1B is **as of 2026-03-31** while the US$10.0B availability is **as of 2026-06-30**, so the 1.64×/0.85× pair is a cross-date boundary comparison and not a point-in-time coverage statement; and the 3.70% blended rate includes a 0%-stated convertible, so it is not a like-for-like cost comparison with 6.80%.

## 8. What would collapse it

1. **A disclosed per-link revenue and coverage** would replace the ranking rule with a computed ranking.
2. **A disclosed CoreWeave customer-concentration ratio** would remove the `c₁` dial and let the chain depth compound on observations.
3. **The next downstream filing** would identify Channel A or B directly, collapsing §6 to one mechanism.
4. **A disclosed fixed-charge coverage or DSCR at either link** would make §3's required-headroom surface checkable against a real number instead of a floor convention.

## 9. Boundary rules

- **No new anchors, no inference between borrowers.** Every input is read from `11` / `04C`; `04C` §11B.5A's rule — do not infer a value from another borrower to complete the matrix — applies unchanged.
- **The concentration ratio is not a distress measure.** At `c = 0.77` the link retains 23% of its revenue under a total origin shutdown; concentration alone says nothing about whether that is enough.
- **The channels are alternatives, not layers.** They must not be added, averaged, or used to bracket a range. Which one operates is an empirical question that the next filing answers.
- **No per-link claim.** Nothing here states any named company's coverage, headroom, or probability of breach.
- **No composite index.** The pass-through multiplier, the required-headroom surface, and the obligation schedule must never be netted into a score or multiplied into a multi-family signal.
- **No scenario switch, no S4, no evidence grade.** This cannot change `10`'s scenario relevance, cannot confirm S4, and cannot enter the frozen chapters.
- **D-grade labeling is mandatory** wherever an output is reused, under `04-research-transparency`'s hierarchy.

## 10. Integration

1. Re-run `scripts/recompute_chain_amplification.py` when `11`'s chain, `04C`'s concentration anchors, or either link's obligation schedule moves.
2. **Feeds `18`'s terminal link.** `18` computes the required-cash curve for a contract-backed facility; this layer computes how an origin shock reaches the facility that holds the contract. Composing them is a **link**, and the same prohibition applies: no composite index may be built from `19` and `18`.
3. **Proposed extension (not yet applied):** once a per-link revenue and coverage are disclosed, `04C` §11B.7C's monetization bridge can carry the absorbable-decline figure as a facility-state field. Until then `04C` is unchanged.
4. `01A` adjudication: a step change in a downstream link's chain revenue would be a financing-family observation — recorded as one family among several, never as a standalone S4 confirmation.

## Sources

No new external source. All anchors are read through `11` and `04C` and carry their source identity there.

- The propagation chain and the discriminating variable — [`11`](11-financing-reflexivity-map.md) §2, §7
- CoreWeave concentration, debt, maturity schedule, undrawn availability, covenant state — `04C` §11B.5, §11B.5C, §11B.7A
- Core Scientific concentration (77%), debt structure, lockbox, interest detail — `04C` §11B.5, §11B.5C; Core Scientific Q2 2026 Form 10-Q
- The 1.15× DSCR covenant convention — `04C` §11B.5 (Nebius secured facility); also used in [`15`](15-capital-to-cash-bridge.md)
- Monetization-bridge fields and the facility-state stress protocol — `04C` §11B.7C, §11B.7D
- Evidence hierarchy and report-side calculation labeling — [Research Transparency](../publication/04-research-transparency.md)
