# Part III · Chapter 26: Education and Talent Systems in the AI Era

> **Role in the report — second-order talent-system module.** Education and skills indicators describe adaptation to the AI production system. They are downstream implications, not evidence that upstream infrastructure concentration or any S1–S4 state has been established.

## 1. Durable talent advantage comes from system understanding, not tool familiarity

This report treats prompting, model calls, and basic automation as capabilities with relatively low barriers to diffusion. The more durable advantage is expected to come from understanding how models, software, compute, data, power, economics, and responsibility interact in a production system.

The more durable capability stack includes:

- models;
- data;
- compute;
- memory;
- software;
- networking;
- power;
- economics;
- responsibility.

This mirrors the industrial shift from competition around a single chip toward competition around the system stack.

## 2. Adoption is moving faster than curriculum and policy

The Stanford HAI 2026 AI Index Education chapter summarizes several adoption and education-system indicators:[^1]

- roughly **4 out of 5** U.S. high-school and college students use AI for schoolwork;
- about half of middle/high schools have an AI-use policy;
- the Stanford summary reports that only **6%** of teachers describe their schools as having clear, comprehensive AI policies;
- the Stanford summary reports an **11%** decline in U.S. four-year university CS undergraduate enrollment from 2024 to 2025;
- AI software-related master's graduates grew **17% from 2023 to 2024**.

These figures come from different underlying studies, populations, and definitions. They are directional indicators, not one internally consistent time series or survey denominator.

The pattern is:

> **Tool Adoption > Curriculum Update > Institutional Reform**

The same Stanford chapter reports that **more than 90% of countries** now offer computer science in primary or secondary education, while formal AI education has spread more slowly.[^1] The United Arab Emirates introduced a national mandatory AI curriculum for government schools beginning in the **2025–26 school year**. In China, national policy direction is being accompanied by provincial / municipal curriculum mandates and pilots rather than one uniform nationwide classroom implementation date.

This moves the question from isolated school experimentation toward education-system design at national and subnational levels.

The question is no longer whether students are using AI.

It is whether institutions can verify that students understand, control, and take responsibility for AI-generated outcomes.

### 2A. International frameworks are already moving beyond tool use

UNESCO's AI Competency Framework for Students defines **12 competencies across four dimensions**: human-centred mindset, ethics of AI, AI techniques and applications, and AI system design, organized across Understand → Apply → Create.[^2]

UNESCO's teacher framework defines **15 competencies across five dimensions**: human-centred mindset, ethics of AI, AI foundations and applications, AI pedagogy, and AI for professional learning.[^3]

The direction is consistent with the broader industrial thesis:

> **AI literacy cannot collapse into prompt technique. Durable capability includes judgment, responsibility, system understanding, application design, and verification.**

A curriculum centered on the currently dominant model or tool is likely to become obsolete quickly. System design, verification, domain reasoning, and responsibility are more portable across models and platforms.

### 2B. School-scale learning evidence now exists, but engagement and retention remain binding

Two August 2026 randomized field studies materially improve the evidence base because they observe repeated school use and delayed learning rather than only one-session AI performance.

**Khanmigo two-year school experiment.** Oreopoulos and Low report a two-year cluster randomized trial across **18 Tennessee middle schools** in which assigned students used Khan Academy with Khanmigo during existing daily remedial mathematics sessions.[^4] Assignment increased math achievement by about **1.3 national percentile ranks per term**, or roughly **0.06–0.08 standard deviations over a school year**; the implied effect of a full year of active participation is about **0.14 SD**.[^4]

The result does not show that AI access automatically transforms learning. The gains resemble those from Khan Academy practice without AI assistance, while actual Khanmigo engagement was limited: **96%** of students tried it at least once, but the median student messaged it on only about one-third of practice days and used it in only about **17% of exercise sessions in which a mistake occurred**.[^4]

The practical constraint is therefore partly:

> **access → engagement → instructional workflow → learning outcome**

—not model availability alone.

**NUMI mastery experiment.** A separate randomized experiment with **more than 6,000 middle-school students** assigned AI versus computer-assisted-learning support and mastery versus non-mastery progression.[^5] Students completed a delayed assessment **one week later** covering practiced and unpracticed material.[^5]

During practice, AI support improved error recovery: after mistakes, students were more likely to answer the next attempt correctly and needed fewer attempts to return to a correct answer, although they progressed more slowly and attempted fewer questions.[^5] The delayed-learning evidence was more limited and context-dependent than the immediate assistance effect, with the most encouraging results arising when AI support was embedded in a mastery workflow rather than offered as a generic shortcut.[^5]

This establishes a more disciplined boundary:

> **immediate AI-assisted correctness ≠ broad delayed retention or transfer.**

The education evidence chain has therefore advanced from adoption-only indicators toward:

> **repeated school deployment → measurable learning effect → partial delayed-retention evidence.**

What remains unresolved at the same standard is:
- broad transfer across topics;
- teacher workload / organizational redesign;
- all-in implementation and support cost;
- persistent multi-year learning;
- system-scale economics across heterogeneous schools.

**Scope note:** Sections 3–11 are report recommendations derived from the industrial framework and cited competency models. They are not presented as externally validated causal findings about one optimal curriculum.

## 3. Layer one: AI literacy

All disciplines need a basic understanding of:

- model limitations;
- hallucination;
- source verification;
- privacy;
- data leakage;
- bias;
- responsible use.

AI literacy is becoming a general digital competency rather than an elective skill for AI specialists.

## 4. Layer two: workflow engineering

Many roles do not require training a foundation model.

They do require:

- model selection;
- context / prompt design;
- retrieval;
- tool orchestration;
- evaluation;
- automation;
- human review.

This forms the application layer of AI engineering.

## 5. Layer three: system engineering

Frontier AI requires accelerators, HBM, networking, distributed computing, compiler/runtime, data centers, and power.

Top-tier AI engineering education therefore must cross:

> **computer science + computer architecture + systems/networking + infrastructure economics**

Model-only coursework cannot capture real industrial constraints.

## 6. Hardware and software cannot remain fully separated

Inference optimization can simultaneously involve:

- quantization;
- kernels;
- HBM bandwidth;
- interconnect;
- batching;
- power.

Future curricula therefore need more cross-layer labs, real performance/cost measurement, and system debugging.

## 7. Multi-stack capability is a strategic skill

Engineers should not learn only a single proprietary stack.

Higher-value capability includes understanding:

- CUDA;
- alternative accelerator stacks;
- cloud custom silicon;
- open compiler/runtime;
- distributed frameworks;

and being able to migrate workloads across systems.

The educational goal is portability, not platform loyalty.

## 8. Physical AI requires a different interdisciplinary stack

Robotics / Physical AI combines control, mechanics, sensing, embedded compute, AI, and safety.

A scarce future skill is likely to be the ability to connect model capability with physical-world reliability.

## 9. Power / cooling / operations belong inside the talent stack

AI data-center buildout makes electrical distribution, power engineering, liquid cooling, networking, and operations part of AI infrastructure.

"AI talent" therefore cannot be measured only by the number of ML engineers.

## 10. Entry-level education must adapt to task compression

If drafting, routine coding, and basic research are increasingly performed by agents, students need earlier exposure to:

- system debugging;
- verification;
- architecture;
- real-world projects;
- responsibility.

Otherwise, education risks continuing to invest heavily in the tasks most likely to be automated first.

## 11. Assessment must measure verification and responsibility

A stronger project-based assessment should require students to explain:

- output correctness;
- source / evidence;
- system design;
- cost;
- reliability;
- power / resource use;
- safety / responsibility.

That is closer to real industrial capability than simply banning AI tools.

## 12. Current read

The evidence now shows that AI-enabled tutoring can produce measurable learning gains in real school settings, but access alone is insufficient: engagement, instructional design, retention, and implementation remain binding. The central educational change is therefore not simply to "create another AI major."

It is:

> **make AI a systems capability across technical and professional education while raising verification, portability, and responsibility into core learning objectives.**

The most durable talent advantage is unlikely to come simply from being best at calling models.

It is more likely to come from the ability to understand systems, verify results, evaluate economics, migrate across stacks, and take responsibility for real-world consequences.

## References

[^1]: Stanford Institute for Human-Centered Artificial Intelligence, “2026 AI Index Report — Education,” https://hai.stanford.edu/ai-index/2026-ai-index-report/education
[^2]: UNESCO, “AI competency framework for students,” 2024, updated 2026-01-16, https://www.unesco.org/en/articles/ai-competency-framework-students?hub=66903
[^3]: UNESCO, “AI competency framework for teachers,” 2024, updated 2026-01-16, https://www.unesco.org/en/articles/ai-competency-framework-teachers?hub=779


[^4]: Philip Oreopoulos and Nina Low, “One Click Away: AI Tutoring with Khanmigo in a Two-Year School Experiment,” NBER Working Paper 35620, August 2026, https://www.nber.org/papers/w35620
[^5]: Philip Oreopoulos, Michael Liut, Alp Sungu, and Nina Low, “Making AI Tutoring Productive: Evidence from a Mastery-Based Math Practice Experiment,” NBER Working Paper 35621, August 2026, https://www.nber.org/papers/w35621
