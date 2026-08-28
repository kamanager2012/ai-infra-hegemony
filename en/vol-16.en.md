# Volume 16: Quantitative Framework for AI Infrastructure — Compute, Memory, Packaging, and Capacity

Chinese source edition: [vol-16.md](../vol-16.md)

> Retrieval and revision cutoff: **2026-08-27**. The purpose of this framework is not to produce one supposedly precise future. It is to keep physical units, evidence grades, and observable variables separate enough that the model can be falsified.

## 1. What the quantitative framework is designed to do

The easiest mistake in AI-infrastructure quantification is to connect numbers from different physical pools and different evidence grades until they look like one precise model.

This volume limits itself to four classes of reproducible analysis:

1. compute and memory intensity;
2. rack-scale material demand;
3. advanced-packaging geometry stress tests;
4. capacity and commitment indicators.

Any quantity that cannot be closed with public data remains a parameter. It is not filled with a convenient point estimate.

## 2. Roofline: why inference is often constrained by memory bandwidth first

The basic Roofline relationship is:

```text
Performance
= min(
    Peak Compute,
    Memory Bandwidth × Arithmetic Intensity
  )
```

The critical arithmetic intensity is:

```text
I_critical
= Peak Compute / Memory Bandwidth
```

When a workload's arithmetic intensity falls below that threshold, the system is in the memory-bound region.

Autoregressive inference repeatedly reads model state and KV cache. Peak FLOPS can therefore rise much faster than realized token throughput if HBM bandwidth and memory movement remain the binding constraint.

That is why frontier-inference performance cannot be evaluated from FLOPS alone.

## 3. MLA: architecture can directly change memory demand

The DeepSeek-V3 technical report discloses:

- **671B** total parameters;
- **37B** activated parameters;
- **14.8T** pre-training tokens;
- **2.788M H800 GPU-hours**;
- MLA compressed KV dimension **d_c = 512**.

The DeepSeek-V2 technical report separately reports, relative to DeepSeek 67B:

- KV-cache reduction of approximately **93.3%**;
- maximum generation throughput of approximately **5.76×**.

Those figures refer to different model generations and should not be combined into one benchmark claim.

The important mechanism is:

> **Model architecture can reduce bytes per token, changing concurrency and serving cost for a given amount of HBM capacity.**

That does not make memory bandwidth irrelevant. It changes the demand function imposed on the memory system.

## 4. How to interpret DeepSeek's training-cost figure

DeepSeek-V3 reports approximately **2.788M H800 GPU-hours** for the full training run.

Using the report-side rental assumption of **$2 per GPU-hour** gives:

```text
2.788M × US$2 ≈ US$5.576M
```

This is **not** the full cash cost of developing a frontier model.

It does not include, among other items:

- research iteration;
- failed runs and ablations;
- data collection and cleaning;
- engineering payroll;
- infrastructure depreciation;
- networking;
- storage;
- the post-training ecosystem.

The figure is useful as an anchor for **effective training-compute scale**. It should not be restated as “a frontier model costs only $5.6M to build.”

## 5. Rack-scale memory demand

The official GB200 NVL72 configuration includes:

- **72 Blackwell GPUs**;
- **36 Grace CPUs**;
- **13.4 TB HBM3E**;
- **17 TB LPDDR5X**.

For a scenario with (R) racks:

```text
HBM(R) = 13.4 TB × R
LPDDR(R) = 17 TB × R
```

| Scenario rack count | HBM3E | LPDDR5X |
|---:|---:|---:|
| 1,000 | 13.4 PB | 17 PB |
| 10,000 | 134 PB | 170 PB |
| 30,000 | 402 PB | 510 PB |
| 50,000 | 670 PB | 850 PB |

These are **scenario-demand identities**, not shipment estimates.

They are useful because the physical bill of materials is observable even when actual rack shipments are not.

## 6. HBM wafer-supply trade ratio

Micron's FY24 Q2 prepared remarks disclosed an industry-wide relationship for HBM3E:

```text
HBM3E wafer supply
≈ 3 × DDR5 wafer supply
```

for the **same technology node** and the **same number of bits**.

The implication is that rising HBM bit demand can amplify pressure on DRAM wafer supply.

This is **A-grade first-party company evidence**. It is a trade ratio under a defined comparison, not a universal constant that can be mechanically extended to every future HBM generation.

Public source: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf

## 7. Advanced-packaging geometry stress test

The report uses **5.37 CoWoS wafers per rack** as a **D-grade geometry stress test**.

The working relationship is:

```text
72 packages
÷ 13.4 packages per wafer
≈ 5.37 wafers per rack
```

The **13.4 packages per wafer** term is a geometry assumption. It is not a TSMC-disclosed yield.

The result is therefore suitable for:

- order-of-magnitude packaging demand;
- scenario comparison;
- bottleneck sensitivity analysis.

It is **not** suitable for:

- dividing TSMC annual wafer shipments;
- inferring actual Blackwell shipments;
- inferring customer-level CoWoS allocation.

The distinction between a geometry coefficient and an observed manufacturing yield is a hard quantitative guardrail.

## 8. Why public data cannot close the shipment model directly

At least three critical public splits are missing:

- actual rack shipments;
- customer-level HBM bits;
- customer-level CoWoS allocation.

Inferring rack counts directly from Data Center revenue introduces an unknown system ASP.

Using that inferred rack count to estimate HBM and CoWoS demand would then propagate one unknown into several apparently precise outputs.

The publication framework therefore uses:

> **observable demand anchors + scenario rack counts + physical system BOM**

rather than:

> **revenue ÷ assumed rack price**.

## 9. Supply commitments are a stronger forward indicator when shipment splits are missing

When shipment detail is unavailable, disclosed supply commitments provide a more defensible forward indicator than a fabricated unit model.

NVIDIA reported manufacturing, supply, and capacity commitments of:

- **US$95.2B** as of 2026-01-25;
- **US$119B** as of 2026-04-26;
- **US$279B** as of 2026-07-26.

The FY27 Q2 10-Q says the latest commitments are primarily tied to memory and manufacturing facilities for data-center infrastructure systems. Source: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm .

These commitments reflect reservation of inventory and manufacturing capacity for future product supply.

They do not disclose the amount assigned to each supplier, technology, or packaging line. But they provide an observable proxy for the intensity of forward resource reservation.

## 10. AHICR: Advanced/HPC Incremental Capacity Capture Ratio

The report introduces:

```text
AHICR
= incremental advanced AI/HPC resources captured by one buyer
  / total incremental advanced AI/HPC resources
```

The numerator and denominator should be evaluated **separately by scarce layer**, including:

- advanced logic;
- HBM;
- CoWoS;
- power.

AHICR is not one synthetic unit that adds wafers, memory bits, packaging, and megawatts together.

Its purpose is to measure how much of the **incremental scarce capacity** a buyer captures within each physical pool.

That makes it more useful for forward resource competition than a historical revenue share.

## 11. Quantitative guardrails

The report applies the following non-equivalences throughout:

- **revenue share ≠ wafer share**;
- **contracted MW ≠ energized MW**;
- **rack specification × hypothetical racks ≠ shipments**;
- **CoWoS geometry ≠ fab yield**;
- **CapEx guidance ≠ actual CapEx**;
- **AI exposure ≠ job loss**;
- **model rental-cost conversion ≠ full company cash cost**.

These are not wording preferences. They prevent unit errors from becoming false industrial conclusions.

## 12. Current conclusion

AI infrastructure can be quantified, but only if dimensions remain consistent.

The most reliable sequence is:

**official system specification  
→ material identity  
→ scenario demand  
→ supply constraint  
→ financial commitment  
→ falsification**

The wrong sequence is to choose a large conclusion first and then backfill numbers until the model appears closed.

Quantification is most useful when it shows exactly **which variable is observed, which one is assumed, and which missing disclosure prevents the next step from being treated as fact**.

## Key public sources for this volume

- DeepSeek-V3 Technical Report — pre-training 2.664M; full formal training 2.788M H800 GPU-hours: https://arxiv.org/abs/2412.19437
- DeepSeek-V2 — 93.3% KV-cache reduction and 5.76× maximum generation throughput relative to DeepSeek 67B: https://github.com/deepseek-ai/DeepSeek-V2
- NVIDIA GB200 NVL72 product page — 36 Grace CPUs, 72 Blackwell GPUs, 13.4 TB HBM3E, 17 TB LPDDR5X: https://www.nvidia.com/en-us/data-center/gb200-nvl72/
- Micron FY24 Q2 event page: https://investors.micron.com/events/event-details/microns-second-quarter-2024-financial-call
- Micron FY24 Q2 prepared remarks — industrywide HBM3E ≈3× DDR5 wafer supply at same node / same bits: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- NVIDIA FY26 10-K — 2026-01-25 supply/capacity commitments baseline: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
- NVIDIA FY27 Q2 10-Q — US$279B commitments: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
