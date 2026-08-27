# Volume 5: HBM, the memory war, and AI supply-chain rebuild (Hynix profit, demand multiplied by cabinet, residual)

Chinese original: [vol-05.md](vol-05.md)

## 1. The question this volume answers

Has HBM already moved from an accessory beside the GPU to the memory industry's main product? After makers switch production, are consumer bits another river, or residual after the same river was drawn down? This volume only follows memory. It does not write 3:1 as a factory constant already measured. It does not promote the draft's Hynix 2023-to-2024 won comparison into an annual report opened in this pass. What this pass can nail is Hynix FY25 operating margin 49%, HBM revenue more than doubling in a year, and one official cabinet of 13.4 TB HBM3E. From those numbers down: who can bid, and who only gets residual.

A margin monopoly on this memory slice does not mean NVIDIA makes the bits. It means the cabinet seller takes 71% to 75% gross margin, then uses prepayments to bid next year's stack lines at the makers. Sellers are already rich: TSMC 2025 gross margin 59.9%, Hynix operating margin 49%. Neither covers the cabinet-selling tranche. Among buyers, Apple, AMD, Qualcomm, Huawei, and the clouds do not have the same pad on selling cabinets. Comparing sticker prices is meaningless. Whoever can prepay can add a tranche. Makers watch this tranche, not a phone-maker bargaining session.

Three layers are not one layer. The phone layer eats LPDDR and consumer bits. The PC layer eats DDR. The AI layer eats HBM and server DIMMs. Matching China phone shipments to HBM in global training cabinets is the wrong layer. CXMT's prospectus: 0 mentions of HBM. 350k wafers per month is not an announcement. Once the international price holds, makers sell first to the high bidder. Huawei's high price is a rent unpaid to NVIDIA inside the iron curtain. It does not mean CXMT has been nursed to HBM.

This volume also nails multiply-by-cabinet. Demand equals cabinets shipped times the bill of materials per cabinet. NVIDIA does not report cabinet counts. Makers do not report full-year absolute bits. The arithmetic stops at per cabinet, per thousand cabinets, per ten thousand cabinets. It is not written as already having bought a global percentage. 10,000 / 30,000 / 50,000 cabinets multiplied out are scenarios, not shipments.

## 2. Official and institutional sources

### 2.1 Hynix FY25

Source: https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/

Original: revenue KRW 97.1467T, operating profit KRW 47.2063T, operating margin 49%, net profit KRW 42.9479T, net margin 44%. DRAM segment: HBM revenue more than doubled in a year. Won are not privately converted to dollars. This pass did not open the full statutory Hynix annual report. It uses this table from the company press release.

This set pulls memory out of the cycle-stock reading. Operating margin 49% is already near TSMC's 50.8% operating margin, still below NVIDIA's last two quarters of 74.9% to 75% gross margin. Hynix is a seller. Seller riches prove the mix is set by the coach: makers expand to the Hopper-to-Blackwell-to-Rubin stack mix, and the increment that comes out is bought first by prepayments. The main line's "makers turn to high price" stands on this table. There is no need to invent each of the three houses' share percentages.

Micron and Samsung latest statutory reports were not opened file-by-file in this pass. Do not invent each house's HBM shipment gigabytes, do not invent each ASP, do not invent "the three already split evenly." The names that can publicly do TSV, multi-layer bonding, and dock to a leading-edge logic base are these three. Oligopoly is a mechanism. The share table is empty. An empty table cannot be filled with adjectives.

The same press release also gives a control year and the quarter. FY24: revenue KRW 66.1930T, operating profit KRW 23.4673T, operating margin 35%, net profit KRW 19.7969T. 4Q25: revenue KRW 32.8267T, up 34% year on year; operating profit KRW 19.1696T, up 68% year on year; operating margin 58%. Besides HBM revenue more than doubling in a year, the release also writes server conventional-memory demand rising sharply; 1.0nm-class conventional DRAM entering volume; 256 GB DDR5 RDIMM; HBM3E and HBM4 shipping together; Cheongju, Yongin, and Indiana advanced packaging under construction. NAND: 321-layer QLC development complete, second half on enterprise SSD, full-year NAND revenue a record. The release does not split DRAM and NAND dollars, and does not report absolute bits. Source 03 is explicit: do not convert 49% into dollars.

Source 03 this pass also added Samsung's press release and call table, and Micron's 10-K segments. Below is written in each maker's currency. Still do not invent the three houses' shares, shipment gigabytes, or ASP.

### 2.2 NVIDIA profit and prepayments: where the cash that locks memory longs comes from

FY26 and supply commitments are in [Volume 1](vol-01.md). This volume does not reopen the full table. The 10-K in the same node names Hynix, Micron, and Samsung for memory. It does not split dollars by vendor. There is no line that says "paid Hynix X billion for HBM." Do not invent one. This volume treats $95.2B to $119.0B as a cash ceiling for locking next-generation material, not as cash already collected by Hynix. Multi-year cloud-service commitments are not memory prepayments. Write them apart.

### 2.3 Official cabinet bill of materials and multiply-by-cabinet

Source: https://www.nvidia.com/en-us/data-center/gb200-nvl72/

Official: 36 Grace, 72 Blackwell, 13.4 TB HBM3E, 17 TB LPDDR5X. The draft wrote 13.8 TB, another scope of 72 times 192 GB, which does not match this product page. This volume uses the page's 13.4. 17 TB of LPDDR is on the CPU side, not HBM, but it competes with the cabinet for the same maker leading-edge capacity.

Identity: demand equals cabinets shipped times the bill of materials per cabinet. NVIDIA does not report cabinet counts. Makers do not report full-year absolute bits. The arithmetic stops at scenarios.

Per thousand cabinets (scenario, not shipments): HBM 13.4 PB; LPDDR 17 PB. 10,000 cabinets: HBM 134 PB, LPDDR 170 PB. 30,000 cabinets: 402 PB and 510 PB. 50,000 cabinets: 670 PB and 850 PB. These are multiplied from the product page, not maker shipments. 1 EB equals 1,000 PB. Do not write 134 PB as EB.

Front-end logic is another line. B200 two dice at about 800 mm² reticle limit, nailed in Electronic Design and IEEE Spectrum, not a 10-K. H100 official blog: 814 mm². 72 packages times two dice is 144 dice. About 2.9 logic wafers per cabinet at 70% yield. 5.39 is a packaging-wafers-per-cabinet estimate: 72 packages divided by about 13.4 per wafer. The two lines must not be mixed. Memory in this volume uses 13.4 TB times cabinets. It does not divide memory bits by 5.39.

### 2.4 TSMC HPC 58%: which increment memory follows

The platform table is in [Volume 4](vol-04.md). This volume does not reopen it. What can be nailed: what is being opened is HPC and packaging, not phones. Memory makers turning to HBM follow this increment, not a phone LPDDR bargaining session. Makers have no financial reason to offend a cabinet contract for a phone maker. Whoever leaves a line for phones and PCs is a slice short in the current profit race. This is a hypothesis from the present, not already "a full about-face, commodity supply down 40%." That 40% sentence is in the draft. This pass matches no maker announcement. It does not enter the fact layer.

### 2.5 Institutions and paraphrase: 51% of bits, about 3× the silicon

The main line cites TrendForce: 51% of 2026 DRAM bits are HBM plus RDIMM. Memory as a share of major CSP capex, 47% in 2026, 68% in 2027. Institutional scope, not a Hynix or Micron segment disclosure. Do not promote it to a maker table.

The same TrendForce official press release (25 August 2026, https://www.trendforce.com/presscenter/news/20260825-13198.html ) also writes: the major CSPs it tracks, total capex up 98% year on year in 2026, then another 50% in 2027. This is an institutional estimate, not a "memory procurement" line in the four clouds' filings. Same paragraph: makers give limited capacity to servers first; 2027 node migration plus new-fab ramp in the second half, expected server DRAM plus HBM combined bit supply up another 27%. Same release, contract-price direction (institutional, not maker list prices): 2H25 server DRAM contract prices up a cumulative 64%, 2026 outlook about another 270%; enterprise SSD about +35% in 2H25, 2026 cumulative outlook about +235%; some longs from 2Q26 carry a price ceiling; HBM contract prices in 2027 may still rise 70% to 140%.

51% is bit supply, not revenue. HBM ASP is high, so revenue share will be higher. RDIMM is already inside this 51%, which means server conventional DDR5 is not another river. It is the socket DIMM inside this half. If clouds restack inference onto DDR5, they are bidding residual already inside this 51%, or residual that is already following the rise. Label institutional. Do not promote it to maker shipments.

Micron 10-K: the same bits, HBM takes more wafers. Hot Chips paraphrase: about 3× DDR5. The main line writes "Hot Chips paraphrase about 3× DDR5." 3:1 is not a measured constant in a factory MES. It is a maker direction plus a paraphrased multiple. What can enter the fact layer is the direction "more wafers" and "about 3×." Stacking up to 4:1 or 5:1 is a forward hypothesis on 16-high stacks. This volume marks it unverified. Do not treat it as an audited fact.

Channel talk: 16G DDR5 from about 450 to 1,800. Huaqiangbei paraphrase, not an annual report. Direction is residual following the rise. Source nailed to CCTV Finance and Cailian Press 7 July 2026 https://m.cls.cn/detail/2418583 , 21st Century Business Herald repeating the same sentence. A 32 GB DDR5 kit rose to nearly 4,000 yuan, three to four times last year. Reporter tally: 16G last year 450 yuan, now 1,800 yuan, up 300%; 32G last year 900 yuan, now 3,800 yuan, up 322%; 1 TB SSD last year 410 yuan, now 950 yuan, up 132%. Grade: channel spot talk, not TrendForce contract prices, not maker list prices. It only proves consumer DIMMs are already paying a "residual tax." It cannot be backed into maker ASP.

TrendForce 2026 Q1 foundry revenue: TSMC 72%, Samsung 6.5%, SMIC 5.1%. Institutional revenue share, not wafers. Public high-end AI logic volume is still mostly TSMC. Memory makers are another oligopoly. The two oligopolies stack on the same cabinet: logic and packaging at TSMC, stacks at Hynix, Micron, and Samsung.

### 2.6 Sellers are already rich. Buyers cannot cover

The profit control is in [Volume 1](vol-01.md). This volume does not reopen it. Clouds bid for HBM with profit from selling software and cloud. NVIDIA bids for HBM with profit from selling cabinets. Same slice of material, two bid functions. A margin monopoly means the second function can add a tranche.

### 2.7 Samsung memory: maker won, no FX conversion

Sources: https://news.samsungsemiconductor.com/global/samsung-electronics-announces-fourth-quarter-and-fy-2025-results/ ; call materials https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2025_4Q_conference_eng.pdf

Company 2025: revenue KRW 333.6T, operating profit KRW 43.6T. Device Solutions full-year revenue KRW 130.1T, up 17% year on year (prior year 111.1); memory full-year revenue KRW 104.1T, up 23% (prior year 84.5). 4Q25 Device Solutions revenue KRW 44.0T, operating profit KRW 16.4T; memory quarterly revenue KRW 37.1T, the release writes a quarterly record. Press-release original: supply limited, still used strong conventional DRAM demand, HBM expansion, and overall price increases to take memory quarterly revenue and operating profit to records; profit improvement from high value-add, naming HBM, server DDR5, and enterprise SSD. Does not split DRAM and NAND dollars, does not report HBM bits. Source 03 is explicit: there is no maker announcement "cut 80,000 wafers back from HBM" — by instruction, do not write it.

2026 outlook, same release: keep prioritizing AI high value-add; Q1 start delivering HBM4 (including 11.7 Gb/s); expand DDR5, LPDDR5X CAMM2, GDDR7; NAND side push high-performance TLC for inference KV SSD. Makers write cabinets, server DIMMs, and enterprise drives as the same priority, not another consumer river.

### 2.8 Micron FY25 segments: residual written on the books

Source: SEC 10-K, fiscal year ended 28 August 2025. https://www.sec.gov/Archives/edgar/data/723125/000072312525000028/mu-20250828.htm

Total revenue $37.378B (prior year $25.111B). DRAM $28.58B (prior year $17.60B). NAND $8.50B (prior year $7.23B). Hyperscale cloud plus all data-center HBM $13.52B (prior year $3.79B). Mid-cloud and enterprise memory plus all data-center storage $7.23B (prior year $4.98B). Mobile, client, and Crucial $11.86B (prior year $11.67B).

Same 10-K: 2025 DRAM bits mostly at 1β; 4Q25 HBM3E 12-high already the majority of HBM shipments; HBM4 36 GB 12-high already sampled. The cloud-memory segment sells HBM, DDR5 and DDR4, LPDDR5, GDDR6. The mobile-and-client segment walked almost flat for the year. The cloud-memory slice jumped from $3.79B to $13.52B. Source 03 writes: this is what "residual" looks like on a maker's books — what rose is the cabinet, not phones and PCs.

10-K original: Due to the higher performance and more complex manufacturing process, HBM requires a higher number of wafers and more cleanroom space to produce the same number of bits as conventional DRAM in the same technology node. Same paragraph: if HBM demand weakens and makers cut capacity from HBM back to conventional DRAM, conventional supply will rise materially. Read the other way: while HBM is still bidding wafers, conventional is residual.

Hot Chips 2026 floor notes (ServeTheHome, https://www.servethehome.com/micron-evolving-memory-architectures-for-ai-at-hot-chips-2026/ ): design architecture, advanced packaging, and manufacturing complexity together, same-capacity HBM3E consumes about 3× the silicon of DDR5. The same piece also writes a typical GPU base plus eight HBM4 exceeding 12,000 mm². Tom's Hardware put 3× in the headline. Scope: same capacity, not a factory split of "one HBM wafer for three DDR5 wafers." 3:1 enters the conference-paraphrase layer. It is not promoted to a 10-K measured multiple. Micron's official slides were not separately posted on the IR page in full.

The three houses' fiscal years do not align. Do not convert won to dollars and then add them to Micron.

## 3. Push the mechanism forward

### 3.1 Makers turn to high price. Residual is not another river

Hypothesis from here. Do not veto. Hynix operating margin 49% and HBM revenue more than doubling in a year are already enough to reject the old reading that "memory is only a cycle stock." Treat it as a cycle stock and you watch capex in the wrong direction: buildout prefers stacks, not consumer bits. TrendForce writing half of 2026 DRAM bits as HBM plus RDIMM is an institutional measure of this turn, not makers' own reported shipment bits.

Multiply-by-cabinet writes the turn as arithmetic. 10,000 cabinets take 134 PB of HBM and 170 PB of LPDDR. 30,000 cabinets 402 and 510. 50,000 cabinets 670 and 850. NVIDIA does not report cabinet counts, so these are scenarios. The use of a scenario is not to report a global percentage already bought. It is to say: once shipments walk as cabinets, demand multiplies by cabinet; supply cannot keep up with the product. Server DDR5 is already residual, not another river. Consumer bits are even fewer. They are what is left after the same river was drawn down.

Price rises that phones and PCs see are the residue of this decision chain. A few dozen brands split the residual. Limited supply of gaming cards is the consumer end of the same line already giving way: the athlete can already give the same leading-edge logic to a 75% gross-margin data center. The first wave is PCs, commercial PCs, general-purpose servers, and phones, competing with the cabinet for the same leading-edge logic, HBM, and server DIMMs.

Whoever leaves a line for phones and PCs is a slice short in the current profit race. This is not an already-happened "full about-face." The Hynix release does not write shutting consumer lines. This volume only writes direction: high-price longs are in; commodity lines cut toward stacks. How much is cut waits for the next maker segment.

Source 03 adds the three together. It does not upgrade them into a new number. Half the bits already go to cabinets; the silicon drawn is harsher than the bits; the three houses' books stand on the cabinet side. Restacking onto DDR5 is adding tax: if inference uses less HBM and more DDR5, what it buys is RDIMMs and consumer residual already inside the 51%, or already following the rise. It is not a new river.

### 3.2 Prepayments lock the next stack, not bits already delivered

Supply commitments are in [Volume 1](vol-01.md). It names Hynix, Micron, and Samsung for memory. It gives no split dollars. The highest-margin name can add a prepayment tranche. Not yet written as fact: Hynix already a captive fab, 16-high stacks bought out in bulk, a contract locking all 2027 HBM. If they are not found, leave them empty. Four-cloud scope: [四云Capex口径核对](四云Capex口径核对.md). Cloud money has other uses. NVIDIA's money is specifically for locking the next slice of material. On this memory slice, two sets of money bid the same stack line.

### 3.3 3:1 is a direction, not a measured constant

The draft used single-layer yield 95% to the 12th power times base yield 90%, got 48.6%, then wrote each HBM wafer as consuming three conventional DRAM wafers. The formula is illustrative. Hot Chips paraphrases about 3×. Micron's 10-K writes the same bits take more wafers. Direction matches. The coefficient is not MES. 4:1 and 5:1 only earn the right to move from forecast to observation after 16-high is in volume and makers still say "one wafer for four." This volume does not write an illustrative formula as a law of nature.

A logic base pulls I/O and power out of the memory process. HBM starts consuming leading-edge logic. Halfway through the memory war it becomes a foundry war. If the base walks 3nm or 5nm, every stack takes more leading-edge logic, and maybe packaging. TSMC packaging is already tight enough to limit customer growth. The base and the GPU die bid the same fab's back end. That is a mechanism, not a disclosed base-wafer count.

Test and burn-in are a hidden penalty outside 3:1. Failure after 12-high bonding happens after the stack. What sinks is 12 dice. Actual wafer consumption may exceed the paraphrased about 3×. This volume does not give another multiple. 48.6% is already an optimistic example, not a conservative floor. Mark analysis add.

### 3.4 CXMT follows the price. It does not transfuse Huawei

CXMT's prospectus: 0 mentions of HBM. 350k wafers per month is not an announcement. YMTC official text writes 200 layers and above. There is no monthly capacity in the tens of thousands of wafers. Once the international price holds, makers sell first to the high bidder. Profit has no nationality. After the three giants pull good capacity to HBM, conventional bits are expensive, and making conventional also pays. Domestic makers follow the floor. That is not a lack of patriotism. It is profit.

CXMT source is the SSE 20 May 2026 registration draft: https://static.sse.com.cn/stock/disclosure/announcement/c/202605/002170_20260520_C5DZ.pdf . Source 03 used full-text search. Full-text HBM in Chinese and English: 0 hits. Products only write DDR and LPDDR two families: DDR covers DDR4 and DDR5; LPDDR covers LPDDR4X and LPDDR5 / LPDDR5X. Process writes "first- through fourth-generation process technology platforms." It does not print a node-nanometer label. Do not invent node names.

Main-business mix (RMB 10,000): 2025 DDR 1,953,128.56, 31.87%; LPDDR 4,070,354.50, 66.43%; other 104,054.15, 1.70%; main-business total 6,127,537.21. The two families together 98.30%. The draft writes main business as 99.74%, 98.97%, and 99.15% of revenue in the last three years, mostly from these two families. There is no HBM row. 2024 and 2023 are likewise DDR plus LPDDR, no HBM row.

Three raised-proceeds items: memory wafer-fab technology upgrade RMB 7.5B; DRAM technology upgrade RMB 18.0B (proposed use of proceeds RMB 13.0B); DRAM forward technology R&D RMB 9.0B. Total RMB 34.5B, proposed use of proceeds RMB 29.5B. The forward project original focuses on future advanced DRAM, construction period written 2026 to 2028. RMB 9.0B is a DRAM forward basket, not a separately listed HBM line. The two characters for HBM do not appear.

Capacity: the company has three 12-inch DRAM fabs in Hefei and Beijing; on Omdia data, by capacity, shipments, and sales, the company is first in China and fourth globally. Full-text search "350,000" is not monthly capacity (hits are R&D-expense decimals). The prospectus does not have 350k wafers per month. The 350k in Korean reporting is a year-end outlook from a semiconductor analysis firm, not the prospectus; the same batch writes HBM allocation as "a very small part." Chosun Ilbo: IPO price RMB 8.66, proceeds before greenshoe RMB 57.9B. 350k wafers per month does not enter the fact layer. What CXMT's books sell is DDR and LPDDR whose international price has already risen. Proceeds add conventional lines and "DRAM forward," not a new HBM river matching the three houses.

YMTC is a NAND IDM, not an HBM spare. The site on 6 August 2025 writes two fifth-generation 3D NAND representative products, 1Tb TLC and 2Tb QLC. That page does not print stack-layer counts. Prospectus filing draft (SSE 21 August 2026): January–March 2026 revenue RMB 47.042B, net income attributable RMB 33.379B; on TrendForce, sales and shipments both third globally and first in China. Reporting period: 2025 revenue RMB 63.185B, net income attributable RMB 14.211B. 2024 and 2023 prospectuses have tables. This volume does not promote loss years into a story. Raised proceeds: volume-line technology upgrade RMB 20.8B, R&D-related RMB 12.2B, total RMB 33.0B. Official layer sentence: 2022 Xtacking 3.0, among the world's first to launch 200-layer-and-above 3D NAND; 2024 iterated Xtacking 4.0. What is printed is "200 layers and above / breaking 200 layers," not 267 layers. Media 267 does not enter the fact layer. There is no official monthly capacity in the tens of thousands of wafers. Do not write "about 200k wafers" second-hand. HBM appears in YMTC prospectus definitions as an industry noun (DRAM stacking), not a YMTC product line. YMTC eats NAND and SSD price rises. It cannot fill HBM, and cannot fill the server-DDR5 half of bits.

Huawei's high price is a rent unpaid to NVIDIA inside the iron curtain. Rationing blocks domestic bits from flowing out. It does not mean CXMT has been nursed. The near gate is an administrative lock. The far gate is non-silicon. If domestic advanced packaging and HBM-class bits can already volume enough to hold a training cabinet, an administrative lock is enough to keep a closed loop. If not, an administrative lock only keeps the phone layer. This volume puts CXMT on the phone layer and the PC layer, not the AI layer. The layer is wrong. The sum is meaningless.

The China market cannot save global cabinets' HBM allocation. The payer is North American cloud. TSMC's increment is HPC. Packaging and HBM mix to the training box. A parallel stack that does not enter this mix does not change this game's supply function. Eastern capacity coming up is a parallel bid, not a substitute seat.

### 3.5 Bundling still misses one check. Memory will still be picked off

Three checks and five interrupts: [Volume 8](vol-08.md). This volume only follows the third check. Phone makers bind residual memory. They cannot bind training-cabinet stacks. What can actually change the cabinet is the bundle that makes accelerator cards and cloud ASICs, plus real-money memory longs. This check is not done now.

## 4. Analysis add (scenarios, the other side, checks that can be tested)

Analysis add. Do not veto. Clouds restacking inference onto DDR5 is not a new river. HBM has already drawn wafers at higher silicon cost; leftover DDR5 bits still split to RDIMMs and phones and PCs. Restacking is adding tax to a slice already rising. Huaqiangbei 16G 450 to 1,800 is residual dying first, as talk. This volume only nails: restacking conventional DIMMs does not change the sentence "half the bits already go to cabinets."

The condition under which the other side can stand is written by Micron's 10-K itself: if HBM demand weakens and makers cut capacity back to conventional, conventional supply will rise materially. This volume does not write "weakening" as already happened. The Samsung release has no "cut back 80,000 wafers." The Hynix release does not write shutting consumer lines. How much is cut waits for the next segment.

Checks that can be tested. Do not invent thresholds. Whether Hynix's next release still writes HBM revenue doubling and server conventional memory rising sharply. Whether Samsung memory next quarter still names HBM, server DDR5, and enterprise SSD. Whether Micron's cloud-memory segment versus mobile-and-client keeps widening or the latter lifts its head. Whether TrendForce still reports HBM plus RDIMM past half of DRAM bits. Whether the next CXMT draft still searches HBM at 0 hits. Whether YMTC official layers still stop at "200 layers and above." These are an observation list, not a forecast table. Unverified. Do not treat as audited fact.

Hypothesis from here: while cabinet-selling gross margin stays 71% to 75%, prepayments can keep rising. Consumer bits are even fewer. They are what is left after the same river was drawn down. The world does not blow up. Upgrades stop one node down. Phones and PCs pay a memory spillover tax.

## 5. What this volume cannot write as fact

Draft Hynix 2023 revenue KRW 32.77T, operating loss KRW −7.73T, 2024 revenue KRW 66.19T, operating profit KRW 23.47T, HBM over 40% of DRAM revenue: corresponding statutory reports were not opened this pass. Do not promote them. This pass uses the FY25 press release 49% and more than doubling in a year.

Draft 3:1, composite yield 48.6%, 1,200 dice versus 400 on the same wafer, maker gross margin above 60%, HBM per cabinet $580k–$680k: illustrative or BOM attribution, not a Hynix segment. 16-high, 4:1, 5:1, 2030 and 2036 penalty rates: unverified. Do not treat as audited fact.

Micron and Samsung have no independent financial tables opened in an earlier pass of this volume's first draft, so those sentences cannot write each house's share. After source 03, they do have opened tables. Still cannot write each house's share percent. Still cannot convert won to dollars and add them to Micron.

TrendForce 51%, cloud capex 47% to 68%: institutional, not maker. 16G from 450 to 1,800: channel talk.

Supply commitments $119.0B are not split to Hynix or HBM. Multi-year cloud services $30.0B are not memory prepayments.

Converting 58%, 24%, and 19% into tens of thousands of wafers. Revenue share is not unit share.

CXMT 350k wafers per month, YMTC monthly capacity in the tens of thousands of wafers: not in the announcements. Prospectus HBM 0 hits can only be written as 0 hits, not as a story beyond "already failed at volume."

Counting equity marks as money that bids for memory capacity. Q1 net income $58,321M includes about $15.9B of unrealized gains. Bidding looks at operating income $53,536M.

Cabinet counts, global absolute HBM bits, stack wafers by customer: empty. Do not invent them.

After source 03, Samsung and Micron are no longer "no independent financial table opened this pass." What can be used is the press release and 10-K segments. Still cannot write each house's share percent. Still cannot convert won to dollars and add them to Micron. Still empty: Micron official-slide original sentences; Hynix and Samsung DRAM/NAND dollar splits, full-year HBM bits, absolute wafers; CXMT monthly capacity and 350k wafers per month; YMTC official layer count (267 does not enter) and monthly capacity in the tens of thousands of wafers; 8.6 and 13.2 TB, three houses 1.8 million wafers per month, Samsung cutting 80,000 wafers back from HBM. These stay empty per source 03. Do not invent them.
