# Volume 37: Four-year depreciation and tokens do not match ($750B cannot be added; the matrix is draft)

Chinese original: [vol-37.md](vol-37.md)

The depreciation wall: [Volume 30](vol-30.md). Four-cloud scope: `四云Capex口径核对.md`. Antitrust: [Volume 11](vol-11.md). This volume does not reopen the case file. The token matrix is marked draft. No sample.

> Retrieval and check cutoff: 2026-08-26. The base is the judgment and [Volume 11](vol-11.md). Capex addition: `四云Capex口径核对.md`. What this draft read is each firm's IR / Exhibit 99.1 / official press releases, not a page-by-page audited full 10-K. New judgments are marked "Analysis added." Quantities without a source are marked "unverified, not an audit fact." Draft compilation sentences are marked "draft number" and are not promoted.

## 1. The question this volume answers

A bubble does not show up in a stock-price slogan. It shows up in whether three books can be made to match: four-year hardware depreciation, token unit price, and real enterprise usage. This volume answers four things. First, after checking, what is that 2024 "four-cloud capex" already on the ground, and is it "AI hardware"; in which year does it become order cuts and destocking. Second, which price–usage combinations survive, and which turn GPUs and HBM from scarce assets into overhang. Third, whether rent the seller has already collected and depreciation the buyer has not yet finished taking are a knock on the same table. Fourth, whether an antitrust investigation can take this depreciation wall down.

The judgment nailed "the numbers are current." What follows from them is a hypothesis from the present. What can change the rules overnight is a breakup or a forced opening of CUDA, not a fine. After national security wrote advanced compute as a license item, a breakup is harder to touch. The application layer is grinding. Data-center revenue is the rent. This volume does not call a stock-price drawdown a bubble burst, and does not treat one DeepSeek training cost as the industry forever needing only five million dollars.

## 2. What the draft already argued, and corrections already checked

### 2.1 How the draft wrote the bubble (compressed; no key number dropped)

The draft's accounting start: the four clouds' combined 2024 capex broke $215B. On four-year straight-line server depreciation and fifteen-year buildings, that stock brings $45–55B of rigid hardware depreciation each year in 2025–2028. The draft called this a hard financial constraint and wired it directly to hunger for high-efficiency architectures (DeepSeek MLA) and true chip-side ROI.

2024 by firm (draft table, labeled 10-K / official filings; this volume did not re-check originals on the draft's scope): Amazon capex $77.7B (+61.5%), Alphabet $52.5B (+62.5%), Microsoft broke $55B, Meta $30.9B. Seller side: Nvidia FY25 revenue $130.497B, data center $1,150+B, gross margin 75.0%, own capex only $2.98B; TSMC 2024 revenue $88.34B, capex $29.85B; SK hynix 2024 operating profit KRW 23.47T (35%), HBM over 40% of DRAM revenue. All of the above are draft numbers.

2026 stress test (draft forecast, not already happened): four-name capex sum $670–750B, hardware about $462.5B, power and buildings about $207.5B, annualized depreciation about $115.5B, holding ROI needs above $155B of incremental AI revenue a year. Against "current enterprise AI software increment about $35–50B," the gap is $60–80B. Another formula: if annual capex is $750B and 65% is IT hardware, then annual hardware depreciation = \(7500\times0.65/4=1218.75\) hundred million dollars; power and opex at $0.08/kWh, PUE=1.2, about $28B a year; breakeven needs more than $150B of net software / API cash recovery a year. All of the above is draft scenario arithmetic, unverified, not an audit fact.

Token sensitivity matrix (draft):

- Usage +50%: price flat, lose $45B; price down 30%, lose $80B; price down 50% (DeepSeek effect) judged "severe capex overhang, destocking triggered."
- Usage +150%: flat, earn $20B; down 30%, roughly balanced (±$5B); down 50%, lose $30B, procurement forced slower.
- Usage +300%: flat, earn $90B; down 30%, earn $45B; down 50%, still earn $15B, mature period.

P&L in the matrix is a scenario, not an audit result. The draft gave no cloud AI-segment split, no real token-price time series, no days of inventory, no supplier-channel inventory. $0.08/kWh, PUE=1.2, hardware 65% of capex: all assumptions.

Algorithm cost-down anchor (draft, DeepSeek technical-report scope): 671B total parameters, 37B activated per token; 2048 H800s, 2.788 million GPU-hours, 14.8T tokens, training cost converted about $5.576 million; MLA compresses KV Cache 93.3%. Traditional trillion-parameter training was written in the draft as easily tens of millions to hundreds of millions of dollars. Public sources this pass checked the DeepSeek-V3 technical report (arXiv:2412.19437): full-text training 2.788M H800 GPU-hours, converted at the report's own "H800 rent $2/GPU-hour" to $5.576 million; pretrain 2664K, context extension 119K, post-train 5K; cluster 2048 H800s; 14.8T tokens. The report itself notes: this includes only official training, not prior ablations and research. MLA compression 93.3% is a draft engineering sentence. This pass did not match that percentage word for word in the paper. Do not promote it.

Clearing window: the draft marked 2025–2027 as a dense depreciation test, high-cost models that miss ROI are culled, the industry moves into an Agents mature period. Downstream keeps carrying 20%–30% chip-cost inflation. 20%–30% is draft paraphrase. Purchase-price reports were not re-checked this pass. Do not promote it.

### 2.2 Scope the judgment and [Volume 11](vol-11.md) already changed

Four-cloud scope: [Volume 8](vol-08.md) and `四云Capex口径核对.md`. This volume nails only three sentences: $215B is not a reproducible same-calendar-year, same-line-item, AI-split sum; mixed-year 2025 has already changed bins; 2026 three-name guidance cannot add the draft $670–750B. Do not knock seller rent against buyer capex into a rent rate. Profit and cash: [Volume 1](vol-01.md).

## 3. Mechanism (physics / commerce / geopolitics)

### 3.1 Accounting definition of a bubble: the depreciation wall before the stock price

Analysis added. A stock-price drawdown can come from rates, positioning, narrative. It need not come from assets already idle. This volume narrows "bubble" to whether two things, accounting and physics, can hold at once: four-year hardware is still taking depreciation, but machine-hours are not full; token unit price is moving down because of open source and methods of the MLA kind, but usage never reaches the right-hand cell of the draft matrix. Both at once is destocking, not "AI is useless."

Four-year straight line is a template, not a sum of four 10-K asset classes. Useful lives for servers, accelerators, networking gear, and buildings are not uniform, and not every firm uses four years. Microsoft later also changed building lives, which changes the depreciation cadence on the statements, not necessarily a campus already poured. So "that 2024 stock contributes $45–55B of hardware depreciation each year in 2025–2028" is a draft template, not an audit fact. The mechanism that can be written: once capex is in, expense appears on schedule in later fiscal years; the year expense appears is not the year of an order cut. Order cuts look at the next round of orders and prepayments, not PPE already booked.

Mixed-year 2025 is already about $354.0–356.5B. Using 2024's $215B again to push a 2026–2028 depreciation wall understates the base. Specific 2026–2028 expense: unverified, not an audit fact. The direction that can be written: the wall is thickening, not thinning. Thickening itself is not a burst. A burst depends on whether incremental revenue can cover the wall.

### 3.2 Rent sits with the seller, depreciation with the buyer. The two books do not match

Rent with the seller, depreciation with the buyer, accounts that do not line up: [Volume 1](vol-01.md), [Volume 8](vol-08.md). Analysis added. The moment profit is recognized at the seller is earlier than the moment the buyer sells machine-hours into software cash. So "buyer depreciation pressure" and "seller fat profit" can hold at once. If a bubble happens, what hurts first is buyer ROI and second-tier model companies' APIs, not free cash already in the seller's pocket. If destocking happens, it happens inside this bidding structure, not in an industry where "everyone is slightly profitable together."

### 3.3 How to read the token matrix, and how to misread it

The draft matrix's x-axis is usage, y-axis is unit price. The most dangerous cell is not "usage doubles but price halves and you still eke a profit." It is "usage up only 50%, price down 50%" — that cell the draft wrote directly as destocking. The +300% / down 50% still-earn-$15B cell assumes usage compounding at a three-year double-or-better pace. Without that usage, a price cut is destocking. DeepSeek makes a unit-price fall more likely. It does not automatically make usage +300%.

Analysis added. The y-axis has already been opened by open source. DeepSeek-V3 broke the faith that "you must stack a hundred thousand cards to enter," so later names no longer take a hundred-thousand-card training run at the old price. What it breaks is pricing power on first-layer inventory, not fourth-layer power contracts. Whether enterprises can write Agents into cash-producing steps is what decides whether the x-axis has the right to walk right. Seat pricing hid inference cost in R&D or the cloud bill. Agents turn tokens into cost of goods. SaaS margin from 85% to 55% is the draft's meter for an application-layer bubble. No sample this pass. Do not promote it. The mechanism that can be written: if an application company cannot get usage to the matrix's +150% or better, it blows up before the clouds — it does not have Amazon's bulk to spread depreciation, and it pays inference by usage. A model company's inventory is another shape: training budgets already burned, weights that cannot be resold. Open source lowers exclusive rent on weights. Hardware destocking is price and lead time. Model destocking is closing APIs and dismissing research groups. Both are often written as one news item. The mechanisms differ.

P&L figures in the matrix — $45 / $80 / $20 / $90B and the rest — are scenario arithmetic, not an audit result. This volume does not invent a "more precise" P&L table to replace it. Replacement would need a real token-price time series and an enterprise AI incremental-revenue split. Neither exists on the public record.

### 3.4 Where destocking inventory sits. Four layers, four speeds

The three characters "destock" make people look only at the Nvidia channel. Real inventory sits on four layers, impairing at different speeds.

The first layer is GPUs and cabinets not yet racked, the easiest place for spot versus contract concessions. Lead times from tens of weeks back to week-scale delivery, softer prepayment terms, and a bid-able second-hand cabinet — those three are closer to a definition of destocking than "a cloud still says we like AI." The draft had no such high-frequency data. This volume lists them as watch items.

The second layer is HBM and CoWoS work-in-process. Physically the hardest to turn. 3:1: [Volume 5](vol-05.md). Tight packaging: [Volume 24](vol-24.md). A line will not revert to consumer because of one quarter of cuts.

The third layer is four-year servers already installed and already depreciating. The only levers are lower utilization or resale. Resale punches new-goods prices directly. This layer can be impaired on the books. The physical cabinets still sit in halls using power.

The fourth layer is fifteen-year buildings and longer power contracts, almost impossible to destock, only becoming idle megawatts. Power contracts are too long to cut. So a "bubble burst" is not every asset going to zero together. Hardware impairs first; power assets stay on the books as long liabilities. That bites Volume 35's nuclear PPAs: signed megawatts and poured liquid-cooled campuses do not vanish because one training run fell to $5.576 million.

Analysis added. Transmission of cuts: the first knife is the longest-lead, most-prepaid high-end training cabinet; the second is added HBM and CoWoS capacity; the third only then reaches already-interconnected buildings. A hard landing does not look like "AI disappeared." It looks like: new-goods prices drop first, lines idle next, plants and campuses stay on the books. Overweighting fourth-layer physical scarcity hurts most in a destocking scenario and is hardest in a mis-kill-then-reconcentrate scenario — the same asset class changes sign with the endgame branch.

### 3.5 Physical stickiness: power and packaging make capacity irreversible

The calculation pool: [Volume 16](vol-16.md) and [Volume 24](vol-24.md). Residual: [Volume 5](vol-05.md). Cloud ASICs: [Volume 4](vol-04.md). Analysis added. A 120 kW cabinet, the wafer penalty of HBM versus DDR5, advanced packaging lifted from single-digit revenue share to a bit over 10% — none of this is capacity that returns to the old state when an order is cancelled. Books can impair. Lines cannot turn instantly. Destocking therefore has physical stickiness. ASICs shunting inference do not automatically turn second-layer inventory into a consumer line that can be turned.

### 3.6 Antitrust does not change depreciation. A fine is a cost

The case file: [Volume 11](vol-11.md). This volume does not reopen it. A fine is a cost. National-security documents exist. "Therefore they will not break it up" does not. Bubble clearing can still happen. The trigger is depreciation not matching usage, not a courtroom. Dual stacks: [Volume 12](vol-12.md). Supply is built as two safety stocks. Demand does not double.

## 4. Analysis added (scenarios, opposition, testable markers)

P&L in the matrix is a draft scenario, unverified, not an audit fact. The three scenarios below do not invent a new P&L table. They only attach mechanisms the judgment allows to a clearing path.

### 4.1 Scenario A: soft landing

Usage runs +150%–+300%, token prices fall less than 30%, clouds trim the next round of spending but do not collapse. Nvidia margin gives some back from 75.0% and is still well above TSMC 2025's 59.9%. The industry enters the draft's Agents mature period. Supply commitments no longer stack at $23.8B every three months, but the $119.0B already locked is paid on schedule. Check: D&A in the annual report rises but free cash does not turn negative; four-cloud group capex decelerates from the mixed-year 2025 order of about $354.0B rather than halving; public-cloud token prices step down, but enterprise annual reports start disclosing AI incremental revenue separately. Unverified: do not forecast which year revenue covers depreciation.

### 4.2 Scenario B: destocking

Usage stops near +50%, open source drives unit price down 50%. The matrix judges overhang. GPU spot versus contract concessions, HBM lead times shorten, CoWoS shows empty slots. TSMC HPC share rolls over from a high, Hynix HBM revenue share gives back from the draft's 40%. That is the back half of a classic capex cycle, not "AI is useless." First-layer inventory reprices first, second-layer lines idle, third-layer installed cabinets lose utilization, fourth-layer power contracts stay on the books. NVIDIA data-center revenue leaving the FY26 $193.7B order, gross margin leaving the 71.1% to 75.0% band — those two sentences are controls, not forecasts. Official text already wrote that some supply agreements can be rescheduled. Reschedulable is not already rescheduled. This volume does not invent reschedule amounts.

### 4.3 Scenario C: mis-kill, then reconcentration

A hard landing clears second-tier model companies and second-tier cloud regions. Quota and nuclear contracts stay with a few giants. The 2036 oligopoly scenario is strengthened by the bubble. The opposing path is an algorithm break: intelligence becomes cheap enough, infrastructure decays into a thin-margin utility, bubble residue becomes a regulated asset. The draft gave probabilities. This volume does not reuse them and does not open new percentages. The mechanism that can be written: after clearing, scarce-slice slots concentrate further, they do not disperse. The judgment: booked 19% is not a safe distance. Occupy the increment and next year's slots belong to the first name. If destocking only clears the second tier, the first name's increment share gets larger.

### 4.4 Testable markers (direction only)

- Combined four-cloud capex versus mixed-year 2024 about $211.9–213.9B and mixed-year 2025 about $354.0–356.5B: still adding, or decelerating sequentially. The 2026 three-name official-guidance midpoint about $490–520B (missing Microsoft) is already above mixed-year 2025, but it is guidance, not actual.
- Whether public-cloud token prices show a 30% or 50% annualized step. There is no official all-market index. Watch each firm's price page. Do not add them into an "industry unit price."
- Whether enterprise annual reports start disclosing AI incremental revenue separately, and whether it can approach the draft's required $155B. $155B is a draft breakeven sentence, unverified.
- Whether Nvidia data-center revenue can still accelerate from FY26 $193.7B; whether gross margin stays in the 71.1%–75.0% band.
- Whether supply commitments keep adding from $119.0B, or rescheduling appears.
- Whether HBM lead times and CoWoS quotes are premia or concessions; whether a bid-able market for second-hand training clusters appears.
- Whether justice.gov shows a *United States v. NVIDIA* complaint; whether France issues a statement of objections; whether the EU shows a 101/102 opening. Investigation without a complaint is the 2026-08-26 state, not an eternal state.
- Next TSMC customer split: whether the first customer leaves 19%. Jensen has said they are already the largest customer. The 20-F does not name names.

### 4.5 Opposition

Calling a stock-price drawdown a bubble burst ignores that depreciation has not yet entered peak years, and ignores that the mixed-year 2025 base is no longer $215B. Treating one DeepSeek training cost as the industry forever needing only $5.576 million ignores the report's own "excludes prior ablations," and ignores that inference scale can still eat a whole cabinet of power. Writing 2026 $670–750B as capex that has already happened. Adding four-cloud capex into "$215B of AI hardware." Writing FY26 data center $193.7B as a four-cloud line item paid to NVIDIA. Writing 10% of annual revenue as a fine about to be issued. Writing a subpoena as a breakup order. Reading a national-security memorandum as "therefore they have already decided not to break it up." Reading "regulators are looking" as "the depreciation wall will be taken down."

### 4.6 How to read the three books at once. Do not knock them into one tax rate

Analysis added. The three things in this volume's title — four-year depreciation, token unit price, destocking — are not three parallel news items. They are one cash-flow projected at three dates. The year capex goes in, the seller recognizes revenue and margin; for four years after, the buyer takes depreciation on schedule; token unit price decides how much cash each machine-hour recovers in those four years. Destocking is a channel phenomenon visible only in year three or four, but it is jointly decided by year-one bids and year-two usage. Compressing the three dates into "already a bubble now" or "not a bubble yet" misreads both.

The first book is buyer PPE. Scope: [Volume 8](vol-08.md). What can be written: the base is rising. Wall thickness depends on hardware share and useful life, which firms do not disclose to a reproducible add. "$45–55B of hardware depreciation a year" can only be a template.

The second book is seller rent. See [Volume 1](vol-01.md). This book recognizes early and takes cash fast. It does not answer whether buyer machine-hours were sold. If destocking happens only in the second tier, this book can keep adding.

The third book is token unit price and usage. There is no all-market index on the public record. The draft matrix gives nine cells. This volume keeps it as a scenario and does not invent another. The only reading that can be written: the y-axis has been opened by open source; the x-axis still depends on whether the workflow produces cash. DeepSeek-V3's $5.576 million is a rent conversion of one official training run, not a clearing price for the inference market. After inference turns tokens into cost of goods, application-layer margin pressure and cloud depreciation pressure meet on the same operating statement. Before they meet, the seller can keep collecting rent, the buyer can keep adding PPE, and stocks can keep arguing "is it a bubble." After they meet, one can talk about which layer the first destocking knife hits.

The three books not matching is not a data error. The accounts were never one-to-one. [Volume 11](vol-11.md) forbids knocking mixed-year capex against data-center revenue. This volume obeys. What is forbidden is a tax rate, not the mechanism. The mechanism is still: the application layer grinds at the front, profit is siphoned at the rear. What grinds is token unit price and seat pricing. What is siphoned is cabinet invoices. Phones and PCs that do not buy GPUs still pay an overflow tax on memory residual. That tax does not enter this volume's matrix, but it makes the shortcut "destocking equals a consumer-electronics thaw" harder — makers have already retuned lines for HBM. Consumer bits are not another river.

Antitrust sits outside these three books. An investigation can change referee power. It does not yet change PPE already booked, or cabinets already shipped. A fine is the seller's cost, depreciation the buyer's expense, tokens the application's cost of goods. The debit sides of the three tables are not the same legal person. So "wait for a fine to clear the bubble" does not hold in accounting. What waiting can get, at most, is a little give on interfaces, and ASICs able to attach to part of the network. Fat profit and prepayments are not touched. Four-year depreciation is still taken.

Power is a fourth book. This volume does not open installed megawatts. It only leaves the interface. Signed megawatts and poured campuses belong to fourth-layer inventory. Tokens can get cheaper. Power contracts will not reschedule on token pricing. If Agents fill machine-hours, power is the bottleneck. If Agents do not fill them, power is idle liability. Both readings hold. They depend on the x-axis, not on the next financing narrative.

Micro signals of an order cut often precede the filing. Lead time, prepayment terms, second-hand cabinet quotes: three thermometers for first-layer inventory. All three softening at once, and the matrix cell +50% / down 50% is no longer hypothetical. Conversely, as long as CoWoS and HBM are still allocated by quota, the main bubble narrative has not entered a clearing segment. Quota still there means the first name is still using profit to lock slots. Slots still there means second-layer inventory has not idled enough to have to revert to a consumer line. This volume does not read "a cloud publicly says capex will still rise" as a disproof — guidance can rise while lead times shorten. Both at once only says seller and buyer narratives are not yet aligned. It does not say destocking has started or ended.

Prepayments can be rescheduled: a sentence the 10-K itself wrote, not already rescheduled. Analysis added: reschedulable means there is a layer of contract elasticity between the first and second layers. When that elasticity is used, the channel has not yet repriced and the line has already skipped the next wafer. That is an earlier internal signal than a spot concession, but outsiders cannot read a split. So the testable item can only be "whether the supply-commitment total keeps adding or rescheduling appears," not "how much was rescheduled to TSMC, how much to Hynix." No split, do not invent.

The China stack cannot catch Western destocking. The wrong layer was already written above. Here only one allocation implication: if Western first-layer inventory reprices, it does not automatically become cheap training cabinets for Huawei or domestic clouds. Export controls block the return channel. Cabinets that reprice and cannot leave the country resell inside the West, hitting Western new-goods prices, not an Eastern supply gap. The East wants domestic bits and packaging that can pass an administrative lock, not a Blackwell cabinet stopped by a license. Writing "global destocking" as "domestic compute copium" is the wrong layer again.

## 5. Gaps and what must not be treated as fact

The draft gave no cloud AI-segment split, no real token-price time series, no days of inventory, no supplier-channel inventory. P&L in the matrix — $45 / $80 / $20 / $90B and the rest — is scenario arithmetic, not an audit result. $0.08/kWh, PUE=1.2, hardware 65% of capex, annualized depreciation $115.5B, breakeven incremental revenue $155B, 2026 four-cloud $670–750B: all draft assumptions or compilations, cannot be added this pass, stay marked unverified. 20%–30% chip-cost inflation, SaaS margin 85%→55%, MLA KV compression 93.3%, CoWoS monthly capacity 13k→130k and 60% lock: not a TSMC or NVIDIA line item. Do not promote them.

This volume did not audit full 10-Ks page by page. SEC HTML fetches from this machine were refused. Figures follow official earnings releases / Exhibit 99.1 / sentences already checked in the judgment. If a 10-K restates, the 10-K wins. Specific destocking quarters, price-drop sizes, and clearing lists cannot be derived from the draft or [Volume 11](vol-11.md). This volume does not invent them.

Not yet happened, cannot be written as already happened: a DOJ complaint, a settlement, a Mellanox split, a forced opening of CUDA; a French statement of objections, a French or EU fine; "a 10% of annual revenue fine about to be issued"; a White House / Pentagon text already forbidding a breakup; four-cloud "AI hardware capex $215B"; 2026 four-cloud already spending $670–750B; token unit price already down 50% annualized; a bid-able second-hand cabinet market already there.

What can be written: the depreciation-wall mechanism is there; template numbers are not an audit; the token matrix is a scenario. Whether a bubble is already clearing: the public record still has no official sample of lead time, prepayments, and second-hand cabinets appearing together. No sample, do not write summer 2026 as a clearing segment.
