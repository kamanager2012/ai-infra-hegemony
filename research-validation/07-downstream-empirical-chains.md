# P2 · Downstream Empirical Chains v0.4

> **Status:** Research-side evidence map; not part of the frozen formal report.  
> **Goal:** strengthen Labor (Ch25), Education (Ch26), and Physical AI (Ch15) without pretending that the evidence is as mature as semiconductors, memory, packaging, power, or CapEx.

## 0. Domain-evidence ownership contract v0.2

This file owns:
- downstream domain-specific evidence chains;
- domain-specific persistence / scale questions;
- evidence gaps for Labor / Education / Physical AI.

It does **not** own the generic workflow-economics denominator.

Authoritative rule:

> **P0-3 §17 is the authoritative workflow-economics acquisition contract.**

07 may add domain-specific fields such as retained mastery, safety intervention, uptime or delayed employment outcomes, but it must not redefine Cost/VSWO, persistence, missingness or Workflow ROI.

Formal-report gate:

> **Downstream evidence can justify a formal chapter update only after the relevant chain closes beyond capability/demo evidence and the frozen report is explicitly reopened.**

## 1. Common rule: a downstream claim needs a chain, not a demo

For each domain, separate:

```text
Capability
→ Adoption
→ Task-level outcome
→ Workflow / organizational change
→ Economic or social outcome
→ Persistence / scale
```

Evidence at one arrow does not prove the next.

Examples:

- benchmark capability ≠ job displacement;
- AI tutor learning gain ≠ system-wide educational transformation;
- robot demo ≠ reliable factory deployment;
- more code generated ≠ more verified software output.

---

# 2. Labor · minimum empirical chain

## 2.1 Required chain

```text
AI access
→ task behavior changes
→ verified productivity / quality changes
→ task mix changes
→ hiring / hours / wages / employment changes
→ persistent occupation-level effect
```

### Labor: what is already supported

**Customer support**
- Brynjolfsson, Li & Raymond: staggered AI-assistant rollout across 5,179 agents;
- roughly 14% higher issues resolved per hour on average in the NBER version;
- gains concentrated among less-experienced/lower-skilled workers;
- customer sentiment and retention also improved.

This supports:
- AI access → task-level productivity;
- heterogeneous worker effects.

It does **not** by itself prove:
- headcount reduction;
- wage decline;
- occupation disappearance.

**Experienced software development**
- METR RCT: 246 real tasks in mature repositories;
- early-2025 AI tools increased completion time by ~19% in that setting.

This is crucial counter-evidence:
- AI access can worsen real workflow productivity even when benchmark capability is strong.

**Coding quasi-experiment**
- 2026 CodeFuse study reports >50% increase in code output.

But “code output” and “verified completed software work” are different denominators.

### Labor: what remains missing

The weakest arrows are:

```text
task productivity
→ firm staffing decision
→ occupation employment/wage effect
```

Those require:
- firm-level adoption panels;
- hiring / separation data;
- hours and wage data;
- task composition;
- controls for demand and macro conditions.

### Labor evidence added in v0.4 — staffing / hiring begins to become observable

#### A. Stanford / ADP payroll evidence — hiring pipeline, not economy-wide displacement

Brynjolfsson, Chandar & Chen's 2026 revision uses high-frequency ADP payroll data covering millions of U.S. workers through June 2026.

The authors report:

- **no evidence of widespread, economy-wide job displacement**;
- employment among workers ages **22–25** in highly AI-exposed occupations is about **19% below** where it would be if it had kept pace with less-exposed peers;
- the gap widened from about 15% in the earlier 2025 vintage;
- the adjustment appears primarily through **reduced hiring rather than increased separations**;
- experienced workers do not show the same gap;
- adjustment so far is more visible in employment than in base pay.

This moves the evidence chain from:

```text
task exposure
→ possible worker effect
```

toward:

```text
occupation exposure
→ age-specific hiring pipeline
→ observed employment divergence
```

But it is still **not** a clean causal estimate of AI displacement.

Potential confounds / boundaries include:
- occupation-specific demand;
- post-pandemic normalization;
- interest-rate / tech-cycle effects;
- firm composition in the ADP sample;
- exposure measures differing from realized adoption.

Therefore the correct conclusion is:

> **AI-linked labor adjustment is now visible in specific early-career hiring pipelines, while broad economy-wide displacement remains unproven.**

#### B. U.S. Census AI supplement — adoption breadth does not imply mass employment reduction

Bonney et al. use nationally representative 2026 Census BTOS data.

Reported structure:

- about **18% of firms** used AI in at least one business function during Nov-2025–Jan-2026;
- employment-weighted adoption was about **32%**;
- **66%** of adopters mainly reported task augmentation;
- employment reductions were reported by only about **2%** of firms;
- functional deployment / operational investment is associated with employment declines in regression analysis, while worker-task use is not after controls.

This is an important organization-level bridge because it separates:

```text
worker uses AI
```

from:

```text
firm integrates AI into functions / operating model
```

The second is more plausibly connected to staffing adjustment.

But the regression is not a randomized causal design.

So:

> **firm-level operational integration is a stronger labor-transmission variable than worker exposure alone, but causal employment effects remain incompletely identified.**

#### C. Cross-country executive survey — strong adoption, weak realized employment effect so far

Yotzov et al. survey nearly 6,000 senior executives in the U.S., U.K., Germany and Australia.

They report:
- roughly **69%** of firms actively use AI;
- more than **80%** report no employment or productivity impact from AI over the previous three years;
- executives expect larger future effects than have been realized so far.

This is useful contrary evidence against interpreting high adoption as already-large labor displacement.

Forecasted employment reductions remain **expectations**, not realized outcomes.

### Labor research rule

Never write:

> “Exposure = displacement.”

Use:

> **exposure → measured task effect → organizational response → labor-market outcome**

and stop at the strongest observed arrow.

---

# 3. Education · minimum empirical chain

## 3.1 Required chain

```text
AI-assisted instruction
→ immediate learning gain
→ delayed retention / transfer
→ teacher/tutor workload change
→ scaling cost
→ institution-level learning outcome
```

### Education: what is already supported

**Harvard undergraduate physics RCT (2025)**
- N=194;
- custom AI tutor vs. active-learning classroom;
- students using the AI tutor learned significantly more in less time and reported stronger engagement/motivation.

This supports:
- well-designed AI tutoring can improve near-term learning in a specific course/context.

It does not prove:
- broad K-12 effect;
- long-run retention;
- teacher replacement;
- system-level cost effectiveness.

**Tutor CoPilot**
- randomized human-AI tutoring study;
- more than 700 tutors and 1,000 students in the published study summary;
- students of tutors with AI support were about 4 percentage points more likely to master math topics;
- gains were larger for students of lower-rated tutors;
- reported tool cost was low relative to ordinary tutoring costs.

This supports:
- AI can improve human tutoring quality;
- effects can be heterogeneous by baseline tutor skill.

### Education: what remains missing

Need more evidence on:
- retention weeks/months later;
- transfer to unseen subjects;
- overreliance / reduced independent problem-solving;
- teacher workload;
- actual implementation and training cost;
- adoption at school-system scale;
- subgroup heterogeneity.

### Education evidence added in v0.4 — school-scale use and delayed learning

#### A. Khanmigo two-year school experiment — institution-scale effect, but engagement is binding

Oreopoulos & Low report a two-year cluster randomized trial across **18 Tennessee middle schools** using Khan Academy with Khanmigo during daily remedial mathematics sessions.

Reported results include:

- assignment raises math achievement by about **1.3 national percentile ranks per term**;
- approximately **0.06–0.08 standard deviations over a school year**;
- implied effect of a full year of active participation reaches about **0.14 SD**;
- gains are similar to those found in Khan Academy practice without AI assistance;
- **96%** of students tried Khanmigo at least once, but median use was only about one-third of practice days;
- students used it in only about **17%** of exercise sessions in which they made a mistake.

This is a major evidence upgrade because it observes:

```text
school deployment
→ repeated use
→ school-year achievement
```

rather than a short lab task.

But it also weakens a simplistic "AI tutor access automatically transforms learning" narrative.

The binding constraint is partly:

> **engagement / instructional integration, not model availability.**

The fact that gains resemble non-AI Khan Academy practice means the incremental AI component cannot be assumed to explain the full achievement effect.

#### B. NUMI 6,000+ student RCT — delayed retention / transfer is weaker than immediate support

Oreopoulos, Liut, Sungu & Low study more than **6,000 middle-school students** randomized across AI vs CAL-only support and mastery vs non-mastery progression.

One week later students completed a delayed assessment covering:
- practiced material;
- unpracticed material.

During practice:
- AI students progressed more slowly;
- attempted fewer questions;
- were more accurate conditional on attempting;
- after mistakes, AI improved next-attempt correctness and reduced attempts needed to return to a correct answer.

But on delayed learning:
- mastery alone did not improve delayed outcomes;
- the most encouraging delayed-test evidence appears when AI is embedded in the mastery workflow;
- gains were marginally significant and concentrated on practiced material rather than broad transfer.

This closes a missing research field:

> **delayed assessment exists.**

But the result is mixed rather than uniformly positive.

Therefore:

```text
immediate correction support
≠
broad delayed retention / transfer
```

The evidence supports a more precise mechanism:

> **AI tutoring is more productive when the workflow structures mistakes into sustained reasoning; access alone is not enough.**

### Education chain status after v0.4

The strongest observed chain is now:

```text
AI-assisted instruction
→ repeated school use
→ measurable achievement / immediate error correction
→ limited / context-dependent delayed retention
```

Still weak / missing:
- broad transfer across topics;
- teacher workload and organizational redesign;
- all-in implementation cost;
- persistent multi-year learning beyond the study environment;
- system-level scaling economics.

### Education research rule

A short RCT learning gain is **not** a 10-year educational forecast.

The full chain must retain:
- retention;
- transfer;
- teacher complementarity;
- implementation cost.

---

# 4. Physical AI · minimum empirical chain

## 4.1 Required chain

```text
Perception / planning / control capability
→ task success in realistic environment
→ reliability / uptime / safety
→ cycle time / throughput
→ unit economics
→ fleet deployment
→ labor / capital substitution
```

### Real-world deployment baseline

IFR World Robotics 2025 reports:
- **542,000 industrial robots** installed globally in 2024;
- **4.664 million** industrial robots in operational use;
- China represented **54%** of global 2024 installations;
- professional service-robot sales were almost **200,000** units in 2024;
- transportation/logistics represented more than half of professional service-robot units.

This proves large-scale **robotics automation** already exists.

It does **not** prove that current “Physical AI” / foundation-model-driven robotics has inherited the same production economics.

That distinction is mandatory.

### What would count as production-grade Physical AI evidence

A case should provide:

1. number of deployed systems;
2. real operating hours;
3. task success rate;
4. intervention / takeover rate;
5. downtime / maintenance;
6. safety incident denominator;
7. throughput vs. human / fixed automation;
8. total cost of ownership;
9. customer renewal / expansion;
10. deployment across more than one controlled site.

A demo video or benchmark score cannot fill these fields.

### Production-grade Physical AI evidence added in v0.3

The evidence base is now strong enough to separate three different production states instead of treating all "Physical AI" as one category.

#### A. AI-enhanced mature robotics fleet — Amazon DeepFleet

Amazon reported in June 2025 that its robotics fleet had reached more than **1 million robots across more than 300 facilities**.

The same first-party release introduced **DeepFleet**, which Amazon describes as a generative-AI foundation model coordinating robot movement across its fulfillment network.

Reported process effect:

- robot travel time / fleet movement efficiency improved by about **10%**;
- the objective is reduced congestion, faster processing and lower operating cost.

This is unusually important because the chain is no longer:

```text
AI model
→ demo robot
```

It is:

```text
AI model
→ existing physical fleet
→ multi-site deployment
→ measured process-efficiency change
```

But the denominator must remain precise.

This is evidence for:

> **AI-enhanced mature warehouse robotics at fleet scale.**

It is **not** evidence that:
- humanoid robots already have the same production economics;
- every robot in the one-million fleet runs one identical foundation-model control stack;
- 10% travel-time improvement equals 10% labor or total-cost reduction;
- the improvement is independently audited.

#### B. Frontier humanoid on a live automotive production line — BMW / Figure 02

BMW's 2026 first-party materials provide one of the strongest current production-grade humanoid observations.

BMW reports that Figure 02 at Plant Spartanburg:

- operated over roughly **10 months**;
- worked **10-hour shifts, Monday–Friday**;
- accumulated about **1,250 operating hours**;
- moved more than **90,000 components**;
- contributed to production of more than **30,000 BMW X3 vehicles**;
- performed repeatable sheet-metal positioning tasks with millimetre-level precision.

This crosses several arrows in the Physical-AI evidence chain:

```text
capability
→ realistic task success
→ repeated shift operation
→ real production-line contribution
```

BMW also disclosed integration lessons that matter for production economics:

- revised safety concepts with additional barriers / partitions;
- improved 5G coverage;
- early involvement of production IT, occupational safety, production-process management and shop-floor logistics;
- integration into BMW's Smart Robotics ecosystem through standardized interfaces.

That is evidence that:

> **deployment cost is not robot hardware alone; safety, connectivity, production IT and process integration are part of the operating system around the robot.**

However, the public materials still do **not** provide:

- task-level intervention / takeover rate;
- uptime percentage;
- MTBF / maintenance burden;
- safety incidents per operating hour;
- human-equivalent throughput denominator;
- TCO / payback period;
- unit labor-cost substitution;
- fleet economics across multiple independent factories.

Therefore the BMW/Figure case is:

> **strong production-workflow evidence, partial reliability / integration evidence, incomplete unit-economics evidence.**

#### C. Commercial humanoid logistics deployment — GXO / Agility Digit

GXO first-party evidence shows a progression from:
- proof-of-concept pilot in 2023;
- to a **multi-year Robots-as-a-Service commercial agreement** in 2024;
- to Digit robots operating in a live SPANX fulfillment environment alongside existing AMRs.

The production task is concrete:

> unloading totes from AMRs and placing them onto conveyors for downstream pack-out.

Agility later reported:
- more than **100,000 totes** moved at the GXO Flowery Branch deployment;
- one-year full-time deployment milestone;
- more than **65,000 aggregate operating hours** across deployment commitments at nine customer facilities.

Evidence identity matters:

- the commercial agreement / live-warehouse deployment is supported by **GXO first-party disclosure**;
- the 100,000-tote and 65,000-hour figures are **Agility vendor-reported operational claims** and should not be promoted to independent customer-audited metrics.

The case supports:

```text
pilot
→ commercial contract
→ repeated live workflow
→ customer expansion intent
```

It still does not publicly close:

```text
intervention rate
+ uptime
+ safety denominator
+ TCO
+ labor substitution
+ independently verified ROI
```

#### D. New evidence hierarchy for Physical AI

| Evidence state | Example | Current confidence |
|---|---|---|
| AI model on mature robot fleet with measured process effect | Amazon DeepFleet | **Strong for fleet-scale process effect; not humanoid/generalist** |
| Frontier humanoid repeated live production workflow | BMW / Figure 02 | **Strong workflow deployment; partial reliability/integration; weak economics** |
| Commercial humanoid RaaS + repeated logistics workflow | GXO / Digit | **Strong commercial/deployment identity; vendor-heavy operating metrics** |
| Multi-customer fleet-hour claims | Agility 65k+ hours / nine facilities | **Directional vendor evidence; requires customer / audited denominators for stronger inference** |
| Humanoid demo / pilot announcement without operating denominator | many frontier announcements | **Insufficient for production-economics claim** |

### Physical-AI measurement gap after v0.3

The weakest part of the chain has moved.

Previously the gap was:

> **Can frontier Physical AI operate repeatedly in a real production environment?**

BMW / Figure and GXO / Digit now provide evidence that the answer is **yes for narrow production tasks**.

The remaining high-value gap is now:

> **Can those deployments demonstrate reliable, safe, economically superior operation at fleet scale?**

The next decisive fields are:

1. intervention / takeover per operating hour;
2. uptime / availability;
3. maintenance labor / parts;
4. safety incident and near-miss denominator;
5. cycle-time / units-per-hour comparison;
6. energy consumption;
7. all-in TCO / RaaS cost;
8. human-equivalent labor and supervision cost;
9. renewal / expansion based on measured ROI;
10. same metrics across multiple independent customer sites.

### Why Physical AI remains an incomplete downstream chain

v0.3 materially strengthens the production-workflow layer, but most frontier Physical AI announcements still emphasize:
- capability;
- generalized policies;
- demos;
- pilot deployments.

The report needs **production economics**, not more showcase examples.

Therefore the honest conclusion remains:

> Physical AI now has credible evidence of narrow production-grade deployments and, in mature warehouse robotics, AI-enhanced fleet-scale efficiency. What remains incompletely observed is the transition from repeated real-world task execution to independently verified reliability, safety, TCO and broad fleet economics.

---

# 5. Cross-domain evidence matrix

| Domain | Causal task effect | Verified workflow outcome | Organization-scale effect | Economy/system-scale effect |
|---|---|---|---|---|
| Customer support | relatively strong | moderate/strong | partial | weak |
| Labor-market staffing / hiring | exposure + adoption evidence | N/A as workflow | **partial: hiring-pipeline signals now observable** | weak / non-causal |
| Software engineering | mixed, improving evidence | moderate | weak | weak |
| Education | multiple RCTs incl. school-scale + delayed assessment | **moderate/strong** | **partial** | weak |
| Industrial robotics | mature deployment stats | strong for traditional robotics | strong in selected industries | strong historical evidence |
| Frontier Physical AI | capability + several real production deployments | **moderate/strong for narrow tasks** | **partial** | very weak |

This table is intentionally asymmetric.

The report should not force all domains to the same confidence level.

---

# 6. How to strengthen Chapters 15 / 25 / 26 later

## 6.1 Labor
Prioritize:
- causal firm adoption studies;
- linked employer-employee data;
- hiring / wage / hours outcomes;
- occupation-level task redesign.

## 6.2 Education
Prioritize:
- preregistered RCTs;
- delayed retention;
- transfer;
- implementation cost;
- teacher workload;
- multi-school replication.

## 6.3 Physical AI
Prioritize:
- real fleet operating hours;
- intervention rates;
- uptime;
- production cycle time;
- TCO;
- renewal / deployment expansion.

---

# 7. Relationship to Verified Workflow Economics

All three downstream domains must reuse P0-3; §17 is authoritative for the common economic denominator.

### Labor
```text
Cost per verified support resolution
Cost per merged/accepted software task
```

### 7.2 Education
```text
Cost per retained mastery outcome
```

not cost per AI interaction.

### 7.3 Physical AI
```text
Cost per verified physical task
```

including:
- depreciation;
- energy;
- maintenance;
- human intervention;
- downtime;
- safety / remediation.

This gives the whole report one downstream economic language.

---

# 8. v0.4 conclusion

The downstream chapters do not need more confident prose.

They need better **denominators and longitudinal data**.

The correct upgrade is:

> from “AI can do task X”  
> to “AI changes verified outcome Y at cost Z, persists for period T, and changes organization/system behavior through observable mechanism M.”

Until that chain exists, uncertainty should remain explicit.

**v0.4 stop rule:** generic capability demos, benchmark gains, adoption headlines, or additional productivity percentages do not justify a version bump unless they close a currently missing downstream link: staffing / organizational transmission, delayed retention / transfer, verified production reliability, TCO, or economy/system-scale consequence.

## Sources

- Brynjolfsson, E.; Li, D.; Raymond, L., **Generative AI at Work**, NBER Working Paper 31161 / QJE 2025: https://www.nber.org/papers/w31161
- METR, **Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity**: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- Gambacorta, L.; Qiu, H.; Shan, S.; Rees, D. M., **Generative AI and labour productivity: A quasi experiment on coding**, 2026: https://www.sciencedirect.com/science/article/pii/S1572308926000458
- Kestin, G. et al., **AI tutoring outperforms in-class active learning**, *Scientific Reports* 2025: https://doi.org/10.1038/s41598-025-97652-6
- Wang, R. E. et al., **Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise**, 2025: https://doi.org/10.26300/81nh-8262
- International Federation of Robotics, **World Robotics 2025**: https://ifr.org/worldrobotics/report-2025


## Physical-AI production sources added in v0.3

- BMW Group, 2026, Figure 02 / Spartanburg production deployment — ~1,250 operating hours, 90,000+ components, 30,000+ X3 vehicles, shift operation and integration/safety lessons: https://www.bmwgroup.com/en/news/general/2026/humanoid-robot-in-leipzig.html
- BMW Group press release, 2026-02-27 — standardized-interface integration and production/safety context: https://www.press.bmwgroup.com/global/article/detail/T0455864EN/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for-the-first-time
- GXO, 2024-06-27 — multi-year Digit RaaS agreement and live warehouse task identity: https://gxo.com/news_article/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics/
- Agility Robotics — Digit 100,000+ tote milestone at GXO; vendor-reported operational metric: https://www.agilityrobotics.com/content/digit-moves-over-100k-totes
- Agility Robotics, 2026 — 65,000+ operating hours across deployment commitments at nine customer facilities; vendor-reported aggregate: https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi
- Amazon, 2025-06-30 — one-million-robot fleet across 300+ facilities and DeepFleet ~10% robot-travel-time improvement: https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model
