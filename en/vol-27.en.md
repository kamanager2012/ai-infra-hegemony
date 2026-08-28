# Volume 27: Agent-Native Software and AI Software Unit Economics

Chinese source edition: [vol-27.md](../vol-27.md)

> Retrieval and revision cutoff: **2026-08-28**. This volume does not assume a universal SaaS gross-margin endpoint. It evaluates AI software through workflow-level variable cost and realized customer value.

## 1. AI software changes the traditional SaaS cost structure

Traditional SaaS often has three favorable characteristics:

- low replication cost;
- infrastructure cost is a relatively small share of revenue;
- adding another seat does not usually increase compute cost linearly.

Agent-native software can behave differently.

One user action may trigger:

- retrieval;
- reasoning;
- multiple model calls;
- tool invocation;
- browser or action execution;
- retries;
- human review.

The relevant cost unit therefore shifts from:

> **cost of maintaining a user account**

toward:

> **cost of executing a workflow successfully.**

## 2. A fixed 85% → 55% margin path is not an industry fact

There is no universal gross-margin endpoint for AI software.

Economics vary with:

- model choice;
- token volume;
- caching;
- retrieval;
- tool and API costs;
- human review;
- pricing model;
- workflow depth.

This report therefore does not use “traditional SaaS 85% → AI SaaS 55%” as an observed industry rule.

It uses **AI Software Unit Economics**.

The purpose is to make the variable-cost drivers explicit rather than embed them in one assumed margin.

## 3. Core workflow-unit economics

A simplified contribution-margin equation is:

```text
Contribution Margin
=
Revenue per Workflow
- Variable AI Cost
- Tool / API Cost
- Human Review Cost
```

Variable AI cost can include:

- inference;
- retrieval;
- storage;
- model routing;
- retries;
- observability.

The key optimization target is therefore:

> **cost per successfully completed workflow**

rather than cost per token alone.

A cheaper token is useful only if the overall workflow remains reliable and does not expand into more retries, tool calls, or human review.

## 4. Why seat pricing can become less informative

Seat pricing can remain effective for relatively shallow features such as:

- summarization;
- autocomplete;
- lightweight assistance.

The economics change when software performs deeper work such as:

- research;
- coding;
- analysis;
- support;
- sales workflows;
- operations.

One seat can then generate very different levels of compute consumption across users.

Agent-native products are therefore more likely to use combinations of:

- usage pricing;
- credits;
- workflow pricing;
- outcome pricing;
- hybrid models.

The pricing model should reflect the execution cost that the product actually incurs.

## 5. Agent depth determines cost structure

A shallow assistant may look like:

**single prompt → single response**

A deeper agent can look like:

**plan  
→ retrieve  
→ reason  
→ call tools  
→ inspect  
→ retry  
→ finalize**

As loop depth rises, inference and tool costs can rise quickly.

Agent products therefore need to optimize several variables simultaneously:

- task success rate;
- loop length;
- model routing;
- caching;
- failure rate.

A system that appears cheap per model call can still be expensive per completed business outcome.

## 6. Multi-model routing becomes a core software capability

A software company does not need to send every task to the most expensive frontier model.

A more efficient architecture can route work by complexity:

- **cheap model:** classification and extraction;
- **medium model:** routine reasoning;
- **frontier model:** complex or high-value tasks;
- **local/custom model:** stable, high-volume workloads.

Routing directly changes unit economics.

It can preserve quality on difficult tasks while reducing the average cost of routine execution.

Model selection therefore becomes part of the software architecture rather than a one-time vendor choice.

## 7. Cloud system-stack competition can flow through to application cost

Most software companies do not directly buy HBM or CoWoS capacity.

But cloud pricing ultimately reflects the cost of:

- accelerators;
- memory;
- networking;
- data centers;
- power.

If cloud system-stack competition lowers compute TCO, some of that reduction can flow into:

- instance prices;
- reserved-compute prices;
- API prices.

This is one reason hyperscaler custom silicon matters to the application layer even when the software vendor never touches the chip directly.

The application layer inherits the economics of the infrastructure beneath it.

## 8. Open models pressure model-layer margins

Open models can:

- reduce model switching cost;
- pressure API pricing;
- expand private deployment;
- increase buyer bargaining power.

Model capability alone therefore becomes a less durable basis for software margin.

More defensible sources of value can shift toward:

- workflow integration;
- proprietary data and context;
- distribution;
- trust and compliance;
- measurable outcomes.

The moat increasingly sits in **what the software gets done**, not simply which model it calls.

## 9. Human review is one of the most frequently omitted variable costs

In high-risk domains such as:

- legal services;
- healthcare;
- finance;
- enterprise operations;

human review can remain necessary for a long time.

If agents generate more output but review work does not fall, the organization may simply move human labor from production into verification.

A useful automation metric is therefore:

```text
Net Human Time Saved
=
Human Time Before
- Human Time After
```

AI usage alone does not measure automation ROI.

## 10. What a durable agent-native software winner looks like

High-quality long-run software economics are more likely when a company combines:

- high workflow-completion rates;
- low variable AI cost;
- strong proprietary context;
- low review burden;
- effective distribution;
- measurable customer ROI.

The competitive unit therefore shifts from a feature checklist toward:

> **workflow economics.**

A product can use the same frontier model as a competitor and still have materially better economics because it routes models better, retries less, integrates more deeply, or creates more customer value per run.

## 11. Current judgment

AI is moving part of software from a low-marginal-cost replicated product toward a system that consumes compute in real time to execute work.

That can compress some traditional software margins, but it does not imply that all AI software becomes low margin.

The decisive dividing line is:

> **Who can convert model calls into repeatable, billable, low-failure business outcomes at sustainable workflow-level economics?**

That is the unit on which agent-native software should be evaluated.
