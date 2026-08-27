# Volume 4: TSMC, 2nm, and the fight for leading-edge manufacturing (ASML High-NA EUV and foundry premiums)

Chinese original: [vol-04.md](vol-04.en.md)

## 1. The question this volume answers

Is the fight for leading-edge manufacturing on a 2nm price list, or on slots for packaging and first-to-market nodes? Can Apple still lock next year's new lines? Is booked first-customer 19% a safe distance? Is 835,000 cabinets locking 3nm the right pool?

This volume does not invent lithography-tool prices, 2nm-fab costs, or customer-level wafer allocations. It uses what TSMC reports directly: shipments, wafer-revenue mix, platforms, customer concentration, packaging/test share, and management statements on tightness. Foundry concentration and customer-specific CoWoS estimates remain institutional or sell-side evidence. Prepayments and profit connect through a **resource-allocation mechanism**: price, long-duration orders, prepayment, customer credit, utilization, roadmap certainty, diversification, and geopolitics all matter. No single gross-margin comparison proves how TSMC must allocate capacity.

The main line nails this: the increment is HPC; booked 19% is not a safe distance. Occupy the increment and next year's slots belong to the first name. The binding line is CoWoS. About 100k cabinets take more than half of this packaging line. You do not need 800,000 cabinets to lock 3nm. 835,000 cabinets equals 4.5 million wafers divided by 5.39. The pool is wrong. This volume writes that line. It does not start a separate price war.

Public pages opened and checked in this pass: TSMC 2025 annual-report site, annual-report chapters 5 and 6, 4Q25 management report and earnings-call transcript, 2Q26 earnings-call transcript, TrendForce 12 June 2026 press release, NVIDIA 72-card cabinet product page, NVIDIA FY26 CFO commentary and press release, NVIDIA Q1 FY27 CFO commentary. Second-hand paraphrase is not promoted. Official splits that were not found stay empty.

## 2. What the draft already argued (compressed; key numbers kept)

The draft Volume 4 title is TSMC, 2nm, and the fight for leading-edge manufacturing, with a subtitle hanging High-NA EUV and a leading-edge foundry premium. The body almost pastes Volume 2's cabinet bill of materials whole. Manufacturing hard numbers are not actually in Volume 4. The discussion draft already judged: the table of contents spins empty; the title is the coach; the body is a repeated cabinet.

What the draft left, and what this volume must mark as draft numbers and not use as a base, are these sets. High-NA $380 million a tool. A single 2nm fab $20B to $25B. A wafer-price table from $10,000 at 7nm to $30,000–$35,000 at 2nm. Actual foundry share 95%. Packaging monthly capacity climbing from 13k wafers to 130k. Cabinet ex-factory reference ASP $2.60 million to $3.30 million, of which packaging $150k–$200k, GPU dice $280k–$350k, HBM $580k–$680k, software and brand premium $1.10 million to $1.40 million. Four-cloud 2024 capex $215B. Downstream chip procurement cost up 20% to 30%. The draft has these numbers. TSMC's annual report, earnings calls, and the NVIDIA product page do not disclose them on this scope. This volume keeps them, demoted to draft claims.

What in the draft can actually join this volume's main line is not a price list. It is the direction of three walls: the memory wall, the interconnect wall, the thermodynamics wall. As the node walks down, a single die still cannot hold the I/O HBM needs. The packaging fight will not end because 2nm enters volume. A middle road can be written: the node name stops at 3nm, packaging climbs with tightness, power stays at TSMC, and the rent line item changes from smaller transistors to more interposer. That sentence is a mechanism, not a filing line that already happened.

The draft also wrote foundry share as 95%. This volume does not use that assertion. What can be publicly measured is two different scopes: TSMC's own annual-report foundry 2.0 industry share, 40% in 2025 and 34% in 2024; TrendForce on traditional foundry revenue, TSMC about 72% in 2026 Q1. Both are revenue share. Neither is wafers. Neither can be written as TSMC's own reported leading-edge logic wafer share. Public high-end AI logic volume is still mostly TSMC, with Samsung as a parallel line. SMIC 5.1% cannot take Western GDS.

## 3. Official and institutional sources

### 3.1 Shipments, capacity, node revenue

TSMC 2025 shipments 15 million 12-inch equivalents; the management report writes 15,022 thousand. 2024 was 12.9 million, detail 12,910 thousand. Annual capacity above 17 million. 2026 shipment outlook 16 to 17 million is an outlook, not completed. Sources: TSMC 2025 annual-report site https://investor.tsmc.com/static/annualReports/2025/english/index.html ; the same sentence in the letter to shareholders; 4Q25 management report.

The annual report also writes: 2025 deployed 305 process technologies and manufactured 12,682 products for 534 customers. Four 12-inch GIGAFABs together already exceed 13 million 12-inch equivalents of capacity. Those sentences say there are many customers and a lot of capacity. They do not say the scarce slice is large. Of the 534, the top ten take 78%, the top two take 36%. Of the factory's 15 million wafers, most are not CoWoS.

There is no capacity or shipment wafer count by node. Nodes are all wafer-revenue share. Same management report. Full-year 2024, full-year 2025, 4Q25: 3nm 18%, 24%, 28%; 5nm 36%, 36%, 35%; 7nm 17%, 14%, 14%; 16/20nm 8%, 7%, 6%; 28nm 7%, 7%, 6%; 7nm and below 69%, 74%, 77%. Annual-report letter to shareholders, same scope: 3nm in its third year of volume, 24% of 2025 wafer revenue; advanced technologies 74% of wafer revenue, prior year 69%.

2nm: the annual report writes 4Q25 entered volume. The table has no separate 2nm row. Do not invent one. Do not convert 3nm 24% into 3.6 million wafers, and do not convert 7nm-and-below 74% into 11 million wafers. Leading-edge ASP is high. Revenue share is far larger than wafer share. 24 of revenue is far smaller than 24 of wafers. Every node percentage in this volume stops at revenue. It is not converted into tens of thousands of wafers.

### 3.2 Platforms: HPC up 48% in a year

Source: the same management report, plus the 4Q25 earnings-call transcript. CFO Wendell Huang original: full-year HPC up 48% year on year. Smartphone, IoT, and automotive up 11%, 15%, and 34%. DCE flat. Full-year HPC 58% of revenue, smartphone 29%, IoT 5%, automotive 5%, DCE 1%.

Annual-report position section, same scope: net revenue by platform, HPC 58%, smartphone 29%, IoT 5%, automotive 5%, DCE 1%, other 2%. 2024 control: HPC 51%, smartphone 35%, IoT 6%, automotive 5%. This is by application platform, not by customer. HPC includes AI, and also server CPUs, ASICs, and networking. Revenue share is not unit share.

2Q26 single quarter, HPC 66% of that quarter's revenue, up 20% sequentially. Source: 2Q26 earnings-call transcript. Control only, not a full year. However high a quarter goes, 66% cannot be written as full-year wafers.

HPC is not NVIDIA. Inside it are also AMD, Broadcom, and cloud ASICs. Smartphone is not Apple. Some of Apple's PC chips are classified into HPC. What can be nailed is direction: what is being opened is HPC and packaging, not phone logic. Smartphones still grew 11% for the year, but share fell from 35% to 29%. The increment pie is not there.

The annual report also splits geography by headquarters: North America 75%, Asia-Pacific excluding China and Japan 9%, China 9%, Japan 4%, EMEA 3%. China 9% is customer-headquarters scope, not the China market being able to change global cabinet allocation. The payer is in North America. The main line writes that the China market cannot save global cabinets, HBM, packaging, and a unified compute architecture. Geography 75% versus 9% is the same sentence's annual-report footnote.

### 3.3 Customers: first name jumped from 12% to 19%

The annual-report risk chapter names first and second, not customer names. Original: the ten largest customers in 2023, 2024, and 2025 accounted for about 70%, 76%, and 78% of net revenue. The largest customer accounted for 25%, 22%, and 19%. The second largest accounted for 11%, 12%, and 17%. Source: 2025 annual report chapter 6 https://investor.tsmc.com/static/annualReports/2025/english/pdf/2025_tsmc_ar_e_ch6.pdf

Revenue table Customer A, Customer B: 2025 Customer A NT$726,974,278 thousand, 19%, 2024 12%, amount NT$352,271,213 thousand. Customer B 2025 NT$645,178,671 thousand, 17%, 2024 22%, amount NT$624,345,477 thousand. Other 64% versus 66%. Total 2025 NT$3,809,054,272 thousand, 2024 NT$2,894,307,699 thousand. Source: annual report chapter 5, table titled customers accounting for at least 10% of annual consolidated net revenue.

What can be nailed: the first name jumped from 12% to 19%; the second fell from 22% to 17%. TSMC does not name them. Huang calling himself the largest customer is another line, not in TSMC's files. 19% is full-year revenue share. It cannot be converted into 19% of wafers. Voice on the scarce slice is larger than this booked number: what is being opened is HPC up 48%, not phones.

The main line's sentence lands here: booked 19% is not a safe distance. Occupy the increment and next year's slots belong to the first name. The top ten already take 78%. The second name falling from 22% means the full-year book is changing names. The scarce slice changes faster, because the scarce slice is the increment itself.

### 3.4 Packaging: official text only admits tight. It does not split CoWoS

4Q24 call, CFO Wendell Huang: we do not break down advanced packaging segments. Advanced packaging and test over 8% last year, will be over 10% this year. Source: 4Q24 transcript. C.C. Wei, same call: today it is all AI focused, capacity is very tight, and cannot even meet customers' need.

4Q25 call, corrected after the call: last year's advanced-packaging revenue contribution a bit over 10%, about 8% in 2024. Expected to grow faster than the company average, 2026 low teens. Source: 4Q25 transcript. What can be nailed: about 8% in 2024, a bit over 10% in 2025, 2026 outlook low teens. What cannot: CoWoS revenue alone, monthly capacity, packaging wafers by customer. The company is explicit that it does not split.

2Q26, C.C. Wei: our packaging capacity is so tight that now it limits my customers' growth. Same call: today the majority is still CoWoS. Source: 2Q26 transcript https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/547d1696765e05ce3adb81c108ce1c8c1682b80c/TSMC%202Q26%20Transcript.pdf Public write-up, same sentence. This pass's retrieval confirms the original is tight, limits growth, welcome a bit more elasticity in the market so the front-end wafer business can keep growing. Front-end is the bulk. The majority is still this packaging. Substitutes are being built to cut cost; the pilot line is about another year from maturity.

The six English words "sold out through 2026": several second-hand paraphrases hang them on the 4 June 2026 shareholders' meeting. The Focus Taiwan shareholders' meeting copy we opened has no CoWoS and no sold-out. What TSMC official transcripts can nail is the two sentences above: tight, cannot meet, already limits customer growth. Second-hand paraphrase is not promoted to an official sentence.

### 3.5 Foundry concentration (institutional)

Specified source: TrendForce press release 12 June 2026 https://www.trendforce.com/presscenter/news/20260612-13095.html Original: TSMC revenue up 6.3% sequentially, nearly $35.86 billion, share further to 72%. Samsung Foundry excluding System LSI, revenue down 5.8% sequentially, a bit over $3.2 billion, share slipped to 6.5%. SMIC revenue up 0.6% sequentially, $2.51 billion, share stable at 5.1%. Top ten together $47.95 billion, up 3.7% sequentially. UMC 3.9%, GlobalFoundries 3.3%.

The press release writes TSMC 72%. It does not print 72.3%. Businesskorea and the semiconductor-ecosystem write-up of the same set write 72.3%. This volume follows the specified press release: 72%, 6.5%, 5.1%. This is institutional revenue share, not wafers, not TSMC's own report. Annual-report foundry 2.0 40% is another industry definition. Do not fuse the two into one official table.

Public high-end AI logic volume is still mostly TSMC, with Samsung as a parallel line. SMIC 5.1% cannot take Western GDS. Export control is statute. Apple, AMD, and Qualcomm handing GDS to a China-controlled fab pass a license gate, not a yield gate. Eastern capacity coming up is a parallel bid, not a substitute seat for these names at TSMC.

### 3.6 Profit cash: who can add a prepayment tranche

FY26, supply commitments, and Intel 1999 are in [Volume 1](vol-01.en.md). This volume does not reopen the full table. This volume uses one sentence: TSMC gross margin 59.9% is already high, and what it still expands is lines and fixtures that walk the first name's mix. Whoever can prepay can add a tranche. A neutrality pledge has no consideration in front of a check. There is no line that says "paid TSMC X billion for packaging or 2nm first silicon." Do not invent one.

### 3.7 Wafers per cabinet and the wrong pool

Official 72-card cabinet materials: 72 Blackwell, 36 Grace, 13.4 TB HBM3E, 17 TB LPDDR5X. Source: https://www.nvidia.com/en-us/data-center/gb200-nvl72/ This pass opened the product-page spec table. The GPU-memory row writes 13.4 TB, the CPU-memory row writes 17 TB, high-speed interconnect 130 TB/s. Second-hand teardowns writing 13.5 or 13.8 do not replace the official table. Seventy-two GPU packages are the numerator of 5.39.

Die area: H100 official 814 mm², source NVIDIA Hopper technical blog. B200 two dice each about 800 mm², package total about 1,600 mm², nailed in Electronic Design and IEEE Spectrum, a reporter geometry sentence, not a product datasheet. A 300 mm wafer area is π times 150 squared, 70,686 mm². There is no official TSMC number for how many B200 packages come off one packaging wafer.

5.39 is an estimate: 72 packages divided by about 13.4 per wafer. 72 is official. 13.4 is a geometry working hypothesis. After two dice plus eight HBM stacks, the interposer is far larger than a single GPU. 70,686 divided by 1,600 is theoretically about 44; after edge, interposer, and stack occupancy, 13 to 15 per wafer is geometrically plausible. 5.39 is not fiction. It is also not logic wafers per cabinet for the whole factory.

Front-end logic is another line. GPU dice per cabinet: 72 times 2 equals 144. Theoretically about 72 per wafer; at 70% yield about 2.9 wafers per cabinet. Grace and switch chips are extra. Front-end does not match 5.39. Mixing them is the wrong pool.

835,000 cabinets equals 4.5 million wafers divided by 5.39. 4.5 million is 30% of full-year shipments of 15 million. 5.39 is packaging wafers per cabinet. Most of the 15 million are phones, MCUs, auto, and mature nodes. Dividing the whole factory, or 30% of it, by 5.39 yields a cabinet count with no physical meaning. Void it. Dividing 15,022 thousand by 5.39 yields about 2.78 million cabinets. That has no physical meaning either.

Sell-side tracking 2026 CoWoS demand about 1 million wafers, NVIDIA about 595,000 and 60%: Morgan Stanley via Longbridge, not TSMC. This pass did not open the Morgan Stanley original. The same paraphrase writes global demand 1 million wafers, TSMC monthly capacity from 32,000 in 2024 to 93,000 at end-2026, 515,000 from TSMC and 80,000 from Amkor and others, equally unofficial. Mizuho via Investing.com is another table at another date: monthly capacity 140,000, NVIDIA 630,000 wafers at TSMC. Do not mix them with 595,000 and 93,000 into one official table. A TSMC split does not exist.

At 5.39, half of sell-side 1 million wafers is 500,000 wafers, about 93,000 cabinets. NVIDIA tracked about 595,000 wafers, about 110,000 cabinets. Rounded: about 100k cabinets take more than half of this packaging line. You do not need 800,000 cabinets to lock 3nm. 800,000 cabinets times 5.39 is about 4.31 million wafers, near 30% of the factory, and 60% 3nm-plus-5nm revenue share is not the same dimension. 60 is revenue, not wafers.

### 3.8 Samsung Taylor long: a parallel line, not a substitute seat

Samsung, 28 July 2025 filing: semiconductor foundry supply agreement, KRW 22.7647T, about $16.54416B, at that day's open 1,376 won per dollar. Counterparty written as a large global company, start 24 July 2025, end 31 December 2033. The filing does not write Taylor, does not write wafers per month, and does not write Tesla. Source: Samsung IR single sale and supply disclosure.

Musk named it: Samsung's new Texas fab will be dedicated to Tesla's next-generation AI6. Reuters lead writes Tesla signed a $16.5 billion deal to source from Samsung. Musk also said TSMC makes AI5, first in Taiwan then Arizona. That is Musk's line split, not Samsung's filing. 16k / 24k / 40k wafers per month: not in the filing, Reuters, or Musk. Do not write them.

This long proves Samsung is a parallel line that can take a customer willing to hand over GDS, such as Tesla. It does not prove Western flagship chips already have a second TSMC. TrendForce share 6.5% versus 72% is the same sentence's institutional footnote.

## 4. Dig into the mechanism

### 4.1 The observation point is whether packaging can deliver, not a ribbon-cutting

Analysis add. The short-term observation point of the manufacturing fight is whether packaging can deliver. As the node name walks down, a single die still cannot hold the I/O HBM needs. B200 already sits near the reticle limit. Another nanometer smaller saves transistor density. It does not save interposer area, and it does not save the occupancy of eight HBM stacks. The packaging fight will not end because 2nm enters volume. Middle road: the node name stops at 3nm, packaging climbs with tightness, power stays at TSMC, and the rent line item changes from smaller transistors to more interposer. C.C. Wei himself says the majority is still this packaging; substitutes are about another year from maturity. The window is not a ribbon-cutting. It is slots for fixtures and interposers.

What official text can nail dead is only: packaging is tight, cannot meet, already limits customer growth. The revenue line item is still only packaging and test a bit over 10%, outlook low teens. A 10% revenue line item jamming customer growth means what is jammed is not the factory's 15 million wafers. It is this slice. Putting the observation point on a 2nm-fab ribbon-cutting is watching the wrong layer.

### 4.2 Apple can lock phone logic. It cannot lock the increment and packaging

Analysis add. Apple can lock a large slice of phone leading-edge logic. It cannot lock the increment and packaging. It just went from ten-year first name to second, still about 17%. Other phone brands split what is left inside the 29% smartphone platform. The smartphone platform still grew 11% for the year, but share dropped six points. Apple locking 3nm cannot save AMD's cabinets, and cannot save the slot for its own small slice of PC chips inside HPC. Even if PC chips are classified into HPC, they still bid against training cabinets, cloud ASICs, and networking chips for the same first-to-market slice and the same packaging slice.

Hypothesis from here: if one platform maintains superior order scale, prepayment capacity, credit quality, utilization, and roadmap certainty, some **incremental** packaging and leading-edge capacity can tilt toward it. The historical 19% customer-revenue share is not a safe-distance metric and must not be converted into a wafer or CoWoS share. The counterweight is a credible second bid plus substitutable system stacks and sufficient memory/power supply—not a claim that TSMC is financially unable to diversify customers.

### 4.3 Prepayments are reproduction. The clouds are not unarmed

The mechanism is in [Volume 1](vol-01.en.md). This volume lands it on the manufacturing end: lock the increment; you need not first take half the factory. Half the factory is the pool of phones plus MCUs plus auto plus mature nodes. Past half of the scarce slice, on a sell-side 1-million-wafer pool, is about 100k cabinets. The two pools differ by an order of magnitude. The wrong pool yields a sentence with no physical meaning, such as needing 800,000 cabinets to lock 3nm.

### 4.4 5.39 only divides packaging, not 15 million

Analysis add. The identity is cabinets times wafers per cabinet, equal to demand on this TSMC slice. Supply minus demand equals residual left for others. This slice must be chosen first. Choose front-end logic, and the coefficient is about 2.9 GPU-die wafers per cabinet; the pool is 3nm or 4nm-class, not the whole factory. Choose packaging, and the coefficient is 5.39; the pool is this packaging's annual wafers, not 15 million.

The 835,000-cabinet error is taking a packaging coefficient and dividing 30% of the whole factory. Thirty percent of the factory includes a large number of wafers that will never enter a 72-card cabinet. The cabinet count you get cannot be used to talk about locking 3nm, and cannot be used to talk about locking 2nm. 800,000 cabinets times 5.39 is about 4.31 million wafers, looking like 29% of the factory, also like some shadow of leading-edge revenue share, but revenue share is not wafers. 3nm plus 5nm at 60% is money, not wafers. Writing 800,000 cabinets as locking 50% of 3nm or 2nm is the wrong dimension.

Sell-side 1 million wafers, NVIDIA about 60%: the direction matches the main line; the coefficient is not an annual report. What official text can nail is tight. Past half at about 100k cabinets is a sell-side pool times an estimate coefficient. This volume writes 100k cabinets as an estimate conclusion, not as a cabinet count TSMC has already disclosed. NVIDIA does not report cabinet counts. TSMC does not report packaging wafers by customer. Any sentence that writes 100k cabinets as already shipped is over-translation.

### 4.5 Onshore US fabs solve an origin story. They do not automatically copy packaging discipline

Analysis add. The annual report writes Arizona as a wholly owned 12-inch fab. The capacity number given is above 17 million inside the managed perimeter. It does not split how much advanced packaging each fab has. Eastern capacity coming up is a parallel bid, not a substitute seat. Three layers: [Volume 12](vol-12.en.md). The Samsung Taylor long is Tesla willing to hand it over; see 3.8 above. 16k / 24k / 40k wafers per month have no announcement. Do not use them to fill the parallel line's capacity.

### 4.6 Cloud ASICs also return to the same slice

Public specs are in later sources and [Volume 25](vol-25.en.md). This volume does not reopen the spec table. To beat today's cabinet you return to 3nm, HBM, and this packaging. Only a true retreat to 5nm and less packaging gets you off the scarce slice. Public next generations have not stopped. So cloud custom silicon does not automatically open a second foundry. They are a second bid on the same slice, not another fab.

## 5. Analysis add (scenarios, the other side, checks that can be tested)

Analysis add. Push forward from the numbers now. Do not assign a separate probability. Do not invent cabinet counts.

Scenario A: the scarce slice past half, TSMC recognizes only the first name. Packaging on a sell-side pool of about 1 million wafers, about 100k cabinets past half. The first-customer jump from 12% to 19% keeps being written on the increment. It need not be written to 50% of the factory. Smartphone 29% of revenue is still there. New lines and fixtures are taken by cabinets first. 2nm first-silicon slots sort by prepayment. C.C. Wei's sentence that it limits customer growth still applies. The second name who wants the same material pays more or does not get it. What can be checked: whether the next annual report's first customer keeps rising, whether HPC stays above 58%, whether packaging and test walks above low teens, whether the call still says tight.

Scenario B: packaging expands faster than demand; tight becomes loose. C.C. Wei welcomes a bit more elasticity in the market; the pilot line matures in a year; Intel EMIB or other packaging takes a slice. If official text no longer says it limits customer growth, this volume's binding line has to be re-estimated. Even if loose, front-end 3nm and 2nm first silicon may still be tight. What loosens is fixtures, not furnaces. What can be checked: packaging-and-test revenue share clearly above low teens and the company changing its wording to "can meet." That is this scenario landing. It is not here now.

Scenario C: the West actually bundles; prepayments large enough that TSMC cannot recognize only one buyer. Apple, AMD, cloud ASICs, and Qualcomm bind three checks together: joint prepay on the same packaging slice, one software stack, memory longs that leave commodity bits. Miss one check and you are still picked off. None of the three is done now. What is done is only NVIDIA supply commitments to $119.0B. What can be checked: a third name also over 10% in the TSMC annual report, and the first name no longer eating the increment alone; or official disclosure that packaging by customer is no longer one-sided. Now the second name fell from 22% to 17%. The direction is the opposite.

Scenario D: cloud ASICs take training off the cabinet. Shunting inference is not enough. Public next generations are still on 3nm, HBM, and this packaging. The condition for taking it away is training also leaving the 72-card domain. What can be checked: a cloud publicly saying next-generation training mainstay retreats to 5nm plus commodity memory. None was found.

Three common other-side sentences this volume does not accept as already fact. First: booked 19% is still far; it is safe. The rebuttal is the increment in HPC up 48%, the first name jumping from 12% to 19%, the second falling, packaging already limiting growth. Safe distance is measured on the increment, not on factory-wide books. Second: you need 800,000 cabinets to lock 3nm. The rebuttal is the wrong pool; the binding line is packaging; about 100k cabinets take more than half. Third: Samsung and SMIC together can take Western flagship chips. The rebuttal is TrendForce 6.5% plus 5.1% is still revenue share; SMIC cannot take GDS; the Samsung Taylor long is Tesla, not Apple or AMD.

Checks that can be tested list only what can be publicly matched. TSMC annual-report first customer, second customer, top ten. Platform HPC and smartphone. Packaging-and-test revenue share. Whether C.C. Wei's call still says tight. TrendForce next-quarter foundry revenue share. Whether NVIDIA supply commitments keep rising. If sell-side 1 million wafers and 60% change their wording, label sell-side. Do not promote it. Cabinet counts, packaging wafers by customer, an official packages-per-wafer number: stay empty.

## 6. What this volume cannot write as fact

High-NA $380 million a tool, a single fab $20B to $25B, a wafer-price table from $10,000 at 7nm to $30,000–$35,000 at 2nm: the draft has them; TSMC earnings write-ups do not. Mark them draft.

Foundry 95% actual share: a draft assertion. This volume uses institutional single-quarter 72% and annual-report foundry 2.0 40%, written apart, not a census, not fused.

CoWoS monthly capacity, official full-year wafers, packaging wafers by customer: not found. Morgan Stanley 93,000, Mizuho 140,000: label sell-side. They do not agree.

"Sold out through 2026" as C.C. Wei official verbatim.

835,000 cabinets, 800,000 cabinets locking 3nm or 2nm.

Converting 19%, 58%, and 24% into tens of thousands of wafers.

2nm first silicon already bought out by NVIDIA. The 10-K only writes prepaid manufacturing and capacity agreements for current and future products. No prepayment sentence naming 2nm was found.

How much prepaid to TSMC, Hynix, and Samsung each. No official split was found.

Samsung Taylor 16k / 24k / 40k wafers per month. Not in the announcement.

An official number for B200 packages per packaging wafer. 5.39 is an estimate.

Writing TrendForce 72% as TSMC's own reported share, or writing 72.3% without noting second-hand paraphrase.

How many cabinets NVIDIA has already shipped. The product page has no cabinet count. Any global percentage multiplied from a cabinet count is a scenario, not a filing.

This volume stops the observation point at whether packaging can deliver, at whether booked 19% is a safe distance, and at which pool 5.39 divides. Price lists, ribbon-cuttings, and half the factory are not this volume's ruler.
