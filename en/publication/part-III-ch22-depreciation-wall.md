# Part III · Chapter 22: The Depreciation Wall and Duration Mismatch

## 1. The depreciation wall is a duration mismatch, not a calendar event

The relevant condition is:

> **When hardware refresh / economic obsolescence runs faster than workload monetization, the installed asset base starts to compress returns and change the next round of capital formation.**

The depreciation wall must be read together with utilization, revenue, residual value, and next-generation investment.

## 2. Accounting useful lives differ across the major clouds

Current company disclosures show materially different server / network-equipment useful-life policies:

**Table 22.1 — Major cloud server / network-equipment useful-life disclosures**

| Company | Server / network-equipment useful-life disclosure |
|---|---|
| Microsoft FY26 | 2–6 years |
| Alphabet 2025 | generally 6 years |
| Meta 2025 | 5–5.5 years |
| Amazon 2025 | 5–6 years; some assets changed from 6 years to 5 years in 2025 |

**Source:** Microsoft FY26 Form 10-K, Alphabet 2025 Form 10-K, Meta 2025 Form 10-K, and Amazon 2025 Form 10-K.[^1][^2][^3][^4]  
**Note:** Accounting useful life is not economic life. Asset categories and depreciation estimates are not mechanically comparable across companies.

These disclosures are sufficient to reject **one universal four-year useful-life assumption** for the major-cloud server/network asset base. The chapter is not claiming that "four years" is itself a documented industry-standard accounting convention.

## 3. Accounting life is not economic life

A server can still be depreciating for accounting purposes even after a new architecture, better memory efficiency, newer software support, or better power efficiency makes it economically less competitive.

That is **economic obsolescence**.

Conversely, the cited company disclosures show that building useful-life ranges can extend materially beyond server/network-equipment ranges—for example, Alphabet, Meta, and Amazon disclose multi-decade building lives.[^2][^3][^4] A PPA or grid asset also follows a different contractual/physical duration clock from an accelerator generation; the report therefore treats these as **long-cycle infrastructure**, not as one uniform useful-life category.

The fundamental mismatch is:

> **short-cycle compute vs. long-cycle physical infrastructure**

## 4. Clearing follows the asset-duration stack

The report uses the following **duration-stack clearing heuristic**:

1. next-generation hardware orders;
2. inventory;
3. used-system / lease prices;
4. discretionary expansion.

Long-cycle assets such as data-center shells, grid assets, generation, and long-duration PPAs are expected to adjust more slowly. This ordering is a report-side analytical sequence, not a sourced empirical law with a fixed cross-industry timing distribution.

That is why a Capital Hard Landing is unlikely to complete in a single quarter.

## 5. CapEx must be evaluated against utilization, not only depreciation years

As a **D-grade sensitivity example**, the same **US$100B** investment has very different economics at **90%** utilization and **30%** utilization. US$100B, 90%, and 30% are illustrative inputs, not industry actuals.

The analysis must include:

> **Revenue / Deployed Compute**

and actual **Utilization**.

A fixed depreciation period only describes the accounting expense schedule. It does not show whether the asset is generating enough cash flow.

## 6. Market-clearing prices can reveal economic depreciation first

Used accelerator / system prices, cloud lease rates, and delivery lead times are treated here as **leading market-clearing indicators to monitor** for generation obsolescence and oversupply. The chapter does not claim a validated historical rule that these indicators always move before formal impairment.

If old-system residual value falls quickly when a new generation launches, buyer-side economic depreciation can move much faster than accounting depreciation.

That is why [Chapter 24](part-III-ch24-capital-clearing.md) treats Market Clearing as an independent S4 signal.

## 7. Algorithmic efficiency can accelerate economic obsolescence

If a new architecture can perform the same workload with less HBM, compute, or communication, an older system can lose competitiveness on cost per task even while it remains physically functional.

Software and model innovation can change hardware economic life directly.

### 7A. Efficiency–utilization break-even: the arithmetic must close

The tension between algorithmic efficiency and capital recovery can be written without assuming any particular demand elasticity.

Let:

```text
Infrastructure Demand = Unit Resource Intensity × Workload Volume
```

Then:

```text
D1 / D0 = (I1 / I0) × (V1 / V0)
```

where (I) is resource intensity per comparable workload and (V) is workload volume.

The break-even condition for keeping aggregate resource demand unchanged is:

```text
V1 / V0 = I0 / I1
```

This is an identity, not a forecast. If a hypothetical architecture reduces comparable resource intensity by **90%** ((I1/I0 = 0.1)), workload volume would need to rise **10×** merely to keep aggregate resource demand unchanged. The report does **not** claim that a 90% efficiency gain or a 10× workload increase will occur; the example is a D-grade sensitivity check.

For existing assets, the hurdle is stricter than aggregate break-even. New workload can migrate disproportionately toward newer systems with better cost per task, memory efficiency, power efficiency, or software support. Aggregate compute demand can remain flat or even grow while an older generation's utilization and residual value deteriorate.

This converts the efficiency question into an observable capital test:

- how quickly comparable cost per verified workload falls;
- how quickly total workload volume grows;
- how workload shifts across hardware generations;
- whether older-system utilization / lease rates / resale values fall faster than accounting depreciation.

Algorithmic progress is neither automatically expansionary nor contractionary for infrastructure demand. It is a **capital-recovery variable** whose effect depends on workload growth and generation-level allocation.

---

## 8. Power assets carry the opposite duration profile

Under the report's S2/S3 high-demand scenarios, long-duration power / grid assets can become scarce moats; the scenario definitions are in [Chapter 30](part-IV-ch30-scenarios.md), while the physical power constraint is documented separately in [Chapter 7](part-I-ch07-power-constraint.md).

In S4, the same PPA, substation, or data-center shell can become a long-duration low-utilization burden.

Asset value depends on demand duration. "Power assets are always safe" is not a valid assumption.

## 9. Anchor Buyers lower financing risk while concentrating demand risk

Long-duration model-company compute contracts can improve revenue visibility and financing certainty. OpenAI's Stargate capacity program, Anthropic/AWS's long-duration compute collaboration, and the 20-year OpenAI lease embedded in PORTS-Pike are current examples of the contract structures discussed here.[^5][^6][^7]

But if an anchor buyer's revenue, financing, or architecture assumptions change, take-or-pay exposure, renegotiation, and stranded-capacity risk can become concentrated.

Customer concentration and contract duration must be analyzed together with useful life.

## 9A. Financing structure can move losses without eliminating them

By August 2026, public disclosures show AI-infrastructure formation using or planning multiple financing structures, including:

- operating leases;
- project finance / third-party infrastructure vehicles;
- long-duration customer contracts;
- supplier equity / credit enhancement.[^8][^9][^10]

The risk-transfer layer is now observable across more than one supplier. NVIDIA's FY27 Q2 Form 10-Q caps aggregate obligations under PORTS-Pike lease guarantees at **US$105B** across leases covering approximately **4.25 GW of IT load**, while AMD's Q2 2026 Form 10-Q reports **US$4.1B of maximum gross exposure** from guarantees tied to certain commercial-partner data-center lease obligations.[^11][^12] Both figures are maximum guarantee exposures, not funded CapEx, current cash outflow, or realized loss; they therefore cannot be added mechanically to infrastructure investment totals.

This is a **structure inventory**, not a time-series claim that every category is increasing at the same rate across the industry.

Those structures change where depreciation, lease expense, interest cost, and residual-value risk are recognized or borne.

They do not remove the underlying economic relationship:

> **if a new system delivers materially lower cost per task, older assets can lose economic value even while they still function.**

A lease can transfer ownership risk. Project finance can isolate part of the risk in an SPV. Seller credit can reduce financing friction.

None of those structures makes technological obsolescence disappear.

The important question is who ultimately bears residual-value risk and whether contracted cash flow is sufficient to cover it.

## 10. A single depreciation cycle cannot determine 2036

Assets enter service on different dates, use different useful lives, and can experience impairment or changes in accounting estimates.

There is no single year in which "all 2026 CapEx finishes depreciating."

The 2036 structure depends on the second and third rounds of buildout, workload growth, system substitution, power, China's parallel stack, and regulation—not a mechanical first-cycle accounting schedule.

## 11. Current read

As of August 2026, [Chapter 19](part-III-ch19-capex-supercycle.md) still documents **active high-intensity CapEx expansion**. This chapter therefore treats **duration mismatch as a live capital-recovery risk**, while the public evidence cited here does **not** establish either broad deterioration in deployed-compute utilization or a broad AI-infrastructure impairment cycle.

The depreciation wall becomes materially more dangerous when sustained utilization decline, rapid residual-value erosion, lower CapEx / commitment signals, and financing stress cross-confirm across actors/layers. Rising impairment strengthens the severity diagnosis when it appears, but formal accounting loss is not a mandatory gate.

## References

[^1]: Microsoft Corporation, FY26 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
[^2]: Alphabet Inc., 2025 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
[^3]: Meta Platforms, Inc., 2025 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
[^4]: Amazon.com, Inc., 2025 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
[^5]: OpenAI, “Announcing The Stargate Project,” 2025-01, long-duration U.S. AI-infrastructure buildout, https://openai.com/index/announcing-the-stargate-project/
[^6]: Anthropic, “Anthropic and Amazon expand collaboration for up to 5 gigawatts of new compute,” 2026-04-20, >US$100B over ten years and up to 5 GW of new compute capacity, https://www.anthropic.com/news/anthropic-amazon-compute?lang=us
[^7]: NVIDIA, 2026-08-17, PORTS-Pike / SB Energy / OpenAI, including a 20-year OpenAI lease, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx
[^8]: Microsoft, FY26 Q4 earnings conference call, operating-lease / CapEx classification change and approximately US$175B calendar-2026 CapEx expectation, https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4
[^9]: NVIDIA, 2026-08-10, announced compute-financing partnerships / MOUs targeting more than US$500B of third-party capital mobilization over time, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Partners-With-Apollo-BlackRock-Blackstone-Brookfield-Goldman-Sachs-and-KKR-to-Establish-AI-Compute-Infrastructure-Financing-Platforms-to-Mobilize-Over-500-Billion-of-Third-Party-Capital/default.aspx
[^10]: NVIDIA, 2026-08-17, PORTS-Pike seller credit support / equity / long-duration customer structure, https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Guarantees-SB-Energys-PORTS-Pike-Technology-Campus-in-Ohio-to-Exclusively-Host-NVIDIA-AI-Compute/default.aspx

[^11]: NVIDIA Corporation, FY27 Q2 Form 10-Q, PORTS-Pike guarantees covering approximately 4.25 GW of IT load, aggregate obligations capped at US$105B, phased effectiveness across nine data centers with the first phase expected in FY2029, and exposure declining as OpenAI fulfills lease payments, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

[^12]: Advanced Micro Devices, Inc., Q2 2026 Form 10-Q, US$4.1B maximum gross exposure from guarantees tied to certain commercial-partner data-center lease obligations with terms up to 15 years; exposure declines as contractual lease payments are made, https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm
