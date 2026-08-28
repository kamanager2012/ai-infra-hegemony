# Volume 03: AI Resource Gravity and Non-AI Residual Capacity

Chinese source edition: [vol-03.md](../vol-03.md)

> Retrieval and revision cutoff: **2026-08-27**. AI expansion does not absorb all semiconductor capacity. The relevant variable is the residual capacity left for non-AI demand inside the specific scarce layers that AI systems also consume.

## 1. Where the “AI siphon” actually occurs

AI-infrastructure expansion does not pull all semiconductor capacity away from every other industry at the same time.

The main change occurs in a subset of scarce layers.

This report defines **AI Resource Gravity** as the tendency for capital and manufacturing capacity to move toward AI-related products when those buyers can offer:

- higher value per unit of scarce resource;
- longer-duration orders;
- prepayments;
- stronger demand growth;
- greater utilization visibility.

The most exposed layers include:

- advanced logic;
- HBM;
- RDIMM and server DRAM;
- advanced packaging;
- high-speed networking;
- power-management components;
- data-center power.

The more useful analytical variable is therefore **Non-AI Residual Capacity**: the effective capacity left for non-AI products after higher-priority demand has absorbed the relevant increment.

## 2. Rack-scale systems turn demand into physical identities

The official GB200 NVL72 configuration includes:

- **72 Blackwell GPUs**;
- **36 Grace CPUs**;
- **13.4 TB HBM3E**;
- **17 TB LPDDR5X**.

For a scenario with (R) racks:

```text
HBM = 13.4 TB × R
LPDDR = 17 TB × R
```

| Scenario rack count | HBM3E | LPDDR5X |
|---:|---:|---:|
| 1,000 | 13.4 PB | 17 PB |
| 10,000 | 134 PB | 170 PB |
| 30,000 | 402 PB | 510 PB |
| 50,000 | 670 PB | 850 PB |

These are **scenario identities**, not shipment estimates.

NVIDIA does not disclose a full-year NVL72 rack-shipment number, so Data Center revenue should not be divided by an assumed rack ASP to manufacture a shipment series.

The value of the BOM is that it converts a rack scenario into a reproducible material-demand scenario without pretending the scenario is observed volume.

## 3. HBM can pressure DRAM supply more than bit share alone suggests

Micron disclosed that, at the same technology node and for the same number of bits, HBM3E requires roughly **3× the wafer supply of DDR5**.

TrendForce estimates that **HBM + RDIMM account for approximately 51% of 2026 DRAM bits**.

These two metrics are not interchangeable.

Together, however, they show why the manufacturing pressure created by HBM can exceed what bit share alone implies.

A plausible crowding-out mechanism is:

**higher AI/server demand  
→ more capital and wafer input allocated to HBM/RDIMM  
→ lower residual conventional-DRAM capacity  
→ greater pricing or configuration pressure in PCs, consumer devices, and general servers**

This is an example of **Observed Crowding-out** at the memory layer.

## 4. Advanced packaging is a separate physical constraint

Blackwell-class systems depend not only on leading-edge logic but also on advanced packaging.

The report uses a **D-grade geometry stress test**:

```text
72 GPU packages
÷ 13.4 packages per wafer
≈ 5.39 CoWoS wafers per rack
```

The inputs have different evidence status:

- 72 packages: derived from the official rack configuration;
- 13.4 packages per wafer: geometry working assumption;
- 5.39 wafers per rack: scenario stress-test result.

The 5.39 figure is **not** a TSMC-disclosed yield and is **not** front-end logic-wafer consumption.

It must not be divided into TSMC's roughly 15M annual wafer shipments to infer global rack capacity.

Those annual shipments include smartphones, automotive, IoT, mature-node products, and many other physical pools.

## 5. Which markets experience residual pressure first?

### 5.1 PCs and gaming

Consumer GPUs and Data Center accelerators share parts of the advanced manufacturing and memory system.

NVIDIA has previously disclosed Gaming supply constraints.

That makes PC/gaming one of the earlier consumer markets in which allocation pressure can become visible.

### 5.2 General-purpose servers

General servers may not use HBM, but they consume DDR5 RDIMM.

Because RDIMM itself is part of the server-driven memory pool, traditional servers do not sit on a completely independent “safe DRAM river.”

They can absorb memory pressure even without using frontier accelerators.

### 5.3 Smartphones

Smartphones remain TSMC's second-largest platform.

TSMC's smartphone platform represented **29% of 2025 revenue**; separately, smartphone-platform revenue grew **11% year over year**. The 29% figure is revenue mix, while +11% is platform-revenue growth. Source: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/bb5dd5e3537d7661e694fa2588e7a29f7c0410e6/4Q25%20Presentation%20%28E%29.pdf .

AI has therefore not displaced smartphones.

The structural change is that HPC is growing faster and is absorbing more of the incremental advanced-investment and packaging attention.

### 5.4 Automotive

Automotive has longer qualification cycles and extensive mature-node usage.

It does not overlap with frontier AI at every layer.

The main shared exposures are more selective:

- power management;
- advanced compute;
- memory;
- selected packaging capacity.

Automotive is therefore more exposed to **selective component pressure** than to an industry-wide frontier-node shortage.

## 6. Resource allocation is not proportional to industry size

AI Resource Gravity does not mean that AI must be the largest end market by unit volume.

It means that AI orders can compete more strongly for a scarce unit of supply.

Allocation can depend on combinations of:

- price;
- long-duration commitments;
- prepayments;
- customer credit;
- utilization;
- roadmap certainty;
- supplier diversification;
- geopolitics.

Consumer electronics can therefore lose part of an increment not because it is strategically “unimportant,” but because its products support different prices, contract durations, and prepayment structures.

## 7. China's parallel supply should not be added mechanically to the global frontier pool

China has a comparatively complete parallel supply base in smartphones and parts of consumer computing.

Frontier AI requires several advanced layers simultaneously:

- advanced logic;
- HBM-class memory;
- advanced packaging;
- high-speed interconnect;
- a mature software stack.

Growth in Chinese consumer-electronics supply therefore does not automatically offset the global frontier-AI bottleneck.

If China develops sufficient scale across those advanced layers, it can instead become a **second resource-gravity center** with its own allocation dynamics.

That is different from being merely the recipient of residual global capacity.

## 8. Current judgment

As of **August 2026**, the evidence supports several conclusions:

- AI/HPC is a major driver of incremental advanced-semiconductor demand;
- HBM and RDIMM are reshaping the DRAM supply mix;
- advanced packaging remains tight;
- consumer markets remain large, but selected categories face residual-capacity pressure;
- the pressure is **layered and selective**, not a universal claim that “AI has taken all chips.”

The key forward variable is **Non-AI Residual Capacity**.

The important question is whether residual capacity continues to fall within memory and packaging, and whether the pressure later spreads into a broader set of traditional end markets.

## Key public sources for this volume

- TrendForce — 2026 HBM + RDIMM = 51% of DRAM bit supply: https://www.trendforce.com/presscenter/news/20260825-13198.html
- Micron FY24 Q3 prepared remarks — HBM3E ≈ 3× DDR5 wafer supply: https://investors.micron.com/static-files/4550f98c-1054-4847-a929-c17d520a0564
