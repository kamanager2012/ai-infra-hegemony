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

Algorithm and architecture choices can change:

- activated compute;
- bytes/token;
- KV-cache requirements;
- communication patterns;
- batch / concurrency;
- serving efficiency.

Public cases such as DeepSeek-V3 / V2 show that architecture improvements can significantly change the unit resources required for a given capability.[^1][^2]

But a changed demand function does not eliminate physical constraints. Whether higher efficiency reduces aggregate infrastructure demand still depends on workload volume and demand elasticity.

## 4. Formal-training compute conversion is not full R&D cost

DeepSeek-V3 reports **2.788M H800 GPU-hours** for full formal training, and the paper uses a **US$2/GPU-hour** rental-cost assumption.[^1]

A clearly labeled **D-grade arithmetic conversion** is therefore:

> **2.788M × US$2 ≈ US$5.576M**

This is only a formal-training compute conversion. It excludes research iteration, failed runs, data engineering, engineering payroll, cluster depreciation, networking, storage, and the post-training ecosystem.

The US$5.576M figure can therefore be used as a public training-run scale anchor, but not as "the full company cost of one frontier model."

## 5. Rack-scale specifications quantify system intensity, not industry shipment demand

The official GB200 NVL72 configuration is:[^3]

- 72 Blackwell GPUs;
- 36 Grace CPUs;
- 13.4 TB HBM3E;
- 17 TB LPDDR5X.

These specifications are useful for describing the **material and memory intensity of one rack-scale system**.

They cannot be multiplied by an invented industry rack count and presented as actual HBM, LPDDR, packaging, or power demand.

Therefore:

> **per-system specification × observed deployment can support demand analysis; per-system specification × hypothetical deployment remains a scenario and should not be used as a factual industry total.**

Where shipment or deployment cannot be closed from public evidence, the formal report prefers seller commitments, vendor supply guidance, customer contracts, lead times, utilization, and other observable indicators over synthetic fleet-size arithmetic.

## 6. The HBM trade ratio amplifies bit-demand pressure on wafer input

Micron FY24 Q2 prepared remarks provide an important first-party boundary:

> **industrywide / same technology node / same number of bits**, HBM3E requires approximately **3× the wafer supply of DDR5**.[^4]

Bit demand and manufacturing input are therefore not one-to-one. As HBM bit share rises, pressure on DRAM wafer / cleanroom input can rise faster than bit share alone would suggest.

The 3× figure is not a fixed Micron-fab MES constant and cannot be mechanically extrapolated into a permanent HBM4/HBM5 ratio.

## 7. Packaging must be quantified in its own physical unit

Advanced-packaging analysis should use observable or source-bounded variables such as qualified capacity, lead time, allocation fulfillment, package starts, or supplier guidance.

The report does not use a synthetic "CoWoS wafers per rack" factor to infer shipments.

Front-end wafers, back-end packaging capacity, HBM bits, and energized MW are different physical pools and must remain dimensionally separate.

## 8. AI Capacity Gap: first ask whether effective supply is short now

For each physical layer (i), define:

```text
AI_Capacity_Gap_i(t)
= AI_Effective_Demand_i(t)
- AI_Effective_Capacity_i(t)
```

The layer (i) can separately represent:

- advanced logic;
- HBM / DRAM;
- advanced packaging;
- networking;
- power.

Demand and capacity must use the same:

- physical layer;
- delivery window;
- qualification / quality boundary;
- physical unit.

Examples include wafers/month, qualified package starts/month, bits/year, and MW.

Interpretation:

- **Gap > 0:** current effective supply is insufficient;
- **Gap ≈ 0:** the market is near balance;
- **Gap < 0:** effective slack exists.

---

## 9. Capacity Growth Gap describes direction, not the current shortage

Define:

```text
AI_Capacity_Growth_Gap_i(t)
= Growth(AI_Effective_Demand_i)
- Growth(AI_Effective_Capacity_i)
```

It answers:

> **Is the current supply-demand gap more likely to widen or narrow?**

- **Growth Gap > 0:** shortage pressure may intensify, or existing slack may shrink;
- **Growth Gap < 0:** supply is catching up and shortage pressure may ease;
- **Growth Gap = 0:** demand and capacity are growing at the same rate; it does not mean the current gap is zero.

Therefore:

> **Absolute Gap and Growth Gap must be read together.**

A market can still be short while supply is catching up rapidly, or still have slack while faster demand growth is eroding that slack.

---

## 10. Non-AI Residual Capacity answers a different question

AI Capacity Gap measures the AI side.

Traditional markets require a separate residual-access measure:

```text
NonAI_Residual(t)
= Effective_Supply(t)
- AI_Server_Absorption(t)
- Other_Priority_Demand(t)
```

It asks:

> **After AI and other priority demand absorb supply, how much effective capacity remains available to non-AI markets?**

AI Capacity Gap, AI Capacity Growth Gap, and Non-AI Residual Capacity are therefore not interchangeable. The first two describe AI-side balance and direction; the third describes residual access for traditional markets.

---

## 11. Power must also be quantified with state and physical boundaries

Approximately **120 kW/rack** can be used as a rack-level power-density input.[^5]

Power must also retain its state identity:

> Announced → Contracted / Secured → Permitted → Construction / Transition → Energized → Utilized

Contracted or secured capacity is not energized capacity; energized capacity is not highly utilized AI load. Generation MW/GW, PPA capacity, and IT-GW must also retain their distinct physical identities.

## 12. When shipment cannot be closed, Forward Commitment is more useful than an invented shipment model

NVIDIA's disclosed manufacturing, supply, and capacity commitments progressed as follows:[^6]

- 2026-01-25: **US$95.2B**;
- 2026-04-26: **US$119B**;
- 2026-07-26: **US$279B**.

The FY27 Q2 10-Q states that the latest commitments are primarily associated with memory and manufacturing facilities required for data-center infrastructure systems.

The figure cannot identify how much goes to any individual supplier, but it is an observable proxy for future resource-reservation intensity.

When customer-level HBM bits, CoWoS allocation, and rack shipment are unavailable, forward commitments are more informative than "revenue divided by an invented rack price."

## 13. Measure incremental scarce-capacity access separately for every physical layer

The report does not collapse advanced logic, HBM, advanced packaging, networking, and power into one composite "capture ratio."

For each layer, track variables such as:

- qualified supplier count;
- lead time;
- allocation fulfillment;
- long-term agreements / prepayments;
- delivery timing;
- buyer credit quality;
- supply elasticity.

A reliable percentage may be used only when customer-level allocation is observable for that specific physical pool.

## 14. Five risk classes should be separated before testing for cascade

System risk in AI infrastructure can be divided into:

1. **Physical bottleneck:** logic / HBM / packaging / interconnect;
2. **Power bottleneck:** grid / substation / permit / cooling;
3. **Capital / utilization risk:** asset utilization fails to cover depreciation, power, operations, and financing;
4. **System-substitution risk:** cloud custom stacks / open software change platform economics;
5. **Regulatory / geopolitical risk:** export controls, supply interruption, interface remedies, regional fragmentation.

One risk does not equal an industry-wide crisis. The more dangerous state is when several clocks begin to reinforce one another.

## 15. Rolling Bottleneck Cascade

AI-infrastructure bottlenecks rotate rather than remaining permanently fixed at one layer.

A positive expansion cascade can look like:

> HBM / packaging tight → hardware delivery constrained → supply expands → more racks reach sites → power / interconnection becomes binding → utilization becomes the next constraint

A reverse capital cascade can look like:

> power delay → utilization decline → buyer ROI decline → next CapEx slows → hardware orders slow → HBM / packaging tightness eases → upstream CapEx slows

This is the **Rolling Bottleneck Cascade**.

It explains why easing HBM does not prove that AI infrastructure has no constraints, and why power becoming a bottleneck does not mean semiconductor constraints have disappeared permanently.

## 16. Capital return must place all duration clocks into one equation

A minimal economic relationship is:

> **Economic Return = Revenue from deployed compute − Depreciation − Power − Operations − Financing**

The core risk is duration mismatch: hardware can turn over rapidly while data-center shells, grid assets, PPAs, and debt remain in place for much longer.

A technically functional system can therefore produce weak capital returns if utilization is low or long-duration obligations are excessive.

## 17. Quantitative guardrails

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

## 18. The most reliable quantitative sequence

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
