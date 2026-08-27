# Volume 13: The AI Energy War — From 120 kW Racks to GW-Scale Power Constraints

Chinese original: [vol-13.md](vol-13.en.md)

## 1. Core question

Power is an independent physical constraint on AI infrastructure. The relevant question is not whether “the cloud has gone nuclear,” but whether delivered compute can be converted into **energized, cooled, utilized capacity** on a timetable compatible with short hardware generations and long infrastructure lives.

This volume tracks four states separately:

```text
announced capacity
→ contracted capacity
→ permitted / interconnected capacity
→ energized load
→ utilized load
```

A signed PPA is not a powered rack. A grid queue is not available load. A 120 kW rack makes local power density, cooling, main transformers, and interconnection first-order design constraints.
## 2. Current evidence boundary

First-party and formal project anchors include:

- NVIDIA GB200/GB300-class NVL72 rack power at roughly **120 kW**.
- Microsoft / Constellation: **20-year PPA**, roughly **835 MW**, restart target around **2028**.
- Talen / AWS: replacement PPA up to **1.92 GW**; front-of-the-meter conversion completed in **April 2026**; actual ramp and utilization remain the live variables.
- Google / Kairos: development target up to **500 MW**, with first commercial projects targeted around **2030**.

Historical claims such as a single **2,600 GW** U.S. queue total, universal 5–7 year interconnection time, 500-rack annual energy totals, copper-cable savings, cooling BOM percentages, or nuclear-operator gross margins are not used as current first-party facts unless separately sourced.

The core analytical distinction is therefore physical status and timing—not nominal MW alone.
## 3. Mechanism: rack density, interconnection, and power-contract duration

### 3.1 Rack density turns power and cooling into deployment conditions

Power density rose by an order of magnitude. Air-cooling heat-exchange area and hall return air fail first. Microchannel cold plates sit on the GPU and the switch die and dump heat into the CDU and the water loop. Leak tests, water quality, and pump redundancy become a go-live gate the way a unified compute architecture is a go-live gate. historical stress-test material's per-cabinet liquid-cooling dollar amount is small. Whether it can be built at scale decides whether the cabinet can run at 120 kW. The heat island also spills into the city: a 60-to-80 MW point load changes the environmental permit on the substation main transformer and the cooling tower. The way the energy war enters the municipal layer is the point load, not the national share of kilowatt-hours.

120 kW is not "a few more air conditioners." Air conditioners handle hall air. Direct liquid cooling handles surface heat flux on the die. A 5-to-10 kW air-cooled cabinet can plug into an ordinary campus. A 120 kW-class cabinet is hard to "plug first and ask later" on an ordinary campus. Density itself screens the business model. Campuses that can take this density already tend to come with power, water, and permits. The system platform sells a turnkey cabinet and defaults the customer to a floor that can take power. Without that floor, the turnkey stops in the warehouse.

This volume does not estimate how many cabinets 835 MW can feed, so a division is not written as fact. It keeps only historical stress-test material's 500-cabinet, 60-to-80 MW pair, marked as an engineering conversion, unchecked. The household comparison (60,000 homes, 600 million kWh) is only a magnitude for non-technical readers. Residential load is dispersed and low-coincidence. Compute load is a high-coincidence block. Dividing users by megawatts understates the local hit and overstates the national share. Keep historical stress-test material comparison. In the gaps, downgrade it to a rhetorical magnitude.

### 3.2 Grid queues measure process, not deliverable AI load

2,600 GW is queue capacity, not capacity under construction. historical stress-test material gives no composition. Duplicate filings, speculative holds, and repeated interconnection-point edits are common diseases of a grid queue. historical stress-test material has no cleaned effective capacity. What actually binds compute is the transformer, short-circuit capacity, and transmission corridor at a local node, plus the 5-to-7-year calendar. Even if national generation capacity is ample, a campus that wants to light 60 to 80 MW inside 18 months can still fail at the substation. The energy war's battlefield is the node, not the country-level installed-capacity table.

5–7 years versus 12–18 months is a clock mismatch. Under ordinary utility process, the hall is built first and then waits for power. The rational responses are three: buy a finished campus that can take power at once; sign a long with an operating nuclear unit and fund a restart; book future baseload as paper SMR capacity. The first two grab in-place baseload. The third bets a ten-year-scale new pile. Whoever first locks a megawatt block of the size historical stress-test material named occupies a time window in the regional grid that others cannot copy. The window is time, not installed capacity.

Interconnection queues above 2,600 GW must not be read as "the United States is about to be short 2,600 GW of data-center power." The queue mixes wind, solar, storage, legacy generation, and load projects. Treating total queue gigawatts as potential compute is an order-of-magnitude error. What matters for AI is not total queue gigawatts. It is the thin slice of high-voltage spurs and main transformers that can actually deliver inside five years. This volume does not invent how large that slice is. With no cleaned number, it stops at the mechanism.

C.C. Wei in 2Q26 said packaging capacity already limits customers' growth. That is a foundry-side limit. If power also limits power-on, customers hit two walls at once: the wafers do not come out, and the cabinets do not light. The two walls need not arrive together. What can be confirm now is the first. The second is still a mechanism, not a checked power-on failure rate.

### 3.3 Nuclear arrangements sit on different delivery clocks

Training clusters want a high load factor and want twenty-four hours. A nuclear output curve fits better than wind and solar. A power-purchase agreement buys the power price and the carbon attribute together, and it also buys the political symbol. Restarting a shut unit takes a safety review, equipment replacement, and a rebuilt crew. A 20-year long is a demand anchor for those fixed costs. The SMR 500 MW is written in 2030 to 2035, the back half of this monograph's ten-year window. It cannot balance the 2026-to-2028 depreciation peak. Large nuclear-linked contracts show long-duration power reservation, but they do not establish that nuclear power has already become the dominant operating supply for AI data centers.

The three contracts stand for three levels of technical maturity. Restarting an in-place pile is fastest and heaviest as a political symbol. Direct connection next to a pile is medium speed and tests the grid's rules for large-user direct supply. SMRs are slowest, an option on campuses after 2030. Writing the three contracts as "tech firms have already solved energy" treats an option as spot. What 2026 to 2028 can use is mainly the first two. In the front half, only operating or restartable blocks count. SMRs in the back half are options. Amazon's $0.65B bought a campus site already tied to a plant. The essence is buying time, not buying a pile type. The dollar amount is a draft claim. The mechanism is buying time.

A nuclear restart and a new SMR are not on the same capex calendar either. Three Mile Island is "waking a unit that already existed." The main uncertainties are the license, the equipment, and local politics. Kairos is "waking a pile type that has not yet run commercially." The uncertainties are design certification, the supply chain, and first-of-a-kind demonstration risk. A 20-year power contract paired with short-lived compute hardware creates duration mismatch: valuable in a constrained-growth scenario and potentially burdensome in a hard landing. The investment-side "overweight nuclear and interconnection rights" must carry this fork. Otherwise overweight is a slogan. historical stress-test material gave no power-price formula. This volume does not invent a price per megawatt-hour.

On geopolitics, the U.S. East becomes historical stress-test material's nuclear-and-compute coupling sample because of Three Mile Island and Susquehanna. Texas and California are named as queue battlefields, but historical stress-test material gives no data-center load numbers for those two regions. Power paths in China, Europe, and the Middle East are not written in this volume's source. Three U.S. cases cannot be extrapolated into global nuclearization. A nuclear permit is a state capability, not a cloud-vendor capability. The United States still has restartable commercial piles and a relatively intact regulator. That is the premise on which the Three Mile Island story can appear. An economy that has only chip subsidies and no permit path will be absent from the back-half campus-power scenarios. This volume does not write those economies' megawatts.

### 3.4 Breaking the chain: cabinets sit in inventory; do prepayments still rise

The engine of the acceleration is: demand rises, profit rises, more capacity and HBM are prepaid. For power to break it, "demand rises" must stop at shipment. Prepayments lock wafers and bits. After the wafers are packaged and the cabinets assembled, there still has to be a floor that can take 120 kW. That floor is not inside a TSMC fab and not inside a Hynix fab. The floor sits at the substation, the feeder, and the permit office.

Hypothesis from here, without rejecting the main line. Two forks.

Fork A: power has not stopped the buildout. Cabinets ship on the prepayment clock. FY26 data center $193.7B keeps serving as global rent. Supply commitments add again from $119.0B. Packaging stays tight. C.C. Wei's "limits customers' growth" stays in force. The HPC 58%, up 48% year on year, increment keeps being occupied by the first name. Residual multiplies by cabinet. Phones and PCs pay a memory tax. This is the judgment's main road: if those five are not done, the line walks past half of the scarce slice. On this road, power is a hall cost, not an interrupt.

Fork B: power becomes the binding brake. Prepaid packaging and systems can become stranded or delayed if campuses cannot energize them. That can reduce utilization, delay take-up, and weaken the next round of commitments. A freed manufacturing slot is not automatically reassigned to a specific rival: the entire line can slow, another high-credit buyer can take it, or suppliers can rebalance across customers. Power therefore interrupts the resource loop through **utilization and order certainty**, not because TSMC has a duty to favor or avoid offending any one customer.

The present walk is Fork A. There is no checked interconnection effective capacity, no checked power-on failure rate, and no checked take-up cancelled because of power. Fork B is a mechanism, not a sentence that can be written as fact in August 2026. This volume leaves Fork B as a falsifiable interrupt. It does not announce a win early.

Microsoft's hundred billion of net income is used on halls. NVIDIA's hundred billion of free cash is used to reproduce the scarce slice. The two sums do not sit on one "who is richer" table. If power stops the buildout, Microsoft's hundred billion becomes cement waiting for power, and NVIDIA's hundred billion becomes inventory waiting for power. Neither side can wait out a four-year depreciation, but the pain points differ. The cloud's pain is construction-in-progress and power longs. The system platform's pain is revenue recognition and whether the next prepayment still rises. The foundry's pain is a slot window. The three pains added together are the cash-flow meaning of "power stops the buildout."

### 3.5 Power is not a platform layer and does not change the three layers

The four corners are system platform, software/runtime layer, supply-coordination layer, and model player. Power does not sell cabinets, does not set a unified compute architecture, does not schedule the Hopper-to-Blackwell-to-Rubin mix, and does not ship Nemotron. The nuclear counterparty is a constraint seller. A cabinet that can take power is still the system platform's product. A power-purchase agreement strengthens "the cabinet that can be delivered." It does not stand up another software/runtime layer. Writing nuclear operators into the 60%-to-75% gross-margin boilerplate mistakes a constraint seller for a platform layer. No plant statements were opened in the current evidence review. Delete the pairing.

Three layers are not one layer. The scarce objects on the phone layer are leading-edge logic and LPDDR. The scarce objects on the PC layer are x86, Windows, and discrete GPUs. The scarce objects on the AI layer are the cabinet, HBM, packaging, high-speed interconnect, and a unified compute architecture. Power binds power-on on the third layer. If power does not stop the buildout, the first and second layers still pay a memory tax, because makers still have a motive to convert to HBM. If power does stop the buildout, third-layer cabinets do not sell; the residual tax on the first and second layers does not vanish on its own. It only draws one fewer slice of new cabinets. The audit already wrote: if power stops the buildout first, the first wave's tax does not vanish, but the system platform's cabinets do not sell and expansion on the 75% side stops. That is "the people who can wait suddenly cannot wait." It has not yet become the sole dominant constraint yet.

The China market cannot save global cabinets and cannot save global power. At home it can at most supply phones in parallel. PCs and AI do not resolve. The layer is wrong. Eastern capacity is a parallel bid. It cannot take the first name's seat on packaging and 2nm, and it cannot take the substation at the gate of a North American cloud campus. This volume does not write China grid numbers. The structure can be written: if the East is to stand up a second bid, it must buy material on the same layer, and it must have power on the same layer. Without power, a parallel bid is also a warehouse.

### 3.6 The depreciation clock, the permit clock, and the chip clock

historical stress-test material wrote four-year server depreciation and fifteen-year data-center civil depreciation as hard accounting constraints. The permit clock is 5–7 years. The chip clock is packaging moving from tight to limiting customers' growth, already happened. The three clocks do not line up. A finance clock shorter than the permit clock is the most dangerous accounting mismatch: the asset-life finance clock finishes a lap while the power permit is still in the queue. Whoever first shortens the permit clock (restarting an in-place pile, building next to a pile, buying a campus that already has power) privatizes the third quota. The public narrative for shortening the permit clock is still only those three, and the megawatts were not checked against originals.

Four-cloud mixed-year equipment purchases of about $211.9B to $213.9B are group-wide, not an AI-hardware line item. How much of that money became cement waiting for power: this volume has no split. Part II writes 2026 power and civil works at about $207.5B, a forecast, unverified. The same civil dollar, spent on a campus with no permit, books as cement; spent on executable megawatts, books as the third quota. Spend it in the wrong place and the sign flips. This volume does not invent how many megawatts are executable.

The light assets sit on NVIDIA's books. FY26 purchases of property and equipment plus intangibles $6,042M, which does not match a wafer fab. The heavy assets sit at TSMC and Hynix. Clouds buy scarcity into depreciation. Power's heavy assets sit at the plant, the main transformer, and the corridor. Three sets of heavy assets are not on one balance sheet. The clocks still have to stack on one delivery chain. If they do not stack, delivery stops. That is the physical reason power can break prepayments. A reason that holds is not an interrupt that has already happened.

### 3.7 Liquid cooling is the in-cabinet energy chain; the battlefield is still the node

Once CDUs, cold plates, quick couplings, and leak detection become standard on a 120 kW cabinet, suppliers move from server parts to the data center's second power-electronics layer. historical stress-test material's $40,000 to $55,000 per-cabinet direct liquid cooling is hardware only. It excludes hall water-loop retrofit, water rights, and discharge permits. The investment side lists liquid-cooling CDUs next to nuclear and interconnection rights for this reason: they are all permit conditions that turn 120 kW from a design value into a running value. This volume does not estimate the liquid-cooling market.

A cabinet that cannot take power is inventory, however high the high-speed interconnect. Two engineering responses then appear. One moves training onto campuses that already have a power-purchase agreement and accepts geographic concentration. One splits inference onto weak-power nodes or the edge and accepts a performance ceiling. The first hardens joint rent between the oligopoly and counterparties who can lock baseload. The second feeds ammunition to an algorithm or edge interrupt. The 120 kW cabinet itself leans toward the first, because this density is hard to plug first and ask later on an ordinary campus. So the energy war is not an appendix to the chip war. It screens which business models are physically feasible. Screening in progress is not nuclearization already finished.

Cross-region comparison must stop in this volume. China's west-to-east transmission, Middle East gas generation, and Nordic hydro can all rewrite local compute siting, but the source Volume 13 gives no non-U.S. numbers. Filling those numbers in would be a violation. A reader who wants a global energy map should go outside Volume 35's task and find original grid files, not look in this volume for "overseas megawatts already checked for you."

## 4. Added analysis

Power extrapolations are unverified.

### 4.1 Scenarios: power wins, power does not win, power arrives late, power is routed around by algorithms

Scenario A: in-place nuclear is fully booked. Latecomers can only queue or go to nodes with higher prices and harder politics. The compute map coincides with the nuclear-plant map. A cabinet that can take power becomes a harder system platform product. That is the discussion's product-side "yes." It strengthens the four corners. It does not split them. In this scenario power does not break the acceleration. It adds a permit moat to the acceleration.

Scenario B: power stops the buildout. Already-prepaid cabinets sit in inventory. Supply commitments stop rising, or they only reschedule instead of locking new capacity. A packaging window opens. The HPC increment is no longer scheduled to the first name's check. That is the judgment's third interrupt winning. There is no checked evidence that has walked here. To win, at least one of power-on failure, delayed take-up, or commitments stopping their add must be visible, public, and recheckable.

Scenario C: SMRs slip. The 500 MW 2030-to-2035 node moves right. The 2026-to-2028 power gap can only be met with gas peakers or delayed cabinet power-on. Capex becomes construction-in-progress. Back-half megawatts cannot hedge front-half depreciation. The clock error itself takes the "nuclearization" narrative apart: in the front half, only operating or restartable blocks count.

Scenario D: algorithms and liquid cooling push power intensity down. Architectures of the low-rank-attention class cut wasted memory movement. PUE improves. A 120 kW-class cabinet still wants a dedicated spur. Lower intensity is not a vanished queue. If cloud ASICs only shunt inference, the training cabinet's point load is still there. Public next-gen parts have not retreated to 5nm plus commodity DDR5. To beat today's cabinet you return to 3nm, HBM, and advanced packaging, and you bid against 75% gross margin. Only a real retreat that uses less packaging dodges the scarce slice and also dodges part of the point load. Public next-gen parts have not stopped. So D is not done either.

Scenario E: local opposition and power-price politics. Residential rates are blamed for subsidizing data centers. Power-purchase agreements are reopened or capped. The nuclearization narrative stalls. This is a municipal-layer interrupt. It is not the same as a national shortage. A node failure is enough to leave one campus's cabinets at the gate.

None of the shared interrupt variables is done. Power's three ways of winning (B; the front-half gap inside C; the node veto inside E) are not done either. A is a strengthening, not an interrupt. The main road is still the judgment's sentence: if they are not done, the line walks past half of the scarce slice. The window is the few years before the next first-to-market node is locked by commitments. For power to act inside the window, commitments must stop rising. A slide of SMRs ten years out is not that.

### 4.2 Counters

Counter 1: power is only a cost, not a strategy. 600 million kWh is a small head against a large state's use. Against a point load and local congestion it is not a small head. Strategy comes from the local, not from the national share. Writing ample national installed capacity as "power is not an interrupt" drops the node.

Counter 2: gas, and wind-and-solar plus storage, are faster. historical stress-test material takes baseload and zero-carbon as a preference the clouds have already revealed. It does not rule out burning gas in a transition. This volume does not invent gas-fired megawatts. Transition gas can shorten the permit clock by a slice and can let "nuclearization" not have to win first. If burning gas really lights the cabinets, this interrupt has even more not won. There is no checked gas-substitution table.

Counter 3: $16B and $0.65B are one-off news, far smaller than mixed-year equipment purchases on the order of $200B, so energy is not yet the main field. The small dollar amount is exactly the point: in-place nuclear blocks that can be bought are few. Scarcity shows up in megawatts and time, not in the percentage of capex. Using a dollar share to deny strategy is the wrong ruler.

Counter 4: replace megawatts with green certificates. A green certificate buys an attribute, not a feeder. An attribute does not fill a four-year depreciation. Write only an environmental target and not executable megawatts, and what you get is a certificate. A certificate does not light a 120 kW cabinet.

Counter 5: use 2,600 GW to prove power is ample, or use a 2036 campus plan of 2 to 5 GW to prove 2026 already has power. The first treats the queue as supply. The second treats an end-state table as spot. The 2036 four-dimension table does not enter the fact layer, not one cell. This volume does not cite that forecast grid to prove power is here or not here.

Counter 6: power will stop the buildout first, so the four corners are already finished. That treats a mechanism as an end state that already happened. With no power-on failure rate, you cannot write hegemony's obituary. Power, like the China stack and cloud ASICs, can overturn. None of them has won. Forecast numbers stay empty.

### 4.3 Falsifiable indicators

What is falsifiable and now empty matters more than a mechanism that can be narrated.

Whether Three Mile Island Unit 1 restarts on the 20-year long and sends historical stress-test material's 835 MW. Whether Cumulus direct supply approaches historical stress-test material's 960 MW. Whether the 7 Kairos units interconnect in historical stress-test material's 2030-to-2035 window. All three must be judged on regulatory or company files, not on news headlines.

Whether PJM, Texas, and California public queues still write above 2,600 GW, and whether a cleaned effective capacity exists. With no cleaned number, 2,600 GW still does not enter the fact layer.

Whether newly announced data-center IT loads commonly enter above 60 MW. Whether liquid-cooled cabinets run at the 120 kW design instead of derating. Derated operation means the density narrative loses first, and the power interrupt weakens by a slice, because the point load never reached historical stress-test material's block.

Whether supply commitments keep rising next quarter. They were already $119.0B at the end of Q1 FY27. If they stop rising or are rescheduled at scale because of power, this interrupt has its first cash-flow evidence. It does not now.

On packaging: whether C.C. Wei still says it limits customers' growth, and whether the reason customers' growth is limited has moved from wafers to power. Official text does not split that. The report does not infer it.

system platform revenue: whether data-center revenue is still recognized on the cabinet, or whether inventory language of "shipped, not powered" appears. The 10-K does not have that sentence. The report does not infer it.

Power price, PUE, and the household conversion stay with historical stress-test material. The report does not infer new ones. In the stress test, power at $0.08 per kWh and PUE 1.2 are assumptions, unverified.

### 4.4 Interfaces with packaging, memory, cloud ASICs, and antitrust

Packaging tightness is a supply-coordination layer-side limit that has already happened. Power is a power-on-side limit not yet checked. Do not add the two into "a double lock already finished." The add is publicity. Split by state is the map: wafer tightness is a checked direction; power tightness is a mechanism.

Memory multiplies by cabinet. If cabinets cannot ship, the HBM draw slows. The residual tax does not vanish at once, because maker conversion lags and longs are still on. A power win will not suddenly make phones and PCs cheap. If power has not yet become the sole dominant constraint, the residual model keeps multiplying by the 10,000 / 30,000 / 50,000-cabinet hypotheses.

Cloud ASICs taking training off the cabinet is another of the five. Public next-gen specs are in [Volume 4](vol-04.en.md): no retreat to 5nm plus commodity DDR5. Those chips also have to take power. If cloud ASICs win, the training load may change cabinets. The point load does not necessarily vanish. Power and cloud ASICs are not interchangeable interrupts. They are two independent forks. Neither is done.

Antitrust hits contracts; see [Volume 11](vol-11.en.md). Power hits a physical permit, not a competition-law permit. Do not mix the two permits. The competition-law permit governs whether you can sell. The grid permit governs whether you can light. The permit that governs lighting has no public evidence yet of having stuck the selling.

Bundling still misses three checks. Power substitutes for none of them. If the West actually bundles, it still has to find a floor. If the East stands up a second bid, it still has to find a floor. Power stopping the buildout is the floor disappearing first. If the floor is still there, the other four still have to be done. This volume does not write power as a universal fork that can replace bundling, stack-switching, or a second bid.

The world does not blow up. Upgrades stop one node down. Phones and PCs pay a memory tax. One firm writes the rules. If power never wins, that sentence still holds. If power wins, upgrades stop earlier, and the reason for stopping one node down gains "cabinets that will not light" on top of "wafers you cannot get." The two stops put the rent in different places. The first still sits on the cabinet price and the packaging quota. The second leaks a slice into cement waiting for power and into inventory write-downs. The rent now visible is still FY26 data center $193.7B. The second has not booked.

### 4.5 The window is still open; power has not closed it

The judgment writes the window as the few years before the next first-to-market node is locked by commitments. The FY26 10-K only writes prepaid manufacturing and capacity agreements for current and future products. It does not name a 2nm first-silicon dollar amount. Empty contracts are still places where someone can add price, bind a long, or switch stacks. For power to act inside the window, that empty contract must stop being added to by the first name alone. What is visible now is the reverse: $23.8B added in three months. The company itself wrote it as locking inventory and capacity. The window is still open. The name adding is still the first name.

A local node short of power and a global halt to prepayment adds are not the same thing. If one campus fails at the substation, the cloud can redirect the next cabinet to a campus that already has a feeder. The system platform recognizes revenue on the cabinet, not on a county's main transformer. So "somewhere cannot take power" is not enough to win. To win, failures must be dense enough that cabinets cannot find the next floor, or dense enough that the cloud will delay take-up and reschedule supply commitments. A single news item, a single power-purchase agreement, a single restarted unit: all prove someone is buying time. None of them proves the floor is already gone. Buying time is Fork A's move: power has not stopped the buildout, so privatize the nodes that can light first.

Booked 19% is not a safe distance. Occupy the increment and next year's slots belong to the first name. Power has not changed that sentence. What power can change is: if the increment will not light, the slot goes empty. Empty, TSMC still has no financial reason to offend the first name for the second, unless the first name truly stops ordering. The first name's FY26 free cash is $96.575B, one quarter of operating income $53.536B, and the last two quarters of gross margin back near 75%. That set says it still has a pad to add. Power has not taken that set off the books. If it cannot take it off, the acceleration engine is still turning.

Hypothesis from here. While the margin holds, commitments keep rising. Anyone else who wants the same material pays more, or does not get it. Packaging stays tight. Slots keep tilting to the first name. Cabinets keep shipping. Memory multiplies by cabinet. The residual goes to a few dozen brands. Power keeps existing as a node permit and keeps forcing clouds to sign longs, buy campuses that already have power, and book piles that have not yet run commercially. Those moves change who lights first, not who first stops being the system platform. Whoever lights first pays the next slice of rent out of the $193.7B. The rent is still paid to the firm that sells cabinets. The nuclear counterparty collects a power bill and a carbon attribute, not the cabinet price. Do not add the two into "energy has already replaced chips as the rent."

Intel 1999: revenue $29,389M, net income $7,314M, gross margin 59.7%. That was CPU share. Today is one year of free cash $96.6B and one quarter of operating income $53.5B. The share-era break was making a second chip that ran the same software. The margin-era break is splitting a unified compute architecture, the 72-card domain, packaging slots, and HBM longs at once. Power is a fifth piece. It splits the floor. Split only the floor among the five and the other four still hold. After the cabinets light, the four corners are still there. So even if Scenario B actually happens, the win is only slowing the buildout clock, not automatically standing up a second software/runtime layer. After the clock is slowed, the window keeps a few more years. In those extra years, Western bundling, cloud ASICs taking training, and an Eastern second bid have time to split the other four. A power win alone buys time. It does not buy a substitute stack.

This volume leaves that sentence to Volume 10 and Volume 15 as a switch: power stopping the buildout is one of the switches, and it is now thrown off. Throwing it on requires a falsifiable power-on failure and a halt to commitment adds. Until then, Volume 13 stops here.

## 5. Gaps and what cannot be treated as fact

2,600 GW is not split into generation, storage, data centers, or duplicate positions. It does not enter the fact layer. 5–7 years and 12–18 months are ranges, with no project sample. 60 to 80 MW, 600 million kWh, and 60,000 households are engineering conversions. This volume did not recheck grid or statistical-agency originals. The Microsoft long "over $16B" appears only in a Part II figure note. Volume 13 did not write it and did not supply a contract text. Three Mile Island 835 MW, Susquehanna planned 960 MW, $0.65B, Kairos 7 units at 500 MW: historical stress-test claims. the current evidence review did not read power-purchase agreements or regulatory files. They do not enter the fact layer. SMR technical route, permitting, and financing are not opened. There are no China, Europe, or Middle East grid numbers. Nuclear-operator 60% to 75% gross margin is a boilerplate sentence, not a plant filing. Delete it. 2026 power infrastructure $207.5B is a forecast. Power at $0.08 and PUE 1.2 are assumptions. This volume read no power-purchase-agreement original and does not claim an audit.

historical stress-test material "four-cloud 2024 capex officially broke $215B of AI" cannot be treated as fact. What can be added is mixed-year group-wide equipment purchases of about $211.9B to $213.9B. 2026 $670B to $750B cannot be added. 2036 campuses at 2 to 5 GW, four-scenario probabilities, and penalty-rate extrapolations: the whole table does not enter the fact layer.

This volume does not estimate how many cabinets 835 MW feeds. It does not estimate the liquid-cooling market. It does not subtract the queue's total gigawatts into "enough once you remove data centers." It does not add the three contracts into "2.3 GW of compute power already exists." The add is publicity. Split by state is the map: signed restart, acquired adjacent build, forward-ordered pile. The three states cannot be added.

The report does not treat power as a platform layer. The report does not treat nuclearization as already rewriting the four corners. The report does not treat an option as 2026-to-2028 supply. The report does not treat hegemony's obituary from an unchecked power-on failure rate. Do not deny a node strategy with ample national installed capacity. Do not deny megawatt scarcity with a dollar share.

The heat-grid-nuclear set will, in reverse, change chip and software design goals. A cabinet that cannot take power is inventory, however high the bandwidth. This volume leaves that sentence in the mechanism layer. Interrupts that have been done: still zero. Cash that has been done: still supply commitments $119.0B, and FY26 data center $193.7B of rent. Power wins only if it stops those two. It has not yet become the sole dominant constraint yet.
