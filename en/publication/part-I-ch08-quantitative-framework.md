# Part I · Chapter 8: Quantitative Framework for AI Infrastructure and the Rolling Bottleneck Cascade

## 1. The purpose of quantification is not to manufacture false precision

The most common quantitative error in AI-infrastructure research is to connect different physical pools, accounting categories, and evidence grades into one apparently complete but unauditable total model.

This report allows four classes of quantitative work into the main argument:

1. **Compute / memory intensity**;
2. **Rack-scale material demand**;
3. **Explicit packaging / power stress tests**;
4. **Capacity / commitment / utilization indicators**.

Any link that cannot be closed with public data remains a parameter rather than being filled with an invented point estimate.

## 2. Roofline: why frontier inference cannot be compared through FLOPS alone

The core Roofline relationship is:

> **Performance = min(Peak Compute, Memory Bandwidth × Arithmetic Intensity)**

The critical arithmetic intensity is:

> **I_critical = Peak Compute / Memory Bandwidth**

When workload arithmetic intensity falls below the critical threshold, the system becomes memory-bound.

Autoregressive inference repeatedly reads model state, KV cache, routing, and activation data. Actual token throughput can therefore remain constrained by HBM bandwidth and memory movement even when accelerator peak FLOPS are very high.

This is why HBM, interconnect, and compute have to be analyzed as one system rather than interpreting frontier inference from peak compute alone.

## 3. Algorithmic architecture changes the demand function without deleting physical constraints

First-party anchors from the DeepSeek-V3 Technical Report include:[^1]

- 671B total parameters;
- 37B activated parameters;
- 14.8T pre-training tokens;
- **2.664M H800 GPU-hours for pre-training**;
- **2.788M H800 GPU-hours for full formal training**.

DeepSeek-V2 separately reports, relative to DeepSeek 67B:[^2]

- approximately **93.3% KV-cache reduction**;
- approximately **5.76× maximum generation throughput**.

These results belong to different model versions and must not be mixed.

Their shared methodological implication is that architecture can change bytes/token, activated compute, communication patterns, and serving concurrency. It therefore changes the demand function for HBM, networking, and compute.

But a changed demand function does not eliminate physical constraints. Whether higher efficiency reduces aggregate infrastructure demand still depends on workload volume and demand elasticity.

## 4. Formal-training compute conversion is not full R&D cost

DeepSeek-V3 reports **2.788M H800 GPU-hours** for full formal training.

Using the paper's **US$2/GPU-hour** assumption:

> **2.788M × US$2 ≈ US$5.576M**

This is only a formal-training compute conversion. It excludes research iteration, failed runs, data engineering, engineering payroll, cluster depreciation, networking, storage, and the post-training ecosystem.

The US$5.576M figure can therefore be used as a public training-run scale anchor, but not as "the full company cost of one frontier model."

## 5. Rack-scale BOM can be quantified; rack shipment cannot be invented

The official GB200 NVL72 configuration is:[^3]

- 72 Blackwell GPUs;
- 36 Grace CPUs;
- 13.4 TB HBM3E;
- 17 TB LPDDR5X.

If a scenario contains R racks:

> **HBM(R) = 13.4 TB × R**

> **LPDDR(R) = 17 TB × R**

**Table 8.1 — NVL72 rack count and HBM/LPDDR scenario demand**

| Scenario rack count | HBM3E | LPDDR5X |
|---:|---:|---:|
| 1,000 | 13.4 PB | 17 PB |
| 10,000 | 134 PB | 170 PB |
| 30,000 | 402 PB | 510 PB |
| 50,000 | 670 PB | 850 PB |

**Source:** NVIDIA official GB200 NVL72 specification; report scenario arithmetic.[^3]  
**Note:** Rack count is an assumed input; the PB values are not actual shipments or consumption.

These are **D-grade scenario calculations**.

NVIDIA does not disclose an annual NVL72 rack-shipment figure that can be multiplied by these specifications. It is therefore invalid to divide Data Center revenue by an invented rack ASP and propagate the resulting hypothetical rack count into "actual" HBM, CoWoS, or power consumption.

## 6. The HBM trade ratio amplifies bit-demand pressure on wafer input

Micron FY24 Q2 prepared remarks provide an important first-party boundary:

> **industrywide / same technology node / same number of bits**, HBM3E requires approximately **3× the wafer supply of DDR5**.[^4]

Bit demand and manufacturing input are therefore not one-to-one. As HBM bit share rises, pressure on DRAM wafer / cleanroom input can rise faster than bit share alone would suggest.

The 3× figure is not a fixed Micron-fab MES constant and cannot be mechanically extrapolated into a permanent HBM4/HBM5 ratio.

## 7. Packaging geometry can support sensitivity analysis, not shipment claims

The report uses approximately **5.37 CoWoS wafers/rack** as a D-grade geometry stress test:

> **72 packages ÷ 13.4 packages/wafer ≈ 5.37 wafers/rack**

The 13.4 packages/wafer denominator is a report-side geometry assumption, not a TSMC disclosed yield or packages-per-wafer metric.

The 5.37 figure may therefore be used for:

- packaging-demand order of magnitude;
- scenario comparison;
- bottleneck sensitivity.

It cannot be used to divide TSMC annual front-end wafer shipments, infer actual Blackwell shipments, or derive customer allocation.

## 8. Power must also be quantified with state and physical boundaries

Approximately **120 kW/rack** can be used as a rack-level power-density input.[^5]

> 500 racks × 120 kW = **60 MW of rack-level full-load power**

This calculation does not include complete facility overhead and does not mean any specific campus has deployed 500 racks.

Power must also retain its state identity:

> Announced → Contracted → Permitted → Energized → Utilized

Contracted MW is not energized MW; energized MW is not highly utilized AI load.

## 9. When shipment cannot be closed, Forward Commitment is more useful than an invented shipment model

NVIDIA's disclosed manufacturing, supply, and capacity commitments progressed as follows:[^6]

- 2026-01-25: **US$95.2B**;
- 2026-04-26: **US$119B**;
- 2026-07-26: **US$279B**.

The FY27 Q2 10-Q states that the latest commitments are primarily associated with memory and manufacturing facilities required for data-center infrastructure systems.

The figure cannot identify how much goes to any individual supplier, but it is an observable proxy for future resource-reservation intensity.

When customer-level HBM bits, CoWoS allocation, and rack shipment are unavailable, forward commitments are more informative than "revenue divided by an invented rack price."

## 10. AHICR: measure incremental capture separately for every scarce layer

The report uses the **Advanced/HPC Incremental Capacity Capture Ratio (AHICR)**:

> **AHICR(layer) = incremental advanced AI/HPC resource captured by one buyer ÷ total industry increment in that physical layer**

AHICR must be observed separately for:

- advanced logic;
- HBM;
- advanced packaging;
- power.

These units cannot be added into one universal "resource ownership" percentage.

The value of AHICR is to test whether next-generation incremental resources are increasingly captured by a small number of buyers—not to reinterpret historical revenue share as future allocation.

## 11. Five risk classes should be separated before testing for cascade

System risk in AI infrastructure can be divided into:

1. **Physical bottleneck:** logic / HBM / packaging / interconnect;
2. **Power bottleneck:** grid / substation / permit / cooling;
3. **Capital / utilization risk:** asset utilization fails to cover depreciation, power, operations, and financing;
4. **System-substitution risk:** cloud custom stacks / open software change platform economics;
5. **Regulatory / geopolitical risk:** export controls, supply interruption, interface remedies, regional fragmentation.

One risk does not equal an industry-wide crisis. The more dangerous state is when several clocks begin to reinforce one another.

## 12. Rolling Bottleneck Cascade

AI-infrastructure bottlenecks rotate rather than remaining permanently fixed at one layer.

A positive expansion cascade can look like:

> HBM / packaging tight → hardware delivery constrained → supply expands → more racks reach sites → power / interconnection becomes binding → utilization becomes the next constraint

A reverse capital cascade can look like:

> power delay → utilization decline → buyer ROI decline → next CapEx slows → hardware orders slow → HBM / packaging tightness eases → upstream CapEx slows

This is the **Rolling Bottleneck Cascade**.

It explains why easing HBM does not prove that AI infrastructure has no constraints, and why power becoming a bottleneck does not mean semiconductor constraints have disappeared permanently.

## 13. Capital return must place all duration clocks into one equation

A minimal economic relationship is:

> **Economic Return = Revenue from deployed compute − Depreciation − Power − Operations − Financing**

The core risk is duration mismatch: hardware can turn over rapidly while data-center shells, grid assets, PPAs, and debt remain in place for much longer.

A technically functional system can therefore produce weak capital returns if utilization is low or long-duration obligations are excessive.

## 14. Quantitative guardrails

The full report maintains the following hard boundaries:

- revenue share ≠ wafer share;
- platform revenue share ≠ physical shipment share;
- contracted MW ≠ energized MW;
- energized MW ≠ utilized AI load;
- rack spec × hypothetical racks ≠ shipment;
- CoWoS geometry ≠ fab yield;
- CapEx guidance ≠ actual CapEx;
- AI exposure ≠ job loss;
- model rental conversion ≠ full company cash cost;
- institutional forecast ≠ company actual;
- one physical pool ≠ another physical pool.

## 15. The most reliable quantitative sequence

The report follows this sequence:

> **official system spec → material identity → scenario demand → supply constraint → forward commitment → utilization → falsification**

The alternative—starting with a grand end-state and searching backward for numbers to fill a model—is not accepted.

This discipline does not require conservative scenarios. It allows scenarios to remain ambitious while preserving an auditable fact layer and consistent physical dimensions.

## References

[^1]: DeepSeek-AI, “DeepSeek-V3 Technical Report,” https://arxiv.org/abs/2412.19437
[^2]: DeepSeek-AI, “DeepSeek-V2,” repository and technical report, https://github.com/deepseek-ai/DeepSeek-V2
[^3]: NVIDIA, “GB200 NVL72,” official product page, https://www.nvidia.com/en-us/data-center/gb200-nvl72/
[^4]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^5]: NVIDIA, DGX GB200 Hardware Guide, rack power approximately 120 kW, https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
[^6]: NVIDIA Corporation, FY27 Q2 Form 10-Q, aggregate manufacturing, supply and capacity commitments, U.S. SEC, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
