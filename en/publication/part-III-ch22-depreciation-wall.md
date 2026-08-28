# Part III · Chapter 22: The Depreciation Wall and Duration Mismatch

> **Publication-layer chapter.** Based primarily on [Volume 30](../vol-30.en.md). Chapter 19 covers CapEx expansion and Chapter 24 covers capital clearing. This chapter focuses on why different asset useful lives create a "depreciation wall" in AI infrastructure and why accounting depreciation and economic obsolescence are not the same thing.

## 1. The depreciation wall is not a fixed-dollar shock that must occur in one specific year

A more accurate definition is:

> **When hardware refresh / economic obsolescence runs faster than workload monetization, the cost of the installed asset base begins to reduce capital returns and alter the next round of CapEx.**

The depreciation wall therefore has to be read together with utilization, revenue, residual value, and next-generation investment.

## 2. Server useful lives are not uniform across the four major clouds

Current company disclosures show materially different server / network-equipment useful-life policies:

| Company | Server / network-equipment useful-life disclosure |
|---|---|
| Microsoft FY26 | 2–6 years |
| Alphabet 2025 | generally 6 years |
| Meta 2025 | 5–5.5 years |
| Amazon 2025 | 5–6 years; some assets changed from 6 years to 5 years in 2025 |

This is enough to show that one universal "four-year straight-line depreciation" assumption cannot be applied to the entire AI-infrastructure stack.

## 3. Accounting useful life is not economic life

A server can still be depreciating for accounting purposes even after a new architecture, better memory efficiency, newer software support, or better power efficiency makes it economically less competitive.

That is **economic obsolescence**.

Conversely, a data-center shell, substation, or PPA often has a much longer economic life than one accelerator generation.

The fundamental mismatch is therefore:

> **short-cycle compute vs. long-cycle physical infrastructure**

## 4. When demand weakens, clearing tends to follow an order

The first adjustments are usually:

1. next-generation hardware orders;
2. inventory;
3. used-system / lease prices;
4. discretionary expansion.

The slowest assets to adjust are data-center shells, grid assets, generation, and long-duration PPAs.

That is why a Capital Hard Landing is unlikely to complete in a single quarter.

## 5. CapEx has to be divided by utilization, not only by years

The same US$100B investment has very different economics at 90% utilization and 30% utilization.

The analysis therefore has to include:

> **Revenue / Deployed Compute**

and actual **Utilization**.

A fixed depreciation period only describes the accounting expense schedule. It does not show whether the asset is generating enough cash flow.

## 6. Market-clearing prices can signal economic depreciation faster than financial statements

Used accelerator / system prices, cloud lease rates, and delivery lead times can show generation obsolescence and oversupply before formal impairment appears.

If old-system residual value falls quickly when a new generation launches, buyer-side economic depreciation can move much faster than accounting depreciation.

That is why Chapter 24 treats Market Clearing as an independent S4 signal.

## 7. Algorithmic efficiency can also create economic obsolescence

If a new architecture can perform the same workload with less HBM, compute, or communication, an older system can lose competitiveness on cost per task even while it remains physically functional.

Software and model innovation can therefore change hardware economic life directly.

## 8. Power assets have the opposite risk profile

In S2/S3 high-demand environments, long-duration power / grid assets can become scarce moats.

In S4, the same PPA, substation, or data-center shell can become a long-duration low-utilization burden.

Asset value therefore depends on demand duration. "Power assets are always safe" is not a valid assumption.

## 9. Anchor Buyers can lower financing risk while concentrating demand risk

Long-duration model-company compute contracts improve revenue visibility and can make infrastructure easier to finance.

But if an anchor buyer's revenue, financing, or architecture assumptions change, take-or-pay exposure, renegotiation, and stranded-capacity risk can become concentrated.

Customer concentration and contract duration therefore have to be analyzed together with useful life.

## 10. 2036 cannot be derived mechanically from one 2026 depreciation cycle

Assets enter service on different dates, use different useful lives, and can experience impairment or changes in accounting estimates.

There is no single year in which "all 2026 CapEx finishes depreciating."

The 2036 structure depends on the second and third rounds of buildout, workload growth, system substitution, power, China's parallel stack, and regulation—not a mechanical first-cycle accounting schedule.

## 11. Current judgment

As of August 2026, the more accurate state is:

> **CapEx expansion + rising duration / utilization risk**

rather than a confirmed broad impairment cycle.

The combination that would make the depreciation wall dangerous is sustained utilization decline, rapid residual-value erosion, lower CapEx guidance, shrinking commitments, and rising impairment at the same time.

## Key public sources

- Microsoft FY26 10-K: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
- Alphabet 2025 10-K: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
- Meta 2025 10-K: https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
- Amazon 2025 10-K: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
