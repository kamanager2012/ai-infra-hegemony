# Phase II · Demand-Side Reflexivity Layer v0.1

> **Status:** Research-side validation layer; not part of the frozen 32-chapter formal report, and does not change the formal 2026-08-28 evidence cutoff.  
> **Purpose:** make the demand-side counterpart of financing reflexivity explicit — whether AI-driven labor-income compression can reduce the final demand that ultimately pays for AI infrastructure, and which observables would show that channel before it reaches the five existing clearing-signal families.  
> **External calibration reference:** Citrini Research / Alap Shah, *The 2028 Global Intelligence Crisis* (2026-02) — a self-labeled scenario (“a scenario, not a prediction”) — used here only as a scenario-shape input, together with its published rebuttals. This file does not restate, reproduce, or adopt that essay's numbers; everything below is the report's own conditional construction for 2026–2036.  
> **Chinese translation (derived):** [14-demand-side-reflexivity.zh.md](14-demand-side-reflexivity.zh.md)

## 0. Ownership contract v0.1

This file owns:

- the **demand-side reflexivity loop** (labor income → consumption → enterprise cash generation → AI monetization → capital clearing);
- the boundary between task-level labor evidence (owned by `07`) and aggregate-demand transmission (owned here);
- demand-side state variables and their clocks;
- the demand-leg integration rule for S4 evidence.

It does **not** own: task / workflow-level labor evidence (`07`), workflow cost-and-value units (`03`), financing structure and financing reflexivity (`11`, `04A`–`04D`), scenario aggregation (`10`), or live clearing adjudication (`01A`).

**Why a new owner rather than an existing layer.** The formal report already allows S4 to be confirmed by “real-economy clearing” ahead of accounting impairment (Ch24 §9, Ch29 §10, Ch30 §5, Ch32 §9). But no existing layer owns aggregate-demand-side observables: `07`'s labor chain terminates at employment / wage outcome and does not return to demand; `03` owns workflow-level verification and cost; `04`/`11` own the supply and structure of financing, not household income or consumption; `10` aggregates states but owns no facts. Without this file the S4 demand leg has a rule but no variables.

## 1. The loop the formal chain does not carry

The formal demand-side closure chain (Ch32 §10) is:

> Physical Infrastructure → System Delivery → Workflow Economics → Verified Output → Adoption / Cash Flow → Utilization → Capital Reinvestment

In that chain, “Adoption / Cash Flow” is an input: the report asks whether enterprises will pay for verified workflow output, and monitors whether capital formation is validated by utilization and cash generation.

The demand-side loop makes part of that input an **output** of the labor market:

```text
        AI adoption / task substitution
                    │
                    ▼
              employment & labor income
                    │
                    ▼
               consumption ──────────────► enterprise revenue
                    │                              │
                    ▼                              ▼
            household credit          AI budgets / monetization
                    │                              │
                    └──────────► capital clearing ◄┘
```

Two properties distinguish this loop from financing reflexivity (`11`):

1. **It attacks the demand leg, not the funding leg.** Supplier support, guarantees, and third-party capital can extend the clock while monetization is weak; household-income compression reduces both the ability to pay and the willingness to expand at the same time.
2. **Its clocks are long and stacked.** The formal report's existing clearing families are largely observable quarterly (guidance, clearing prices, spreads). The loop's first leg (hiring) is observable in months; its later legs (wages, consumption, credit, fiscal) accumulate over years. A ten-year window can carry the full sequence, but the sequence is not evidence of itself at any single point.

## 2. The 2026 baseline: a conditional channel, not the base case

The report's existing labor evidence already fixes the starting state, and this file reuses it rather than re-deriving it:

- **No economy-wide displacement is observed.** The Stanford / ADP payroll evidence recorded in `07` §2.2A shows employment among workers aged 22–25 in highly AI-exposed occupations about 19% below the path of less-exposed peers, operating primarily through **reduced hiring rather than increased separations**, with the authors labeling the result descriptive, not causal.
- **Adoption is not displacement.** The Census BTOS evidence in `07` §2.2B: about 18% of firms used AI in at least one business function, about 66% of adopters mainly reported task augmentation, and employment reductions were reported by only about 2% of firms.
- **Executives report larger expected than realized effects.** The cross-country survey in `07` §2.2C: roughly 69% of firms actively use AI, while more than 80% report no employment or productivity impact over the previous three years.
- **Exposure is not outcome.** ILO and IMF exposure measures (Ch25 §2) cannot be converted into unemployment rates.

Therefore, as of the 2026-08-28 cutoff, **gate G1 below is not open**; what exists is a hiring-pipeline signal concentrated in early-career, high-exposure occupations. This file treats the full loop as a conditional 2026–2036 channel, not as the current state or a forecast.

## 3. Gates the loop must pass

Each gate can stop the loop independently. None is a threshold with a fixed number; each is a state to observe.

**G1 — Substitution depth.** AI substitutes verified work at a pace that outruns the creation of new tasks and categories. Owned upstream by `03`; this file consumes, not re-derives, that state.

**G2 — Income incidence.** Which cohorts lose income, and how much of aggregate consumption they carry. A displacement that lands on low-consumption-propensity cohorts is a different demand event than one that lands on high-propensity cohorts. The commonly repeated claim that the top income deciles drive a disproportionate share of spending is a **scenario assumption here, not a fact**, until stated with its own same-denominator source.

**G3 — Credit buffers.** Household debt service and delinquency states define the lag between income loss and demand loss. Buffers turn a flow shock into a stock problem with a delay; depleted buffers transmit within quarters.

**G4 — Price versus margin pass-through.** Whether AI cost savings arrive as price declines that expand volume (the `02` elasticity question: cheaper intelligence can grow total demand) or as retained margin plus headcount reduction (demand-compressing). This gate determines whether the loop's own cost savings offset its demand destruction.

**G5 — Replacement demand and policy.** New categories of work, public-sector absorption, transfers, and tax design are the loop-closing variables. They are scenario variables until legislated and observed; proposals and political conflict are not evidence.

**G6 — Clock stacking.** Hiring (months) → wages (1–3 years) → consumption (immediate once income falls, but income falls slowly) → credit (1–3 years after sustained income loss) → fiscal (after the tax base moves). The loop's severity depends on whether earlier legs keep moving while later legs have not yet responded.

## 4. State variables and clocks

Public proxies for the demand leg. All are research-side; none replaces a formal-report fact, and none may be double-counted with `04`/`11` (see §5).

| Variable | Public proxy | Clock | What it updates | What it cannot prove |
|---|---|---|---|---|
| Labor income level | BLS Employment Cost Index / average hourly earnings (FRED `ECIALLCIV`) | Monthly–quarterly | G2, G4 | Not cohort-specific; composition shifts can mask cohort losses |
| Hiring / separations | JOLTS openings, quits, layoffs (FRED `JTSJOL`); age-occupation payroll panels as in `07` | Monthly | G1, G6 | Openings ≠ realized hiring; stock measures lag |
| Household debt service | NY Fed Household Debt and Credit Report; FRED `TDSP` | Quarterly | G3 | Aggregate; composition and refinancing terms matter |
| Delinquency states | NY Fed HHDC delinquency transition rates | Quarterly | G3, G6 | Early-stage flows are noisy; forbearance can suppress observed stress |
| Consumption | BEA Personal Consumption Expenditures; Census retail sales | Monthly–quarterly | G2, G5 | Aggregates cannot attribute cause to AI |
| Consumer-linked enterprise revenue | Card-network and intermediation volumes; seat- or consumption-based software disclosures | Quarterly | G4, G5 | C-grade unless first-party; industry structure changes confound |
| AI monetization quality | `04B` / `04D` panels (link only — not owned here) | Quarterly | S4 financing leg | Do not count twice with financing evidence |
| Fiscal position | Receipts versus transfers, automatic stabilizers | Quarterly–annual | G5 | Proposals are scenario variables, not observations |

**Anti-overreach rules.** No exposure→unemployment arithmetic. No “output without income” residual computed from different-denominator accounts. No single-quarter trigger. No promotion of institutional or media estimates into first-party facts.

## 5. Interaction with S1–S4, and double-counting rules

- **Demand-side compression is not automatically S4.** If G4 resolves toward price pass-through with volume expansion, cheaper intelligence can raise total demand — an S1-compatible outcome. If compression is slow and concentrated, S2/S3 can persist while the loop builds underneath.
- **What demand-side evidence can contribute to S4.** It can supply or reinforce the **real-economy leg** — weakening enterprise cash generation and monetization quality — but it cannot alone confirm S4, which still requires multiple causal-independent families across actors and layers (Ch24 §9, Ch30 §5).
- **Double-counting rule.** A single underlying fact updates either the financing family (`04`/`11`) or the demand family (this file), not both, unless it is genuinely two-sided evidence (for example, a consumer-credit deterioration that is simultaneously a financing-quality observation). The `11` anti-double-counting discipline applies unchanged.
- **Interaction with financing reflexivity.** `11`'s reflexivity condition is supplier support rising while utilization, monetization, independent risk appetite, and clearing weaken. A demand-side loop would satisfy the “monetization weakening” clause from a different direction; the two must be recorded as separate contributions to the same family, not as two confirmations.

## 6. Conditional 2026–2036 milestones

Aligned with the Ch28 phase structure; each row is `condition → milestone → contrary signal`, not a calendar forecast.

| Phase | Condition that would open the loop | Milestone to observe | Contrary signal |
|---|---|---|---|
| I · 2026–2027 | Early-career hiring-pipeline divergence spreads to **separations**, or beyond technology occupations | Layoff and quits data show displacement, not only reduced entry | Separations stable; hiring broadens; augmentation share stays dominant |
| II · 2028–2030 | Wage growth and cohort income compress beyond entry level; consumption decelerates with income | Consumer-linked enterprise revenue weakens while AI budgets keep growing (the OpEx-substitution shape) | AI savings arrive as price declines with expanding volumes; new categories absorb cohorts |
| III · 2031–2033 | Household credit deterioration becomes flow, not stock; fiscal receipts weaken against transfers | Household debt-service and delinquency states deteriorate on trend, not in a single shock | Policy closes the loop in time; productivity-driven demand expansion outruns compression |
| IV · 2034–2036 | The compression either equilibrates into a new structure or persists | Labor share and consumption stabilize at a new level, or continue declining | Wage share stabilizes; reallocation dominates; demand for verified output keeps growing |

**Explicitly out of scope:** any year-stamped unemployment rate, any equity-index level, any “crisis by 2028” claim. The formal report's timeline discipline (Ch28 §1) applies unchanged to this layer.

## 7. Falsification conditions

The loop is weakened or closed by any of the following, each observable in the panels above:

1. **Separations stay flat** through Phase II while AI adoption deepens — adoption without displacement.
2. **Wage growth and consumption remain stable** while `03`-type verified workflow substitution scales — the substitution does not reach income.
3. **Price pass-through dominates** (G4): AI cost savings appear as price declines and volume expansion rather than margin retention plus headcount cuts.
4. **New-task creation** absorbs displaced cohorts at observable scale (hiring composition, not just aggregate employment).
5. **Policy closes the loop** (G5) in time: transfers, tax design, or public absorption offset private income loss.
6. **Enterprise AI budgets keep growing** faster than consumer-linked revenue falls — the monetization base is not, in fact, consumer-income-dependent in the relevant window.

## 8. Boundary rules

- Scenario ≠ prediction. The external reference in the header is a scenario shape with published rebuttals; this file neither adopts nor argues its numbers.
- Every number in this file must be traceable to a graded source already used by the report, or to the panels in §4; no new numeric identities are created here.
- Observations dated after 2026-08-28 are research-side only and cannot enter the frozen chapters without an explicit reopen (Phase II freeze boundary, `README`).
- No redistribution, political, or moral argument is made here; G5 is recorded as a scenario variable because it changes demand arithmetic, not because it is endorsed.

## 9. Integration rule

1. Record demand-side states and clocks in this file and, when they change, update the corresponding row rather than appending narrative.
2. **Proposed extension (not yet applied):** Dashboard I's demand-quality family (`10`, Ch29 §10) could add the §4 rows as a tagged sub-list with their clocks. That is a formal-text-adjacent change and requires the owner's adjudication like any other Phase II result; until then, `10` is unchanged.
3. If demand-side evidence and financing-side evidence deteriorate together, the `01A` adjudication ledger records them as separate family contributions — never multiplied into one index.

## Sources

- Brynjolfsson, E.; Chandar, B.; Chen, R., *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence*, Stanford Digital Economy Lab, revised 2026-08-12 (ADP payroll data through June 2026; descriptive, not causal): https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/
- U.S. Census Bureau, Business Trends and Outlook Survey (BTOS), experimental data product: https://www.census.gov/data/experimental-data-products/business-trends-and-outlook-survey.html
- Brynjolfsson, E.; Li, D.; Raymond, L., *Generative AI at Work*, NBER Working Paper 31161: https://www.nber.org/papers/w31161
- METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- ILO, Gmyrek et al., *Generative AI and Jobs: A Refined Global Index of Occupational Exposure*, Working Paper 140, May 2025: https://www.ilo.org/sites/default/files/2025-05/WP140_web.pdf
- IMF, *Gen-AI: Artificial Intelligence and the Future of Work*, Staff Discussion Note SDN/2024/001: https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf
- Federal Reserve Bank of New York, *Household Debt and Credit Report*: https://www.newyorkfed.org/microeconomics/hhdc.html
- Household Debt Service Ratio (FRED series TDSP): https://fred.stlouisfed.org/series/TDSP
- Employment Cost Index, total compensation, civilian (FRED series ECIALLCIV): https://fred.stlouisfed.org/series/ECIALLCIV
- Job Openings: Total Nonfarm (FRED series JTSJOL): https://fred.stlouisfed.org/series/JTSJOL
- U.S. Bureau of Economic Analysis, Personal Consumption Expenditures: https://www.bea.gov/data/consumer-spending/main
- Citrini Research / A. Shah, *The 2028 Global Intelligence Crisis*, 2026-02 (scenario, not prediction; calibration reference only): https://www.citriniresearch.com/p/2028gic
- Citadel Securities rebuttal, as reported: https://fortune.com/2026/02/26/citadel-demolishes-viral-ai-doom-essay-citrini-macro-fundamentals-engels-pause/
- *The 2028 Global Intelligence Renaissance* (contrary scenario): https://blog.neuralnexus.press/p/the-2028-global-intelligence-renaissance
- J. Daly, *The Convergence Problem: Rethinking the 2028 Global Intelligence Crisis*: https://www.jeremydaly.com/the-convergence-problem/
