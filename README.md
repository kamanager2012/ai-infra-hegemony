<div align="center">

# AI Infrastructure Reordering, 2026–2036: A Structural Industry Outlook
### AI基础设施格局重塑：2026–2036结构性产业展望

[![English](https://img.shields.io/badge/Language-English-blue?style=for-the-badge)](README.md)
[![简体中文](https://img.shields.io/badge/语言-简体中文-green?style=for-the-badge)](README.zh-CN.md)
[![Web Edition](https://img.shields.io/badge/Live-Web%20Edition-purple?style=for-the-badge)](https://kamanager2012.github.io/ai-infra-hegemony/)

**English Canonical** | [简体中文版 (README.zh-CN.md)](README.zh-CN.md) | [32-Chapter English Report](en/publication/README.md) | [32章中文完整报告](publication/README.md) | [2026 Q4 Addendum](2026-Q4-ROLLING-ADDENDUM.en.md)

</div>

> [!TIP]
> **中文读者导读：** 本报告由作者团队提供完整中文专业翻译与技术分析。您可以直接点击切换至 **[简体中文主页 (README.zh-CN.md)](README.zh-CN.md)**，或直接阅读 **[32章中文完整报告](publication/README.md)** 与最新 **[2026 Q4 滚动研究补丁 (中文版)](2026-Q4-ROLLING-ADDENDUM.md)**。

---

**How the AI Compute Buildout Is Reallocating Semiconductors, Memory, Advanced Packaging, Power, Capital, and End-Market Capacity**

A long-form industry research report on AI infrastructure, semiconductors, cloud systems, capital formation, and industrial strategy.

Canonical research language: **English**. The Chinese edition is the authorized professional Chinese translation of the English canonical analytical text. Chinese syntax may be localized and standard industry terms may remain in English, but the Chinese edition must not independently add, remove, reorder, or redefine claims, mechanisms, denominators, evidence identities, scenario states, falsification boundaries, or section hierarchy. Any substantive revision is resolved in English first and then translated into Chinese.

**Version:** 1.0  
**Release status:** Final publication snapshot  
**Release date:** September 4, 2026  
**Evidence cutoff:** August 28, 2026  
**Edition revision:** September 14, 2026  
Research claims use evidence available by the cutoff. Later edits in this edition are limited to corrections, evidence-boundary repairs, bilingual parity, and editorial restructuring; the revision history is documented separately.

[Web edition source](docs/) · [Research Brief](en/publication/RESEARCH_BRIEF.md) · [Read the 32-chapter English report](en/publication/README.md) · [Executive Summary](en/publication/part-I-ch01-executive-summary.md) · [Master View](en/publication/part-IV-ch32-master-judgment.md) · [2026 Q4 Rolling Addendum](2026-Q4-ROLLING-ADDENDUM.md) · [中文版](README.zh-CN.md)

> [!NOTE]
> **Rolling Research Update (November 2026):** See [2026 Q4 Rolling Research Addendum](2026-Q4-ROLLING-ADDENDUM.md) for Q3 hyperscaler earnings updates, the FERC decision on Talen/AWS nuclear co-location (validating that secured capacity ≠ energized load), the shift toward test-time reasoning compute, and real-world downstream transmission (PC component & smartphone inflation).

---

## What this report studies

This report does not argue that “only AI matters.” Smartphones, PCs, game consoles, vehicles, industrial equipment, robotics, and long-lifecycle high-reliability electronics remain important. The core question is whether **non-AI end systems can still obtain enough, stable, affordable supply on their own BOM, qualification, lifecycle, and product cadence when AI/HPC demand reprioritizes shared or adjacent upstream resources through higher willingness to pay, longer commitments, and stronger capital formation.**

AI competition is moving from "who has the faster accelerator" toward the full **system stack**:

> **advanced logic + HBM + advanced packaging + interconnect + compiler/runtime + rack/data center + power + capital + workload**

The report examines how that shift changes:

- competition between NVIDIA and hyperscaler custom systems;
- resource allocation across TSMC, HBM, and advanced packaging;
- where the next marginal semiconductor and infrastructure dollar is deployed;
- power, LPS, and Time-to-Power as deployment constraints;
- model companies evolving from cloud tenants into Anchor Compute Buyers;
- residual supply available to smartphones, PCs, game consoles, automotive, and industrial markets;
- China's frontier parallel stack, Production-Grade Gates, and autonomous frontier closure;
- AI-infrastructure CapEx, depreciation, financing, and capital clearing;
- Agent-Native Software, Physical AI, labor, and talent systems;
- conditional industrial states for 2026–2036.

These are not separate topic silos. They form one industrial transmission chain:

> **Physical Supply → System Delivery → Compute Cost and Availability → Workflow Economics → Enterprise Adoption and Cash Flow → Capital Recovery → Second-Order Restructuring of Labor, Talent, and Physical AI**

This is also the report's core framework for the next decade: infrastructure expansion becomes economically durable only when it is converted into verifiable, monetizable, repeatable workflow output.

---

## 2026 load-bearing evidence snapshot

This table is intentionally narrow: it shows the public observations and report-side calculations that currently carry the most analytical weight, together with the denominator boundary that prevents overclaiming.

| Signal | 2026 observation / calculation | Evidence identity | Boundary |
|---|---|---|---|
| TSMC demand mix | HPC **66%** of 2Q26 revenue; 7 nm and below **77%** of wafer revenue | first-party actual | revenue mix ≠ customer wafer allocation |
| HBM manufacturing intensity | Micron: HBM3E requires **≈3× wafer supply** vs. DDR5 at the same node / same bits | first-party physical trade ratio | not a price multiple; not a permanent ratio for every HBM generation |
| HBM allocation intensity | TrendForce 2026E: HBM wafer input **among the top three suppliers** ≈**22%** of total DRAM wafer input; HBM bit supply ≈**9%** of total DRAM bit supply | B-grade institutional forecast | the scopes are not identical enough to divide 22% by 9%; use Micron's same-node / same-bits ≈3× as the comparable physical anchor |
| Aggregate DRAM balance | 2026 sufficiency ratio estimated at roughly **−1% to −2%** | B-grade institutional forecast | aggregate DRAM, not HBM-specific |
| Forward supply commitments | NVIDIA manufacturing / supply / capacity commitments: **US$95.2B → US$279B** from Jan. 25 to Jul. 26, 2026 | first-party filing | aggregate commitments; no supplier-level split |
| LPS / power coordination | PORTS-Pike initial **4.25 IT-GW design capacity**, phased delivery planned from 2028 | first-party project disclosure | design / secured capacity ≠ energized ≠ utilized load |
| Infrastructure finance | **>US$500B** third-party-capital mobilization target announced by NVIDIA and financial partners | first-party target | target ≠ funded / committed / deployed capital |

For the full denominator audit and calculations, see [Chapter 8 — Quantitative Framework](en/publication/part-I-ch08-quantitative-framework.md).

---

## Core findings

These are landing-page highlights, not a second list of claims. They follow the report's canonical **Ten load-bearing judgments** in the same order; the full table and chapter mapping are in [Chapter 1 — Executive Summary](en/publication/part-I-ch01-executive-summary.md).

### 1. The competitive unit is the system stack

NVIDIA's current advantage cannot be explained by GPU benchmarks or market share alone.

Competition now spans compute, memory, interconnect, software, rack architecture, data centers, and power. Google Ironwood, AWS Trainium3, Microsoft Maia, Meta MTIA, and AMD Instinct/ROCm are also moving toward fuller system stacks.

The long-run question is not:

> Who owns the fastest chip?

It is:

> **Who can continuously deliver complete systems to real workloads with lower migration cost, high utilization, and reliable supply?**

### 2. AI/HPC is changing the marginal destination of capital

TSMC's HPC platform accounted for **66%** of 2Q26 revenue, while advanced technologies at 7 nm and below accounted for **77%** of wafer revenue. These are revenue-mix measures, not AI wafer share, but they show that HPC has become one of the central marginal drivers of advanced-manufacturing capital formation.

The report describes this as a **Two-Speed Semiconductor Economy**:

> The AI Infrastructure Economy and the Traditional Device Economy share upstream resources, but differ in willingness to pay, order duration, prepayment capacity, and the ability to induce new capital formation.

### 3. Gross supply can rise while effective supply for other end markets worsens

The report uses **Non-AI Residual Capacity**:

```text
NonAI_Residual
= Effective_Supply
- AI_Server_Absorption
- Other_Priority_Demand
```

Global wafer, DRAM, or packaging capacity can rise while smartphones, PCs, automotive, and industrial buyers still face higher prices, weaker allocation, or slower configuration upgrades.

### 4. Scarcity must be measured layer by layer

HBM, advanced packaging, networking, land/power/shell, and energized power are different physical pools with different denominators, so one aggregate "AI capacity" number is misleading.

- **HBM manufacturing intensity cannot be inferred from bit share alone.** Micron disclosed that, under **same technology node / same number of bits** conditions, HBM3E requires approximately **3× the wafer supply of DDR5**—a manufacturing-input trade ratio, not a price multiple and not a permanent constant for every HBM generation. TrendForce's estimate that HBM + RDIMM will represent approximately **51% of 2026 DRAM bit supply** remains a **2026E institutional forecast**, not a full-year actual.
- **Advanced packaging and power are independent constraints.** TSMC has explicitly stated that advanced-packaging tightness can limit customer growth. High-density AI systems also push scarcity into powered land, grid interconnection, substations, cooling, firm power, and permitting. The 2026-08-17 PORTS-Pike project extends this into **land + power + shell (LPS)**; NVIDIA disclosed credit support for an initial **4.25 IT-GW** design capacity with OpenAI as the customer, with phased delivery planned from 2028.

The report strictly separates:

> **secured / contracted capacity ≠ energized capacity ≠ utilized AI load**

and also:

> **IT-GW ≠ generation GW ≠ PPA capacity**

### 5. Substitution can weaken platform economics without automatically relieving upstream scarcity

Hyperscaler custom stacks are a real second route, but they still consume advanced logic, HBM, advanced packaging, networking, and power.

Substitution therefore changes **who captures platform value** without necessarily loosening the constrained physical layers. A cheaper die, a stronger isolated benchmark, or an alternative accelerator does not by itself prove lower migration cost, production-workload displacement, or relief in the scarce layers.

### 6. China requires two separate closure tests

China is no longer at the stage where no substitute system exists, but the frontier layer must still separate “a real parallel stack with partial production deployment exists” from “all seven Production-Grade Gates have closed.” On current public evidence, the latter **cannot yet be confirmed**.

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

### 7. Capital risk is a utilization, monetization, and financing-quality problem

High CapEx is neither proof of durable demand nor proof of a bubble.

On 2026-08-10, NVIDIA announced AI compute-infrastructure financing platforms with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs, and KKR, targeting **more than US$500B of third-party capital mobilization over time**. This is a mobilization target, not funded, committed, or deployed capital.

The relevant question is whether utilization, market clearing, customer cash generation, and financing quality can validate the asset base. S4 requires broad deterioration across multiple causally independent clearing-signal families and actors/layers, not a large spending number.

### 8. Model companies have become Anchor Compute Buyers

OpenAI Stargate and the Anthropic/AWS relationship illustrate that leading model companies are no longer simply renting whatever cloud capacity already exists.

Long-duration model demand can create:

> **revenue visibility → financing certainty → earlier infrastructure buildout → earlier resource reservation**

The same mechanism can also raise customer-concentration and duration risk.

### 9. Infrastructure must close through verified workflow output

The long-run value of AI infrastructure cannot be proven by GPU shipments, CapEx, or token volume alone. The verified-workflow standard below is a **long-run economic criterion, not an empirically calibrated fact metric as of the evidence cutoff**. Public studies still rarely join AI cost, human time, verification, failure/retry, persistence, and business value on the same workflow denominator. Agent-Native Software, Physical AI, and enterprise automation ultimately return to the same economic question:

> **How much Compute, Energy, Human Review, and Capital is required per verified workflow outcome, and can the resulting business value sustainably cover those costs?**

Until that criterion is empirically calibrated, lower unit Compute cost should not be presumed to imply either lower total infrastructure demand or a Jevons-style increase in demand. If future evidence shows that lower cost unlocks more verified workflows, total demand can expand; conversely, if infrastructure grows persistently faster than verified business output and cash flow, the risk of **S4 — Capital Hard Landing** rises structurally.

### 10. The 2026–2036 path is conditional

The report uses four conditional states rather than one 2036 point forecast:

- **S1 — Competitive Expansion**
- **S2 — Baseline Concentration**
- **S3 — Resource Hegemony**
- **S4 — Capital Hard Landing**

As of August 2026, the evidence mix is closest to **S2**:

> **high growth, high concentration, and credible substitution paths coexist.**

S2 is the current baseline, not a ten-year point forecast: supply elasticity, substitution, algorithmic efficiency, workload growth, power, financing quality, and system closure can move the industry toward S1, S3, or S4.

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

### End-system / consumer / game-console / automotive / industrial readers

For a first pass, read:

**Ch01 → Ch03 → Ch21 → Ch20 §10 → Ch32**

That path explains residual capacity, quantity assurance, upgrade tax, and end-system transmission first. NVIDIA, hyperscalers, China's parallel stack, and S1–S4 can be read on the second pass as mechanism background.

### Fastest path

1. [Chapter 1 — Executive Summary](en/publication/part-I-ch01-executive-summary.md)
2. [Chapter 32 — Master Judgment](en/publication/part-IV-ch32-master-judgment.md)
3. [Chapter 30 — S1–S4 Scenarios](en/publication/part-IV-ch30-scenarios.md)

### Full report

- [32-chapter English report](en/publication/README.md)
- [Scope and Evidence Boundaries](en/publication/00-front-matter.md)
- [List of Figures](en/publication/01-list-of-figures.md)
- [List of Tables](en/publication/02-list-of-tables.md)
- [Abbreviations and Core Glossary](en/publication/03-abbreviations-and-glossary.md)
- [Research Transparency, Limitations, and Correction Policy](en/publication/04-research-transparency.md)
- [Competitive Set, Substitution Paths, and Counter-Evidence Matrix](en/publication/05-competitive-evidence-matrix.md)

### Evidence and methodology

- [Chapter 27 — Research Method and Evidence Architecture](en/publication/part-IV-ch27-research-method.md)
- [Core Evidence Ledger](en/核心证据台账.en.md)
- [Core Source Index](en/核心参考文献索引.en.md)
- [Core Concepts and Model Index](en/核心概念与模型索引.en.md)
- [Core Hypothesis Matrix](en/核心假设矩阵.en.md)
- [Research Architecture](en/PUBLICATION_STRUCTURE.md)
- [External Research Comparison Index](en/外部研究对照索引.en.md)

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

Original research text is **All Rights Reserved**. Public availability does not grant a general reuse license. See [LICENSE](LICENSE) for the rights reservation, permissions policy, and treatment of automated extraction / AI use. Third-party material remains subject to the rights and licenses of its respective owners.

Citation metadata is available in [CITATION.cff](CITATION.cff).

## Corrections and counterevidence

Corrections, source upgrades, mechanism challenges, counterevidence, and falsification signals are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).
