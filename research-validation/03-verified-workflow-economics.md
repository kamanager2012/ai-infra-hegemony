# P0-3 · Verified Workflow Economics v0.2

> **Status:** Research-side validation; not part of the frozen 32-chapter formal report.  
> **Goal:** turn “cost per verified workflow outcome” from a conceptual statement into an auditable operating metric.

## 1. The unit of analysis

The report should not optimize:

- cost per token;
- cost per API call;
- cost per model response;
- cost per agent run;
- raw output volume.

The economically relevant denominator is:

> **Verified Successful Workflow Outcome (VSWO)**

A VSWO is a workflow result that satisfies a predefined acceptance rule and therefore counts as usable business output.

Examples:

- customer-support issue resolved without reopening within the verification window;
- code change merged after tests/review;
- invoice/document extraction accepted without material correction;
- research memo accepted against a factual/citation rubric;
- sales/operations action completed and accepted by the downstream system.

The acceptance rule must be specified **before** comparing AI and non-AI workflows.

---

## 2. Core metric

For workflow class (w):

```text
Cost_per_VSWO_w
=
Total_Cost_w
/
Verified_Successful_Outcomes_w
```

where:

```text
Total_Cost
=
Model / Inference Cost
+ Retrieval / Storage Cost
+ Tool / API Cost
+ Human Production Time Cost
+ Human Review Time Cost
+ Retry / Exception Cost
+ Failure Remediation Cost
+ Workflow Infrastructure / Observability Cost
```

The metric is deliberately broader than model spend.

A cheap model that creates more retries or review can have a **higher** cost per verified outcome.

---

## 3. Required companion metrics

Cost per VSWO cannot be interpreted alone.

Every benchmark should also report:

### 3.1 Verified success rate

```text
Verified Success Rate
=
Verified Successful Outcomes
/
Attempted Workflows
```

### 3.2 Human minutes per VSWO

```text
Human Minutes per VSWO
=
(Production Minutes + Review Minutes + Remediation Minutes)
/
Verified Successful Outcomes
```

### 3.3 Attempts per VSWO

```text
Attempts per VSWO
=
Total Attempts
/
Verified Successful Outcomes
```

### 3.4 Resource intensity per VSWO

```text
Resource Intensity per VSWO
=
Total AI Resource Consumption
/
Verified Successful Outcomes
```

Resource consumption may be recorded as:
- input/output tokens;
- model calls;
- GPU-seconds where available;
- tool calls;
- retrieval operations.

### 3.5 Cycle time

```text
Cycle Time per VSWO
=
End-to-end elapsed time
/
Verified Successful Outcomes
```

This separates “AI reduced labor minutes” from “AI reduced customer/business latency.”

---

## 4. Baseline-vs-AI comparison

For every workflow, compare:

```text
Baseline arm
vs.
AI-assisted / agentic arm
```

Primary effect:

```text
Economic Improvement
=
1 - Cost_per_VSWO_AI / Cost_per_VSWO_Baseline
```

A positive value means the AI workflow is cheaper per accepted outcome.

Also report:

```text
Human-Time Improvement
=
1 - Human_Minutes_per_VSWO_AI
    / Human_Minutes_per_VSWO_Baseline
```

and:

```text
Throughput Improvement
=
VSWO_per_Hour_AI
/
VSWO_per_Hour_Baseline
- 1
```

No workflow is allowed to claim “productivity improvement” if quality/acceptance thresholds were relaxed in the AI arm.

---

## 5. Quality floor and verification design

The word **verified** is the hard part.

Each workflow must define:

1. **Acceptance criterion** — what counts as successful?
2. **Verifier** — human reviewer, automated test, downstream business state, or a combination;
3. **Verification window** — immediate, 24h, 7d, etc.;
4. **Severity weighting** — whether a material error counts more than a cosmetic error;
5. **Reopen / rollback rule** — whether later failure reverses the original success;
6. **Blinding where possible** — reviewer should not know which arm produced the output.

### 5.1 Examples

**Coding**
- tests pass;
- reviewer accepts;
- change merges;
- no rollback / critical regression in the agreed window.

**Customer support**
- issue marked resolved;
- no reopen within the agreed window;
- quality/customer-satisfaction floor maintained.

**Document extraction**
- field-level accuracy above threshold;
- critical fields exact;
- accepted without manual correction beyond a defined tolerance.

**Research**
- factual claims pass source audit;
- citations support claim scope;
- no material hallucination;
- reviewer accepts deliverable.

---

## 6. Why existing empirical studies matter

### 6.1 Customer support — strong outcome-style evidence

Brynjolfsson, Li & Raymond studied the staggered rollout of a generative-AI assistant to **5,179 customer-support agents**.

The NBER version reports roughly **14% higher productivity**, measured as issues resolved per hour, with larger gains among less-experienced/lower-skilled workers.

This is valuable because the outcome is much closer to a business workflow than token usage.

But it still does not provide the full Cost_per_VSWO denominator because the published headline effect does not include:
- model/API cost;
- implementation cost;
- full review/remediation cost.

So it is an **outcome/throughput anchor**, not a complete workflow-unit-economics estimate.

### 6.2 Experienced software developers — negative control

METR randomized **246 real software tasks** from experienced open-source developers.

For early-2025 tools, AI access increased completion time by about **19%** in that setting.

This is crucial for report discipline:

> AI capability or benchmark strength does not guarantee lower cost per verified outcome in mature, context-heavy production work.

A valid workflow metric must be able to produce a **negative ROI result** when AI adds review/context overhead.

### 6.3 Coding quasi-experiment — positive but different estimand

A 2026 quasi-experiment around Ant Group’s CodeFuse rollout reports code output increasing by **over 50%**.

This should not be directly compared with METR as if one must be wrong:
- task populations differ;
- worker populations differ;
- output measures differ;
- experimental identification differs;
- “code output” is not necessarily “verified merged business outcome.”

This reinforces the need for a common VSWO denominator.

### 6.4 Anthropic Economic Index — useful primitives, incomplete economics

Anthropic’s 2026 Economic Index adds measures for:
- task complexity;
- autonomy;
- success;
- work/personal use;
- longer-running agentic tasks.

These are useful ingredients for workflow measurement.

But product-usage telemetry alone does not supply:
- customer labor cost;
- review cost;
- business value;
- accepted outcome count across firms.

Therefore it can improve the **measurement schema** without completing unit economics.

---

## 7. Minimum viable benchmark table

Every Phase II workflow case should eventually populate:

| Field | Baseline | AI-assisted |
|---|---:|---:|
| attempted workflows |  |  |
| verified successful outcomes |  |  |
| verified success rate |  |  |
| human production minutes |  |  |
| human review minutes |  |  |
| remediation minutes |  |  |
| model/inference cost | 0 or baseline |  |
| tool/API cost |  |  |
| infrastructure/observability cost |  |  |
| total cost |  |  |
| cost per VSWO |  |  |
| attempts per VSWO |  |  |
| cycle time per VSWO |  |  |
| quality/reopen metric |  |  |

Without enough fields to populate this table, the case cannot be called a full workflow-economics benchmark.

---

## 8. Evidence-completeness ledger v0.1

The purpose of this ledger is to stop treating every “AI productivity study” as if it already measures workflow economics.

### 8.1 Customer support — Brynjolfsson / Li / Raymond

Observed design:

- **5,179 agents** in the study population;
- roughly **1,300** received access during the staggered rollout;
- primary productivity measure: customer issues resolved per hour;
- average productivity gain: about **14%**;
- gains up to roughly **35%** among the lowest-skill / least-experienced group;
- customer-satisfaction / conversation-quality measures provide a quality floor.

Field coverage:

| VSWO field | Available? | Comment |
|---|---|---|
| attempted workflows | partial | customer interactions exist, but the public headline statistics do not expose a full attempt ledger |
| verified successful outcomes | **partial/strong** | resolved issues are close to an accepted business outcome |
| human time | **yes, indirectly** | issues per hour provides a labor-time denominator |
| quality floor | **yes** | customer satisfaction / conversation quality |
| model/inference cost | no | not sufficient for Cost/VSWO |
| implementation cost | no | not sufficient |
| review/remediation cost | no | not sufficient |
| reopen / later-failure window | incomplete | not a full VSWO persistence measure |
| business value | incomplete | throughput is measured; gross value is not fully attributed |

**Classification:** strong **workflow-outcome productivity anchor**, incomplete workflow-unit-economics benchmark.

### 8.2 Experienced open-source software — METR early-2025 RCT

Observed design:

- **16 experienced developers**;
- **246 real tasks** in mature repositories;
- developers averaged about five years of prior experience in those codebases;
- task-level random assignment to AI-allowed vs. AI-disallowed;
- early-2025 AI tools caused completion time to increase by about **19%**;
- METR's later methodological update reports an early-study confidence interval of roughly **+2% to +39% slowdown**;
- submitted PR quality was similar across treatment conditions.

Field coverage:

| VSWO field | Available? | Comment |
|---|---|---|
| real attempted workflows | **yes** | repository issues / features / refactors |
| completed outcomes | **yes** | completed tasks are observed |
| verification quality | **moderate/strong** | real repo work and similar PR quality, but not a single standardized acceptance rule |
| human time | **yes** | primary outcome |
| model/inference cost | no | not reported as workflow cost |
| review/remediation cost | incomplete | some workflow burden is embedded in elapsed work time, not decomposed |
| rollback / long-run defect window | incomplete | not the main endpoint |
| business value | no | no monetized outcome value |

**Classification:** strong **human-time / quality negative-control benchmark**; still not full Cost/VSWO.

### 8.3 METR late-2025 / early-2026 follow-up — do not overread

METR's February 2026 update is methodologically important because the second experiment became affected by:

- developers declining participation because they did not want to work without AI;
- changed participant compensation;
- concurrent multi-agent workflows that made time measurement harder.

Raw estimates suggested more favorable productivity effects than the early-2025 study, but METR explicitly judged the data an **unreliable signal of the current causal effect**.

This becomes a Phase II rule:

> **As AI adoption becomes endogenous, randomized “AI vs. no-AI” experiments can become harder to recruit and less representative.**

So longitudinal workflow economics will need:
- natural experiments;
- within-firm phased rollouts;
- task-level telemetry;
- before/after matched workflow panels;
- explicit selection-bias diagnostics.

### 8.4 CodeFuse / Ant Group — high output effect, weak VSWO denominator

The 2026 quasi-experiment reports:

- a six-week initial access window;
- treatment/control groups from comparable programmers;
- about **55% more lines of code** in the treatment group;
- roughly one-third of the increase directly generated by the model.

This is useful evidence that AI can change production volume.

But:

> **lines of code ≠ verified software outcome**

The study does not, from the headline evidence used here, provide a common merged/accepted/rollback-adjusted denominator comparable with METR's real-task completion-time measure.

**Classification:** causal/quasi-causal **production-volume anchor**, not a VSWO benchmark.

---

## 9. Benchmark completeness score

To prevent qualitative inflation, Phase II assigns a non-economic completeness score.

One point for each observable field:

1. attempted workflow denominator;
2. accepted/verified outcome;
3. human time;
4. quality / failure;
5. AI variable cost;
6. tool / infrastructure cost;
7. review / remediation;
8. persistence / reopen / rollback;
9. business value;
10. comparable baseline/control.

This score measures **data completeness**, not study quality.

| Study | Completeness /10 | What it can support |
|---|---:|---|
| Customer-support rollout | ~5/10 | causal workflow throughput + quality |
| METR early-2025 coding RCT | ~5/10 | causal human-time effect + realistic quality |
| CodeFuse quasi-experiment | ~3/10 | causal/quasi-causal output-volume effect |
| product telemetry / token studies | ~1–2/10 | resource usage, not workflow economics |

No current case in this first ledger is sufficient for a full:

> **Cost per VSWO + Workflow ROI**

calculation.

That absence is itself a substantive research result.

---

## 10. What data would close the denominator

For a firm-level production workflow, the minimum export should contain:

```text
workflow_id
treatment / model / routing
start_time
end_time
human_minutes
model_calls
input_tokens
output_tokens
tool_calls
AI_cost
tool_cost
review_minutes
remediation_minutes
acceptance_result
failure_severity
reopen_or_rollback
business_value_if_observable
```

The decisive improvement over existing literature is not another productivity percentage.

It is joining:

> **cost telemetry + human labor + verified outcome + persistence**

at the same workflow ID.

---

## 11. ROI layer

If business value can be observed:

```text
Net_Value_per_VSWO
=
Gross_Business_Value_per_VSWO
- Cost_per_VSWO
```

and:

```text
Workflow_ROI
=
(Incremental Business Value - Incremental Cost)
/
Incremental Cost
```

But value should be omitted rather than invented when:
- revenue attribution is unclear;
- quality effects are hard to monetize;
- avoided labor does not translate into actual cost reduction or incremental capacity.

A time saving is not automatically cash savings.

---

## 12. Link to demand elasticity

P0-2 and P0-3 connect through:

```text
E3
=
% change in Verified Workflow Volume
/
% change in Cost per VSWO
```

This is the report’s most relevant demand elasticity.

Only after P0-3 creates a stable denominator can the report ask:

> When an accepted business outcome becomes 10% cheaper, how many additional accepted workflows become economically worthwhile?

That is much closer to a genuine Jevons question than token-price elasticity.

---

## 13. Link to infrastructure demand

Once VSWO is observable:

```text
Infrastructure Demand
=
Verified Workflow Volume
× Attempts per VSWO
× Resource Intensity per Attempt
```

This decomposition exposes three different mechanisms:

1. **adoption effect** — more verified workflows;
2. **agent-depth effect** — more attempts / loops per outcome;
3. **efficiency effect** — fewer resources per attempt.

The total can rise even while model unit cost and resource intensity fall.

---

## 14. Phase II benchmark classes

Start with four classes that have comparatively observable verification:

1. **Customer Support**
   - verifier: issue resolution / reopen / quality;
   - best existing causal literature.

2. **Software Engineering**
   - verifier: tests + merge/review + rollback window;
   - includes both positive and negative empirical evidence.

3. **Document / Structured Extraction**
   - verifier: exact field-level ground truth;
   - easiest place to measure retries, model routing and human review.

4. **Research / Analytical Deliverables**
   - verifier: claim-source audit + acceptance rubric;
   - closest to complex agentic knowledge work, but hardest to blind.

Do not start with sales revenue or strategy work, where attribution is too weak for v0.1.

---

## 15. Current conclusion

The report’s prior phrase “cost per verified workflow outcome” is directionally correct but previously under-specified.

After v0.2 it has both an operational definition and a first evidence-completeness ledger:

> **all variable and human workflow costs divided by outputs that pass a fixed acceptance rule, with success rate, review burden, attempts, resource intensity and cycle time reported alongside.**

The next step is to obtain datasets that join **cost + human time + verification + persistence** at the workflow-ID level. Existing causal productivity studies are valuable anchors, but none of the first reviewed cases yet fills the complete Cost/VSWO denominator.

## Sources

- Brynjolfsson, E.; Li, D.; Raymond, L., **Generative AI at Work**, NBER Working Paper 31161; published in *Quarterly Journal of Economics* 140(2), 2025: https://www.nber.org/papers/w31161
- METR, **Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity**, 2025: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- METR, **We are Changing our Developer Productivity Experiment Design**, 2026-02-24: https://metr.org/blog/2026-02-24-uplift-update/
- Gambacorta, L.; Qiu, H.; Shan, S.; Rees, D. M., **Generative AI and labour productivity: A quasi experiment on coding**, *Journal of Financial Stability* 84, 2026: https://www.sciencedirect.com/science/article/pii/S1572308926000458
- Anthropic, **Anthropic Economic Index: Economic primitives**, 2026-01-15: https://www.anthropic.com/research/anthropic-economic-index-january-2026-report
- Anthropic, **Anthropic Economic Index: Cadences**, 2026-06-26: https://www.anthropic.com/research/economic-index-june-2026-report
