# Volume 06: Model-Company Unit Economics, Algorithmic Efficiency, and Open-Source Competition

Chinese original: [vol-06.md](vol-06.en.md)

Cloud ASIC specs: [Volume 4](vol-04.en.md). The two attachments of model firms: [Volume 26](vol-26.en.md). This volume does not reopen a spec table. It only writes this: MLA and a million-dollar training bill change the HBM demand function. They do not cancel the cabinet, and they are not a commercialization dead end.

## 1. Core question

How do algorithmic efficiency, open weights, cloud system stacks, and infrastructure cost change the bargaining power and unit economics of model companies?

Model companies do not control every physical layer of the stack, but by 2026 they are no longer merely thin API tenants either. Long-duration commitments such as Stargate and Anthropic/AWS show that frontier labs can become **Anchor Compute Buyers**. At the same time, open-source and algorithmic efficiency can reduce compute required per delivered capability and compress API pricing.

The relevant question is therefore not “open source kills model companies” or “only the most expensive rack can produce intelligence.” It is whether a model company can convert capability into durable workflow revenue while controlling enough of its compute, migration, and infrastructure economics.
## 2. Official and institutional sources

### 2.1 Roofline, MLA, and DeepSeek: what current evidence supports

DeepSeek-V3 provides a first-party anchor of **671B total parameters**, **37B activated parameters**, **14.8T pretraining tokens**, and **2.788M H800 GPU-hours** for formal training. The report-side rental conversion at $2/GPU-hour is approximately **$5.576M**, explicitly excluding prior research and ablations.

DeepSeek-V2 separately reports a **93.3% KV-cache reduction** and up to **5.76×** peak generation throughput versus its stated baseline. Those V2 figures must not be mixed into V3 as if they were the same experiment.

The durable mechanism is that low-rank attention, MoE, routing, caching, and systems optimization can materially change compute and memory demand per useful workload. They do not eliminate HBM, interconnect, packaging, or power constraints.
### 2.2 Four-cloud ASICs, capex, profit, and the TSMC increment

Specs: [Volume 4](vol-04.en.md). Four-cloud capex scope: [四云Capex口径核对](四云Capex口径核对.md). Profit and prepayments: [Volume 1](vol-01.en.md). Booked 19%: [Volume 4](vol-04.en.md). This volume does not reopen them. No cloud was found saying it is going back to 5nm plus commodity DDR5 as the inference mainstay.

## 3. Push the mechanism forward

### 3.1 Open source thins the API premium, not the cabinet

Hypothesis from here, not a veto. DeepSeek's technical-report evidence weakens the assumption that frontier capability necessarily requires the same compute budget structure across all model architectures. Once weights are open, inference price is competed down toward the clouds' marginal power and depreciation. If model firms keep collecting software-grade margin by seat or by token, they hit the introduction's 85% to 55%: the real cost structure is already four-year server depreciation, not the near-zero marginal cost of copying software.

Physically, the commercial bind comes from roofline. Whoever compresses per-token KV from 8192 to 512 releases nearly 10× concurrency on the same HBM. The 72-card cabinet's 130 TB/s backplane is still worth money, but the way it is worth money changes from "it has to be this large to hold the context" to "the same context can serve more sessions." HBM still eats more wafers than commodity bits. The model layer is changing the HBM demand function. Changing the demand function is not cancelling the supply constraint. Concurrency goes up, token unit price goes down, cabinets are still bought. Only the recovery function changes.

Commercially, open source splits "can afford to train" from "can sell dear." $5.576 million and 2.788 million GPU-hours (historical stress-test values) hit the entry ticket, not full cost. Data, alignment, inference inventory, failed experiments: historical stress-test material does not write them. Even if full cost is still tens of millions of dollars, that does not deny the bracket "entry is no longer hundreds of millions." The old closed-API method held premium with parameter count and eval scores. Open source put total parameters, active parameters, and the training bill on the same technical report. That takes the right to define "good enough" out of the lab budget's hands.

The clouds sit in a tighter twist. They are the model firms' landlord, competitors with in-house models, and they still have to prove on TPUs, Trainium, and Maia that they can buy less NVIDIA. The closer depreciation gets to historical stress-test material's annualized $45B to $55B (unverified), the harder the top-layer premium covers the landlord's capex, and the more model firms look like "independent software that raises cloud utilization." The only live path is embedding the model in a workflow: customers buy the result, not the token. The dead-end condition is equally clear: if volume stalls and unit price falls again, a pure API is not a business that can hold software-grade margin. This volume does not pick a branch.

The other face of the open-source game is ecosystem lock. Open weights do not automatically lift a unified compute architecture, intermediate ISA, or high-speed-interconnect semantics. An open model that nearly 10×es concurrency on an 8-GPU server may still only run that 10× to the full inside NVIDIA's unified-memory story. So the "dimensionality cut" hits closed-API price. It does not necessarily hit the cabinet's software premium. What would hit model and system at once is an implementation that both compresses KV and reproduces the 93.3% gain on TPU, Trainium, and Ascend. The sources give no such cross-hardware control. This volume does not invent one.

### 3.2 Cloud ASICs have not dodged the scarce slice

Specs: the opening pointer and [Volume 25](vol-25.en.md). This volume does not reopen them. To beat today's cabinet you return to 3nm, HBM, and advanced packaging. Only a real retreat to 5nm with less packaging dodges the scarce slice. Public next-gen parts have not stopped. If they do not stop, ASICs still bid the same slice against NVIDIA. Of the five interrupts, "cloud ASICs take training off the cabinet" is now taking some inference, not the training cabinet.

### 3.3 Model and deployment products can extend platform power without a separately disclosed profit pool

The deepening rewrite of Volume 6: DeepSeek only proves open source can thin the API. NVIDIA as model/deployment extension is written as a conflict structure, not a second profit pool. The China stack survives on people who cannot buy, not on cheapness punching through a unified compute architecture.

The conflict structure is this. The system platform sells cabinets. The software/runtime layer sets the interface. The roadmap and supply-coordination layer sets the mix. The model/deployment extension ships weights and deploy microservices. Once the platform-control layers are welded, customers do not compare single-card FLOPs. They compare whether they can enter a 72-card high-speed domain, and whether models inside that domain can be pulled up with official microservices. Once inside the domain, the next generation is bought inside the same domain. Open weights can run outside the domain, but running nearly 10× concurrency to the full often still returns to unified memory and official kernels. If a model firm only sells weights, it sells the layer that can be copied open. NVIDIA sells the domain that cannot be opened.

That the revenue bulk is still on cabinets can already be confirm. R&D $18,497M is group-wide. The main line has that row. There is no model-software split. This volume does not invent inference-microservice ARR. If no split is found, leave it empty.

The model firm's dead end is not "the model is not good enough." It is that cost structure and price structure no longer belong to the same class of good. Software-era 85% margin assumes the marginal cost of copying a weight is near zero. In the AI-infrastructure era the cost is a cabinet depreciated over four years, rack-scale power, and group-wide capex already written on the clouds' books. Once API unit price is beaten by open inference down toward marginal power, model firms must remanufacture scarcity with product form, or they go from software companies to cloud channels. The introduction writes this as margin 85% to 55%. This volume reads it as: seat-license software is being replaced by "intelligence that carries depreciation." Whether the replacement is done waits on a same-scope filing, not a demo.

Put model firms back in the three layers of power and the seat is set. The bottleneck layer takes 60% to 75% gross margin (historical stress-test values, matching the main line's seller 49% to 59.9% and cabinet-seller 71% to 75%). The cloud layer takes the landlord right that matches mixed-year group-wide capex of $211.9B to $213.9B. The model layer controls neither wafers nor power. It controls weights that can be copied open. Multi-head latent attention and $5.576 million (historical stress-test values) cut the cost of "copy" again. The model layer's bargaining room is therefore narrower than the 2023 story, not wider. To widen it, it has to change from a weight seller to a workflow seller, so the customer stops production if it leaves the model. Draft Volume 6 gives no revenue evidence that any firm has already finished that rewrite.

### 3.4 Lower price alone does not eliminate system-stack switching costs

Cheapness alone is not enough. A unified compute architecture is a ten-year developer stack. UXL and oneAPI have people on stage. That is digging, not already through. A 75% pad means it can also cut price. Hardware can be cheaper. The switching tax remains. Open models beat API price down. The switching tax is still due: kernels, compilers, communication primitives, the in-cabinet domain. The China stack survives on people who cannot buy NVIDIA, not on cheapness punching through a unified compute architecture. A high-price peer only lets Huawei join the high-price bid. Domestic clouds switch stacks only under cutoff and policy. Both sides are expensive.

Geopolitically, DeepSeek running this set of historical stress-test values on post-export-control silicon is a demonstration: the locked side can trade structure and scheduling for a hardware generation gap. That does not cancel the 72-card cabinet's system premium. It does rewrite the story that "only an unrestricted top card can ship a frontier model." Control then moves from "forbid compute" to "forbid the highest-bandwidth system." The model-layer open-source game becomes a gauge of control. What it measures: can a notch-down of hardware plus algorithm approach the frontier. What it approaches is API-layer "good enough," not the system-layer domain.

Three layers are not one layer. The phone layer eats LPDDR and consumer bits. The PC layer eats DDR sticks. The AI layer eats HBM, server DIMMs, advanced packaging, and the high-speed domain. An open-source training bill is the model layer cutting the API layer down a dimension. It is not a rewrite of the AI-layer supply function. Matching a domestic open model to global cabinet allocation is the wrong layer.

### 3.5 China's parallel stack is driven by access constraints, domestic demand, and system capability

Three layers: [Volume 12](vol-12.en.md). This volume does not reopen a prospectus. Open weights can run on parallel stacks and reduce dependence on one API vendor, but frontier training substitution still depends on hardware, memory, packaging, interconnect, software maturity, and deployment scale. Open source thins the closed API. Domestic substitution stands up a parallel bid. Stacked together, the two still do not break the North American cloud plus unified compute architecture plus advanced packaging plus HBM weld.

### 3.6 Bundling still misses three checks. The model layer will be picked off

The three checks and five interrupts: [Volume 8](vol-08.en.md). What the model layer can supply is the second check: bind weights, compilers, and communication into one stack that can change base. That check is still an embryo. Open weights are embryo material, not a base already dug through. For model firms, the closest of the five are the second and the fifth. The second is not done: public next-gen ASICs are still on HBM and leading-edge nodes. The fifth is not done: there is no case forcing the interface open. So model firms still face this: the API is thinned by open source, the base is not forced open, and the landlord has stepped onto the field.

## 4. Scenarios, counters, and testable markers

Main scenario (analysis add): from 2026 to 2028 the model market splits into three layers. The bottom is open weights plus self-built or rented inference, price near power and depreciation. The middle is clouds mixing ASICs and GPUs and selling them as tokens. The top is a few closed firms collecting premium on product form (deep research, agent workflows, compliance isolation), not on parameter count. The closer depreciation gets to historical stress-test material's annualized $45B to $55B (unverified), the harder the top-layer premium covers the landlord's capex. Model firms look more like independent software that raises cloud utilization.

Counter 1: closed firms still hold assets that cannot be opened — data, tool use, product distribution — so API margin need not follow training cost. Counter 2: $5.576 million covers pretraining only; true full cost is still tens of millions of dollars; the moat remains. Counter 3: agent workflows pull token burn up, so even if unit price falls year on year, clouds can still recover group-wide capex on volume. historical stress-test material sensitivity table has a column with call volume +300% and unit price down 50% a year that still writes a $15B return. That column is a scenario, not a realized result. Counter 4: if 93.3% does not reproduce on long context and multimodal, the memory-bandwidth bound returns to the old seat and the HBM demand function is not rewritten. Counter 5: if the next official cloud-ASIC note truly writes 5nm plus commodity DRAM as the inference mainstay, the main line's fifth clause "have not stopped" has to be rewritten. the current evidence review found no such sentence.

Testable markers. Do public technical reports still write this set: 671 billion, 37 billion, 2.788 million GPU-hours, $5.576 million. Do cloud token quotes show historical stress-test material's implied 30% to 50% year-on-year drop. Is there one same-scope case of software-as-a-service margin from 85% to 55%. Is there a real "nearly 10×" concurrency control on an 8-GPU server for an open model. Do the next official notes from Microsoft, Google, Amazon, and Meta still write HBM and leading-edge nodes, or does a "retreat to commodity DRAM" sentence appear. Will Google or Amazon name a foundry for the first time. Will Meta, after the 300 generation, name TSMC or 3nm. Do supply commitments rise again next quarter or go flat. Do not treat Part II's $35B to $50B of AI software revenue as an audited industry size.

This volume does not pick a branch. It only requires later citations to keep $5.576 million, 93.3%, and 85% to 55% labeled as historical stress-test values or unverified judgments, not as an industry liquidation already finished. Whether the dead end has already happened waits on the first same-scope filing of margin walking from 85% to 55%.

## 5. Gaps and what cannot be written as fact

$5.576 million is a conversion. Rate, whether cluster depreciation is included, and whether the bill is pretraining only, historical stress-test material does not unpack. The 85%+ cut is set against "tens of millions to hundreds of millions," a range, not a sample mean. the current evidence review did not open the technical-report original. 671 billion, 37 billion, latent dim 512, head dim 8192, model FLOPS utilization above 50%, 14.8 trillion tokens: all historical stress-test values.

93.3% and "nearly 10×" give no multi-head baseline and no context length. A cross-hardware reproduction control is not in the sources. The report does not infer one.

Software-as-a-service 85% to 55%, 2026 capex $670B to $750B, AI software revenue $35B to $50B, a $60B to $80B gap, annualized depreciation $45B to $55B and $115.5B: all models or forecasts, unverified, do not treat as audited fact. historical stress-test material $215B is not an addable formula. This volume uses mixed-year group-wide $211.9B to $213.9B, and the 2025 mixed year of about $354B to $356.5B. The four clouds have no "AI hardware" line item.

This volume invents no model-firm ARR, user count, or profit. OpenAI and Anthropic have almost no standalone financial rows in draft Volume 6. Nemotron, NeMo, and inference microservices have no revenue split.

Google and Amazon's latest official generation do not name TSMC. The report does not treat that they have left, and do not write that they have named one. Meta's 300 generation names Broadcom. It does not name TSMC. It does not name 3nm. Third-party transistor counts, Hynix stacks, 3nm compute dice, Broadcom's packaging percentage, and ASIC TCO-savings percentages do not enter the fact layer. Seventy-two-card cabinet dollars and a bill-of-materials split are not sources for this volume.

Samsung 16k, 24k, 40k wafers per month; CXMT 350k wafers per month; YMTC monthly wafers in the tens of thousands: not in the announcements. SMIC 5.1% is institutional revenue share, not units. Converting HPC 58%, 3nm 24%, first-customer 19% into tens of thousands of wafers: revenue share is not units.

Do not fold equity marks into the cash that bids for capacity. Q1 net income includes about $15.9B of unrealized gains. Bidding looks at operating income $53,536M.

Cabinet counts, global absolute HBM bits, packaging wafers by customer, a realized year-on-year drop in public token quotes, the first same-scope filing of margin walking from 85% to 55%: leave them empty. The report does not infer them.
