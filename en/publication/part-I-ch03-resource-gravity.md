# Part I · Chapter 3: AI Resource Gravity and Non-AI Residual Capacity

## 1. "AI absorption" does not mean every semiconductor capacity pool is being drained

AI infrastructure affects the supply chain unevenly. The resources most exposed to reprioritization are those shared with frontier AI and relatively inelastic in the short run:

- advanced logic;
- HBM / RDIMM / selected DRAM;
- advanced packaging;
- high-end substrates / networking;
- power-management components;
- data-center power.

This report defines the pull that high-value demand exerts on capital and capacity as **AI Resource Gravity**.

## 2. The economics of Resource Gravity

If one demand pool offers higher willingness to pay, longer contracts, greater utilization certainty, and stronger credit quality, suppliers have an economic incentive to direct more incremental capital and capacity toward it.

The transmission chain is:

> high-value AI/server demand → higher expected return → product-mix / capacity-allocation shift → lower residual capacity for lower-priority demand

This does not mean suppliers serve only the top buyer, nor that traditional markets stop receiving supply. It describes a change in the priority of **incremental** resources.

### 2.1 Price is not the only clearing mechanism: Allocation Assurance matters more than spot price

In an extreme shortage, the market does not clear through price alone. **Long-term agreements, customer credit, prepayments, purchasing scale, and allocation fulfillment** can determine first whether a buyer receives enough volume.

TrendForce stated in January 2026 that as U.S. CSPs locked in capacity, other customers had to accept higher prices to secure supply allocations. In March 2026, it further noted that PC OEMs and module makers with lower allocation-fulfillment rates were forced to procure incremental supply at higher prices.

Therefore:

> **willingness-to-pay ≠ guaranteed quantity**

The systemic risk is not only how much prices rise. It is whether residual capacity falls far enough that secondary buyers cannot obtain sufficient, timely, and sustainable supply even after accepting higher prices.

This mechanism is more auditable than the absolute claim that one buyer has captured "100% of capacity."

## 3. Why Non-AI Residual Capacity matters more than gross capacity

The effective supply available to traditional markets can be represented as:

> **Non-AI Residual Capacity = total effective supply − AI/server absorption − other priority demand**

If total supply rises 20% while AI/server demand absorbs 40% more, effective residual capacity for non-AI markets can still decline.

"Global capacity is increasing" therefore does not automatically imply that PCs, smartphones, general servers, or consumer GPUs are returning to abundant supply.

## 4. Memory is the clearest observed crowding-out path

Micron disclosed that HBM3E requires approximately **3× the wafer supply of DDR5** on the same technology node and for the same number of bits. TrendForce forecasts HBM + RDIMM at roughly **51% of 2026 DRAM bit supply**.

That creates an observable memory-layer mechanism:

> HBM/RDIMM demand rises → wafer/cleanroom/capital shifts toward higher-value server products → conventional DDR/LPDDR residual supply changes → consumer/general-compute price and configuration pressure increases

The 51% figure is a 2026E bit-supply forecast. It is not an HBM-only share and not a wafer share.

## 5. PCs and Gaming: dual exposure to GPU allocation and memory residuals

NVIDIA's FY26 10-K reports Gaming revenue of roughly **US$16.0B, up 41% year over year**, while also stating that supply constraints were expected to be a headwind to Gaming in FY27 Q1 and beyond.

That is evidence of supply constraints on the gaming side, but it does not prove that every constraint was caused by Data Center allocation.

PCs also face a second channel: server/HBM demand changes DRAM product mix and therefore the residual supply of DDR5/LPDDR. PC economics can therefore be exposed simultaneously to GPU availability and memory pricing.

## 6. General servers: RDIMM sits inside the same high-value memory pool

General servers do not necessarily use HBM, but they consume large amounts of DDR5 RDIMM. TrendForce includes RDIMM and HBM together in its forward view of 2026 DRAM bit supply, showing that traditional server memory is not a fully independent commodity river.

AI/server infrastructure expansion can therefore raise general-server cost through memory allocation even when the server itself does not use a frontier accelerator.

## 7. Smartphones: not displaced by AI, but competing under a new incremental-resource regime

TSMC's 2025 smartphone platform accounted for **29%** of annual net revenue and grew **11% year over year**; HPC accounted for **58%** and grew faster.

This does not support the statement that "AI replaced smartphones." A more accurate description is:

- smartphone remains a very large demand platform;
- HPC has greater pull on incremental leading-edge investment;
- LPDDR / selected packaging / power-management resources can share upstream inputs with AI/server demand;
- flagship input cost and mid-range node-migration cadence become more exposed to residual-capacity pressure.

## 8. Automotive: slower and more selective exposure

Automotive semiconductors have long qualification cycles, high reliability requirements, and extensive mature-node usage. They do not compete directly with frontier AI across every layer.

The strongest overlap is more likely to appear in central compute, memory, power management, and selected advanced packaging. Automotive is therefore better described as a **second-stage selective transmission channel** rather than part of the first broad shortage wave.

## 9. Residual pressure usually appears first as an upgrade tax, not a production stop

When effective residual capacity falls, common corporate responses include:

1. raising prices;
2. reducing specifications;
3. delaying upgrades;
4. extending the use of mature nodes or alternative suppliers.

Supply-chain pressure is therefore more likely to appear first as higher flagship BOM cost, longer replacement cycles, slower diffusion of high-end features, and sharper product segmentation—not immediate shutdown of an entire industry.

## 10. China's parallel supply can change domestic residual structure without closing the frontier bottleneck

China's expansion in logic, DRAM, NAND, and terminal manufacturing can relieve part of the pressure in domestic consumer markets.

But substitution must still be analyzed by layer: consumer computing is relatively strong; general compute has partial alternatives; frontier AI still depends on advanced logic, HBM-class memory, advanced packaging, interconnect, and software closure.

Domestic consumer-supply growth can therefore improve local residual capacity without automatically removing the upstream bottlenecks of global frontier AI.

## 11. Real-economy firms face a second layer of AI adoption cost

Manufacturing and other operating companies adopting AI face not only hardware/input costs but also cloud inference, software integration, data pipelines, security/compliance, and workflow redesign.

The relevant productivity equation is:

> **Net productivity value = productivity gain − total AI adoption cost**

Upstream resource inflation and downstream AI-service cost can therefore affect the same company at the same time.

## 12. Current judgment and falsification

As of August 2026, the evidence is more consistent with:

> **selective transmission + product segmentation + Non-AI Residual Capacity pressure**

than with the claim that "AI is taking every chip."

The crowding-out thesis should be weakened if DDR/LPDDR pricing and supply become sustainably loose, consumer-GPU availability improves materially, smartphone/general-server upgrades no longer show shared-resource pressure, and memory/packaging product mix stops tilting toward AI/server demand.

## Key public sources

- NVIDIA FY26 10-K — Gaming +41% and supply-constraint headwind: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
- Micron FY24 Q2 Prepared Remarks — HBM3E ≈3× DDR5 wafer supply: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- TrendForce — 2026E HBM + RDIMM = 51% of DRAM bit supply: https://www.trendforce.com/presscenter/news/20260825-13198.html
- TSMC 4Q25 Presentation — smartphone 29%, HPC 58%: https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
- TrendForce 2026-01-05 — CSPs lock capacity, other buyers accept higher prices to secure allocation: https://www.trendforce.com/presscenter/news/20260105-12860.html
- TrendForce 2026-03-31 — lower allocation fulfillment forces OEMs to procure at higher prices: https://www.trendforce.com/presscenter/news/20260331-12995.html
