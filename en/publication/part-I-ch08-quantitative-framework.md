# Part I · Chapter 8: Quantitative Framework — What Can Be Measured, What Cannot, and Why

## 1. Quantification starts with denominator closure

The first quantitative question is not “what is the number?” It is **whether a defensible number exists at all**.

A metric is admissible only when numerator, denominator, physical unit, delivery window, qualification boundary, and evidence identity can be made consistent. Front-end wafers, HBM bits, package starts, energized MW, accounting CapEx, and seller commitments are not interchangeable components of one synthetic total.

The report therefore permits four quantitative classes in the main argument:

1. **Compute / memory intensity**;
2. **Rack-scale material or power intensity**;
3. **Layer-specific stress tests**;
4. **Capacity / commitment / utilization indicators**.

If a public denominator cannot be closed, the variable remains a parameter or proxy. The report does not insert a point estimate merely to create the appearance of completeness.

## 2. Peak FLOPS is not a workload denominator

The core Roofline relationship is:

> **Performance = min(Peak Compute, Memory Bandwidth × Arithmetic Intensity)**

The critical arithmetic intensity is:

> **I_critical = Peak Compute / Memory Bandwidth**

When workload arithmetic intensity falls below the critical threshold, the system becomes memory-bound.

Autoregressive inference repeatedly reads model state, KV cache, routing, and activation data. Actual token throughput can therefore remain constrained by HBM bandwidth and memory movement even when accelerator peak FLOPS are very high.

This is why HBM, interconnect, and compute have to be analyzed as one system rather than interpreting frontier inference from peak compute alone.

## 3. Efficiency changes the demand function, not the measurement standard

Algorithm and architecture choices can change:

- activated compute;
- bytes/token;
- KV-cache requirements;
- communication patterns;
- batch / concurrency;
- serving efficiency.

Public cases such as DeepSeek-V3 / V2 show that architecture improvements can significantly change the unit resources required for a given capability.[^1][^2]

But a changed demand function does not eliminate physical constraints. Whether higher efficiency reduces aggregate infrastructure demand still depends on workload volume and demand elasticity.

## 4. Training-run arithmetic is a bounded cost conversion

DeepSeek-V3 reports **2.788M H800 GPU-hours** for full formal training, and the paper uses a **US$2/GPU-hour** rental-cost assumption.[^1]

A clearly labeled **D-grade arithmetic conversion** is therefore:

> **2.788M × US$2 ≈ US$5.576M**

This is only a formal-training compute conversion. It excludes research iteration, failed runs, data engineering, engineering payroll, cluster depreciation, networking, storage, and the post-training ecosystem.

The US$5.576M figure can therefore be used as a public training-run scale anchor, but not as "the full company cost of one frontier model."

## 5. System specs support intensity analysis, not deployment inference

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

## 6. HBM: bits and wafer input are different denominators

Micron FY24 Q2 prepared remarks provide an important first-party boundary:

> **industrywide / same technology node / same number of bits**, HBM3E requires approximately **3× the wafer supply of DDR5**.[^4]

Bit demand and manufacturing input are therefore not one-to-one. As HBM bit share rises, pressure on DRAM wafer / cleanroom input can rise faster than bit share alone would suggest.

The 3× figure is not a fixed Micron-fab MES constant and cannot be mechanically extrapolated into a permanent HBM4/HBM5 ratio.

## 7. Advanced packaging requires a separate physical denominator

Advanced-packaging analysis should use observable or source-bounded variables such as qualified capacity, lead time, allocation fulfillment, package starts, or supplier guidance.

The report does not use a synthetic "CoWoS wafers per rack" factor to infer shipments.

Front-end wafers, back-end packaging capacity, HBM bits, and energized MW are different physical pools and must remain dimensionally separate.

## 8. Absolute Capacity Gap: current balance

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

## 9. Capacity Growth Gap: direction of travel

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

## 11. Power needs both physical quantity and delivery state

Approximately **120 kW/rack** can be used as a rack-level power-density input.[^5]

Power must also retain its state identity:

> Announced → Contracted / Secured → Permitted → Construction / Transition → Energized → Utilized

Contracted or secured capacity is not energized capacity; energized capacity is not highly utilized AI load. Generation MW/GW, PPA capacity, and IT-GW must also retain their distinct physical identities.

### Table 8.1 — NVL72 rack-to-MW D-grade intensity conversion

| Item | Official / known input | Mechanical conversion at 1 MW of rack IT load |
|---|---:|---:|
| Rack power | ≈120 kW / rack | ≈8.33 racks |
| GPU | 72 / rack | ≈600 GPUs |
| HBM3E | 13.4 TB / rack | ≈111.7 TB |
| LPDDR5X | 17 TB / rack | ≈141.7 TB |

**Source:** NVIDIA GB200 NVL72 official specification and DGX GB200 Hardware Guide.[^3][^5]  
**Note:** This is a **D-grade mechanical intensity conversion**. It answers only: “if 1 MW of rack IT load were composed entirely of this rack configuration, what would the hardware intensity be?” It is **not** a shipment, deployment, energized-facility, or industry-demand estimate, and it excludes PUE, network/storage, power-conversion, redundancy, and facility overhead.

This kind of conversion turns system specifications into auditable engineering intensity while preserving the boundary that specification is not deployment.

## 12. When shipment is unobservable, use bounded forward indicators

NVIDIA's disclosed manufacturing, supply, and capacity commitments progressed as follows:[^6]

- 2026-01-25: **US$95.2B**;
- 2026-04-26: **US$119B**;
- 2026-07-26: **US$279B**.

The FY27 Q2 10-Q states that the latest commitments are primarily associated with memory and manufacturing facilities required for data-center infrastructure systems.

The figure cannot identify how much goes to any individual supplier, but it is an observable proxy for future resource-reservation intensity.

When customer-level HBM bits, CoWoS allocation, and rack shipments are unavailable, forward commitments are more informative than synthetic fleet arithmetic built from an assumed rack price.

## 13. Scarce-capacity access remains layer-specific

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

### Table 8.2 — 2026 public-data quantification readiness by layer

| Physical layer | Publicly observable inputs today | Can Absolute Gap be closed? | More defensible 2026 output |
|---|---|---|---|
| Advanced logic | node / platform revenue mix, CapEx, supplier guidance, selected roadmaps | **No**: customer-level qualified wafer demand / allocation is missing | direction, access proxies, node mix; no synthetic wafer-share gap |
| HBM / DRAM | vendor supply guidance, same-bits wafer trade ratio, institutional bit forecasts | **Partly quantifiable, but no global gap closure**: customer-level bits / wafer allocation is missing | manufacturing intensity, tightness, product-mix shift |
| Advanced packaging | supplier guidance, tightness statements, selected institutional demand estimates | **No**: no unified qualified package-start denominator or customer allocation | lead time, qualification, allocation proxies |
| Networking | system specifications, public topology / deployment, vendor product data | **Partial**: no unified workload-level topology / utilization denominator | workload-specific bandwidth / latency / TCO |
| Power / LPS | project-level contracted / secured / permitted / construction / energized states | **Partly at project level; not globally** | Time-to-Power, state conversion, project delivery gap |
| Capital / Utilization | CapEx, supply commitments, financing structure, selected revenue disclosure | **Capital base is visible; real utilization is not broadly public** | capital-base growth versus utilization / monetization proxies |

**Source:** Report synthesis based on the degree to which public evidence can close each denominator.  
**Note:** “Not closed” is not an excuse for missing data. It identifies **which denominator is absent**. A layer should be upgraded to an auditable Absolute Gap only when demand and capacity are observable in the same physical unit, delivery window, and qualification boundary.

The quantitative rule is therefore:

> **Calculate what can be closed; use explicit proxies where closure is partial; do not fill a missing denominator with a point estimate.**

## 13A. 2026 public-data gap / intensity ledger

The readiness table above should not become a permanent excuse for leaving public evidence unstructured. Where a same-unit demand/capacity pair exists, the report should calculate it; where only an institutional balance or intensity signal exists, it should be recorded with its exact scope; where the denominator is missing, the output remains not measurable.

### Table 8.3 — 2026 public-data gap / intensity ledger

| Layer / metric | Public input at the cutoff | Bounded output | Status | Boundary |
|---|---|---|---|---|
| HBM manufacturing intensity | TrendForce estimates HBM wafer input **among the top three suppliers** at ~**22%** of total DRAM wafer input in 2026, while HBM bit supply is expected at ~**9%** of total DRAM bit supply[^7] | read jointly with Micron's same-node / same-bits **≈3×** physical trade ratio | **B-grade institutional intensity signal** | the two TrendForce percentages are not scope-identical enough to support a formal 22/9 intensity ratio; not an absolute HBM supply gap |
| Aggregate DRAM balance | TrendForce estimates a **~−1% to −2% 2026 DRAM sufficiency ratio**[^8] | institutional balance range indicates a modest aggregate deficit | **B-grade institutional forecast** | not HBM-specific; underlying demand/capacity volumes and customer allocation are not public |
| Advanced logic | node mix, CapEx, supplier guidance | no same-unit AI qualified-demand / qualified-capacity pair | **Not measurable as Absolute Gap** | revenue mix cannot be converted into wafer allocation |
| Advanced packaging | supplier tightness statements and partial capacity estimates | no unified qualified package-start demand/capacity pair in one auditable source | **Not measurable as formal Absolute Gap** | media / investor gap estimates remain C-grade unless methodology and denominator close |
| Networking | product topology and system specifications | workload-specific engineering ratios only | **Partial** | no unified deployment/utilization denominator |
| Power / LPS | project-level secured / permitted / construction / energized states | project delivery-state tracking only | **Partial at project level** | IT-GW, generation GW, PPA MW, energized load, and utilized load remain different quantities |

**Source:** TrendForce institutional estimates, read alongside Micron's first-party manufacturing-input anchor.[^4][^7][^8]  
**Denominator note:** TrendForce's two percentages should **not** be divided into a formal intensity ratio. The wafer-input statement is scoped to HBM wafer input **among the top three suppliers**, while the bit-supply statement is framed against total DRAM bit supply. The pair is **consistent with** higher HBM manufacturing intensity, but the scope mismatch prevents a formal ratio or exact cross-share inference. The clean comparable physical anchor remains Micron's approximately **3×** same-node / same-bits HBM3E-to-DDR5 disclosure.[^4]

This is the standard for future upgrades to the ledger:

> **Calculate only when the denominator closes; otherwise preserve the best bounded institutional signal and state what remains unmeasurable.**

The next quantitative upgrade should occur only when a layer gains a same-unit demand/capacity pair or an auditable institutional balance metric. Until then, the ledger records the missing denominator rather than manufacturing one.

---

### Table 8.4 — 2026 computable anchors versus unclosed denominators

| Observable | Auditable calculation / bounded read | Evidence identity | What it still cannot prove |
|---|---|---|---|
| DeepSeek-V3 formal training | 2.788M H800 GPU-hours × US$2 ≈ **US$5.576M** | D-grade arithmetic on a paper-stated rental assumption | total R&D / company / model-program cost |
| GB200 NVL72 rack intensity | at 120 kW/rack, 1 MW rack IT load ≈ **8.33 racks / 600 GPUs / 111.7 TB HBM3E** | D-grade mechanical conversion from official system specs | shipments, energized fleet size, industry demand |
| Micron HBM3E manufacturing trade ratio | same node / same bits requires approximately **3×** DDR5 wafer supply | A-grade first-party physical anchor | a permanent HBM4/HBM5 ratio or global wafer-allocation share |
| NVIDIA manufacturing / supply / capacity commitments | US$95.2B → US$279B = approximately **2.93×** the January level, or **+193%** mechanically | D-grade arithmetic on A-grade filing values | supplier-specific allocation, shipments, utilization, independent end-demand quality |
| Aggregate DRAM balance | 2026 sufficiency ratio approximately **−1% to −2%** | B-grade institutional forecast | HBM-specific shortage or customer allocation |

**Source:** DeepSeek, NVIDIA, Micron, and TrendForce.[^1][^3][^4][^6][^8]  
**Note:** The table deliberately mixes evidence grades only because the **identity of each row is explicit**. Mechanical arithmetic does not upgrade the underlying evidence. The purpose is to show that the framework produces auditable outputs where denominators close, while refusing to turn those outputs into broader claims they do not support.

This is the quantitative standard for the report: **a small number of closed calculations is more valuable than a large model built from incompatible denominators.**

---

## 14. Separate risk classes before testing for cascade

System risk in AI infrastructure can be divided into:

1. **Physical bottleneck:** logic / HBM / packaging / interconnect;
2. **Power bottleneck:** grid / substation / permit / cooling;
3. **Capital / utilization risk:** asset utilization fails to cover depreciation, power, operations, and financing;
4. **System-substitution risk:** cloud custom stacks / open software change platform economics;
5. **Regulatory / geopolitical risk:** export controls, supply interruption, interface remedies, regional fragmentation.

One risk does not equal an industry-wide crisis. The more dangerous state is when several clocks begin to reinforce one another.

## 15. Rolling Bottleneck Cascade is a state-transition model

AI-infrastructure bottlenecks rotate rather than remaining permanently fixed at one layer.

A positive expansion cascade can look like:

> HBM / packaging tight → hardware delivery constrained → supply expands → more racks reach sites → power / interconnection becomes binding → utilization becomes the next constraint

A reverse capital cascade can look like:

> power delay → utilization decline → buyer ROI decline → next CapEx slows → hardware orders slow → HBM / packaging tightness eases → upstream CapEx slows

This is the **Rolling Bottleneck Cascade**.

It explains why easing HBM does not prove that AI infrastructure has no constraints, and why power becoming a bottleneck does not mean semiconductor constraints have disappeared permanently.

## 16. Capital returns have to reconcile different asset clocks

A minimal economic relationship is:

> **Economic Return = Revenue from deployed compute − Depreciation − Power − Operations − Financing**

The core risk is duration mismatch: hardware can turn over rapidly while data-center shells, grid assets, PPAs, and debt remain in place for much longer.

A technically functional system can therefore produce weak capital returns if utilization is low or long-duration obligations are excessive.

## 17. False-precision guardrails

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

## 18. Preferred quantitative workflow

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
[^7]: TrendForce, 2026-06-02, HBM wafer-input and bit-supply shares for 2025–2027, https://www.trendforce.com/presscenter/news/20260602-13074.html
[^8]: TrendForce, 2026-07-30, 2026 DRAM sufficiency ratio estimate of approximately -1% to -2%, https://www.trendforce.com/presscenter/news/20260730-13158.html
