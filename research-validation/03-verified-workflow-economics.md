# P0-3 · Verified Workflow Economics v0.7

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

## 11. New enterprise-field evidence

### 11.1 Cross-industry Microsoft field experiment — time savings do not automatically change organization output

Dillon, Jaffe, Immorlica & Stanton ran a six-month randomized field experiment across **66 firms and 7,137 knowledge workers**.

Workers received an AI tool integrated into existing email, meeting and document workflows.

Key result:

- treated users who actually used the tool regularly spent about **two fewer hours per week on email** in the later half of the experiment;
- working outside regular hours also fell;
- documents appeared to be completed moderately faster;
- but the study did **not** detect a broad shift in the quantity or composition of workers' tasks from individual-level AI provision.

This adds a crucial workflow-economics constraint:

> **individual time saving ≠ organization-level throughput gain**

when coordination, meetings, approval chains or downstream bottlenecks do not change.

Field coverage:

| VSWO field | Available? | Comment |
|---|---|---|
| treatment/control | **yes** | randomized access |
| human time | **strong** | email/document/working-time telemetry |
| workflow output | partial | document completion and work-pattern changes |
| verified quality | incomplete | not a universal task-acceptance rule |
| model cost | incomplete | not a full Cost/VSWO denominator |
| organizational throughput | **negative/limited evidence** | no broad task quantity/composition shift |
| persistence | **moderate** | six-month field experiment |

**Classification:** strong evidence for **coordination bottlenecks and time-vs-output separation**.

### 11.2 P&G product innovation RCT — AI can substitute for some team-composition benefits

Dell'Acqua et al. ran a preregistered field experiment with **776 professionals at Procter & Gamble** working on real product-innovation challenges.

Participants were randomized across:
- individual vs. team work;
- AI vs. no-AI access.

The central result is unusually relevant to workflow design:

> **individuals with AI achieved performance comparable to teams without AI.**

AI also improved performance across the product-innovation work and changed how expertise was combined.

This does not prove that AI eliminates teams.

It supports a narrower mechanism:

> **for some knowledge workflows, AI can reduce the coordination/expertise-combination cost normally supplied by an additional human collaborator.**

For VSWO economics this means the baseline must sometimes be:

> one worker + AI

versus:

> two-worker team without AI

—not merely one worker vs. one worker.

Field coverage:

| VSWO field | Available? | Comment |
|---|---|---|
| realistic accepted task | **strong** | real product-innovation challenges |
| treatment/control | **yes** | preregistered randomized design |
| quality/performance | **strong** | expert-rated task performance |
| human-team structure | **yes** | individual/team comparison |
| human time / labor units | partial | team composition observable, full labor-cost ledger incomplete |
| AI variable cost | no | not a complete unit-cost estimate |
| persistence / downstream commercialization | no | innovation output is not final market success |

**Classification:** strong **quality + organizational-design benchmark**, incomplete Cost/VSWO.

### 11.3 Online-retail randomized field experiments — business value is observable, cost ledger remains incomplete

Fang et al. study GenAI deployment across **seven consumer-facing business workflows** on a large cross-border online-retail platform, involving millions of users and products.

Across the experiments:

- sales effects ranged from roughly **0% to 16.3%** depending on the workflow;
- four applications produced positive effects;
- the authors estimate about **US$5 annual incremental value per consumer** across those positive applications;
- inputs and prices were held constant across experimental arms, allowing the authors to interpret positive sales effects as productivity improvements.

This is especially useful because it moves closer to:

> **observable business value**

rather than only time saved or output volume.

But it still does not publish the full:
- inference cost;
- integration cost;
- human review/remediation cost;
- failure persistence

needed for Cost/VSWO.

**Classification:** strong **business-value causal anchor**, incomplete workflow-cost denominator.

---

### 11.4 Mapping AI into Production — firm-performance bridge, but not a pure AI-access RCT

Kim, Kim & Koning (2026) study **515 high-growth startups** in a field experiment focused on what they call the **mapping problem**: firms often fail not because AI lacks capability, but because they do not know where in the production process AI creates value.

The treatment is important to classify correctly.

Treated firms were shown how other firms had reorganized production around AI and were prompted to search more broadly for use cases. The experiment is therefore **not** a pure:

> AI access vs. no AI access

randomization.

It is closer to:

> **better AI-use-case mapping / organizational search vs. baseline discovery process.**

Reported outcomes:

- AI use cases discovered: **+44%**;
- completed tasks: **+12%**;
- probability of acquiring paying customers: **+18%**;
- revenue: approximately **1.9×**;
- external-capital demand: **-39.5%** relative to control;
- labor demand: no proportional increase.

This is valuable because it connects several layers that are usually observed separately:

```text
AI use-case discovery
→ workflow deployment
→ task completion
→ paying customers
→ revenue
→ external-capital demand
```

That makes it the strongest current **firm-performance bridge** in the P0-3 ledger.

But it still does not close Cost/VSWO because the public evidence used here does not expose:

- model / inference cost by workflow;
- human review / remediation minutes;
- accepted-outcome persistence at workflow level;
- workflow-specific revenue attribution;
- implementation / observability cost.

**Classification:** strong **organizational mapping + firm-performance causal anchor**, incomplete Cost/VSWO.

### 11.5 Alibaba customer-service RCT — speed, subjective quality and objective persistence can diverge

Ni et al. study a large-scale randomized field experiment in Alibaba after-sales customer service.

Agents assigned AI access received AI-generated:
- issue diagnoses;
- proposed solutions;

while retaining discretion to adopt, modify, or ignore them.

The reported results show:

- faster issue identification;
- shorter chat duration;
- improved customer ratings / lower dissatisfaction;
- **no significant improvement in objective customer retrial rate**.

The heterogeneity is especially important:

- lower-performing agents improved the most;
- top-performing agents showed little speed gain and could experience worse subjective and objective quality;
- the paper links part of the deterioration to greater multitasking / longer shift-away time across concurrent chats.

This creates an important VSWO rule:

> **speed improvement and subjective quality improvement do not substitute for objective persistence / reopen measurement.**

For customer service, a better acceptance identity is:

```text
Initial Resolution
+
No Retrial / Reopen
+
Quality Floor
```

—not chat duration alone.

It also shows why AI routing may need to be heterogeneous:

> **AI can be high-value for low-performing workers and neutral or harmful for already-high-performing workers in the same workflow.**

Therefore firm-wide average ROI can hide worker / task segments with opposite treatment effects.

**Classification:** strong **human-time + quality + persistence-counterexample**; still missing full AI cost and business-value ledger.

### 11.6 Property-tax appeal RCT — completed action is still not final economic value

Holz et al. (NBER, August 2026) recruited **645 households** in Dallas County.

All households received personalized information and filing support; half also received an AI chatbot.

Reported outcomes:

- **78%** of households offered the chatbot initiated a conversation;
- chatbot access increased filing an appeal **without a human agent by 9.1 percentage points**, from **41.4% to 50.5%**.

This is useful because the observed endpoint is a real downstream action.

But the public abstract does not establish:

- whether the appeal succeeded;
- realized tax savings;
- total AI / platform cost;
- household time cost;
- later correction / dispute cost.

So:

> **action completion ≠ verified final economic outcome.**

For this workflow, the denominator would need to progress through:

```text
eligible case
→ appeal filed
→ appeal accepted / adjudicated
→ tax outcome
→ net value after time / AI / professional cost
```

The study is therefore a clean example of why P0-3 must distinguish **workflow completion** from **economic realization**.

**Classification:** strong **behavioral / action-completion causal anchor**, incomplete final-value and cost denominator.

---

## 12. Updated evidence-completeness ledger

| Study | Main strength | Completeness /10 | Missing decisive fields |
|---|---|---:|---|
| Customer-support rollout | accepted-outcome throughput + quality | ~5 | model/implementation/review cost, persistence |
| METR early-2025 coding | real tasks + human time + negative control | ~5 | AI cost, decomposed review/remediation, business value |
| CodeFuse | production-volume causal effect | ~3 | verified accepted outcome, full quality/cost |
| Microsoft 66-firm RCT | longitudinal human-time telemetry + coordination constraint | ~5 | universal accepted outcome, AI cost, business value |
| P&G innovation RCT | quality + team-structure substitution | ~5 | AI cost, downstream persistence/value |
| Online-retail RCTs | randomized business-value outcome | ~6 | workflow-level AI/human cost and failure persistence |
| Mapping AI into Production | organizational mapping → tasks / paying customers / revenue / capital demand | ~6 | workflow-level AI cost, review/remediation, persistence, workflow-specific value attribution |
| Alibaba customer-service RCT | speed + subjective quality + objective retrial counterexample | ~6 | AI cost, full business-value attribution, long-run reopen economics |
| Property-tax appeal RCT | real action completion without human agent | ~4 | final appeal success/value, AI cost, human time, persistence |
| Cruces et al. education-gap RCT | assisted quality + unassisted follow-up persistence | ~5 | production cost, integration cost, business value, long-run persistence |

The new studies strengthen one conclusion:

> **The literature is rapidly improving on either the numerator (business value / quality) or the denominator (human time), but still rarely joins value + AI cost + human cost + verified persistence at the same workflow ID.**

This remains the missing measurement standard.

---

## 12A. Persistence / skill-transfer evidence: assisted output is not the whole outcome

Cruces et al. (NBER WP 34851, 2026) add a useful dimension that most enterprise studies do not measure.

Design:
- **1,174 adults aged 25–45**;
- randomized AI vs. no-AI access;
- incentivized workplace-style business problem-solving task;
- followed by a **non-AI-assisted follow-up module**.

Main findings:
- AI improved task performance for all participants;
- the higher- vs. lower-education performance gap fell from **0.548 SD** without AI to **0.139 SD** with AI;
- once AI was removed, treated participants did **not** perform worse than controls;
- lower-education participants retained part of the gain, although a sizable gap re-emerged;
- follow-up performance was stronger when intensive AI use was combined with sustained user effort.

This is important for VSWO economics because it separates two different assets:

1. **assisted workflow output**;
2. **human capability that remains after the tool is removed**.

The report should therefore add a persistence companion metric when the workflow has learning / capability value:

```text
Persistence_Retention
=
Unassisted Follow-up Performance
/
AI-assisted Performance Gain
```

This ratio is conceptual until a task-specific denominator is defined.

The more important rule is:

> **A high AI-assisted success rate does not tell us whether the organization is accumulating capability, merely renting capability, or doing both.**

This matters differently by workflow:
- customer support may care mostly about current verified throughput;
- coding / engineering may care about review and maintainability;
- education / training may care directly about retained human capability;
- safety-critical analytical work may require both accepted output and retained operator understanding.

### Evidence-completeness impact

This study strengthens:
- treatment/control;
- verified task performance;
- a short persistence / transfer check.

It still does not supply:
- production AI cost;
- workflow integration cost;
- downstream business value;
- long-run reopen / rollback;
- organization-level persistence.

**Classification:** strong persistence / human-capital benchmark, incomplete Cost/VSWO.

---

## 12B. Workflow-ID closure protocol v0.1

The empirical gap is now specific enough to define a **closure standard**.

A dataset qualifies as a full VSWO economics panel only if one stable `workflow_id` can join five domains:

### Domain A — Resource cost
- model / inference cost;
- retrieval / tool cost;
- infrastructure / observability cost.

### Domain B — Human labor
- production minutes;
- review minutes;
- remediation minutes;
- escalation minutes.

### Domain C — Verification
- acceptance result;
- quality score;
- severity-weighted error;
- blinded / automated verifier where feasible.

### Domain D — Persistence
- reopen / retrial;
- rollback;
- later correction;
- verification window.

### Domain E — Business value
- revenue / gross margin;
- avoided cost;
- customer retention;
- accepted transaction value;
- or another pre-specified economic endpoint.

Minimum join identity:

```text
workflow_id
→ treatment / model
→ AI resource cost
→ human time
→ accepted outcome
→ persistence outcome
→ business value
```

### 12B.1 Three levels of empirical closure

**Level 1 — Productivity closure**
- human time;
- accepted output;
- quality.

Supports:
> does AI improve verified productivity?

**Level 2 — Cost closure**
- Level 1;
- AI / tool / infra cost;
- remediation cost.

Supports:
> does AI lower Cost per VSWO?

**Level 3 — Economic closure**
- Level 2;
- persistence;
- realized business value.

Supports:
> does AI create positive durable Workflow ROI?

Current literature has multiple strong Level-1 cases and partial Level-2/3 components.

The research set still lacks a public production dataset that cleanly satisfies all Level-3 fields at the same workflow ID.

### 12B.2 Organizational mapping is a separate economic variable

The 515-startup experiment adds a variable that the original Cost/VSWO schema understated:

> **Use-Case Discovery / Mapping Cost**

A firm may own a capable model and still fail to realize value because it has not identified:

- which workflow;
- which step;
- which acceptance rule;
- which human role;
- which integration point

should change.

Therefore total adoption economics should be represented as:

```text
AI Transformation Cost
=
Mapping / Discovery Cost
+
Integration Cost
+
Workflow Operating Cost
+
Verification / Remediation Cost
```

This prevents a narrow model-cost calculation from understating implementation economics.

### 12B.3 Heterogeneous-treatment rule

Alibaba and other field experiments show that average treatment effects can hide opposite segment effects.

Every production workflow benchmark should therefore report, where statistically defensible:

- baseline skill / experience;
- workflow difficulty;
- task novelty;
- AI adoption intensity;
- model / route;
- human-review intensity.

A positive average ROI does not imply every worker/task segment should use the same AI route.

### 12B.4 Completion-to-value ladder

P0-3 now distinguishes five nested outcomes:

```text
Output Produced
→ Output Accepted
→ Workflow Completed
→ Outcome Persists
→ Economic Value Realized
```

Each arrow is a possible failure point.

A study that measures an earlier stage must not be described as if it measured a later stage.

---

## 12C. Public Level-3 Workflow-ID Candidate Audit v0.6

P0-3 下一步不是继续堆“AI 提升 X%”案例，而是检查公开数据能否真正满足：

```text
workflow_id
→ AI/tool cost
→ human time
→ verification
→ persistence
→ realized business value
```

本轮优先审计了最接近闭环的公开候选。

| Candidate | Stable workflow / task ID | AI / tool cost at same ID | Human time | Verification / accepted output | Persistence | Realized business value | Closure verdict |
|---|---|---|---|---|---|---|---|
| **METR experienced OSS developers** | **Yes** — public `issue_id` for 246 valid completed issues | **No** | **Strong** — `initial_implementation_time`；部分样本还有 `post_review_implementation_time` 到 merge | **Partial/Strong** — real issue → PR review → merge path，且数据只保留 valid completed issues | **No durable rollback / regression window in public dataset** | **No** | **Closest public workflow-ID productivity panel; Level 1, not Level 3** |
| **Brynjolfsson–Li–Raymond customer support** | underlying conversation / agent records exist in study, but no public workflow-ID panel used here | **No** | **Strong at operational-data level** — issues resolved/hour | **Strong outcome-style** — resolved issues + customer sentiment | **Partial** — employee retention / learning are worker-level, not per-case reopen persistence | **No workflow-specific realized value** | **Strong production productivity anchor; not public Level 3** |
| **Klarna AI Assistant** | company operates millions of customer conversations, but public disclosure does not expose a joinable conversation-level panel | **No workflow-level tool-cost ledger** | aggregate equivalence / efficiency only | aggregate service metrics | public disclosures do not expose conversation-level reopen/persistence join | **Yes at aggregate level** — company disclosed about **US$40M annualized savings** | **Economic closure at aggregate program level, not workflow-ID Level 3** |
| **Online-retail randomized field experiments** | experiment/workflow units exist | **No full public cost ledger** | partial / workflow dependent | **Strong** randomized customer/business outcomes | incomplete | **Strong causal sales/value outcome** | **Value-side bridge; not Level 3** |
| **Mapping AI into Production** | firm-level experimental unit, not accepted-output workflow ID | **No** | incomplete | tasks / paying-customer outcomes | incomplete | revenue / capital-demand outcomes at firm level | **Firm-economic bridge; not workflow-ID Level 3** |

### 12C.1 Why METR is the strongest public workflow-ID candidate so far

The released METR dataset exposes:

- `dev_id`;
- `issue_id` for **246** completed issues;
- `ai_treatment`;
- pre-randomization expected completion time;
- `initial_implementation_time` to pull request;
- for part of the sample, `post_review_implementation_time` until merge.

This is materially better than an aggregate productivity headline because a stable task identity can connect treatment and human-time telemetry.

It also supplies a useful **negative ROI direction** at the productivity layer: the core regression reports about **18.8% more completion time with AI** in this setting.

But P0-3 must not overstate what the public panel contains.

The same `issue_id` does **not** publicly join:

- actual model / inference spend;
- tool-call / retrieval cost;
- reviewer minutes as a complete separate cost field;
- post-merge rollback / production incident window;
- revenue, avoided cost, customer value, or other realized business endpoint.

Therefore:

> **public task identity ≠ full economic closure.**

METR is a high-quality Level-1 panel, not a Level-3 panel.

### 12C.2 Why aggregate economics cannot be spliced onto task-level telemetry

Klarna provides the opposite side of the evidence gap.

Its public financial communication says the AI Assistant had engaged millions of customers and was expected to deliver roughly **US$40M of annualized savings**.

That is valuable realized-economics evidence.

But public disclosures do not provide a row such as:

```text
conversation_id
→ model/tool cost
→ human minutes
→ resolution accepted
→ no reopen
→ attributed savings / margin
```

Therefore P0-3 explicitly prohibits this construction:

```text
METR task-level time
+
Klarna aggregate savings
=
"complete AI workflow ROI"
```

Those measurements come from different organizations, workflows, populations, cost structures, and economic endpoints.

> **Cross-study component assembly is not workflow-ID closure.**

### 12C.3 Level-3 public-data status after the audit

Current status remains:

> **No verified public production dataset in the P0-3 evidence set closes all Level-3 fields at one workflow ID.**

This is not treated as “data unavailable, therefore assume ROI.”

It is a measurement result.

The next acceptable upgrade requires one of two things:

1. a public or auditable production dataset exposing the full join; or
2. a first-party enterprise dataset constructed prospectively with the P0-3 schema.

Until then:

- Level-1 studies can support verified-productivity claims;
- partial Level-2 evidence can support bounded cost claims;
- aggregate business-value studies can support organization-level economic claims;
- **none may be relabeled as workflow-level durable ROI without the join.**

### 12C.4 Minimum Level-3 acquisition schema — bridge to §17

This candidate-audit section records the minimum field groups that motivated the full prospective contract.

> **For any new first-party collection, §17 is authoritative.**

The table below is a compact audit bridge, not a second competing schema.

A future dataset should expose at minimum:

| Field group | Required columns |
|---|---|
| Identity | `workflow_id`, workflow class, timestamp, treatment/model/version |
| AI cost | input/output usage, inference cost, tool/API cost, infra allocation |
| Human cost | production, review, remediation, escalation minutes |
| Verification | accepted/rejected, quality score, verifier, severity |
| Persistence | reopen/rollback/correction, verification window |
| Economic value | revenue, gross margin, avoided cash cost, retained customer value, or prespecified business endpoint |
| Mapping / integration | workflow discovery allocation, integration/observability allocation where material |

The hard requirement is not that every value be perfectly precise.

It is:

> **all material fields must resolve to the same workflow identity or to a documented allocation rule.**

---

## 13. ROI layer

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

## 14. Link to demand elasticity

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

## 15. Link to infrastructure demand

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

## 16. Phase II benchmark classes

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

## 17. Prospective first-party Level-3 acquisition contract v0.7

The public candidate audit is complete.

P0-3 should therefore stop accumulating generic productivity studies unless a new study materially improves the same-workflow economic closure.

The next valid empirical object is a **prospectively captured first-party workflow panel**.

This is not a proprietary scoring framework. It is a data-acquisition contract whose purpose is to preserve auditable joins between cost, labor, verification, persistence and realized value.

### 17.1 Unit of observation

The primary key is:

```text
workflow_id
```

A workflow is one economically meaningful unit of work that has:
- a defined start;
- a defined acceptance rule;
- a terminal state;
- and, where applicable, a later persistence/value observation.

Examples:
- one support ticket;
- one software issue / pull request;
- one extraction job;
- one research deliverable with a fixed acceptance rubric.

Do not use:
- one model call;
- one chat turn;
- one document token batch;
- one employee-day

as the Level-3 denominator unless that is genuinely the economic workflow being purchased.

### 17.2 Minimum raw tables

A production dataset should be joinable through `workflow_id` across six logical tables.

#### A. Workflow identity

| Field | Requirement |
|---|---|
| `workflow_id` | stable unique ID |
| `workflow_type` | fixed taxonomy |
| `created_at` | timestamp |
| `closed_at` | timestamp / null if still open |
| `treatment_state` | AI-assisted / baseline / routing variant |
| `model_route` | actual model / policy used |
| `difficulty_or_case_mix` | pre-treatment observable where available |
| `owner_or_team_id` | pseudonymous stable operator/team key |

#### B. AI / tool cost ledger

| Field | Requirement |
|---|---|
| `model_calls` | actual calls |
| `input_tokens` / `output_tokens` | where meaningful and available |
| `inference_cost` | actual billed or internally allocated variable cost |
| `tool_cost` | search / browser / code execution / external API variable cost |
| `compute_or_runtime_cost` | non-model variable infrastructure cost where material |
| `retry_count` | retries attributable to the same workflow |
| `routing_overhead_cost` | orchestration / router cost where separately measurable |

Hard rule:

> **Do not substitute list-price × tokens for actual cost when contracted / cached / bundled pricing materially differs and actual allocation is available.**

If actual allocation is unavailable, label the estimate explicitly.

#### C. Human labor ledger

| Field | Requirement |
|---|---|
| `execution_minutes` | direct human task time |
| `review_minutes` | verification / approval time |
| `remediation_minutes` | rework after failed verification |
| `coordination_minutes` | handoff / escalation / specialist consultation where material |
| `labor_cost_basis` | wage / loaded hourly cost / internal standard cost |
| `human_cost` | derived from the disclosed basis |

Do not hide review and remediation inside a generic “time saved” estimate.

#### D. Verification ledger

| Field | Requirement |
|---|---|
| `acceptance_rule_version` | frozen rubric / test version |
| `acceptance_result` | pass / fail / partial where the workflow genuinely allows partial acceptance |
| `quality_score` | optional, only if independently defined |
| `failure_class` | reason for rejection |
| `reviewer_id` | pseudonymous reviewer / automated verifier identity |
| `verification_time` | timestamp |

The acceptance rule must be defined **before** comparing workflow economics.

Changing the rubric after observing AI performance creates denominator drift.

#### E. Persistence ledger

| Field | Requirement |
|---|---|
| `persistence_window` | workflow-relevant observation horizon |
| `reopen` | ticket reopened / issue reactivated |
| `rollback` | deployment reverted |
| `defect_or_rework_event` | later failure attributable to the workflow |
| `persistence_pass` | whether accepted output remained valid through the stated window |

There is no universal persistence duration.

It must match the workflow:
- support may use reopen / repeat-contact windows;
- software may use merge-to-production / rollback / defect windows;
- extraction may use downstream audit;
- analytical work may use claim-source audit / acceptance without later factual reversal.

### 17.3 Realized-value ledger

A Level-3 record additionally requires a business-value mapping.

| Value type | Examples | Required discipline |
|---|---|---|
| direct revenue | incremental sale / retained revenue | workflow-level attribution or controlled estimate |
| avoided labor | verified labor minutes no longer required | use loaded labor cost, not headline salary alone |
| avoided external spend | contractor / BPO / vendor cost displaced | record actual avoided invoice / contract basis |
| loss avoidance | prevented refund / error / outage / compliance cost | require documented counterfactual basis |
| throughput value | additional accepted cases completed | monetize only if marginal throughput has economic value |
| none observable | research / internal workflow with no defensible value mapping | keep Level 2; do not invent ROI |

Hard rule:

> **A workflow does not become Level 3 merely because management believes it is valuable.**

If realized value cannot be linked or estimated on a documented causal / accounting basis, classification remains Level 2.

### 17.4 Required closure identity

For each accepted workflow:

```text
Workflow_Cost
=
AI / Tool / Runtime Cost
+
Human Execution Cost
+
Review Cost
+
Remediation Cost
+
Allocated Integration / Mapping Cost
```

Then:

```text
Cost_per_Persistent_Verified_Outcome
=
Σ Workflow_Cost
/
Σ Persistent Accepted Outcomes
```

And only when value is observable:

```text
Workflow_ROI
=
(Realized Business Value - Workflow_Cost)
/
Workflow_Cost
```

The denominator must use **persistent accepted outcomes**, not raw attempts or model generations.

### 17.5 Integration / mapping-cost rule

The Mapping-AI-into-Production evidence shows that organizational search and use-case mapping can be a real economic input.

Therefore implementation cost must not disappear from ROI.

For a prospective deployment, separately record:
- workflow redesign;
- integration engineering;
- prompt / policy development;
- evaluator construction;
- data cleanup;
- change management / training.

These should be:
- expensed directly when workflow-specific;
- or allocated over an explicit expected / observed production volume when shared.

Do not allocate them only to successful workflows after the fact.

### 17.6 Missingness and censoring

The dataset must distinguish:

```text
0
≠
not applicable
≠
not measured
≠
not yet observed
```

Examples:
- no rollback is `0 / false`;
- rollback not meaningful for a workflow is `N/A`;
- rollback telemetry absent is `not measured`;
- persistence window still open is `not yet observed`.

This distinction is mandatory because treating unobserved persistence as “no failure” systematically inflates AI workflow economics.

### 17.7 Baseline and case-mix discipline

Where causal comparison is intended, preserve:
- pre-treatment case-mix variables;
- routing / assignment rule;
- operator experience;
- workflow difficulty;
- time period;
- baseline process definition.

Preferred designs, depending on operational feasibility:
- randomized rollout;
- phased rollout;
- matched contemporaneous controls;
- within-workflow or within-team natural experiments.

Do not compare:
- easy AI-routed cases
against
- hard human-only cases

and call the difference productivity.

### 17.8 Minimum publishable output

A Level-3 study should report at least:

1. attempted workflows;
2. accepted workflows;
3. persistent accepted workflows;
4. success / persistence rate;
5. human minutes per persistent accepted workflow;
6. AI/tool cost per persistent accepted workflow;
7. review + remediation burden;
8. total workflow cost;
9. realized value where observable;
10. case-mix / baseline design;
11. missing-data / censoring policy;
12. distribution, not only mean, for cost and cycle time.

No universal ROI threshold is defined here.

The purpose is to make the economics **auditable**, not to manufacture a pass/fail benchmark.

### 17.9 P0-3 stop rule

After v0.7:

> **P0-3 literature expansion is frozen unless new evidence closes a field that the current evidence ledger cannot close.**

Valid future upgrades are limited to:
- a public same-`workflow_id` Level-3 dataset;
- a first-party prospective dataset following this acquisition contract;
- a methodological result that materially changes verification, persistence or causal attribution.

Generic “AI saves X% time” studies no longer justify a version bump.

---

## 18. Current conclusion

The report’s prior phrase “cost per verified workflow outcome” is directionally correct but previously under-specified.

After v0.7 it has an operational definition, an evidence-completeness ledger, a separate persistence / capability-retention dimension, and a prospective first-party Level-3 acquisition contract:

> **all variable and human workflow costs divided by outputs that pass a fixed acceptance rule, with success rate, review burden, attempts, resource intensity and cycle time reported alongside.**

The next step is no longer to accumulate generic productivity studies. P0-3 now has a stop rule: only a public same-`workflow_id` closure, a prospectively captured first-party dataset following §17, or a material methodological change to verification / persistence / attribution justifies further expansion. No public case in the current ledger yet closes the full Cost/VSWO + durable Workflow ROI denominator.

## Sources

- Brynjolfsson, E.; Li, D.; Raymond, L., **Generative AI at Work**, NBER Working Paper 31161; published in *Quarterly Journal of Economics* 140(2), 2025: https://www.nber.org/papers/w31161
- METR, **Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity**, 2025: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- METR, **We are Changing our Developer Productivity Experiment Design**, 2026-02-24: https://metr.org/blog/2026-02-24-uplift-update/
- Gambacorta, L.; Qiu, H.; Shan, S.; Rees, D. M., **Generative AI and labour productivity: A quasi experiment on coding**, *Journal of Financial Stability* 84, 2026: https://www.sciencedirect.com/science/article/pii/S1572308926000458
- Anthropic, **Anthropic Economic Index: Economic primitives**, 2026-01-15: https://www.anthropic.com/research/anthropic-economic-index-january-2026-report
- Anthropic, **Anthropic Economic Index: Cadences**, 2026-06-26: https://www.anthropic.com/research/economic-index-june-2026-report
- Dillon, E.; Jaffe, S.; Immorlica, N.; Stanton, C., **Shifting Work Patterns with Generative AI**, NBER Working Paper 33795, revised 2025: https://www.nber.org/papers/w33795
- Dell'Acqua, F. et al., **The Cybernetic Teammate: A Field Experiment on Generative AI Reshaping Teamwork and Expertise**, NBER Working Paper 33641; published online in *Organization Science*, 2026: https://www.nber.org/papers/w33641
- Fang, L.; Yuan, Z.; Zhang, K.; Donati, D.; Sarvary, M., **Generative AI and Firm Productivity: Field Experiments in Online Retail**, 2025/2026 working paper: https://business.columbia.edu/faculty/research/generative-ai-and-firm-productivity-field-experiments-online-retail
- Cruces, G.; Fernández Meijide, D.; Galiani, S.; Gálvez, R. H.; Lombardi, M., **Does Generative AI Narrow Education-Based Productivity Gaps? Evidence from a Randomized Experiment**, NBER Working Paper 34851, revised May 2026: https://www.nber.org/papers/w34851


- Kim, Kim & Koning, “Mapping AI into Production: A Field Experiment on Firm Performance,” INSEAD Working Paper 2026/20/STR, 2026: https://www.insead.edu/faculty-research/publications/working-papers/mapping-ai-production-a-field-experiment-firm
- Ni et al., “Generative AI in Action: Field Experimental Evidence from Alibaba's Customer Service Operations,” revised 2026-07-31: https://arxiv.org/abs/2603.29888
- Holz et al., “Taxpayer Behavior in the Age of AI: A Field Experiment on Property Tax Appeals,” NBER Working Paper 35632, 2026-08: https://www.nber.org/papers/w35632


## Level-3 candidate-audit sources added in v0.6

- METR public replication repository — anonymized `data_complete.csv`, stable `issue_id`, treatment, implementation time and partial post-review-to-merge time: https://github.com/METR/Measuring-Early-2025-AI-on-Exp-OSS-Devs
- METR study paper / announcement — 16 experienced developers, 246 tasks, early-2025 AI access increased completion time by about 19% in the study setting: https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf
- NBER Working Paper 31161, *Generative AI at Work* — 5,179 support agents; productivity +14% on average with heterogeneous effects: https://www.nber.org/papers/w31161
- Klarna 2024 results — AI Assistant customer scale and approximately US$40M annualized savings at the program level: https://investors.klarna.com/News--Events/news/news-details/2024/Klarna-Announces-Profitable-Start-to-2024-as-It-Sets-the-Stage-for-a-Year-of-Innovation-and-Growth/default.aspx
