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
- 4Q25 transcript, using the company's corrected wording: **advanced packaging slightly over 10% of 2025 revenue**.[^5]

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

## 5. Packaging capacity must remain a separate physical pool

The formal report does not use a report-side "CoWoS wafers per rack" geometry factor to infer industry rack capacity.

Advanced-packaging capacity depends on packaging flow, interposer/substrate constraints, HBM integration, tool capacity, testing, yield, and qualification. It is not interchangeable with TSMC's front-end 12-inch-equivalent wafer shipments.

Therefore:

- front-end logic wafers cannot be divided by a packaging-geometry factor to infer rack output;
- packaging demand share cannot be converted into customer allocation;
- rack specifications cannot be converted into actual shipments without observed deployment data.

## 6. Why packaging can become the quantity gate before the node does

Leading-edge logic supply can grow through new fabs, process migration, and capacity expansion. Advanced packaging simultaneously depends on tools, interposers, substrates, testing, process flows, HBM integration, and qualification.

The result is:

> **logic wafer available ≠ system deliverable**

Advanced nodes are closer to an entry ticket into a frontier system; advanced packaging can become the quantity gate that determines how many complete systems are delivered. Both matter, but their physical units and expansion clocks are different.

## 7. Incremental packaging access must be evaluated directly

The forward question is not a synthetic cross-layer capture ratio.

It is whether competing buyers can obtain qualified advanced-packaging supply with acceptable:

- lead time;
- allocation fulfillment;
- delivery stability;
- supplier diversification;
- generation transition;
- integration yield.

That evidence should be evaluated directly at the packaging layer.

## 8. Cloud custom silicon does not automatically bypass packaging/HBM

Google, AWS, Microsoft, and Meta custom accelerator systems can divert part of NVIDIA's platform profit, but their next-generation systems still rely heavily on advanced logic, HBM, and high-density integration.

Two effects can therefore coexist:

1. **platform substitution:** in-house cloud systems reduce dependence on the full NVIDIA platform;
2. **upstream competition:** those same systems increase demand for the same advanced manufacturing, HBM, and packaging resources.

More custom silicon does not automatically mean lower CoWoS/HBM pressure.

## 9. Bottleneck location is not the same as profit location

Advanced packaging can be the system-delivery bottleneck without having the highest margin in the value chain. TSMC management stated in 2Q24 that advanced-packaging gross margin had historically been significantly below corporate average and was approaching, but had not yet reached, the company average.[^4]

Physical bottlenecks and profit pools therefore have to remain separate:

- packaging may determine **whether the system can be delivered**;
- the system platform can still capture stronger economics through software, interconnect, integration, and customer switching costs.

> **bottleneck location ≠ profit location**

This distinction is essential for AI-infrastructure value-capture analysis.

## 10. Packaging is an independent gate for China's Production-Grade Parallel Stack

A frontier AI parallel stack cannot be judged from logic nodes alone. Even if accelerator dies can be produced, insufficient advanced packaging, substrates, HBM integration, testing, or high-volume yield can still prevent stable delivery of large systems.

"Domestic chip production" therefore cannot hide packaging as an independent physical layer. China system closure must validate logic, HBM, packaging, interconnect, software, and power separately.

## 11. Current judgment and falsification

As of August 2026, the most defensible conclusions are:

- TSMC has confirmed advanced-packaging tightness with first-party evidence;
- TrendForce provides a B-grade institutional anchor for highly concentrated NVIDIA CoWoS demand;
- customer-level allocation remains undisclosed by TSMC;
- 5.37 wafers/rack is only a D-grade geometry stress test;
- custom silicon can still compete for the same upstream scarce resources.

The judgment that advanced packaging is a core scarce layer should be weakened if TSMC stops describing packaging as a growth constraint, lead times fall materially, customer-level allocation becomes more distributed, and HBM/packaging supply elasticity continues to improve.

## References

[^1]: TSMC, 4Q24 Earnings Conference Transcript, advanced packaging and testing >8% of revenue; capacity “very tight,” https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf
[^2]: TSMC, 2Q26 Earnings Conference Transcript, packaging capacity limiting customer growth, https://investor.tsmc.com/english/quarterly-results/2026/q2
[^3]: TrendForce, 2025 CoWoS demand structure, NVIDIA estimated >60%, B-grade institutional estimate, https://www.trendforce.com/research/download/RP250314ZJ
[^4]: TSMC, 2Q24 Earnings Conference Transcript, advanced-packaging margin relative to corporate average, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2024-08/5122725a56670882d777a8e8bfe0ed247cc55330/TSMC%202Q24%20Transcript.pdf
[^5]: TSMC, 4Q25 Earnings Conference Transcript, corrected 2025 advanced-packaging revenue identity, https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
