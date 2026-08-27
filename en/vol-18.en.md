# Volume 18: Research Methodology and Evidence Architecture

> **This volume does not maintain a second evidence system.** The highest-order rules for the English edition are [Research Methodology and Evidence Grading](研究方法与证据分级.en.md), [Core Evidence Ledger](核心证据台账.en.md), [Core Source Index](核心参考文献索引.en.md), [Core Concepts and Model Index](核心概念与模型索引.en.md), and [Core Hypothesis Matrix](核心假设矩阵.en.md).

Chinese original: [vol-18.md](../vol-18.md)

## 1. What this volume answers

The most dangerous error in a forty-volume report is not a small numerical miss. It is writing different kinds of claims as if they were the same kind of fact.

Common failure modes include treating a company disclosure and an institutional forecast as equivalent; turning revenue share into wafer share; treating contracted MW as already energized load; presenting engineering geometry as disclosed fab capacity; writing a stress test as if it had already happened; using a 2030/2036 scenario to infer a 2026 fact; or repeating one secondary estimate across many chapters until it looks like multi-source confirmation.

This chapter therefore asks three methodological questions:

1. Does a claim belong to **F / H / M / S / X**?
2. Is its evidence **A / B / C / D**?
3. Is the causal chain from fact to future outcome closed and falsifiable?

## 2. The common structure: F → H → M → S → X

### F — Fact

An observed and checkable fact. It must preserve time, accounting or engineering scope, denominator, source, the distinction between guidance and actuals, and the distinction between an estimate and a company disclosure.

### H — Hypothesis

A future input used in scenario analysis. A hypothesis may be aggressive, but it must remain compatible with known physical, financial, and industrial constraints and must state what observable change would invalidate it.

### M — Mechanism

A mechanism explains why fact A can push the system toward result B. The common mechanism set includes Super-buyer Effect, AI Resource Gravity, Capacity Preemption, Advanced HPC Incremental Capacity Capture, Non-AI Residual Capacity, Scarcity-layer Value Capture, Installed-base Flywheel, Rolling Bottleneck Cascade, Cloud System-Stack Substitution, Anchor Compute Buyer Effect, AI Software Unit Economics, and Task-to-Job Translation.

### S — Scenario

A scenario is the state produced when a defined set of hypotheses activates a defined set of mechanisms. The formal endgame uses:

- **S1 — Competitive Expansion**
- **S2 — Baseline Concentration**
- **S3 — Resource Hegemony**
- **S4 — Capital Hard Landing**

The early 40% / 30% / 15% / 15% discussion weights are not part of the formal model.

### X — Falsification

Every strong claim must answer: **what evidence would force this conclusion to weaken, reverse, or be rewritten?**

A claim without a reverse signal is rhetoric, not a research proposition.

## 3. Evidence grades

### A — First-party confirmation

Company filings, formal earnings materials, official product specifications, contracts, regulatory documents, court records, and other first-party disclosures.

### B — High-quality independent research

OECD, IEA, ILO, Stanford HAI, academic research, industry associations, TrendForce, and comparable institutions with explicit scope and methodology.

### C — Sell-side / supply-chain estimate

Broker research, channel checks, media-reported capacity allocation, customer shares, prices, and lead times. Useful for scenario anchoring but not issuer disclosure.

### D — Report hypothesis or model output

Stress tests, scenario parameters, geometry calculations, counterfactual outputs, and other report-generated values.

Evidence grade does not automatically determine importance. A B-grade institutional estimate may be strategically important, but it must remain labeled as an estimate.

## 4. Dimensional discipline

The report keeps the following quantities separate:

- revenue share;
- wafer share;
- node revenue share;
- advanced-packaging share;
- customer allocation;
- contracted power;
- energized load;
- utilized load;
- company-wide CapEx;
- AI-specific hardware spend;
- seller revenue;
- buyer depreciation.

A valid model may connect two quantities only through an explicit conversion or causal mechanism. Repetition is not conversion.

## 5. The two most important quantitative identities

### 5.1 Non-AI Residual Capacity

```text
NonAI_Residual(t)
= Effective_Supply(t)
- AI_Absorption(t)
- Other_Priority_Demand(t)
```

This prevents the report from equating total supply growth with recovery for smartphones, PCs, general-purpose servers, or other non-AI markets.

### 5.2 Advanced HPC Incremental Capacity Capture Ratio

```text
AHICR
= leading platform's incremental advanced-HPC capacity
/ total incremental advanced-HPC capacity
```

The report uses 50% / 60% / 70% / 80% as stress levels. They are not current observed TSMC customer shares.

## 6. Scenario discipline

A scenario must specify:

- which H variables are active;
- which mechanisms transmit them;
- which observable indicators would confirm movement toward the state;
- which reverse signals would falsify it.

The report does not assign new probabilities chapter by chapter. Volumes 10, 15, 30, 37, and 40 must all use the same S1–S4 framework.

## 7. Source discipline

High-impact claims should be traceable through the [Core Evidence Ledger](核心证据台账.en.md) and [Core Source Index](核心参考文献索引.en.md). Chapter-level citations provide detail; the central indexes prevent cross-volume drift.

Rules:

- later first-party disclosure overrides an older secondary estimate;
- guidance remains guidance until actual results are published;
- contracted MW remains separate from energized MW;
- revenue share remains separate from physical allocation;
- one report-generated coefficient cannot be repeated until it looks official;
- legal inquiry, complaint, decision, remedy, and penalty are separate states.

## 8. Publication rule

The English edition is not a loose translation layer. It must preserve the same analytical ontology as the Chinese source-of-truth edition. Where older English chapters contain legacy wording, the current F/H/M/S/X framework and central English evidence files govern.

The purpose of this methodology is not to make the report cautious for its own sake. It is to make strong conclusions **traceable, updateable, and falsifiable**.
