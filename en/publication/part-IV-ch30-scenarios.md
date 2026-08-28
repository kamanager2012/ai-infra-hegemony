# Part IV · Chapter 30: The Four Standard Scenarios — S1 to S4

## 1. Scenario analysis is not a point forecast

This book does not assign one deterministic answer to 2030 or 2036, nor does it use a fixed probability table such as 40% / 30% / 15% / 15%.

Scenario weighting depends on observable variables including:

- advanced-capacity allocation;
- HBM supply;
- advanced packaging;
- cloud system-stack substitution;
- Anchor Buyer long-duration demand;
- power / Time-to-Power;
- software migration;
- China's parallel stack;
- regulation;
- utilization;
- CapEx / financing discipline.

## 2. S1 — Competitive Expansion

### Definition

AI demand keeps growing, but supply expansion and alternative systems mature fast enough to reduce concentration.

Typical conditions include:

- leading-edge capacity expands with more qualified supply;
- HBM supply elasticity improves;
- advanced-packaging tightness eases materially;
- cloud custom systems carry large production workloads;
- open software / interfaces reduce migration cost;
- energized power keeps pace with buildout;
- multiple system stacks coexist in production over long periods.

### Economic result

The dominant platform can remain very large while buyer optionality and bargaining power improve.

Scarcity premiums decline and value capture becomes more distributed.

This is:

> **market expands + concentration declines**

not "AI infrastructure disappears."

## 3. S2 — Baseline Concentration

### Definition

The current core trends continue:

- AI demand remains high;
- leading system-platform seller economics remain strong;
- HBM / advanced packaging remain periodically tight;
- cloud custom systems continue expanding without fully replacing frontier workloads;
- power becomes an independent deployment constraint;
- China's parallel stack keeps developing but frontier closure remains incomplete;
- CapEx / forward commitments remain high.

### Economic result

The market continues expanding rapidly while value capture remains concentrated in a small number of system platforms and scarce-layer suppliers.

As of August 2026, this is the **baseline state** that best matches the current evidence mix.

It is not a fixed ten-year forecast.

## 4. S3 — Resource Hegemony

### Definition

Demand growth continues to outrun substitution and supply expansion while multiple scarce layers remain concentrated at the same time.

Typical conditions include:

- advanced packaging stays structurally tight;
- HBM manufacturing intensity / generation constraints persist;
- leading-edge incremental capacity remains highly concentrated;
- proprietary software / interconnect migration costs stay high;
- cloud custom systems divert only part of the workload;
- powered land / firm MW are locked for long periods by a small set of buyers;
- Anchor Buyer and seller forward commitments continue expanding.

### Mechanism

> high profit → stronger commitments / prepayment → greater future resource reservation → higher delivery certainty → stronger installed base / workload retention

This describes stronger system-level resource coordination.

It is not a legal monopoly verdict.

## 5. S4 — Capital Hard Landing

### Definition

AI workload demand, utilization, and monetization fail to cover a rapidly expanding capital base.

Typical synchronized signals include:

- token / workflow volume growth disappoints;
- instance / lease prices fall rapidly;
- utilization declines;
- enterprise AI monetization remains weak;
- hyperscaler CapEx guidance falls;
- seller / Anchor Buyer commitments shrink or cancel;
- used-hardware residual value declines quickly;
- impairment / write-down rises.

### Clearing order

The first pressure usually appears in:

- next-generation hardware orders;
- inventory;
- short-lived system residual value;
- speculative / highly concentrated financing.

If weakness persists, the pressure can move into semiconductor CapEx, data-center expansion, and power buildout.

S4 does not mean AI usage disappears.

After capital clearing, cheaper compute can still stimulate new applications.

## 5A. AI Capacity Gap: a cross-scenario diagnostic axis

S1–S4 remain parallel conditional states. The report does not introduce a second scenario taxonomy. Instead, it adds a cross-scenario diagnostic variable:

```text
AI_Capacity_Gap_i(t)
= Growth(AI_Demand_i(t))
- Growth(AI_Effective_Capacity_i(t))
```

where (i) is a physical layer such as advanced logic, HBM/DRAM, advanced packaging, networking, or power. Layer-level gaps can move in opposite directions, so they must not be collapsed prematurely into one “global AI capacity gap.”

Interpretation:

- **persistent Gap > 0 across several critical layers:** scarcity remains strong and relative weight shifts toward S2 / S3;
- **critical-layer gaps converge toward zero while multi-sourcing and substitution improve:** relative weight shifts toward S1;
- **Gap < 0 while utilization remains healthy:** supply is loosening, but this is not by itself S4;
- **Gap < 0 + falling utilization + weaker clearing prices + shrinking commitments:** the combined evidence materially raises S4 weight.

AI Capacity Gap must be read together with Non-AI Residual Capacity. The former asks how much incremental supply AI still lacks; the latter asks how much effective capacity remains for non-AI demand after priority allocation.

## 6. Five variable classes determine scenario structure

### Supply

Leading-edge wafers, HBM, advanced packaging, power.

### Substitution

Cloud custom systems, open compiler/runtime, alternative interconnect, China's parallel stack.

### Demand

Token/workflow volume, enterprise adoption, Anchor Buyer commitments, sovereign demand.

### Finance

Seller cash generation, hyperscaler CapEx, depreciation, utilization, financing cost, residual value.

### Regulation / Geopolitics

Export controls, antitrust remedies, interface openness, industrial policy, regional fragmentation.

## 7. Anchor Compute Buyer is a new scenario variable

Multi-year compute commitments from large model companies can influence infrastructure financing, custom silicon, power, and data-center buildout.

If Anchor Buyer demand expands and converts into real utilization, S2/S3 weighting rises.

If long-duration commitments are delayed, renegotiated, or underutilized at scale, S4 weighting rises.

Model-company contracts therefore cannot be treated as ordinary cloud-customer spending.

## 8. Observable signals from S2 toward S1

- alternative system stacks scale in frontier / high-value production workloads;
- HBM / packaging lead times decline sustainably;
- access to advanced capacity becomes more distributed;
- open software / interfaces reduce migration cost materially;
- power expansion shortens Time-to-Power;
- buyer multi-sourcing becomes normal production practice.

## 9. Observable signals from S2 toward S3

- seller forward commitments keep expanding rapidly;
- HBM / packaging tightness persists across generations;
- proprietary-system switching cost rises;
- leading-edge incremental supply remains highly concentrated;
- scarce power / powered land is locked by a small set of Anchor Buyers;
- alternative stacks fail to create enough production-scale optionality.

## 10. Observable signals from S2 toward S4

- CapEx guidance declines repeatedly;
- utilization falls;
- seller / Anchor Buyer commitments cancel or shrink materially;
- second-hand system clearing prices fall quickly;
- cloud discounts / lease rates deteriorate;
- impairment rises;
- enterprise AI monetization remains persistently below depreciation / operating cost.

## 11. Why S1, S2, S3, and S4 are not sequential stages

They are parallel conditional states.

One region can experience S3-style power scarcity while selected workloads already operate in S1-style multi-stack competition.

Memory can temporarily loosen while packaging remains tight.

Capital markets can clear locally while productive workloads continue to grow.

Scenario weighting therefore describes **relative structure**, not one compulsory industry path.

## 12. Current baseline

As of August 2026, the formal baseline is:

> **S2 — Baseline Concentration**

because:

- NVIDIA / leading-platform seller economics remain strong;
- HBM and advanced packaging remain important bottlenecks;
- cloud custom systems are real competitors but have not shown comprehensive frontier-workload substitution;
- infrastructure CapEx and forward commitments remain high;
- power constraints are rising;
- China's parallel stack has not reached equivalent closure across every frontier critical layer;
- synchronized evidence of an industry-wide Capital Hard Landing remains insufficient.

The baseline remains valid only while this evidence mix remains valid.

## 13. Final use of the framework

Future updates should not ask:

> "Which ten-year prediction was proven correct?"

They should ask:

> **Which observable variables changed, and how should S1–S4 relative weighting adjust?**

That keeps long-run judgment responsive to industrial evidence rather than dependent on a one-time bet.

## Core monitoring navigation

- [Chapter 29: Core Metrics and Evidence-Monitoring Framework](part-IV-ch29-monitoring-framework.md)
- [Chapter 32: Master Judgment](part-IV-ch32-master-judgment.md)
- [Core Hypothesis Matrix](../核心假设矩阵.en.md)
