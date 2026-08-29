# Part I · Chapter 3: AI Resource Gravity and Non-AI Residual Capacity

## 1. Core judgment: AI changes marginal resource priority before it “takes all capacity”

AI infrastructure affects the supply chain unevenly. The resources most exposed to reprioritization are those shared with frontier AI and relatively inelastic in the short run:

- advanced logic;
- HBM / selected DRAM;
- advanced packaging;
- high-end substrates / networking;
- selected power-management components;
- data-center power.

This report defines the pull that high-value AI/server demand exerts on capital and effective supply as **AI Resource Gravity**.

It does not mean “AI takes all semiconductors.” It means:

> **When the risk-adjusted return, order duration, payment certainty, and expected utilization of AI/server workloads exceed those of other demand pools, incremental capital and constrained supply tend to move toward that demand.**

---

## 2. The economics of Resource Gravity

Resource reallocation can be described as:

> **high-value AI/server demand → higher expected return → product-mix / capacity-allocation shift → lower residual capacity for lower-priority demand**

The mechanism requires several conditions:

- capacity cannot expand quickly in the short run;
- different end markets share a physical or capital pool;
- AI/server customers can offer longer orders, prepayments, or greater purchasing certainty;
- suppliers expect higher risk-adjusted returns from the higher-value demand.

AI Resource Gravity is therefore not simply “a higher price.” It is a repricing of the **opportunity cost of the next unit of scarce resource**.

---

## 3. Price is not the only clearing mechanism: Quantity Assurance matters too

During severe shortages, markets do not clear through spot price alone.

Long-term agreements, customer credit, prepayments, purchasing scale, and allocation fulfillment affect how much volume a buyer actually receives.

TrendForce stated in January 2026 that after U.S. CSPs locked in part of available capacity, other buyers had to accept higher prices to secure supply allocation. In March 2026, it also reported that PC OEMs and module makers with lower allocation-fulfillment rates had to obtain incremental supply at higher prices.[^1][^2]

Therefore:

> **willingness-to-pay ≠ guaranteed quantity**

Resource pressure must be separated into two variables:

1. **Price Pressure:** how much a buyer must pay for the same quantity;
2. **Quantity Assurance:** whether the buyer can obtain enough volume on schedule even if it accepts the price.

For traditional end markets, the second variable can matter more than short-term spot pricing.

---

## 4. Non-AI Residual Capacity: traditional end markets face residual supply, not global gross supply

Effective supply available to traditional markets can be represented as:

```text
NonAI_Residual(t)
= Effective_Supply(t)
- AI_Server_Absorption(t)
- Other_Priority_Demand(t)
```

This resolves a common analytical error:

> **Growth in total supply does not imply equal growth in supply available to traditional end markets.**

If total effective supply expands but AI/server absorption expands faster, Non-AI Residual Capacity can still decline.

Evaluating whether smartphones, PCs, general servers, automotive, or industrial markets are returning to looser conditions therefore requires more than tracking:

- global wafer capacity;
- global DRAM bit growth;
- global packaging capacity;
- global power-project pipelines.

The relevant question is **how much effective residual supply those end markets can obtain within the same quality, qualification, generation, and delivery window**.

---

## 5. Two-Speed Semiconductor Economy: AI also changes where the next capital dollar goes

The long-run effect of AI Resource Gravity extends beyond current allocation into the next round of capital formation.

The AI Infrastructure Economy and Traditional Device Economy share parts of the same advanced-logic, memory, packaging, and power-management resource base, but they differ in:

- willingness to pay;
- contract duration;
- prepayment structure;
- utilization visibility;
- BOM sensitivity;
- end-market price elasticity.

Suppliers are therefore deciding not only “who receives more capacity today,” but also:

> **which product class offers the higher risk-adjusted return on the next dollar of CapEx.**

This report calls that structure the **Two-Speed Semiconductor Economy**.

It is not a claim that consumer electronics are permanently sacrificed. It means **AI/HPC is gaining greater influence over marginal semiconductor capital formation**.

---

## 6. Memory is currently the clearest observed path

Micron disclosed that, under **same technology node / same number of bits** conditions, HBM3E requires approximately **3× the wafer supply of DDR5**.[^3]

TrendForce forecasts HBM + RDIMM at approximately **51% of 2026 DRAM bit supply**.[^4]

Together, these two anchors show:

> **The manufacturing-resource intensity of high-value AI/server memory can exceed what bit share alone implies.**

The memory-layer transmission mechanism is therefore:

> HBM / server-memory demand rises → wafer / cleanroom / capital tilts toward higher-value products → conventional DDR/LPDDR residual supply changes → price / configuration / quantity-assurance pressure reaches traditional end markets

The boundaries remain important:

- 3× is a same-node / same-bits wafer-supply trade ratio;
- 51% includes HBM + RDIMM;
- 51% is a 2026E forecast;
- neither figure can be rewritten as HBM wafer share.

---

## 7. Advanced logic and packaging share demand pressure but are not one physical pool

TSMC's 2025 smartphone platform represented **29%** of annual net revenue, while HPC represented **58%**.[^5]

That establishes HPC as the largest revenue platform, but these are revenue-mix measures—not customer-level wafer allocation.

Leading-edge logic and advanced packaging must also remain separate:

- logic wafer availability does not guarantee a complete system can be delivered;
- packaging tightness does not imply equal customer allocation;
- customer revenue share cannot be converted into wafer share or CoWoS share.

AI Resource Gravity therefore cannot be summarized by one synthetic “AI share of global capacity.” It is a set of allocation shifts across different layers with different physical units.

---

## 8. Why pressure differs across traditional industries

Transmission into traditional markets depends on three conditions.

### Shared-resource exposure

The more an end market shares physical inputs with AI, the higher its exposure.

### Supply elasticity

The harder the resource is to expand quickly, the stronger the short-run pressure.

### Buyer power

Buyers with LTAs, purchasing scale, inventory, strong balance sheets, and end-market pricing power can absorb or delay the shock more effectively.

These end systems should not be placed into one universal “AI took the chips” funnel.

**Table 3.1 — Layered exposure of non-AI / Physical-AI end systems**

| End system | Main shared or adjacent upstream layers | Main transmission path | What can be inferred | What must not be inferred |
|---|---|---|---|---|
| Smartphone / PC | selected leading-edge SoC/GPU, LPDDR/DRAM, NAND, selected packaging | BOM, configuration, upgrade tax, replacement cycle, quantity assurance | opportunity cost of shared resources can rise | industry disappearance; a named customer losing a known wafer quantity |
| Game console | custom SoC/APU, GDDR/DRAM, NAND/SSD, selected packaging/test | BOM, promotion, hardware margin, long-generation cost-down, quantity assurance | memory procurement can affect hardware volume, promotion, and profit cadence | direct HBM competition; known wafers taken by AI; next generation must be delayed or repriced |
| Router / broadband | consumer DRAM/NAND, low bargaining power | higher price + weaker allocation | weaker buyers can face price and quantity pressure together | all end markets rise by the same multiple |
| Automotive / industrial / production lines | mature memory, MCU/analog, power, selected ADAS compute, packaging/test | lead time, qualification, EOL/part number, supply continuity | long qualification and long lifecycles reduce rapid substitution; adjacent product-mix shifts can matter | automotive electronics are directly “consumed” by GPU/HBM demand |
| Robotics / Physical AI | industrial control + sensors/actuation + edge accelerator + cloud retraining | industrial-electronics and edge-AI constraints can stack | robots can be exposed to both industrial and AI-compute pools | every robot needs frontier HBM; factories stop because AI took GPUs |
| Avionics / radar / space electronics | trusted/qualified logic, RF/power, rad-hard/rad-tolerant parts, special packaging/test | small-volume line economics, qualification, trusted access, long-lifecycle support | commercial high-volume markets can weaken small-volume special-demand bargaining power | aircraft, radar, or satellites are directly stopped by HBM shortage |
| Naval / other long-life defense systems | long-life qualified electronics, power/communications, trusted supply, maintenance spares | EOL, supplier longevity, small-volume economics | long-lived systems need sustained part-number and trusted-supply continuity | naval platforms “need NVIDIA capacity” |

**Source:** Chapter 21 smartphone / PC / game-console / consumer / industrial transmission evidence; NXP / ST automotive-longevity disclosures; U.S. GAO / DMEA trusted-microelectronics evidence; NASA/JPL space-radiation assurance materials.[^6][^7][^8][^9][^10]  
**Note:** The AI-era transmission strength differs substantially across the later rows. For defense / aerospace / space, the public evidence primarily establishes the structural weakness of low-volume, special, long-life, trusted supply in a commercial market; it does **not** establish AI/HPC as the direct cause of a specific program's cost or delay.

The key boundary is:

> **Resource Gravity is selective. The closer an end system is to shared advanced logic / memory / packaging, the more direct the transmission. The more it depends on trusted, long-life, RF/power, rad-hard, or special-process capacity, the more likely the channel runs through capital, equipment, engineering capacity, and supplier economics.**

Detailed transmission into pricing, configuration, replacement cycles, and observed examples belongs in [Chapter 21](part-III-ch21-consumer-transmission.md).

---

## 9. Resource Gravity is not an infinite one-way process

Resource reallocation contains a self-correcting mechanism.

If AI/HBM demand absorbs enough supply to drive up conventional DRAM, other logic-product, or traditional-component pricing, the per-unit resource economics of non-AI products improve.

That can produce:

> **AI allocation rises → non-AI residual supply tightens → non-AI price / margin rises → supplier rebalancing incentive strengthens**

Likewise, if AI workload monetization weakens, utilization falls, or supply elasticity improves rapidly, AI Resource Gravity can weaken.

It is therefore not a permanent law that “AI always drains every resource.” It is a **dynamic capital-allocation mechanism**.

---

## 10. How to tell whether Resource Gravity is strengthening or weakening

Signals of **strengthening** include:

- larger AI/server forward commitments;
- HBM / advanced-packaging tightness persisting across generations;
- supplier product mix continuing to tilt toward high-value AI/server products;
- declining Non-AI Residual Capacity;
- widening gaps in quantity assurance;
- incremental CapEx becoming more explicitly centered on AI/HPC.

Signals of **weakening** include:

- materially higher supply elasticity;
- stronger traditional-product economics inducing supplier rebalancing;
- sustained reductions in HBM / packaging lead times;
- improved allocation fulfillment;
- weaker AI utilization / monetization;
- forward commitments being reduced or delayed.

---

## 11. Current judgment

As of August 2026, public evidence is more consistent with:

> **AI Resource Gravity materially affecting selected shared scarce layers and changing the resource environment for traditional end markets through Non-AI Residual Capacity and quantity assurance.**

The process remains selective and dynamic, and it is subject to price feedback, supply expansion, and substitution.

The most accurate formulation is therefore not “AI is taking every chip.” It is:

> **AI is raising the opportunity cost of selected critical resources and changing how suppliers rank incremental capacity, product mix, and priority customers.**

## References

[^1]: TrendForce, 2026-01-05, CSP capacity locking and allocation pricing, https://www.trendforce.com/presscenter/news/20260105-12860.html
[^2]: TrendForce, 2026-03-31, allocation fulfillment and higher-price procurement by OEMs/module makers, https://www.trendforce.com/presscenter/news/20260331-12995.html
[^3]: Micron Technology, FY24 Q2 Prepared Remarks, 2024-03-20, HBM3E wafer-supply trade ratio versus DDR5, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^4]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^5]: TSMC, 4Q25 Presentation / 2025 full-year platform mix, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf


[^6]: NXP Semiconductors, S32G Vehicle Network Processors, minimum 15-year product support under the Product Longevity program, https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32g-vehicle-network-processors%3AS32G-PROCESSORS
[^7]: STMicroelectronics, 2025-09-08, selected SPC58 automotive MCUs extended to 20-year availability, https://newsroom.st.com/media-center/press-item.html/n4718.html
[^8]: U.S. GAO, 2015, Trusted Defense Microelectronics: Future Access and Capabilities Are Uncertain, low-volume unique defense needs and limited influence on commercial markets, https://www.gao.gov/products/gao-16-185t
[^9]: U.S. DMEA Trusted Access Program Office, Trusted Foundry / Trusted Supplier Program, guaranteed access for typically low-volume U.S. Government needs, https://www.acq.osd.mil/asds/dmea/tapo/trusted-supplier-programs.html
[^10]: NASA/JPL, Space Radiation Effects on Integrated Circuits, special design/fabrication and radiation-hardening requirements, https://parts.jpl.nasa.gov/asic/Appendix.3.html
