# Volume 26: Model Companies, Anchor Compute Buyers, and Infrastructure Co-Build

Chinese original: [vol-26.md](../vol-26.md)

Cloud-system specs: [Volume 4](vol-04.en.md) and [Volume 25](vol-25.en.md). Residual capacity: [Volume 5](vol-05.en.md). Anchor Compute Buyer Effect: [Core concepts and models](../核心概念与模型索引.md). This volume no longer treats "model company depends on cloud" as a one-way relationship; it studies how long-duration capacity commitments can shape chips, data centers, and power while model companies remain constrained by physical assets and system stacks.

## 1. The question this volume answers

Between model firms such as OpenAI, Anthropic, and DeepSeek and platforms that control land, power, racks, and compiler stacks, where does bargaining power sit? By 2026 the question cannot be reduced to "model companies depend on clouds." OpenAI is organizing multi-party infrastructure through Stargate, and Anthropic has made a long-duration, large-scale AWS capacity commitment. Frontier model companies are becoming **super-scale compute buyers** that can influence chip roadmaps, data-center construction, and power planning.

This volume tracks five relationships: system-stack dependence; long-duration compute contracts; who carries infrastructure capital; whether algorithmic efficiency lowers unit demand; and whether model-company order scale can reshape cloud and semiconductor roadmaps.

Dependence must be split into **three** accounts. First is **using a stack**: chips, interconnect, compiler/runtime, and rack-level system. Second is the **long-duration compute bill**: a model company can trade multi-year commitments for priority capacity. Third is **asset ownership**: data centers, power, servers, and networks usually remain on cloud, infrastructure, utility, or financing-partner balance sheets. A sufficiently large model buyer can influence the second and third accounts without owning a fab, an HBM line, or a grid.

Public next-generation cloud systems do not retreat to 5nm + commodity DDR5: Maia 200 uses TSMC N3 and 216 GB HBM3e; Ironwood 192 GB HBM3E; Trainium3 3nm and 144 GB HBM3e; MTIA generations from 300 onward use HBM stacks. Changing clouds can change chips, interconnect, compiler, runtime, and the invoice name, but it does not automatically remove HBM and advanced-system constraints. China's parallel stack is developing, but frontier training still requires advanced manufacturing, HBM/packaging, interconnect, and manageable software-migration cost to close together.

## 2. Current evidence boundary

The central evidence in this volume is no longer limited to model architecture. Model-company infrastructure commitments are now first-order observable variables:

- **OpenAI / Stargate:** target of up to **$500B** of U.S. AI infrastructure investment over four years; OpenAI/Oracle later announced another **4.5 GW**, taking disclosed capacity under development above **5 GW** with Abilene.
- **Anthropic / AWS:** commitment to spend **more than $100B over ten years** on AWS technology, with the ability to reserve up to **5 GW** of new capacity; Anthropic said it was already using **more than 1M Trainium2 chips** and expected close to **1 GW** of Trainium2/3 capacity by the end of 2026.
- **DeepSeek-V3:** **2.788M H800 GPU-hours** of formal training is useful as an algorithmic-efficiency anchor, but its report-side cost conversion is not a complete company R&D cost.

Unverified cabinet software-premium estimates, unchecked latency figures, fixed depreciation templates, and undisclosed model-company economics remain outside the fact layer.
## 3. Mechanism: model firms depend on the stack, not one brand's advertising copy

### 3.1 Training dependence: whoever holds unified memory issues the start-work permit

A 671B-total, 37B-active mixture of experts is no longer a single-card problem. Pretrain needs gradient sync and expert routing across thousands of cards. Sensitivity to latency sits above sensitivity to single-card FLOPs. earlier stress-test material wrote a 72-card fabric as one giant logic chip. A model firm without an equivalent fabric can only buy time from a cloud or a cabinet channel that owns that fabric. That is the first meaning of infrastructure dependence: not a need for some accelerator cards, but a need for unified memory with low enough latency. The judgment's official single cabinet is 72 GPUs, 36 Grace, 13.4 TB HBM, 17 TB LPDDR. NVLink 1.8 TB/s per card, 130 TB/s per cabinet, latency under 100 ns, are unverified engineering values. Without that fabric, 671B expert routing hits the interconnect wall first, then the memory wall.

Cloud ASICs do not rewrite this meaning. Microsoft wrote Maia 200 main memory as co-packaged HBM3e, 216 GB, 7 TB/s. Google wrote Ironwood as eight HBM3E stacks per chip, 192 GB, about 7.4 TB/s, and cluster-directly-addressable HBM as 1.77 PB. Amazon wrote Trainium3 as 144 GB HBM3e, up to 20.7 TB on an ultra-server. Those specs serve the clouds' own training and inference instances. They do not open a commodity-DDR5 back door for model firms. Changing clouds changes the name on the invoice, not the memory type.

A privileged position can be written: training has to pass their stack and their cabinet; they sit closer to the raw batch than any model firm. That is structure. A backdoor or theft of training data is an allegation. There is no public forensics. It does not enter the fact layer.

### 3.2 Changing clouds changes the name on the invoice, not HBM

The four official spec sets are already in [Volume 4](vol-04.en.md) and [Volume 24](vol-24.en.md). This volume keeps one sentence: whichever cloud a model firm binds, training and high-quality inference still land on HBM. Changing clouds changes the name on the invoice, not the memory type. The current evidence review did not read any cloud saying "retreat to 5nm + commodity DDR5 as the inference mainstay." The four sentences together are not "in-house silicon equals a model-firm breakout." They are "in-house silicon turns the scarce-slice buyer from one name into five." Five names bidding together does not automatically make price or lead time friendly to a lab.

### 3.3 Inference escape has a boundary: MLA reduces rank; it does not cancel the memory wall

DeepSeek-V2's **93.3% KV-cache reduction** is a first-party comparison against its stated baseline; the older “nearly 10×” concurrency claim is not used as a current fact anchor. inference-side dependence is therefore looser than training-side dependence. A model firm can run some inference on open weights plus ordinary servers without locking a whole cabinet. The boundary is also clear. Long context, multimodal work, and tool-call-heavy agents push KV and traffic back up. MLA is a rank reduction, not a cancellation of the memory wall. The harder boundary is supply: 51% of 2026 DRAM bits are already HBM plus registered DIMMs. Memory is 47% of major CSP capex in 2026 and 68% in 2027. Server DDR5 is residual. Even if a model firm moves inference onto commodity sticks, what it adds load to is the slice already rising. Channel talk of 16G from 450 to 1800 is not a 10-K. It only shows residual bits are getting more expensive. You can buy them. The price is higher. Micron provides first-party evidence that HBM3E requires roughly **3× the wafer supply of DDR5** at the same node and bit capacity. Makers shifting lines to HBM leave fewer consumer bits.

AWS itself moved its inference chip from 8 GB DDR4 per die to 32 GB HBM, 4x capacity and 10x bandwidth. Meta wrote HBM bandwidth as the most important factor for generative inference, and moved from off-chip LPDDR5 to HBM stacks. The clouds, as landlords to model firms, have not themselves retreated to commodity sticks as the mainstay. Tenants have even less reason to assume "change the algorithm and the landlord will quote DDR5." A search of the four official domains (azure.microsoft.com, blogs.microsoft.com, techcommunity.microsoft.com, cloud.google.com, blog.google, aws.amazon.com, ai.meta.com) did not find a sentence that said "5nm + DDR5 as the inference mainstay" or "retreat from HBM to commodity DRAM." The direction read is the opposite.

### 3.4 $5.576M rewrites the table, not the physical wall

DeepSeek-V3 reports 2.788M H800 GPU-hours for formal training and a report-side $5.576M rental conversion. The older “more than 85% cheaper” comparison lacks a consistent industry baseline and is not used as a fact. if that magnitude holds, closed model firms can no longer treat "we burned money others cannot burn" as the only moat. The compute platform's single story ("only the highest-priced cabinet can make a frontier model") takes a discount. But $5.576M is a compute conversion, not full cost. Data, people, failed runs, and inference deployment are not inside it. The comparison baseline "traditional trillion-parameter models at tens of millions of dollars" has no sample. It cannot be lined up against an undisclosed closed lab's total R&D, and it cannot be written as "training is already cheap enough to leave HBM." The current edition uses the technical report directly and keeps the scope narrow: formal-training compute is public; complete R&D cost is not.

H800 itself shows that dependence has a license dimension. Export control writes which card you can rent as a border. An algorithm edge can partly hedge interconnect and memory specs. It cannot assume every lab can copy the supply condition of 2048 cards and 2.788 million GPU-hours. If a domestic shop reproduces on Ascend, earlier stress-test material comparison is interconnect at 392 GB/s versus 1.8 TB/s, and CXMT's prospectus with 0 mentions of HBM. The layer is wrong. Not the same river. The China stack catches people who cannot buy NVIDIA. It does not tear global labs off CUDA. UXL / oneAPI is an embryo. It has not dug through. Cheapness does not fill the CUDA switching cost. A 71.1% to 75.0% pad means it can also cut price.

### 3.5 Commercial relations have moved toward long-duration capacity commitments and infrastructure co-build

By 2026, primary public material is sufficient to retire the old "contract amounts are blank" framing.

**OpenAI / Stargate.** OpenAI announced Stargate in 2025 with a target of investing up to $500B in U.S. AI infrastructure over four years. Initial equity participants included SoftBank, OpenAI, Oracle, and MGX; OpenAI is responsible for operations and SoftBank for financial responsibility. In July 2025, OpenAI and Oracle announced another 4.5 GW of Stargate data-center capacity, taking capacity under development above 5 GW with Abilene, and said the platform would run more than two million chips. Stargate spans multiple infrastructure partners; Microsoft continues to provide cloud services.

**Anthropic / AWS.** In April 2026, Anthropic announced an expanded Amazon relationship: a commitment to spend **more than $100B over ten years** on AWS technology and reserve up to **5 GW** of new capacity. Anthropic said it was already using **more than one million Trainium2 chips** to train and serve Claude and expected close to 1 GW of Trainium2/Trainium3 capacity online by the end of 2026.

These facts change the bargaining model:

```
model demand scale
→ long-duration compute commitment
→ financing certainty for cloud / infrastructure
→ new data-center, power, and chip scheduling
→ priority capacity for the model company
→ larger training / inference
→ larger long-duration commitment
```

A frontier model company can therefore become an **anchor tenant / anchor compute buyer**, and may help define the next system generation.

Asset ownership still matters. Stargate does not mean OpenAI owns every site, power plant, server, and fab; Anthropic's 5 GW is not 5 GW of already-energized self-owned capacity. Model firms gain long-duration capacity, operational influence, and priority; irreversible capital and manufacturing remain distributed across clouds, data centers, utilities, chipmakers, and financing partners.

The dependence is now two-way: infrastructure platforms need high-value model demand; model companies need executable power, racks, HBM, advanced packaging, and system software. Bargaining power depends on substitutability, who carries irreversible capital, who controls next-generation scarce resources, and whether the model company can move its demand to another platform.

### 3.6 Compiler/runtime switching costs remain a core dependency

Historical 40%–45% cabinet software-premium estimates are not segment disclosures and do not enter the fact layer. The durable mechanism is stack-switching cost: training frameworks, inference engines, operator libraries, compilers, and deployment tooling are not interchangeable at zero cost. A model company that wants to move across CUDA, TPU, Neuron, Maia, MTIA, or domestic stacks must maintain multiple compile-and-debug paths, which smaller labs may not be able to do efficiently.

China can already provide parallel supply in smartphones and parts of consumer computing, while frontier training still requires advanced logic, HBM/advanced packaging, high-speed interconnect, and mature software to close simultaneously at scale. Replacing one compiler or one domestic chip is therefore not equivalent to replacing the full frontier system stack. UXL and oneAPI demonstrate that real open cross-architecture migration paths exist; public evidence does not yet show that frontier workloads can move across CUDA, TPU, Neuron, MTIA, and domestic stacks at negligible migration cost.

FY26 NVIDIA Data Center revenue of $193.737B is one of the largest single seller-side proxies for AI-infrastructure monetary flow and value capture. It is not equal to all global compute-platform value capture. The application layer can face lower prices while the backend still captures substantial value.

### 3.7 Samsung's long and Tesla: irrelevant to this volume, and it must be written clear

Samsung announced KRW 22.76T, about $16.544B, through 2033. The counterparty is written as a large global company, about 7.6% of its then-expected 2024 revenue. The filing does not write Taylor, does not write wafers per month, and does not write Tesla. Musk that day named the Texas Taylor fab for the sixth-generation automotive chip. 16,000, 24,000, and 40,000 wafers per month have no announcement. 2nm yield at 55% is not official. This line is automotive AI, not OpenAI or Anthropic training quota. TrendForce 2026 Q1 Samsung foundry share 6.5%. SMIC at 5.1% cannot take Western GDS. Export control and trust: the third item does not pass. SMIC takes phones, TVs, notebooks, and mature nodes, not Azure / GCP training cabinets. Intel Foundry is not in this pure-play foundry top ten. Rapidus is not in volume. Model firms have no second leading-edge-logic river to flee to. Write the node as 5nm or as 3nm: public, volume-ready advanced AI logic at the four clouds is still mostly TSMC.

### 3.8 How the two bills land on the bid

The using-the-stack bill decides whether a model firm can start work, which IR it uses, and whether weights move across clouds without loss. The paying-the-invoice bill decides who advances depreciation and at what tariff it is passed to the lab. Four-cloud PPE proves halls are being built. See [Volume 1](vol-01.en.md) and the four-cloud scope check. Those lines do not prove a buyer can push seller gross margin down from 71.1% or the quarter's 75.0%. Prepayments, HPC 58%, first customer 19%: see the judgment. Matching Apple's phone share against a model firm's training cabinets is the wrong layer.

A model firm that thinks switching to an ASIC cloud escapes the scarce slice still pays an HBM bill. Specs: [Volume 4](vol-04.en.md). Acting alone on exclusive deals means handing over each year's new lines and packaging. The major interrupt variables remain incomplete and should be monitored through the shared S1–S4 framework.

### 3.9 residual-capacity pressure also hits model firms on the inference side

Even if a lab moves some inference onto ordinary servers, the added load is still residual. 51% and cabinet-times-spec: [Volume 5](vol-05.en.md). If a cloud moves inference at scale onto ASICs plus conventional DDR5: it stops bidding against NVIDIA for full HBM output, the only physical benefit of that path; but the added load is the slice already rising, bid by phones, PCs, and ordinary servers together. Not a dead end. A tax. Domestic memory does not automatically open a tax-free DDR5 river for model labs. See [Volume 12](vol-12.en.md). What model firms contest is not one wafer in full-factory shipments. It is the packaging and HBM slice. 5.39 and the wrong pool: `测算-投片与柜-20260826.md`.

## 4. Scenarios, counterarguments, and testable markers

New quantities are unverified. Do not treat them as verified first-party facts.

Scenario A: algorithms reduce rank; model-firm weight rises. Low-rank attention and mixture of experts become the default. Training bills stay priced in million GPU-hours and million dollars. Testable: whether later open models repeat thousand-card, million-GPU-hour training disclosures; whether closed-source interface prices are forced to follow. Unverified: this volume does not forecast a token-price path.

Scenario B: agent workloads bind model firms back to high-bandwidth cabinets. Tool calls, long memory, and multimodal work eat the nearly 10x concurrency with context growth. Testable: context length, KV occupancy, and cross-card traffic share in public technical reports; whether cloud official pages still write HBM3e. All four write it now.

Scenario C: platforms reverse-integrate models. Clouds and NVIDIA use a mature compiler stack plus depreciation pressure to make the model layer an in-house product. Independent labs become a channel. Nemotron / NeMo / NIM are product lines already on this side. No split. Testable: whether a cloud's own model becomes the console default; whether independent labs must accept compute-for-equity to expand; whether NIM is disclosed alone. earlier stress-test material has no contract amounts. The report does not infer them. No split, no second profit pool.

Scenario D: a model firm thinks switching to an ASIC cloud escapes the scarce slice; the bill is still HBM. Testable: whether official Maia, Ironwood, Trainium, and MTIA memory reverts to commodity sticks. It has not. Maia 200 writes N3 plus HBM3e. Trainium3 writes 3nm plus HBM3e. Ironwood writes HBM3E. From MTIA 300 on, the pages write HBM stacks.

Scenario E: the West actually bundles. Prepayments large enough that one buyer cannot be the only name recognized; software bound into one stack; memory longs that leave a line for commodity bits. Testable: whether a joint capacity commitment appears across clouds and across accelerators; whether UXL / oneAPI moves from embryo to a portable default IR. It has not. The four-cloud 2025 mixed year of about $354.0B is a sum of acting alone, not a joint prepayment. Microsoft at $106.265B is large and still orders alone.

Counters. First, $5.576M may not be reproducible. It is one successful run, not an industry cost function. Second, even if OpenAI and Anthropic never appear in earlier stress-test material number table, brand and enterprise contracts may still let them take the large share of the split, with infrastructure only a cost line. Third, a flood of open weights can press both model-firm and cloud rental prices at once. Power does not automatically go to either side. Fourth, if an official inference mainstay really retreats to commodity memory, this volume's "still on the scarce slice" has to be rewritten. Fifth, CSPs were only about 50% of Q4 FY25 data center. Sovereign and enterprise self-build dilute "the four clouds decide everything." Sixth, cloud buyers are large enough to exert buyer-side pricing pressure through volume and long-duration commitments. platform value capture does not collapse into a single margin or revenue line. None of the six counters licenses inventing a contract amount, or knocking seller revenue against buyer capex.

## 5. Gaps and what cannot be treated as fact

OpenAI and Anthropic now have first-party infrastructure commitments that anchor this volume, while undisclosed accelerator pricing, utilization, revenue, valuation, and profit-sharing remain unquantified. DeepSeek-V3's 671B total parameters, 37B activated parameters, and 2.788M H800 GPU-hours are technical-report anchors; the $5.576M figure remains a report-side rental conversion rather than a complete development-cost measure. The "more than 85% cheaper" baseline lists no sample. Nearly 10x concurrency gave no test set, batch, precision, or hardware comparison table. $215B and $45B to $55B of depreciation are used to explain model-vendor behavior, but most model firms are not on annual-report tables. Depreciation pressure lands on the clouds first, then passes through rental prices. The older $45B–$55B depreciation estimate is a stress-test template, not a sum of disclosed four-cloud asset classes. The 2025 mixed year is already about $354.0B. Pushing 2026 to 2028 from 2024's $215B understates the later base. 2026-to-2028 expense: unverified. Do not treat as an verified first-party fact.

This volume has no IR license terms and no reserved-cabinet list from any cloud. The power game can be written as mechanism. It cannot be written as contract numbers. Samsung wafers per month, ASIC TCO-savings percentages, a $3.00M cabinet, cabinet ASP $2.60M to $3.30M, switch-chip gross margin above 85%: do not write them. Broadcom's share of CoWoS is not a TSMC split. The report does not treat it. Domestic CXMT monthly capacity of 350k wafers is not an announcement. The report does not treat it. "sold out through 2026" at the shareholders' meeting has no official transcript. Do not promote it. No Google official sentence naming TSMC or Broadcom was found. No AWS official sentence "foundried by TSMC" was found. No MTIA 300-generation sentence naming TSMC or 3nm was found. Leave those three empty. Do not fill them from third parties. The current evidence review did not read a node or HBM-capacity sentence on eighth-generation TPU. Do not fill it. NIM has no split. The report does not treat the model player as a second profit pool. The report does not treat that a backdoor has already happened. Seller data-center revenue and four-cloud capex cannot serve as each other's proof of payment.
