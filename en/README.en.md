# The Age of AI Infrastructure Hegemony

**Structural Reallocation of Compute, Semiconductors, Memory, Advanced Packaging, Power, and Capital**

A long-form industry research report on AI infrastructure, semiconductors, cloud systems, capital formation, and industrial strategy.

**Retrieval and revision cutoff: August 28, 2026**

[Read the 32-chapter English report](publication/README.md) · [Executive Summary](publication/part-I-ch01-executive-summary.md) · [Master Judgment](publication/part-IV-ch32-master-judgment.md) · [中文](../README.zh-CN.md)

---

## What this report studies

AI competition is moving from "who has the faster accelerator" toward the full **system stack**:

> **advanced logic + HBM + advanced packaging + interconnect + compiler/runtime + rack/data center + power + capital + workload**

The report examines how that shift changes:

- competition between NVIDIA and hyperscaler custom systems;
- resource allocation across TSMC, HBM, and advanced packaging;
- where the next semiconductor and infrastructure capital dollar goes;
- power, LPS, and Time-to-Power as deployment constraints;
- model companies evolving from cloud tenants into Anchor Compute Buyers;
- residual supply available to smartphones, PCs, automotive, and industrial markets;
- China's production-grade parallel stack and autonomous frontier closure;
- AI-infrastructure CapEx, depreciation, financing, and capital clearing;
- Agent-Native Software, Physical AI, labor, and talent systems;
- conditional industrial states for 2026–2036.

---

## Core findings

### 1. The competitive unit has moved from the chip to the system stack

NVIDIA's current advantage cannot be explained by GPU benchmarks or market share alone.

Competition now spans compute, memory, interconnect, software, rack architecture, data centers, and power. Google Ironwood, AWS Trainium3, Microsoft Maia, Meta MTIA, and AMD Instinct/ROCm are also moving toward fuller system stacks.

The long-run question is not:

> Who owns the fastest chip?

It is:

> **Who can continuously deliver complete systems to real workloads with lower migration cost, high utilization, and reliable supply?**

### 2. AI is changing where the next semiconductor capital dollar goes

TSMC's 2Q26 HPC platform represented **66%** of revenue, while advanced technologies at 7 nm and below represented **77%** of wafer revenue. These are revenue-mix measures, not AI wafer share, but they show that HPC has become one of the central marginal drivers of advanced-manufacturing capital formation.

The report describes this as a **Two-Speed Semiconductor Economy**:

> The AI Infrastructure Economy and the Traditional Device Economy share upstream resources, but differ in willingness to pay, order duration, prepayment capacity, and the ability to induce new capital formation.

### 3. Total supply growth does not mean traditional industries receive more supply

The report uses **Non-AI Residual Capacity**:

```text
NonAI_Residual
= Effective_Supply
- AI_Absorption
- Other_Priority_Demand
```

Global wafer, DRAM, or packaging capacity can rise while smartphones, PCs, automotive, and industrial buyers still face higher prices, weaker allocation, or slower configuration upgrades.

### 4. HBM manufacturing intensity cannot be inferred from bit share alone

Micron disclosed that, under **same technology node / same number of bits** conditions, HBM3E requires approximately **3× the wafer supply of DDR5**.

This is a manufacturing-input trade ratio, not a price multiple and not a permanent constant for every HBM generation.

TrendForce's estimate that HBM + RDIMM will represent approximately **51% of 2026 DRAM bit supply** remains a **2026E institutional forecast**, not a full-year actual.

### 5. Advanced Packaging and Power are independent constraints

TSMC has explicitly stated that advanced-packaging tightness can limit customer growth.

High-density AI systems also push scarcity into:

- powered land;
- grid interconnection;
- substations;
- cooling;
- firm power;
- permitting.

The 2026-08-17 PORTS-Pike project extends this further into **land + power + shell (LPS)**. NVIDIA disclosed credit support for an initial **4.25 IT-GW** design capacity with OpenAI as the customer, with phased delivery planned from 2028.

The report strictly separates:

> **secured / contracted capacity ≠ energized capacity ≠ utilized AI load**

and also:

> **IT-GW ≠ generation GW ≠ PPA capacity**

### 6. Model companies are becoming Anchor Compute Buyers

OpenAI Stargate and Anthropic/AWS show that leading model companies are no longer simply renting whatever cloud capacity already exists.

Long-duration model demand can create:

> **revenue visibility → financing certainty → earlier infrastructure buildout → earlier resource reservation**

The same mechanism can also raise customer-concentration and duration risk.

### 7. Capital competition is expanding beyond corporate CapEx

On 2026-08-10, NVIDIA announced AI compute-infrastructure financing platforms with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs, and KKR, targeting **more than US$500B of third-party capital mobilization over time**.

This is a mobilization target, not funded, committed, or deployed capital.

The development matters because AI compute is increasingly being structured as a long-duration infrastructure-finance asset, not merely purchased through hyperscaler corporate CapEx.

### 8. China must be assessed through two levels of closure

China has moved beyond the stage of having no substitute system, but two different questions must be kept separate.

**Production-Grade Parallel Stack** asks whether a substitute system can run real production workloads across:

- accelerator / compute;
- HBM-class or equivalent memory subsystem;
- advanced packaging;
- high-speed interconnect;
- compiler/runtime;
- production workload;
- utilization, reliability, and economics.

**Autonomous Frontier Closure** asks whether the stack can continue scaling across generations when critical external inputs are constrained, which additionally requires:

- advanced-manufacturing continuity;
- equipment / materials / software / service;
- cross-generation process upgrades;
- durable HBM / packaging / LPS / power / capital formation.

Import dependence does not mean there is no production-grade parallel stack. Conversely, production deployment does not prove autonomous frontier closure.

### 9. The current evidence mix is closest to S2 — Baseline Concentration

The report uses four conditional states rather than one 2036 point forecast:

- **S1 — Competitive Expansion**
- **S2 — Baseline Concentration**
- **S3 — Resource Hegemony**
- **S4 — Capital Hard Landing**

As of August 2026, the evidence mix is closest to **S2**:

> **high growth, high concentration, and credible substitution paths coexist.**

---

## Research method

The report uses:

> **F → H → M → S → X**

- **F — Fact:** observed and publicly verifiable;
- **H — Hypothesis:** a future input condition;
- **M — Mechanism:** the causal transmission between variables;
- **S — Scenario:** a future state created by a set of conditions;
- **X — Falsification:** evidence strong enough to force the judgment to change.

Evidence is also separated into:

- **A:** first-party / formal evidence;
- **B:** institutional / academic research;
- **C:** sell-side / supply-chain / media estimate;
- **D:** report-side calculation / sensitivity / scenario input.

Core rule:

> **Observed facts must be accurate. Future analysis can be bold, but its conditions, denominators, evidence identity, and falsification criteria must remain explicit.**

---

## Reading paths

### Fastest path

1. [Chapter 1 — Executive Summary](publication/part-I-ch01-executive-summary.md)
2. [Chapter 32 — Master Judgment](publication/part-IV-ch32-master-judgment.md)
3. [Chapter 30 — S1–S4 Scenarios](publication/part-IV-ch30-scenarios.md)

### Full report

- [32-chapter English report](publication/README.md)
- [Scope and Evidence Boundaries](publication/00-front-matter.md)
- [List of Tables](publication/02-list-of-tables.md)
- [Abbreviations and Core Glossary](publication/03-abbreviations-and-glossary.md)
- [Research Transparency, Limitations, and Correction Policy](publication/04-research-transparency.md)
- [Competitive Set, Substitution Paths, and Counter-Evidence Matrix](publication/05-competitive-evidence-matrix.md)

### Evidence and methodology

- [Chapter 27 — Research Method and Evidence Architecture](publication/part-IV-ch27-research-method.md)
- [Core Evidence Ledger](核心证据台账.en.md)
- [Core Source Index](核心参考文献索引.en.md)
- [Core Concepts and Model Index](核心概念与模型索引.en.md)
- [Core Hypothesis Matrix](核心假设矩阵.en.md)
- [External Research Comparison Index](外部研究对照索引.en.md)

---

## Evidence boundaries that must not be crossed

Unless direct evidence exists, the report does not infer:

- revenue share → wafer share;
- customer revenue → CoWoS allocation;
- HBM demand share → actual packaging allocation;
- contracted / secured capacity → energized / utilized load;
- IT-GW → generation GW;
- company-wide CapEx → AI hardware CapEx;
- model-training compute → full corporate R&D cost;
- occupational exposure → unemployment;
- conventional DRAM / NAND capability → HBM closure;
- production-grade substitution → autonomous frontier closure;
- foundry revenue share → frontier-AI capability.

Facts that appear after the research cutoff are new research inputs. They are not retroactively treated as facts that were already known by August 28, 2026.

---

## Disclaimer

This report is for industry research and information exchange. It does not constitute:

- investment advice;
- a securities rating;
- legal advice;
- an audit opinion;
- a guaranteed forecast or trading recommendation.

Future judgments can change as technology, demand, capital, regulation, geopolitics, and supply evolve.

## Copyright and citation

Original research text is governed by the repository [LICENSE](../LICENSE). Third-party material remains subject to the rights and licenses of its respective owners.

Citation metadata is available in [CITATION.cff](../CITATION.cff).
