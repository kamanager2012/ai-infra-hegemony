# Volume 28: Physical AI and the Real Bottlenecks in Robotics

Chinese original: [vol-28.md](../vol-28.md)

## 1. The question this volume answers

If embodied intelligence is to turn tokens inside a cabinet into torque on a factory floor or in a home, which parts carry the cost and the power? This volume takes apart only three things: the whole-machine BOM historical stress-test material gave; the physical break between edge compute and a cloud cabinet; and whether the actuator and sensor supply chain will copy the pattern of NVIDIA collecting a software premium.

The deeper pass already set the tone. Volume 28 hangs only on residual bits. It does not hang a new filing. Thor at 50W to 100W, more than 1000 TOPS, and actuators at 35% remain unverified engineering specifications. There is no whole-machine dollar figure and no shipment. What can be wired to the main line is only this: the default edge brain sits on the leading compute platform's module; consumer goods and robots compete with phones and PCs for the same residual bits. Cabinet selling prices are high enough that even expensive memory cannot crush the profit on one accelerator board. In PCs and phones, 16G from about 450 to 1800 breaks the whole machine first. The report does not treat that a robot revolution has already broken out.

Samsung's $16.54B long contract (announced at KRW 22.76T, through 2033) is Tesla. Musk named the Taylor fab for the sixth-generation automotive chip. That is a parallel foundry river for automotive AI. It is not proof of humanoid whole-machine shipments, and it is not a diversion of four-cloud training cabinets. Official cloud-ASIC memory specs (Maia / TPU / Trainium / MTIA) serve inference and training inside halls. They do not serve 50W to 100W next to a joint. The report does not treat two thermodynamic systems as one.

## 2. Evidence boundary

Robotics BOM structures vary substantially across humanoids, AMRs, industrial arms, autonomous vehicles, and drones. Historical 35% actuator / 20% perception / 25% compute shares, Jetson Thor power/TOPS figures, and whole-machine cost assumptions therefore remain engineering hypotheses unless supported by a specific first-party BOM or production program.

The current framework relies on a narrower set of durable observations: cloud-side training and simulation remain compute intensive; edge control faces power, thermal, latency, safety, and battery constraints; actuators/reducers and sensors can be independent physical bottlenecks; and mass production requires yield, reliability, assembly, and maintenance economics that cannot be inferred from demonstrations.
## 3. Mechanism: two thermodynamic systems; residual bits reach the joint last

### 3.1 Cloud cabinet 120 kW; one edge chip 50W to 100W

A cloud cabinet is 120 kW. One edge Thor is 50W to 100W (historical stress-test values). Three orders of magnitude. Analysis added here: embodied intelligence cannot move "unified 13.4 TB of memory" next to a joint. The on-body model must be distilled, quantized, and cut into perceive–plan–control layers. Heavy retraining and mass simulation can stay in the cloud. The online loop must live inside 50W to 100W and battery energy density. Whoever controls the cloud training fabric controls the robot's "brain before it leaves the factory." Whoever controls supply and the SDK for the 50W-to-100W module controls the "brain after it leaves." historical stress-test material wrote the latter as Jetson Thor, which hands the default edge seat to NVIDIA.

The judgment's official single cabinet is 72 GPUs, 36 Grace, 13.4 TB HBM, 17 TB LPDDR. Grace exists on the server side. That means they do not want to leave the CPU slice to a rival either. A demotion is not an extinction. Thor next to a joint is an accelerator, not a general server CPU. Automotive FY25 $1,694M shows that profit is not in the old general automotive-electronics scope. It also does not prove humanoids have entered that segment. No shipments. The report does not treat share.

### 3.2 BOM power is not in the GPU. It is in whether the machine can turn

Actuators plus reducers at 35% sit above compute at 25% and perception at 20% (historical stress-test values). Analysis added here: yield, noise, life, and unit price on harmonic reducers, planetary roller screws, and frameless torque motors decide whether a whole machine can walk from prototype to a line. That is the same class of constraint as advanced packaging being tight and unable to meet demand. The relevant scarcity is repeatable, reliable manufacturing at scale rather than demonstration performance. C.C. Wei, 4Q24: CoWoS tight / cannot meet demand. 2Q26: limits customers' growth. Packaging and test revenue about 8% in 2024, a bit over 10% in 2025. CoWoS monthly capacity from 13k to 130k wafers is a draft number in the Volume 24 title. It is not a TSMC split. This volume does not promote it to verified. If reducers, screws, or actuators remain concentrated and slow to scale, robotics can develop a physical bottleneck independent of the compute platform. Gross margin need not reach 60% to 75%. Lead time can still freeze the whole machine.

The remaining 20% is unsplit. Battery and structure can invert the ranking. 35 / 20 / 25 are shares, not an first-party cost book. There is no whole-machine dollar BOM, no annual volume, and no revenue or shipments from any whole-machine company. Frameless torque motors, harmonic reducers, and planetary roller screws have no unit prices, lead times, or supplier shares. The report does not infer them.

### 3.3 Perception at 20% is reliability and litigation cost

Six-axis force, tactile, binocular (historical stress-test material's list) decide whether a robot can stop its hand under unknown contact force. Analysis added here: a cloud model's error is a wrong token. A robot's error is a newton. Closed-loop frequency, calibration, and redundancy in perception and control are not directly improved by MLA's 93.3% KV compression. Stuffing a language model into a joint does not solve force control. Cloud-side MLA cutting KV by 93.3% and lifting concurrency nearly 10x is a memory ledger for text decode. Joint servos want deterministic latency and force feedback, not more tokens per second. Using a large model as a real-time controller steps on the memory wall and the control-system sampling-period wall at once. A practical architecture therefore separates cloud-side training/simulation from edge inference, deterministic control, and safe-stop functions. Liquid-cooling CDUs and nuclear metrics in the investment guidance serve the first half, simulation and training, not the joint itself.

### 3.4 NVIDIA can extend its platform, but robotics economics are different from rack-scale AI

software/platform premium inside a cloud cabinet at 40% to 45%, $1.10M to $1.40M (historical stress-test values), is an estimate, not a 10-K. Thor is written only as 50W to 100W and more than 1000 TOPS. There is no module unit price, no precision (INT8, FP8, or sparse), and no supply volume. Analysis added here: if whole-machine price sits more than an order of magnitude below a cabinet (historical stress-test material gave no whole-machine dollar price, so do not invent one), the absolute dollars in a 25% compute BOM are limited. NVIDIA is more likely to collect rent on volume and on a CUDA / Isaac-class software stack than on a $1.10M premium per unit. Whether it locks depends on whether whole-machine makers can run the same control graph off Thor. Nemotron / NeMo / NIM exist. There is no split. The report does not treat the model player as a second robot profit pool.

FY26 gross margin 71.1%, quarterly 75.0%. However expensive the whole cabinet, a memory price rise can be swallowed. Cabinet selling prices are high enough that even expensive memory cannot crush the profit on one accelerator board. In PCs and phones the memory share is high. 16G from about 450 to 1800 breaks the whole machine first. If a robot stuffs consumer-grade bits into a joint controller, what breaks first is the whole-machine BOM, not cabinet profit.

### 3.5 Residual bits: robots bid against phones and PCs for the same bits

After makers shift lines to HBM, consumer bits shrink. HBM eats about three times the wafer of ordinary DRAM per GB. Move one line and residual bits shrink more. TrendForce: HBM plus RDIMM about 51% of 2026 DRAM bit supply. More than half of the memory increment already goes to cabinets. Channel: 16G DDR5 about 450 to 1800. Supply cannot keep up with cabinets times spec. What remains is split among phones, PCs, consumer drives, and robots — a few dozen brands. HDDs are not inside the cabinet. They sit next to cloud storage and are still sucked by hall budgets.

CXMT's prospectus contains no disclosed HBM product line, and public wafer-per-month figures should not be promoted without a primary source. Domestic memory therefore does not automatically subsidize domestic robotics. The layered conclusion is more precise: **China has a stronger parallel-supply base in smartphones, consumer computing, and many electromechanical components, while a high-end local AI/robotics stack still depends on advanced compute, HBM-class memory, packaging, interconnect, and software closing together.** If a robot needs scarce high-end components, it still participates in those resource markets.

### 3.6 Official cloud-ASIC sentences serve halls, not joints

Specs: [Volume 4](vol-04.md). This volume does not reopen them. Those specs explain pre-shipment simulation and cloud-side skill learning. They do not explain a 50W-to-100W online loop. Cloud ASICs stop in the hall. The edge default is still written as Thor. Do not weld two thermodynamic systems into one sentence that says "self-designed chips have already liberated robots."

### 3.7 The Samsung long is Tesla, not humanoid shipments

Samsung announced KRW 22.76T, about $16.544B, through 31 December 2033. The counterparty is written as a large global company, about 7.6% of its then-expected 2024 revenue. The announcement does not write Taylor, does not write wafers per month, and does not write Tesla. Musk that day named the Texas Taylor fab for the sixth-generation automotive chip. 16,000 / 24,000 / 40,000 wafers per month are not in any announcement. A 55% 2nm yield is not official. TrendForce 2026 Q1 Samsung foundry share 6.5%. This line is automotive AI. It is not a foundry quota for humanoid whole-machine makers, and it is not four-cloud cabinets. SMIC at 5.1% cannot take Western masks. Intel Foundry is not in the pure-foundry top ten. Rapidus is not in volume. Robot whole machines have no second leading-edge logic river to flee to. If the edge continues to be written with a Blackwell core, it still bids against cabinets in the same slot queue.

### 3.8 Geography: actuator supply and chip supply sit in different places

Harmonic reducers, roller screws, frameless torque motors, and other precision components sit closer to East Asian manufacturing strength than frontier HBM/advanced packaging does. Export controls can constrain high-end compute without constraining every actuator at the same time. Conversely, if reducers or screws become the bottleneck, a country strong in precision manufacturing can hold more bargaining power in embodied intelligence than it does in a frontier data-center fabric. That does **not** mean the high-end local AI loop is already closed: advanced compute, memory, packaging, interconnect, and software remain separate constraints.

NVIDIA supply commitments rose from $95.2B at FY26 year-end to $119.0B at Q1 FY27, most payable on a near-term schedule. TSMC's 2025 HPC mix was 58%, up 48% year on year. These facts support a **resource-competition mechanism**, not an automatic "pay more or get nothing" rule. Price, long-duration demand, prepayment, credit, utilization, roadmap certainty, supplier diversification, and geopolitics all influence allocation. A robot edge module that requires frontier logic/HBM therefore competes for scarce inputs, but the outcome is not determined by gross margin alone.

## 4. Scenarios, counterarguments, and testable indicators

New quantities not given are unverified. Do not treat them as first-party fact.

Scenario A: Closed factory scenes scale first. Fixed stations, known loads. The 35% actuators can follow industrial-robot cost-down. Thor-class modules do vision and dispatch only. Testable: whether whole-machine makers publish actuator localization rates and hours to failure; whether they still treat "humanoid" as a necessary form.

Scenario B: Edge compute is locked on NVIDIA. More than 1000 TOPS / 50W to 100W becomes the de facto standard. The control stack is bound to the same ecosystem. Testable: whether a non-NVIDIA module can publish a checkable TOPS/W and SDK maturity on a public benchmark. Unverified: this volume does not forecast Thor share.

Scenario C: Cloud-side depreciation delays embodiment. Mixed-year $211.9B to $213.9B, the 2025 mixed year about $354.0B, and historical stress-test material's $45B to $55B annual depreciation force capital to protect data-center returns first. Robot whole-machine financing is pushed back. Testable: whether whole-machine financing and capex move with four-cloud capex year on year, or lag it clearly.

Scenario D: A residual-memory pressure breaks consumer whole machines first, then home robots. If 16G 450 to 1800 holds, electronics outside battery and structure break first. Testable: whether consumer memory prices still sit at that channel-verbal magnitude; whether whole-machine BOMs rewrite compute 25% as cheaper microcontrollers.

Counters. First, BOM shares are draft engineering experience with no sample. A production vehicle may make battery or structure the largest item. 35 / 20 / 25 then fail. Second, industrial arms already do most factory motion. "Humanoid" is not a necessary form. Third, open-source models plus domestic actuators can take compute 25% off NVIDIA and leave only the physical wall of motors and reducers. Fourth, if the clouds officially retreat inference mainstay to commodity memory, the cost anchor of pre-shipment simulation changes. All four now write HBM.

### 3.9 Cabinets times spec is demand, not robot shipments

One official rack reference contains 72 GPUs, 36 Grace CPUs, 13.4 TB HBM, and 17 TB LPDDR. Multiplying that specification by 10k / 30k / 50k hypothetical racks gives demand tonnage, not disclosed sales. **Micron provides A-grade first-party evidence that HBM3E requires about 3× the wafer supply of DDR5 at the same node and bit capacity.** The report's **5.39 CoWoS wafers-per-rack coefficient is D-grade geometry**, not a TSMC disclosure. These two inputs should not be merged into one certainty level. The mechanism for robotics is residual-capacity pressure: edge devices that do not need frontier packaging can avoid some AI bottlenecks; edge devices that do require frontier logic/HBM still compete with data-center demand.

Two B200 dice about 800 mm² at the reticle limit (Electronic Design / IEEE Spectrum). H100 814 mm² (NVIDIA blog). The reticle limit explains why one die fills an interposer in a hall. It does not explain why next to a joint the budget can only be 50W to 100W. The two thermodynamic systems differ in area too. Putting the hall reticle-limit story on Thor is the wrong layer.

Gaming FY25 $11,350M against data center FY26 $193,737M is not the same fiscal year. Use it only as a magnitude check. Q4 FY25 Gaming −11% year on year, −22% sequential. The official sentence is limited supply for Blackwell and Ada. It is not "they have already disclosed how many tens of thousands of gaming cards were cut." It admits consumer cards and the data center bid for the same supply. If Thor uses a Blackwell core, it sits inside that supply sentence. Wafers, advanced packaging, and HBM feed the data center at 71.1% to 75.0% gross margin first. The edge module is residual.

### 3.10 Prepayments and the HPC increment do not yield to humanoids

Supply commitments rose from $95.2B to $119.0B in one quarter. TSMC HPC 58%, up 48% year on year. What is being opened is HPC and packaging. Apple locks phone logic. Booked 19% is not a safe distance. Humanoid whole-machine makers are not the first customer and not the second. Want the same 3nm and HBM and you pay more, or you do not get it. Microsoft Intelligent Cloud FY25 $106.265B is large. It is still a cloud buyer placing its own orders, not capacity already bundled for robots. Four-cloud 2025 mixed year about $354.0B is an each-for-itself sum. Of the five interrupts, the ones that touch this volume are power stopping the buildout, and memory longs that leave a line for commodity bits. Neither is done. Until they are, the residual-memory pressure keeps hitting joint controllers and consumer whole machines.

C.C. Wei, 4Q24: CoWoS tight / cannot meet demand. 2Q26: limits customers' growth. Packaging and test about 8% in 2024, a bit over 10% in 2025. "Sold out through 2026" at the shareholders' meeting has no official transcript. Do not promote it. NVL72 at $3M a cabinet and whole-cabinet software premium $1.10M to $1.40M are estimates, not a 10-K. This volume does not write them as unit-price anchors for robot modules.

### 3.11 On the joint the software stack collects SDK/platform switching cost, not a whole-cabinet premium

The 40% to 45% software/platform premium inside a cloud cabinet corresponds to CUDA, an inference engine, and a cabinet standard. It is an estimate, not a segment filing. Next to a joint there is no 72-card fabric and no 130 TB/s backplane. If an Isaac-class control stack locks, what it collects is an SDK and a sim-to-real migration tax, not $1.10M per unit. Whether it locks still depends on whether whole-machine makers can run the same control graph off Thor. Open-source models plus domestic actuators can take compute 25%. That counter holds only if a checkable substitute module exists at 50W to 100W and more than 1000 TOPS. This volume has no such public benchmark. The report does not infer share.

The old "under 5% rewrite" figure for CANN migration remains a draft number unless independently reproduced. More importantly, cloud-side model migration is not the same thing as joint-level robotics control. A domestic robot stack can be strong in actuators, sensors, manufacturing, and edge control while still facing constraints in frontier compute, HBM-class memory, advanced packaging, and software ecosystems. The correct conclusion is **layered capability**, not "China stops at phones" and not "one good-enough domestic rack closes the whole embodied-intelligence stack."

A search of the four official domains found no sentence that says "5nm + DDR5 as the main robot brain." Maia 200 writes N3 plus HBM3e. Trainium3 writes 3nm plus HBM3e. Ironwood writes HBM3E. MTIA 300 onward writes HBM stacks. Those sentences serve simulation halls. After shipment, 50W to 100W is still written as Thor. Two thermodynamic systems, two memories, two powers. This volume hangs only on residual bits. It does not write either set as a revolution that has already broken out.

### 3.12 This volume stops at the layer it can write

Actuators 35%, perception 20%, compute 25% are unverified BOM shares. Thor 50W to 100W, more than 1000 TOPS, are unverified engineering specifications. Cloud-side 120 kW and the official single cabinet 13.4 TB plus 17 TB are the comparison. Residual 51% and channel 450 to 1800 are the memory side. Samsung $16.54B is Tesla. The four ASIC official sentences serve halls. All of the above can be written. Whole-machine dollars, annual volume, module unit price, reducer share, and a humanoid outbreak already here cannot be written. Do not fill what is missing.

Consumer-card limited supply is a public financial write-up, not an accusation. Edge modules and cabinets bid for the same Blackwell and Ada supply. Whoever can prepay takes first. Whole-machine makers cannot prepay at the $119.0B band, so they take residual. Residual has a price. 450 to 1800 is channel-verbal, not a 10-K. You can buy it. The price is higher.

Stop first at the layer that can be written. Below, the judgment and the cloud self-design sources nail pre-shipment simulation again. The report does not treat that a revolution has broken out. The report does not treat module share. The report does not treat whole-machine dollars.

### 3.13 Official memory specs at the four firms

See [Volume 4](vol-04.md). This volume does not reopen them.

### 3.14 Of the five interrupts, the one that truly touches this volume is cloud self-design taking training

The five: [Volume 8](vol-08.md). This volume asks only: if simulation still runs on the scarce slice, the joint has already paid cloud-infrastructure cost before it leaves the factory. Only taking training changes that layer. Public next generations have not taken it.

### 3.15 cloud-infrastructure cost before shipment; residual-memory pressure after

Rent: [Volume 1](vol-01.md). Four-cloud scope: [Volume 8](vol-08.md). If a robot whole machine still has to pass cloud-side simulation, it pays this rent first. If after shipment it stuffs consumer-grade bits into a joint controller, it then pays a residual-memory pressure. Do not weld the two into one "robot-revolution capex." Humanoid whole machines have no window of their own. They borrow the few years before halls are locked.

Memory as a share of major cloud capex: 47% in 2026, 68% in 2027. More than half of the memory increment already goes to cabinets. 51% of 2026 DRAM bits are HBM plus registered DIMMs. Micron FY24 Q3 prepared remarks disclose that, industry-wide, HBM3E requires approximately **3× the wafer supply of DDR5** to produce a given number of bits in the same technology node; Micron's FY25 10-K later confirms that HBM requires more wafers and cleanroom space for the same bits. The ~3× ratio is A-grade first-party evidence, not merely a conference paraphrase, while still not being a universal fab-control constant. Hynix: HBM revenue more than doubled in a year. After makers shift, consumer bits shrink. Robots, phones, PCs, and consumer drives split the same residual pool. Channel-verbal 16G DDR5 from about 450 to 1800. You can buy it. The price is higher. Cabinet selling prices are high enough that even expensive memory cannot crush the profit on one accelerator board. In PCs and phones the memory share is high. The whole machine breaks first. If electronics in a robot BOM price with the consumer, what breaks first is also the whole machine, not cabinet profit.

### 3.16 5nm plus ordinary memory to beat old cards still needs someone to make it

See [Volume 4](vol-04.md). This volume does not reopen it. If the edge continues to be written with a Blackwell core, it still bids against cabinets in the same slot queue.

### 3.17 Three China-stack layers land on the joint

Three layers: [Volume 12](vol-12.md). This volume does not reopen them. Joint actuator supply can sit at home. Leading-edge logic for the edge does not pass the gate. The layer is wrong, not the clock.

### 3.18 For simulation to beat today's cabinet, you return to the scarce slice and bid

Embodied-intelligence training is not done next to a joint. Heavy retraining, mass simulation, and skill distillation land on the cloud fabric. Public next generations of that fabric: all four write HBM and a more advanced node. Microsoft's 200-generation: 3nm, 216 GB, 7 TB/s. Google Ironwood: 192 GB, about 7.4 TB/s, eight stacks. Amazon's third generation: 144 GB, 4.9 TB/s. Meta from the 300 generation writes HBM stacks and names Broadcom. Those specs and the leading compute platform's whole cabinet bid for the same material. Cloud self-design hits the die. It does not hit the cash used to prepay at 71% to 75%.

To actually dodge, the clouds would have to take a lower tier of performance in exchange for material: stop at 5nm, use less advanced packaging, put main memory back on commodity DIMMs. Public next generations have not stopped. If they do not stop, the pre-shipment brain keeps bidding against 75% gross margin. The post-shipment brain keeps being written as 50W to 100W and more than 1000 TOPS. Two thermodynamic systems, two memories, two powers. This volume hangs only on residual bits. It does not write either set as a revolution that has already broken out.

## 4 continued. Three more scenarios

New quantities not given are unverified. Do not treat them as first-party fact.

Scenario E: Cloud self-design actually takes training. Pre-shipment simulation leaves the leading compute platform's cabinet. Whole-machine makers pay one less cloud-infrastructure cost. Testable: whether the four official spec pages still write main memory as HBM; whether a sentence appears that says "retreat to commodity DIMMs as the simulation mainstay." None now. Unverified: this volume does not forecast the year of a retreat.

Scenario F: Actuators become a non-NVIDIA bottleneck party. Lead times on harmonics, screws, and frameless motors freeze the whole machine. Gross margin need not reach 60% to 75%. Testable: whether whole-machine makers publish lead times and localization rates on those three; whether a line stops for reducer lead time. No unit prices. The report does not infer share.

Scenario G: The near gate freezes only the edge module. Motors can still ship. Export controls freeze the leading compute platform's module and high-end accelerators. They need not freeze motors at the same time. Testable: whether the control list names the edge module; whether whole-machine makers publish a control stack that excludes the leading compute platform's module. historical stress-test material gave no volumes for Chinese robot parts. The above is structural inference only.

Scenario H: Capital first protects hall returns. Whole-machine financing lags clearly. Mixed-year $211.9B to $213.9B, and the 2025 mixed year about $354.0B, are not robot capex. Testable: whether whole-machine financing and capex move with four-cloud capex year on year, or lag it clearly. $45B to $55B annual depreciation is a draft template, not a sum of four annual-report asset classes. Do not make it a new anchor.

Two more counters. Fifth, the four cloud buyers are large enough. Intelligent Cloud $106.265B, 2025 mixed year about $354.0B, can press athlete selling prices with volume. the platform-control layers need not collapse into a single rent. That is not a disclosure of how many simulation machine-hours any one of them reserved for humanoid whole machines. Testable, fill when a number exists: whether data-center revenue growth falls to single digits; whether packaging and test share crosses 10% as TSMC said; whether the four official spec pages still write main memory as HBM; whether channel 16G still sits at the verbal 450-to-1800 band; whether whole-machine makers publish actuator localization rates and hours to failure. If not, leave them empty. Whole-machine dollars, annual volume, module unit price, reducer share stay empty.

## 5. Gaps and what cannot be treated as fact

There is no whole-machine dollar BOM, no annual volume, and no revenue or shipments from any whole-machine company. 35%, 20%, and 25% are shares, not an first-party cost book. The remaining 20% is unsplit. Battery and structure can invert the ranking. Jetson Thor "more than 1000 TOPS" gives no precision, no module price, and no supply volume. Frameless torque motors, harmonic reducers, and planetary roller screws have no unit prices, lead times, or supplier shares. Putting cloud-side $215B depreciation on robots is cross-volume boilerplate, not a capital flow this volume measured. This volume does not claim that a mass-market robotics shipment inflection has already occurred. Unverified. Do not treat as first-party fact. Samsung wafers per month, ASIC TCO-save percentages, and $3M per whole cabinet are not written. Automotive $1,694M cannot be written as humanoid revenue. No official Google sentence naming TSMC was found. No official AWS sentence that TSMC is the foundry was found. No MTIA 300-generation sentence naming 3nm was found. Those three stay empty.
