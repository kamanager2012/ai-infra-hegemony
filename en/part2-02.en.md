# Essay 2: Nvidia's hardware–software empire, the NVL72 BOM, and interconnect

Chinese original: [part2-02.md](part2-02.md)

The cabinet as sales unit: [Volume 2](vol-02.md) and [Volume 32](vol-32.md). Official single-cabinet spec follows the judgment: 72 GPU, 36 Grace, HBM 13.4 TB, LPDDR 17 TB. This essay does not reopen the FY26 table.

## 1. The question this essay answers

Is Nvidia's hegemony single-chip benchmark lead, or welding a compute die, HBM, NVLink, a copper backplane, and liquid cooling into a system that cannot be sold in pieces? What does the official BOM give, and what does it not give? Can Ethernet or a self-built ASIC go around this interconnect? How do the four corners (athlete, referee, coach, model player) land on this one cabinet?

This essay only nails public sources: the NVIDIA GB200 NVL72 product page, the technical blog, the 18 March 2024 newsroom, the FY26 press release and 10-K / CFO. The draft's whole-cabinet dollar split table is not official. This essay does not promote it, does not fill it, does not invent it.

## 2. What the draft already argued (compressed; official numbers kept, dollar BOM removed)

The sales unit has already moved up from the chip to the cabinet. The judgment's four corners land in this essay on NVL72 as one commodity.

What is in one official cabinet follows the product page (https://www.nvidia.com/en-us/data-center/gb200-nvl72/):

- 36 Grace CPUs, 72 Blackwell GPUs
- GPU memory 13.4 TB HBM3E
- CPU memory 17 TB LPDDR5X
- NVLink bandwidth 130 TB/s
- 2,592 Arm Neoverse V2 cores
- NVFP4 Tensor Core 1,440 PFLOPS (sparse); FP8/FP6 720 PFLOPS (sparse); a footnote writes dense as half of sparse
- On-page claims versus H100: inference 30×, training 4×, energy efficiency 25×. The same page writes projected performance subject to change. That is the company's own promotional scope, not a third-party measurement.

The technical blog (developer.nvidia.com, the GB200 NVL72 piece) opens the mechanical structure. One GB200 Superchip is two Blackwell plus one Grace, NVLink-C2C bidirectional 900 GB/s; what the application sees is a unified address space. Compute trays follow MGX: two Grace, four Blackwell, liquid-cooled cold plates, PCIe Gen6, NVLink cable-cartridge interfaces; a single tray is written as 80 petaflops AI, 1.7 TB fast memory. A whole cabinet is 18 compute nodes, 9 NVLink switch trays, copper cable cartridges interconnecting them. NVL72 can be one cabinet of 72 cards (18 dual-Superchip nodes), or split into two cabinets. Fifth-generation NVLink is 1.8 TB/s bidirectional per GPU; the text writes more than 14× PCIe Gen5. Each switch tray has 144 NVLink ports, 100 GB per port; nine trays fully connect 18 ports on each of 72 cards. The blog writes the whole cabinet as 72 cards, 30 TB unified memory, 130 TB/s fabric. 30 TB is the order of 13.4 plus 17. The product page prints the two pools separately. This essay follows the product page's 13.4 TB / 17 TB.

The 18 March 2024 newsroom (Blackwell platform launch) announced the chip and the cabinet together. Blackwell GPU 208 billion transistors, TSMC custom 4NP, two reticle-limit dies fused into one logical GPU with a 10 TB/s die-to-die link. Fifth-generation NVLink 1.8 TB/s per card, up to 576 cards. GB200 NVL72 is 36 Superchips, 72 GPUs plus 36 CPUs, with BlueField-3. The press release writes the whole cabinet as "a single GPU," 1.4 exaflops AI, 30 TB fast memory. Versus H100, inference up to 30×, cost and energy down up to 25×. These are launch sentences, with up to. They are not an unboxing measurement.

Company books and supply commitments: [Volume 1](vol-01.md). The 10-K nails prepayments. It does not split cabinet price, and has no factory-gate cabinet price.

The draft had a whole-cabinet ASP range and a line-item dollar BOM (die, HBM, CoWoS, Switch, copper cable, liquid cooling, software premium of forty-odd points). NVIDIA's product page, newsroom, and 10-K print neither a factory-gate cabinet price nor line-item dollars. The judgment called "re-sticking a BOM" idle work. This essay deletes that dollar set. Do not fill in $2.5–3.0M/cabinet, and do not back-calculate 75% gross margin into "software premium XXX ten-thousand per cabinet." BOM in this essay means only the official physical composition: how many cards, how much memory, how many switch trays, what interconnect.

Cabinet count times spec: [Volume 16](vol-16.md). The reticle limit explains why one logical GPU needs two dies, and why packaging hits the ceiling before the front end.

Jensen Huang's original sentence in the FY26 press release: "Grace Blackwell with NVLink is the king of inference today." This essay reads that sentence as the company itself admitting: what is sold is the Grace + Blackwell + NVLink set, not loose cards.

## 3. Mechanism (physical / commercial / geopolitical)

Physically, what this cabinet has to solve is not "one more faster GPU." It is turning All-to-All among 72 cards from a network problem into an in-domain problem. The product page writes the 72-GPU NVLink domain as acts as a single, massive GPU. The technical blog spreads the mechanical parts: 18 compute trays, 9 switch trays, copper cable cartridges, liquid cooling. Fifth-generation NVLink 1.8 TB/s per card, whole cabinet 130 TB/s. The launch write-up writes the die-to-die link as 10 TB/s, C2C as 900 GB/s. These numbers are official. An Ethernet scheme has no official head-to-head table. The product page anchors the comparison on "H100 scaled over InfiniBand" versus "NVL72," not a third-party audit of "loose cards plus 800G RoCE." Analysis added: if a buyer splits 72 cards over Ethernet, what they buy is another curve the official page has not admitted as equivalent. Nanoseconds of latency, how far MFU drops: this essay finds no official instrument record. Do not invent one. How many kilowatts copper saves versus optics: the product page only writes that liquid cooling raises density and cuts footprint. It does not print "20 kW saved per cabinet."

Memory is two pools, not one. HBM3E 13.4 TB sits next to the GPU. LPDDR5X 17 TB sits on Grace. C2C lets software see a unified space. The blog writes 30 TB. The product page prints them apart. The judgment wrote residual this way: makers convert to HBM, consumer bits get fewer; server DDR5 is already residual, not another river. One cabinet eats HBM and LPDDR at once. Expanding cabinets is expanding both pools. The 10-K writes memory bought from three names. It does not make HBM itself. So the heaviest slice of the physical BOM is officially admitted as bought-in. What the athlete collects is the right to bundle bought-in HBM, bought-in wafers, own NVLink, and CUDA into a turnkey. It is not smelting copper or pulling wafers itself.

Interconnect is also two layers. Do not mix them. In-domain is fifth-generation NVLink plus switch trays, officially written as scale-up. Between domains is Quantum InfiniBand, Spectrum Ethernet, BlueField-3, officially written as connecting hundreds or thousands of Blackwells out. The press release's 576 cards, 1 PB/s, is an upper-bound promotion of a larger NVLink domain, not 576 cards in every cabinet. This essay's sales unit is this one NVL72 cabinet. Cabinet to cabinet still walks their NICs and switches. Referee power stretches from the backplane to the campus network.

Commercially, the empire does not stand on an undisclosed line-item dollar BOM. It stands on three things being true at once. First, the sales unit moved up: NVL72 writes cabinet dimensions, liquid cooling, and the NVLink domain as a reference design; OEMs assemble to drawing. Second, margin lives at the company layer, not in a cabinet line item. See [Volume 1](vol-01.md). Third, prepayments lock the next generation. They have not already bought the whole factory dead.

Referee power sits in software and interfaces. CUDA, PTX, TensorRT-LLM, NeMo, NIM, Mission Control: the product page treats them all as existing product lines. A generation can change without tearing customer software. Do not write NIM as a second profit pool. Coach power sits in the mix. Packaging tightness: [Volume 24](vol-24.md). The China stack: [Volume 12](vol-12.md). NVL72 is the commodity that welds a margin monopoly into a cabinet outline.

The technical blog also writes interconnect generations. NVLink walked from first-generation 160 GB/s in 2014 to fifth-generation 1.8 TB/s; the text writes per-card bandwidth as 12× the first generation; domain size expanded from at most 8 cards on a board (HGX H200, 900 GB/s per card) to 72 cards. 576 cards, over 1 PB/s, 240 TB fast memory, is an upper-bound promotion of a larger domain, not this NVL72 cabinet's spec. This essay nails the cabinet spec to the product page: 72 cards, 13.4 TB, 17 TB, 130 TB/s. The generation story is only used to show how referee power grew: bandwidth and domain size rose together. What Ethernet has to chase is not one point. It is a curve they defined themselves.

The physical BOM has four levels. Do not quote a price by skipping a level. Die: two reticle-limit dies fused into one logical GPU; the launch write-up writes 10 TB/s die-to-die. Superchip: two GPUs plus one Grace, C2C 900 GB/s. Tray: two Grace plus four GPUs, liquid-cooled, 80 petaflops, 1.7 TB. Whole cabinet: 18 trays plus 9 switch trays, copper cable cartridges. What official sources give is composition at this level, not dollars at this level. Someone using company gross margin 75% to back out "software XXX ten-thousand per cabinet" — the equation does not hold. Gross margin is a full-year weighted average of all products. Inside it are gaming cards, professional cards, auto, the H20 charge. The 10-K has no "NVL72 line-item gross margin" row. Inventory $21.4B at FY26 year-end, $25.8B at Q1 end; product-warranty liability $2.8B at FY26 year-end: all company-layer. Warranty or inventory cannot be divided by an undisclosed cabinet count and treated as unit cost.

Tape-out: [Volume 16](vol-16.md) and [Volume 24](vol-24.md). This essay only borrows: what is truly scarce is packaging and HBM, not front-end logic unit count. Dollars stay blank.

## 4. Analysis added (scenarios, counters, testable indicators)

Analysis added.

Scenario A: system premium holds. MoE training and low-latency inference still want in-domain All-to-All. NVL72-class cabinets remain the default buy unit. Official sources do not publish cabinet price. Premium is written in company gross margin 71%–75% and supply commitments adding up. Clouds shunt internal recommendation onto ASICs. External general training keeps buying cabinets. Public next-generation ASICs (Maia 200, Ironwood, Trainium3) themselves are also asking for HBM and advanced packaging (judgment path five). They are not a retreat to 5nm plus commodity DDR5. To beat today's cabinet you return to 3nm, HBM, CoWoS, and you bid against 75% gross margin.

Scenario B: algorithms lower interconnect sensitivity. Routed experts get fewer, KV is flattened, an Ethernet cluster's effective throughput is no longer clearly worse than in-domain NVLink. Customers start breaking cabinets and buying loose cards. Nvidia still sells GPUs and NICs. It cannot sell "whole-cabinet rent." The test is whether mainstream MoE is still officially demoed on NVL72 as default. Official demos have kept using 1.8T-class GPT-MoE. That itself is saying: this class of model needs this domain.

Scenario C: self-built ASICs plus optical switching work well on a general framework. Cabinet-level NVLink uniqueness falls. That requires a compiler and an ecosystem, not only a chip spec. The TPU path exists. The page does not name TSMC or Broadcom. If it is done, the athlete's share will drop. If it is not done, referee power stays. Of the five paths the judgment can interrupt, this one is "a cloud ASIC pulls training off." It has not been done.

Counters. Comparing "who is faster" on single-card TFLOPS, and going around the 72-card domain. Writing undisclosed whole-cabinet dollars as audit fact. Treating 30× / 4× / 25× promotional sentences as already instrument-checked. Writing supply commitments $119.0B as already buying TSMC's whole factory dead. Writing NIM as a second profit pool. Mixing 13.4 TB and 13.8 TB, 30 TB into a precise unified memory without marking the source.

Testable indicators (write the number when there is one; leave blank when there is not):

- Whether public deliveries are still mainly whole cabinets / NVLink domains, not loose cards plus Ethernet
- Whether company gross margin holds above 70% (last two quarters already back near 75%)
- Whether supply commitments keep adding (already from $95.2B to $119.0B)
- Whether the product page still prints the 13.4 TB / 17 TB / 130 TB/s set
- Whether CUDA / NIM / Mission Control is still the default deploy stack
- Whether next-generation Rubin first silicon is still locked by the same prepayment language
- Whether public cloud-ASIC specs still want HBM and CoWoS, rather than retreating to commodity DDR5

For buyers: the fight must happen before a campus pours concrete to this liquid-cooling and copper-backplane set. An ASIC must leave another set on power and network. An algorithm must lower dependence on a 72-card unified domain in the model structure. Wait until cabinets are in place and then talk "multi-chip elastic scheduling," and the scheduling space has already been narrowed by domain size. Essay 2 is not a hymn. It marks for later essays the place the counter must happen early.

Counterfactual. Suppose an Ethernet appears, and official or checkable third parties put bandwidth and latency near a 1.8 TB/s in-domain. NVL72's system premium becomes a negotiable integration fee. This essay finds no official evidence that such an Ethernet already exists. Suppose new hardware features ship as an open intermediate representation, not only from CUDA kernel scheduling. Referee power thins a slice. Reality is written the other way. Attack latency, bandwidth, kernel scheduling, and you attack the empire. Attack the stock price or public opinion, and you do not.

The test of a system monopoly, in the end, is whether a customer can move one training job wholly off the cabinet without changing the model structure. If they cannot, company-layer 75% gross margin is the mirror of rent. If they can, the whole cabinet is negotiable integration. Today's official product definition is designed as cannot-move. This essay leaves that sentence for later essays, to see whether algorithms and ASICs can rewrite it.

The four corners' division of labor on this cabinet can be written as one sentence. The athlete sells 72 cards, 36 Grace, 9 switch trays, and a copper backplane. The referee sets the NVLink domain, CUDA, and the cabinet outline. The coach sets the HBM / CoWoS / NVLink mix; prepayments buy the queue. The model player ships Nemotron / NIM and does not grab the cabinet P&L. Drop one corner and this cabinet is still a commodity. All four corners at once, and this cabinet is the empire's sales unit.

The newsroom partner list is side evidence that the sales unit moved up, not a shipment table. The 18 March 2024 piece names AWS, Google Cloud, Microsoft Azure, Oracle, and CoreWeave, Lambda, and others. Later blogs write that CoreWeave first made GB200 NVL72 instances public, and OCI put up liquid-cooled cabinets. The list proves clouds are taking cabinets as cabinets. It does not prove how many cabinets any one name bought, and does not prove cabinet price. The product page has already opened GB300 NVL72 (72 Blackwell Ultra plus 36 Grace), which says the sales unit will keep walking this outline. This essay does not write GB300's unchecked memory or unchecked cabinet price.

Cabinet count cannot be backed out of free cash. $96,575M free cash divided by any cabinet price yields a fake cabinet count. Official sources give no divisor. This essay refuses that division. What can be written is the direction: free cash and operating income are large enough that prepayments can still add; the result of adding is written in supply commitments from $95.2B to $119.0B, not in "how many cabinets shipped this year."

## 5. Gaps and what must not be treated as fact

NVIDIA has not published an NVL72 factory-gate price, a channel price, or a line-item dollar BOM. The draft's whole-cabinet ASP range, software premium of forty-odd points, HBM tens of thousands of dollars per cabinet: none enter this essay's fact layer. Do not invent $2.5–3.0M/cabinet either. Gross margin 71.1% / 75.0% is company-layer, not cabinet line-item gross margin.

The product page does not print whole-cabinet watts. 120 kW is the judgment's and the industry's common scope. This essay does not promote it to official. Copper "2 miles," in-domain latency "under 100 ns," Ethernet MFU "25%": neither the official page nor the 10-K has them. Do not write them.

30× / 4× / 25× is official promotion. The same page marks projected, subject to change. 1.4 exaflops, 30 TB is the 18 March 2024 press release. The product page now prints 13.4 TB plus 17 TB. Both scopes sit together. Do not fuse a third.

Prepayments are not split to TSMC, not split to CoWoS, and do not name a 2nm first-silicon amount. Supply commitments "some can be rescheduled." Multi-year cloud $27B / $30B is not wafer prepayments.

Net margin 55.6% is a back-calculation. PTX 95%, AMD lagging 30%–50%, single-die Switch gross margin, NIM ARR, whole-cabinet shipments: not found. This essay opened the product page, the technical blog, the newsroom Blackwell piece, the FY26 press release, and carries [Volume 1](vol-01.md)'s 10-K / CFO citations. It did no unboxing, and did not reread every 10-K footnote. Quantitative forecasts without a source are marked unverified. Do not treat them as audit fact.
