# Part III · Chapter 22: The Depreciation Wall and Duration Mismatch

## 1. The depreciation wall is a duration mismatch, not a calendar event

The relevant condition is:

> **When hardware refresh / economic obsolescence runs faster than workload monetization, the installed asset base starts to compress returns and change the next round of capital formation.**

The depreciation wall has to be read together with utilization, revenue, residual value, and next-generation investment.

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

This is enough to show that one universal "four-year straight-line depreciation" assumption cannot be applied to the entire AI-infrastructure stack.

## 3. Accounting life is not economic life

A server can still be depreciating for accounting purposes even after a new architecture, better memory efficiency, newer software support, or better power efficiency makes it economically less competitive.

That is **economic obsolescence**.

Conversely, a data-center shell, substation, or PPA often has a much longer economic life than one accelerator generation.

The fundamental mismatch is:

> **short-cycle compute vs. long-cycle physical infrastructure**

## 4. Clearing follows the asset-duration stack

The first adjustments are usually:

1. next-generation hardware orders;
2. inventory;
3. used-system / lease prices;
4. discretionary expansion.

The slowest assets to adjust are data-center shells, grid assets, generation, and long-duration PPAs.

That is why a Capital Hard Landing is unlikely to complete in a single quarter.

## 5. CapEx has to be divided by utilization, not only by years

As a **D-grade sensitivity example**, the same **US$100B** investment has very different economics at **90%** utilization and **30%** utilization. US$100B, 90%, and 30% are illustrative inputs, not industry actuals.

The analysis has to include:

> **Revenue / Deployed Compute**

and actual **Utilization**.

A fixed depreciation period only describes the accounting expense schedule. It does not show whether the asset is generating enough cash flow.

## 6. Market-clearing prices can reveal economic depreciation first

Used accelerator / system prices, cloud lease rates, and delivery lead times can show generation obsolescence and oversupply before formal impairment appears.

If old-system residual value falls quickly when a new generation launches, buyer-side economic depreciation can move much faster than accounting depreciation.

That is why Chapter 24 treats Market Clearing as an independent S4 signal.

## 7. Algorithmic efficiency can accelerate economic obsolescence

If a new architecture can perform the same workload with less HBM, compute, or communication, an older system can lose competitiveness on cost per task even while it remains physically functional.

Software and model innovation can change hardware economic life directly.

### 7A. Efficiency–utilization break-even: the arithmetic has to close

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

This is an identity, not a forecast. If a hypothetical architecture reduces comparable resource intensity by **90%** ((I1/I0 = 0.1)), workload volume would have to rise **10×** merely to keep aggregate resource demand unchanged. The report does **not** claim that a 90% efficiency gain or a 10× workload increase will occur; the example is a D-grade sensitivity check.

For existing assets, the hurdle is stricter than aggregate break-even. New workload can migrate disproportionately toward newer systems with better cost per task, memory efficiency, power efficiency, or software support. Aggregate compute demand can remain flat or even grow while an older generation's utilization and residual value deteriorate.

This converts the efficiency question into an observable capital test:

- how quickly comparable cost per verified workload falls;
- how quickly total workload volume grows;
- how workload shifts across hardware generations;
- whether older-system utilization / lease rates / resale values fall faster than accounting depreciation.

Algorithmic progress is neither automatically expansionary nor contractionary for infrastructure demand. It is a **capital-recovery variable** whose effect depends on workload growth and generation-level allocation.

---

## 8. Power assets carry the opposite duration profile

In S2/S3 high-demand environments, long-duration power / grid assets can become scarce moats.

In S4, the same PPA, substation, or data-center shell can become a long-duration low-utilization burden.

Asset value depends on demand duration. "Power assets are always safe" is not a valid assumption.

## 9. Anchor Buyers lower financing risk while concentrating demand risk

Long-duration model-company compute contracts improve revenue visibility and can make infrastructure easier to finance.

But if an anchor buyer's revenue, financing, or architecture assumptions change, take-or-pay exposure, renegotiation, and stranded-capacity risk can become concentrated.

Customer concentration and contract duration have to be analyzed together with useful life.

## 9A. Financing structure can move losses without eliminating them

AI infrastructure can increasingly be financed through:

- operating leases;
- project finance;
- third-party infrastructure vehicles;
- long-duration customer contracts;
- supplier equity / credit enhancement.

Those structures change where depreciation, lease expense, interest cost, and residual-value risk appear.

They do not remove the underlying economic relationship:

> **if a new system delivers materially lower cost per task, older assets can lose economic value even while they still function.**

A lease can transfer ownership risk. Project finance can isolate part of the risk in an SPV. Seller credit can reduce financing friction.

None of those structures makes technological obsolescence disappear.

The important question is who ultimately bears residual-value risk and whether contracted cash flow is sufficient to cover it.

## 10. One depreciation cycle cannot determine 2036

Assets enter service on different dates, use different useful lives, and can experience impairment or changes in accounting estimates.

There is no single year in which "all 2026 CapEx finishes depreciating."

The 2036 structure depends on the second and third rounds of buildout, workload growth, system substitution, power, China's parallel stack, and regulation—not a mechanical first-cycle accounting schedule.

## 11. Current read

As of August 2026, the more accurate interpretation is that **CapEx expansion remains active while duration and utilization risk are rising**, rather than that a broad impairment cycle has already begun.

The depreciation wall becomes materially more dangerous when sustained utilization decline, rapid residual-value erosion, lower CapEx / commitment signals, and financing stress cross-confirm across actors/layers. Rising impairment strengthens the severity diagnosis when it appears, but formal accounting loss is not a mandatory gate.

## References

[^1]: Microsoft Corporation, FY26 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
[^2]: Alphabet Inc., 2025 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
[^3]: Meta Platforms, Inc., 2025 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
[^4]: Amazon.com, Inc., 2025 Form 10-K, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
