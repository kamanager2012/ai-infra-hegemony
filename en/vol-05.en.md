# Volume 5: HBM, the memory war, and the AI supply-chain rewrite (SK Hynix / Micron / Samsung and the ~3× wafer-supply trade ratio)

Chinese original: [vol-05.md](vol-05.md)

## 1. The question this volume answers

Has HBM already moved from a part next to the GPU to the main product of the memory industry? After makers shift production, are consumer bits another river, or the residual of the same river after the draw? This volume follows memory only. It does not write 3:1 as a factory constant already measured. It does not promote the draft's Hynix 2023-to-2024 won pair to a statutory report opened in this pass. What this pass can nail is Hynix FY25 operating margin 49%, HBM revenue more than doubled in a year, and the official 13.4 TB of HBM3e per cabinet. From those numbers down, the question is who can bid the price and who can only take residual bits.

A margin monopoly on this memory slice does not mean NVIDIA makes the dies. It means the firm that sells cabinets takes 71% to 75% gross margin and then uses prepayments to bid next year's stack lines at the makers. Sellers are already rich: TSMC 2025 gross margin 59.9%, Hynix operating margin 49%. Neither covers the cabinet-selling tranche. Among buyers — Apple, AMD, Qualcomm, Huawei, the clouds — none has the same pad on selling cabinets. Comparing sticker prices is meaningless. Whoever can prepay can add a tranche. Makers watch that tranche, not the phone-makers' pricing meeting.

Three layers are not one layer. The phone layer eats LPDDR and consumer dies. The PC layer eats DDR sticks. The AI layer eats HBM and server sticks. Matching domestic phone shipments to HBM on global training cabinets is the wrong layer. CXMT's prospectus: 0 mentions of HBM in a full-text search. 350k wafers per month is not an announcement. Once the international price holds, makers sell first to the high bidder. Huawei's high price is a rent unpaid to NVIDIA inside the iron curtain. It does not mean CXMT has been nursed to HBM.

This volume also nails multiply-by-cabinet. Demand equals cabinets shipped times the bill of materials per cabinet. NVIDIA does not report cabinet counts. Makers do not report full-year absolute bits. The arithmetic stops at per cabinet, per thousand cabinets, per ten thousand cabinets. It is not written as already having bought some percent of the world. 10,000, 30,000, and 50,000 cabinets times the page are scenarios, not shipments.

## 2. Official and institutional sources

### 2.1 SK hynix FY25

Source: https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/

Original: revenue KRW 97.1467T, operating profit KRW 47.2063T, operating margin 49%, net profit KRW 42.9479T, net margin 44%. DRAM segment: HBM revenue more than doubled in a year. Won are not privately converted to dollars. This pass did not open the full Hynix statutory report. It uses this table from the company press release.

These numbers pull memory out of the cycle-stock file. Operating margin 49% is already near TSMC's 50.8% operating margin, and still below NVIDIA's last two quarters of 74.9% to 75% gross margin. Hynix is a seller. Seller riches prove the mix is locked by the coach: makers expand to the Hopper-to-Blackwell-to-Rubin stack mix, and the increment is bought first by prepayments. The main line's "makers turn to the high price" stands on this table. There is no need to invent each of the three firms' share percentages.

Micron and Samsung's latest statutory reports were not opened file-by-file in this pass. Do not invent each firm's HBM gigabytes shipped. Do not invent each ASP. Do not invent "the three already split it evenly." The named parties that can do TSV, multi-layer bonding, and a leading-edge logic base die at once are these three. Oligopoly is the mechanism. The share table is empty. An empty table is not filled with adjectives.

The same press release also gives the comparison year and the quarter. FY24: revenue KRW 66.1930T, operating profit KRW 23.4673T, operating margin 35%, net profit KRW 19.7969T. 4Q25: revenue KRW 32.8267T, up 34% year on year; operating profit KRW 19.1696T, up 68%; operating margin 58%. Besides HBM revenue more than doubling in a year, the release also writes a sharp rise in conventional server memory demand; 1c-nm conventional DRAM entering volume; 256 GB DDR5 RDIMM; HBM3e and HBM4 shipping at once; advanced packaging under construction in Cheongju, Yongin, and Indiana. NAND: 321-layer QLC development completed; second half leans on enterprise SSD; full-year NAND revenue a record. The release does not split DRAM and NAND dollars and does not report absolute bits. Source 03 writes: do not convert 49% into dollars.

Source 03 in this pass added the Samsung press release and earnings slides, and the Micron 10-K segments. Below is written in each maker's own currency. Still do not invent the three firms' shares, gigabytes shipped, or ASPs.

### 2.2 NVIDIA profit and prepayments: where the cash that locks memory longs comes from

FY26 and supply commitments: [Volume 1](vol-01.md). This volume does not reopen the full table. The 10-K at the same node names Hynix, Micron, and Samsung for memory purchases. It does not split dollars by vendor. There is no line that says "paid Hynix X billion for HBM." Do not invent one. This volume treats $95.2B to $119.0B as the cash ceiling for locking the next material, not as cash already booked as receipts at Hynix. Multi-year cloud-service commitments are not memory prepayments. Write them apart.

### 2.3 Official per-cabinet bill of materials and multiply-by-cabinet

Source: https://www.nvidia.com/en-us/data-center/gb200-nvl72/

Official: 36 Grace, 72 Blackwell, 13.4 TB HBM3e, 17 TB LPDDR5. The draft wrote 13.8 TB, another scope of 72 times 192 GB, which does not match this product page. This volume uses the page's 13.4. The 17 TB of LPDDR is on the CPU side, not HBM, but it bids the same maker leading-edge capacity against the cabinet.

Identity: demand equals cabinets shipped times the bill of materials per cabinet. NVIDIA does not report cabinet counts. Makers do not report full-year absolute bits. The arithmetic stops at scenarios.

Per thousand cabinets (scenario, not shipments): HBM 13.4 PB; LPDDR 17 PB. 10,000 cabinets: HBM 134 PB, LPDDR 170 PB. 30,000 cabinets: 402 PB and 510 PB. 50,000 cabinets: 670 PB and 850 PB. These are the product page multiplied out, not maker shipments. 1 EB equals 1,000 PB. Do not write 134 PB as exabytes.

Front-end logic is another line. Two B200 dies are about 800 mm² at the reticle limit, nailed in Electronic Design and IEEE Spectrum, not in an annual report. The H100 official blog writes 814 mm². 72 packages times two dies is 144 dies. At 70% yield, about 2.9 logic wafers per cabinet. 5.39 is a packaging-wafers-per-cabinet estimate: 72 packages divided by about 13.4 per wafer. The two lines must not be mixed. This memory volume uses 13.4 TB times cabinet count. It does not divide memory bits by 5.39.

### 2.4 TSMC HPC 58%: which increment memory follows

The platform table is in [Volume 4](vol-04.md). This volume does not reopen it. What can be nailed: what is being opened is HPC and packaging, not phones. Memory makers turning to HBM follow this increment, not the phone LPDDR pricing meeting. Makers have no financial reason to offend a cabinet contract for a phone maker. Whoever leaves a line for phones and PCs gives up a slice in the current profit race. That is a hypothesis from the present, not an already-happened "full pivot, commodity supply down 40%." The 40% sentence is in the draft. This pass matches no maker announcement. It does not enter the fact layer.

### 2.5 Evidence stack: 51% of bits and Micron's first-party ~3× wafer-supply trade ratio

The judgment cites TrendForce: 51% of 2026 DRAM bits are HBM plus RDIMM. Memory is 47% of major CSP capex in 2026 and 68% in 2027. Institutional scope, not a Hynix or Micron segment disclosure. Do not promote it to a maker table.

The same official TrendForce release (25 August 2026, https://www.trendforce.com/presscenter/news/20260825-13198.html ) also writes: total capex at the major CSPs it tracks is up 98% year on year in 2026 and up another 50% in 2027. That is an institutional estimate for "the major CSPs it tracks," not a "memory purchases" line in the four clouds' filings. Same paragraph: makers give scarce capacity to servers first; 2027 process migration plus second-half new-fab ramp, server DRAM plus HBM bit supply expected up another 27%. Same release, contract-price direction (institutional, not a maker list price): 2H25 server DRAM contract prices up a cumulative 64%, 2026 outlook about another 270%; enterprise SSD about +35% in 2H25, 2026 cumulative outlook about +235%; some long-term agreements from 2Q26 carry a price ceiling; HBM contract prices in 2027 may still rise 70% to 140%.

51% is bit supply, not revenue. HBM unit prices are high, so the revenue share will be higher. RDIMM is already inside this 51%. That means conventional server DDR5 is not another river. It is the socket stick inside this half. If the clouds restack inference onto DDR5, they are bidding the residual already inside this 51%, or the residual already rising with it. Mark it institutional. Do not promote it to maker shipments.

Micron FY24 Q3 prepared remarks state that, industry-wide, HBM3E consumes approximately **3× the wafer supply of DDR5** to produce a given number of bits in the same technology node, and that the HBM4 trade ratio is expected to be higher. Micron's FY25 10-K later confirms the direction by stating that HBM requires more wafers and cleanroom space for the same bits. The ~3× ratio is therefore **A-grade first-party company evidence**; Hot Chips 2026 is corroborating context, not the primary basis. The judgment writes "Micron first-party ~3× wafer-supply ratio versus DDR5." 3:1 is not a measured constant inside a factory MES. It is a maker direction plus a paraphrased multiple. What can enter the fact layer is "more wafers" and the "about 3×" direction. Stepping it up to 4:1 or 5:1 is a forward hypothesis on 16-Hi stacks. This volume marks it unverified. Do not treat as audit fact.

Channel talk: 16G DDR5 from about 450 to 1,800. Huaqiangbei paraphrase, not an annual report; the direction is residual bits following the rise. Source nailed to 7 July 2026, CCTV Finance and Cailian, https://m.cls.cn/detail/2418583 ; 21st Century Business Herald carried the same sentence. A 32 GB DDR5 kit rose to nearly RMB 4,000, three to four times last year. The reporter's tally: 16G last year RMB 450, now RMB 1,800, up 300%; 32G last year RMB 900, now RMB 3,800, up 322%; 1 TB SSD last year RMB 410, now RMB 950, up 132%. Grade: channel spot talk, not a TrendForce contract price, not a maker list price. It only shows consumer sticks already paying a "residual tax." Do not back out a maker ASP.

TrendForce 2026 Q1 foundry revenue: TSMC 72%, Samsung 6.5%, SMIC 5.1%. Institutional revenue share, not units. Public high-end AI logic volume is still mostly TSMC. Memory makers are another oligopoly. Two oligopolies sit on the same cabinet: logic and packaging at TSMC, stacks at Hynix, Micron, and Samsung.

### 2.6 Sellers are already rich. Buyers cannot cover

The profit comparison is in [Volume 1](vol-01.md). This volume does not reopen it. Clouds bid HBM with profits from software and cloud. NVIDIA bids HBM with profits from selling cabinets. Same slice of material, two bid functions. A margin monopoly means the second function can add a tranche.

### 2.7 Samsung Memory: maker won, no FX conversion

Sources: https://news.samsungsemiconductor.com/global/samsung-electronics-announces-fourth-quarter-and-fy-2025-results/ ; earnings slides https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2025_4Q_conference_eng.pdf

Company 2025: revenue KRW 333.6T, operating profit KRW 43.6T. DS Division full-year revenue KRW 130.1T, up 17% (prior year 111.1); Memory full-year revenue KRW 104.1T, up 23% (prior year 84.5). 4Q25 DS revenue KRW 44.0T, operating profit KRW 16.4T; Memory quarterly revenue KRW 37.1T, written as a quarterly record. Press-release text: supply limited, still a strong conventional DRAM bid, HBM sales expansion, and an overall price rise, took Memory quarterly revenue and operating profit to records; profit improved on high-value-add, naming HBM, server DDR5, and enterprise SSD. No DRAM/NAND dollar split, no HBM bits. Source 03 writes: there is no maker announcement of "cutting 80k wafers back from HBM" — do not write it, per the instruction.

2026 outlook, same release: keep prioritizing high-value AI; begin HBM4 deliveries in Q1 (including 11.7 Gbps); expand DDR5, SOCAMM2, and GDDR7; on NAND, push high-performance TLC into inference KV-SSD. The maker writes cabinets, server sticks, and enterprise drives as the same priority. It is not opening another consumer river.

### 2.8 Micron FY25 segments: residual bits sit on the books

Source: SEC 10-K, fiscal year ended 28 August 2025. https://www.sec.gov/Archives/edgar/data/723125/000072312525000028/mu-20250828.htm

Total revenue $37.378B (prior year $25.111B). DRAM $28.58B (prior year $17.60B). NAND $8.50B (prior year $7.23B). Cloud and data-center HBM unit (hyperscale cloud plus all data-center HBM) $13.52B (prior year $3.79B). Mid-cloud and enterprise memory plus all data-center storage $7.23B (prior year $4.98B). Mobile, client, and Crucial $11.86B (prior year $11.67B).

Same 10-K: most 2025 DRAM bits on 1β; in FQ4 2025, HBM3e 12-Hi already the majority of HBM shipments; HBM4 36 GB 12-Hi already sampled. The cloud-memory unit sells HBM, DDR5 and DDR4, LPDDR5, and GDDR6. The mobile-client unit walked almost sideways for a year. The cloud-memory slice jumped from 3.79 to 13.52. Source 03 writes: this is what "residual" looks like on a maker's books — what rose is the cabinet, not phones and PCs.

10-K original: Due to the higher performance and more complex manufacturing process, HBM requires a higher number of wafers and more cleanroom space to produce the same number of bits as conventional DRAM in the same technology node. Same paragraph: if HBM demand weakens and makers cut capacity from HBM back to conventional DRAM, conventional supply will rise markedly. Read backwards: while HBM is still taking wafers, conventional is residual.

Hot Chips 2026 floor notes (ServeTheHome, https://www.servethehome.com/micron-evolving-memory-architectures-for-ai-at-hot-chips-2026/ ): design architecture, advanced packaging, and manufacturing complexity together mean the same capacity of HBM3e consumes about 3× the silicon of DDR5. The same piece also writes that a typical GPU counted as base die plus eight HBM4 stacks exceeds 12,000 mm². The Tom's Hardware headline put 3× in the title. Scope: the same capacity, not a factory split of "one HBM wafer trades for three DDR5 wafers." The ~3× ratio is A-grade first-party company evidence; it is not a universal fab-control constant. Micron's official slides in full text are not separately posted on the investor page.

The three firms' fiscal years do not align. Do not convert won into dollars and add them to Micron.

## 3. Push the mechanism forward

### 3.1 Makers turn to the high price. Residual is not another river

Hypothesis from here. Do not refute. Hynix operating margin 49% and HBM revenue more than doubled in a year are already enough to kill the old reading that "memory is only a cycle stock." Treat it as a cycle stock and you misread the direction of capex: expansion first expands stacks, not consumer dies. TrendForce writing half of 2026 DRAM bits as HBM plus RDIMM is an institutional measure of this turn, not bits the makers themselves reported.

Multiply-by-cabinet writes the turn as arithmetic. 10,000 cabinets take 134 PB of HBM and 170 PB of LPDDR. 30,000 cabinets: 402 and 510. 50,000 cabinets: 670 and 850. NVIDIA does not report cabinet counts, so these are scenarios. The use of a scenario is not to report some percent of the world already bought. It is to say: once shipments run by cabinet, demand multiplies by cabinet; supply does not keep up with the product. Server DDR5 is already residual, not another river. Consumer bits are even thinner. They are what is left after the same river was drawn.

The price rise phones and PCs see is the slag of this decision chain. A few dozen brands split the remainder. Limited game-card supply is the consumer end of the same line already yielding: the athlete can today give the same leading-edge logic to a 75% gross-margin data center. The first wave is PCs, commercial PCs, general-purpose servers, and phones, bidding the same leading-edge logic, HBM, and server sticks against the cabinet.

Whoever leaves a line for phones and PCs gives up a slice in the current profit race. This is not an already-happened "full pivot." The Hynix release does not write that consumer lines were stopped. This volume writes only the direction: high-price longs are in; commodity lines cut toward stacks. How much is cut waits on the next maker segment.

Source 03 puts the three together and does not promote them to a new number. Half the bits already go to cabinets; the silicon drawn is harsher than the bits; the three makers' books stand on the cabinet side. Restacking onto DDR5 is a tax: if inference uses less HBM and more DDR5, what it buys is RDIMM and consumer residual already inside the 51%, or already rising with it. It is not opening another river.

### 3.2 Prepayments lock the next stack, not dies already delivered

Supply commitments: [Volume 1](vol-01.md). It names Hynix, Micron, and Samsung for memory and gives no split. The highest-profit name can add a prepayment tranche. Not yet written as fact: Hynix already a captive fab, 16-Hi stacks bought out in bulk, some contract locking all 2027 HBM. If it is not found, leave it empty. Four-cloud scope: [四云Capex口径核对](四云Capex口径核对.md). Cloud money has other uses. NVIDIA's money is used to lock the next slice of material. On this memory slice, two piles of money bid the same stack line.

### 3.3 ~3× is a disclosed industry trade ratio, not a universal fab constant

The draft derived its own 3:1 ratio from an uncalibrated compound-yield sketch; that derivation is rejected. Independently, Micron's FY24 Q3 prepared remarks disclose that industry-wide HBM3E requires approximately 3× the wafer supply of DDR5 for the same bits at the same node, while the FY25 10-K confirms the direction. The company disclosure is usable as A-grade evidence, but it is still an industry trade ratio rather than a fab MES constant. 4:1 and 5:1 only earn the right to move from forecast to observation after 16-Hi is in volume and makers still say "one wafer counts as four." This volume does not write a sketch formula as a law of nature.

The logic base die lifts I/O and power out of the memory process. HBM starts to consume leading-edge logic. Halfway through the memory war it becomes a foundry war. If the base die runs 3nm or 5nm, every stack takes leading-edge logic again, and maybe packaging. TSMC packaging is already tight enough to limit customer growth. Base die and GPU die bid the same factory's back end. That is mechanism, not a disclosed base-die wafer count.

Test and burn-in are a hidden penalty outside 3:1. A fail after 12-Hi bonding happens after the stack. What is sunk is twelve dies. Actual wafer use may sit above the paraphrased about-3×. This volume does not give another multiple. 48.6% is already an optimistic example, not a conservative floor. Mark it an analysis addendum.

### 3.4 CXMT follows the price. It does not feed Huawei

CXMT's prospectus: 0 mentions of HBM in a full-text search. 350k wafers per month is not an announcement. YMTC official text writes 200 layers and above, and no monthly capacity in the tens of thousands of wafers. Once the international price holds, makers sell first to the high bidder. Profit has no nationality. After the three take good capacity into HBM, conventional dies are expensive, and making conventional still pays. Domestic makers walk the floor. That is not a failure of patriotism. It is a demand for profit.

CXMT source is the SSE registration draft dated 20 May 2026: https://static.sse.com.cn/stock/disclosure/announcement/c/202605/002170_20260520_C5DZ.pdf . Source 03 read it by text search. Full-text search for HBM in Chinese and English: 0 hits. Products write only DDR and LPDDR: DDR covers DDR4 and DDR5; LPDDR covers LPDDR4X and LPDDR5 / LPDDR5X. Process writes "first- through fourth-generation process platforms" and prints no node-nanometer label. Do not invent a node name.

Main-product mix (RMB 10,000s): 2025 DDR 1,953,128.56, 31.87%; LPDDR 4,070,354.50, 66.43%; other 104,054.15, 1.70%; main-product total 6,127,537.21. The two series sum to 98.30%. The draft writes that in the last three years main products were 99.74%, 98.97%, and 99.15% of revenue, mainly from these two series. There is no HBM line. 2024 and 2023 are likewise DDR plus LPDDR, with no HBM line.

Three raised-fund projects: memory wafer manufacturing volume-line upgrade and rebuild, RMB 7.5B; DRAM technology upgrade, RMB 18.0B (RMB 13.0B proposed from the raise); DRAM forward-looking technology research and development, RMB 9.0B. Total RMB 34.5B, RMB 29.5B proposed from the raise. The forward-looking project original focuses on future advanced DRAM, with a build window written through 2026–2028. RMB 9.0B is a DRAM forward-looking basket, not a separately listed HBM line. The two characters for HBM do not appear.

Capacity: the company has three 12-inch DRAM wafer fabs in Hefei and Beijing; on Omdia figures for capacity, shipments, and sales, it has become China's first and the world's fourth. A full-text search for "350,000" is not monthly capacity (the hits are R&D-expense decimals). The prospectus does not contain 350k wafers per month. The 350k in Korean coverage is a year-end outlook from a semiconductor analysis firm, not the prospectus; the same batch writes HBM allocated capacity as "only a tiny share." Chosun Ilbo: IPO price RMB 8.66, RMB 57.9B raised before the greenshoe. 350k wafers per month does not enter the fact layer. What CXMT's books sell is DDR and LPDDR whose international price has already risen. The raise adds conventional lines and "DRAM forward-looking," not a new HBM river that peers with the three.

YMTC is a NAND IDM, not an HBM spare. The 6 August 2025 site writes two fifth-generation 3D NAND flagships, 1 Tb TLC and 2 Tb QLC. That page does not print stack-layer counts. The prospectus filing draft (SSE, 21 August 2026): January–March 2026 revenue RMB 47.042B, net income attributable to the parent RMB 33.379B; on TrendForce, third globally and first in China by both sales dollars and bits shipped. Reporting period: 2025 revenue RMB 63.185B, net income attributable to the parent RMB 14.211B. 2024 and 2023 have tables in the prospectus; this volume does not promote the loss year into a story. Raised funds: volume-line upgrade RMB 20.8B, R&D-related RMB 12.2B, total RMB 33.0B. Official layer sentence: 2022 Xtacking 3.0, among the world's first to ship 3D NAND at 200 layers and above; 2024 iterated Xtacking 4.0. What is printed is "200 layers and above / broke 200 layers," not 267 layers. Press 267 does not enter the fact layer. The full text has no official monthly capacity in the tens of thousands of wafers. Do not write second-hand figures such as "about 200k wafers." HBM appears in the YMTC prospectus glossary as an industry noun (DRAM stacks), not as a YMTC product line. YMTC eats the NAND and SSD price rise. It cannot backfill HBM, and it cannot backfill that half of bits that is server DDR5.

Huawei's high price is a rent unpaid to NVIDIA inside the iron curtain. Rationing blocks domestic bits from flowing out. It does not mean CXMT has been nursed. The near gate is an administrative lock. The far gate is non-silicon. If domestic advanced packaging and HBM-class bits can already volume enough to hold up a training cabinet, an administrative lock is enough to keep a closed loop. If they cannot, an administrative lock leaves only the phone layer. This volume puts CXMT on the phone layer and the PC layer, not on the AI layer. The layer is wrong. The sum is meaningless.

The China market cannot save the HBM allocation of global cabinets. The payer sits in the North American cloud. TSMC's increment is in HPC. Packaging and HBM are matched to training boxes. A parallel stack that does not enter this mix does not change this board's supply function. Eastern capacity standing up is a parallel bid, not a substitute seat.

### 3.5 Bundling still misses one check. Memory will still be picked off

The three checks and the five interrupts are in [Volume 8](vol-08.md). This volume follows only the third check. Phone makers bind memory residual. They cannot bind the stacks on training cabinets. What can actually change the cabinet is the bundle that makes accelerator cards and cloud ASICs, plus memory longs in real cash. That check is not done yet.

## 4. Analysis addendum (scenarios, the other side, testable markers)

Analysis addendum. Do not refute. Clouds restacking inference onto DDR5 is not opening another river. HBM has already drawn wafers at a higher silicon cost; the DDR5 bits left are still split between RDIMM and phones and PCs. Stacking more is a tax on the slice already rising. Huaqiangbei 16G from 450 to 1,800 is residual dying first, as talk. This volume nails only this: restacking onto commodity sticks does not change the sentence "half the bits already go to cabinets."

The condition on which the other side can stand is written by Micron itself: if HBM demand weakens and makers cut capacity back to conventional, conventional supply will rise markedly. This volume does not write "weakens" as already happened. The Samsung release has no "cut back 80k wafers." The Hynix release does not write that consumer lines were stopped. How much is cut waits on the next segment.

Testable markers. Do not invent thresholds. Whether the next Hynix release still writes HBM revenue doubling and a sharp rise in conventional server memory. Whether next-quarter Samsung Memory still names HBM, server DDR5, and enterprise SSD. Whether Micron's cloud-memory unit keeps pulling away from mobile-client, or the latter lifts its head. Whether TrendForce still reports HBM plus RDIMM over half of DRAM bits. Whether the next CXMT draft still searches to 0 HBM hits. Whether YMTC official layers still stop at "200 and above." This is a watch list, not a forecast table. Unverified. Do not treat as audit fact.

Hypothesis from here: while cabinet-selling gross margin holds at 71% to 75%, prepayments can keep rising. Consumer bits get thinner. They are what is left after the same river was drawn. The world does not blow up. Upgrades stop one node down. Phones and PCs pay a memory spillover tax.

## 5. What this volume cannot write as fact

Draft Hynix 2023 revenue KRW 32.77T, operating loss KRW −7.73T, 2024 revenue KRW 66.19T, operating profit KRW 23.47T, HBM over 40% of DRAM revenue: the matching statutory reports were not opened in this pass. Do not promote them. This pass uses the FY25 press release 49% and more than doubled in a year.

Draft 3:1, composite yield 48.6%, 1,200 dies versus 400 on the same wafer, maker gross margin above 60%, HBM per cabinet $580,000 to $680,000: sketch or bill-of-materials attribution, not a Hynix segment. 16-Hi, 4:1, 5:1, 2030 and 2036 penalty rates: unverified. Do not treat as audit fact.

Micron and Samsung have no independent financial tables opened file-by-file in this pass. Do not write each of the three firms' shares in percent.

TrendForce 51%, cloud capex 47% to 68%, are institutional, not maker. 16G from 450 to 1,800 is channel talk.

The $119.0B supply commitment is not split to Hynix or to HBM. The $30.0B multi-year cloud service is not a memory prepayment.

Converting 58%, 24%, and 19% into tens of thousands of wafers. Revenue share is not unit share.

CXMT 350k wafers per month, YMTC monthly capacity in the tens of thousands of wafers: not in the announcements. Prospectus HBM at 0 hits can only be written as 0 hits. It cannot be written as a story beyond "volume already failed."

Counting equity marks as money that bids for memory capacity. Q1 net income $58,321M includes about $15.9B of unrealized gains. Bidding looks at operating income $53,536M.

Cabinet counts, global HBM absolute bits, stack wafers by customer: leave empty. Do not invent.

After Source 03 was added, Samsung and Micron are no longer "no independent financial table opened in this pass." What can be used is the press release and the 10-K segments. Still do not write each of the three firms' shares in percent. Still do not convert won into dollars and add them to Micron. Still empty: Micron official slide original sentences; Hynix and Samsung DRAM/NAND dollar splits, full-year HBM bits, absolute wafers; CXMT monthly capacity and 350k wafers per month; YMTC official layer count (267 does not enter) and monthly capacity in the tens of thousands of wafers; 8.6 and 13.2 TB, the three makers at 1.8 million wafers per month, Samsung cutting 80k wafers back from HBM. These stay empty per Source 03. Do not invent.
