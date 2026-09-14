# Phase II · Channel Discrimination Test v0.1

> **Status:** Research-side validation layer; not part of the frozen 32-chapter formal report, and does not change the formal 2026-08-28 evidence cutoff.  
> **Purpose:** turn `19` §6's claim that "the next downstream filing tests which channel is operating" into an executable test — the observable, the statistic, its two predicted values, the resolution the test needs, and the verdict table fixed before the data arrives.  
> **Reproducible artifact:** `scripts/recompute_channel_discriminator.py` over `data/channel-discriminator-inputs.json`. Outputs are D-grade report-side calculations.  
> **Chinese translation (derived):** [22-channel-discrimination-test.zh.md](22-channel-discrimination-test.zh.md)

## 0. Ownership contract v0.1

This file owns:

- the **observable** that separates the two transmission channels, and the statement that it is a pair of reported series rather than one filing;
- the **statistic** — the downstream link's chain revenue against the upstream link's decline — together with its two predicted slopes;
- the **resolving-power surface**: the smallest upstream decline each level of disclosure granularity requires;
- the **pre-registered verdict table**, including the two outcomes that falsify claims the layer system currently makes.

It does **not** own: the propagation chain (`11` §2), the two channels themselves (`19` §6), the concentration anchor (`04C` §11B.5), clearing adjudication (`01A`), or any per-link revenue, coverage or breach probability — none of which is carried anywhere in the repository. It creates **no anchors**. The single input is the observed concentration `04C` §11B.5 carries and `19` §2 already builds a surface from.

**Why a new owner.** `19` §6 states that the channels differ in shape, that the observed lockbox is evidence for the fixed-obligation channel, and that the next downstream filing "tests which channel is operating". Those are three different kinds of statement, and the third does not follow from the first two as written: it names no quantity to read, no value that would count for either channel, and no threshold. It also omits a precondition — see §3. **A test that cannot be failed in a stated way is not a test**, and the layer that established the channels is not the layer that should supply the rule by which its own inference is adjudicated.

## 1. Two claims about one slope

The channels are not two models of different quantities. They are two claims about the **same** quantity: the slope relating the downstream link's chain revenue to the upstream link's decline.

Under **A — proportional pass-through**, the intermediate obligation is variable, the decline arrives continuously, and the downstream link retains `1 − c u`. Under **B — counterparty step**, the obligation is fixed and the cash ring-fenced, so the downstream link is insulated until the upstream link breaches and then takes one step of size `c`.

Both are functions of the single observed concentration `c = 0.77`. Nothing else is needed, and nothing else is asserted.

## 2. What each channel predicts

Retention is the downstream link's chain revenue as a fraction of its prior level; the upstream decline is the upstream link's own reported revenue decline. Channel B's column is flat because the breach has not happened in any row shown; the row at a total upstream decline stands for the step itself.

| Upstream decline | A retention | B retention | Separation |
|---:|---:|---:|---:|
| 10% | 92.3% | 100.0% | 7.7% |
| 20% | 84.6% | 100.0% | 15.4% |
| 30% | 76.9% | 100.0% | 23.1% |
| 50% | 61.5% | 100.0% | 38.5% |
| 77% | 40.7% | 100.0% | 59.3% |
| 100% | 23.0% | 100.0% | 77.0% |

**The separation is `c u`, so the downstream series is always a damped copy of the upstream one** — strictly damped, because `c < 1`. That is the test's ceiling: no observation of the downstream link can be more sensitive than the chain is transmissive, and the chain's transmissivity is the concentration ratio itself.

The retention column is the function `19` §2 already tabulated. That layer computed it without labelling it: **its table is Channel A's prediction curve**, parameterised on the origin's payment decline, and Channel B's is the constant `100.0%` that `19` never wrote beside it. The two agree wherever the upstream link's reported decline is attributable to the chain in full — the boundary §3 states, and one this table does not assume.

## 3. The precondition that was not stated

At an upstream decline of zero, both channels predict the same observation: `100.0%`. **The two hypotheses are observationally identical when nothing has declined.**

So a flat downstream series is evidence for B only in proportion to a measured upstream decline. Read without one it is consistent with both channels, and `19` §6's "the next downstream filing tests which channel is operating" is therefore not a single-filing test. **It is a two-series test**: the upstream link's reported revenue is the antecedent, the downstream link's chain revenue is the consequent, and neither alone decides anything.

That is a correction to `19` rather than an addition to it, and it cuts both ways. The test is also *cheaper* in one respect the earlier statement implied and did not establish: no origin-economics data is needed at all, because the antecedent is observable one link in. And it is *weaker* in another: the antecedent must be the chain-attributable part of the upstream link's revenue decline, and to the extent that decline comes from business outside the chain, the measured slope is attenuated by exactly that dilution. `19` §5 already carries the upstream concentration `c₁` as a dial for the same reason; this test reads the upstream decline directly and so does not need `c₁`, which is what makes it cheap — and that substitution is the boundary it inherits.

## 4. Resolving power

The two channels differ by exactly `c u`, so a downstream observation separates them only once that difference exceeds what the disclosure can resolve. Inverting: an upstream decline of `δ / c` is the smallest that moves the downstream series by more than a resolution `δ`.

| Resolution (of the downstream link's chain revenue) | Upstream decline required |
|---:|---:|
| 1% | 1.3% |
| 2% | 2.6% |
| 5% | 6.5% |
| 10% | 13.0% |
| 15% | 19.5% |

Both columns are fractions of their own series, so the table carries no revenue level and is dimensionless: the reader substitutes the reporting granularity of the series they actually have.

Two consequences worth stating, because both run against the intuition that a finer disclosure is simply better. First, **the test's floor is set by the consequent's granularity, not the antecedent's** — a precise upstream number is wasted against a coarse downstream one. Second, because `c < 1`, **every upstream decline is discounted before it becomes a downstream signal**, so a chain that transmits weakly is also a chain that is hard to test. The same concentration that decides how far a shock travels decides how little of it the observation can see.

## 5. Pre-registered verdicts

Four outcomes, not two. The table is fixed here, before the data, so that the reading cannot be chosen after the fact.

| Observed slope | Verdict | What it does to the layer system |
|---|---|---|
| near `0` | **B operating.** The fixed obligation holds in behaviour as well as in structure. | `19` §6 collapses to one mechanism; the observation goes to `01A` as one financing-family entry, never as a standalone confirmation. |
| near `−0.770` | **A operating.** The obligation is variable despite the lockbox's structure. | `19` §6's structural inference is contradicted by behaviour and must be re-derived from the obligation terms, not re-labelled. |
| strictly between | **Neither channel.** Partial pass-through is the mechanism. | The dichotomy itself is falsified by observation. It must be re-derived, not re-labelled — and note that this is the outcome the boundary rule against averaging would conceal. |
| steeper than `−0.770` | **The denominator is wrong.** Something other than the chain moved the downstream link's revenue. | The antecedent is not chain-attributable in the way §3 requires, and the dilution boundary is what has to be measured first. |

The third row is the one this layer exists for. `19` §9 forbids adding or averaging the channels, and that rule is correct for a *model*; but if the world returns a slope between the two, the prohibition is not what was violated — **the assumption that the channels are alternatives is**. A rule that prevents the analyst from averaging two hypotheses must not also prevent the data from rejecting both.

## 6. What would collapse it

1. **Disclosed obligation terms at the intermediate link** — whether the lease is take-or-pay, its term, and whether the cash is contractually ring-fenced — would make B a matter of contract rather than inference, and the test unnecessary. The test is what a reader needs when the contract is not in hand.
2. **A disclosed upstream concentration `c₁`** would make the antecedent's chain-attributable share measurable, removing §3's dilution boundary.
3. **A disclosed per-link revenue split** would make both series clean and let the slope be read directly rather than inferred through a boundary.
4. **The disclosure itself** would replace §4's dial with the actual granularity of the series, turning the resolving-power surface into a statement about one pair of filings.

## 7. Boundary rules

- **No new anchors.** The single input is the concentration `04C` §11B.5 carries; `04C` §11B.5A's rule — do not infer a value from another borrower to complete the matrix — applies unchanged.
- **The channels are alternatives, not layers.** They are two hypotheses about one slope. Averaging them produces a slope that belongs to neither and, worse, makes the third verdict in §5 unreachable.
- **The verdict table is pre-registered.** It is stated before the data and may not be edited after a filing is read. A table that can be adjusted once the observation is in hand is a description, not a test.
- **No per-link claim.** Nothing here states any named company's revenue, coverage, headroom, or probability of breach, and no slope is asserted for any company.
- **No composite index.** The retention curve, the separation column and the resolving-power surface must never be netted into a score or multiplied into a multi-family signal.
- **No scenario switch, no S4, no evidence grade.** This cannot change `10`'s scenario relevance, cannot confirm S4, and cannot enter the frozen chapters.
- **D-grade labeling is mandatory** wherever an output is reused, under `04-research-transparency`'s hierarchy.

## 8. Integration

1. Re-run `scripts/recompute_channel_discriminator.py` when `19`'s channels, `04C`'s concentration anchor, or the observed series change.
2. **Supplies `19` §6's missing rule.** `19` states the difference in shape and names the test; this layer defines the observable, the statistic and the verdicts. `19` §6 and §8.3 carry a back-reference so a reader who meets the claim there is not left with a test that cannot be run.
3. `01A` adjudication: a confirmed step is a financing-family observation — recorded as one family among several, never as a standalone S4 confirmation, under `01A`'s existing state vocabulary.
4. **Proposed extension (not yet applied):** once a per-link revenue split is disclosed, the retention series becomes a facility-state field in `04C` §11B.7C's monetization bridge, and §4's resolution dial is replaced by the actual granularity. Until then `04C` is unchanged.

## Sources

No new external source. The single anchor is read through `19` and `04C` and carries its source identity there.

- The two transmission channels, the lockbox evidence, and the claim that the next filing tests them — [`19`](19-chain-concentration-amplification.md) §6, §8.3, §10.4
- Concentration `c = 0.77`, and the rule against inferring one borrower's value from another's — `04C` §11B.5, §11B.5A
- The propagation chain and the upstream concentration dial `c₁` — [`11`](11-financing-reflexivity-map.md) §2, and `19` §5
- Clearing-adjudication state vocabulary and the financing-family rule — [`01A`](01a-prospective-adjudication-ledger.md) §3, §4.2
- Evidence hierarchy and report-side calculation labeling — [Research Transparency](../publication/04-research-transparency.md)
