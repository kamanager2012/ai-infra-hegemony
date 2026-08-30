# Part II · Chapter 14: Agent-Native Software and AI Software Unit Economics

## 1. Agent-native software changes the cost structure

Traditional SaaS typically has low software-replication cost, and seat growth does not necessarily increase variable compute linearly.

Agent-native software is different. A single task may trigger retrieval, reasoning, multiple model calls, tool invocation, browser/action execution, retries, and human review.

The cost unit therefore shifts from:

> **account / seat**

toward:

> **workflow execution**

## 1A. 2026 adoption baseline: AI is widespread, but agent deployment remains early

Stanford AI Index 2026 reports that **88%** of surveyed organizations say they use AI and **70%** use Generative AI in at least one business function. Yet AI-agent deployment remains in the **single digits across nearly all business functions**.[^3]

The correct reading is not a fixed penetration forecast. It is a stage-of-market distinction:

> **Broad AI adoption has already occurred, while production-grade autonomous or semi-autonomous workflow deployment is still early.**

That creates a large potential workflow pool, but production reliability, review burden, integration cost, and unit economics have not yet been proven at the same scale.

Anthropic's June 2026 Economic Index also reports that its product usage has shifted toward more long-running agentic tasks and that higher compute use is associated with higher estimated artifact value.[^4] Because this is first-party product telemetry, it should not be treated as representative of the entire enterprise-software market.

## 1B. AI Inheritance Effect: AI inherits decades of Information Technology installed base

Moving a physical industrial process into the digital domain usually requires sensors, networks, databases, software, identity systems, process digitization, and organizational change. A highly digitized organization starts from a different position: ERP, CRM, MES, CAD/PLM, databases, cloud systems, APIs, digital documents, source code, identity/access systems, and workflow logs already form a reusable digital substrate.

This report defines the structural advantage created when **AI can add an intelligence layer on top of existing digital assets and workflows without rebuilding the full digital foundation** as the **AI Inheritance Effect**.

The demand transmission is:

> **Digital Installed Base → AI Overlay → Workflow Penetration → Automation Depth → Workload Volume → Infrastructure Demand**

Long-run AI-infrastructure demand therefore does not depend only on whether individual models keep scaling upward. It also depends on **how many existing digital workflows begin invoking AI and how deeply each workflow moves from assistant features toward semi-autonomous or autonomous execution**.

This mechanism is compatible with Algorithmic Efficiency:

- compute / memory required per task can keep falling;
- the number of workflows for which AI becomes economical can expand;
- execution frequency and agent depth inside each workflow can rise;
- aggregate infrastructure demand therefore depends on whether **unit resource intensity falls faster or slower than workflow penetration and execution volume rise**.

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

The more defensible statement is therefore:

> **Relative to Industrial → Digital transformation, highly digitized organizations generally face lower marginal transformation cost when moving from Digital → AI. AI can inherit the IT installed base, but it cannot skip production integration or responsibility constraints.**

## 2. There is no universal end-state for "AI SaaS gross margin"

Variable cost differs by product and depends on model choice, context length, caching, retrieval, tools/APIs, failure/retry rates, human review, pricing model, and task depth.

This report therefore does not treat a fixed path such as "traditional SaaS 85% → AI SaaS 55%" as fact.

It uses **AI Software Unit Economics** instead.

## 3. Core unit-economics formula

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

## 4. Agent depth determines the cost curve

A shallow assistant may look like:

> single prompt → single response

A deeper agent looks more like:

> plan → retrieve → reason → tool call → inspect → retry → finalize

As loop depth grows, compute, tool usage, and the failure surface all expand.

Agent products therefore have to optimize:

- task success;
- loop length;
- model routing;
- caching;
- tool reliability;
- failure / retry rate.

## 5. Why seat pricing comes under pressure

Seat pricing can remain effective for summarization, autocomplete, and shallow-assistant products.

If one seat can launch research, coding, support, sales, and operations workflows with very different depths, compute variance becomes much larger.

Long-run pricing can therefore shift toward combinations of:

- usage;
- credits;
- workflow;
- outcome;
- hybrid models.

This does not imply that seat pricing disappears. It means agent depth weakens the correlation between a seat and real variable cost.

## 6. Multi-model routing becomes a foundational software capability

Sending every task to the most expensive model directly damages unit economics.

A more efficient system design can use:

- cheap / local models for classification, extraction, and high-volume routine work;
- medium models for routine reasoning;
- frontier models for complex tasks and high-uncertainty decisions;
- specialist/custom models for stable professional workloads.

Routing is a dynamic allocation problem across quality, latency, cost, and failure probability.

## 7. Open source can move profit from "model capability" toward workflow and distribution

Open-source models increase portability, pressure API premiums, expand private deployment, and improve buyer bargaining power.

Model capability itself therefore becomes harder to preserve as permanent software margin.

More durable value can move toward:

- proprietary workflow;
- domain data / context;
- distribution;
- integration;
- trust / compliance;
- measurable outcomes.

## 8. Cloud System-Stack Competition can transmit into application cost

Software companies usually do not purchase HBM, CoWoS, or grid capacity directly.

Cloud pricing, however, embeds accelerator, memory, networking, data-center, and power costs.

If hyperscaler custom stacks lower real system TCO, part of that benefit can transmit over time through instance or API pricing into the application layer.

Infrastructure competition around Google Ironwood TPU, AWS Trainium3, and other systems therefore affects software contribution margin as well as the chip market.[^1][^2]

## 8A. Workflow Elasticity: lower unit cost does not imply lower total infrastructure demand

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

## 9. Human review is an often-underestimated variable cost

In high-risk workflows such as legal, finance, and enterprise operations, human review may remain necessary for a long time.

If agent-generation speed rises 10× but review burden does not fall, labor has simply moved from production to verification.

True automation ROI should include:

> **Human time before − Human time after − new review / exception-handling time**

rather than measuring AI usage or generated tokens alone.

## 10. Where high-quality profit in agent-native software can come from

Products with stronger long-run economics are more likely to combine:

- high workflow completion;
- low variable AI cost;
- low retry / review burden;
- strong proprietary context;
- distribution;
- measurable customer ROI;
- the ability to route across models and providers.

Software competition is therefore moving from feature competition toward **workflow economics competition**.

## 11. Current judgment

AI is moving part of software from low-marginal-cost replication toward real-time compute-consuming workflow systems.

This can compress some traditional software margins, but it does not imply that all software becomes a low-margin business.

The dividing line is:

> **who can convert model calls into repeatable, verifiable, low-failure, monetizable business outcomes while keeping workflow-demand growth inside sustainable unit economics.**

## References

[^1]: Google Cloud, “Ironwood TPU,” https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/
[^2]: Amazon Web Services, “Amazon EC2 Trn3 UltraServers,” https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/
[^3]: Stanford HAI, “2026 AI Index Report — Economy,” organizational AI adoption, Generative AI use, and early-stage agent deployment, https://hai.stanford.edu/ai-index/2026-ai-index-report/economy
[^4]: Anthropic, “Anthropic Economic Index report: Cadences,” 2026-06-26, long-running agentic tasks and the relationship between compute use and estimated artifact value; first-party product sample, https://www.anthropic.com/research/economic-index-june-2026-report

## Cross-references

- [Chapter 10: Model Unit Economics, Algorithmic Efficiency, and Open-Source Competition](part-II-ch10-model-economics.md)
- [Chapter 12: Hyperscaler System-Stack Competition](part-II-ch12-hyperscaler-system-stack.md)
- [Chapter 20: Value Capture Map](part-III-ch20-value-capture-map.md)
- [Chapter 25: AI and Labor Markets](part-III-ch25-labor-market.md)
