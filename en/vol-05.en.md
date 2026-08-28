# Volume 05: HBM, the Memory War, and AI Supply-Chain Restructuring

Chinese source edition: [vol-05.md](../vol-05.md)

> Retrieval and revision cutoff: **2026-08-27**. HBM is analyzed here as a system-level resource. The report separates first-party wafer-supply tradeoffs, institutional bit-share estimates, and scenario rack demand.

## 1. HBM has moved from component to system bottleneck

In frontier AI systems, HBM is not merely memory attached to a GPU.

It directly affects:

- model scale;
- batch size;
- context length;
- concurrency;
- system utilization.

The official GB200 NVL72 configuration contains **13.4 TB of HBM3E per rack**.

Once the commercial unit moves toward rack-scale systems, memory demand also moves upward—from “GB per accelerator” to “PB per data center.”

HBM therefore influences several layers simultaneously:

- accelerator-system performance;
- memory-vendor product mix;
- DRAM wafer allocation;
- advanced packaging;
- residual conventional-DRAM supply.

## 2. Micron's ~3× disclosure is the first-party physical anchor

Micron disclosed in its FY24 Q3 prepared remarks that, industry-wide, HBM3E requires roughly **3× the wafer supply of DDR5** to produce the same number of bits at the same technology node.

Micron's FY25 10-K later confirmed the direction: HBM requires more wafers and cleanroom space for the same bit output.

The evidence boundary is clear:

- **~3× = A-grade first-party company evidence**;
- it describes an HBM3E-versus-DDR5 wafer-supply trade ratio;
- it is not a permanent manufacturing constant for every fab;
- it should not be mechanically extended to every future HBM generation.

Micron has also indicated that the trade ratio is expected to rise for HBM4, which would increase the pressure HBM places on DRAM manufacturing input if realized.

## 3. SK hynix: HBM has already changed memory-vendor economics

SK hynix reported for FY25:

- revenue: **KRW 97.1467T**;
- operating profit: **KRW 47.2063T**;
- operating margin: **49%**;
- net income: **KRW 42.9479T**;
- HBM revenue: more than doubled year over year.

Public source: https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/

These figures show that HBM demand is changing not only product mix but also the profitability structure of the memory industry.

At the same time, SK hynix continued to describe strong demand for conventional server memory.

HBM and DDR5/RDIMM are therefore not two fully independent supply chains.

They compete within a manufacturing system that shares capital, cleanroom space, and some wafer input.

## 4. Samsung, SK hynix, and Micron form a concentrated HBM supply structure

High-end global HBM supply is concentrated among:

- SK hynix;
- Samsung;
- Micron.

Competition spans several technical layers:

- TSV;
- stacking;
- advanced-packaging cooperation;
- logic-base integration;
- HBM qualification.

Public first-party evidence is not sufficient to build one perfectly comparable company-by-company global HBM market-share table.

The stronger industrial conclusion is narrower:

> **HBM supply remains concentrated among a very small number of memory manufacturers capable of combining advanced DRAM manufacturing with stacked-memory integration.**

That concentration makes qualification, yield, and capacity expansion strategically important.

## 5. What the 51% DRAM-bit estimate means

TrendForce estimates that **HBM + RDIMM account for approximately 51% of 2026 DRAM bits**.

This does not mean 51% of DRAM is HBM.

It means AI/server-related memory represents a very large share of bit demand.

Because HBM itself requires more wafer input per delivered bit than comparable DDR5 under Micron's disclosed comparison, the supply effect can propagate through the memory system:

**higher HBM demand  
→ more wafer supply and cleanroom allocated to high-value products  
→ lower residual conventional-DRAM capacity  
→ higher probability of DDR5/LPDDR tightness or price pressure**

This is the memory-specific form of **Non-AI Residual Capacity**.

## 6. Rack-scale demand shows the order of magnitude

GB200 NVL72 contains:

```text
13.4 TB HBM3E per rack
```

Scenario demand is therefore:

| Scenario rack count | HBM3E demand |
|---:|---:|
| 1,000 | 13.4 PB |
| 10,000 | 134 PB |
| 30,000 | 402 PB |
| 50,000 | 670 PB |

These figures are stress tests, not observed shipments.

NVIDIA does not disclose a full-year rack-shipment total, and SK hynix, Samsung, and Micron do not disclose customer-level annual HBM bits that can be mapped directly to those rack scenarios.

The table therefore measures physical demand intensity, not realized consumption.

## 7. Moving some inference to DDR5 does not fully escape the memory constraint

A common argument is that training requires HBM while inference can return to commodity DDR5 and bypass the HBM bottleneck.

That can be true for some workloads.

It should not be generalized to all frontier inference because demand can still be shaped by:

- KV-cache bandwidth;
- large-batch inference;
- long context;
- mixture-of-experts routing;
- low-latency serving;
- multi-accelerator communication.

More importantly, DDR5/RDIMM already sits inside the same broader server-driven memory pool.

Moving a workload from HBM to DDR5 may reduce unit memory cost and bandwidth requirements.

It does not necessarily create an independent supply river unaffected by AI/server demand.

## 8. Boundary of China's memory supply

China's domestic DRAM and NAND capabilities are expanding, but the product layers must remain separate.

CXMT's public offering materials disclose DDR and LPDDR products but do not disclose an HBM product line.

That evidence supports only the statement:

> **the public filing does not disclose an HBM product line.**

It does not prove the absence of all HBM R&D.

YMTC operates in NAND and cannot be used as a direct substitute for HBM or DRAM constraints.

China's ability to buffer consumer-computing memory supply is therefore different from its ability to close the HBM-class memory layer of a frontier AI system.

## 9. Current judgment

As of **August 2026**, the memory industry shows three structural changes:

1. HBM has become a high-margin, capital-intensive core product;
2. AI/server memory represents a large share of DRAM bit demand;
3. HBM's wafer-supply trade ratio amplifies pressure on residual conventional-DRAM capacity.

The most important forward indicators include:

- HBM bit growth;
- the HBM4 trade ratio;
- CapEx allocation at SK hynix, Samsung, and Micron;
- conventional-DRAM pricing and supply;
- HBM configurations in cloud custom silicon;
- HBM packaging capacity;
- whether China demonstrates HBM-class products at verifiable scale.

HBM has moved from “high-end memory next to the GPU” into a core resource layer of AI-infrastructure competition.
