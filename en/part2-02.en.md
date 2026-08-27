# Macro Essay 2: AI Platform Concentration and NVIDIA's System-Level Power

Chinese original: [part2-02.md](part2-02.md)

The cabinet as sales unit: [Volume 2](vol-02.en.md) and [Volume 32](vol-32.en.md). Official single-cabinet spec follows the judgment: 72 GPU, 36 Grace, HBM 13.4 TB, LPDDR 17 TB. This essay does not reopen the FY26 table.

## 1. The question this essay answers

Is NVIDIA's platform power primarily a single-chip benchmark advantage, or the result of integrating compute dies, HBM, NVLink, rack-scale interconnect, cooling, software, and deployment standards into one system stack? What does the official physical BOM confirm, what remains undisclosed, and where can Ethernet or hyperscaler-built systems create credible substitution?

This essay only confirm public sources: the NVIDIA GB200 NVL72 product page, the technical blog, the 18 March 2024 newsroom, the FY26 press release and 10-K / CFO. The draft's whole-cabinet dollar split table is not official. This essay does not promote it, does not fill it, does not invent it.

## 2. Evidence boundary

Official NVIDIA materials support the physical composition of GB200 NVL72: 72 Blackwell GPUs, 36 Grace CPUs, 13.4 TB HBM3E, 17 TB LPDDR5X, NVLink scale-up, switch trays, copper interconnect, and liquid cooling.

They do **not** disclose:
- a factory-gate rack price;
- a line-item dollar BOM;
- a cabinet-specific software premium;
- an official Ethernet-versus-NVLink MFU or latency table.

Historical rack-ASP and software-premium estimates therefore remain outside the fact layer. The analysis focuses on physical integration, interface control, switching cost, and system-level substitution.
## 3. Mechanism (physical / commercial / geopolitical)

Physically, what this cabinet has to solve is not "one more faster GPU." It is turning All-to-All among 72 cards from a network problem into an in-domain problem. The product page writes the 72-GPU NVLink domain as acts as a single, massive GPU. The technical blog spreads the mechanical parts: 18 compute trays, 9 switch trays, copper cable cartridges, liquid cooling. Fifth-generation NVLink 1.8 TB/s per card, whole cabinet 130 TB/s. The launch write-up writes the die-to-die link as 10 TB/s, C2C as 900 GB/s. These numbers are official. An Ethernet scheme has no official head-to-head table. The product page anchors the comparison on "H100 scaled over InfiniBand" versus "NVL72," not a third-party audit of "loose cards plus 800G RoCE."  if a buyer splits 72 cards over Ethernet, what they buy is another curve the official page has not admitted as equivalent. Nanoseconds of latency, how far MFU drops: this essay finds no official instrument record. Do not invent one. How many kilowatts copper saves versus optics: the product page only writes that liquid cooling raises density and cuts footprint. It does not print "20 kW saved per cabinet."

Memory is two pools, not one. HBM3E 13.4 TB sits next to the GPU. LPDDR5X 17 TB sits on Grace. C2C lets software see a unified space. The blog writes 30 TB. The product page prints them apart. The judgment wrote residual this way: makers convert to HBM, consumer bits get fewer; server DDR5 is already residual, not another river. One cabinet eats HBM and LPDDR at once. Expanding cabinets is expanding both pools. The 10-K writes memory bought from three names. It does not make HBM itself. So the heaviest slice of the physical BOM is officially admitted as bought-in. What the system seller collects is the right to bundle bought-in HBM, bought-in wafers, own NVLink, and CUDA into a turnkey. It is not smelting copper or pulling wafers itself.

Interconnect is also two layers. Do not mix them. In-domain is fifth-generation NVLink plus switch trays, officially written as scale-up. Between domains is Quantum InfiniBand, Spectrum Ethernet, BlueField-3, officially written as connecting hundreds or thousands of Blackwells out. The press release's 576 cards, 1 PB/s, is an upper-bound promotion of a larger NVLink domain, not 576 cards in every cabinet. This essay's sales unit is this one NVL72 cabinet. Cabinet to cabinet still walks their NICs and switches. Interface control extends from the scale-up domain to the broader campus network.

Commercially, the platform does not stand on an undisclosed line-item dollar BOM. It stands on three things being true at once. First, the sales unit moved up: NVL72 writes cabinet dimensions, liquid cooling, and the NVLink domain as a reference design; OEMs assemble to drawing. Second, margin lives at the company layer, not in a cabinet line item. See [Volume 1](vol-01.en.md). Third, prepayments lock the next generation. They have not already bought the whole factory dead.

Software and interface control sits in CUDA, PTX, TensorRT-LLM, NeMo, NIM, and Mission Control, all of which can reinforce switching costs and system integration. Supply coordination sits in how chips, HBM, packaging, interconnect, cooling, and racks are co-designed. The economic object is therefore **system-stack value capture**, not "a margin monopoly welded into a cabinet."

The technical blog also writes interconnect generations. NVLink walked from first-generation 160 GB/s in 2014 to fifth-generation 1.8 TB/s; the text writes per-card bandwidth as 12× the first generation; domain size expanded from at most 8 cards on a board (HGX H200, 900 GB/s per card) to 72 cards. 576 cards, over 1 PB/s, 240 TB fast memory, is an upper-bound promotion of a larger domain, not this NVL72 cabinet's spec. This essay confirms the cabinet spec to the product page: 72 cards, 13.4 TB, 17 TB, 130 TB/s. The generation story is only used to show how interface control expanded: bandwidth and domain size rose together. What Ethernet has to chase is not one point. It is a curve they defined themselves.

The physical BOM has four levels. Do not quote a price by skipping a level. Die: two reticle-limit dies fused into one logical GPU; the launch write-up writes 10 TB/s die-to-die. Superchip: two GPUs plus one Grace, C2C 900 GB/s. Tray: two Grace plus four GPUs, liquid-cooled, 80 petaflops, 1.7 TB. Whole cabinet: 18 trays plus 9 switch trays, copper cable cartridges. What official sources give is composition at this level, not dollars at this level. Someone using company gross margin 75% to back out "software XXX ten-thousand per cabinet" — the equation does not hold. Gross margin is a full-year weighted average of all products. Inside it are gaming cards, professional cards, auto, the H20 charge. The 10-K has no "NVL72 line-item gross margin" row. Inventory $21.4B at FY26 year-end, $25.8B at Q1 end; product-warranty liability $2.8B at FY26 year-end: all company-layer. Warranty or inventory cannot be divided by an undisclosed cabinet count and treated as unit cost.

Tape-out: [Volume 16](vol-16.en.md) and [Volume 24](vol-24.en.md). This essay only borrows: what is truly scarce is packaging and HBM, not front-end logic unit count. Dollars stay blank.

## 4. Scenarios, counterarguments, and testable indicators

Scenario A: system premium holds. MoE training and low-latency inference still want in-domain All-to-All. NVL72-class cabinets remain the default buy unit. Official sources do not publish cabinet price. Premium is written in company gross margin 71%–75% and supply commitments adding up. Clouds shunt internal recommendation onto ASICs. External general training keeps buying cabinets. Public next-generation ASICs (Maia 200, Ironwood, Trainium3) themselves are also asking for HBM and advanced packaging (judgment path five). They are not a retreat to 5nm plus commodity DDR5. To beat today's cabinet you return to 3nm, HBM, CoWoS, and you bid against 75% gross margin.

Scenario B: algorithms lower interconnect sensitivity. Routed experts get fewer, KV is flattened, an Ethernet cluster's effective throughput is no longer clearly worse than in-domain NVLink. Customers start breaking cabinets and buying loose cards. Nvidia still sells GPUs and NICs. It cannot sell "whole-cabinet rent." The test is whether mainstream MoE is still officially demoed on NVL72 as default. Official demos have kept using 1.8T-class GPT-MoE. That itself is saying: this class of model needs this domain.

Scenario C: self-built ASICs plus optical switching work well on a general framework. Cabinet-level NVLink uniqueness falls. That requires a compiler and an ecosystem, not only a chip spec. The TPU path exists. The page does not name TSMC or Broadcom. If production training migrates at scale, incumbent system share can fall. If not, software/runtime switching costs remain material. The relevant test is whether cloud system stacks take a meaningful share of training, not merely whether custom chips exist.

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

Counterfactual. Suppose an Ethernet appears, and official or checkable third parties put bandwidth and latency near a 1.8 TB/s in-domain. NVL72's system premium becomes a negotiable integration fee. This essay finds no official evidence that such an Ethernet already exists. Suppose new hardware features ship as an open intermediate representation, not only from CUDA kernel scheduling. Interface control weakens. Reality is written the other way. A credible substitute must match production requirements in latency, bandwidth, kernel scheduling, compilers, and deployment tooling. Stock-price or narrative changes do not provide that substitution.

The test of a system monopoly, in the end, is whether a customer can move one training job wholly off the cabinet without changing the model structure. If they cannot, company-layer 75% gross margin is the mirror of rent. If they can, the whole cabinet is negotiable integration. Today's official product definition is designed as cannot-move. This essay leaves that sentence for later essays, to see whether algorithms and ASICs can rewrite it.

The platform-control layers' division of labor on this cabinet can be written as one sentence. the system seller sells 72 cards, 36 Grace, 9 switch trays, and a copper backplane. the software/interface layer sets the NVLink domain, CUDA, and the cabinet outline. the supply-coordination layer sets the HBM / CoWoS / NVLink mix; prepayments buy the queue. The model player ships Nemotron / NIM and does not grab the cabinet P&L. Drop one corner and this cabinet is still a commodity. All platform-control layers at once, and this cabinet is the platform's sales unit.

The newsroom partner list is side evidence that the sales unit moved up, not a shipment table. The 18 March 2024 piece names AWS, Google Cloud, Microsoft Azure, Oracle, and CoreWeave, Lambda, and others. Later blogs write that CoreWeave first made GB200 NVL72 instances public, and OCI put up liquid-cooled cabinets. The list proves clouds are taking cabinets as cabinets. It does not prove how many cabinets any one name bought, and does not prove cabinet price. The product page has already opened GB300 NVL72 (72 Blackwell Ultra plus 36 Grace), which says the sales unit will keep walking this outline. This essay does not write GB300's unchecked memory or unchecked cabinet price.

Cabinet count cannot be backed out of free cash. $96,575M free cash divided by any cabinet price yields a fake cabinet count. Official sources give no divisor. This essay refuses that division. What can be written is the direction: free cash and operating income are large enough that prepayments can still add; the result of adding is written in supply commitments from $95.2B to $119.0B, not in "how many cabinets shipped this year."

## 5. Gaps and what must not be treated as fact

NVIDIA has not published an NVL72 factory-gate price, a channel price, or a line-item dollar BOM. The draft's whole-cabinet ASP range, software premium of forty-odd points, HBM tens of thousands of dollars per cabinet: none enter this essay's fact layer. Do not invent $2.5–3.0M/cabinet either. Gross margin 71.1% / 75.0% is company-layer, not cabinet line-item gross margin.

The product page does not print whole-cabinet watts. 120 kW is the judgment's and the industry's common scope. This essay does not promote it to official. Copper "2 miles," in-domain latency "under 100 ns," Ethernet MFU "25%": neither the official page nor the 10-K has them. Do not write them.

30× / 4× / 25× is official promotion. The same page marks projected, subject to change. 1.4 exaflops, 30 TB is the 18 March 2024 press release. The product page now prints 13.4 TB plus 17 TB. Both scopes sit together. Do not fuse a third.

Prepayments are not split to TSMC, not split to CoWoS, and do not name a 2nm first-silicon amount. Supply commitments "some can be rescheduled." Multi-year cloud $27B / $30B is not wafer prepayments.

Net margin 55.6% is a back-calculation. PTX 95%, AMD lagging 30%–50%, single-die Switch gross margin, NIM ARR, whole-cabinet shipments: not found. This essay opened the product page, the technical blog, the newsroom Blackwell piece, the FY26 press release, and carries [Volume 1](vol-01.en.md)'s 10-K / CFO citations. It did no unboxing, and did not reread every 10-K footnote. Quantitative forecasts without a source are marked unverified. Do not treat them as audit fact.
