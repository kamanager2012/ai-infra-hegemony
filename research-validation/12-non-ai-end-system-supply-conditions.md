# Phase II · Non-AI End-System Supply Conditions v0.4

> **Status:** Research-side downstream exposure map; not part of the frozen formal facts.  
> **Purpose:** make the report's intended reader explicit: AI does not make smartphones, PCs, game consoles, vehicles, factories, robotics, aerospace, or other long-lifecycle high-reliability systems “unimportant.” The question is whether their electronics are now buying into a supply system whose capital allocation, contracting and margin priorities are being reset by AI/HPC.

## 0. Response-evidence ownership contract v0.4

This file owns **observed non-AI end-system responses** to shared-resource conditions.

It may record:
- procurement / volume-assurance changes;
- BOM / margin response;
- lead-time / EOL / qualification effects;
- product cadence / promotion changes;
- substitution / cost-down counterevidence.

It does **not** own upstream scarcity state itself.

Upstream tightness must come from the relevant semiconductor / memory / packaging / supply evidence. This file asks only:

> **Did the end system actually change behavior because of that upstream condition?**

Hard anti-attribution rule:

> **Upstream AI/HPC tightness without an observed downstream response is exposure, not realized transmission.**

Formal Chapter 21 remains frozen unless a new response chain meets §9 and the report is explicitly reopened.

## 1. First-principles statement

The report's downstream thesis should not be:

> **AI matters more than every other industrial system.**

It should be:

> **important end systems do not receive semiconductor capacity because they are important; they receive it through specific foundry, memory, packaging, qualification, contracting and financing relationships. When AI/HPC demand changes the economics of those upstream layers, non-AI end systems can face higher opportunity cost, longer lead times, slower upgrades or weaker supply assurance even when their social or strategic importance is unchanged.**

The correct variable is therefore not “importance.”

It is:

> **shared-resource exposure × supplier economics × qualification rigidity × contract duration × supply assurance.**

## 2. Four exposure classes

### Class I — Direct competition for advanced shared layers

Examples:
- flagship smartphones;
- high-end PCs / workstations;
- selected automotive ADAS / domain controllers;
- edge AI systems;
- high-end robotics compute.

Potentially shared layers:
- selected leading-edge logic;
- LPDDR / DRAM / NAND;
- advanced packaging in some designs;
- high-end substrate / test / engineering capacity.

Evidence can support:
> AI/HPC can raise the opportunity cost of these shared layers.

Evidence cannot automatically support:
> AI physically removed a specific number of wafers from a named non-AI customer.

### Class II — Adjacent competition through supplier product mix

Examples:
- mainstream automotive electronics;
- industrial control;
- factory automation;
- power electronics;
- routers / broadband devices;
- robot actuator/control electronics.

These often rely heavily on:
- mature-node MCU / analog;
- NOR / SLC NAND;
- power semiconductors;
- sensors;
- long-lived qualified components.

The transmission mechanism is often indirect:

> supplier capital / equipment / engineering / memory product mix shifts toward higher-return AI/server products → mature or long-life lines receive less incremental attention → price, availability and redesign risk rise.

This is not the same as “the car competes for an H100.”

### Class III — High-reliability / defense / aerospace small-volume electronics

Examples:
- avionics;
- naval electronics;
- radar and electronic systems;
- satellites;
- launch vehicles;
- other high-reliability government systems.

These systems often require:
- trusted supply;
- radiation tolerance for space;
- long lifecycle;
- special qualification;
- low-volume production;
- dedicated packaging/test or screening;
- process continuity.

GAO has explicitly noted a structural mismatch: commercial microelectronics are optimized for high-volume, short-life-cycle markets, while U.S. defense requirements are often low-volume, unique and have little influence on the commercial market. DMEA maintains Trusted Foundry access specifically to guarantee advanced trusted services for typically low-volume government needs.

NASA/JPL likewise documents that space electronics often require special radiation-hardening design/fabrication and mission-specific reliability assurance.

The defensible AI-era mechanism is therefore:

> **commercial AI can worsen the economics of preserving small-volume, long-life, special-process supply even when those systems do not directly use HBM or frontier AI accelerators.**

Do **not** write:
- “ships cannot be built because NVIDIA took the chips”;
- “radar competes directly with HBM3E”;
- “satellites are blocked by AI wafers.”

### Class IV — Physical AI / robotics: hybrid exposure

Robots and automated production systems straddle two worlds:

**mechanical / industrial side**
- MCU;
- sensor;
- actuator;
- power electronics;
- motor control;
- industrial memory.

**AI / edge-compute side**
- edge accelerator;
- high-bandwidth memory in some higher-end systems;
- cloud simulation / training / fleet analytics.

They can therefore be exposed simultaneously to:
- industrial-electronics supply conditions;
- AI-edge compute allocation;
- cloud-side retraining demand.

This makes Physical AI the downstream category with the clearest future overlap between traditional industrial electronics and AI-system economics.

## 3. Why qualification rigidity matters

Automotive evidence makes the point directly.

NXP's S32G vehicle processors carry a **minimum 15-year product-support commitment** through its Product Longevity program.

STMicroelectronics extended selected SPC58 automotive MCUs to a **20-year availability commitment**, with some lines available into 2038–2041.

This means automotive customers optimize not only for unit price and peak performance, but for:

- qualification continuity;
- long-term supply;
- functional safety;
- redesign avoidance;
- platform lifetime.

Therefore:

> **a traditional customer can be economically important and still be less flexible than an AI buyer when a supplier reallocates capital or capacity.**

## 4. Why high-reliability systems are structurally different

DMEA's Trusted Foundry program exists to provide guaranteed access to advanced trusted microelectronics for **typically low-volume U.S. Government needs**, including prototype and production services.

GAO's defense-microelectronics work highlights:

- rising leading-edge manufacturing capital costs;
- commercial focus on high-volume markets;
- short commercial product life cycles;
- low-volume / unique defense requirements;
- weak defense influence on commercial market allocation.

NASA/JPL adds a different constraint:

- radiation environment can require special IC design and fabrication;
- mission electronics must retain function over mission life;
- qualification and radiation assurance are part of the supply problem.

The correct structural concern is:

> **small-volume strategic electronics can become more expensive to sustain when the commercial semiconductor system optimizes around higher-volume, higher-return AI and consumer/server demand.**

This is a supply-economics problem, not a claim that all strategic systems share one physical semiconductor pool.

## 5. End-system exposure matrix

| End system | Main upstream collision | Publicly visible signal | What can be inferred | What must not be inferred |
|---|---|---|---|---|
| Smartphone / PC | leading-edge SoC/GPU, LPDDR/DRAM/NAND, selected packaging | memory pricing, allocation, system prices, node mix | upgrade cost / configuration pressure can rise | smartphone/PC industry disappears |
| Game console | custom SoC/APU, GDDR/DRAM, NAND/SSD, selected packaging/test | memory procurement, hardware margin, promotion, long-generation cost-down | quantity assurance and BOM can alter hardware cadence | console directly competes for HBM; next generation must be delayed/repriced |
| Automotive | long-life MCU/analog/power + selected advanced ADAS compute + memory | product-longevity programs, BOM/memory pressure, long-term SiC supply agreements | redesign and supply-assurance cost matter | all automotive electronics directly competes with AI GPU capacity |
| Industrial / factory automation | mature-node control, sensors, power, industrial memory + some edge AI | mature-memory pricing, supplier longevity, industrial component lead time | product-mix reallocation can hit BOM/availability | factories stop because AI took advanced wafers |
| Robotics | industrial control + edge accelerator + cloud retraining | edge platform adoption, memory content, component availability | hybrid exposure to industrial and AI pools | every robot requires frontier HBM |
| Aviation / high-reliability electronics | trusted / qualified / long-life logic, analog, RF, power, packaging/test | trusted supplier access, product longevity, qualification capacity | small-volume supply economics can worsen | aviation directly competes for AI racks |
| Radar / defense electronics | trusted microelectronics, RF/power, special qualification, some advanced processing | DMEA/GAO trusted-supply indicators | low-volume strategic demand can lose commercial influence | radar shortage = HBM shortage |
| Satellite / launch electronics | rad-hard / rad-tolerant logic, memory, power, special test | NASA/JPL radiation assurance and parts-supply indicators | special-process continuity matters | space hardware is blocked by AI memory alone |
| Naval / long-life platforms | long-life qualified electronics, power, communications, maintenance spares | longevity / trusted-supply / obsolescence indicators | EOL and sustainment risk can rise | a naval platform “needs NVIDIA capacity” |

## 6. Allocation is not a moral ranking

One strategic message should be explicit:

> **Semiconductor allocation does not follow social importance.**

Suppliers respond to:
- gross margin;
- volume;
- contract visibility;
- prepayment;
- qualification cost;
- opportunity cost;
- capital intensity;
- strategic policy;
- customer credit.

Therefore a strategically important but low-volume customer can face worse economics than a commercial AI buyer with:
- longer commitments;
- higher willingness to pay;
- financing support;
- larger volume;
- faster capital payback.

This does not mean the supplier is making a political judgment that AI is “more important.”

It means the allocation mechanism is economic unless policy creates a different protected channel.

## 6A. 2025–2026 observed end-system transmission: three different outcomes

The framework now has three useful public anchors that show why end-system exposure must be monitored as a **state variable**, not assumed from upstream scarcity alone.

### Sony / PlayStation — quantity assurance reaches hardware planning

Sony's FY2025 Q4 / FY2026 outlook states that FY26 PS5 hardware sales will be based on memory volume procurable at reasonable prices, with unit sales and promotional plans adjusted if needed to manage profitability.

This supports a direct chain:

> **memory procurement → hardware volume / promotion → hardware profitability**

This is the strongest current console-side evidence that upstream memory conditions have crossed into an end-system operating decision.

### Microsoft / PC ecosystem — memory pricing reaches OEM inventory and device pricing

Microsoft's FY2026 disclosures provide a separate PC-side transmission path:

- FY26 Q2: Windows OEM benefited from elevated inventory as OEM partners purchased ahead of expected memory-price increases;
- FY26 Q3: OEM inventory continued to reflect increasing memory pricing;
- FY26 Q4 outlook for FY27: higher component costs were expected to increase device pricing and weigh on PC demand.

The defensible chain is:

> **memory / component pricing → OEM inventory behavior → device pricing → PC demand**

This is materially stronger than merely citing DRAM contract-price forecasts because an end-system platform operator is describing the downstream behavioral response.

### Nintendo / Switch 2 — a useful counterexample

Nintendo's November 2025 management Q&A acknowledged rising memory-module and other material costs but stated that, absent significant external changes, it did **not** then expect the recent cost increase to materially reduce Switch 2 hardware profitability because mass-production cost reductions could offset part of the pressure.

That creates an important counterexample:

> **component-cost pressure ≠ automatic margin compression**

The transmission depends on:
- inventory position;
- procurement timing;
- manufacturing learning / cost-down;
- pricing;
- product mix;
- promotional strategy.

This is exactly the kind of counterevidence the report needs to avoid turning Residual Capacity into a one-way story.

### Research implication

The three cases together imply:

| Case | Upstream signal | Downstream response | Interpretation |
|---|---|---|---|
| Sony PS5 | memory quantity / price constraint | hardware volume + promotion management | quantity assurance is binding enough to enter planning |
| Microsoft PC ecosystem | higher memory / component pricing | forward inventory + higher device pricing | cost pressure is transmitting into channel behavior and demand |
| Nintendo Switch 2 | rising material / memory costs | profitability expected to remain broadly maintained | cost-down can absorb part of the shock |

Therefore:

> **End-system residual pressure should be measured through observed response functions, not inferred from upstream tightness alone.**

The minimum response variables are:
- inventory behavior;
- configuration / SKU change;
- promotion;
- retail/device pricing;
- hardware margin;
- unit guidance;
- replacement / upgrade cadence.

---

## 6B. Automotive / industrial attribution gate — 2026 supplier-side counterevidence

The automotive / industrial chain remains **exposure-rich but response-poor**.

Current first-party semiconductor evidence does not support a simple claim that AI/HPC has already crowded automotive / industrial customers out of supply.

### NXP — end-market recovery rather than obvious shortage transmission

NXP Q2 2026 reported:

- Automotive revenue **US$1.938B**, +12% YoY and +9% sequentially;
- Industrial & IoT revenue **US$755M**, +38% YoY and +20% sequentially;
- channel inventory at **11 weeks**, unchanged from Q1 and above 9 weeks in Q2 2025.

This is supplier-side evidence of healthy / recovering non-AI demand.

It does **not** prove that every automotive or industrial customer has abundant supply.

But it is contrary evidence against:

> **AI demand has already produced a broad automotive / industrial semiconductor shortage.**

### Infineon — AI growth and automotive recovery can coexist

Infineon's 2026 disclosures show two things at the same time:

- AI data-center power solutions are a major / leading growth driver;
- Automotive order intake is improving.

Infineon's €5B Dresden Smart Power Fab is explicitly positioned to serve applications spanning:
- AI data-center power;
- automotive;
- industrial / grid / renewable applications;

and the company says capacity ramp can be accelerated when market opportunities require it.

This matters because the resource-reordering mechanism is not one-way.

A shared or adjacent supplier can respond to high-return AI demand through:

> **capacity expansion / faster ramp**

rather than only:

> **reallocation away from automotive / industrial.**

Therefore the downstream model must retain supply elasticity.

### STMicroelectronics — tightness exists, but attribution remains unresolved

ST's Q2 2026 first-party release reports:

- higher demand and strong bookings across end markets;
- improved visibility;
- signs of tight supply in several product categories;
- distribution inventory below its standard target;
- strong AI-data-center demand as an important forward growth driver.

This is useful because it shows that:

> **tight supply and AI growth can coexist inside a diversified semiconductor supplier.**

But it still does not establish:

> **the tight product categories are tight because AI displaced automotive / industrial supply.**

That causal step requires product / capacity / customer linkage.

### 6B.1 New automotive / industrial response rule

For automotive / industrial, upgrade from **Exposure** to **Realized Transmission** only when at least one downstream actor discloses a behavioral response such as:

- production / unit guidance changed because qualified semiconductor supply was unavailable;
- component price / availability forced BOM or vehicle / equipment pricing changes;
- qualification of a second source was accelerated because incumbent supply assurance deteriorated;
- redesign / EOL / line-transfer cost rose;
- lead time affected customer delivery;
- inventory was built specifically to protect against semiconductor / memory supply risk.

Supplier-side tightness alone is insufficient.

### 6B.2 Counterevidence must be recorded symmetrically

The response ledger must also record:

- supplier capacity expansion;
- order / revenue recovery in automotive / industrial;
- inventory normalization;
- improved lead time;
- successful second sourcing;
- cost-down;
- product redesign that absorbs pressure.

Therefore:

> **AI/HPC resource reordering is a mechanism to test, not a universal attribution label.**

Current 2026 automotive / industrial research-side state:

> **shared-resource exposure = credible; broad realized AI-attributed downstream pressure = not established.**

No formal Chapter 21 expansion is justified by these supplier observations alone.

---

## 7. The other side of the cycle: resource return can also hurt

If AI workload economics fail to support the installed capital base, the same end systems can face a different problem:

> **resource reflow after clearing.**

Potential effects:
- memory and accelerator prices fall;
- specialized AI capacity is impaired;
- supplier CapEx is cut;
- equipment orders are canceled;
- the industry enters inventory and depreciation clearing.

Traditional electronics may regain some purchasing power, but supplier retrenchment can also damage:
- long-life line support;
- small-volume specialty capacity;
- supplier balance sheets;
- engineering continuity.

So the report should fear both:
- **crowding during expansion**, and
- **industrial whiplash during clearing**.

## 8. Link to formal Chapter 21

Formal Chapter 21 now establishes the strongest evidenced transmission for:
- smartphone;
- PC;
- game console;
- automotive/industrial memory;
- broadband devices.

This research-side extension adds the missing boundary:

> **the further an end system moves from shared advanced logic / memory into trusted, long-life, rad-hard, RF/power or other special-process electronics, the more indirect the AI crowding mechanism becomes.**

This prevents the report from turning “Cross-Market Resource Reordering” into a universal claim.

## 9. Formal-expansion gate v0.4

Before automotive / industrial supplier-side tightness is upgraded into a new AI-attributed formal response claim—or before aircraft / naval / radar / satellite / launch systems are added to the frozen formal chapter as AI-affected sectors—require at least one of:

1. supplier or government disclosure linking commercial capacity/equipment allocation to strategic-system access;
2. lead-time / EOL / trusted-capacity evidence showing deterioration during the AI capital cycle;
3. project-level evidence of cost/schedule impact traceable to shared semiconductor/packaging/test resources;
4. measurable competition for engineering, equipment or specialty-fab capacity.

Until then, the formal conclusion should remain:

> **risk mechanism identified; direct AI-attribution not yet established.**

## 10. Sources

- NXP S32G vehicle network processors — minimum 15 years of support: https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32g-vehicle-network-processors%3AS32G-PROCESSORS
- STMicroelectronics, 2025-09-08 — selected SPC58 automotive MCUs extended to 20-year availability: https://newsroom.st.com/media-center/press-item.html/n4718.html
- U.S. GAO, **Trusted Defense Microelectronics: Future Access and Capabilities Are Uncertain**, 2015: https://www.gao.gov/products/gao-16-185t
- U.S. DMEA Trusted Access Program Office — Trusted Foundry / Trusted Supplier Program: https://www.acq.osd.mil/asds/dmea/tapo/trusted-supplier-programs.html
- U.S. GAO, **Defense Industrial Base: Actions Needed to Address Risks Posed by Dependence on Foreign Suppliers**, 2025: https://files.gao.gov/reports/GAO-25-107283/index.html
- NASA JPL, **Space Radiation Effects on Integrated Circuits**: https://parts.jpl.nasa.gov/asic/Appendix.3.html
- NASA TechPort, **Radiation Hardened High Speed Integrated Circuits Double Data Rate I/O for Extreme Operating Environments**, updated 2026: https://techport.nasa.gov/projects/93719
- Infineon HiRel supply-longevity program for aerospace / military / defense applications: https://www.infineon.com/products/high-reliability/custom-services/supply-longevity


- Microsoft FY26 Q2 earnings — OEM inventory purchased ahead of memory-price increases and PC-market sensitivity to higher memory pricing: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2
- Microsoft FY26 Q3 More Personal Computing — OEM inventory behavior amid increasing memory pricing: https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q3/more-personal-computing-performance
- Microsoft FY26 Q4 earnings — higher component costs expected to raise device pricing and weigh on PC demand: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4
- Sony FY2025 Q4 earnings speech / FY2026 outlook — PS5 hardware planning tied to memory procurement: https://www.sony.com/en/SonyInfo/IR/library/presen/er/pdf/25q4_sonyspeech.pdf
- Nintendo, FY ending March 2026 six-month results Q&A — rising component / memory costs but hardware profitability expected to remain broadly maintained through cost-down absent major external changes: https://www.nintendo.co.jp/ir/pdf/2025/251105_2e.pdf


## Automotive / industrial counterevidence sources added in v0.4

- NXP Q2 2026 — automotive / industrial recovery and channel inventory: https://investors.nxp.com/news-releases/news-release-details/nxp-semiconductors-reports-second-quarter-2026-results/
- Infineon Q3 FY2026 — AI data-center demand strong while automotive orders also improve: https://www.infineon.com/press-release/2026/infpr202608-125
- Infineon Dresden Smart Power Fab, 2026-07-02 — €5B capacity serving power / analog / mixed-signal applications across AI data centers, automotive and industrial markets, with accelerated ramp optionality: https://www.infineon.com/press-release/2026/ifxpr202607-117
- STMicroelectronics Q2 2026 — strong bookings, selected supply tightness, distribution inventory below target, AI-data-center growth: https://newsroom.st.com/media-center/press-item.html/c3403.html
