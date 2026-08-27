# Volume 2: Nvidia compute-empire model (system-level monopoly, Blackwell microarchitecture, and the CUDA lock)

Chinese original: [vol-02.md](vol-02.en.md)

Moat tables and the draft BOM audit are in [Volume 32](vol-32.en.md). This volume only writes why the sales unit moved up to the cabinet, and why the referee seat cannot be punched through by cheapness alone.

## 1. The question this volume answers

Is the empire already finished? If it is still underway, which layer is locked: the chip, the board, the cabinet, or the developer stack? This volume does not write a dollar bill of materials. It does not write a single switch-chip gross margin above 85%. It does not write a 95% PTX coverage as a measured sample. What it answers is why the sales unit moved from the chip up to the cabinet, why the referee seat cannot be punched through by cheapness alone, how the coach's mix pulls foundry and memory buildout, and how the highest-margin name uses prepayments to buy the next generation's slots.

The main line writes NVIDIA as four corners: the athlete sells GPUs, cabinets, and interconnect; the referee sets a unified compute architecture, high-speed interconnect, and a cabinet standard; the coach sets the Hopper-to-Blackwell-to-Rubin mix of HBM, packaging, and interconnect; and it trains models itself. The revenue bulk is still on cabinets. This volume is the mechanism core of athlete plus referee. The coach is caught with TSMC's official sentences and packaging tightness. The model player is written as structure only. Do not invent ARR.

The draft wrote the empire as a system-level monopoly plus an ecosystem lock. What can be nailed is the official cabinet spec, data-center revenue, the unified compute architecture as an interface fact, and supply commitments that are still rising. What cannot be nailed is an undisclosed software-premium percentage, PTX covering 95% of the world, AMD trailing 30% to 50%, or a cabinet leaving the factory at two to three million dollars. "The trust is already complete" and "rivals no longer exist" are scenarios, not the present.

This volume also nails two things that are easy to mix. First, they already made cards. The FY26 gaming line in the official press release is a record $16.0 billion, up 41% year on year; professional visualization $3.2 billion for the year. What changed is selling training as a cabinet, not never having made cards. Second, booked first-customer 19% is not a safe distance. What is being opened is HPC and packaging. Occupy the increment and next year's slots belong to the first name. The binding line is packaging, not the factory's 15 million wafers.

Forecasts are pushed forward from the present. They are marked as hypotheses. Present numbers come from the main line and two source files whose official texts have already been opened, plus the product page and press releases checked in this pass. If a split is not found, leave it empty. Do not invent one.

## 2. What the draft already argued

The draft table of contents wrote this volume as a system-level monopoly, the Blackwell microarchitecture, and a unified-compute-architecture ecosystem lock. What is actually useful in the body is not a dollar table. It is cabinet semantics: 36 Grace, 72 Blackwell, liquid cooling, a high-speed domain that uses 72 dice as one logic chip. That slice joins the main line's move of the sales unit. It should stay.

The draft also pasted a materials dollar table. It wrote software and brand premium at 40% to 45%, switch-chip gross margin above 85%, and a cabinet leaving the factory at $2.60 million to $3.30 million. The product page and the 10-K do not have those lines. Source 01 does not have them either. This volume deletes the dollar table used as an audit. It keeps the official physical build.

The draft wrote PTX coverage of 95% and AMD throughput trailing 30% to 50% as share sentences. There is no sample. A unified compute architecture explains why others have trouble switching stacks. It does not explain a quarter of scarce gaming cards. Scarcity is the same leading-edge logic, packaging, and HBM being fed to the data center first.

The draft almost never talks about the coach, the model player, or gaming cards giving way on supply. This volume fills those three slices from the main line: packaging-and-test revenue from about 8% to a bit over 10%; Nemotron, NeMo, and inference-microservice product lines exist, and the revenue bulk is still on cabinets; gaming $16.0 billion for the year, $3.7 billion in Q4, down sequentially, the company writing channel inventory coming down, the outlook writing that supply constraints will drag gaming in the next fiscal year. The athlete can already give the same material to the higher-margin data center.

The draft wrote backdoors and distillation as already having happened. The main line and the frame treat them this way: a backdoor is an allegation; there is no public forensics; it does not enter the fact layer. What can be written is a privileged position: training has to pass their stack and their cabinet; they sit closer to the raw batch than any model firm. If distillation happens, the mechanism is visibility on a compute path, not proven theft.

## 3. Dig into the mechanism

### 3.1 The athlete is already selling cabinets

Official product page: the GB200 NVL72 connects 36 Grace and 72 Blackwell in a rack-scale, liquid-cooled design, a 72-GPU high-speed domain acting as one giant GPU. Spec table: GPU memory 13.4 TB HBM3E, CPU memory 17 TB LPDDR5X, NVLink bandwidth 130 TB/s, 2,592 Arm CPU cores. Source: https://www.nvidia.com/en-us/data-center/gb200-nvl72/ This pass opened the product page. The three rows on configuration, memory, and interconnect match source 02. The page also writes inference, training, and energy multiples versus H100. Those are the company's own comparison sentences, with assumptions. Do not treat them as third-party measurements.

Seventy-two GPU packages per cabinet are the numerator of 5.39 later. 13.4 TB is the official anchor for memory demand multiplied by cabinet. 17 TB of LPDDR is on the CPU side, not HBM, but it competes with the cabinet for the same maker leading-edge capacity. The draft wrote 13.8 TB, another scope of 72 times 192 GB, which does not match this product page. This volume uses the page's 13.4.

The full FY26 / Q1 FY27 table is in [Volume 1](vol-01.en.md). This volume does not reopen it. The press release opened in this pass writes the platform splits in full: gaming a record $16.0 billion for the year, up 41%; Q4 $3.7 billion, down 13% sequentially as channel inventory came down; professional visualization $3.2 billion for the year; automotive $2.3 billion for the year. They already made cards. What changed is selling training as a cabinet. Once the cabinet is the default sales unit, customers do not compare single-card FLOPs. They compare whether they can enter a 72-card high-speed domain.

Asset-light is a mechanism, not an adjective. FY26 purchases of property and equipment and intangibles were only $6,042M, against operating income $130,387M and free cash $96,575M. The cabinet's heavy assets sit at TSMC, the three memory makers, and Foxconn / Quanta final assembly. What it collects is the right to weld those parts into a trainable system, plus the switching cost of the developer stack. Analysis add: the asset-light name uses profit to lock next year's slots at the heavy-asset names.

### 3.2 Referee seat: a unified compute architecture is a tax, not an atom

CUDA, PTX, high-speed interconnect, and the cabinet reference design are interface facts. A ten-year developer stack is in place. The CFO write-up describes the platform as processors, interconnect, software, algorithms, systems, and services. Compute and networking is the book where athlete and referee are welded: source 01 splits data center into compute $162,361M and networking $31,376M. Networking is not an accessory line. It is the ticket into the domain. Once inside a 72-card high-speed domain, 72 dice act as one logic chip. The next generation, Rubin, is still sold inside this domain. Referee and athlete are welded shut.

PTX coverage of 95% and AMD trailing 30% to 50% have no sample. They do not enter the fact layer. A unified compute architecture explains why others have trouble switching stacks. The switching tax is rewriting kernels, rebuilding cluster scheduling, and re-validating models. Hardware can be cheaper. A margin pad near 75% means it can also cut price. Cheapness alone does not punch through.

UXL and oneAPI have people on stage. That is digging, not already through. The main line writes that bundling needs three checks. Software is one of them: the switching tax becomes a change of base rather than a change of vendor. Miss that check and each stack switch is picked off one by one. The China stack survives on people who cannot buy, not on cheapness punching through a unified compute architecture. A high-price peer only lets Huawei join the high-price bid. Domestic clouds switch stacks only under cutoff and policy. Both sides are expensive.

For a cloud ASIC to win, it must also split this domain on training, not only shunt inference. Main-line point five: public next generations are not 5nm plus commodity DDR5. Maia, TPU, Trainium, and MTIA all move toward HBM and a leading-edge node. The direction is the opposite. To beat today's cabinet you return to 3nm, HBM, and packaging, and you bid against 75% gross margin. Only a true retreat to 5nm and less packaging gets you off the scarce slice. Public next generations have not stopped. This volume does not recopy the cloud-ASIC node table. That is source 04's scope. Here it only nails the referee seat: training is still inside this domain. Shunting inference is not enough.

### 3.3 Coach: the mix pulls foundry and memory

The roadmap is public: Hopper, Blackwell, Rubin. The 10-K writes that Rubin is expected to begin volume shipments in the second half of FY27. The press release writes Vera Rubin as six new chips, cutting inference token cost versus Blackwell by up to an order of magnitude. That is a company forward sentence, not a shipped filing line. The mix walks HBM, packaging, and high-speed interconnect together. The coach need not own a factory. Prepayments and supply commitments buy next year's factory slots.

TSMC advanced packaging and test revenue, CFO Wendell Huang on the 4Q24 call: overall advanced packaging and test accounted for over 8% of revenue last year and will account for over 10% this year. The company is explicit that it does not break packaging segments. 4Q25 call, corrected after the call: last year a bit over 10%, about 8% in 2024, 2026 outlook low teens. What can be nailed: about 8% in 2024, a bit over 10% in 2025, 2026 outlook low teens. What cannot: packaging revenue alone, monthly capacity, packaging wafers by customer.

C.C. Wei, 4Q24 original: today it is all AI, capacity is very tight, and cannot even meet customers' need. 2Q26 original: packaging capacity is so tight that now it limits my customers' growth. Same call: today the majority is still CoWoS. The six English words "sold out through 2026" at the shareholders' meeting: the Focus Taiwan shareholders' meeting copy opened in source 02 has no packaging and no "sold out." Second-hand paraphrase is not promoted to an official sentence. This volume uses only the two sentences that can be nailed: tight, cannot meet, already limits customer growth.

SK hynix FY25 press release: revenue KRW 97.1467T, operating profit KRW 47.2063T, operating margin 49%, net profit KRW 42.9479T, net margin 44%. HBM revenue in the DRAM segment more than doubled in a year. Won are not privately converted to dollars. Makers expand to this mix. The coach sets the mix. Sellers expand to the mix. The increment that comes out is bought first by prepayments. Sellers are already rich. They still cannot cover the cabinet-selling tranche.

Samsung, 28 July 2025, announced a foundry supply long: KRW 22.76T, about $16.544B, 24 July 2025 to 31 December 2033. The counterparty is written as a large global company. The filing does not write Taylor, does not write wafers per month, and does not write Tesla. Musk named the new Texas fab for Tesla's next-generation AI6. 16k / 24k / 40k wafers per month are in neither the filing nor Reuters. Do not write them. This parallel line proves the second-name foundry is not another TSMC: the long is there, monthly capacity is empty, and it cannot take the GDS queue of Western flagship chips.

### 3.4 Profit decides the bid

Profit, cash, and supply commitments are maintained in [Volume 1](vol-01.en.md). This volume uses only the mechanism: strong free cash flow and order certainty increase a platform's ability to reserve future scarce resources. That does **not** make TSMC a captive fab or imply a one-variable auction. Price, order scale, prepayment, credit, utilization, roadmap certainty, diversification, and geopolitics all affect allocation. High-NA bulk-buyout stories, undisclosed N2 first-silicon contract amounts, and customer-specific packaging splits remain outside the fact layer unless primary evidence appears.

### 3.5 Booked 19% is not a safe distance

TSMC shipments, node revenue, platforms, and Customer A / B are in [Volume 4](vol-04.en.md). This volume does not reopen them. 19% is full-year revenue share. Voice on the scarce slice is larger than this booked number. What is being opened is HPC and packaging, not phones. Occupy the increment and next year's slots belong to the first name. Booked 19% is not a safe distance.

### 3.6 5.39 and the pool

5.39 is a packaging-wafers-per-cabinet estimate: 72 GPU packages divided by about 13.4 packages per wafer. 72 is official. About 13.4 is a geometry working hypothesis: two dice totaling about 1,600 mm², plus eight HBM stacks, an interposer far larger than a single GPU. A 300 mm wafer is about 70,686 mm². There is no official TSMC number for how many B200 packages come off one packaging wafer. 5.39 is an estimate. It is not fiction. It is also not logic wafers per cabinet for the whole factory.

Die area. B200 two dice at about 800 mm² reticle limit, nailed in Electronic Design and IEEE Spectrum, a reporter geometry sentence, not a 10-K. H100 official blog: 814 mm². Front-end logic is another line: 144 dice, about 2.9 wafers per cabinet at 70% yield. That does not match 5.39. Mixing them is the wrong pool.

835,000 cabinets equals 4.5 million wafers divided by 5.39. 4.5 million is 30% of TSMC's 2025 shipments of 15 million. 5.39 is packaging wafers per cabinet. Most of the 15 million are phones, MCUs, auto, and mature nodes. Dividing the whole factory, or 30% of it, by 5.39 yields a cabinet count with no physical meaning. The whole factory 15 million divided by 5.39 yields 2.78 million cabinets. That cannot be used either.

A sell-side pool must be labeled sell-side. Morgan Stanley paraphrase: 2026 global packaging demand about 1 million wafers, NVIDIA about 595,000 and 60%, TSMC monthly capacity from 32,000 wafers in 2024 to 93,000 in 2026. This pass did not open the Morgan Stanley original. It is nailed to the Longbridge paraphrase. Mizuho at another date: monthly capacity 140,000, NVIDIA 630,000 wafers at TSMC. The two sell-sides do not agree. A TSMC split does not exist. The main line uses only: packaging is tight, sold-out direction; when half is taken on a sell-side 1-million-wafer pool, label it sell-side.

At 5.39 packaging wafers per cabinet and sell-side 2026 demand of about 1 million wafers: half equals 500,000 wafers, about 93,000 cabinets. NVIDIA's tracked 595,000 wafers is about 110,000 cabinets, already past half of this packaging line. Rounded: about 100k cabinets take more than half. 800,000 cabinets times 5.39 equals 4.31 million wafers, 29% of the factory's 15 million, also near the 3nm-plus-5nm revenue share, but 24% plus 36% equals 60% is revenue, not wafers. Do not write 800,000 cabinets as locking 50% of 3nm or 2nm. You do not need 800,000 cabinets to lock 3nm. The binding line is packaging.

What official text can nail dead is only: packaging is tight, cannot meet, already limits customer growth. 100k cabinets is a sell-side pool times an estimate coefficient. The direction matches the main line. The coefficient is not an annual report.

### 3.7 The model player is written as structure only

Nemotron, NeMo, and inference-microservice product lines exist. The 10-K writes NVIDIA AI Enterprise, NIM, NeMo, and blueprints. The press release launched the Nemotron 3 open-model family. The revenue bulk is still on cabinets. Do not invent model ARR. Do not write a second profit pool. Power extends: others train on its stack; it sells adjacent models and inference products. If distillation happens, the mechanism is visibility on a compute path, not proven theft. A backdoor already happened: no forensics. It does not enter the fact layer.

Multi-year cloud-service commitments rose from $27.0B to $30.0B, officially for R&D, not confirmed cloud revenue, and still less model revenue. The draft promoted this line to cloud ARR. The scope is wrong.

### 3.8 Gaming cards are already giving way

The athlete can already give the same material to the higher-margin data center. This is not a guess. The FY25 CFO write-up already wrote limited supply for both Blackwell and Ada gaming GPUs. FY26 press release: gaming $16.0 billion for the year, $3.7 billion in Q4, still strong year on year, sequentially down as channel inventory came down. The outlook writes that supply constraints will drag gaming in Q1 FY27 and after. Scarcity is the same leading-edge logic, packaging, and HBM being fed to the data center first. It is not a published cut of how many tens of thousands of cards. It is an admission that consumer cards and the data center compete for the same supply, and the consumer end is squeezed.

The difference from a backdoor: this sentence is a public finance write-up. It can enter the body. A unified compute architecture explains why switching stacks is hard. It does not explain a quarter of scarce gaming cards. Do not weld the two into one sentence.

## 4. Analysis add

### 4.1 After the sales unit moves up, the comparison object changes

Analysis add. Once the cabinet is the default sales unit, comparison moves from single-card FLOPs to whether you can enter the domain. Inside a 72-card high-speed interconnect, 72 dice act as one logic chip. The customer is not buying 72 cards and then finding a switch. The customer is buying a hall unit already welded. The next generation is still bought inside this domain. Referee and athlete are welded shut. The 8-card board is a transition. The CFO write-up writes the transition as from a small NVLink-8 plus InfiniBand to a large NVLink-72. Sales unit: card, to 8-card board, to 72-card cabinet.

The CPU is not extinguished inside the cabinet. 36 Grace, 2,592 cores, and 17 TB of LPDDR prove it made the CPU a cabinet accessory, not that it announced the CPU gone. The profit center has already moved to the accelerator. Scheduling and the edge still need a CPU. Downgrade is not extinction. Consumer CPUs and whole PCs are not the current disclosed main line. They may extend. There are no shipments and no revenue. Do not invent them. Game consoles do not make a brand now. They already make silicon. That is an existing fact beside the scenario, not a forecast that whole PCs have already been absorbed.

### 4.2 Cheapness alone does not punch through

Analysis add. The China stack, the AMD stack, and the Intel stack can be cheaper in hardware. The switching tax is rewriting kernels, rebuilding cluster scheduling, and re-validating models. A 75% pad lets it follow a price cut down. The China stack survives on people who cannot buy, not on cheapness punching through a unified compute architecture. Three layers: [Volume 12](vol-12.en.md). This volume does not reopen a prospectus. To get AMD, Intel, Apple, and Qualcomm off TSMC's queue, the third item is export control and trust. The gate is law, not yield. Those firms are still in TSMC's queue. In the queue they sit behind NVIDIA.

### 4.3 Bundling still misses three checks

Acting alone can weaken a buyer's position in the next scarce increment, but supplier allocation is not determined by whether TSMC would "offend" one customer. The testable mechanism is multi-variable: long-duration demand, prepayment, credit quality, utilization, and roadmap certainty can tilt incremental capacity toward the strongest bid, while TSMC still values customer diversification, geopolitical resilience, and long-run bargaining power. The 19% historical revenue share is therefore not a safe-distance metric, and neither is it proof of automatic exclusivity.

To change the allocation, bind three checks. First, prepayments large enough that TSMC cannot recognize only one buyer. Second, software bound into one stack, so the switching tax becomes a change of base rather than a change of vendor; UXL and oneAPI are embryos. Third, memory longs that leave a line for commodity bits. Miss one check and you are still picked off one by one. Apple does not bid against AMD for cabinets. What can actually change the cabinet is the bundle that makes accelerator cards and cloud ASICs. Phone makers bind residual memory.

A neutral foundry pledge has no consideration in front of a check. This is not a moral judgment. It is a board answering to shareholders. When the first name's profit exceeds the increment from everyone else, leaving a line for the second name is handing the high-margin increment to someone else. Seller 59.9% and 49% are already high, and those firms still expand to its mix. They are not the firms bidding against it for cabinets.

### 4.4 The engine and the five interrupts

Hypothesis from here: demand pushes profit, profit pushes commitments, commitments lock capacity and HBM, rivals' costs rise, deliveries slow, profits thin, they have even less money to bind longs and switch stacks, and share widens again. That is the engine. The five interrupts are in [Volume 8](vol-08.en.md). What is done is only supply commitments to $119.0B. Inquiries exist. Complaints do not. If those five are not done, the line walks past half of the scarce slice. The world does not blow up. Upgrades stop one node down. One firm writes the rules.

### 4.5 Whole-system OEM is a scenario, not a forecast

Analysis add. Rivals are all still here today. There is no official "already extinguished" series for CPUs, phone SoCs, or x86 attach. Do not write who exits in which year. The mechanism can be written: if CUDA plus the cabinet reference design locks, brand machines move from defining their own product to assembling to a drawing. The AI-server and workstation slice has already started. Chip foundry is still TSMC. Dell, Lenovo, ASUS, and HP can become whole-system CMs, an Apple-to-Foxconn structure, not wafer fabs. What can be checked: whether OEM AI servers are only an approved list; whether consumer-notebook CPUs can still ship a non-NVIDIA option; whether AMD and Intel accelerated-compute revenue disappears from filings. If there is no number, leave it empty. Hang it under expansion after demand steadies. Mark it a scenario. Do not put it in this volume's conclusion as a trust already completed.

### 4.6 Checks that can be tested

Speak when there is a number. Leave it empty when there is not. Whether data-center revenue is still sold as cabinets, and whether hyperscale is still about half. Whether supply commitments keep rising or start to shrink. Whether packaging-and-test revenue walks to the low-teens outlook, and whether C.C. Wei still says it limits customer growth. Whether TSMC's first-customer share keeps walking up from 19%, and whether HPC stays above 58%. Whether gaming is still written by the company as supply-constrained. Whether inference microservices are disclosed as their own revenue. Whether a cloud ASIC splits the 72-card domain on training, not only shunts inference. Whether the West shows bundled prepayments large enough that TSMC cannot recognize only one buyer. Whether the East shows a second bid that can take Western GDS. Whether power stops the buildout. These are checks, not a forecast timetable.

## 5. Gaps and what this volume cannot write as fact

A dollar bill of materials, software and brand premium 40% to 45%, switch-chip gross margin above 85%, a cabinet leaving the factory at $2.60 million to $3.30 million: the draft has them; the official product page and 10-K do not. They do not enter the fact layer.

Packaging exclusive 60%, monthly-capacity path from 13k to 130k: sell-side or draft, not a TSMC split. Do not mix Morgan Stanley 595,000 wafers and Mizuho 630,000 wafers into one official table. There is no official number for how many B200 packages come off one packaging wafer. 5.39 is an estimate. The 835,000-cabinet pool is the wrong pool. Void it.

PTX 95%, AMD trailing 30% to 50%: no sample. A unified compute architecture is an interface fact, not a citable share.

A backdoor already happened: no forensics. Distilling every model house's data: no judicial or audit material. A privileged position can be written. Theft cannot.

Inference-microservice ARR: no split. Multi-year cloud-service commitments $27.0B to $30.0B, officially for R&D, not confirmed cloud revenue.

The trust already complete, rivals no longer exist, Dells already become CMs: scenarios, not the present. There is no official "already extinguished" CPU attach series.

How much prepaid to TSMC, Hynix, and Samsung each: no official split was found. Locking next-generation 2nm first silicon as a disclosed contract: no prepayment sentence naming 2nm was found. The 10-K only writes prepaid manufacturing and capacity agreements for current and future products.

C.C. Wei at the shareholders' meeting, verbatim "sold out through 2026": official earnings calls are tight, cannot meet, limits growth. Do not promote it.

Samsung Taylor monthly capacity 16k / 24k / 40k: not in the announcement. Converting HPC 58% or 3nm 24% into tens of thousands of wafers: cannot. Writing TrendForce 72% as TSMC's own reported share: cannot.

NVIDIA net margin 55.6% and Intel 1999 net margin 25%: official text does not print them. This volume writes them only as back-calculations. Latest full gross margins for Apple, AMD, Qualcomm, and Huawei were not checked in this pass. Do not invent them. Limited supply of gaming cards has no quantity, and no allocation table of wafers, packaging, and HBM between gaming and data center.

This volume does not claim to have re-audited a full 10-K. Hard numbers sit on official sentences already opened in the main line, source 01, and source 02, plus the product page and the FY26 and Q1 FY27 press releases checked in this pass. A hypothesis from here can write a mechanism. It is not written as already having taken a percentage.
