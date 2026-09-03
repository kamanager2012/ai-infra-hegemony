# Part II · Chapter 14: Agent-Native Software and AI Software Unit Economics

> **Role in the report — demand-side validation module.** This chapter tests whether installed AI infrastructure can convert into repeatable, monetizable workflows. It informs demand duration and utilization, but it is not direct evidence of scarce-layer allocation and does not independently determine S1–S4.

## 1. The unit of software economics shifts from seat to workflow

Traditional SaaS can often add seats without proportional increases in variable compute. Agent-native software cannot assume the same cost structure.

A single workflow may trigger retrieval, reasoning, multiple model calls, tool invocation, browser/action execution, retries, and human review.

The cost unit shifts from:

> **account / seat**

toward:

> **workflow execution**

## 1A. 2026 evidence baseline: broad AI use, early scaled-agent deployment

Stanford AI Index 2026 summarizes organizational survey evidence collected in 2025: **88% of respondents say their organization uses AI in at least one business function**, while **79% say their organization regularly uses Generative AI in at least one function**.[^3] The same chapter shows that **scaled AI-agent use remains in the single digits for the cross-function aggregate across nearly all business functions**, while specific industry/function pairs can be materially higher: in the technology sector, scaled use reaches **24% in software engineering, 22% in IT, and 21% in service operations**.[^3]

The underlying survey evidence is **self-reported**. Stanford explicitly says these results should be viewed as **directional rather than comprehensive**; they measure reported organizational use and deployment stage, not independently observed production telemetry or verified workflow utilization.

The correct reading is not a fixed penetration forecast, but a stage-of-market distinction:

> **Broad AI adoption has already occurred, while production-grade autonomous or semi-autonomous workflow deployment is still early.**

That creates a large potential workflow pool, but production reliability, review burden, integration cost, and unit economics have not yet been demonstrated at the same scale.

Anthropic's June 2026 Economic Index also reports that its product usage has shifted toward more long-running agentic tasks and that higher compute use is associated with higher estimated artifact value.[^4] Because this is first-party product telemetry, it should not be treated as representative of the entire enterprise-software market.

## 1B. AI inheritance: IT is the installed base

Moving a physical industrial process into the digital domain usually requires sensors, networks, databases, software, identity systems, process digitization, and organizational change. A highly digitized organization starts from a different position: ERP, CRM, MES, CAD/PLM, databases, cloud systems, APIs, digital documents, source code, identity/access systems, and workflow logs already form a reusable digital substrate.

The report uses **AI inheritance** as shorthand for the structural advantage created when AI can add an intelligence layer on top of existing digital assets and workflows without rebuilding the full digital foundation.

The demand transmission is:

> **Digital Installed Base → AI Overlay → Workflow Penetration → Automation Depth → Workload Volume → Infrastructure Demand**

Long-run AI-infrastructure demand does not depend only on whether individual models keep scaling upward. It also depends on **how many existing digital workflows begin invoking AI and how deeply each workflow moves from assistant features toward semi-autonomous or autonomous execution**.

This mechanism is compatible with algorithmic efficiency:

- compute / memory required per task can keep falling;
- the number of workflows for which AI becomes economical can expand;
- execution frequency and agent depth inside each workflow can rise;
- aggregate infrastructure demand depends on whether **unit resource intensity falls faster or slower than workflow penetration and execution volume rise**.

### Boundary: lower Digital → AI friction does not mean zero-friction deployment

Existing digital infrastructure can reduce marginal deployment friction, but production-grade AI can still be constrained by:

- data quality / access;
- legacy integration;
- identity / permission;
- security / privacy;
- compliance / responsibility;
- workflow redesign;
- reliability / observability;
- human review;
- unit economics.

Physical AI and industrial processes that are not yet digitized still require sensorization, control integration, qualification, safety engineering, and field modification.

A more defensible statement is:

> **Relative to Industrial → Digital transformation, highly digitized organizations generally face lower marginal transformation cost when moving from Digital → AI. AI can inherit the IT installed base, but it cannot skip production integration or responsibility constraints.**

## 2. There is no universal AI-software margin structure

Variable cost differs by product and depends on model choice, context length, caching, retrieval, tools/APIs, failure/retry rates, human review, pricing model, and task depth.

A fixed path such as "traditional SaaS 85% → AI SaaS 55%" is not treated as fact.

The report uses **AI Software Unit Economics** instead.

## 3. Core unit-economics identity

A production workflow can be approximated as:

> **Contribution Margin = Revenue / Productivity Value per workflow − Variable AI cost − Tools/APIs − Human review**

Variable AI cost includes at least:

- inference;
- retrieval / storage;
- model routing;
- retries;
- observability;
- failure handling.

The optimization target is **cost per successfully completed workflow**, not merely cost per token.

## 4. Agent depth changes the cost curve

A shallow assistant may look like:

> single prompt → single response

A deeper agent looks more like:

> plan → retrieve → reason → tool call → inspect → retry → finalize

As loop depth grows, compute, tool usage, and the failure surface all expand.

Agent products must optimize:

- task success;
- loop length;
- model routing;
- caching;
- tool reliability;
- failure / retry rate.

## 5. Seat pricing comes under pressure

Seat pricing can remain effective for summarization, autocomplete, and shallow-assistant products.

If one seat can launch research, coding, support, sales, and operations workflows with very different depths, compute variance becomes much larger.

Long-run pricing can shift toward combinations of:

- usage;
- credits;
- workflow;
- outcome;
- hybrid models.

This does not imply that seat pricing disappears. It means agent depth weakens the correlation between a seat and real variable cost.

## 6. Multi-model routing becomes infrastructure

Sending every task to the most expensive model directly weakens unit economics.

A more efficient system design can use:

- cheap / local models for classification, extraction, and high-volume routine work;
- medium models for routine reasoning;
- frontier models for complex tasks and high-uncertainty decisions;
- specialist/custom models for stable professional workloads.

Routing is a dynamic allocation problem across quality, latency, cost, and failure probability.

## 7. Open source can move profit toward workflow and distribution

Open-source models increase portability, pressure API premiums, expand private deployment, and improve buyer bargaining power.

Model capability itself becomes harder to preserve as permanent software margin.

More durable value can move toward:

- proprietary workflow;
- domain data / context;
- distribution;
- integration;
- trust / compliance;
- measurable outcomes.

## 8. System-stack competition can transmit into application cost

Software companies usually do not purchase HBM, CoWoS, or grid capacity directly.

Cloud pricing, however, embeds accelerator, memory, networking, data-center, and power costs.

If hyperscaler custom stacks lower real system TCO, **application-layer benefit still depends on cloud pricing pass-through**. The cited Ironwood and Trainium disclosures establish alternative infrastructure systems; they do not by themselves prove that lower infrastructure TCO has already been transmitted into instance/API pricing or software contribution margin.[^1][^2]

The report therefore treats system-TCO → cloud-price → application-margin transmission as a **conditional mechanism to monitor**, not as an observed pricing fact.

## 8A. Workflow elasticity: lower unit cost does not imply lower total demand

Once agent software turns model calls into workflow execution, aggregate infrastructure demand can be approximated as:

```text
Total AI Infrastructure Demand
≈ Workflow Count
× Attempts per Workflow
× Resource Intensity per Attempt
```

Lower model prices or more efficient routing reduce only part of this expression.

If lower cost also produces:

- more users;
- longer agent loops;
- more tool calls;
- deeper retry / exploration;
- automation of workflows that were previously uneconomic;

then total compute / memory / network demand can still rise.

The software layer's feedback into infrastructure is therefore better summarized as:

> **cost per verified workflow × demand elasticity**

This is why agent adoption can compress model-layer margin while still expanding aggregate use of cloud, accelerators, memory, and networking.

## 9. Human review is a variable-cost line

In high-risk workflows such as legal, finance, and enterprise operations, human review may remain necessary for a long time.

If agent-generation speed rises 10× but review burden does not fall, labor has simply moved from production to verification.

True automation ROI should include:

> **Human time before − Human time after − new review / exception-handling time**

rather than measuring AI usage or generated tokens alone.

## 10. Sources of durable software profit

Products with stronger long-run economics are more likely to combine:

- high workflow completion;
- low variable AI cost;
- low retry / review burden;
- strong proprietary context;
- distribution;
- measurable customer ROI;
- the ability to route across models and providers.

Software competition is moving from feature competition toward **workflow economics competition**.

## 11. Current read

AI is moving part of software from low-marginal-cost replication toward real-time compute-consuming workflow systems.

This can compress some traditional software margins, but it does not imply that all software becomes low-margin.

The dividing line is:

> **who can convert model calls into repeatable, verifiable, low-failure, monetizable business outcomes while keeping workflow-demand growth inside sustainable unit economics.**

## References

[^1]: Google Cloud, “Ironwood TPU,” https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/
[^2]: Amazon Web Services, “Amazon EC2 Trn3 UltraServers,” https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/
[^3]: Stanford HAI, “2026 AI Index Report — Economy,” full Chapter 4 / Figures 4.3.1, 4.3.7 and 4.3.8, based on McKinsey's 2025 organizational survey: 88% AI use and 79% regular Generative-AI use in at least one business function; scaled AI-agent use is in the single digits across nearly all business functions in the aggregate, while the technology sector reaches 24% in software engineering, 22% in IT, and 21% in service operations. Stanford also states that the survey results are self-reported and should be viewed as directional rather than comprehensive. The chapter-highlight webpage separately prints 70% for GenAI, so this report follows the full chapter figure/text rather than that inconsistent highlight, https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_4_economy.pdf
[^4]: Anthropic, “Anthropic Economic Index report: Cadences,” 2026-06-26, long-running agentic tasks and the relationship between compute use and estimated artifact value; first-party product sample, https://www.anthropic.com/research/economic-index-june-2026-report

## Cross-references

- [Chapter 10: Model Unit Economics, Algorithmic Efficiency, and Open-Source Competition](part-II-ch10-model-economics.md)
- [Chapter 12: Hyperscaler System-Stack Competition](part-II-ch12-hyperscaler-system-stack.md)
- [Chapter 20: Value Capture Map](part-III-ch20-value-capture-map.md)
- [Chapter 25: AI and Labor Markets](part-III-ch25-labor-market.md)
