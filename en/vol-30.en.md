# Volume 30: The Depreciation Wall, Capital Clearing, and Long-Run Industry Structure

Chinese source edition: [vol-30.md](../vol-30.md)

> Retrieval and revision cutoff: **2026-08-28**. The “depreciation wall” is a capital-return mechanism, not a claim that one fixed dollar shock must occur in one predetermined year.

## 1. Depreciation is a capital constraint, not a calendar forecast

The depreciation-wall thesis is often simplified into:

> “A fixed amount of AI depreciation will hit profits in a specific year.”

The more defensible definition is:

> **When hardware refresh cycles move faster than workload monetization, the asset burden lowers capital returns and pressures the buyer to reduce the next investment round.**

Depreciation therefore has to be analyzed together with:

- utilization;
- revenue;
- residual value;
- next-generation CapEx.

## 2. Hardware and infrastructure have different economic lives

AI investment includes:

- accelerators and servers;
- networking;
- data-center shells;
- cooling;
- grid infrastructure;
- power contracts.

These assets do not share one useful life. Current first-party accounting policies also differ: Microsoft FY26 lists **2–6 years** for servers and network equipment; Alphabet 2025 generally uses **6 years**; Meta 2025 uses **5–5.5 years** for servers and network assets; Amazon 2025 uses **5–6 years** for servers and networking equipment. Companies can also revise these estimates as technology changes.

A universal “four-year straight-line depreciation” model is therefore inappropriate for the entire AI-infrastructure stack.

The key risk is **duration mismatch**:

> **shorter-cycle hardware vs. longer-cycle infrastructure**

The mismatch becomes more severe when the workload or architecture changes before the long-duration asset has earned an adequate return.

## 3. Where capital pressure appears first

When demand is weaker than expected, the fastest-moving adjustments are usually:

1. next-generation hardware orders;
2. inventory;
3. second-hand system prices;
4. discretionary expansion.

The slowest-moving assets include:

- power contracts;
- data-center shells;
- grid assets.

Capital clearing therefore has a sequence.

Short-duration assets reprice first; long-duration obligations remain.

## 4. CapEx cannot be interpreted without utilization

As an **illustrative sensitivity input**, the same **$100B** of CapEx can represent very different economics; $100B here is not an observed industry total.

At high utilization, it can be a productive growth asset.

At low utilization, it can be excess capacity.

The capital-cycle model therefore needs variables such as:

```text
Revenue / Deployed Compute
```

and:

```text
Utilization
```

CapEx alone is not enough.

## 5. Second-hand prices are important clearing signals

Financial statements can lag market conditions.

Second-hand GPU and system prices can reveal:

- oversupply;
- generational obsolescence;
- weaker demand.

If a new generation causes the residual value of the previous generation to fall sharply, the buyer's **economic depreciation** can accelerate even if accounting schedules do not change immediately.

Market-clearing prices are therefore useful S4 indicators.

## 6. Algorithmic efficiency can accelerate economic obsolescence

If a new model architecture delivers the same workload with less:

- HBM;
- FLOPS;
- network traffic;

then an older system can become economically obsolete before it becomes physically unusable.

This is **economic obsolescence**.

It can be more important than accounting depreciation in a rapidly changing technology cycle.

## 7. Long-duration power assets move in the opposite direction

Power and data-center infrastructure have much longer durations.

Under sustained AI demand, they can become scarce and valuable assets.

Under **S4 Capital Hard Landing**, the same assets can become stranded.

A long-duration PPA can therefore be:

- a moat in S2 or S3;
- a burden in S4.

Asset value depends on the future workload that actually uses the infrastructure.

## 8. Which firms can survive the capital cycle best?

Stronger positions generally combine one or more of:

- high utilization;
- diversified workloads;
- strong free cash flow;
- flexible system stacks;
- low financing cost;
- ownership of scarce assets.

System platforms, hyperscalers, power-asset owners, and foundries therefore experience the same cycle differently.

Their balance sheets and risk clocks are not interchangeable.

## 9. Model-company capital fragility

A model company that locks large amounts of long-duration compute without creating stable revenue can face:

- take-or-pay obligations;
- financing pressure;
- contract renegotiation;
- dilution.

The **Anchor Compute Buyer Effect** therefore creates both growth and concentration risk.

Demand certainty makes projects financeable, but weak monetization can turn the same commitment into a liability.

## 10. 2036 cannot be derived directly from 2026 depreciation

A 2026 investment wave will enter depreciation or amortization according to each asset's useful life, in-service date, impairments, and later estimate changes. There is no single year in which the whole wave mechanically “finishes depreciating.”

The industry structure in 2036 will depend on:

- whether second and third buildout waves occur;
- workload demand;
- system substitution;
- power;
- China's parallel stack;
- regulation.

A single depreciation cycle cannot determine which companies dominate a decade later.

Long-run structure is shaped by repeated investment and clearing rounds.

## 11. AI does not disappear after capital clearing

Even if **S4 Capital Hard Landing** occurs, the installed infrastructure still exists.

Historical fiber, telecom, and cloud cycles show a recurring pattern:

**capital overbuild  
→ asset-price decline  
→ lower access cost  
→ new applications**

AI infrastructure can follow a similar path.

Capital losses and long-run AI usage growth are therefore not contradictory.

## 12. Current judgment

As of **August 2026**, the evidence is insufficient to say that AI infrastructure has entered full capital clearing.

The current state is better described as:

> **CapEx expansion + rising ROI pressure**

The combination that would materially strengthen S4 is:

- falling utilization;
- lower CapEx guidance;
- declining supply commitments;
- rapidly falling second-hand system prices;
- increasing impairments;
- weakening enterprise AI monetization.

Only when several of these signals deteriorate together should S4 move from stress test to dominant current interpretation.


## Key public sources for this volume

- Microsoft FY26 10-K — servers/network equipment useful life 2–6 years: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
- Alphabet 2025 10-K — servers/network equipment generally 6 years: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
- Meta 2025 10-K — servers/network assets 5–5.5 years: https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
- Amazon 2025 10-K — servers/networking equipment 5–6 years; subset changed from 6 to 5 years in 2025: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
