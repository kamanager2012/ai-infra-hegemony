# P2 · Downstream Empirical Chains v0.1

> **Status:** Research-side evidence map; not part of the frozen formal report.  
> **Goal:** strengthen Labor (Ch25), Education (Ch26), and Physical AI (Ch15) without pretending that the evidence is as mature as semiconductors, memory, packaging, power, or CapEx.

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

### What is already supported

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

### What remains missing

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

### What is already supported

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

### What remains missing

Need more evidence on:
- retention weeks/months later;
- transfer to unseen subjects;
- overreliance / reduced independent problem-solving;
- teacher workload;
- actual implementation and training cost;
- adoption at school-system scale;
- subgroup heterogeneity.

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

### Why Physical AI remains the weakest downstream chapter

Most frontier Physical AI announcements still emphasize:
- capability;
- generalized policies;
- demos;
- pilot deployments.

The report needs **production economics**, not more showcase examples.

Therefore the honest conclusion remains:

> Physical AI has very large upside, but the causal chain from model capability to reliable, economical, scaled physical deployment is still incompletely observed.

---

# 5. Cross-domain evidence matrix

| Domain | Causal task effect | Verified workflow outcome | Organization-scale effect | Economy/system-scale effect |
|---|---|---|---|---|
| Customer support | relatively strong | moderate/strong | partial | weak |
| Software engineering | mixed, improving evidence | moderate | weak | weak |
| Education | several RCT anchors | moderate | weak | weak |
| Industrial robotics | mature deployment stats | strong for traditional robotics | strong in selected industries | strong historical evidence |
| Frontier Physical AI | capability/pilot evidence | weak/moderate | weak | very weak |

This table is intentionally asymmetric.

The report should not force all domains to the same confidence level.

---

# 6. How to strengthen Chapters 15 / 25 / 26 later

## Labor
Prioritize:
- causal firm adoption studies;
- linked employer-employee data;
- hiring / wage / hours outcomes;
- occupation-level task redesign.

## Education
Prioritize:
- preregistered RCTs;
- delayed retention;
- transfer;
- implementation cost;
- teacher workload;
- multi-school replication.

## Physical AI
Prioritize:
- real fleet operating hours;
- intervention rates;
- uptime;
- production cycle time;
- TCO;
- renewal / deployment expansion.

---

# 7. Relationship to Verified Workflow Economics

All three downstream domains should reuse P0-3.

### Labor
```text
Cost per verified support resolution
Cost per merged/accepted software task
```

### Education
```text
Cost per retained mastery outcome
```

not cost per AI interaction.

### Physical AI
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

# 8. v0.1 conclusion

The downstream chapters do not need more confident prose.

They need better **denominators and longitudinal data**.

The correct upgrade is:

> from “AI can do task X”  
> to “AI changes verified outcome Y at cost Z, persists for period T, and changes organization/system behavior through observable mechanism M.”

Until that chain exists, uncertainty should remain explicit.

## Sources

- Brynjolfsson, E.; Li, D.; Raymond, L., **Generative AI at Work**, NBER Working Paper 31161 / QJE 2025: https://www.nber.org/papers/w31161
- METR, **Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity**: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- Gambacorta, L.; Qiu, H.; Shan, S.; Rees, D. M., **Generative AI and labour productivity: A quasi experiment on coding**, 2026: https://www.sciencedirect.com/science/article/pii/S1572308926000458
- Kestin, G. et al., **AI tutoring outperforms in-class active learning**, *Scientific Reports* 2025: https://doi.org/10.1038/s41598-025-97652-6
- Wang, R. E. et al., **Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise**, 2025: https://doi.org/10.26300/81nh-8262
- International Federation of Robotics, **World Robotics 2025**: https://ifr.org/worldrobotics/report-2025
