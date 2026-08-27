# Volume 14: AI Infrastructure Value-Capture Map — Profit Pools and Residual Pressure

Chinese original: [vol-14.md](vol-14.en.md)

Scarce-layer value capture and seller-side economics are in [Volume 1](vol-01.en.md). Non-AI Residual Capacity is in [Volume 5](vol-05.en.md) and [Volume 9](vol-09.en.md). AI Software Unit Economics is in [Volume 27](vol-27.en.md). This volume maps where value is captured, where capital intensity sits, and where residual pressure is transmitted.

## 1. Core question

Which layers of the AI infrastructure stack can capture durable economic value, and which layers mainly absorb capital cost, utilization risk, or residual supply pressure?

The answer cannot be reduced to a winner/loser list based on one year's gross margin. The report distinguishes:

- **system platforms** — integration, software, interconnect, and rack-scale value capture;
- **foundry and advanced packaging** — high capital intensity plus scarce manufacturing capability;
- **memory** — HBM/server demand, cyclical capacity, and wafer tradeoffs;
- **hyperscalers** — enormous scale but heavy CapEx and depreciation;
- **power / interconnection** — long-duration scarce infrastructure;
- **AI software** — outcome pricing and variable inference/tool/review cost;
- **consumer/general-purpose computing** — exposure to residual-capacity pressure.

The same company can be a scale winner and a return-on-capital loser in different scenarios.
## 2. Evidence boundary

Historical versions used a single 60%–75% “bottleneck margin” band, fixed consumer cost inflation, a 40-month replacement cycle, cabinet BOM estimates, and a SaaS 85%→55% margin path. Those values do not form a valid cross-industry profit-pool table.

Current analysis relies on:
- NVIDIA's seller-side financials and system-stack economics;
- TSMC's foundry and packaging disclosures;
- SK hynix / Micron / Samsung memory economics;
- hyperscaler company-wide CapEx and asset duration;
- formal power-project status;
- AI Software Unit Economics rather than a fixed SaaS endpoint;
- Non-AI Residual Capacity rather than a universal consumer “tax.”

The objective is to map mechanisms, not manufacture a precise ranking from incomparable accounting denominators.
## 3. Push the mechanism (physics / commerce / geopolitics)

### 3.1 Profit, increment, the binding line, and foundry share

Scarce-layer value capture is in [Volume 1](vol-01.en.md). The increment in HPC and booked 19% are in [Volume 4](vol-04.en.md). The binding line at CoWoS is in [Volume 24](vol-24.en.md). Foundry share 72% is in [Volume 4](vol-04.en.md). This volume does not reopen them. It only draws winners and losers: who collects scarcity value, who pays the residual-capacity pressure.

### 3.5 System platforms, memory, and packaging capture value through different mechanisms

Draw the map on the platform-control layers, not on an industry catalog.

The system-sales layer currently captures substantial value: FY26 Data Center revenue was **$193.737B**, and FY26 free cash flow was **$96.575B**. Asset-light: capex is tiny versus revenue; residual value is mostly not on its own balance sheet. The software/interface layer wins on the switching tax: a unified compute architecture is a ten-year developer stack. UXL and oneAPI exist. They are digging. They have not dug through. Hardware can be cheap. The switching tax is still there. A 75% pad means it can also cut price. The roadmap and supply-coordination layer wins on the mix: Hopper to Blackwell to Rubin, with HBM, advanced packaging, and interconnect scheduled together. The model/deployment extension has products. That is not the winners' main book. Writing "they train models" as a second profit pool splits the platform-control layers into an ordinary chip firm and an ordinary software firm. The question leans.

The three memory makers who follow the price are the second ring of winners. SK hynix FY2025 official press release: revenue KRW 97.1467T, operating profit KRW 47.2063T, operating margin 49%, net profit KRW 42.9479T. Prior-year control: revenue KRW 66.1930T, operating profit KRW 23.4673T, operating margin 35%. One year from 35% to 49% is a snapshot of HBM pulling memory from a bulk cycle toward a "compute attachment." It is not a permanent tax regime. Hynix itself wrote that HBM revenue more than doubled in a year. New fabs are named for AI. Samsung Memory and Micron actively moving wafers and high-value capacity toward cabinets is the same floor. After the three turn to high price, the residual is thinner. A few dozen brands split what is left. That holds up "no bundle, no commodity-bit long." Once memory walks from shortage back to bulk, 49% can snap back to a 2023-style loss year. Whether chip scarcity value is terminal depends on whether the penalty ratio is still there, not on one year of operating profit.

Packaging is the third ring. TSMC packaging and test from 8% to slightly over 10%. C.C. Wei said it is so tight it limits customer growth, and that the majority is still chip-on-wafer-on-substrate. Advanced-packaging revenue share is still far smaller than wafers. The gate is here. Sell-side puts NVIDIA at about 60%. Once past half, what the second name wants is not a bit more money. It is whether a slot exists. Packaging houses and substrate vendors pulled along eat the overflow. They eat the slice the roadmap and supply-coordination layer cannot schedule. They do not eat the software/interface layer.

Power and interconnection can become a separate scarce-infrastructure value-capture layer, but project economics depend on contract structure, energization, utilization, and duration. The master judgment writes "power stops the buildout" as one of five interrupts. It has not won. Counterparties who can sign a baseload long have a chance to collect scarce scarcity value. Unit megawatts and PPA dollars that cannot be written do not enter the fact layer. historical stress-test material pointed at 835 MW and 960 MW. the current evidence review does not recheck them. They are not a completed winner cell. Power is a constraint, not the platform-control layers themselves.

### 3.6 First-wave residual pressure falls on consumer and general-purpose computing

The first wave is not "manufacturing digitalization paying cloud scarcity value." It is PCs, commercial PCs, general-purpose servers, phones, and game cards, competing with cabinets for the same slice of packaging and the same slice of high-price memory. Those who cannot compete pay a residual-capacity pressure: longer lead times, higher bit prices, longer replacement. Those who can still get a node down and a bit down. Brand extinction stays a scenario. No names. Not written as a loser list that already happened.

Phones are still here. TSMC's smartphone platform in 2025 was still 29%, still up 11% year on year. The river did not dry. What changed is the increment: HPC up 48%, revenue share from 51% to 58%. Flagships keep paying leading-edge ASP. Mid and low end go back to mature nodes. Draft SoC quotes, controller share of BOM above 30%, replacement beyond 40 months — the current evidence review did not recheck the original reports. They stay historical stress-test claims. What can be confirm is the platform table and the packaging sentences: phones are still here, but they are not who the roadmap and supply-coordination layer feeds first.

PCs and game cards have already been conceded by the system-sales layer. Consumer accelerators and the data center queue in the same supply-commitment book. Official text writes Blackwell and Ada supply as limited. That is not an analyst guess. PCs pay a memory residual pressure, plus missing discrete GPUs. Commercial PCs still have to pass security management and long-cycle driver certification. Advanced packaging will not yield this slice. General-purpose servers and AI cabinets are not the same order, but they compete for memory makers' wafers. TrendForce official copy: 51% of 2026 DRAM bits are HBM plus RDIMM. Registered DIMMs are already inside that half "for cabinets." If a general-purpose server is still buying DDR5 RDIMMs, it is buying residual after the pull, and the price follows the residual. Official cabinet: 13.4 TB plus 17 TB. 10,000 cabinets is 134 PB of HBM. That is the product page multiplied. It is not a shipment forecast.

CPUs are demoted, not extinguished. Data-center revenue has already left gaming and automotive far behind. Grace is still on the cabinet BOM, 36 versus 72 accelerators. It is an accessory. The profit center is not there. Intel 1999 share-era scarcity value does not map onto selling cabinets today. Applied in this volume: CPU vendors are still here, but they are accessories. Writing "already dead" crosses the scenario line.

Traditional seat-license software gross margin from 85% to 55% is a draft assertion. It names no 10-K and no year. The mechanism is plausible: seat-license marginal cost is near zero; an agent has to write every inference into COGS. No sample, and it does not enter the fact layer. Whoever only announces an assistant product and does not change revenue recognition and COGS structure is sticking a label on the old profit pool. This volume does not draw that sentence onto the winner-loser map.

### 3.7 Clouds are buyers. The depreciation book is harder

The four clouds are scale winners and conditional profit winners, not sellers bidding against 75%. Capex scope is in [四云Capex口径核对](四云Capex口径核对.md). NVIDIA revenue and four-cloud capex cannot be knocked against each other. The two sides are different accounts. Cloud ASICs have not retreated to 5nm plus commodity DDR5. Specs are in [Volume 4](vol-04.en.md). The winner condition is AI incremental revenue covering hardware depreciation without punching through group gross margin. The loser condition is capex ahead of workflow monetization, the cloud becoming a utility that keeps accelerators for customers.

### 3.8 Geopolitics: two winner tables. The China market cannot save global cabinets

Firms that can enter CUDA and advanced packaging keep collecting dollar scarcity value. In regions locked out by controls, winners become systems integrators and algorithm firms on a substitute stack. Their margin band does not automatically equal 75%. China's parallel stack can alter regional supply and competition, but frontier-AI substitution remains a system-level question rather than a single regional demand offset. The closed loop is in [Volume 12](vol-12.en.md). The five interrupts are in [Volume 8](vol-08.en.md). The case file is in [Volume 11](vol-11.en.md).

## 4. Scenarios, counterarguments, and testable indicators

Push forward from the numbers now on the table. No extra probabilities. A four-scenario probability table does not enter the fact layer.

Scenario A: bottleneck scarcity value continues. NVIDIA gross margin stays near 71% to 75%; Q4 was already back to 75%. Hynix operating margin stays high. TSMC HPC holds the first platform. Packaging and test stays above 10%. C.C. Wei still says tight. Prepayments keep rising. About 100k cabinets take more than half of this packaging line. The first wave keeps paying the residual-capacity pressure. Phone revenue at 29% is still there. New lines and packaging go to cabinets first. Consumer-electronics brand extinction is still only a scenario, not a base-case fact.

Scenario B: clouds digest internally. The four clouds run past depreciation on ads, office, and internal recommendation. External APIs can lose; internal efficiency still counts as a win. External model firms fare worse. Cloud ASICs stay on 3nm plus HBM and bid against 75%. They do not retreat to commodity memory. Scale winners are still the four clouds. Profit winners are still four-corner hardware.

Scenario C: algorithm deflation. Training and inference costs move down the DeepSeek path. historical stress-test material wrote KV-cache compression 93.3% and pretraining converted at about $5.576M. This volume did not recheck the technical report. Hardware ASP is under pressure. Winners move from chips to applications that can still lock data and workflow. This scenario only holds if cabinet prices and prepayments come down together. Supply commitments rose $23.8B in three months. The direction is the opposite.

Scenario D: hard landing. The cell where calls rise and unit price falls appears. Destocking. Memory and foundry are hurt before software. Hynix 49% returns to a cyclical loss. TSMC HPC share falls back. The first wave briefly gets mature nodes flowing back. What flows back is a node down, not same-generation advanced packaging.

Objection 1: clouds are the biggest winners, because customers cannot leave. 2024 and 2025 revenue support "large." Capex and depreciation support "brittle." Winning or losing is whether incremental revenue covers the halls. Do not replace the income statement with market cap. Objection 2: booked 19% means Apple is still there, so it is safe. The annual report itself writes the first name up from 12% and the second name down from 22%, with HPC already at 58%. A safe distance is measured on the increment, not on a full-year blended share. Objection 3: 5.39 is made up. It is an estimate. The numerator 72 is official. The denominator about 13.4 is a geometry working assumption. Using it on the full-factory 15,022 thousand wafers is what is made up. Objection 4: consumer electronics will pass cost through by raising price. What can be confirm is official limited supply on game cards, and half of DRAM bits already written to cabinets. Objection 5: a Samsung Taylor long will split foundry concentration. The announcement is a parallel line. No monthly wafers. It cannot take the Western flagship-chip queue.

Testable marks, observation items only. Go back to the makers and the original press releases. This volume does not audit for them. Whether NVIDIA gross margin is still 71% to 75%; whether supply commitments keep leaving $119.0B. Whether TSMC HPC is still above 58%; whether packaging and test is still above 10%; whether C.C. Wei still says tight; whether the first customer keeps leaving 19%. Whether TrendForce foundry revenue share is still above 70%. Whether Hynix operating margin stays high. Whether game cards are still written as supply-limited. Whether HBM plus registered DIMMs are still written by institutions as more than half of bits. Whether the four clouds' cash-flow statements split out an AI line item — if not, do not invent one.

## 5. What this volume cannot write as fact

TSMC has no CoWoS monthly capacity, no official full-year wafer count, and no packaging wafers by customer. C.C. Wei at the shareholders' meeting, verbatim "sold out through 2026," was not found. How many B200s come off one advanced-packaging wafer has no official number. Samsung Taylor 16k / 24k / 40k wafers per month is not in the announcements. Do not convert HPC 58% or 3nm 24% into tens of thousands of wafers. The report does not treat TrendForce 72% as a share TSMC itself reported. NVIDIA at about 60%, 595,000 wafers, is a sell-side paraphrase. 100k cabinets taking more than half is a sell-side pool times an estimate. 835,000 cabinets is void.

Seat-license gross margin from 85% to 55% has no company and no year. It does not enter the fact layer. Cabinet software premium and switch gross margin were cut by the frame. Consumer-electronics purchase cost, SoC quotes, 40-month replacement, and robot BOM were not rechecked in the current evidence review. They stay historical stress-test claims. Nuclear-unit megawatts do not enter the fact layer. $215B is not an AI-hardware line item. 2026 $670B to $750B is a forecast, unverified; do not treat as an audited fact. This volume does not claim to have audited a 10-K.

There is no industry-by-industry profit-pool table, no named loser list, and no first-wave unit-shipment control. What can be written is the mechanism: they compete with cabinets for the same slice of packaging and the same slice of high-price bits. The result is in TSMC's platform table and the packaging sentences.

## 6. Split scale winners from profit winners

The map must split scale winners from profit winners, or four-cloud revenue will hide depreciation. On revenue, all four clouds are larger than NVIDIA. On gross margin, free cash, and prepayments, NVIDIA turns the scarce slice itself into cash. TSMC's 59.9% gross margin is manufacturing scarcity value that has to keep sinking heavy capital to hold the bottleneck. Hynix 49% is attachment scarcity value. Once the attachment returns to bulk, the tier collapses. The same firm can win on the revenue layer and lose on free cash flow.

Who the residual is pushed to is the cross-period dark line. NVIDIA is asset-light; residual value is mostly not on its own books. The clouds are asset-heavy; residual value sits in the halls. Phone and auto plants carry chips bought dear and inventory. The winner is the link that can push residual onto someone else and collect only definition-rights cash. That is compatible at once with 71% to 75% gross margin, free cash $96.6B, and supply commitments of $119.0B.

Pricing power sits with NVIDIA, HBM makers, and power counterparties who hold a baseload block. Volume without pricing power: phone OEMs, model-API firms that must buy accelerators at the market, and demoted CPUs. The four clouds have volume and some pricing power, but group-wide capex makes that power conditional. TSMC sits in the middle: 59.9% says it is not a coolie; heavy capital says pricing power has to be bought again every year. Booked 19% is not a safe distance.

The world does not blow up. Upgrades stop one node down. One firm writes the rules. If those five are not done, the line walks past half of the scarce slice. The window is the few years before the next first-to-market node is locked by commitments. If Volume 14 is written again as a four-layer industry catalog, or if the seat-license margin assertion and consumer-electronics extinction are written as fact, the question leans. The map is an arrangement of observation marks, not a ranking.
