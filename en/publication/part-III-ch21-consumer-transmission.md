# Part III · Chapter 21: How AI Reprices Consumer Electronics and Other End Systems

## 1. Transmission, not displacement

AI does not need to consume the same chips as a smartphone, router, console, vehicle, or industrial controller in order to change that end system's economics.

The relevant question is **where the two demand pools overlap, directly or indirectly**.

Direct overlap is strongest in advanced logic, DRAM / LPDDR, selected packaging, workstation/consumer GPU resources, storage, and some power-management components. Indirect exposure is more important in long-life, trusted, RF/power, rad-hard, or other special-process systems, where capital allocation, equipment continuity, engineering capacity, qualification, and supplier economics matter more than direct competition for an AI accelerator.

The transmission chain is:

> **AI/server product mix rises → allocation priority changes in shared or adjacent resource pools → Non-AI Residual Capacity and Quantity Assurance change → price / configuration / volume adjust → Product-Mix Polarization → Vendor Operating-Model Adaptation**

This chapter therefore tests **transmission and attribution**. It does not assume that every component-price increase is caused by AI, nor does it require literal one-for-one competition for the same device.

## 2. Memory is the cleanest observed transmission layer

Micron first-party evidence states that at the same node and same number of bits, HBM3E requires approximately **3× the wafer supply of DDR5**.[^1]

TrendForce forecasts HBM + RDIMM at roughly **51% of 2026 DRAM bit supply**.[^2]

Consumer-DRAM pressure therefore cannot be judged from bit share alone.

If high-value memory also requires more manufacturing input per bit, it can reduce the effective residual supply available to conventional DRAM.

## 2A. Attribution test: price alone is not enough

Even when AI/server demand is changing memory and advanced-node allocation, smartphone and PC component prices are also affected by:

- supplier inventory policy;
- conventional demand recovery or weakness;
- wafer-start discipline;
- product transitions;
- FX;
- channel inventory;
- geopolitics / trade policy;
- supplier-specific yield and product mix.

The report therefore requires evidence of a **shared physical resource, product-mix reallocation, allocation change, or explicit supplier/institutional linkage** before attributing a traditional-market supply effect to AI.

A higher memory price by itself proves a price cycle, not a single-cause AI mechanism.

This is why later moderation in mobile-DRAM price growth is important counterevidence: resource pressure can be offset by inventory, end-market demand, supplier response, and price elasticity.

## 3. Smartphones: the first adjustment appears in BOM and configuration

TrendForce's February 11, 2026 example for 1Q26 showed estimated contract prices for mainstream **8GB + 256GB** smartphone memory approaching **+200% year over year**.[^3]

For 2Q26, TrendForce estimated:[^4]

- LPDDR4X solution ASP: **+70–75% QoQ**;
- LPDDR5X: **+78–83% QoQ**.

TrendForce's 2026-08-03 **3Q26 forecast** projected that the mobile-DRAM increase would narrow materially to approximately **+8–13% QoQ**.[^5]

At the same time, TrendForce continued to state that suppliers were shifting capacity toward server / HBM applications.

A more accurate interpretation is therefore:

> **structural residual pressure remains, but the rate of price increase does not accelerate forever.**

## 4. Smartphones are segmenting, not disappearing

TSMC's 2025 smartphone platform represented **29%** of annual net revenue and grew **11% year over year**.[^6]

AI/HPC growth therefore does not imply that smartphone demand disappeared.

Counterpoint's H1 2026 data provides a more direct view of the pressure:[^7]

- global smartphone SoC shipments: **-15% YoY**;
- MediaTek and Qualcomm shipments: both **down more than 25% YoY**;
- Q2 2026 smartphone memory prices: **up about 300% YoY**;
- GenAI smartphone SoC shipments: **+24% YoY**;
- UNISOC gained market share in the period; Counterpoint links part of its H1 2026 growth to entry-level models migrating to UNISOC 4G platforms to reduce BOM cost, while also noting progress in 5G adoption.[^7]

The result is **segmentation and restructuring rather than uniform collapse**: entry/mid-range devices are more exposed to memory/BOM pressure, premium/GenAI devices are relatively more resilient, and lower-cost SoC paths can gain share.

The real change is that HPC has stronger pull on incremental advanced resources and memory economics tilts more toward server/HBM, making flagship BOM, memory configuration, and mid-range node strategy more exposed to upstream constraints.

## 4A. Three product clocks: premium reprices and shrinks, mid-range stretches, entry exits

Describing this as a uniform industry-wide freeze would still be too coarse. End-device vendors are operating on three different product clocks.

IDC's August 26, 2026 smartphone outlook forecasts:[^30]

- 2026 global smartphone shipments down **16.7% YoY**, to just above **1 billion units**;
- average selling price rising to **US$581**, up **27.6% YoY**;
- total market value still increasing **6.3%** to roughly **US$613B**;
- the sub-US$100 smartphone segment, which still shipped about **173 million units** in 2025, facing severe viability pressure as low-end Android vendors reduce low-price models and move product mix upward.

The key implication is that **unit contraction and revenue resilience can coexist**. The industry does not need to decline uniformly; vendors can sacrifice volume while defending mix, ASP, and margin.

The more defensible three-layer structure is:

- **Premium:** absorbs cost through higher ASP, financing, brand premium, and stronger supply leverage; technical progress continues, but volume need not expand.
- **Mid-range:** has the hardest time preserving price band, memory/storage configuration, and the annual performance narrative at the same time; platform life extends and replacement cycles lengthen.
- **Entry:** when BOM inflation breaks the price ceiling, the outcome may be fewer SKUs, lower-cost platforms, refurbished/used substitution, or exit from the price band rather than a proportional price increase.

Gartner's February 2026 outlook points in the same direction: it expects PC lifetimes by year-end 2026 to extend by roughly **15% for business buyers** and **20% for consumers**, and forecasts that the **sub-US$500 entry-level PC segment will disappear by 2028**.[^32] This remains a **B-grade institutional forecast**, not an observed terminal state.

The correct interpretation is therefore not that all end-system specifications freeze together, but that:

> **premium devices can keep advancing at higher prices and smaller volumes; mid-range devices absorb the constraint through slower upgrades and longer lives; entry tiers carry the highest exit risk.**

## 4B. Routers / broadband: bargaining power changes the transmission severity

Counterpoint Research reported in February 2026 that consumer DRAM/NAND prices had risen by more than **600%** year over year—roughly the same order of magnitude described in its headline as a **sevenfold** surge for broadband-device memory. Memory's share of the BOM in low-to-mid-range routers increased from roughly **3%** to **more than 20%**.[^16]

This is important because it shows that:

> **the severity of resource crowding-out is strongly related to bargaining power and supply assurance.**

Large buyers can use LTAs, scale, and stronger balance sheets to absorb part of the shock. Smaller OEMs are more exposed to the combination of higher prices and lower allocations.


## 5. Cross-market reordering: allocation logic is changing

TrendForce stated in April 2026 that AI demand had created bottlenecks in **3 nm–2 nm wafers and 2.5D/3D advanced packaging**, and that NVIDIA had moved early to secure large volumes of **4/3 nm wafer capacity, CoWoS, HBM, T-glass, substrates, PCBs, and SSDs**.[^8]

Its June foundry research said TSMC **3 nm capacity remained severely constrained**.[^9] TrendForce also stated that foundries were dedicating a larger share of wafer capacity to AI-related products, materially changing the supply-demand balance for mature nodes as well.[^10]

This is a case of **cross-market resource reordering**: higher expected returns and stronger demand certainty in AI can cause incremental resources that previously served multiple end markets to be reprioritized toward AI/server applications.

This is not a claim that capacity used to be distributed evenly or that NVIDIA now receives everything.

What the evidence supports is:

- advanced-node / packaging / memory / power-device allocation logic is changing;
- traditional end markets face lower Non-AI Residual Capacity;
- allocation assurance and bargaining power matter more;
- lower-margin, lower-bargaining-power, shorter-duration buyers are more exposed to higher prices and lower quantities.

The evidence does **not** disclose how many wafers Apple, Qualcomm, AMD, or Intel individually lost, and it does not support a "100% capacity capture" claim.

## 6. PCs: memory and system pricing can reinforce each other

NVIDIA's FY26 10-K reported Gaming revenue up **41%** and said supply constraints were expected to remain a Gaming headwind into FY27 Q1 and beyond.[^11]

By FY27 Q1, the company's Edge Computing discussion also noted slower consumer-PC demand, partly because of **elevated memory and systems prices**.[^12]

Two channels can therefore overlap:

- consumer GPU / system availability;
- DDR / LPDDR / system-memory cost.

IDC's June 2026 PC outlook forecasts global PC shipments down **11.3% YoY** in 2026 while PC ASP rises **17%**, and says it does not expect meaningful relief from the memory shortage before the end of 2027.[^31] This is still a forecast, not a guaranteed future path, but it reinforces the same operating problem: vendors must manage higher system cost, weaker unit demand, and a harder-to-sustain full product portfolio at the same time.

## 6A. Vendor Operating-Model Adaptation: vendors cannot simply wait for users to delay replacement

Consumers can postpone a purchase. Device vendors still carry annual product planning, channel inventory, tooling and R&D amortization, minimum procurement scale, retail commitments, and market-share targets. The same shortage that appears as “I will upgrade later” to the user can force a **break in the vendor's previous operating model**.

The following is a **report-side operating-model heuristic**, not a sourced historical time series for the entire consumer-electronics industry. The mainstream consumer-electronics model has often relied on a combination of:

- advanced-node capability diffusing down the stack;
- declining memory/storage cost over long periods;
- mid-range volume absorbing fixed R&D, tooling, and channel cost;
- entry products covering price bands and share;
- flagship products carrying brand, ASP, and technical narrative.

When memory, advanced logic, and adjacent manufacturing resources are repriced or reprioritized, those conditions cannot all be preserved. Vendor responses narrow to five broad choices:

1. **Raise price:** defend margin, accept lower volume and weaker low-end share.
2. **Reduce or freeze specification:** preserve a price band, weaken the annual upgrade case.
3. **Cut SKUs and extend lifecycle:** open fewer new designs and amortize platforms longer.
4. **Shift the product narrative:** move from compute/memory toward camera, display, battery, form factor, software, and services.
5. **Exit selected price bands, regions, or product lines:** shrink the portfolio when low-margin SKUs no longer cover BOM and channel economics.

Sony already provides a strong first-party example: its FY26 PS5 hardware planning explicitly links memory procurement at reasonable prices to unit sales, promotional plans, and hardware profitability.[^27] IDC and Gartner forecasts for smartphones and PCs show the same broader combination of **higher ASP + lower units + premiumization + longer replacement cycles**.[^30][^31][^32]

The vendor problem is therefore not whether consumers can tolerate slower upgrades, but:

> **How does a company built around annual hardware improvement and scale expansion continue to cover fixed cost, channels, and product cadence after scarce upstream resources are repriced under a different return structure?**

### 6A.1 Scale still matters, but it no longer guarantees marginal allocation priority

The report does not assume that lower consumer volume automatically causes lower future allocation. Purchase scale, LTAs, prepayment, multi-sourcing, and supplier relationships still improve Quantity Assurance.

But historical unit scale also cannot be treated as an automatic claim on the next unit of scarce capacity. A narrower mechanism is:

> **When another buyer can offer higher willingness to pay, longer commitments, stronger prepayment, or higher supplier returns for the same or adjacent resource, the allocation value of traditional end-market scale can weaken at the margin.**

This creates a feedback loop worth monitoring rather than assuming:

> **Residual Capacity Compression → Price / Specification Adjustment → Longer Replacement Cycles → Lower Unit Volume → possible weakening of marginal allocation position → further Product-Mix Adjustment**

Public evidence already supports the first half of this chain. Whether lower unit volume systematically weakens future allocation is still an **M — Mechanism / H — Hypothesis** that requires cross-cycle contract, allocation, wafer-start, and supplier-mix evidence.

## 6B. Game consoles: long generations make residual pressure persistent

Game consoles are a useful test case for Non-AI Residual Capacity because they do not directly compete with AI servers for the same accelerator, yet they remain materially exposed to **memory, storage, custom SoC/APU, and selected manufacturing / packaging resources**.

Current console specifications establish that boundary:

- PlayStation 5 uses a custom AMD Zen 2 / RDNA-based processor, **16 GB GDDR6**, and a custom SSD;[^24]
- Xbox Series X uses a custom Zen 2 / RDNA 2 processor, **16 GB GDDR6**, and **1–2 TB custom NVMe SSD**;[^25]
- Nintendo Switch 2 uses a **custom NVIDIA processor** and **256 GB UFS storage**, with microSD Express expansion.[^26]

These specifications do **not** imply that game consoles directly compete for HBM.

The more accurate relationship is:

> **console memory / storage / SoCs sit inside the same broader semiconductor and memory capital system as AI/server demand, while their specific product pools, packaging formats, and qualification paths remain different.**

### 6B.1 Hardware-economics pressure is directly observable

Sony stated in its FY2025 Q4 / FY2026 outlook that:

- cumulative PS5 unit sales exceeded **93 million units** by March 2026;
- FY26 PS5 hardware sales would be based on the volume of memory it could procure at **reasonable prices**;
- if conditions changed, it would manage profitability by adjusting **unit sales and promotional plans**.[^27]
- in the same earnings Q&A, Sony said it had **already secured the memory volumes necessary for FY26**, with pricing agreed to a certain extent.[^27]

Sony's FY2025 Form 20-F also identifies global memory-semiconductor price increases and supply shortages since the second half of FY2025 as a business risk, and notes that shortages or delayed shipments of critical or custom components can reduce or suspend production where supplier or production capacity is limited.[^29]

This is unusually strong first-party transmission evidence because it links:

> **memory procurement → hardware volume / promotion → hardware profitability**

The counterevidence matters: **Sony's disclosed FY26 state is not an unresolved PS5 quantity shortfall.** The transmission mechanism is currently expressed through procurement cost, pricing / promotion flexibility, and future supply conditions rather than evidence that FY26 required volume remains unsecured.

TrendForce's December 2025 institutional outlook for the 2026 console market additionally estimated:

- the 2026 global game-console shipment forecast was revised from **-3.5% YoY** to **-4.4% YoY**;
- for **Switch 2**, memory was estimated at roughly **21%–23% of hardware cost** in 2026;
- for **Sony and Microsoft consoles**, memory cost was estimated to rise to **more than 35% of BOM** in 2026;
- hardware gross margins and promotional flexibility would therefore be pressured.[^28]

This is a **B-grade institutional estimate**, not an audited Sony / Microsoft / Nintendo BOM.

Combined with Sony's first-party procurement statement, the evidence supports a narrower conclusion:

> **Game consoles are already an end-system case where memory residual pressure can affect shipment cadence, promotion capacity, and hardware margin.**

### 6B.2 Why one cost shock can affect an entire console generation

Game consoles usually combine:

- long hardware generations;
- relatively rigid price bands;
- highly customized SoC/APU designs;
- fixed memory / storage architectures;
- platform economics in which software, network services, and content monetize a large installed base over time.

Sony's 2026 disclosures reinforce that structure: cumulative PS5 unit sales exceeded 93 million, and Sony said the expanded installed base contributed to stable software and network-services profit, while hardware volume still must be balanced against memory procurement and total segment profitability.[^27]

The risk therefore extends beyond one quarter of higher memory prices.

If a new generation reaches architecture freeze / BOM freeze while memory, storage, or advanced-logic opportunity cost is elevated, the effect can persist through:

- launch configuration;
- SKU segmentation;
- promotion cadence;
- multi-year cost-down curves.

That is the console version of an **upgrade tax**:

> **the same price band buys a slower hardware-specification improvement, or the same target specification requires a higher BOM / weaker promotional subsidy.**

### 6B.3 Attribution boundary

The report does not infer:

- PlayStation / Xbox / Nintendo will be displaced by AI;
- game consoles are “short HBM”;
- NVIDIA / AI servers took a known number of wafers from a console maker;
- the 2026 console shipment slowdown is entirely caused by AI;
- the next console generation must be more expensive or delayed.

Console demand also depends on:

- generation timing;
- game/content pipeline;
- installed-base saturation;
- retail pricing;
- FX;
- consumer demand;
- product strategy.

The most defensible judgment is therefore:

> **Game consoles are not an obsolete side market in the AI era. They are long-generation, hardware-margin-sensitive platforms with meaningful memory/storage exposure; stronger AI/server memory demand forces a harder tradeoff among quantity assurance, BOM, promotion, and hardware cadence.**

---

## 7. Quantity Assurance and Price are distinct variables

In a severe shortage, end-product vendors face more than rising ASPs. They can also face insufficient allocation fulfillment.

TrendForce stated in March 2026 that PC OEMs / module makers with lower allocations had to procure incremental supply at higher prices.[^13]

The analysis therefore separates:

> **Price Pressure**

from

> **Quantity Assurance**

A willingness to pay more does not guarantee the quantity required by the production plan.

The ability to absorb the shock depends on:

- LTA coverage;
- purchase scale;
- balance-sheet strength;
- inventory;
- multi-sourcing;
- supplier relationships;
- end-market pricing power.

This is why the same memory shortage can affect a premium global brand and a smaller OEM very differently.

### 7A. Hardware constraints raise the value of software efficiency, but do not by themselves make software lean

Slower hardware improvement changes software optimization boundaries, but it does not imply that the software industry will universally become more efficient.

When 8 GB memory, constrained storage, or prior-generation GPUs remain in the mainstream installed base for longer, software vendors can respond in at least four ways:

1. **Local optimization:** lower memory footprint, package size, cold-start cost, and background activity.
2. **Feature tiering:** use lightweight modes, on-demand loading, modular features, or different quality presets by memory/compute tier.
3. **Cloud offload:** move models, indexing, rendering, or other heavy workloads to data centers; the endpoint becomes lighter while total system resource use does not necessarily fall.
4. **Support cutoff:** raise minimum requirements or end support earlier, transferring compatibility cost to the installed base.

Hardware constraint is therefore a **necessary pressure, not a sufficient condition** for software efficiency. Organizations still optimize across engineering cost, time to market, cloud cost, subscription revenue, and retention.

This is especially important for AI software: consumer endpoints may be forced to economize on local memory while model serving, KV cache, retrieval, agent loops, and evaluation expand data-center resource use. A second transmission mechanism can therefore emerge:

> **consumer hardware constraint → local convergence / cloud offload → higher dependence on remote compute → reinforcement of data-center demand**

This chain is best treated as an **M — Mechanism**, not as a closed reflexive demand loop. A lighter local application does not imply lower total system resource intensity.

For core claims, contract / allocation evidence, institutional contract-price research, vendor filings, and company commentary should take priority over channel anecdotes.

---

## 8. Automotive / industrial: qualification turns price pressure into continuity risk

Automotive and industrial systems have longer qualification cycles, but that does not insulate them from AI-era product-mix reallocation.

TrendForce stated in June 2026 that major memory suppliers were prioritizing HBM and advanced-layer 3D NAND, squeezing mature NOR Flash and SLC NAND capacity; cumulative 1H26 contract-price increases for both categories exceeded 100%.[^14] In July, TrendForce raised its 2H26 SLC NAND forecast to **+120–170% versus 1H26**, with automotive, industrial, and networking buyers among the affected customers.[^15]

What can be supported is **structural shortage and price inflation in specific mature-memory categories**.

This report does not upgrade that evidence into unverified whole-vehicle claims such as "all automotive memory +180%," "RMB7,000–10,000 added memory cost per vehicle," or "annual supply fulfillment below 50%."

Automotive electronics also carry **qualification and product-longevity rigidity**. NXP gives S32G vehicle network processors a minimum **15-year** support commitment, while STMicroelectronics extended selected SPC58 automotive MCUs to **20-year availability**, with some part families supported into 2038–2041.[^19][^20]

These first-party disclosures establish a different kind of constraint:

> **For automotive electronics, the problem is not only today's component price; it is whether a qualified part remains supportable across a platform lifecycle.**

MCUs, analog components, power semiconductors, and most automotive electronics do not directly compete for the same physical pool as AI servers. But supplier CapEx, packaging/test capacity, engineering priority, and long-life product economics can still be influenced by higher-return markets. Without project-level evidence, this report does not rewrite that adjacent pressure as “AI caused a specific vehicle shortage.”

### 8.1 Production lines: lead time, redesign, and downtime are the relevant channels

PLC, servo control, industrial PCs, sensors, MCU/analog/power components, and industrial memory often share four properties:

- long qualification / validation cycles;
- embedded-software and hardware-BOM coupling;
- component substitution requires revalidation;
- installed equipment may need many years of maintenance and spare-part support.

The likely transmission is therefore:

> **longer lead time → redesign / requalification cost → spare-part / maintenance risk**

rather than “the factory cannot buy a training GPU.”

The attribution rule from Section 2A still applies. A price increase or lead-time extension in one industrial component is not enough to prove AI causation. Stronger attribution requires shared-resource exposure, supplier product-mix shift, capacity/engineering reallocation, or explicit supplier/institutional evidence.

### 8.2 Aerospace / defense: low-volume continuity is the relevant exposure

These systems have a different exposure profile from smartphones and PCs.

A **2015 U.S. GAO assessment** documented the structural mismatch between high-volume commercial microelectronics markets and low-volume, unique defense requirements with limited influence on commercial allocation.[^21] It is used here as historical structural evidence, not as a 2026 market snapshot. The current DMEA Trusted Foundry / Trusted Supplier framework independently shows that preserving trusted access for typically low-volume government needs remains an active institutional requirement.[^22]

NASA/JPL materials on space electronics add another boundary: radiation environments can require special IC design, fabrication, screening, and assurance.[^23]

The defensible AI-era mechanism is therefore limited to:

> **As commercial semiconductor capital, equipment, and engineering capacity optimize around higher-volume and higher-return markets, maintaining low-volume, high-reliability, long-life, trusted, or special-process supply can become more difficult or expensive.**

Public evidence does **not** support stronger claims such as:

- aerospace or space programs being delayed because HBM is sold out;
- radar or naval electronics directly competing for the same AI accelerator pool;
- a specific percentage cost increase or supply-fulfillment loss caused by AI.

Those would require program-level, supplier-level, or government-procurement evidence.


## 9. Local substitution can relieve pressure without proving frontier closure

China's growing capability in DDR, LPDDR, NAND, smartphone manufacturing, and terminal supply chains can improve local consumer residual capacity.

But consumer DRAM / NAND capability cannot be extrapolated automatically into HBM-class frontier-memory supply.

Domestic substitution can therefore change smartphone / PC cost structures without eliminating the frontier AI bottlenecks in HBM and advanced packaging.

## 10. Storage: HDD and SSD remain workload-specific complements and substitutes

AI data-center storage is becoming a segmented market.

TrendForce observed both severe nearline-HDD shortages and faster substitution toward high-capacity QLC nearline SSDs.[^17] At the same time, Seagate's FY26 results explicitly linked AI-driven data growth to stronger mass-capacity storage demand.[^18]

A more accurate structure is:

- latency / inference-sensitive workloads raise the attractiveness of SSD / QLC nearline SSD;
- cold and mass-capacity storage continues to create real HDD demand;
- HDD supply and HAMR ramp can themselves become storage bottlenecks.

AI data centers therefore do not make HDD strategically irrelevant by default.

## 11. Real-economy firms also face AI adoption cost

Manufacturers and other operating businesses also pay for:

- cloud inference;
- software integration;
- data pipelines;
- security / compliance;
- workflow redesign;
- human review.

The relevant equation is therefore:

> **Net Productivity Value = Productivity Gain − Upstream Input Pressure − Total AI Adoption Cost**

This is why cheaper AI models do not automatically produce higher ROI for operating companies.

## 12. Current read

As of August 2026, the evidence supports:

> **AI infrastructure has transmitted part of its cost pressure into consumer electronics, automotive/industrial systems, and other end systems through memory, shared leading-edge resources, allocation priority, and system pricing; the further an end system sits from those shared advanced layers, the more the transmission must be validated through supply continuity, product mix, and supplier economics.**

The defensible long-run conclusion is neither “AI eliminates consumer electronics” nor “all consumer hardware freezes uniformly.”

> **AI is raising the opportunity cost of selected upstream resources and translating that pressure into three different product clocks: premium reprices and shrinks while still advancing, mid-range stretches and slows, and entry tiers carry the highest exit risk.**

At the vendor level, the mechanism can be summarized as:

> **Residual Capacity Compression → Product-Mix Polarization → Vendor Operating-Model Adaptation**

Price increases, specification cuts, SKU reduction, longer platform life, narrative shifts, and price-band exits already have observed or institutional support. Whether lower unit volume then weakens future marginal allocation remains a mechanism to be tested.

At the software layer, hardware constraint raises the value of local efficiency, but cloud offload, feature tiering, and support cutoffs provide alternative escape routes. The report therefore does not assume a universal return to “lean software.”

The final boundary is:

> **As of 2026, the evidence supports erosion of the cheap mass-market upgrade model in consumer computing; it does not yet establish structural terminal decline across the smartphone, PC, and gaming ecosystems.**

## References

[^1]: Micron Technology, FY24 Q2 Prepared Remarks, HBM3E ≈3× DDR5 wafer supply at same node / same bits, https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
[^2]: TrendForce, 2026-08-25, 2026E HBM + RDIMM share of DRAM bit supply, https://www.trendforce.com/presscenter/news/20260825-13198.html
[^3]: TrendForce, 2026-02-11, 1Q26 mainstream smartphone memory contract cost, https://www.trendforce.com/presscenter/news/20260211-12922.html
[^4]: TrendForce, 2026-05-14, 2Q26 LPDDR4X and LPDDR5X ASP changes, https://www.trendforce.com/presscenter/news/20260514-13044.html
[^5]: TrendForce, 2026-08-03, 3Q26 mobile DRAM price outlook, https://www.trendforce.com/research/download/RP260803NC
[^6]: TSMC, 4Q25 Presentation / 2025 full-year platform mix, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
[^7]: Counterpoint Research, 2026-07-28, H1 2026 smartphone SoC shipment and memory-price trends, https://counterpointresearch.com/en/insights/global-smartphone-soc-shipments-fall-15percent-yoy-in-h12026
[^8]: TrendForce, 2026-04-30, AI supply-chain arms race and advanced-node / packaging bottlenecks, https://www.trendforce.com/presscenter/news/20260430-13028.html
[^9]: TrendForce, 2026-06-08, TSMC 3 nm capacity remains severely constrained, https://www.trendforce.com/research/download/RP260608SX3
[^10]: TrendForce, 2026-06-30, foundry capacity reallocation toward AI-related products, https://www.trendforce.com/presscenter/news/20260630-13127.html
[^11]: NVIDIA Corporation, FY26 Form 10-K, Gaming revenue and supply-constraint disclosure, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
[^12]: NVIDIA, FY27 Q1 CFO commentary, consumer PC demand tempered by elevated memory and systems prices, https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27cfocommentary.htm
[^13]: TrendForce, 2026-03-31, allocation fulfillment and higher-price procurement, https://www.trendforce.com/presscenter/news/20260331-12995.html
[^14]: TrendForce, 2026-06-16, NOR Flash / SLC NAND mature-capacity squeeze, https://www.trendforce.com/presscenter/news/20260616-13102.html
[^15]: TrendForce, 2026-07-13, SLC NAND 2H26 price forecast, https://www.trendforce.com/presscenter/news/20260713-13142.html
[^16]: Counterpoint Research, 2026-02-11, broadband memory-price surge and router BOM impact, https://counterpointresearch.com/en/insights/7times-memory-price-surge-threatens-telcos-broadband-router-set-topbox-supply
[^17]: TrendForce, 2025-09-15, nearline HDD shortage and QLC SSD substitution, https://www.trendforce.com/presscenter/news/20250915-12714.html
[^18]: Seagate Technology, FY26 results, AI/cloud data generation and mass-capacity storage demand, https://investors.seagate.com/news/news-details/2026/Seagate-Technology-Reports-Fiscal-Fourth-Quarter-and-Fiscal-Year-2026-Financial-Results/default.aspx


[^19]: NXP Semiconductors, S32G Vehicle Network Processors, minimum 15-year product support under the Product Longevity program, https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32g-vehicle-network-processors%3AS32G-PROCESSORS
[^20]: STMicroelectronics, 2025-09-08, selected SPC58 automotive MCUs extended to 20-year availability, https://newsroom.st.com/media-center/press-item.html/n4718.html
[^21]: U.S. GAO, 2015, Trusted Defense Microelectronics: Future Access and Capabilities Are Uncertain, https://www.gao.gov/products/gao-16-185t
[^22]: U.S. DMEA Trusted Access Program Office, Trusted Foundry / Trusted Supplier Program, https://www.acq.osd.mil/asds/dmea/tapo/trusted-supplier-programs.html
[^23]: NASA/JPL, Space Radiation Effects on Integrated Circuits, https://parts.jpl.nasa.gov/asic/Appendix.3.html


[^24]: PlayStation, PS5 official specifications, custom AMD Zen 2 / RDNA-based processor, 16 GB GDDR6 and custom SSD, https://www.playstation.com/content/dam/global_pdc/en-gb/corporate/support/manuals/ps5-docs/2100ab/CFI-21XX_PS5_Instruction_Manual_Web%24en-gb.pdf
[^25]: Xbox, Xbox Series X official technical specifications, custom Zen 2 / RDNA 2 processor, 16 GB GDDR6 and 1–2 TB custom NVMe SSD, https://www.xbox.com/en-US/consoles/xbox-series-x
[^26]: Nintendo, Nintendo Switch 2 official technical specifications, custom NVIDIA processor and 256 GB UFS storage, https://www.nintendo.com/us/gaming-systems/switch-2/tech-specs/
[^27]: Sony Group, FY2025 Q4 earnings speech / FY2026 outlook, PS5 hardware sales based on memory volume procurable at reasonable prices and flexible unit-sales / promotion management, https://www.sony.com/en/SonyInfo/IR/library/presen/er/pdf/25q4_sonyspeech.pdf ; FY2025 Q4 earnings Q&A, FY26 memory volume already secured and pricing agreed to a certain extent, https://www.sony.com/en/SonyInfo/IR/library/presen/er/pdf/25q4_qa.pdf
[^28]: TrendForce, 2025-12-02, Memory Price Surge Squeezes Game Console Margins; 2026 Shipment Forecast Revised Downward, https://www.trendforce.com/presscenter/news/20251202-12811.html


[^29]: Sony Group, FY2025 Form 20-F, global memory-semiconductor price increases / shortages and component-capacity risk, https://www.sony.com/en/SonyInfo/IR/library/FY2025_20F_PDF.pdf
[^30]: IDC, 2026-08-26, Smartphone Shipments Set for Record 16.7% Drop in 2026, as the Memory Crisis Hits Full Force, https://www.idc.com/resource-center/blog/smartphone-shipments-set-for-record-16-7-drop-in-2026-as-the-memory-crisis-hits-full-force/
[^31]: IDC, 2026-06-02, PC Market Enters Volatile Territory as Memory Shortage Persists Through 2027, https://www.idc.com/resource-center/blog/pc-market-enters-volatile-territory-as-memory-shortage-persists-through-2027/
[^32]: Gartner, 2026-02-26, Gartner Says Surging Memory Costs Will Reduce Global PC and Smartphone Shipments in 2026, https://www.gartner.com/en/newsroom/press-releases/2026-02-26-gartner-says-surging-memory-costs-will-reduce-global-pc-and-smartphone-shipments-in-2026
