# Volume 19: 2026–2036 AI-Infrastructure Timeline and Milestones

Chinese original: [vol-19.md](vol-19.en.md)

The end-state switch is [Volume 15](vol-15.en.md). First-stage three ends are [Volume 20](vol-20.en.md). How to live the decade is [Volume 40](vol-40.en.md). Nuclear-contract detail is [Volume 35](vol-35.en.md). This volume only ranks nodes that already happened or that earlier stress-test material named. It does not invent a 2036 calendar.

## 1. Core question

A useful ten-year timeline must distinguish observed milestones, formal company roadmaps, contractual targets, and scenario-only dates.

This volume therefore aligns several clocks:
- product generations;
- foundry / memory / packaging expansion;
- capital deployment and depreciation;
- power contracts, permitting, and energization;
- software/system-stack substitution;
- China parallel-stack development.

The purpose is not to assign a precise event to every year through 2036, but to identify which clocks can collide and which future milestones are already anchored by public roadmaps or contracts.
## 2. Timeline anchors

### Observed through August 2026

- **2024–2025:** hyperscaler infrastructure spending accelerated sharply; mixed-year company-wide CapEx/PPE rose from roughly **$211.9B–$213.9B** in 2024 to roughly **$354.0B–$356.5B** in 2025.
- **2025:** TSMC HPC reached **58%** of platform revenue; advanced packaging/testing rose to slightly above **10%** of revenue; CoWoS remained tight.
- **2025–2026:** HBM and server memory absorbed a large share of DRAM resources; Micron's first-party disclosure established an HBM3E wafer-supply trade ratio of roughly **3× DDR5** for the same node and bit capacity.
- **2025–2026:** hyperscaler alternatives advanced from custom chips toward system stacks: Ironwood, Trainium3 UltraServer, Maia, and MTIA.
- **2025–2026:** model firms became infrastructure anchor buyers through Stargate and Anthropic/AWS long-duration commitments.
- **April 2026:** Talen completed the front-of-the-meter conversion for the AWS/Susquehanna structure; the live variable became the **1.92 GW** contract ramp and actual utilization.
- **FY27 Q2 / July 2026 quarter:** NVIDIA revenue **$96.221B**, Data Center **$89.0B**, GAAP gross margin **75.0%**, operating income **$63.734B**; Vera Rubin entered full production.

### Contractual / roadmap milestones

- **2H26:** TSMC plans N2P/A16 production, subject to product-specific adoption.
- **2028 target:** Constellation's Crane Clean Energy Center / former Three Mile Island Unit 1 restart under the Microsoft-linked 20-year PPA.
- **~2030 onward:** first Kairos/Google commercial SMR projects targeted to begin, with development through the mid-2030s and an aggregate target up to **500 MW**.
- **through 2032:** the Talen/AWS **1.92 GW** contractual ramp remains a key observable power milestone.

### 2030–2036

Beyond formal roadmaps and contracts, the report does not use a deterministic calendar. Outcomes are represented through **S1 Competitive Expansion, S2 Baseline Concentration, S3 Resource Hegemony, and S4 Capital Hard Landing**. Old point forecasts for CoWoS monthly capacity, wafer ASP, campus GW scale, or fixed scenario probabilities remain stress-test material rather than timeline facts.
## 3. Mechanism: aligning product, capacity, capital, and power clocks

What makes a timeline useful is not "which chip ships in which year." It is whether several clocks line up. ()

**The product clock is fast.** GPUs and models change by the year: Blackwell / GB200 NVL72, N2, and Vera Rubin are placed by earlier stress-test material in 2025–2026. CUDA / PTX backward compatibility is written as zero-cost migration for developers, so the product clock can be fast and the ecosystem clock can be slow — one reason Nvidia can collect the system premium on the whole cabinet (BOM table, earlier stress-test values). The central framework writes the sales unit as having moved from the chip to the cabinet. Once the cabinet clock is welded to HBM and CoWoS, a product launch cannot stand alone as the industry calendar.

**The capacity clock is medium.** Advanced packaging and HBM expansion operate on multi-year capacity cycles rather than quarterly product clocks. Memory-maker capital spending had already accelerated before the 2026 supply squeeze, showing that the capacity clock began well before end-market relief became visible. 2025 struck that clock: Hynix FY25 operating margin 49%, HBM revenue more than doubled, and it also named a sharp rise in conventional server memory; Samsung Memory KRW 104.1T, priority on high value-add; Micron CMBU from $3.79B to $13.52B in one year. Yield and the logic base die decide that HBM cannot be released by the quarter the way ordinary DRAM can. Micron FY24 Q3 prepared remarks disclose that, industry-wide, HBM3E requires approximately **3× the wafer supply of DDR5** to produce a given number of bits in the same technology node; Micron's FY25 10-K later confirms that HBM requires more wafers and cleanroom space for the same bits. The ~3× ratio is A-grade first-party evidence, while still not being a universal fab-control constant. The capacity clock is therefore not "open a few more DDR5 lines." It is "every HBM order accepted leaves even fewer conventional bits."

**The memory-structure clock checks the table in 2026.** TrendForce 2026-08-25: HBM+RDIMM together are 51% of 2026 DRAM bit supply; memory is 47% of major CSP CapEx in 2026 and 68% in 2027. https://www.trendforce.com/presscenter/news/20260825-13198.html The same note also puts the contract-price path on this axis: 2H25 server DRAM cumulative +64%, 2026 outlook about +270%; enterprise SSD 2H25 about +35%, 2026 cumulative outlook about +235%; HBM in 2027 may still be +70–140%. 2026 is therefore not a blank year in which one "waits another year to see if memory is tight." It is the year bits go past half and capex structure turns toward the die. 2027's 68% is an outlook. Mark it institutional. Do not mark it as already happened.

**The power and regulation clock is slow.** Interconnection 5–7 years; data-center civil works 12–18 months; SMRs written to 2030–2035. The Three Mile Island restart is "old unit + new offtake," faster than a new pile, but still regulated. Whoever's clock is slow becomes the 2026–2028 tight constraint: not whether the next GPU can be designed, but whether a 120 kW cabinet can be tied to stable baseload before depreciation has run. Power is slow, memory is fast. The timeline will first show "dies are expensive, cabinets are still queued for power."

**The consumer clock is dragged by the residual.** A replacement cycle written as beyond 40 months is a result, not a start. Huaqiangbei channel talk on 2026-07-07: 16G DDR5 was 450 yuan last year, 1,800 yuan now. https://m.cls.cn/detail/2418583 That is not a contract price, but it is enough to mark summer 2026 as an observation point that the residual-capacity pressure has already hit retail. CXMT's 2025 DDR revenue share rose from 13.26% to 31.87%; LPDDR is still 66.43%, which means it is eating conventional DRAM whose international price has already risen, not an HBM year suddenly opened in 2026. The prospectus has 0 mentions of HBM. 2026 cannot write "domestic HBM ramps" onto the timeline.

Commercially, 2025–2028 is the first depreciation ridge. 2024's $215B already happened; 2026's $750B is a forecast (unverified; do not treat as first-party fact). If the product clock keeps pushing clouds to order while the power clock stalls energization, the timeline will first show "book capex is there, cabinets are not full," then "guidance cut." If memory then eats 47% to 68% of CSP CapEx, that ridge gets steeper. This is nearer, and more observable, than the 2036 four scenarios.

The geopolitical clock is a step, not a smooth curve: one export-control revision can cut the purchasable set. earlier stress-test material puts Huawei Ascend and CANN in the hedge column, but it gives no volume month or yield that can be merged into this timeline, so the China path in this volume can only be marked "a parallel track, nodes not aligned." It cannot be marked as a peer substitute in some month of 2027. YMTC's January–March 2026 revenue RMB 47.042B, official 200 layers and above, is a NAND clock, not an HBM clock.

The wafer-cabinet estimate draws another 2026 line on packaging: more than half the scarce slice lands at the 100k-cabinet order of magnitude. You do not need 800k cabinets to lock 3nm. Sell-side is still reporting tens of thousands of Blackwell cabinets this year, already near that line. The window is not waiting for a cabinet count divided from the wrong pool. This volume marks that line as "observable in 2026, not something that starts in 2030."

## 4. Scenario windows and testable milestones

Read the decade as three broad phases rather than ten equal annual boxes:

- **2026–2028: the depreciation, energization, and residual reconciliation.** What to watch is no longer only whether the supply chain wrote some month-end CoWoS capacity. It is: whether HBM+RDIMM is still written as more than half of DRAM bits; whether memory's share of CSP CapEx is still walking from 47% toward 68%; whether Hynix / Samsung / Micron still write capacity language toward HBM and servers; whether Three Mile Island 835 MW and Susquehanna 960 MW begin to form actual load; whether Huaqiangbei or contract prices are still taxing the residual; whether CXMT later discloses a standalone HBM line. If DeepSeek-class architectures spread, they will raise "tokens per dollar" in this stretch, which may delay cuts or make the 2026 $750B forecast look too high. Shifting inference onto DDR5 is not relief in this stretch. It is a fight for RDIMM inside the 51%, or for the leftover consumer bits.

- **2029–2032: a second technology step, or rebuild after a washout.** A16, CoPoS, higher stacks, and the first SMR pile all crowd near here. If the first stretch already washed out, this stretch is rebuilt capex. If advertising and cloud revenue carried the first stretch, this stretch is further concentration. CXMT's forward project writes completion of a DRAM forward platform in 2028. That is still not an HBM timetable.

- **2033–2036: the end-state fork.** earlier stress-test material's four scenarios only make sense here. The algorithm-break scenario depends on language like "compute demand falls 1,000×" (unverified; do not treat as first-party fact). The oligopoly scenario depends on single-fab cost "breaking $40B" and 80% compute monopoly (also unverified). This volume gives no new probabilities.

The other side: a common timeline-forecast error is treating a supply-chain "year-end capacity guide" as installed capacity. Another is treating the Nvidia product roadmap as the industry calendar: if Vera Rubin slips, N2 wafers are not automatically in surplus, because Apple and ASICs are still bidding the same node. A third: writing 2026's 51% as "the memory-cycle peak," ignoring that TrendForce itself still writes 2027 server DRAM+HBM bits another +27% and contract prices still high. Past half is structure, not an endpoint.

Testable marks: whether TSMC earnings calls still put HPC as the first platform, and whether 3nm revenue share is still near 18% or a next-node share is given; whether Hynix still discloses a large HBM-revenue rise; whether Micron CMBU and MCBU are still one jump and one flat; whether TrendForce still holds 51% / 47% / 68% or issues a revision; the direction of the four clouds' next-year capex guides relative to $215B; commercial-operation notices on nuclear PPAs, not signing dates; whether later CXMT / YMTC prospectuses or periodic reports have an HBM line or a monthly-capacity line. The "beyond 40 months" replacement cycle only enters this timeline if brand filings' unit shipments confirm it. Otherwise it is an analyst sentence.

Draw these clocks on one sheet and the decade is not symmetric. () The first half is packed with four things: packaging tight, the four clouds having to depreciate capital already spent, nuclear offtakes having to go from signature to interconnection, and memory bits past half going to cabinets. The second half is written by earlier stress-test material with a thinner pen as "A16, CoPoS, 1nm, campus GW-scale." Evidence density falls. An honest timeline-forecast model should admit: 2026–2028 can be checked against a table. After 2029 it is more and more a branch of a scenario tree, not an industry calendar that can be named to the quarter.

There is also an algorithm clock that is easy to miss. () DeepSeek writes training cost as $5.576M and KV Cache compression as 93.3%. If reports like that keep being treated as procurement evidence by enterprises in 2026–2027, the hardware timeline will be pushed right by "the same intelligence, fewer cards." Conversely, if enterprises turn the saved budget at once into more concurrent agents, the hardware timeline will be pulled left. If the savings go to stacking DDR5, the timeline will not move right. It will only bring the residual-capacity pressure forward. earlier stress-test material wrote both directions. It did not give an observation protocol for which one wins. What this volume can do is mark this algorithm clock on its own, and write that it does not automatically open a new memory river.

For firms and investors, this timeline is not used to "bet a launch year." It is used to bet which clock stops first. () If interconnection and energization keep lagging whole-cabinet shipments in 2026–2027, what you should see is cabinets waiting for power, not chip-shortage news. If the residual clock is faster, you should first see phone and PC shipments and channel prices, not training cabinets stopping. If the algorithm clock is faster, you should see effective tokens per cabinet rise and new-order growth fall. All three can happen. This volume leaves the fields: energization, shipments, depreciation, replacement, bit structure, CapEx structure. Keep them separate. Do not recombine them into one pretend-precise ten-year prophecy.

## 5. Gaps and what cannot be treated as fact

1. This timeline is a synthesis of milestones and scenario variables from the rest of the monograph. It is not an issuer calendar or a stand-alone deterministic forecast model.
2. CoWoS monthly capacity from end-2025 on, 2026 $750B, the 2030 / 2036 four-dimension table, the four-scenario probabilities, "compute demand falls 1,000×," and single-fab $40B are all extrapolations (unverified; do not treat as first-party fact).
3. The N2 / A16 buyer list and the Vera Rubin node come from earlier stress-test material's paraphrase of roadmaps, not from shipped statistics.
4. The SMR 500 MW 2030–2035 window has no per-pile commercial-operation year. The Three Mile Island 20-year offtake amount appears only in Part II as "over $16B," and was not reconciled dollar-per-megawatt with 835 MW.
5. No volume year for higher stacks, no first-production year for CoPoS, no introduction year for CPO. The title's "technology-breakthrough nodes" are empty on these key items.
6. 68% is a 2027 institutional outlook. CXMT monthly capacity and YMTC exact layer count do not enter the timeline. The report does not treat 8.6 / 13.2.
7. Grid-queue claims are used only where supported by the cited public or institutional sources; no unsupported aggregate queue figure is promoted into the fact layer.

This volume introduces no independent numeric forecast layer; it reorganizes already-supported milestones and scenario conditions into a common timeline.

The end-state switch is [Volume 15](vol-15.en.md). First-stage three-end action is [Volume 20](vol-20.en.md). How to live the decade is [Volume 40](vol-40.en.md). This volume only puts several clocks on one axis. It does not reopen the scenario tree.
