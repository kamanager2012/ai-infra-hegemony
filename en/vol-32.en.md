# Volume 32: NVIDIA Full-Stack Architecture — GPU, NVLink, CUDA/PTX, and Rack-Scale Systems

Chinese original: [vol-32.md](vol-32.en.md)

The system-stack mechanism is developed in [Volume 2](vol-02.en.md), while hyperscaler alternatives are covered in [Volume 4](vol-04.en.md) and [Volume 25](vol-25.en.md). This volume focuses on the physical and software architecture that turns many accelerators into a rack-scale system.

## 1. Core question

Is NVIDIA's moat the accelerator die itself, or the integration of GPU, HBM, NVLink, CUDA/PTX, rack-scale design, cooling, power, and deployment tooling into one deliverable compute system?

The durable evidence is the official rack-scale architecture and company financials. Historical BOM estimates—whole-rack ASP, software/brand premium, switch-chip margin, cable cost, cooling cost, and similar teardown values—remain engineering estimates and do not enter the fact layer.

The relevant competitive test is therefore whether alternative platforms can reproduce effective workload performance, memory/fabric behavior, compiler/runtime maturity, reliability, and deployment scale—not whether they can design one accelerator die.
## 2. Evidence boundary

First-party anchors include:
- GB200 NVL72: **72 GPUs**, **36 Grace CPUs**, **13.4 TB HBM3E**, **17 TB LPDDR5X**, and rack-scale NVLink;
- NVIDIA's current financial and Data Center results;
- official CUDA/PTX, NVLink, system, and deployment documentation;
- TSMC's first-party advanced-packaging tightness disclosures.

Historical teardown estimates for cabinet ASP, software premium, BOM percentages, switch-chip margins, cable savings, cooling cost, and per-customer packaging shares are not company disclosures. They may illustrate engineering structure but cannot be used to reconstruct company gross margin or current customer allocation.
## 3. Dig into the mechanism (physics / business / geopolitics)

### 3.1 The platform-control layers all hold. A teardown is not a cost table

The object of this volume is not an "NVIDIA empire narrative." It is four surfaces of the same power. The system seller sells GPUs, cabinets, and interconnect. The software/runtime layer sets CUDA, NVLink, and the cabinet standard. The supply-coordination layer sets Hopper to Blackwell to Rubin, and the HBM / CoWoS / NVLink mix. The model player reaches: Nemotron / NeMo / NIM. The revenue bulk is still on cabinets. When the platform-control layers hold at once, the cloud war is not "four clouds versus one GPU vendor." It is buyers fighting an opponent that sets the rules, sets the mix, and ships models itself.

The sales unit has already moved from the chip up to the whole cabinet. One cabinet, 72 GPUs plus 36 Grace, is the product build, not a BOM price. Grace exists on the server side. That means they also do not want to leave this slice of CPU to a rival. A downgrade is not extinction. The profit center moved from general-purpose CPUs to accelerator cards. Automotive $1,694 million (frame-checked FY25) only says this slice is not the main line now. It does not say they have given up defining the server CPU. Consumer CPUs and whole PCs are not the currently disclosed main line: they may extend; there is no shipment and no revenue; do not invent one.

Backdoors / stolen training data are allegations. There is no public forensics. They do not enter the fact layer. What can be written is a privileged position: training has to pass their stack and their cabinet; they sit closer to the raw batch than any model firm. That is structure. If distillation happens, the mechanism looks more like "visibility on a compute path," and it would need an undisclosed channel in the chip, the driver, or the cluster software. There is no citable judicial or audit material yet.

### 3.2 Use the segment, not the BOM, for the revenue structure

Profit is not in the die, it is in the system. That direction can stay. What cannot hold that direction up is the $2.60 million to $3.30 million teardown table. The 10-K does not split die, HBM, CoWoS, Switch, copper, liquid cooling, and software premium that way. Single-switch-chip gross margin >85% has no matching segment filing. Software premium 40% to 45% is also not the reported counterpart of Compute & Networking. FY25 Compute & Networking $116,193 million is the neighboring segment. It contains interconnect hardware. It is not the "software tax" cell.

Gross margin fell from 75.0% to 71.1%. The company itself wrote an H20 inventory charge. It is not "the software premium has already collapsed." Q4 was back to 75.0%. After the charge, seller fat is still at this level. Profit cash is in [Volume 1](vol-01.en.md). Hypothesis from here: while the margin holds at this level, commitments keep rising. Anyone else who wants the same material pays more, or does not get it.

One-quarter operating-income scale against Intel is in [Volume 1](vol-01.en.md). Four-cloud scope is in [Volume 8](vol-08.en.md). Do not knock seller revenue against buyer capex. The report does not treat supply commitments as already having bought all advanced packaging. What can be written: cash has already gone out ahead of the slot. Some agreements can be rescheduled. Reschedule is not cancel. Q4 FY25 only says cloud-service providers were about 50% of that quarter's data-center revenue. There is no full-year split. Sovereign, enterprise self-build, and contract-manufactured cabinets are the other half. The system seller is still collecting. The software/runtime layer is still there.

### 3.3 Demand multiplies by cabinet. The binding line is packaging

What this volume can write is not a BOM dollar teardown. It is this multiplication: demand is cabinet count times 13.4 terabytes of high-bandwidth memory, not a FLOPs slogan. The estimate pool is in [Volume 16](vol-16.en.md) and [Volume 24](vol-24.en.md). Residual is in [Volume 5](vol-05.en.md). These are demand figures multiplied from a hypothetical cabinet count, not disclosed sales.

Q4 Blackwell $11.0B that quarter says the increment is already counted by whole generation, not by single card. Gaming cards themselves write limited supply. The consumer end is already giving way to the data center. Wafers, advanced packaging, and HBM feed the data center at 71.1% to 75.0% gross margin first. This is a public financial write-up. You do not have to wait for demand to peak, and you do not have to invent "how many tens of thousands of gaming cards have already been cut."

### 3.4 Cloud system stacks attack chips, interconnect, software, and rack economics while still sharing scarce upstream resources

The spec table is in [Volume 4](vol-04.en.md). This volume does not reopen it. Older BOM estimates suggested that the accelerator die was only one component of total rack cost, but those percentages and dollar values are not company disclosures. The durable point is that HBM, advanced packaging, interconnect, power delivery, and system integration all matter to rack-scale economics. Without stack and interposer quota, cloning one GPU still cannot assemble 13.4 TB. The BOM is not official. The direction matches the official spec: what public next generations themselves add is HBM, not a de-spec to commodity DRAM. About 820 mm² and H100's 814 mm² sit near the same reticle-limit band. They are not "small chips dodging packaging."

Die-level versus cabinet-level, and the two paths that once used commodity memory, are below in 3.8 and 3.9. The Samsung long is Tesla, not the four clouds, in [Volume 25](vol-25.en.md).

### 3.5 The software/runtime layer seat is an interface, not a 40% to 45% audited figure

CUDA 12.x, TensorRT-LLM, DOCA, PTX, and NVLink are products and documents that exist. With no replaceable intermediate representation and driver, earlier stress-test material's 40% to 45% does not automatically fall to the sum of hardware costs. That is mechanism, not share. From architecture common sense, PTX is CUDA's stable intermediate representation, the confirm that pins a high-level kernel to the NVIDIA pipeline. earlier stress-test material gives no PTX ISA version, opcode, or any compiler number. This volume cannot invent PTX detail, and it cannot write "covers 95% of frontier operators." Compute & Networking $116,193 million cannot be read as an irreplaceable software tax. CANN / self-designed ASICs / open-source models tearing the software/runtime layer open is the counter, not a fact already done. UXL / oneAPI are embryos. They have not dug through. Cheapness does not fill CUDA's tax. A 75% pad means it can also cut price.

The fabric turns 72 cards into one chip. That is the physical sentence of a system monopoly. 1.8 TB/s × 72 makes a 130 TB/s backplane, latency <100 ns, are earlier stress-test values. Unified memory lets a model firm write programs as "one giant chip," not as a distributed system. Older MFU-loss estimates on RoCE paths are not used as current measured facts. The mechanism that can stay: buying an Ethernet-card cluster to "replace GPUs" has to pass communication first. Older NVLink Switch tray prices and single-chip margin estimates are not segment disclosures and remain outside the fact layer. They are neither a GPU die nor general-purpose Ethernet. If a cloud ASIC keeps walking RoCE, it accepts the communication penalty. If it designs its own fabric, it also has to design a compiler stack that can eat the system premium. Both have to be done before you can say "training has been taken off the cabinet." Inference shunt alone is not counted as an interrupt by the judgment.

Short-reach copper can be a power and reliability choice inside rack-scale systems, but older 5,000-cable and 20 kW/rack estimates are not treated as first-party measurements. CPO and short-reach copper solve different distance, power, and reliability problems. Because the older 20 kW/rack saving, 7.2 Tbps figure, and 97.5% efficiency value are not backed here by a first-party test report, they remain outside the fact layer.

### 3.6 Asset-light against a heavy cabinet. The chokepoint is not the whole-system CM

NVIDIA capital-intensity comparisons use the current official cash-flow figures rather than older unchecked CapEx estimates. Four-cloud mixed-year scope is in [Volume 8](vol-08.en.md). Do not use "AI-specific $215B." Asset-light versus asset-heavy still holds: the seller sets its own Capex against the buyer group's Capex. NVIDIA leaves multi-year depreciation and 120 kW interconnection risk to the buyer, and keeps 71.1% to 75.0% gross margin for itself. No unsupported ODM assembly-dollar or percentage split is used in the current fact layer. What can choke NVIDIA on the supply chain is TSMC advanced logic and CoWoS quota, plus the three HBM makers, not the whole-system CM. What Dell, Lenovo, Quanta, and Foxconn can become is whole-system contract manufacturing (an Apple-to-Foxconn structure), not a wafer fab. That is a scenario, not an already-announced list.

Geopolitics: foundry and packaging in Taiwan, high-bandwidth memory in Korea, system definition at NVIDIA. Export control can change an accelerator's spec suffix. It cannot change the BOM structure. The official spec is still 13.4 terabytes of high-bandwidth memory plus advanced packaging. The China stack is in [Volume 12](vol-12.en.md).

### 3.7 None of the five interrupts is done

The five interrupts are in [Volume 8](vol-08.en.md). The docket is in [Volume 11](vol-11.en.md). The most direct interrupt for this volume is cloud-custom chips taking training away. Public next generations have not taken it away. They have walked into the same slice of material. See [Volume 4](vol-04.en.md). The window is the few years before the next first-to-market node is locked by commitments.


### 3.8 Die-level memory does not match cabinet-level demand. The direction is the same line

[Volume 4](vol-04.en.md) confirm memory per chip. The judgment confirm one cabinet. The spec table is in [Volume 4](vol-04.en.md). The two sets cannot be subtracted directly. The direction can still match. Die-level is tens to a bit over two hundred GB. Cabinet-level is the official NVL72 13.4 TB HBM plus 17 TB LPDDR. The gap is 72 packages and the fabric, not "the clouds have already replaced the whole cabinet with commodity DIMMs."

The 1.77 PB in the Ironwood software-stack write-up is a cluster total, not a single-cabinet control. Trainium3 UltraServer is written as cabinet-scale or super-cabinet-scale. The memory type is still HBM3e, not DDR5. What all four add is capacity and bandwidth, not a de-spec. This volume does not sum die-level GB into "how many cabinets cloud ASICs have already replaced." There are no shipments. A sum has no meaning.

Cabinet count times spec is in [Volume 16](vol-16.en.md). Residual is in [Volume 5](vol-05.en.md). These numbers only say: as long as whole cabinets still ship at this spec, high-bandwidth memory and commodity memory are both pulled away by the cabinet. If the clouds move inference at scale onto custom chips plus traditional fifth-generation double data rate, and stop bidding against NVIDIA for full HBM output, that is the only physical upside of this path. What they are adding, though, is the residual slice that is already rising. You can still buy it. The price is higher. Not a dead end. A tax. Public next generations have not chosen this path.

### 3.9 The two paths that once used commodity memory are both leaving

Among the four, the only two that officially admit they "used commodity-class DRAM" are these two, and both are walking toward HBM.

The first is AWS Inferentia. Generation one, 8 GB DDR4 per chip. Generation two, 32 GB HBM per chip, 4× capacity, 10× bandwidth. That is a generation change the company itself wrote on the product page. It proved "an inference chip can start on DDR." It did not prove "the next generation will retreat to DDR." The direction is leaving. The Trainium line wrote HBM from the start: Trainium2 96 GiB per chip, 2.9 TB/s, instance total 1.5 TB HBM3; Trainium3 written as first 3nm AWS AI chip, 144 GB HBM3e, 4.9 TB/s. The inference line left DDR4. The training line adds 3nm and HBM3e. Neither line has stopped at 5nm plus commodity DIMMs.

The second is Meta MTIA. The official table for the first two generations is TSMC 7nm / 5nm plus off-chip LPDDR5. That is the only generation among the four that officially admits "leading-edge logic + commodity-class DRAM" was once the mainstay. What it hit was ranking and recommendation, not a fight with Blackwell for training cabinets. The 300 generation names Broadcom from the start, writes HBM stacks, and writes HBM bandwidth as the most important factor for GenAI inference. The path is LPDDR5 walking toward HBM. Different chiplets can land on different nodes. The company itself writes most cost-effective. It does not write "the compute die retreats to 5nm, main memory retreats to LPDDR." Third-party paraphrase of a 3nm compute die / 5nm I/O is not promoted to an official sentence. What can be confirmed: once GenAI inference is the job, the company itself writes HBM as the most important factor.

Microsoft never walked a commodity-DRAM generation. Maia 100 was already 5nm plus HBM2E plus CoWoS-S. Maia 200 is written directly as N3 plus HBM3e. Google's public three-generation spec table has HBM in all three columns. Ironwood is written as HBM3E. So "retreat to 5nm plus DDR5" is not the path the four clouds are walking. It is a hypothesis the judgment allows and that no one is walking on a public page. Walking it would be dodging the scarce slice. Not walking it, the ASIC is still bidding against 71.1% to 75.0% gross margin.

### 3.10 Prepayments are reproduction. Buyer capex builds halls

Two hundred-billion checks are not the same thing. Profit cash and supply commitments are in [Volume 1](vol-01.en.md). Four-cloud scope is in [Volume 8](vol-08.en.md). The depreciation wall is in [Volume 30](vol-30.en.md). The seller presses cash already earned back into the scarce slice, so the next slot recognizes itself first. The buyer's check builds halls. Cloud-custom chips hit the die. They do not hit the cash used to prepay. If a breakout only replaces single-card FLOPs, bidding power stays on the margin side.

### 3.11 Booked 19% is not a safe distance. The increment has already tilted

TSMC's books are in [Volume 4](vol-04.en.md). Packaging tightness is in [Volume 24](vol-24.en.md). Booked 19% is not a safe distance. What is being opened is HPC and packaging. However large Apple is, it locks phone logic. The window is not waiting for the book to hit 50%. It is the few years before the next first-to-market node is locked by commitments. The parallel line now catching is Tesla, not the four clouds' cabinets. See [Volume 25](vol-25.en.md).

### 3.12 Gaming-card limited supply is system seller behavior that can be written today

You do not have to wait for demand to peak, and you do not have to invent "how many tens of thousands of gaming cards have already been cut." FY25 Gaming $11,350 million against data center $115,186 million (frame-checked). Q4 Gaming -11% year on year, -22% sequentially. The official sentence is limited supply for both Blackwell and Ada GPUs. Consumer cards and the data center bid for the same supply. The consumer end is squeezed. Mechanism: wafers, advanced packaging, and HBM feed the data center at 71.1% to 75.0% gross margin first. The system seller pulls supply from the low-margin item to the high-margin item. This is not a backdoor. It is a public financial write-up.

The siphon reaches consumer electronics, general-purpose servers, and phones bidding for the same kit, but "brand extinction" is marked a scenario. It does not name a bankruptcy. TSMC only admits CoWoS is tight and that packaging-and-test share is rising. There is no official allocation table proving rivals cannot get capacity. Gaming $11,350 million is still there. The consumer end is not an abandoned zero. What can be checked: whether later quarters still write limited supply; whether Gaming grows large again; whether consumer-notebook CPUs can still ship a non-NVIDIA option. If there is no number, leave it empty.

Professional cards take it on the chin. After the sales unit moved up, DGX / whole-cabinet reference designs have already moved OEMs from "defining their own product" to "assembling to a drawing." That is a rule change. It can be written. The report does not infer DGX / NVL72 shipments or whole-cabinet ASP as a share of revenue. What the Dells can become is whole-system contract manufacturing, not a wafer fab. Chip foundry is still TSMC.

### 3.13 To take training away, which pieces have to be done at once

The relevant substitution test is whether cloud system stacks take meaningful training as well as inference workloads. This volume splits that sentence with [Volume 4](vol-04.en.md). The inference shunt has already happened: Inferentia, Maia, TPU v6e, and the first two MTIA generations are all public products on the inference or recommendation side. Whether training has been taken away is not whether a self-designed chip exists. It is whether training still needs a high-bandwidth fabric, HBM, and advanced packaging, and whether compile still has to pass CUDA / PTX / the deploy stack.

On official pages, the training side has not been taken away. Trainium3 is written as 3nm plus HBM3e. Ironwood is written as 192 GB HBM3E; the software-stack write-up writes 1.77 PB directly addressable. Maia 200 is written as N3 plus HBM3e; the company main blog places it on inference; a deep look is still the same slice of material. The MTIA 300 generation adds HBM stacks for GenAI inference. No firm writes "training moves to 5nm plus commodity DDR5." No firm writes "training no longer needs advanced packaging." CoWoS share and TCO savings that third parties often write do not enter the fact layer.

All have to be done at once before it is an interrupt: the self-designed chip no longer queues the same CoWoS and the same class of HBM; the self-designed fabric no longer accepts RoCE's communication penalty, or accepts the penalty and still reaches an acceptable MFU in production; the compiler stack no longer leaves the switching tax on CUDA / PTX. If one of those layers remains dependent on the incumbent stack, substitution remains incomplete. Replacing only single-card FLOPS, bidding power stays on the 71.1% to 75.0% side. Prepayments keep rising. Anyone else who wants the same material pays more, or does not get it.

Power, a second global resource bid, and structural or interoperability remedies are additional system-level variables. See [Volume 8](vol-08.en.md), [Volume 13](vol-13.en.md), [Volume 11](vol-11.en.md). This volume does not open them. What the China stack can catch is people who cannot buy NVIDIA, not tearing global labs off CUDA. See [Volume 12](vol-12.en.md).


### 3.14 This volume does not collapse the platform-control layers into a single rent, and it does not start a counter-story

The platform-control layers holding at once does not mean the world's AI bill all enters NVIDIA's 10-K. FY26 data center $193,737 million is the rent the seller has confirmed, not global AI spend. Model-firm APIs, cloud-customer bills, application distribution, the grid, and China's sovereign stack do not automatically merge into this cell. CSPs about 50% of Q4 FY25 data-center revenue means half of that quarter was not these four clouds. Sovereign, enterprise self-build, and OEM cabinets: the system seller is still collecting, the software/runtime layer is still there. Volume 26 cannot be written as "only three labs × four clouds." Neither can this volume.

The other way: a buyer large enough does not automatically weaken the platform-control layers. Microsoft Intelligent Cloud $106,265 million, 2025 mixed-year four-cloud group capex about $354.0–356.5B, proves buyers can pay. It does not prove buyers, selling cabinets, can outbid 71.1% to 75.0%. If a self-designed chip still has to pass CUDA / PTX / the deploy stack, the software/runtime layer seat is still there. If training still needs a high-bandwidth fabric and HBM, the system seller's whole cabinet is still there. The public next generation read in [Volume 4](vol-04.en.md) is exactly the second sentence. Nemotron / NeMo / NIM exist. That is a reach of power: others train on its stack, and it sells adjacent model services. There is no revenue split. The report does not treat "models have become a second profit pool." The conflict with independent labs is structure: the software/runtime layer sets what can run, the system seller sells the cabinet needed to run it, and the model player then ships competing weights on the same stack. All three can be true at once.

So the teardown's conclusion is not "NVIDIA has already collected all the rent." It is "the allocation now visible is still walking past half of the scarce slice." It lands on the cabinet itself: spec times cabinet count is demand; public ASICs have not changed the spec; prepayments are still rising. The five are in [Volume 8](vol-08.en.md). Numbers only reuse the judgment, [Volume 4](vol-04.en.md), and what earlier stress-test material already had.

## 4. Scenarios, counterarguments, and testable indicators

New quantities are marked "unverified; do not treat as verified first-party fact."

Scenario A: the system premium holds. The next cabinet still writes the fabric and the compiler stack as irreplaceable interfaces. GAAP gross margin stays near 71.1% to 75.0%. Supply commitments keep rising. Public cloud ASICs keep writing HBM3e / HBM3E and 3nm. Testable: whether NVIDIA's gross margin leaves this band; whether supply commitments keep rising above $119.0B; whether each firm's official page keeps writing HBM, and does not write "mainstay inference uses DDR5 or LPDDR, no HBM." Unverified: do not forecast the endpoint of the premium percentage, and do not use the BOM's 40% to 45% as an official target.

Scenario B: cloud ASICs truly retreat to 5nm, use less packaging, and move to commodity DRAM. That is the path the judgment allows for dodging the scarce slice. The condition is that the clouds are willing to trade a lower performance tier for material. Public next generations have not walked it. If they do, this wafer slice is easier to grab than a 3nm first-to-market node, and TSMC is also willing to fill 5nm / 7nm utilization with ASICs (those two nodes are 36% plus 14% of wafer revenue). The cost is no longer comparing against today's cabinet. Testable: whether an official sentence appears, "mainstay inference retreats to 5nm + DDR5"; whether the next Maia / Trainium / Ironwood / MTIA tier cuts HBM and cuts advanced packaging. Unverified: do not forecast which year it is walked, and do not invent a TCO-savings percentage.

Scenario C: a copper-to-CPO power reversal. Cabinet power exceeds copper's reach and thermal envelope. earlier stress-test material's 20 kW advantage disappears. Switch and optics vendors cut away part of the interconnect. Testable: whether official cabinet power still writes 120 kW; whether copper cable count is still 5000+. 120 kW and 5000+ are both earlier stress-test values, not re-checked in this volume. Unverified: do not forecast CPO penetration.

Scenario D: buyers jointly press the software tax. Four-cloud mixed-year group capex is already about $354.0B. Depreciation will force a common compile layer. The switching tax moves from a change of vendor to a change of base. Testable: whether a framework appears that can port between NVLink and a self-designed fabric, and that can reach near earlier stress-test material's 60% MFU in production. Whether UXL / oneAPI move from embryo to a deployable production stack. Unverified: do not forecast which band the premium percentage falls to. 85%→55% has no sample. It is not a statistic.

Scenario E: power stops the buildout. If the power wall holds, the bottleneck list gains a utility. Silicon and packaging slots are dragged by the interconnection queue. Rack power around **120 kW** is supported by NVIDIA product documentation and is treated as a product-level engineering anchor, not a utilization forecast. Testable: whether four-cloud group capex slows for two years running because of power, not silicon; whether official text writes interconnection, not CoWoS, as the first constraint. Unverified: do not forecast which year the interconnection queue is digested.

Counter one: cloud buyers are large enough. Microsoft Intelligent Cloud $106,265 million, 2025 mixed-year four-cloud group capex already about $354.0B, can press system seller ASP by volume. The platform-control layers need not collapse into a single rent. Counter two: CSPs are only about 50% of Q4 FY25 data center. Sovereign and enterprise self-build dilute "the four clouds decide everything." Counter three: CANN / self-designed ASICs / open-source models tear the software/runtime layer open. Compute & Networking $116,193 million cannot be read as an irreplaceable software tax. Counter four: Gaming $11,350 million is still there. The consumer end is not an abandoned zero. Q4's limited supply may also return to gaming cards after supply loosens. Counter five: the BOM is an estimate range. The $2.60 million to $3.30 million sum may double-count or miss a line. It cannot be treated as NVIDIA's revenue-recognition unit price. Even using official 13.4 TB, you cannot back out whole-cabinet ASP. Counter six: Google and AWS latest-generation official pages do not name TSMC. There is a possibility they "have already left, or will soon leave, TSMC." This volume only writes "official pages do not name them." It does not write "already left," and it does not write "must still be there." Counter seven: some supply commitments can be rescheduled. $119.0B is not an irrevocable buyout. Counter eight: if CoWoS about 60% is forcibly spread by TSMC, NVIDIA's volume right is hurt before its pricing right. This is not a TSMC split. It is only sell-side research.

Testable; fill when there is a number:

- Whether data-center revenue is still growing at the FY26 $193,737 million scale, and whether growth falls to single digits; whether Q-level Blackwell / the next generation is still disclosed separately.
- Whether gross margin leaves the 71.1% to 75.0% band.
- Whether supply commitments keep rising, or walk back from $119.0B.
- Whether CSP share of data-center revenue is still near "about 50%," or a full-year split appears.
- Whether Intelligent Cloud and Azure growth move with four-cloud group capex.
- Whether Gaming keeps writing limited supply; whether packaging-and-test share crosses 10% as TSMC said.
- Whether each cloud's official page keeps writing HBM3e / HBM3E / 3nm; whether an official sentence appears, "mainstay inference uses DDR5 or LPDDR, no HBM."
- Whether NIM / models are disclosed separately. If not, leave it empty.
- OpenAI / Anthropic contracts: keep empty.
- Whether TSMC's first customer is still walking up near 19%, and whether HPC is still on the 58% / +48% increment.

## 5. Gaps and what this volume cannot write as fact

- "PTX assembly" in the title has no instruction, version, toolchain, or performance control in earlier stress-test material. This volume invents no PTX detail and does not write 95% coverage.
- The BOM is not a 10-K and not an NVIDIA official price list. Ranges and shares give no sampling method. Whole-cabinet ASP $2.60 million to $3.30 million, software premium 40% to 45%, single-switch-chip gross margin >85%, all stay "supply-chain estimates."
- The geometric relation of "144 Die" and "two dice about 1600 mm²" to reticle limit 858 mm² and 3.3× reticle is not derived step by step in earlier stress-test material. This volume does not invent a fake formula. B200 about 800 mm² and H100 814 mm² are public engineering numbers cited by the judgment. They cannot be used to back out BOM dollars.
- 7.2 Tbps, 97.5% power efficiency, single-chip gross margin >85%, the 20 kW save, MFU 60%→25%, latency <100 ns versus 1.5 to 3.0 μs, all have no test report kept in this volume.
- This volume did not independently verify a 10-K. FY26 numbers come from the judgment. FY25 point estimates come from the frame-checked set. If the 10-K restates, the 10-K wins.
- The report does not infer an NVIDIA revenue split by multiplying whole-cabinet ASP by an unknown shipment count. Do not treat $193,737 million and four-cloud capex as each other's payment proof.
- CoWoS monthly capacity 13k → 130k, NVIDIA exclusive 60%/70%, is not a TSMC split. 5.39 wafers per cabinet, 100k cabinets taking more than half the packaging line, are estimates, not TSMC's books.
- Google and AWS latest-generation official pages do not name TSMC and do not name Broadcom. Third-party TSMC N3P, Broadcom, and CoWoS share do not enter the fact layer. Meta's 300 generation does not name 3nm.
- No cloud was found saying it is retreating to 5nm plus commodity DDR5 as the inference mainstay. No official sentence was found saying "already left TSMC." Invent neither end.
- NVL72 dollars per cabinet, how many percent TCO an ASIC saves, how many percent of CoWoS Broadcom takes: the companies themselves do not say this on the pages listed in [Volume 4](vol-04.en.md). The report does not treat them.
- Samsung 16k / 24k / 40k wafers per month, CXMT 350k wafers per month, SMIC plus CXMT plus YMTC combined monthly capacity: no announcement. The report does not treat them.
- Microsoft becoming a software-and-games brand, hardware left only to NVIDIA: it conflicts with Intelligent Cloud $106,265 million. Delete. Sony thinning is another scenario.
- OpenAI / Anthropic compute contracts, reservations, revenue share: empty.
- A backdoor already happened: an allegation. It does not enter the fact layer.
- The four clouds will spend $670–750B in 2026: it cannot be added. Microsoft official guidance is missing. Keep the mark: unverified; do not treat as verified first-party fact.
- FY25 Capex $2.98B was not re-checked the current evidence review. Do not use it as a new anchor.

The sentence this volume can hold: the object of the teardown is the platform-control layers, not a BOM. The system seller's revenue is on cabinets. The software/runtime layer's interface is still there. The supply-coordination layer's prepayments are rising. Public next-generation cloud ASICs have not dodged 3nm and HBM. None of the five interrupts is done. Until they are, do not start a counter-story that "the clouds have beaten the system monopoly."
