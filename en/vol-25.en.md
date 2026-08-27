# Volume 25: Hyperscaler System-Stack Competition

Chinese original: [vol-25.md](../vol-25.md)

Cloud-system specifications: [Volume 4](vol-04.en.md). System-stack framework: [Core concepts and models](../核心概念与模型索引.md). Four-cloud accounting scope: [Volume 8](vol-08.en.md) and `../四云Capex口径核对.md`. The question is no longer "GPU die vs ASIC die," but whether clouds can organize chips, interconnect, software, racks/pods, and real workloads into durable substitute systems—and whether those systems still depend on the same advanced logic, HBM, packaging, and power.

## 1. The question this volume answers

Can the four clouds' CapEx and in-house accelerators weaken NVIDIA at both the compute and platform-rule layers? The upgraded question is: **can one system stack substitute for another system stack while both still compete for advanced logic, HBM, packaging, and power?**

This volume separates group-wide CapEx from "AI-only" spend, tracks foundry and memory choices, checks whether any public roadmap retreats to 5nm + commodity memory, and asks how far the clouds' counterattack has moved from chip definition into interconnect, compilers, runtimes, racks/pods, and deployment scale.

Public next-generation cloud systems do not retreat to cheap commodity hardware: Microsoft, Google, Amazon, and Meta are moving toward 3nm-class logic, HBM, higher-bandwidth interconnect, and larger system units. Samsung's KRW 22.76T long contract is a Tesla line, not disclosed capacity for the four clouds. China can build parallel supply in smartphones and parts of consumer computing, but it does not yet offer an equivalent frontier-training combination of advanced logic, HBM, advanced packaging, interconnect, and mature software. Third-party node estimates, packaging shares, and total-cost savings remain outside the fact layer unless independently sourced.

## 2. Accounting and evidence boundary

Cloud CapEx is company-wide capital investment, not a clean "AI accelerator" line. Mixed-year 2024 equipment purchases are roughly **$211.9B–$213.9B**, while the 2025 mixed-year level is roughly **$354.0B–$356.5B**. These figures use different fiscal windows and company definitions and must not be converted into a single official "AI hardware" total.

Likewise, unverified cabinet ASPs, fixed in-house TCO savings, monthly wafer counts, or point estimates of software premium do not enter the fact layer. The analysis focuses instead on observable system-stack components, actual CapEx line items, first-party product specifications, and clearly graded institutional estimates.
## 3. Mechanism: system-stack substitution and upstream resource competition

### 3.1 Accounting: capex becomes depreciation first, then a compulsion to fill utilization

The mixed-year CapEx totals are not current-period expenses. Hardware, buildings, network, land, and power assets enter depreciation on different schedules. Microsoft FY2025 net income was **$101.832B** and property-and-equipment additions were **$64.551B**, demonstrating strong buyer-side capital capacity. NVIDIA's seller-side cash flow and supply commitments have a different economic role: they can be directed more directly toward inventory, manufacturing, and next-generation capacity reservation.

Intel in 1999: revenue $29.389B, net income $7.314B, gross margin 59.7%. That was CPU share. Today NVIDIA has about $96.6B of annual free cash flow and FY27 Q2 operating income of $63.734B. TSMC 2025 gross margin was 59.9%; Hynix operating margin 49%. Buyer and seller margins are not directly comparable. The allocation mechanism is broader: price, order scale, prepayment, customer credit, utilization, and next-generation roadmap certainty all matter. If the leading platform remains strongest across those variables, incremental resources have an economic incentive to tilt toward it; suppliers still value customer diversification, geopolitical resilience, and long-run bargaining power. The historical 19% TSMC revenue share is therefore not a safe-distance metric, but neither is allocation a one-customer rule.

Buyer CapEx and seller supply commitments must therefore remain separate accounting objects. The relevant question is not simply who has more cash, but how directly that cash can be converted into scarce-resource reservation, system deployment, and workload utilization.

### 3.2 The four official spec sheets are not reopened in this volume

Foundry and memory sentences for the four firms: [Volume 4](vol-04.en.md). This volume does not reopen the spec table. It only takes apart which layer the in-house chip stops on, and whether Samsung's long contract is a four-cloud diversion.

Meta's first two generations are the official sample that recommendation ranking used: TSMC 5nm plus off-chip LPDDR. They did not have to bid for full-output HBM from the first day. Once the job became generative inference, the same company wrote bandwidth as the most important factor and publicly added memory stacks. Recommendation can stop on commodity-class memory. Generative cannot. The cloud war this volume discusses has its main battlefield on training cabinets and generative inference, not recommendation ranking. Using the first two generations to prove "a retreat is possible" is the wrong battlefield.

### 3.6 Decompose in-house systems into five layers

"In-house" must be decomposed into at least five layers:

1. chip definition;
2. compiler, runtime, and framework;
3. scale-up/scale-out interconnect plus rack/pod;
4. foundry, advanced packaging, and HBM physical supply;
5. enough internal workload and deployment scale to turn a cost advantage into platform power.

A breakout that stops at chip definition is insufficient. But 2026 reality is already further along: Google, AWS, Meta, and Microsoft are building parts of their own interconnect, software, rack/pod, and deployment layers.

The accounting still has to be split. NVIDIA Data Center revenue is seller-side value capture; four-cloud group-wide CapEx is buyer investment. In-house systems can **increase upstream competition for advanced resources** while simultaneously **diverting platform profit and software control away from NVIDIA**. Those two effects are not contradictory and must not be collapsed into "crowding only."

Public frontier roadmaps still return to advanced logic, HBM, high-speed interconnect, and large-system deployment. The relevant allocation question is not "75% margin automatically wins every bid," but which buyer can combine price, long-duration demand, prepayment, credit quality, and roadmap certainty while maintaining a viable platform. FY27 Q2 operating income of $63.734B strengthens NVIDIA's position; it does not make alternative system stacks economically impossible.

### 3.7 Samsung's long contract is not evidence of a four-cloud foundry shift

Samsung's long contract should not be treated as evidence that the four hyperscalers have shifted their frontier systems to Samsung. The announcement text is KRW 22.76T, about $16.544B, from 24 July 2025 to 31 December 2033. The counterparty is written as a large global company, about 7.6% of Samsung's then-expected 2024 revenue. The announcement does not write Taylor, does not write monthly wafers, and does not write Tesla. That day Musk named the Texas Taylor fab for the sixth-generation automotive chip; the fifth generation was then said to be TSMC, Taiwan first and then Arizona. Later industry notes wrote that Taylor 2nm had already taped out; the post was then deleted. Volume targets still mostly sit in the second half of 2027. 16k, 24k, and 40k wafers per month, and another $14.5B to $20B on the sixth generation, are not in a Samsung or Tesla announcement. They do not enter the fact layer. A 55% 2nm yield is not official. It does not enter the fact layer.

Samsung foundry share in 2026 Q1 was 6.5%, with TSMC still dominant. Samsung's long contract demonstrates that a second advanced-foundry route can exist for a specific customer and workload; it is not evidence that Microsoft, Google, Amazon, or Meta have already shifted their frontier cloud systems to Samsung. SMIC supports substantial domestic and mature-node supply, but export controls, process capability, advanced packaging/HBM, software, and customer qualification mean it is not yet an equivalent foundry path for Western frontier training systems. The correct conclusion is **concentrated leading-edge supply with limited parallel sources**, not "only one company can ever manufacture advanced AI logic."

### 3.8 No sentence was found that says "retreat to 5nm plus commodity memory as the inference mainstay"

The search result is in [Volume 4](vol-04.en.md). This volume does not reopen it. The direction that was read is the opposite. To beat today's cabinet you return to 3nm, HBM, and advanced packaging. Public next-generation parts have not stopped.

### 3.9 Depreciation capacity freed on 5nm is a hypothesis, not a product roadmap

In TSMC's 2025 wafer revenue, 5nm is 36% and 7nm is 14%; 5 plus 7 is half. That is revenue, not wafers. As Apple, Qualcomm flagships, and NVIDIA walk to 3nm and 2nm, 5nm lines will free depreciated capacity. If the clouds truly stop at 5nm and use less advanced packaging, that wafer slice is easier to grab than 3nm first silicon, and TSMC is also willing to fill utilization with in-house chips. The sources and the judgment both write this sentence as "the only physical benefit that can dodge the scarce slice." Public products have not taken it.

The condition for that road is that the clouds are willing to trade a notch of performance for material. Public next-generation parts have not stopped. Microsoft wrote the second generation directly as 3nm. Amazon wrote "first 3nm" into the product name. Google wrote eight stacks of HBM3E into the software stack. Meta wrote bandwidth as the most important factor. None of the four says on an official page: we are preparing to hit the inference mainstay with 5nm plus commodity DIMMs. A hypothesis can be written. A product cannot be written as already happened.

A real retreat still adds load onto residual DRAM supply. 51% of 2026 DRAM bits are already HBM plus registered DIMMs. Memory as a share of major cloud capex is written by the institution as 47% in 2026 and 68% in 2027. Micron provides first-party evidence that, at the same node and bit capacity, HBM3E requires roughly **3× the wafer supply of DDR5**. Hynix writes that HBM revenue more than doubled in a year. Channel talk, 16G commodity DIMMs from 450 to 1800, is not an annual report. It only says residual DRAM supply are rising in price. If the clouds move inference at scale onto in-house chips plus traditional commodity DIMMs: they no longer bid against NVIDIA for full-output HBM, which is that road's only physical benefit; but what they add load onto is the residual already rising in price, and phones, PCs, and ordinary servers bid together; they can buy it, at a higher price. It is not a dead end. It is a tax.

Monthly-capacity splits among the three majors, HBM at 22% to 25% of wafer starts, Samsung cutting 80k wafers per month back from HBM, CXMT at 350k wafers per month already matching Micron: none of that is in a maker filing or an annual report. It does not enter the fact layer. CXMT's prospectus points at conventional memory. Once the international price holds, it sells first to the high bidder. It can pull some low-end demand off consumer disks and let the three majors leave leading-edge nodes for server DIMMs. That is a reallocation of residual DRAM supply. It is not a unconstrained commodity-memory pool opened for cloud in-house chips.

### 3.10 The cabinet spec says which river the demand sits on

Official rack: 72 GPUs, 36 host processors, 13.4 TB HBM, 17 TB LPDDR. The 10,000 / 30,000 / 50,000 rack HBM totals are scenario arithmetic, not shipment counts. The report's 5.39 CoWoS wafers-per-rack coefficient is a **D-grade geometry estimate** used only for pressure testing. TrendForce's estimate that NVIDIA represents more than 60% of CoWoS demand is **B-grade institutional evidence**; TSMC does not publish the customer split. The report does not combine 5.39 with the entire foundry wafer pool or promote it into a disclosed capacity share.

If cloud in-house chips keep writing HBM, they walk into the same demand river of their own will. Microsoft's 216 GB, Google's 192 GB, and Amazon's 144 GB are not "another kind of memory." They bid against the 13.4 TB cabinet for the same class of stack. What in-house chips can change is who writes the spec and who collects the software/platform profit. What they cannot change is that the stacks still have to be built by Hynix, Micron, and Samsung, and packaging still has to be slotted by someone.

### 3.11 A domestic grid does not save this volume's foundry question

China's stack: [Volume 12](vol-12.en.md). China's parallel stack does not currently provide an equivalent foundry path for the four Western hyperscalers' frontier systems.

### 3.12 The conditions that would interrupt are not done

A credible counterweight to concentrated allocation requires several mechanisms to improve together: stronger long-duration purchasing power, lower cross-stack switching cost, and more diversified memory and packaging supply. In-house systems can divert platform profit while still competing for the same HBM, advanced logic, packaging, and power. The key test is whether those upstream dependencies materially decline.

## 4. Scenarios, objections, and testable checks

Scenario quantities remain conditional and do not enter the fact layer.

First scenario: the four clouds keep walking onto 3nm and HBM. Microsoft's second generation, Google Ironwood, and Amazon's third-generation training chip ship to the official specs. They bid against NVIDIA for the same slice of packaging and stacks. Testable: whether each firm still writes HBM3E on official pages; whether TSMC packaging-and-test share is still above 10%; whether supply commitments still rise from $119.0B. Do not forecast any firm's wafer shipments in any year.

Second scenario: one firm truly retreats to 5nm plus commodity memory as the inference mainstay. That is the only physical benefit that interrupts the scarce slice. It no longer cuts against full-output HBM, but it adds load onto residual server commodity DIMMs already rising in price. HBM plus registered DIMMs already take more than half of 2026 DRAM bits. They can buy it, at a higher price. Testable: whether an official sentence appears that says "the inference mainstay uses commodity DIMMs or LPDDR, not HBM." None is found now.

Third scenario: Samsung turns the Tesla long contract into a second leading-edge logic river, and the four clouds still do not cross. $16.5B locked through 2033 serves automotive AI. Testable: whether a Samsung announcement names a second cloud customer; whether four-cloud official pages write Samsung as foundry; whether Musk's oral line changes. Monthly wafers are not in an announcement. Do not use oral wafer counts as a test.

Fourth scenario: buyers press the seller with prepayments and in-house chips at the same time. Microsoft Intelligent Cloud revenue is large enough to fund in-house chips and buy cabinets together. Funding both is not the same as outbidding 71%. Prepayments are reproduction. Property and equipment are halls. The two sums sit on different accounts. Testable: whether NVIDIA's gross margin leaves the 71% to 75% band; whether supply commitments slow.

Write the objections in full. First, Google and Amazon official pages do not name TSMC. "All at TSMC" cannot be written as something the four firms themselves admitted; industry notes that write about 90% of sub-7nm at TSMC are not an annual report. The direction is right. The precision is not enough. Second, Amazon's first-generation inference used ordinary memory, and Meta's first two generations used LPDDR, which proves the clouds were willing to use commodity-class memory and later moved off it; it cannot be written as "the clouds never used ordinary memory." Third, Microsoft cloud revenue is large enough to fund two stacks at once. A 75% gross margin does not necessarily win every bid. Fourth, recommendation ranking can stop on LPDDR. Success at recommendation cannot be written as a breakout on training cabinets. None of the four objections denies "public next-generation parts have not retreated to commodity DIMMs."

## 5. Gaps and what cannot be written as fact

This volume did not open annual-report originals page by page. Mixed-year capex comes from cash-flow statements read in the scope check. Google and Amazon's latest generations do not name a foundry. That cannot be written as already having left TSMC. Samsung's $16.5B announcement does not write Tesla. Tesla is Musk's oral line. Monthly wafers are not in the announcement. There are no four-cloud in-house shipment, wafer, or packaging-wafer counts. No official sentence was found that retreats to 5nm plus commodity DIMMs. If it is not found, write that it was not found. The report does not infer a sentence that a retreat already happened. earlier stress-test material $215B, the Microsoft range, and $45B to $55B of annual depreciation stay demoted. Cabinet unit price, in-house total-cost savings, and Broadcom's packaging share are not sentences the companies themselves said on product pages. The HBM tonnage on 10,000, 30,000, and 50,000 cabinets is the judgment's hypothesis from the official single-cabinet spec. It is not shipments. TSMC's 2026 16 million to 17 million wafers is an outlook. Channel-talk commodity DIMM prices are not an annual report. This volume does not write sell-side Broadcom shares or in-house-alliance shares as a TSMC disclosure. Where an official TPU node or capacity disclosure is unavailable, the quantity remains unfilled rather than inferred. CXMT monthly capacity and a domestic three-firm sum do not match official figures. They do not enter the fact layer.

The current conclusion is narrower and more durable: hyperscalers can divert NVIDIA platform profit by building their own system stacks, but public next-generation systems still rely heavily on advanced logic, HBM, high-speed interconnect, and large-scale deployment. This means system-stack substitution can strengthen **upstream resource competition** even as it weakens NVIDIA's platform share. China's parallel supply is stronger in smartphones and parts of consumer computing, while frontier-AI substitution still depends on advanced logic, HBM, advanced packaging, interconnect, software maturity, and deployment scale. New first-party disclosures should update this conclusion.
