# Volume 27: Agent-Native Software and AI Software Unit Economics

Chinese original: [vol-27.md](vol-27.en.md)

Cloud ASICs: [Volume 4](vol-04.en.md). Four-cloud mixed-year scope: `四云Capex口径核对.md`. This volume has no Salesforce or Adobe gross-margin sample. It does not write 85→55 as something that already happened.

## 1. Core question

AI-native software changes the cost structure of software because one user action can trigger repeated inference, retrieval, tool/API calls, storage, and human review. The relevant question is not whether every SaaS gross margin falls from 85% to 55%; those fixed endpoints have no representative sample and remain stress-test values.

The correct analytical object is **AI Software Unit Economics**:

```text
AI_Gross_Margin
=
(Revenue
- Model_Inference_Cost
- Retrieval_Storage_Cost
- Tool_API_Cost
- Human_Review_Cost
- AI_Specific_Cloud_Cost)
/
Revenue
```

A seat is no longer a sufficient statistic when usage depth varies materially across customers and workflows.
## 2. Evidence boundary

Historical versions used fixed SaaS-margin endpoints, mixed-year hyperscaler CapEx, and DeepSeek-derived engineering examples to illustrate cost pressure. Those figures are not direct disclosures of Salesforce, Adobe, ServiceNow, Microsoft Office, or another representative software cohort.

The current framework keeps only the mechanism:
- model calls create variable cost;
- retrieval, tools, and human review add additional variable cost;
- cloud and accelerator pricing influence COGS;
- workflow depth and routing/caching determine cost per completed outcome;
- pricing power and ARPU determine whether lower gross margin still produces a larger profit pool.

The old **85% → 55%** path remains a stress test, not an industry fact.
## 3. Mechanism: a seat is no longer a sufficient statistic

### 3.1 Seat pricing assumes low incremental delivery cost

Traditional seat software often carries high fixed R&D cost and relatively low marginal delivery cost, which can support high gross margins. Seat fees are weakly related to usage: the thousandth seat almost never adds inference. Agent-native software turns one click into a model loop that can run long: retrieve, plan, call tools, generate again. Each step is autoregressive decoding. It lands exactly in historical stress-test material's memory-bound zone. Cost of goods moves from storage plus an ordinary CPU to HBM bandwidth times seconds. The older 55% endpoint is not an industry median. The mechanism is that inference, retrieval/storage, tool/API calls, human review, and AI-specific cloud costs can move more expense into cost of revenue. 85% and 55% have no sample firm, no year, and no scope (GAAP or non-GAAP, stock-based compensation in or out). They cannot be treated as an industry statistic that already happened.

A shallow wrap, one summary button, can still sell by seat. A workflow product may be better priced by usage, task, outcome, or a hybrid structure rather than by seat count alone. historical stress-test material's ask of the enterprise side, "focus on workflows that produce commercial value directly," is an admission that a shallow wrap cannot carry the depreciation on the mixed-year two-hundred-billion side. Call depth, not whether there is an AI feature, is the physical core of the software-industry rewrite.

### 3.2 How depreciation reaches the software price list

Hyperscaler depreciation does not map one-for-one into a software vendor's cost of revenue. the cloud recoups depreciation with accelerator instance prices, token prices, or reserved commitments. A software vendor that embeds a model has three roads. Fold usage into the seat: the 85% look holds for a while, then heavy users arbitrage it. Surcharge by token or task makes variable inference cost explicit and can lower or stabilize gross margin depending on pricing power and usage. Park the model cost outside and let the customer bring their own key: the seat statement looks clean and the product difference is hollowed out. On any of the three roads, a seat is no longer a sufficient statistic. The lead writes 85% to 55% and $215B in one sentence. The chain is cloud depreciation, inference unit price hard to return to zero, seat-software margin structure rewritten. It is not "every software firm's reported gross margin is already 55%."

Microsoft cannot be written in this volume as the Office seat either. Intelligent Cloud $106.265B is cloud, not a desktop license. Model cost on desktop and coding-assistant products has no split in the current evidence review. The report does not infer one. A game console can thin. Intelligent Cloud will not. Four-cloud 2025 mixed year of about $354.0B is each acting alone, added up. It is not a bundled joint prepayment. Software firms face four price lists, not one industry inference price.

There is no public transmission coefficient. You cannot multiply $354.0B by a homemade ratio and write it as already allocated into seat-software cost of goods. What can be written is direction: halls enter PP&E first, then expense over each firm's useful life, then show up on the software firm's cloud bill as instance prices and token prices. Whether the bill enters cost of goods depends on whether the software firm books the model as its own product cost or as a key the customer brought. This volume has no such accounting split. Leave it empty.

### 3.3 Official cloud sentences: the models software embeds, the landlord itself writes as HBM

The source set confirms only the foundry and memory relationships that companies themselves disclose. Third-party node estimates, advanced-packaging shares, and percent TCO saved by a custom chip do not enter the fact layer. No first-party cloud source reviewed here states that next-generation inference systems are retreating to 5 nm plus commodity DRAM. If a software firm assumes models will get cheap enough to use without limit on a seat, it first has to pass these four landlords' own spec pages.

Official specs for the four: [Volume 4](vol-04.en.md). The search did not read a sentence that 5nm plus commodity DRAM is the inference mainstay. The software-industry rewrite is therefore not "models return to commodity DIMMs and the seat automatically restores." It is "cost of goods is confirm to the scarce slice; the price list must change." Switching clouds is not switching memory type. The bill header can move from one cloud to another. The memory spec page does not open a commodity-DRAM back door for software firms.

### 3.4 Physics: low-rank attention eases the memory wall. It does not delete call depth

Low-rank attention compresses KV 93.3% and lifts concurrency nearly 10×, historical stress-test values. Algorithms can ease the memory wall. They cannot delete it. If an agent on average walks several more loops than a single completion, compute burn can still cancel that 10×. : 93.3% is a dimension reduction of memory occupancy. It is not turning a workflow back into one copy. DeepSeek-V3's $5.576M is a pretraining conversion, not a software firm's token cost function. The comparison baseline has no sample. the current evidence review did not re-check the paper. What it can show is only that a training bill exists as a public self-report on the order of a million dollars; if it is widely copied, inference unit prices have downward pressure and the seat has room for a partial restoration. It cannot be written as "software cost of goods is already back to zero."

Institutional memory research: 51% of 2026 DRAM bits are already HBM plus registered DIMMs. Memory is 47% of major CSP capex in 2026 and 68% in 2027. Micron FY24 Q3 prepared remarks disclose that, industry-wide, HBM3E requires approximately **3× the wafer supply of DDR5** to produce a given number of bits in the same technology node; Micron's FY25 10-K later confirms that HBM requires more wafers and cleanroom space for the same bits. The ~3× ratio is A-grade first-party evidence, while still not being a universal fab-control constant. Hynix: HBM revenue more than doubled in a year. Channel talk: a 16G commodity DIMM from 450 to 1,800. Even if a software firm moves inference onto commodity DIMMs, the add lands on residual bits that are already rising. Commodity memory may remain purchasable while becoming more expensive; this is a unit-economics pressure, not proof of a software dead end.

### 3.5 Supply siphoning will pin software's end demand from the chip side

A flagship Snapdragon at $180 to $190, the application processor past 30% of phone BOM, replacement cycles past 40 months: historical stress-test values. New software entries on personal devices slow down. : if an agent can only run on the latest on-device NPU, penetration is dragged by the replacement cycle; if it mainly runs in the cloud, it walks back to the four clouds' cabinets and the interconnection queue. For comparison, the official GB200 NVL72 reference configuration is a ~120 kW liquid-cooled rack with 72 GPUs, 36 Grace CPUs, 13.4 TB HBM3E, and 17 TB LPDDR5X. Software vendors cannot assume user devices will keep up on their own. Gaming in Q4 FY25: down 11% year on year, down 22% quarter on quarter. Official reason: limited supply for two GPU generations. The consumer end is already yielding to the data center. The hardware base of on-device software competes with the cabinet for the same supply.

### 3.6 Geography: API lock-in is another tariff. The switching cost sits on the AI layer

historical stress-test material repeats "avoid proprietary API lock-in." : when a software firm's core difference becomes a closed model's system prompt and tool protocol, it outsources margin and compliance risk to the model firm and the cloud at once. If the protocol also has to pass a unified compute architecture or a deployment stack, the software/runtime layer collects a second rent. In-house models, frameworks, and inference-microservice lines exist. There is no revenue split. The second rent is written as structure, not as an amount. historical stress-test material writes software and brand premium as 40% to 45% of a cabinet. That is an estimate, not a segment filing. Do not promote it to a checked figure.

A domestic compile stack cutting open-source model migration rewrites to under 5% is a Volume 29 historical stress-test value. In another ecosystem, 'can migrate' is itself an engineering target. A 5% rewrite figure, even if verified, would measure code-change effort rather than full ecosystem switching cost. The software-industry rewrite is therefore not only pricing. It is also whether the base can be changed inside 90 days. Ninety days is a test window, not a measured duration. Open cross-architecture interfaces can reduce stack-switching cost, but current evidence does not show negligible migration across all frontier workloads. Limited portability weakens buyer leverage over both software and scarce hardware. If software firms each lock to one cloud's model protocol, the switching cost becomes a change of base rather than a change of vendor. The missing check is that one bind-into-one-stack payment.

China's parallel supply is stronger in smartphones and parts of consumer computing, while frontier-AI substitution still depends on advanced logic, HBM-class memory, packaging, interconnect, software maturity, and deployment scale. A software firm cannot expect that swapping in a domestic compiler moves cost of goods off the scarce slice. SMIC's foundry share of 5.1% cannot take Western masks. Samsung's $16.54B long (announced KRW 22.76T, through 2033) is Tesla. Musk named the Taylor plant for an automotive chip. It is not seat software's second inference river. 16k / 24k / 40k wafers per month are not in the announcements. CXMT's prospectus: 0 mentions of HBM. 350k wafers per month is not an announcement. Once the international price holds, makers sell first to the high bidder. If domestic software is deployed inside a restricted market, administrative policy can influence demand and resource retention, but it does not substitute for HBM-class supply or advanced packaging at scale. An administrative lock can keep a closed loop only if advanced packaging and HBM-class bits can already be produced at a volume that holds a training cabinet. If those frontier layers remain constrained, administrative protection alone cannot create an equivalent training-system stack.

### 3.7 Bidding: 71% to 75% pins machine-hours, not seat fees

Scarce-layer value capture: [Volume 1](vol-01.en.md). A software firm's seat fee, after the cloud price list, has a slice that becomes a bid for HBM and advanced packaging. Booked 19% is not a safe distance. If software's "AI attach" revenue really grows, the add lands on this slot, not on another 5nm river.

C.C. Wei, 4Q24: advanced packaging is tight and cannot meet demand. 2Q26: it limits customers' growth. Packaging and test about 8% of revenue in 2024, a bit over 10% in 2025. A $3M cabinet, custom silicon saving 40% to 60% of TCO: no company said so. The report does not treat it. Sell-side estimates put NVIDIA at about 60% of advanced packaging. That is not a TSMC split. Do not promote it to official exclusivity. The software volume does not need that allocation table to stand: the scarce slice is past half; the price list arrives later.

### 3.8 Prepayments lock next-generation machine-hours. The software price list comes after

Supply commitments $95.2B at FY26 year-end, $119.0B one quarter later, a three-month add of $23.8B, most of it due in FY27. Official text writes locking inventory and capacity. It does not split to TSMC or advanced packaging. Some agreements can be rescheduled. A software firm does not see this prepayment. It will see it 12 to 18 months later on instance prices and token prices. Twelve to 18 months is a mechanism window, not a disclosed lag. TSMC 2025: HPC 58% of revenue, up 48% year on year; first customer from 12% to 19%. A 19% annual customer revenue share is not a forward allocation guarantee. If software AI usage expands, its infrastructure demand competes for capacity that is already being reserved through long-duration commitments rather than for an unconstrained pool of depreciated legacy capacity.

TSMC 2025 wafer revenue: 3nm 24%, 5nm 36%, 7nm 14%, 7nm and below 74%. Five plus seven is half of revenue. That is revenue, not wafers. If the clouds really stop at 5nm and use less packaging, that wafer slice is easier to grab than 3nm first silicon. The path holds only if a cloud will trade a notch of performance for material and then sell cheaper machine-hours to software. Public next generations have not stopped. Microsoft's next, Amazon's fourth, Google's latest, Meta's 300 generation: all write HBM or 3nm. The physical anchor of software cost of goods is confirm by the landlord's own spec page.

### 3.9 Official inference-chip generation change is the control that software cannot still assume cheap DIMMs are enough

Amazon's inference chip publicly walked DDR4. The next generation did not walk back. It changed to HBM. What this volume confirm is the software meaning: if the seat's hidden assumption is that copy cost is near zero and inference bytes can land on ordinary memory, the company itself crossed that assumption out. 4× capacity and 10× bandwidth are not marketing adjectives. They are the spec gap from 8 GB of ordinary memory to 32 GB of HBM. A software firm that prices from the first-generation inference chip's cost function will mis-price cost of goods on second-generation inference and fourth-generation training. Fourth-generation training then writes the first 3nm chip and 144 GB of HBM3e, 20.7 TB on the ultraserver. The direction walks one way.

Meta's first two generations of LPDDR are the exception, not the retreat. They hit ranking and recommendation. From the 300 generation the company writes HBM bandwidth as the most important factor for generative inference. If the software embeds a generative workflow, it matches the 300 generation. It does not match 64 GB of LPDDR. The only generation among the four that officially ran leading-edge logic plus commodity-class memory as a mainstay has already been turned by the company itself. Ranking can still use commodity-class memory. Generative workflows are not written that way by the companies. If seat software writes a ranking button and a generative agent as one cost function, it stacks two layers. This volume keeps them apart.

### 3.10 Each cloud's own capex is not a common price list for the software industry

Microsoft FY25 purchases of property and equipment $64,551M; Amazon CY25 net $128,320M; Google CY25 $91,447M; Meta CY25 equipment $69,691M, company figure $72,215M. Those four lines prove halls are being built. They do not prove software firms face one industry inference price. Amazon includes fulfillment. Meta includes other labs. Google includes other technical facilities. A group-wide line cannot be written as an AI split, still less as already allocated into a CRM vendor's cost of goods. By August 2026, all four hyperscalers had public scale indicators, but their windows still differed: Microsoft calendar-2026 CapEx expectation around $190B, Alphabet $180–190B, Meta $125–145B, and Amazon about $169B of TTM net PPE purchase. These figures still cannot be mechanically summed into one official AI-hardware CapEx total. Keep that line unverified. If a software firm stress-tests 2026 cost of goods against $670B, the base is invented.

Seller revenue cannot be crossed against buyer capex. FY26 data center $193,737M is not "the four clouds paid NVIDIA the $211.9B." Q4 FY25 only says CSPs were about 50% of that quarter's data-center revenue. That quarter's data center was $35,580M. There is no full-year CSP split. Of the models software embeds, half the machine-hours may not sit on these four clouds. Sovereign and enterprise buildouts still pass the stack. They still pay HBM. The physical reason the seat dies does not depend on the cloud brand. It depends on whether decoding still lands memory-bound.

FY26 NVIDIA Data Center revenue of $193.737B is a major seller-side value-capture anchor, not a measure of all global compute spending. Software-seat economics can still inherit infrastructure cost through inference, memory, and platform switching even when the end user never buys a GPU directly.

### 3.11 Switching clouds is not switching rivers: public next generations are still on the same slice

Third parties often write Google as some foundry plus some designer, and Amazon's fourth generation as some foundry at some node. The source does not write those two as foundry Google or Amazon themselves named. What can be confirm is memory type, and the foundry Microsoft and Meta named. The software volume does not need a foundry name to stand: public next generations run on HBM. To beat today's high-end accelerator you return to 3nm, HBM, and advanced packaging, and you bid against 75% gross margin. A real retreat to 5nm and less packaging is what would dodge the scarce slice. Public next generations have not stopped. Software cost of goods therefore has no second river to move to.

### 3.12 Two switching-cost layers: model protocol and compile/runtime stack

The first switching-cost layer sits on the model protocol. Software makes its difference a closed model's prompt, tool protocol, and retrieval wrap. Margin and compliance are outsourced together. Changing models is not changing an interface file. It is changing the workflow graph, the evals, and the safety review. The second switching-cost layer sits on the compile/runtime stack. Training and high-quality inference default to one intermediate representation and one deployment stack. Each cloud custom chip has its own stack. Changing stacks is a switching cost, not zero cost. The judgment writes binding software into one stack as an interrupt condition. It is not done. Small and mid-size software firms cannot keep four compile-and-debug stacks. They continue to bear switching and integration costs when relying on the mature stack. This is the broad form of platform switching cost: it is not necessarily paid to NVIDIA, but it is paid to whoever can compile the model onto HBM.

### 3.13 The three bundle checks: the software check is still empty

Changing allocation requires several mechanisms to improve together: Prepayments large enough that one buyer cannot be the only name recognized; software bound into one stack, so the switching cost becomes a change of base rather than a change of vendor; memory longs that force makers to leave a line for commodity bits. If one remains weak, bargaining power and portability remain limited. Four-cloud 2025 mixed year of about $354.0B is each acting alone, added up. It is not a joint prepayment. Software firms each signing an exclusive model protocol is splitting the second check as well. TSMC allocates incremental capacity using multiple commercial and strategic criteria; large prepayments and long-duration demand can strengthen a buyer's position without guaranteeing allocation.

The five interrupts: the judgment and [Volume 8](vol-08.en.md). The case file: [Volume 11](vol-11.en.md). The switching cost does not fall on its own because an inquiry exists.

### 3.14 A private cabinet does not return cost of goods to zero

The counter often says: regulation or enterprise security keeps data on a private cabinet, software becomes license plus professional services again, and the margin path is entirely different. What holds: the statement line moves from cloud inference cost to own depreciation and professional services. What does not hold: four-year hardware depreciation does not vanish, and the HBM queue is not cancelled. A private cabinet still wants a fabric on the order of 72 accelerators, still wants a spec on the order of 13.4 TB of HBM, still has to pass advanced packaging. The sales unit has already moved from the chip up to the cabinet. If software follows the cabinet into the hall, it sells license plus implementation, not a zero-marginal-cost copy. Gross margin may no longer sit near 85%, and it need not land on 55%, because the cost function of professional services and the token fee are not the same table. This volume has no software-revenue sample on private cabinets. It gives no median. What can be tested: which of license, professional services, and cloud inference is rising in the enterprise IT budget.

## 4. Added analysis (scenarios, counters, testable marks)

New quantities: unverified. Do not treat as audit fact.

Scenario A: a seat shell plus a usage core. The old brand keeps the seat. What actually earns is the task pack and excess inference. Reported gross margin may decline, remain stable, or recover depending on usage depth, pricing power, routing efficiency, and cost per completed outcome. Test: whether software 10-Ks split "AI attach" revenue and related cost; whether margin guidance stops holding the historic high.

Scenario B: agent-native new vendors charge by outcome and old seat software is hollowed out. The workflow is done by the model firm or the cloud. Middle-layer software loses the seat. Test: which line is rising in the enterprise IT budget, software licenses or model / cloud inference. Unverified: this volume gives no 2030 share.

Scenario C: high-cost models are cleared, inference unit prices fall, the seat partly restores. If DeepSeek-class $5.576M training and 93.3% KV compression, historical stress-test values, are widely copied, token cost falls, software cost of goods falls, and gross margin can recover as cost per completed outcome falls. Test: cloud accelerator rent and public API prices; whether software firms raise long-term seat discounts again; whether cloud official pages still write HBM. All four write it now.

Scenario D: the switching cost locks software to one cloud's model protocol. Test: whether the base can be changed inside 90 days; whether an open interface moves from embryo to default intermediate representation; whether inference microservices are disclosed on their own. No split, no second-rent amount.

Counters. First: 85% and 55% may only be rhetorical ends, not an auditable industry median. Second: platform seat software owns the data and the workflow graph; the model is a plug-in; the seat can live through this round. Third: if regulation or enterprise security keeps data on a private cabinet, software becomes license plus professional services again and the margin path is entirely different; see 3.14. Fourth: if an official inference mainstay that retreats to commodity memory actually appears, the physical anchor of cost of goods has to be rewritten. No such first-party commodity-memory inference-mainstay shift is used in the current evidence base. Fifth: cloud buyers are large enough. Intelligent Cloud $106.265B, 2025 mixed year about $354.0B, can press machine-hour prices with volume. That does not automatically make the seat a sufficient statistic again.

## 5. Gaps and what cannot be treated as fact

85% and 55% have no sample firm, no year, and no scope. They cannot be treated as an industry statistic that already happened. This volume has no Salesforce, Adobe, ServiceNow, Microsoft Office, or other software-vendor revenue or gross margin. The report does not infer them. Model cost on desktop and coding assistants has no split. The report does not infer one. "$50B-plus of hard depreciation hits seat software" is a lead sentence. It gives no coefficient from four-cloud depreciation to software cost of goods. $45B to $55B is a template, not a sum of the four firms' 10-K asset classes. The DeepSeek block was pasted into this volume in full. It has no direct data interface to seat pricing. DeepSeek-V3's $5.576M figure is treated only as the paper's formal-training rental conversion, not a complete R&D cost. The "more than 85%" comparison baseline has no sample. Nearly 10× concurrency gave no test set. "Agent mature period" is ten-year stock language, not a forecast of software recurring revenue. Unverified. Do not treat as audit fact. Percent TCO saved by a custom chip, a $3M cabinet, exclusive packaging rulers: do not write them. No official Google sentence naming TSMC was found. No official Amazon sentence that TSMC foundries it was found. No Meta 300-generation sentence naming 3nm was found. Leave those three empty. Lab compute contracts, reservations, and splits: do not invent them. Inference microservices have no split. The report does not treat a second-rent amount. Four-cloud 2026 $670B to $750B cannot be added. It does not enter a stress-test base.
