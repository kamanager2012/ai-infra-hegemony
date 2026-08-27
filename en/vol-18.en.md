# Volume 18: Research method and evidence architecture

> **This volume does not maintain a second evidence system.** The highest-order rules for the monograph are the root-level [Research method and evidence grading](../研究方法与证据分级.md), [Core evidence ledger](../核心证据台账.md), [Core reference index](../核心参考文献索引.md), [Core concepts and model index](../核心概念与模型索引.md), and [Core hypothesis matrix](../核心假设矩阵.md). This chapter only explains how those rules are applied to industry analysis.

The master judgment owns conclusions. This volume owns the ruler. If a number, mechanism, or future claim in this chapter conflicts with the central method or evidence ledger, **the central files govern**.

## 1. What this volume answers

The most dangerous error in a forty-volume report is not a small numerical miss. It is writing different kinds of claims as if they were the same kind of fact.

Common failure modes include:
- treating a company disclosure and an institutional forecast as equivalent;
- turning revenue share into wafer share;
- treating contracted MW as already energized load;
- presenting engineering geometry as disclosed fab capacity;
- writing a stress test as if it had already happened;
- using a 2030/2036 scenario to infer a 2026 fact;
- repeating one secondary estimate across many chapters until it looks like multi-source confirmation.

This chapter therefore asks only three methodological questions:

1. Does a claim belong to **F / H / M / S / X**?
2. Is its evidence **A / B / C / D**?
3. Is the causal chain from fact to future outcome closed and falsifiable?

## 2. The common structure: F → H → M → S → X

### F — Fact

An observed and checkable fact.

Typical fact-layer material:
- company filings, 10-Ks, 20-Fs, and formal earnings material;
- official product specifications;
- contracts, regulatory filings, and court records;
- company-disclosed revenue, capacity, and customer concentration;
- high-quality institutional historical statistics, while retaining their institutional identity.

A fact must preserve:
- time;
- accounting or engineering scope;
- denominator;
- source;
- the distinction between guidance and actuals;
- the distinction between an estimate and a company disclosure.

### H — Hypothesis

A future input used in scenario analysis.

Examples:
- AI-demand growth;
- effective advanced-node supply growth;
- 50% / 60% / 70% / 80% AHICR stress levels;
- CoWoS expansion;
- future HBM wafer-supply trade ratios;
- actual grid-interconnection progress;
- token-price decline;
- whether long-duration model-company compute commitments continue to expand.

A hypothesis may be aggressive, but it must say:
1. why it is compatible with known physical, financial, and industrial constraints; and
2. what observable change would invalidate it.

### M — Mechanism

A mechanism explains why fact A can push the system toward result B.

The report's common mechanism set includes:
- Super-buyer Effect;
- AI Resource Gravity;
- Capacity Preemption;
- Advanced HPC Incremental Capacity Capture;
- Non-AI Residual Capacity;
- Scarcity-layer Value Capture;
- Installed-base Flywheel;
- Rolling Bottleneck Cascade;
- Cloud System-Stack Substitution;
- Anchor Compute Buyer Effect;
- AI Software Unit Economics;
- Task-to-Job Translation Layer.

A mechanism must be expressible as a causal chain, not as a slogan.

### S — Scenario

A scenario is the state produced when a defined set of hypotheses activates a defined set of mechanisms.

The formal endgame uses the four states in the [Core hypothesis matrix](../核心假设矩阵.md):
- **S1 — Competitive Expansion**
- **S2 — Baseline Concentration**
- **S3 — Resource Hegemony**
- **S4 — Capital Hard Landing**

The early 40% / 30% / 15% / 15% weights no longer serve as the formal model.

### X — Falsification

Every strong claim must answer:

> What observable event would force this report to reduce, reject, or rewrite the claim?

Examples:
- a second frontier AI foundry/packaging source becomes genuinely scalable and substitutable;
- AI-demand growth remains below effective supply growth;
- HBM or advanced packaging ceases to be scarce;
- cloud system stacks achieve large-scale training and inference substitution at low migration cost;
- frontier compute no longer depends materially on the latest nodes;
- grid and power constraints are removed at scale and low cost;
- model-company capacity commitments are systematically reduced, rescheduled, or under-utilized.

A ten-year claim without a falsification condition is an opinion, not a formal scenario in this report.

## 3. The common evidence grades: A / B / C / D

The grades below are taken directly from the root method file.

### A — First-party confirmation

Company filings, 10-K/20-F, regulatory announcements, official product pages, government documents, formal contract disclosures, and court materials.

High-impact current examples include:
- NVIDIA FY27 Q2 actual financials;
- TSMC's formal statements that advanced packaging is tight and can limit customer growth;
- **Micron's first-party disclosure that HBM3E requires about 3× the wafer supply of DDR5 at the same node and bit capacity**;
- formal Stargate and Anthropic/AWS infrastructure commitments;
- formal contract/regulatory/SEC status for major power projects.

### B — High-quality independent research

OECD, IEA, academic research, industry associations, TrendForce, and similar institutions with explicit methods and sustained coverage.

Key example:
- **TrendForce's estimate that NVIDIA was the largest CoWoS-demand customer in 2025, at more than 60% of demand.**

B-grade evidence can anchor a scenario. It cannot be rewritten as "TSMC officially confirmed."

### C — Sell-side / supply-chain estimates

Broker research, channel checks, and media-reported customer allocations, specific capacity numbers, prices, and lead times.

Examples:
- specific annual CoWoS wafer-demand estimates by customer;
- undisclosed monthly capacity estimates;
- channel spot pricing;
- supply-chain customer-share tables.

C-grade evidence may inform stress tests but cannot masquerade as issuer disclosure.

### D — Report hypotheses and model outputs

This includes:
- **the 5.39 CoWoS-wafers-per-rack geometry estimate**;
- 50% / 60% / 70% / 80% AHICR stress levels;
- counterfactual crowding-out calculations;
- 2030/2036 scenario values;
- unverified BOM/MFU assumptions or fixed SaaS-margin endpoints.

**Unified correction: Micron HBM ≈3× is A; TrendForce CoWoS >60% is B; 5.39 is D. They must not be collapsed into one evidence grade.**

## 4. Macro-to-micro reasoning is one-way

The legal causal direction is:

```
historical cash flow / contracts / demand
→ physical objects purchased
→ constraints on those objects
→ allocation of scarce resources
→ incremental supply versus residual supply
→ revenue / cost / depreciation / profit effects
→ scenario state under explicit H variables
```

The reverse direction is forbidden:

```
2036 scenario
→ therefore this already happened in 2026
```

Examples of forbidden reverse inference:
- using a 2036 CoWoS forecast to infer current CoWoS capacity;
- using S3 to claim NVIDIA already holds 80% of TSMC N2;
- using a future hard-landing scenario to claim current CapEx is already a bubble;
- using algorithmic efficiency to claim HBM demand has already disappeared.

## 5. Five common dimensional errors

### 5.1 Revenue share ≠ wafer share ≠ leading-node share ≠ CoWoS share

A TSMC customer revenue share is a concentration indicator. It is not a direct conversion into N2 wafers or CoWoS wafers.

### 5.2 Total supply growth ≠ non-AI recovery

The report uses:

```
NonAI_Residual(t)
= Effective_Supply(t)
- AI_Absorption(t)
- Other_Priority_Demand(t)
```

Total supply can grow while Non-AI Residual Capacity still falls.

### 5.3 Contracted capacity ≠ planned capacity ≠ energized load ≠ annual utilization

Every MW/GW figure must identify which quantity it represents. A long-duration PPA is not automatically today's AI load.

### 5.4 Product specification × hypothetical quantity ≠ shipments

13.4 TB HBM and 17 TB LPDDR per rack are product specifications. Multiplying them by 10,000 racks gives a scenario demand number, not disclosed shipments.

### 5.5 Component-price inflation ≠ identical BOM inflation

Memory contract prices, channel spot prices, device BOMs, and retail prices have different denominators and cannot be mechanically converted into one another.

## 6. How the core models enter the report

### 6.1 AHICR applies only to incremental advanced HPC resources

```
AHICR
= Head_Player_Incremental_Advanced_HPC_Capacity
/ Total_Incremental_Advanced_HPC_Capacity
```

The 50%–80% levels are stress tests, not disclosed present shares.

### 6.2 Non-AI Residual Capacity subtracts priority absorption first

The research question is not simply whether capacity expands. It is who absorbs the expansion before non-AI industries receive the remainder.

### 6.3 Cloud System-Stack Substitution is not a one-chip contest

At minimum it must track:
- accelerator;
- HBM / packaging;
- scale-up / scale-out interconnect;
- compiler / runtime;
- rack / pod;
- real workloads and deployment scale.

Cloud system stacks can divert NVIDIA's platform profit while **simultaneously** competing with NVIDIA for advanced logic, HBM, packaging, and power. These effects are not contradictory.

### 6.4 Anchor Compute Buyer Effect means model companies are not only tenants

Long-duration model demand can increase financing certainty and shape the pace of cloud, chip, data-center, and power expansion. Rescheduling, under-utilization, or contraction can become leading signals for a hard landing.

### 6.5 AI Software Unit Economics replaces fixed SaaS endpoints

AI software must account for inference, retrieval/storage, tools/APIs, human review, and AI-specific cloud cost. The old "85% → 55%" margin path remains only a stress-test endpoint.

## 7. How to use negative evidence

"Not found in this document" proves only that **the document did not disclose it**.

Correct:
> The CXMT prospectus did not disclose an HBM product line.

Incorrect:
> CXMT has no HBM research anywhere.

Negative evidence is valuable because it blocks unsupported positive claims from entering the fact layer. It must not create a new absolute claim.

## 8. Scenario variables and falsification use the same system

Formal future work uses H1–H17 from the [Core hypothesis matrix](../核心假设矩阵.md), including:
- AI demand versus effective supply;
- AHICR;
- HBM / CoWoS;
- power and interconnection;
- cloud system-stack substitution;
- software migration cost;
- CapEx / depreciation / utilization;
- China's parallel-stack capability;
- regulation;
- **H17 — long-duration model-company compute commitments / Anchor Buyer Demand**.

The four scenarios are states produced by these variables, not belief labels.

## 9. Publication checklist

Before a chapter enters `main`, check at minimum:

1. Does every major number have a time, denominator, and scope?
2. Has a revenue share been silently converted into a physical share?
3. Has guidance been written as actual?
4. Has B/C evidence been promoted into A?
5. Has a D-grade model output been presented as company disclosure?
6. Has contracted MW been presented as energized MW?
7. Has product spec × hypothetical quantity been presented as shipments?
8. Are early uncalibrated probabilities still being used as the formal endgame?
9. Does every strong scenario state a falsification condition?
10. Does the chapter conflict with the [Core evidence ledger](../核心证据台账.md) or [Core hypothesis matrix](../核心假设矩阵.md)?

If there is a conflict, **the central ledger wins and the chapter must change**.

## 10. Where this volume stops

Volume 18 does not create another methodological asset. Its purpose is to ensure that the monograph uses one ruler:

**F → H → M → S → X**

and one evidence hierarchy:

**A first-party → B high-quality independent research → C sell-side/supply-chain → D report models and stress tests.**

Later chapters may add facts, update hypotheses, revise mechanisms, or recalculate scenarios. They may not invent a second evidence system.