# Macro Essay 3: Physical Manufacturing Limits and the Global Semiconductor Supply Contest

Chinese source edition: [part2-03.md](../part2-03.md)

> Retrieval and revision cutoff: **2026-08-27**. Advanced logic, advanced packaging, and HBM are different physical pools. Their metrics cannot be substituted for one another, and the shortest layer determines system delivery.

## 1. The core question

Around 2026, which physical layer most directly limits rack-scale AI-system delivery?

The answer cannot be derived from one number such as:

- TSMC's largest-customer revenue share;
- HPC revenue share;
- packaging revenue share;
- an estimated CoWoS monthly capacity;
- an HBM bit share.

These quantities measure different objects.

The correct framework separates three ceilings:

1. **leading-edge logic**;
2. **advanced packaging**;
3. **HBM / DRAM manufacturing input**.

All three must be satisfied at the same time.

## 2. Leading-edge logic: an entry ticket, not the full delivery system

TSMC's 2025 public disclosures show:

- 3 nm at **24% of wafer revenue**;
- 5 nm at **36%**;
- 7 nm at **14%**;
- 7 nm and below at **74%**;
- HPC at **58% of revenue**;
- N2 entering volume production in **4Q25**.

These are strong indicators of leading-edge concentration and HPC demand.

They do not disclose:

- physical wafers by customer;
- N2 customer allocation;
- N2 revenue share;
- customer-level frontier-AI capacity.

A node is therefore the **entry ticket**.

It is not the complete system-delivery constraint.

## 3. Advanced packaging: the clearest first-party short-term bottleneck

TSMC has repeatedly described advanced-packaging capacity as very tight.

The company said in 2024 Q4 that it could not meet all customer needs.

By 2026 Q2, management said packaging capacity was tight enough to **limit customers' growth**.

TSMC also disclosed advanced packaging + testing at approximately:

- **8% of revenue in 2024**;
- slightly above **10% in 2025**.

The key evidence boundary is:

> **Packaging tightness is first-party fact. Customer-level CoWoS allocation is not publicly disclosed by TSMC.**

That makes advanced packaging one of the clearest observable short-term delivery constraints.

## 4. The 5.39 wafers-per-rack coefficient is a geometry stress test

The report's working relation is:

```text
72 GPU packages
÷ 13.4 packages per CoWoS wafer
≈ 5.39 CoWoS wafers per rack
```

The **72** is tied to the official NVL72 configuration.

The **13.4 packages per wafer** term is a geometry assumption.

The resulting **5.39** is therefore **D-grade engineering geometry**.

It is not:

- a TSMC-disclosed yield;
- a front-end logic-wafer coefficient;
- a customer-allocation disclosure.

The coefficient is useful for scenario stress tests.

It is not valid to divide TSMC's full annual wafer shipments by 5.39 and claim a global rack-production limit.

That mixes different physical pools.

## 5. Why the “835,000 racks” style calculation fails

TSMC's full-fab wafer shipments include:

- smartphones;
- automotive;
- IoT;
- mature-node products;
- many non-CoWoS flows.

CoWoS is a back-end advanced-packaging pool.

Front-end logic wafers are another pool.

A rack can consume both, but their coefficients cannot be added or applied to the same denominator.

This is the central quantitative discipline:

> **Do not divide a packaging coefficient into a foundry-wide front-end wafer total.**

A model can look arithmetically clean while being physically meaningless.

## 6. HBM: manufacturing pressure exceeds simple bit share

Micron disclosed that HBM3E requires roughly **3× the wafer supply of DDR5** for the same number of bits at the same technology node.

This is **A-grade first-party evidence**.

TrendForce estimates that HBM + RDIMM represent about **51% of 2026 DRAM bits**.

Together, these observations show why AI/server memory can consume a disproportionate share of manufacturing input.

The ~3× figure is not:

- a price multiple;
- a permanent universal constant;
- a fab-accounting identity.

It is a defined industry trade ratio.

## 7. Scarcity moves across the three ceilings

The binding constraint can migrate.

### If packaging is tight

Logic exists, but complete systems cannot be assembled fast enough.

### If packaging loosens

HBM or power may become the next bottleneck.

### If HBM expands

Leading-edge logic, power, or utilization can become more important.

This is why the report uses the **Rolling Bottleneck Cascade** rather than declaring one layer permanently dominant.

## 8. Customer concentration must be read carefully

TSMC's largest customer represented **19% of 2025 annual revenue**.

That is not:

- 19% of CoWoS;
- 19% of N2;
- 19% of frontier-AI wafers.

Revenue share can change because the numerator changes, the company-wide denominator changes, or both.

The forward strategic question is therefore not historical share.

It is **incremental scarce-capacity capture** across each physical layer.

## 9. Current macro judgment

As of August 2026:

- advanced logic remains highly concentrated;
- N2 has entered production but customer allocation remains undisclosed;
- advanced packaging is explicitly described by TSMC as growth-limiting;
- HBM's manufacturing-input intensity is confirmed by Micron;
- cloud custom systems continue to bid for the same upstream resources.

The correct macro picture is:

> **process is the entry ticket, packaging is a quantity gate, and HBM is a manufacturing-input multiplier.**

The shortest of the three determines how many complete frontier systems can actually leave the line.
