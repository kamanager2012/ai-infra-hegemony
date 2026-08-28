# Part I · Chapter 6: Advanced Packaging, CoWoS, and the System-Delivery Bottleneck

## 1. Advanced packaging has become a system-delivery layer, not a supporting afterthought

Frontier AI accelerators increasingly depend on multi-die integration, HBM, large interposers, and high-speed die-to-die connections. Advanced packaging is no longer merely a downstream step after chip fabrication. It has become:

> **a scarce manufacturing layer that can determine how many complete frontier AI systems can actually be delivered.**

This explains an apparently contradictory state: foundry logic-wafer capacity can keep expanding while complete-system delivery remains constrained by insufficient packaging/HBM integration.

## 2. TSMC has confirmed tightness, but year-specific disclosure labels must remain separate

TSMC's public statements are sufficient to establish advanced-packaging tightness:[^1][^2]

- 4Q24: management described relevant capacity as **very tight** and unable to satisfy all customer demand;
- 2Q26: management stated more directly that packaging capacity was **so tight that now it limits my customers' growth**.

Revenue disclosures must retain their original year-specific labels:

- 4Q24 transcript: **advanced packaging and testing >8% of revenue**;
- 4Q25 transcript, using the company's corrected wording: **advanced packaging slightly over 10% of 2025 revenue**.[^6]

These labels are not perfectly identical. This report therefore does **not** treat >8% → >10% as a strict same-denominator time series, nor does it rewrite the 2025 "advanced packaging" figure back into "advanced packaging + testing."

## 3. CoWoS tightness is A-grade fact; customer allocation is not disclosed

TSMC public material supports the following: advanced packaging is tight, CoWoS is an important part of that system, and packaging tightness is limiting customer growth.

TSMC does not disclose an auditable customer-level CoWoS allocation table for this report, nor does it provide an official CoWoS share by customer.

Two questions therefore have to remain separate:

- **A-grade fact:** packaging / CoWoS tightness;
- **not disclosed:** exactly how much CoWoS capacity each customer receives.

Annual customer revenue share, wafer revenue share, and CoWoS customer share are not interchangeable.

## 4. NVIDIA >60% of CoWoS demand is a B-grade institutional anchor

TrendForce's research on 2025 CoWoS demand identifies NVIDIA as the largest demand customer and estimates its demand share at **more than 60%**.[^3]

The evidence grade must remain **B — institutional estimate**. The figure is useful for analyzing demand concentration and designing stress tests, but it cannot be rewritten as:

- TSMC officially confirming that NVIDIA received >60% of allocation;
- >60% being a 2026 actual;
- NVIDIA possessing exclusive CoWoS rights.

The correct use is: **highly concentrated demand has a real institutional anchor, while actual allocation still awaits first-party disclosure.**

## 5. 5.37 CoWoS wafers/rack is a D-grade geometry stress test

This report uses an order-of-magnitude geometry model:

72 GPU packages ÷ approximately 13.4 packages/wafer ≈ **5.37 CoWoS wafers/rack**. The 72-GPU input comes from NVIDIA's official NVL72 specification.[^4]

The inputs are:

- 72 GPUs from the official NVL72 specification;[^4]
- ~13.4 packages/wafer as a report-side geometry assumption;
- therefore, 5.37 as a **D-grade stress test**.

It is **not** TSMC disclosed yield, actual wafer starts, logic-wafer demand, or customer allocation.

This distinction matters because advanced-packaging wafers and TSMC's annual 12-inch-equivalent wafer shipments are not the same physical capacity pool.

## 6. Why total foundry wafer shipments cannot be divided by 5.37

TSMC shipped roughly **15.0M 12-inch-equivalent wafers** in 2025 across smartphones, HPC, automotive, IoT, mature nodes, and many other front-end products.[^7] The 5.37 figure is a report-side geometry stress test for **CoWoS packaging wafers per rack**.

The following calculation is physically invalid:

> total annual fab wafer shipments ÷ 5.37 = number of AI racks producible

It mixes the front-end logic wafer pool with the back-end advanced-packaging pool. Any resulting six-figure or million-rack number is not a fact about system-delivery capacity.

Likewise, front-end logic wafers/rack and back-end CoWoS wafers/rack cannot be added into one "TSMC wafers consumed per rack" metric. They sit in different manufacturing stages and capacity pools.

## 7. Why packaging can become the quantity gate before the node does

Leading-edge logic supply can grow through new fabs, process migration, and capacity expansion. Advanced packaging simultaneously depends on tools, interposers, substrates, testing, process flows, HBM integration, and qualification.

The result is:

> **logic wafer available ≠ system deliverable**

Advanced nodes are closer to an entry ticket into a frontier system; advanced packaging can become the quantity gate that determines how many complete systems are delivered. Both matter, but their physical units and expansion clocks are different.

## 8. Incremental Capacity Capture should be modeled as scenarios, not fabricated current shares

If incremental packaging capacity is C and one platform captures a share s, the residual increment available to other buyers is:

> **Residual = (1 − s) × C**

**Table 6.1 — Residual sensitivity under incremental packaging-capacity capture**

| Assumed capture rate | Residual for other buyers |
|---:|---:|
| 50% | 50% |
| 60% | 40% |
| 70% | 30% |
| 80% | 20% |

**Source:** Report D-grade scenario model.  
**Note:** Capture rates are not current TSMC customer-allocation facts; they are sensitivity inputs for studying concentration of incremental resources.

These 50/60/70/80% values are **D-grade scenario levels**, not TSMC's current customer allocation.

The model's purpose is to show nonlinearity: if a leading buyer consistently captures a larger share of **incremental** resources, the capacity left for second- and third-tier buyers can contract quickly even while total industry packaging capacity continues to grow.

## 9. Cloud custom silicon does not automatically bypass packaging/HBM

Google, AWS, Microsoft, and Meta custom accelerator systems can divert part of NVIDIA's platform profit, but their next-generation systems still rely heavily on advanced logic, HBM, and high-density integration.

Two effects can therefore coexist:

1. **platform substitution:** in-house cloud systems reduce dependence on the full NVIDIA platform;
2. **upstream competition:** those same systems increase demand for the same advanced manufacturing, HBM, and packaging resources.

More custom silicon does not automatically mean lower CoWoS/HBM pressure.

## 10. Bottleneck location is not the same as profit location

Advanced packaging can be the system-delivery bottleneck without having the highest margin in the value chain. TSMC management stated in 2Q24 that advanced-packaging gross margin had historically been significantly below corporate average and was approaching, but had not yet reached, the company average.[^5]

Physical bottlenecks and profit pools therefore have to remain separate:

- packaging may determine **whether the system can be delivered**;
- the system platform can still capture stronger economics through software, interconnect, integration, and customer switching costs.

> **bottleneck location ≠ profit location**

This distinction is essential for AI-infrastructure value-capture analysis.

## 11. Packaging is also an independent closure gate for China's Parallel Stack

A frontier AI parallel stack cannot be judged from logic nodes alone. Even if accelerator dies can be produced, insufficient advanced packaging, substrates, HBM integration, testing, or high-volume yield can still prevent stable delivery of large systems.

"Domestic chip production" therefore cannot hide packaging as an independent physical layer. China system closure must validate logic, HBM, packaging, interconnect, software, and power separately.

## 12. Current judgment and falsification

As of August 2026, the most defensible conclusions are:

- TSMC has confirmed advanced-packaging tightness with first-party evidence;
- TrendForce provides a B-grade institutional anchor for highly concentrated NVIDIA CoWoS demand;
- customer-level allocation remains undisclosed by TSMC;
- 5.37 wafers/rack is only a D-grade geometry stress test;
- custom silicon can still compete for the same upstream scarce resources.

The judgment that advanced packaging is a core scarce layer should be weakened if TSMC stops describing packaging as a growth constraint, lead times fall materially, customer-level allocation becomes more distributed, and HBM/packaging supply elasticity continues to improve.

## References

[^1]: TSMC, 4Q24 Earnings Conference Transcript, advanced packaging and testing >8% of revenue; capacity “very tight,” https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf
[^2]: TSMC, 2Q26 Earnings Conference Transcript, packaging capacity limiting customer growth, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
[^3]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^4]: NVIDIA, “GB200 NVL72,” official product page, 72 Blackwell GPUs per rack, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^5]: TSMC, 2Q24 Earnings Conference Transcript, advanced-packaging margin relative to corporate average, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2024-08/5122725a56670882d777a8e8bfe0ed247cc55330/TSMC%202Q24%20Transcript.pdf
[^6]: TSMC, 4Q25 Earnings Conference Transcript, corrected 2025 advanced-packaging revenue identity, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
[^7]: TSMC, 2025 Annual Report, annual wafer shipments and manufacturing footprint, https://investor.tsmc.com/static/annualReports/2025/english/index.html
