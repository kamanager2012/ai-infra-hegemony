# Volume 9: Transmission from AI Infrastructure into the Physical Supply Chain

Chinese original: [vol-09.md](vol-09.en.md)

The residual model is in [Volume 5](vol-05.en.md). The residual-capacity pressure on consumer electronics is in [Volume 22](vol-22.en.md). 5.39 and the wrong pool are in `测算-投片与柜-20260826.md`. China's three layers are in [Volume 12](vol-12.en.md). This volume does not reopen those tables. This volume writes only that the first wave squeezed is PCs, general-purpose servers, and phones, not factories moving to the cloud.

## 1. Core question

How does AI infrastructure expansion transmit into PCs, smartphones, general-purpose servers, gaming, and other physical industries that do not directly buy frontier training systems?

The report answers this through **Non-AI Residual Capacity** rather than a generalized “resource reallocation” metaphor:

```text
NonAI_Residual
= Effective_Supply
- AI_Absorption
- Other_Priority_Demand
```

The first-wave effect is not that every factory suddenly pays a cloud tax. It is that consumer and general-purpose computing can receive less effective logic, memory, packaging, or component capacity after higher-priority AI/server demand absorbs the increment.
## 2. Evidence boundary

Historical versions used analyst SoC quotes, fixed 20%–30% downstream cost inflation, replacement-cycle assumptions, and self-derived HBM yield formulas. Those values are not used as publication facts.

Current anchors are stronger:
- TSMC 2025 HPC platform share **58%** and smartphone share **29%**;
- advanced packaging/testing slightly above **10%** of TSMC revenue, with management repeatedly describing tightness;
- Micron first-party **~3× HBM3E wafer-supply trade ratio versus DDR5**;
- TrendForce institutional evidence on HBM/RDIMM absorption and consumer-memory price pressure;
- NVIDIA's first-party disclosures showing consumer/gaming supply can be constrained while Data Center demand remains strong.

The mechanism is therefore resource competition and residual supply, not a universal device-BOM inflation coefficient.
## 3. Mechanism: resource allocation, residual supply, and product-cycle pressure

TSMC shipments, platforms, Customer A and B, and the packaging sentences are in [Volume 4](vol-04.en.md). 51% and the makers' shift are in [Volume 5](vol-05.en.md). The 5.39 wrong pool is in [Volume 4](vol-04.en.md) and `测算-投片与柜-20260826.md`. This volume does not reopen the ledger. This volume only lands those numbers on first-wave boxes.

**Packaging pressure must use the correct denominator.** The report's 5.39 CoWoS wafers/rack coefficient is a D-grade geometry stress test and must not be divided into TSMC's total foundry wafer shipments. 835,000 cabinets is void. The binding line is CoWoS. On a sell-side pool of about 1 million wafers, about 100,000 cabinets take more than half. You do not need 800,000 cabinets to lock 3nm. What first-wave box makers feel is not the whole factory bought out. It is increment slots and packaging slots going to cabinets first.

**Consumer and general-purpose compute draw from shared upstream resource pools.** The first wave is not "manufacturing digitization charged cloud rent." It is personal computers, commercial boxes, general-purpose servers, phones, and gaming cards fighting cabinets for the same slice of packaging and the same slice of high-price memory. Gaming cards: NVIDIA Q4 FY25 CFO commentary writes Blackwell and Ada supply limited. That is harder than any phone-analyst quote. How the four classes are squeezed is in sections 6 and 12.

**Commerce layer.** Prepayments and capacity commitments are in [Volume 1](vol-01.en.md). While the margin holds, commitments keep rising. Apple locks phone logic. However large phone logic is, it is not this increment. Why PC makers cannot bind the three checks is in section 13.

**Geopolitics layer.** Three layers are in [Volume 12](vol-12.en.md). The first wave is siphoned outside controls, and hit by licenses and residual prices together inside controls. The digital-transformation trap is a side branch: it explains who pays the rent; it does not explain who is squeezed in the first wave.

## 4. Scenarios, counterarguments, and testable indicators

Push forward from the numbers now. Do not assign extra probabilities.

Scenario A: AI demand continues to absorb a large share of incremental scarce resources. On the report's D-grade CoWoS geometry and external supply estimates, roughly 100,000 racks already represents a substantial packaging stress test. This does not imply a deterministic TSMC customer-allocation rule. Smartphone remains a large platform, while incremental HPC and packaging demand can still reduce the residual available to other products. PCs and general-purpose servers cannot buy same-generation HBM and same-generation packaging; DDR5 channel prices follow up. Gaming cards received the official "supply limited." A longer replacement cycle is a result, not a cause.

Scenario B: algorithm downscaling eases the endpoint; the resource reallocation turns from across-the-board price increases into a high/low split. Architectures like DeepSeek-V3 compress KV Cache 93.3% and convert pretrain to about $5.576M (earlier stress-test values; this volume did not re-open the technical report). If that spills into on-device distillation, phones and industrial boxes can run a good-enough local model, and the pathological demand for top-tier HBM falls. Training clusters stay expensive. In the first wave, flagships still pay the 3nm tax; mid and low end go back to mature-node residual. The river did not split. The up- and downstream price gap on the same river widened.

Scenario C: buyers cut; leading-edge capacity flows back to consumer. The other side says box giants have scale purchase power, and the resource reallocation is only a cycle. The rebuttal: however large the buyer, it cannot change reticle area or CoWoS fixture-hours; what can be talked is allocation order. The stronger other side: enterprise AI ROI misses, clouds cut capex, 3nm and packaging flow back to phones. That other side holds only if the cut actually happens, not if it appears only in the tone of a sell-side call. Official check: C.C. Wei in 2Q26 still said packaging is so tight that it limits customers' growth; NVIDIA supply commitments up $23.8B in three months. Neither is done now.

Other side four: booked 19% means Apple is still there; safe. The annual report itself writes the leading customer up from 12%, the second down from 22%, HPC already 58%. Safe distance is measured on the increment, not on full-year blended share. Other side five: 5.39 is invented. It is an estimate. The numerator 72 is official; the denominator about 13.4 is a geometry working assumption, not a 10-K. Using it on the whole factory's 15,022 thousand wafers is what invents. This volume crosses out the wrong pool. It does not promote the coefficient to official.

Falsifiable indicators (observation items only): whether TSMC's next call still has HPC above 58%, packaging and test still above 10%, and C.C. Wei still saying CoWoS tight or loosening; whether first-customer share keeps leaving 19% up or down; whether TrendForce next-quarter foundry revenue share still has TSMC above 70%; whether gaming cards and the data center are still written by the company as competing for supply; whether HBM+RDIMM is still written by the house as more than half of DRAM bits. These indicators go back to the makers and the original releases. This volume does not independently verify them here.

## 5. Gaps and what cannot be treated as fact

TSMC publishes no CoWoS monthly capacity, no official full-year wafer count, no packaging wafers by customer. C.C. Wei at the shareholders' meeting, the verbatim "sold out through 2026," cannot be found. How many B200s one CoWoS wafer yields has no official number. Samsung Taylor 16k / 24k / 40k wafers per month is not in the announcement. Do not convert HPC 58% or 3nm 24% into tens of thousands of wafers. The report does not treat TrendForce 72% as a share TSMC itself reported. NVIDIA 60%, 595k wafers is sell-side paraphrase. About 100,000 cabinets taking more than half is a sell-side pool times an estimate.

Older 20%–30% chip-cost, SoC-price, replacement-cycle, and robot-BOM estimates are not used as current fact-layer anchors. $215B is not an AI-hardware line item. The 3:1 wafer penalty: Micron's FY24 Q3 prepared remarks explicitly disclose the ~3× wafer-supply trade ratio; 8.6 and 13.2 are not maker multipliers. Volume 9 has no manufacturing output, employment, or inventory. This volume does not claim a factory in some country will close in some year.

The first-wave unit check — global PC units, general-purpose server units, smartphone units — has no newly checked maker series in this volume. Leave it empty. What can be written is the mechanism: they fight cabinets for the same slice of CoWoS and the same slice of high-price bits. The result of the fight is written in TSMC's platform table and the packaging sentences, not on an unchecked box-unit table.

The inventory channel of centralized inflation still holds, but the result is not the cause. Lead times widen; box makers place longs early; if clouds later cut GPU longs, manufacturing eats high-price inventory and a longer replacement cycle at once. The demand-side main engine has already moved from phones to training clusters. Phones are the residual squeezed out. A CIO signing a three-year frame at peak cloud quotes is an accounting mismatch in the side branch, not this volume's main question.

Geopolitical split amplifies the same mechanism. A factory that can buy a Blackwell-class system makes inspection a low-latency closed loop; a factory that cannot goes to cloud inference or a domestic accelerator. Two standard hours inside one group. The surface is digitization. The fact is supply-chain politics entering the process file. Once export controls make high-end accelerators a license good, the first wave inside controls is no longer only a residual-capacity pressure. It is the license queue itself. This volume invents no country's substitution rate.

Back to the spine. The system platform sells cabinets. The supply-coordination layer queues CoWoS and HBM. The software/runtime layer uses CUDA and the cabinet standard to lock the cabinet into a unit that does not come apart. The first wave is residual demand the supply-coordination layer squeezed out. If Volume 9 is written again as "cloud rent on factories," it has left the question. What can be checked is whether next quarter TSMC still says tight, whether HPC is still above 58%, and whether the first customer is still changing names.

## 6. How the four first-wave box classes are each squeezed

Personal computers. Consumer GPUs and data-center accelerators queue in the same firm's same set of supply commitments. Official text already writes Blackwell and Ada supply limited. That is not an analyst guess. PC box makers can talk board quota and channel price. They cannot talk CoWoS fixture-hours. HBM does not enter mainstream consumer DIMMs, but after makers move wafers from commodity DRAM to HBM, DDR5 channel prices follow up. PCs pay a memory residual pressure, plus discrete-GPU shortage. The CPU is still on the motherboard. The profit center is not there. The spine writes the CPU demoted to a cabinet accessory. Extinction is still a scenario. This volume does not write it as already happened.

Commercial PCs. Enterprise replacement was already slower than consumer. After the resource reallocation is added, the IT budget gains a slice of "AI PC" premium; what can be bought is often a same-generation or next-down SoC, not training-cluster-class packaging. Commercial boxes still have to pass security management and long-cycle driver certification. CoWoS will not yield this slice. When C.C. Wei says packaging already limits customer growth, that customer is first an accelerator customer, not a commercial-notebook customer. If a commercial box's digitization project then stacks a cloud-inference bill, it hits the transformation trap in the title. The trap is the second layer. The first layer is material.

General-purpose servers. CPU general-purpose servers and AI cabinets are not the same order, yet they fight the same fab's some mature nodes, power management, and substrate capacity, and they fight memory makers' wafers even more. TrendForce writes 51% of 2026 DRAM bits as HBM+RDIMM. RDIMM is a server DIMM, already counted in the half of bits "for cabinets," not a consumer DIMM. If a general-purpose server is still buying DDR5 RDIMM, it is buying residual after HBM has drawn, and the price follows the residual. Official cabinet: 13.4 TB HBM plus 17 TB LPDDR; 10,000 cabinets is 134 PB HBM. That is the product page multiplied, not a shipment forecast. General-purpose servers do not have this multiplier, and they do not enter the CoWoS queue.

Phones. TSMC's smartphone platform was still 29% in 2025, still up 11% year on year. The river did not dry. What changed is the increment: HPC +48%, revenue share from 51% to 58%. Apple locks phone logic. However large phone logic is, it is not the newly opened slice of 3nm / 2nm plus CoWoS. The annual report writes N2 entered volume in 4Q25; the table has no separate 2nm row; do not invent a share. Flagships keep paying leading-edge logic ASP; mid and low end go back to mature nodes. Older SoC price, BOM-share, and replacement-cycle estimates remain outside the current fact layer. What can be confirmed is the platform table and the packaging sentences: phones are still there, but they are not who the supply-coordination layer feeds first.

Gaming cards. They are not one of the four classes in the title, yet they are the give-way the system platform itself admits. Consumer cards and the data center fight the same front end and the same packaging. Official text writes supply limited. If Volume 9 only writes phone-analyst quotes and not this sentence, it has left the hardest first-wave evidence outside the volume.

## 7. How the residual-capacity pressure walks from packaging to the shelf

Packaging first, then memory, then the box. Packaging is the shortest gate. C.C. Wei in 4Q24 said all AI, tight, cannot meet; in 2Q26 said it already limits customer growth, the majority still CoWoS. Official text publishes no monthly capacity. Sell-side puts 2026 demand at about 1 million wafers, NVIDIA about 60%. At 5.39, about 100,000 cabinets take more than half. When packaging remains tight, competing buyers face allocation risk rather than a simple spot-price decision. Prepayments, order scale, credit, utilization, roadmap certainty, supplier diversification, and geopolitics all affect the allocation of incremental capacity.

Memory is the second gate. HBM eats more wafers per bit. The house writes half of 2026 DRAM bits as HBM+RDIMM. Makers turn to the high price. Consumer DIMMs and some server DIMMs are leftover. Leftover is not free. It follows the price up. Huaqiangbei talk, 450 to 1800, is only channel temperature, not a maker list.

The box is the third gate. A maker that cannot buy same-generation material either raises price, or specs down, or stretches replacement. That is the shelf form of centralized inflation. It is not a PMI series. It is BOM and lead time. Volume 9 has no newly checked box units. The report does not infer how many global phones fell. The mechanism is already enough: the supply-coordination layer queues material; the first wave pays tax.

Antitrust cannot knock this slice out. Source 05: a U.S. DOJ inquiry exists, a complaint does not; France is near the end, no statement of objections issued; the EU sent questionnaires, cleared Run:ai unconditionally, no 101/102 opening. 10% of annual turnover is a statutory ceiling. FY26 × 10% = $21.6B. That is not a fine. A fine does not change the bid, and it does not change CoWoS fixture-hours. Once national security writes advanced chips as license items, a split is harder to land. So the first wave cannot count on a court giving material back to PCs and phones. What can change allocation is a combination of stronger purchasing commitments, lower software migration costs, additional manufacturing sources, memory supply expansion, and executable power. These variables are tracked through the shared S1–S4 framework rather than a single “bundling” threshold.

## 8. Interface to the judgment and source 02

Judgment section 3: the increment is HPC; booked 19% is not a safe distance. Section 4: 5.39 is a CoWoS estimate; the 835,000-cabinet pool is wrong; the binding line is CoWoS; about 100,000 cabinets take more than half. Volume 9 lands those two sections on first-wave boxes. The China analysis remains layered: domestic supply is stronger in smartphones and parts of consumer computing, while a frontier-AI substitute still requires advanced logic, HBM-class memory, advanced packaging, interconnect, software maturity, and deployment scale.

Empty items in source 02 stay empty in this volume. Do not fill CoWoS monthly capacity. Do not fill Taylor wafers per month. The report does not treat 72% as a TSMC annual-report share. Source 05's "inquiries exist, complaints do not" is used here only to say the resource reallocation will not be broken by a fine. Four-cloud capex is not knocked into "AI hardware $215B." FY26 data center $193.7B is NVIDIA's own reported rent, not a four-cloud capex line item, and not Volume 9's manufacturing output.

This volume still outputs no global PC or phone unit decline for any year. With no unit series, a hard-written unit count can only be fiction. If a reader sees a sentence in this volume like "phones shipped X hundred million fewer units in 2026," the writer has broken the rule.

## 9. Why whole-factory division cannot tell the manufacturing shock

Divide 15,022 thousand wafers by 5.39 and you get a large cabinet count that sounds like "every factory in the world is feeding cabinets." That is the 835,000-cabinet error, amplified. Inside 15,022 thousand wafers sit phones, MCUs, auto, mature nodes, IoT. C.C. Wei also said in 2Q26: among mature nodes, only what is AI-related is tight, first power management, because data centers need large volumes of power chips. That sentence shows two things. First, the resource reallocation spills onto some mature nodes, not only 3nm. Second, what spills is "the few parts related to the cabinet," not a whole 28nm fab converted to GPUs. The manufacturing shock is therefore selective: parts that fight cabinets for packaging, HBM, and power management move first on lead time and price; MCUs and display drivers unrelated to cabinets walk their own cycle. If Volume 9 writes "the whole factory's 15 million wafers" as the shock total, it writes a selective shock as a full stop. A full stop is not the judgment, and it is not source 02.

The annual report writes 2025: 305 processes deployed, 12,682 products built for 534 customers. The customer count is still there. One name did not eat the factory. What was eaten is increment slots and packaging slots. 534 minus 1 is still not 0. That is how "booked 19% is not a safe distance" and "the whole factory was not bought out by one name" can both hold: full-year blended share is still 19%; voice on the scarce slice is already larger than 19%. What a manufacturing buyer feels is the second sentence, not the first.

Capacity above 17 million, shipments 15,022 thousand: in between sit utilization and mix. Do not treat the gap as "remainder left for phones." Official text has no wafers by platform. This volume stops at revenue share and the packaging sentences. It does not subtract 17 million minus 15,022 thousand and invent remainder wafers.

## 10. The annual report changes names: share fell, dollars barely rose

Put the two annual-report tables together and the first-wave squeeze is no longer a metaphor. The risk chapter writes first customer 2023 / 2024 / 2025 at 25% / 22% / 19%, second customer 11% / 12% / 17%, top ten 70% / 76% / 78%. The revenue table hides names as Customer A and Customer B: Customer A from NT$352,271,213 thousand to 726,974,278, share from 12% to 19%; Customer B from 624,345,477 to 645,178,671, share from 22% to 17%; the company from 2,894,307,699 to 3,809,054,272. These are annual-report text, not estimates.

Subtract the three rows only as a reading aid. Do not open a new scope. Customer A rose NT$374,703,065 thousand in a year; Customer B rose only 20,833,194; the company rose 914,746,573. Customer A took four-tenths of the increment; Customer B almost stood still. Share from 22% to 17% is not the competing customer thrown out of the fab. The pie grew and it did not keep up. What a buyer feels on the desk is the second sentence: the same material, slots first to the increment customer. Booked 19% looks more dispersed than 2023's 25%. That is full-year blend. Newly opened HPC rose 48% year on year; smartphones only 11%. Blended share walks down; voice on the scarce slice walks up. Both sentences sit in the same report.

Jensen saying they are already the largest customer is another line. It is not in TSMC's annual report. This volume does not name Customer A as anyone. What can be confirmed is the direction of the name change: leading customer jumped from 12%, second fell from 22%, top ten tightened from 70% to 78%. Seats among the ten are tighter, not looser. A manufacturing buyer wants next year's slot, not last year's blended share. Slots follow the increment. The increment is HPC and packaging. Leading-edge logic and advanced packaging that PCs, general-purpose servers, and phones want sit behind this increment.

The annual report also writes 2025: 305 processes deployed, 12,682 products built for 534 customers. The customer count is still there. The product count is still there. One name did not eat the factory. What was eaten is increment slots and packaging slots. 534 minus 1 is still not 0. That is the accounting writing of "booked 19% is not a safe distance" and "the whole factory was not bought out by one name" holding at once: full-year blend is still 19%; the scarce slice has already changed names. What first-wave box makers feel is the second sentence.

## 11. Cloud in-house accelerators sit on the same gate

Specs are in [Volume 4](vol-04.en.md). This volume does not reopen them. Cloud in-house cards are not a parallel river that yields to consumer electronics. They are a second group of buyers on the same scarce slice. The first wave is squeezed from both sides: cabinets take the slots the supply-coordination layer queues first; the clouds' own accelerators then take another part of 3nm and HBM. What PCs and phones see as "foundry still there, memory still there" is residual after these two buyer groups have drawn. The Samsung long is Tesla, not the four clouds handing GDS to a second TSMC.

## 12. Where the tax on the four box classes lands

Section 6 wrote how the four classes are squeezed. Here only fill where the tax lands. Do not repeat the queue story.

Personal computers pay two slices. One is discrete GPUs: the system platform's own CFO commentary already writes Blackwell and Ada supply limited; the consumer end yields to the data center. PC makers can talk board quota. They cannot talk packaging fixtures, and they cannot talk the prepaid manufacturing agreements on the books. Supply commitments from $95.2B to $119.0B, up $23.8B in three months; PC orders are not at the front of that table. The other slice is memory spillover. HBM does not enter mainstream consumer DIMMs; after makers move wafers over, DDR5 channel prices follow up. The house writes 51% of 2026 DRAM bits as HBM plus RDIMM. PC DIMMs are the more consumer slice of the remaining half. Channel talk, 16G from 450 to 1800, is only temperature, not a maker list. The CPU is still on the motherboard. The profit center is not there. Demotion to a cabinet accessory is a scenario. This volume does not write it as already happened.

Commercial PCs pay a premium plus certification lag. The IT budget gains a slice of "AI PC" premium; what is bought is a same-generation or next-down SoC, not training-cluster-class packaging. Security management and long-cycle drivers still have to pass. When C.C. Wei says packaging limits customer growth, that customer is first an accelerator customer. A digitization project that then stacks a cloud-inference bill hits the transformation trap. The trap is the second layer. The first layer is material.

General-purpose servers pay residual RDIMM after the draw. They and AI cabinets are not the same order, yet they fight the same fab's some mature nodes, power management, and memory wafers. RDIMM is already counted in the half of bits "for cabinets." Micron's FY24 Q3 prepared remarks explicitly disclose the ~3× wafer-supply trade ratio. Official cabinet 13.4 TB HBM; 10,000 cabinets is 134 PB, 30,000 is 402, 50,000 is 670 — product page multiplied, not a shipment forecast. General-purpose servers do not have this multiplier, and they do not enter packaging. C.C. Wei said among mature nodes only what is AI-related is tight, first power management. What spills is the few parts related to the cabinet, not a whole 28nm fab converted to accelerators. A selective shock, not a full stop.

Phones pay leading-edge logic ASP, not a packaging slot. The smartphone platform is still 29%, up 11% year on year. The river did not dry. What changed is the increment: HPC up 48%, share from 51% to 58%. 3nm revenue from 18% in 2024 to 24% in 2025, 28% in Q4, still revenue not wafers. N2 entered volume in 4Q25; the table has no separate row; do not invent a share. Apple locks phone logic, not newly opened packaging. The China framework does not collapse consumer electronics and frontier AI into one substitution ratio. The CXMT prospectus did not disclose an HBM product line; that negative evidence is scoped to the document and does not by itself resolve the broader frontier-AI stack. Older SoC-price and replacement-cycle estimates are not used as current fact-layer anchors.

Gaming cards are not one of the four classes in the title, yet they are the give-way the system platform itself admits. Official text writes supply limited. That sentence is harder than any phone-analyst quote.

## 13. Why PC makers cannot bind the three checks

Judgment section 7: to change allocation, bind three checks. Consumer and general-purpose buyers have less ability than hyperscalers to combine large prepayments, long-duration system demand, software-stack leverage, and memory contracts. That difference can weaken their bargaining position without implying that they are excluded from supply.

Prepayments. The system platform's books already write $119.0B, up $23.8B in three months. TSMC's allocation decisions reflect multiple economic and strategic variables rather than a deterministic first-customer rule. Public-scope prepayments from PC ODMs and brands have no commitment that matches this magnitude. What they can do is place longs with board and module makers. They cannot lock a foundry packaging slot. The long sits on the box layer, not on the scarce-slice layer. The clouds have money: Microsoft FY25 net income $101.832B, PPE up $64.551B. The clouds are not poor. That hundred billion builds halls. NVIDIA free cash $96.575B is earned selling the scarce slice itself; prepayments are reproduction. PC makers sit in neither hundred billion.

Software. The software/runtime layer uses a unified compute architecture, high-speed interconnect, and a cabinet standard to lock the cabinet into a unit that does not come apart. PC makers sell boxes and drivers. They do not hold this set. UXL and oneAPI are embryos. They have not been bound into software that lets a buyer switch slots. Miss this check and a larger prepayment is only a higher-price queue inside the same standard.

Memory longs. Box makers buy modules, not wafers. After makers turn to HBM, the commodity-bit line is the makers' own mix, not a line a PC long can hold alone. The house has already written half of 2026 DRAM bits as HBM+RDIMM. Consumer DIMMs and some server DIMMs are leftover. Leftover follows the price up. Huaqiangbei talk is only channel temperature. Miss this check and PC makers pay a spillover tax, not locked capacity.

If joint purchasing, stack portability, and memory-side long-term supply arrangements all remain weak, non-AI buyers have less leverage over incremental advanced capacity. Supply commitments had already risen to **$119.0B** at FY27 Q1, while major regulatory processes had not yet reached structural remedies. Consumer replacement cycles therefore operate on a slower clock than next-generation capacity reservation.

## 14. The license queue and the residual-capacity pressure are two layers, not one

Export controls split "who can buy an advanced accelerator" from "who must carry a domestic-substitute BOM." A manufacturing group's overseas plant and its plant in China may face entirely different chip lead times. Standard cost in the ERP will go false. This is not a tariff table Volume 9 is to invent. It is the mechanism: the first wave is siphoned outside controls, and hit by licenses and residual prices together inside controls.

China's stack must be analyzed in layers. Administrative controls can influence where domestic DDR, LPDDR, NAND, tools, and substrates are sold, but they cannot by themselves create frontier-equivalent advanced logic, HBM-class memory, advanced packaging, interconnect, and software portability. Domestic protection therefore changes allocation inside the existing supply base; it does not prove that every frontier-AI layer has already reached scale.

A factory that can buy a Blackwell-class system makes inspection a low-latency closed loop; a factory that cannot goes to cloud inference or a domestic accelerator. Two standard hours inside one group. The surface is digitization. The fact is supply-chain politics entering the process file. The digital-transformation question remains relevant, but it is secondary to the resource-allocation mechanism. It helps explain who absorbs higher costs, not which segment is constrained first. This volume's main question is still the resource reallocation.

## 15. Between C.C. Wei's two sentences, the gate did not loosen

The official sentences that can be confirmed are not the six English words "sold out through 2026." 4Q24 call, asked whether CoWoS was all for AI and whether other products would come: C.C. Wei said today is all AI focused, capacity is very tight, and cannot even meet customers' need. 2Q26 call, asked whether Intel EMIB would take packaging: he said packaging capacity is so tight that now it limits customers' growth; today the majority is still CoWoS. About a year and a half between the two sentences. The company did not change its mouth in those two calls and say it had loosened. The CFO in the same window took advanced packaging and test from about 8% in 2024 to a bit over 10% in 2025, 2026 outlook low teens. Revenue share is growing. The gate is still tight. What grew in revenue is price and mix, not "slots already enough for the competing customer."

"Sold out through 2026" at the shareholders' meeting has no official transcript. Several secondary paraphrases hang it on the 4 June 2026 meeting; the Focus Taiwan copy of that day that was opened has no CoWoS and no sold out. Secondary paraphrase is not promoted to an official sentence. What official text can confirm is still tight, cannot meet, already limits customer growth. If a first-wave box maker reads "annual capacity above 17 million wafers" as "the gate has loosened," it is treating whole-factory capacity as the scarce slice. Capacity above 17 million, shipments 15,022 thousand: in between sit utilization and mix. Do not treat the gap as remainder left for phones. Official text has no wafers by platform. This volume stops at revenue share and the packaging sentences.

The institutional layer points the same way. TrendForce 2026 Q1 release: TSMC share 72%, revenue nearly $35.86B; Samsung Foundry excluding System LSI 6.5%; SMIC 5.1%. Top ten $47.95B. UMC 3.9%, GlobalFoundries 3.3%. Institutional revenue share, not units, not a share TSMC itself reported. Public high-end AI logic volume is still mostly TSMC, with Samsung as a parallel line. competing customer 6.5% is not a second TSMC. A PC maker moving the order to Samsung or SMIC does not pass the same yield gate.

## 16. Increment wafers cannot be split by platform

2025 shipments 15,022 thousand wafers, 2024 12,910 thousand, subtract and the add is 2,112 thousand. That is two official numbers subtracted, not a new scope. There are no shipments by node or by platform. The report does not treat these 2,112 thousand wafers as all HPC or all phones. What can be written is the revenue side: HPC up 48% year on year, smartphones 11%, IoT 15%, automotive 34%, DCE flat. Increment revenue is in HPC. Mapping revenue increment one-for-one onto wafer increment is converting 58% into tens of thousands of wafers. Source 02 writes that it cannot be done. Section 3 already crossed out the 5.39 pool: it divides packaging, not the whole factory. 835,000 cabinets and 2.78 million cabinets have no physical meaning. The binding line is still packaging. About 100,000 cabinets taking more than half is a sell-side pool times an estimate. This volume does not promote the coefficient to official.

## 17. A fine does not change fixture-hours; rent does not explain who is squeezed

The docket is in [Volume 11](vol-11.en.md). Rent is in [Volume 8](vol-08.en.md). This volume does not reopen them. A fine does not change CoWoS fixture-hours. The first wave cannot count on a court giving material back to PCs and phones. This volume asks only: whom the supply-coordination layer queues first, and who in the first wave pays tax. With no unit series, it outputs no global PC or phone unit decline for any year.
