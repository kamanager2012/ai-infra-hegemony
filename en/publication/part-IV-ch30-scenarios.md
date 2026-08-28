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

## 5.1 Comparative framework for the four standard scenarios

**Table 30.1 — Core drivers, primary outcomes, and reverse signals for S1–S4**

| Scenario | Core drivers | Primary industry outcome | Key reverse signal |
|---|---|---|---|
| S1 — Competitive Expansion | higher supply elasticity, multi-sourcing, and portability | more distributed value capture and greater buyer optionality | scarce-layer tightness strengthens again or migration costs rise |
| S2 — Baseline Concentration | strong demand, strong leading platforms, substitution develops but remains incomplete | high growth and concentration coexist | supply/substitution improve materially or ROI/commitments deteriorate together |
| S3 — Resource Hegemony | multi-layer scarcity + switching costs + forward reservation strengthen | incremental capacity becomes more concentrated and replication costs rise | capacity access broadens and open interfaces materially lower migration costs |
| S4 — Capital Hard Landing | utilization / monetization falls short of the capital base | clearing prices, orders, CapEx, and asset values decline | utilization, clearing prices, and forward commitments recover |

**Source:** Report S1–S4 scenario framework.  
**Note:** The four scenarios are parallel conditional states. They do not carry fixed probabilities and are not inevitable sequential stages.

## 5A. AI Capacity Gap: a cross-scenario diagnostic axis

S1–S4 remain parallel conditional states; the report does not introduce a second scenario taxonomy. To separate “is the layer short today?” from “is the pressure widening or converging?”, it uses two complementary metrics.

### Absolute gap

```text
AI_Capacity_Gap_i(t)
= AI_Effective_Demand_i(t)
- AI_Effective_Capacity_i(t)
```

Demand and capacity must be measured within the same physical layer, delivery window, and qualification/quality boundary. Units can include wafers/month, qualified package starts/month, bits/year, or MW.

- **Absolute Gap > 0:** current deliverable supply is insufficient;
- **Absolute Gap ≈ 0:** current supply and demand are near balance;
- **Absolute Gap < 0:** current effective headroom exists.

### Growth gap

```text
AI_Capacity_Growth_Gap_i(t)
= Growth(AI_Effective_Demand_i(t))
- Growth(AI_Effective_Capacity_i(t))
```

The Growth Gap is a same-period growth-rate difference and describes whether the absolute gap is more likely to widen or converge:

- **Growth Gap > 0:** scarcity may widen, or existing headroom may be eroded;
- **Growth Gap < 0:** scarcity may converge, or effective headroom may expand;
- **Growth Gap = 0:** supply and demand are changing at the same rate; it does not mean no shortage exists.

Therefore:

- **Absolute Gap > 0 and Growth Gap > 0 across several critical layers:** scarcity is strengthening and relative weight shifts toward S2 / S3;
- **Absolute Gap > 0 but Growth Gap < 0:** the layer remains short, but supply is catching up and S1 weight can rise;
- **Absolute Gap < 0 with healthy utilization:** supply has headroom, but this is not S4 by itself;
- **Absolute Gap < 0 + falling utilization + weaker clearing prices + shrinking commitments:** S4 weight rises materially.

AI Capacity Gap / Growth Gap must be read together with Non-AI Residual Capacity. The first two ask how much AI currently lacks and how that gap is changing; NARC asks how much effective supply remains for non-AI demand after priority allocation.

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

As of August 2026, the report's baseline is:

> **S2 — Baseline Concentration**

because:

- NVIDIA / leading-platform seller economics remain strong;[^1]
- HBM and advanced packaging remain important bottlenecks;[^2][^3]
- cloud custom systems are real competitors but have not shown comprehensive frontier-workload substitution;[^4]
- infrastructure CapEx and forward commitments remain high;[^5]
- power constraints are rising;[^6]
- China's parallel stack has not reached equivalent closure across every frontier critical layer;
- synchronized evidence of an industry-wide Capital Hard Landing remains insufficient.

The baseline remains valid only while this evidence mix remains valid.

## 13. Final use of the framework

Future updates should not ask:

> "Which ten-year prediction was proven correct?"

They should ask:

> **Which observable variables changed, and how should S1–S4 relative weighting adjust?**

That keeps long-run judgment responsive to industrial evidence rather than dependent on a one-time bet.

## References

[^1]: NVIDIA, FY27 Q2 official results, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^2]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E wafer-supply trade ratio, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^3]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging tightness limiting customer growth, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^4]: Google Ironwood TPU, https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; AWS Trainium3 UltraServers, https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ ; Microsoft Maia 200, https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ ; Meta MTIA 300, https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
[^5]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^6]: NVIDIA, DGX GB200 Hardware Guide, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html ; Talen Energy, 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm

## Cross-references

- [Chapter 29: Core Metrics and Evidence-Monitoring Framework](part-IV-ch29-monitoring-framework.md)
- [Chapter 32: Master Judgment](part-IV-ch32-master-judgment.md)
- [Core Hypothesis Matrix](../核心假设矩阵.en.md)
