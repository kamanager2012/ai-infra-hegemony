# Research Transparency, Limitations, and Correction Policy

## 1. Research positioning

The report is authored by **James (kamanager2012)**.

The GitHub repository stores versioned research text, source indexes, evidence ledgers, and revision history. This traceability helps readers inspect how claims change over time, but it **does not constitute external peer review, audit assurance, a securities-research rating, or institutional endorsement**.

**Retrieval and revision cutoff: August 28, 2026.**

**Date interpretation:** the evidence cutoff and text-freeze dates are governance markers for the research snapshot. They define which facts may enter this edition and when general revision stops; the interval between those dates **does not represent the duration of the underlying research, evidence accumulation, or review process**.

---

## 2. External-review boundary

As of the research cutoff, the report does not claim to have received:

- independent peer review;
- audit assurance;
- a securities-research rating;
- legal opinion;
- formal institutional endorsement of all conclusions.

When a chapter cites an expert, company, regulator, or research institution, the citation supports only the corresponding fact or view. It does not imply endorsement of the report as a whole.

---

## 3. Evidence-selection principles

The report generally prioritizes:

1. statutory filings, regulator/government documents, and formal contracts;
2. company IR, official product materials, and technical documentation;
3. high-quality institutional and academic research;
4. sell-side, supply-chain, and media estimates;
5. report-side calculations, sensitivities, and scenarios.

Source quality and claim identity are handled separately.

For example:

- an observed financial figure in a 10-Q may enter the **Fact** layer;
- company guidance must retain its forward-looking identity;
- institutional forecasts must retain the institution name and forecast window;
- report-side calculations must state assumptions and denominators;
- a scenario does not become fact because its arithmetic is precise.

---

## 4. Structural limitations of public data

Many variables that matter most in AI infrastructure are not publicly disclosed, including:

- customer-level wafer allocation;
- HBM customer mix;
- actual CoWoS allocation;
- process yield;
- private contract pricing;
- cluster utilization;
- workload-level profitability;
- supplier-level splits of future capacity reservations.

The report therefore follows this rule:

> **Public data failing to confirm something does not prove that it does not exist; but a claim without sufficient public evidence cannot be written as an observed fact.**

Public evidence also contains structural biases:

- companies disclose selectively;
- disclosure depth differs across countries and firms;
- institutional/supply-chain research may contain unpublished assumptions;
- fast-moving industries create publication lag;
- the same variable can appear inconsistent when measured by shipment, revenue, capacity, bits, wafers, or other denominators.

---

## 5. What the report does not infer directly from public data

Unless sufficiently direct evidence exists, the report does not infer:

- revenue share → wafer share;
- platform revenue mix → customer allocation;
- HBM demand share → actual packaging allocation;
- contracted / secured capacity → energized / utilized AI load;
- IT-GW → generation GW;
- company-wide CapEx → AI-specific hardware CapEx;
- model-training compute → full corporate R&D cost;
- occupational exposure → unemployment rate;
- conventional DRAM / NAND capability → frontier HBM closure;
- production-grade substitution → autonomous frontier closure;
- foundry revenue share → frontier-AI system capability.

These boundaries are constraints on the causal analysis itself.

---

## 6. Counterevidence and uncertainty

A research conclusion is useful only if it can accommodate counterevidence.

Every strong judgment should therefore answer:

1. what the current evidence supports;
2. what the current evidence does not support;
3. which alternative explanations remain plausible;
4. which future facts would force the judgment to be downgraded or rewritten.

For example, an "advanced packaging remains a growth constraint" judgment must weaken if supply becomes sustainably abundant and lead times fall. A "system-stack concentration remains strong" judgment must weaken if large production workloads migrate to multiple alternative stacks at low switching cost.

---

## 7. Correction policy

When a high-impact factual error is found, the correction logic is:

1. return to the original source;
2. identify whether the error concerns the fact itself, denominator, time window, forecast/actual identity, translation, or calculation;
3. correct the factual statement;
4. review mechanisms, scenarios, and conclusions that depend on it;
5. preserve a traceable revision history.

The report does not use "the long-run thesis still holds" as a reason to ignore a fact that has been contradicted by evidence.

---

## 8. Time boundary

The current research cross-section includes information that could be obtained and verified **on or before August 28, 2026**.

Facts that appear after the research cutoff are new research inputs. They may strengthen, weaken, or overturn current judgments, but they should not be backdated into the August 28, 2026 evidence set or automatically inserted into the frozen formal text. They may enter a new research snapshot only if the formal-text freeze is explicitly reopened.

**Post-freeze correction rule for pre-cutoff sources:** if a source or fact was already publicly available **on or before August 28, 2026**, but is re-retrieved or re-verified during an August 29 freeze correction, it may be used to correct or strengthen the same August 28 evidence snapshot only if:

- no fact that first occurred after August 28 is introduced;
- the source publication date / observation window remains within the cutoff;
- the evidence ledger records the real access / correction date rather than backdating it;
- Git history preserves the actual post-freeze correction;
- the correction is not used as a pretext to strengthen an unrelated future scenario.

The **evidence-event/source-availability cutoff** and the **post-freeze verification date** must therefore be recorded separately.

### 8A. August 29, 2026 material-correction pass

The formal text was **explicitly reopened once on August 29, 2026** to correct already identified material research issues, not for general expansion. The pass covered:

- end-system / non-AI reader framing and residual-capacity exposure;
- China frontier parallel-stack Production-Grade Gate language;
- the “not yet empirically calibrated” identity of the verified-workflow criterion;
- public-proxy S1–S4 monitoring and the end-system dashboard;
- pre-cutoff source supplementation and evidence boundaries.

The correction pass **did not add a fifth scenario, redefine S1–S4, promote S2 into S3, or backdate facts that first occurred after August 28 into the current evidence snapshot**.

The formal text was refrozen after this material-correction pass.

### 8B. August 29, 2026 Developer Distribution material-event supplement

On August 29, 2026, the formal text was **reopened in a narrowly scoped second pass** to incorporate a material event that occurred inside the existing evidence cutoff: the August 27 Reuters report, citing The Information, concerning a reported NVIDIA / Hugging Face acquisition.

The pass was limited to:

- Ch02 NVIDIA system-stack / platform-power boundaries;
- Ch18 antitrust / vertical integration;
- the competitive-evidence matrix;
- the core evidence ledger / source index;
- the Phase II Developer Distribution Chokepoint validation layer.

Governance boundaries:

- transaction status remains **reported transaction**, not completed acquisition;
- the media transaction report remains C-grade while Hugging Face platform-function facts are supported separately by A-grade first-party documentation;
- Hugging Face ownership is not treated as ownership of open-model IP;
- potential vertical foreclosure is not treated as realized self-preferencing or completed software monopoly;
- the S1–S4 definitions and current S2 baseline judgment are unchanged.

After this targeted supplement, the formal text was refrozen again.

### 8C. August 30, 2026 definition-level clearing and optionality correction

On August 30, 2026, the formal text was reopened only to correct **definition-level inconsistencies** identified by Phase II validation.

First, the historical clearing replay showed that Accounting is a high-value confirmation / severity channel but **not a mandatory gate** for systemic capital clearing. Financing-led or real-economy clearing can be confirmed before qualifying impairment / write-down evidence appears, provided cross-signal confirmation and cross-actor / cross-layer causal breadth are strong enough.

Second, the decision-invariant falsification pass showed that continuously maintaining a production-like second path is **not a universal hard invariant**. The durable rule is to price executable optionality explicitly and maintain a second path only when continuity / bargaining / recovery value exceeds carrying cost.

The correction was limited to the affected definitions / strategy language in:
- Ch01 — Executive Summary;
- Ch19 — CapEx Supercycle;
- Ch22 — Depreciation Wall;
- Ch24 — Capital Clearing;
- Ch29 — Monitoring Framework;
- Ch30 — S1–S4 Scenarios;
- Ch31 — Strategic Optionality;
- Ch32 — Master Judgment;
- corresponding publication-status metadata.

The pass did **not** change:
- the August 28, 2026 evidence cutoff;
- the current S2 baseline judgment;
- the four-scenario taxonomy;
- any pre-cutoff factual observation;
- the requirement for broad, persistent, causally independent confirmation before S4 is upgraded.

The formal text was refrozen after this definition-level correction.

### 8D. August 30, 2026 bilingual Master-Judgment parity correction

A subsequent bilingual parity audit found that the Chinese Chapter 32 opening summarized the master judgment in **eight points**, while the English Chapter 32 contained only seven because the end-system / residual-capacity judgment had been omitted from the English opening sequence.

The English Chapter 32 was corrected to restore that missing third point and renumber the remaining judgments to eight. This was a **translation / analytical-parity repair only**:
- no new evidence was added;
- no Chinese source-of-truth claim was changed;
- the August 28 evidence cutoff remained unchanged;
- the S2 baseline judgment and S1–S4 taxonomy remained unchanged.

The formal text was refrozen again after this bilingual-parity repair.

---


## 9. External-use boundary

This report is intended for industry research and information exchange. It does not constitute:

- investment advice;
- a securities rating;
- legal advice;
- an audit opinion;
- a guaranteed forecast.

Readers should keep the following identities separate:

> **Fact / Company Guidance / Institutional Estimate / Report Calculation / Scenario**

The objective is not to eliminate uncertainty. It is to make the sources of uncertainty, the strength of evidence, and the conditions that could change the conclusions explicit.
