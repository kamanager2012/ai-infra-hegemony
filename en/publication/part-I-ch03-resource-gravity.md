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

TrendForce stated in January 2026 that as U.S. CSPs locked in capacity, other customers had to accept higher prices to secure supply allocations. In March 2026, it further noted that PC OEMs and module makers with lower allocation-fulfillment rates were forced to procure incremental supply at higher prices.[^1][^2]

Therefore:

> **willingness-to-pay ≠ guaranteed quantity**

The systemic risk is not only how much prices rise. It is whether residual capacity falls far enough that secondary buyers cannot obtain sufficient, timely, and sustainable supply even after accepting higher prices.

This mechanism is more auditable than the absolute claim that one buyer has captured "100% of capacity."

## 3. Why Non-AI Residual Capacity matters more than gross capacity

The effective supply available to traditional markets can be represented as:

> **Non-AI Residual Capacity = total effective supply − AI/server absorption − other priority demand**

If total supply rises 20% while AI/server demand absorbs 40% more, effective residual capacity for non-AI markets can still decline.

"Global capacity is increasing" therefore does not automatically imply that PCs, smartphones, general servers, or consumer GPUs are returning to abundant supply.

### 3.1 Two-Speed Semiconductor Economy: shared resources, different capital-formation speeds

The AI Infrastructure Economy and the Traditional Device Economy share parts of the same advanced-logic, memory, packaging, and power-management resource base, but they differ materially in willingness to pay, contract duration, use of prepayments, BOM constraints, and end-market price elasticity.

The long-run consequence of AI Resource Gravity is therefore not limited to current-period allocation. It also affects the next round of capital formation: suppliers decide where the next dollar of CapEx goes based on risk-adjusted returns. The **Two-Speed Semiconductor Economy** describes this difference in resource economics; it is not a factual declaration that consumer electronics are being permanently “sacrificed.”

### 3.2 AI Capacity Gap: separate the absolute gap from the growth gap

To determine whether a physical layer is **actually short of deliverable supply today**, the report defines an absolute gap:

```text
AI_Capacity_Gap_i(t)
= AI_Effective_Demand_i(t)
- AI_Effective_Capacity_i(t)
```

where \(i\) represents physical layers such as advanced logic, HBM/DRAM, advanced packaging, networking, and power. Demand and capacity must use the **same delivery window, qualification/quality boundary, and physical unit**, such as wafers/month, qualified package starts/month, bits/year, or MW.

- **Absolute Gap > 0:** current deliverable supply is insufficient;
- **Absolute Gap ≈ 0:** current supply and demand are near balance;
- **Absolute Gap < 0:** current effective headroom exists.

To determine whether scarcity pressure is widening or converging, the report separately defines:

```text
AI_Capacity_Growth_Gap_i(t)
= Growth(AI_Effective_Demand_i(t))
- Growth(AI_Effective_Capacity_i(t))
```

The Growth Gap is a difference in growth rates over the same period, measured in percentage points. It describes the **direction of pressure**, not the current stock gap:

- **Growth Gap > 0:** scarcity may widen, or existing headroom may be eroded;
- **Growth Gap < 0:** scarcity may converge, or effective headroom may expand;
- **Growth Gap = 0:** supply and demand are changing at the same rate; it does not imply that no shortage exists.

A strong S4 Capital Hard Landing signal therefore requires **Absolute Gap < 0 / excess capacity** together with deterioration in utilization, clearing prices, and forward commitments—not a negative Growth Gap by itself.

AI Capacity Gap, AI Capacity Growth Gap, and Non-AI Residual Capacity answer different questions: the first two measure the current AI-side shortfall and its direction of change; NARC measures effective supply left for non-AI demand after priority allocation.

## 4. Memory is the clearest observed crowding-out path

Micron disclosed that HBM3E requires approximately **3× the wafer supply of DDR5** on the same technology node and for the same number of bits; TrendForce forecasts HBM + RDIMM at roughly **51% of 2026 DRAM bit supply**.[^3][^4]

That creates an observable memory-layer mechanism:

> HBM/RDIMM demand rises → wafer/cleanroom/capital shifts toward higher-value server products → conventional DDR/LPDDR residual supply changes → consumer/general-compute price and configuration pressure increases

The 51% figure is a 2026E bit-supply forecast. It is not an HBM-only share and not a wafer share.

## 5. PCs and Gaming: dual exposure to GPU allocation and memory residuals

NVIDIA's FY26 10-K reports Gaming revenue of roughly **US$16.0B, up 41% year over year**, while also stating that supply constraints were expected to be a headwind to Gaming in FY27 Q1 and beyond.[^5]

That is evidence of supply constraints on the gaming side, but it does not prove that every constraint was caused by Data Center allocation.

PCs also face a second channel: server/HBM demand changes DRAM product mix and therefore the residual supply of DDR5/LPDDR. PC economics can therefore be exposed simultaneously to GPU availability and memory pricing.

## 6. General servers: RDIMM sits inside the same high-value memory pool

General servers do not necessarily use HBM, but they consume large amounts of DDR5 RDIMM. TrendForce includes RDIMM and HBM together in its forward view of 2026 DRAM bit supply, showing that traditional server memory is not a fully independent commodity river.

AI/server infrastructure expansion can therefore raise general-server cost through memory allocation even when the server itself does not use a frontier accelerator.

## 7. Smartphones: not displaced by AI, but competing under a new incremental-resource regime

TSMC's 2025 smartphone platform accounted for **29%** of annual net revenue and grew **11% year over year**; HPC accounted for **58%**.[^6]

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

## References

[^1]: TrendForce, 2026-01-05, CSP capacity locking and allocation pricing, https://www.trendforce.com/presscenter/news/20260105-12860.html
[^2]: TrendForce, 2026-03-31, allocation fulfillment and higher-price procurement by OEMs/module makers, https://www.trendforce.com/presscenter/news/20260331-12995.html
[^3]: Micron Technology, FY24 Q2 Prepared Remarks, 2024-03-20, HBM3E wafer-supply trade ratio versus DDR5, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^4]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^5]: NVIDIA Corporation, FY26 Form 10-K, U.S. SEC, Gaming revenue and supply-constraint disclosure, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
[^6]: TSMC, 4Q25 Presentation / 2025 full-year platform mix, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
