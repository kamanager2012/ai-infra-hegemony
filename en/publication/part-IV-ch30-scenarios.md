# Part IV · Chapter 30: Scenario Framework — Discriminating S1 to S4

## 1. Scenarios are adjudication states, not stories

The framework does not assign one deterministic 2030 or 2036 outcome, and it does not attach fixed probabilities to S1–S4.

Its purpose is operational: **given the evidence now, which structural state best fits the system, which variables discriminate the alternatives, and what observations would force a reweighting?**

Scenario weighting therefore depends on state variables that can be monitored:

- layer-specific scarce-capacity access;
- HBM / advanced-packaging supply;
- second-stack substitution;
- Anchor Buyer commitments;
- power delivery / Time-to-Power;
- software migration;
- China closure tests;
- utilization / monetization;
- financing quality;
- regulation / geopolitics.

## 2. S1 — Competitive Expansion: supply and substitution outrun concentration

### Structural condition

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

### 2A. Supply-response overshoot can accelerate S1

The Rolling Bottleneck Cascade does not imply that the same scarce layer remains short for a decade. Fabs, memory, and packaging all have long construction and qualification cycles. **High prices and high margins can induce several suppliers to expand at the same time; if effective output arrives in a similar window while demand growth decelerates, a layer can move rapidly from shortage to headroom or even oversupply.**

Public forward evidence at the report cutoff already shows this response can be **layer-specific rather than uniform**. TrendForce on July 30, 2026 expected DRAM to remain tight in 2027 while NAND Flash could move toward a looser supply-demand structure in **2H27** as new capacity and bit-output growth arrive; it also expected meaningful output contribution from some new DRAM capacity to emerge only in **2028**.[^10]

The report therefore does not extrapolate 2024–2026 HBM / packaging tightness into permanent ten-year scarcity. The variables to monitor by layer are:

- effective capacity ramp;
- qualification / yield;
- demand-growth deceleration;
- lead time / clearing price;
- utilization;
- product-mix reversal.

If supply growth persistently exceeds demand growth across several scarce layers while lead times and scarcity premiums decline, S1 weight should rise materially. If that easing is accompanied by weakening utilization and clearing prices, S4 weight can rise as well.

## 3. S2 — Baseline Concentration: growth and concentration coexist

### Definition

The current core trends continue:

- AI demand remains high;
- leading system-platform seller economics remain strong;
- HBM / advanced packaging remain periodically tight;
- cloud custom systems continue expanding without fully replacing frontier workloads;
- power becomes an independent deployment constraint;
- China's frontier parallel stack keeps iterating with partial production deployment, while a complete production-grade frontier closure remains unconfirmed by public evidence;
- CapEx / forward commitments remain high.

### Economic result

The market continues expanding rapidly while value capture remains concentrated in a small number of system platforms and scarce-layer suppliers.

For traditional end systems, S2 is not merely background: **high growth and high concentration can coexist with tighter Non-AI Residual Capacity, differentiated quantity assurance, slower configuration upgrades, or an upgrade tax.** This does not mean every end market is shrinking; it means the benefits of growth and the burden of resource pressure can sit at different points in the value chain.

As of August 2026, this is the **baseline state** that best matches the current evidence mix.

It is not a fixed ten-year forecast.

## 4. S3 — Resource Hegemony: multi-layer concentration becomes self-reinforcing

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

### Reinforcement mechanism

> high profit → stronger commitments / prepayment → greater future resource reservation → higher delivery certainty → stronger installed base / workload retention

This describes stronger system-level resource coordination.

It is not a legal monopoly verdict.

## 5. S4 — Capital Hard Landing: capital formation outruns productive demand

### Definition

AI workload demand, utilization, and monetization fail to cover a rapidly expanding capital base.

Typical synchronized signals include:

- utilization and effective AI revenue fall behind the installed capital base;
- instance / lease prices and secondary-market values weaken;
- enterprise AI monetization remains weak;
- hyperscaler CapEx guidance falls;
- seller / Anchor Buyer commitments shrink, reschedule, or cancel;
- impairment / write-down rises;
- customer cash generation weakens while supplier equity / credit support or refinancing dependency rises;
- independent third-party risk capital becomes less willing to absorb exposure.

These are **typical signal families, not a mandatory five-of-five gate**. S4 confirmation depends on cross-signal confirmation plus cross-actor / cross-layer causal breadth. Accounting impairment is confirmatory / severity evidence, not a prerequisite; financing-led or real-economy clearing can be confirmed before qualifying write-down evidence appears.

### Clearing order

The first pressure usually appears in:

- next-generation hardware orders;
- inventory;
- short-lived system residual value;
- speculative / highly concentrated financing.

If weakness persists, the pressure can move into semiconductor CapEx, data-center expansion, and power buildout.

S4 does not mean AI usage disappears.

After capital clearing, cheaper compute can still stimulate new applications.

## 5.1 Comparative scenario matrix

**Table 30.1 — Core drivers, primary outcomes, and reverse signals for S1–S4**

| Scenario | Core drivers | Primary industry outcome | Key reverse signal |
|---|---|---|---|
| S1 — Competitive Expansion | higher supply elasticity, multi-sourcing, and portability | more distributed value capture and greater buyer optionality | scarce-layer tightness strengthens again or migration costs rise |
| S2 — Baseline Concentration | strong demand, strong leading platforms, substitution develops but remains incomplete | high growth and concentration coexist | supply/substitution improve materially or ROI/commitments deteriorate together |
| S3 — Resource Hegemony | multi-layer scarcity + switching costs + forward reservation strengthen | incremental capacity becomes more concentrated and replication costs rise | capacity access broadens and open interfaces materially lower migration costs |
| S4 — Capital Hard Landing | utilization / monetization and demand-financing quality fall short of the capital base | clearing prices, orders, CapEx, asset values, and financing quality weaken | utilization, clearing prices, independent financing, and forward commitments recover |

**Source:** Report S1–S4 scenario framework.  
**Note:** The four scenarios are parallel conditional states. They do not carry fixed probabilities and are not inevitable sequential stages.

## 5A. Capacity Gap is a diagnostic axis, not a fifth scenario

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

## 6. Six variable classes discriminate the scenarios

### Supply

Leading-edge wafers, HBM, advanced packaging, power.

### Substitution

Cloud custom systems, open compiler/runtime, alternative interconnect, China's parallel stack.

### Demand

Token/workflow volume, enterprise adoption, Anchor Buyer commitments, sovereign demand.

### Capital / Monetization

Seller cash generation, hyperscaler CapEx, depreciation, utilization, workload revenue, residual value.

### Financing Quality

Anchor Buyer credit quality, third-party risk capital, supplier equity / credit support, refinancing dependency, asset transferability.

### Regulation / Geopolitics

Export controls, antitrust remedies, interface openness, industrial policy, regional fragmentation.

## 7. Anchor Buyers and financing quality can amplify expansion or clearing

Multi-year compute commitments from large model companies can influence infrastructure financing, custom silicon, power, and data-center buildout.

The 2026 financing layer is now observable in first-party disclosures: NVIDIA has announced compute-financing platforms targeting **more than US$500B of third-party capital mobilization over time**, and PORTS-Pike adds seller credit support around initial **4.25 IT-GW** design capacity.[^7][^8]

If Anchor Buyer demand expands and converts into real utilization, S2/S3 weighting rises.

If long-duration commitments are delayed, renegotiated, or underutilized at scale, S4 weighting rises.

Model-company contracts therefore cannot be treated as ordinary cloud-customer spending.

Seller-assisted financing can strengthen infrastructure formation when it is supported by real utilization, monetization, and independent capital.

It becomes an S4 risk amplifier when customer cash generation weakens while supplier equity / credit support and refinancing dependency keep increasing.

The report therefore distinguishes Anchor Buyer demand from **Financing Reflexivity** rather than treating every financing-supported order as either fully organic or automatically artificial.

## 8. Signals that move S2 toward S1

- alternative system stacks scale in frontier / high-value production workloads;
- HBM / packaging lead times decline sustainably;
- access to advanced capacity becomes more distributed;
- open software / interfaces reduce migration cost materially;
- power expansion shortens Time-to-Power;
- buyer multi-sourcing becomes normal production practice.

## 9. Signals that move S2 toward S3

- seller forward commitments keep expanding rapidly;
- HBM / packaging tightness persists across generations;
- proprietary-system switching cost rises;
- leading-edge incremental supply remains highly concentrated;
- scarce power / powered land is locked by a small set of Anchor Buyers;
- alternative stacks fail to create enough production-scale optionality.

## 10. Signals that move S2 toward S4

- CapEx guidance declines repeatedly;
- utilization falls;
- seller / Anchor Buyer commitments cancel or shrink materially;
- second-hand system clearing prices fall quickly;
- cloud discounts / lease rates deteriorate;
- impairment rises;
- enterprise AI monetization remains persistently below depreciation / operating cost;
- supplier equity / credit support rises while independent customer financing / third-party risk-taking weakens.

## 11. These are states, not stages

They are parallel conditional states.

One region can experience S3-style power scarcity while selected workloads already operate in S1-style multi-stack competition.

Memory can temporarily loosen while packaging remains tight.

Capital markets can clear locally while productive workloads continue to grow.

Scenario weighting therefore describes **relative structure**, not one compulsory industry path.

## 12. Current baseline: S2

As of August 2026, the report's baseline is:

> **S2 — Baseline Concentration**

because:

- NVIDIA / leading-platform seller economics remain strong;[^1]
- HBM and advanced packaging remain important bottlenecks;[^2][^3]
- cloud custom systems are real competitors but have not shown comprehensive frontier-workload substitution;[^4]
- infrastructure CapEx and forward commitments remain high;[^5]
- power constraints are rising;[^6]
- China has real frontier parallel alternatives and partial production deployment, but under Chapter 17's seven Production-Grade Gates a complete production-grade frontier closure remains unconfirmed by public evidence;
- synchronized evidence of an industry-wide Capital Hard Landing remains insufficient.

The baseline remains valid only while this evidence mix remains valid; the discrimination rules are in Section 12A.

## 12A. Discrimination rules

Scenarios are distinguished along the following axes rather than by any single aggregate metric:

- **S1 ↔ S2:** the degree to which alternative systems scale in frontier / high-value production workloads, and whether HBM / packaging lead times keep falling;
- **S2 ↔ S3:** the direction of allocation concentration at scarce layers, the growth rate of seller forward commitments, proprietary switching costs, and the degree of powered-land lockup;
- **S3 ↔ S4:** the ratio of utilization / monetization to the capital base — not publicly disclosed, so judged through public proxies: clearing prices (used-system prices, lease rates, cloud discounts), commitment growth, the share of seller equity / credit support, third-party capital risk premia, and refinancing dependency.

The same capital evidence (for example the **>US$500B** mobilization target, the **US$50B** frontier-lab investment, and **2 GW** of credit support)[^7][^8][^9] supports S2/S3 infrastructure coordination while the proxy signals are healthy, and shifts weight toward S4 when the proxies deteriorate broadly and persistently; the judgment never rests on a single data point.

Boundary case: if demand growth slows materially without producing sufficient cross-signal confirmation and causal breadth across multiple S4 signal families, assignment follows substitution strength — expanding substitution raises S1 weight, while persistent scarce-layer tightness places the state in S2 (reading "high demand" as "demand growth still above effective-supply growth").

## 12B. Calibration status

As of the report cutoff, the S1–S4 discrimination axes are explicit, but there is **no statistically validated universal threshold, fixed observation window, or automatic state-switch rule**.

Therefore:

- one CapEx cut cannot independently trigger S4;
- one packaging / HBM tightness signal cannot independently trigger S3;
- one alternative-chip launch cannot independently trigger S1;
- S2 cannot become a permanent default merely because most observations can still be narrated inside it.

Changes in scenario weight require **several independent public proxies to move in the same direction across repeated observations**, while counterevidence and segment breadth remain explicit. Because disclosure frequencies differ across quarterly, semiannual, and annual data, this report does not force them into a false single observation window.

In other words:

> **The framework already specifies what to observe, but it does not pretend that “how much” and “for how long” have already been statistically calibrated.**

Historical backtesting, lead/lag analysis, and threshold calibration belong to later empirical validation. Until then, S1–S4 should be read as an updateable structural discrimination framework, not a mechanical classifier.

---

## 13. How to use the framework

Future updates should not ask:

> "Which ten-year prediction was proven correct?"

They should ask:

> **Which observable variables changed, and how should S1–S4 relative weighting adjust?**

That keeps long-run judgment responsive to industrial evidence rather than dependent on a one-time bet.

## References

[^1]: NVIDIA, FY27 Q2 official results, https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
[^2]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E wafer-supply trade ratio, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^3]: TSMC, 2Q26 Earnings Conference Transcript, advanced-packaging tightness limiting customer growth, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^4]: Google Ironwood TPU, https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ ; AWS Trainium3 UltraServers, https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/ ; Microsoft Maia 200, https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ ; Meta MTIA 300, https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
[^5]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
[^6]: NVIDIA, DGX GB200 Hardware Guide, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html ; Talen Energy, 2026 Q2 Form 10-Q, https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm
[^7]: NVIDIA, 2026-08-10, AI compute infrastructure financing platforms and >US$500B third-party-capital mobilization target, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Partners-With-Apollo-BlackRock-Blackstone-Brookfield-Goldman-Sachs-and-KKR-to-Establish-AI-Compute-Infrastructure-Financing-Platforms-to-Mobilize-Over-500-Billion-of-Third-Party-Capital/default.aspx
[^8]: NVIDIA, 2026-08-17, PORTS-Pike / SB Energy / OpenAI, LPS credit support and initial 4.25 IT-GW design capacity, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx
[^9]: NVIDIA, FY27 Q2 Earnings Call transcript, 2026-08-26, frontier-lab investment close to US$50B and selective credit enhancement for close to 2 GW of compute, https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf

[^10]: TrendForce, 2026-07-30, “Diverging Memory Market Outlook in 2027 as DRAM Supply Remains Tight While NAND Flash Supply Conditions Ease,” https://www.trendforce.com/presscenter/news/20260730-13158.html

## Cross-references

- [Chapter 29: Core Metrics and Evidence-Monitoring Framework](part-IV-ch29-monitoring-framework.md)
- [Chapter 32: Master Judgment](part-IV-ch32-master-judgment.md)
- [Core Hypothesis Matrix](../核心假设矩阵.en.md)
