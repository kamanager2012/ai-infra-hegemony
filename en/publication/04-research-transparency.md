# Research Transparency, Limitations, and Correction Policy

## 1. Research positioning

The report is authored by **James (kamanager2012)**.

The GitHub repository stores versioned research text, source indexes, evidence ledgers, and revision history. This traceability helps readers inspect how claims change over time, but it **does not constitute external peer review, audit assurance, a securities-research rating, or institutional endorsement**.

**Retrieval and revision cutoff: August 28, 2026.**

**Date interpretation:** the **evidence cutoff** determines which observed facts and external materials may support this edition. The **edition revision date** records when the current text was last materially edited. Detailed correction history remains available below and in Git history; these dates do not imply external review or audit status.

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

### 8A. Material revisions after the evidence cutoff

The evidence cutoff and the revision date are separate controls.

After August 28, 2026, the report was edited only when one of the following conditions applied:

- a pre-cutoff fact, denominator, evidence identity, translation, or calculation required correction;
- a definition-level inconsistency affected scenario classification or falsification;
- bilingual analytical parity required repair;
- reader-facing structure required editorial reorganization without changing the evidence set.

These revisions did **not** authorize post-cutoff events to be backdated into the August 28 evidence snapshot.

Several material corrections made during August 29–31 remain analytically relevant and are therefore disclosed here in compressed form:

1. **End-system / residual-capacity framing was strengthened.** Consumer electronics, game consoles, industrial systems, and other non-AI end markets are analyzed through shared-resource exposure, Quantity Assurance, and Non-AI Residual Capacity rather than a blanket “AI displaces everything” claim.
2. **China's frontier assessment was separated into Production-Grade Parallel Stack and Autonomous Frontier Closure.** A system that can run production workloads is not automatically an autonomous multi-generation frontier stack.
3. **Capital-clearing decision logic was corrected.** Accounting impairment is a high-value confirmation / severity channel, not a mandatory gate. Direct falsification of a mechanism cannot be ignored merely because system-level cross-signal breadth has not yet accumulated.
4. **Developer-distribution risk was added as a conditional mechanism.** The August 27 Reuters report, citing The Information, concerning a reported NVIDIA / Hugging Face agreement remains C-grade transaction evidence and is not treated as a completed acquisition or realized software foreclosure.
5. **Strategy optionality language was corrected.** Chapter 31 no longer treats a continuously maintained executable second production path as universally optimal. The hard rule is to price executable optionality / resilience against carrying cost; maintaining a second production path remains conditional on continuity, bargaining, recovery, and switching value exceeding that cost.
6. **Physical-AI evidence boundaries were repaired.** Chapter 15 now records pre-cutoff production evidence from BMW/Figure 02, Amazon DeepFleet, and GXO/Digit. The correction does not claim broad humanoid economics are closed; it distinguishes narrow production-grade deployment from the still-missing intervention, uptime, safety, TCO, and multi-site fleet-economics evidence.
7. **English-first canonical workflow and translation parity were formalized.** English is the sole canonical analytical layer; Chinese is the professional translation of that text, not an independent analytical edition. Claims, section order, evidence grades, denominators, mechanisms, scenario identities, and falsification boundaries must remain equivalent.

The public rule is therefore simple:

> **Correct the research record when the evidence or definition is wrong; do not turn editorial history into a second research narrative.**

Detailed file-by-file chronology remains available through repository history and research-side validation materials rather than being repeated in the reader-facing report.

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
