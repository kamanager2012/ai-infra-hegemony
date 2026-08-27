# Volume 37: AI Infrastructure Bubble Detection and Market-Clearing Framework

Chinese original: [vol-37.md](../vol-37.md)

Depreciation and capital clearing: [Volume 30](vol-30.md). Hyperscaler CapEx scope: [Volume 8](vol-08.en.md) and [../四云Capex口径核对.md](../四云Capex口径核对.md). Regulatory procedure: [Volume 11](vol-11.md).

> Retrieval and revision cutoff: **2026-08-27**. This volume distinguishes observed facts, scenario stress tests, and market-clearing indicators. Large CapEx by itself is not evidence of a bubble; the relevant question is whether utilization, clearing prices, and forward commitments deteriorate together.

## 1. The question this volume answers

A bubble does not show up in a stock-price slogan. It shows up in whether three books can be made to match: four-year hardware depreciation, token unit price, and real enterprise usage. This volume answers four things. First, after checking, what is that 2024 "four-cloud capex" already on the ground, and is it "AI hardware"; in which year does it become order cuts and destocking. Second, which price–usage combinations survive, and which turn GPUs and HBM from scarce assets into overhang. Third, whether seller-side value capture the seller has already collected and depreciation the buyer has not yet finished taking are a knock on the same table. Fourth, whether an antitrust investigation can take this depreciation wall down.

The report does not call a stock-price drawdown a bubble burst, and it does not treat one public training-cost example as an industry-wide cost function. A hard landing requires a combination of accounting pressure, weak utilization, market-clearing deterioration, and weaker forward commitments.

## 2. Evidence boundary and stress-test inputs

Historical versions used a fixed token price–usage matrix, a four-year hardware depreciation template, and point estimates such as $215B of "four-cloud AI CapEx." Those inputs remain useful only as stress tests.

The current evidence base is narrower and stronger:

- mixed-year 2024 company-wide CapEx/PPE of roughly **$211.9B–$213.9B**;
- mixed-year 2025 company-wide CapEx/PPE of roughly **$354.0B–$356.5B**;
- 2026 public company guidance/TTM figures that use different windows and therefore cannot be directly summed;
- NVIDIA FY27 Q2 actuals: revenue **$96.221B**, Data Center **$89.0B**, GAAP gross margin **75.0%**, operating income **$63.734B**;
- supply-related commitments of **$119.0B** at FY27 Q1;
- first-party evidence that HBM3E requires roughly **3× the wafer supply of DDR5** at the same node and bit capacity;
- repeated first-party statements that advanced packaging remains tight.

The old token matrix and fixed breakeven-P&L values are not publication facts. They are sensitivity tests that require a real price series, utilization data, and an AI-specific revenue denominator before being upgraded.
## 3. Mechanism: accounting pressure, utilization, clearing, and commitments

### 3.1 A bubble requires four classes of clearing signals

This report does **not** define a bubble as "CapEx is large." Large infrastructure investment can be rational if real demand and utilization rise with it. A risk state has to be read through at least four signal classes:

1. **Accounting:** depreciation and infrastructure operating cost keep rising.
2. **Utilization / revenue:** incremental AI revenue, calls, or machine-hour utilization fail to cover the rising cost base.
3. **Market clearing:** GPU/rack spot discounts appear, lead times shorten materially, or HBM/CoWoS move from quota allocation toward readily available supply.
4. **Forward commitments:** cloud CapEx guidance is cut, or semiconductor supply commitments / prepayments stop growing, are rescheduled, or are cancelled.

Accounting pressure alone is **capital intensification**, not a burst. Accounting + weak utilization is **ROI pressure**. When all four groups line up, the system begins to resemble **infrastructure destocking / a hard landing**.

A stock-price drawdown can come from rates, positioning, or narrative and therefore is not sufficient evidence. The four-year straight-line model is itself only a template: useful lives for servers, accelerators, networking, and buildings differ by company. The mechanism is that sunk CapEx creates expense over later years; order cuts are visible in the **next** round of orders and commitments, not in PPE that is already booked.

Mixed-year 2025 is already about $354.0B–$356.5B. Reusing the 2024 "$215B" base to project 2026–2028 understates the capital base, while mechanically summing the latest non-comparable guidance and dividing by four creates false precision. The direction can be stated: the depreciation wall is thickening. Thickening is not itself a burst.

### 3.2 seller-side value capture sits with the seller, depreciation with the buyer. The two books do not match

seller-side value capture with the seller, depreciation with the buyer, accounts that do not line up: [Volume 1](vol-01.md), [Volume 8](vol-08.md). The moment profit is recognized at the seller is earlier than the moment the buyer sells machine-hours into software cash. So "buyer depreciation pressure" and "seller fat profit" can hold at once. If a hard landing develops, buyer utilization and second-tier model-company economics are likely to weaken before previously recognized seller revenue is reversed. If destocking happens, it happens inside this bidding structure, not in an industry where "everyone is slightly profitable together."

### 3.3 How to read the token matrix, and how to misread it

historical stress-test material matrix's x-axis is usage, y-axis is unit price. The most dangerous cell is not "usage doubles but price halves and you still eke a profit." It is "usage up only 50%, price down 50%" — that cell historical stress-test material wrote directly as destocking. The +300% / down 50% still-earn-$15B cell assumes usage compounding at a three-year double-or-better pace. Without that usage, a price cut is destocking. DeepSeek makes a unit-price fall more likely. It does not automatically make usage +300%.

Open source and DeepSeek-class efficiency have already opened the token-price axis, but that does not mechanically determine the usage axis. Application risk should therefore be read through **AI Software Unit Economics**, not a fixed "SaaS margin 85%→55%" claim. Revenue must cover inference, retrieval/storage, tool/API calls, human review, AI-specific cloud cost, and the relevant depreciation. Falling unit cost can expand demand; falling price without enough usage growth can still destroy ROI. The old matrix remains a stress test, not an industry P&L forecast.

P&L figures in the matrix — $45 / $80 / $20 / $90B and the rest — are scenario arithmetic, not an first-party result. This volume does not invent a "more precise" P&L table to replace it. Replacement would need a real token-price time series and an enterprise AI incremental-revenue split. Neither exists on the public record.

### 3.4 Where destocking inventory sits. Four layers, four speeds

The three characters "destock" make people look only at the Nvidia channel. Real inventory sits on four layers, impairing at different speeds.

The first layer is GPUs and cabinets not yet racked, the easiest place for spot versus contract concessions. Lead times from tens of weeks back to week-scale delivery, softer prepayment terms, and a bid-able second-hand cabinet — those three are closer to a definition of destocking than "a cloud still says we like AI." historical stress-test material had no such high-frequency data. This volume lists them as watch items.

The second layer is HBM and CoWoS work-in-process, physically the hardest inventory to turn. Micron provides **first-party evidence** that, at the same node and bit capacity, HBM3E requires about **3× the wafer supply** of DDR5. Tight advanced packaging and the HBM wafer penalty therefore make this layer sticky. One quarter of order cuts does not instantly turn an HBM/advanced-packaging line back into unconstrained consumer supply.

The third layer is four-year servers already installed and already depreciating. The only levers are lower utilization or resale. Resale punches new-goods prices directly. This layer can be impaired on the books. The physical cabinets still sit in halls using power.

The fourth layer is fifteen-year buildings and longer power contracts, almost impossible to destock, only becoming idle megawatts. Power contracts are too long to cut. So a "bubble burst" is not every asset going to zero together. Hardware impairs first; power assets stay on the books as long liabilities. That bites Volume 35's nuclear PPAs: signed megawatts and poured liquid-cooled campuses do not vanish because one training run fell to $5.576 million.

Transmission of cuts: the first knife is the longest-lead, most-prepaid high-end training cabinet; the second is added HBM and CoWoS capacity; the third only then reaches already-interconnected buildings. A hard landing does not look like "AI disappeared." It looks like: new-goods prices drop first, lines idle next, plants and campuses stay on the books. Overweighting fourth-layer physical scarcity hurts most in a destocking scenario and is hardest in a mis-kill-then-reconcentrate scenario — the same asset class changes sign with the endgame branch.

### 3.5 Physical stickiness: power and packaging make capacity irreversible

The calculation pool: [Volume 16](vol-16.md) and [Volume 24](vol-24.md). Residual: [Volume 5](vol-05.md). Cloud ASICs: [Volume 4](vol-04.md). A 120 kW cabinet, the wafer penalty of HBM versus DDR5, advanced packaging lifted from single-digit revenue share to a bit over 10% — none of this is capacity that returns to the old state when an order is cancelled. Books can impair. Lines cannot turn instantly. Destocking therefore has physical stickiness. ASICs shunting inference do not automatically turn second-layer inventory into a consumer line that can be turned.

### 3.6 Antitrust does not change depreciation. A fine is a cost

The case file: [Volume 11](vol-11.md). This volume does not reopen it. A fine is a cost. National-security documents exist. "Therefore they will not break it up" does not. Bubble clearing can still happen. The trigger is depreciation not matching usage, not a courtroom. Dual stacks: [Volume 12](vol-12.md). Supply is built as two safety stocks. Demand does not double.

## 4. Scenarios, counterarguments, and testable markers

P&L in the matrix is a historical stress-test scenario, unverified, not an first-party fact. The scenarios below do not introduce a second probability system; they map observable clearing mechanisms onto the standard S1–S4 framework.

### 4.1 Soft landing / S2-like normalization

Usage runs +150%–+300%, token prices fall less than 30%, clouds trim the next round of spending but do not collapse. Nvidia margin gives some back from 75.0% and is still well above TSMC 2025's 59.9%. The industry enters historical stress-test material's Agents mature period. Supply commitments no longer stack at $23.8B every three months, but the $119.0B already locked is paid on schedule. Check: D&A in the annual report rises but free cash does not turn negative; four-cloud group capex decelerates from the mixed-year 2025 order of about $354.0B rather than halving; public-cloud token prices step down, but enterprise annual reports start disclosing AI incremental revenue separately. Unverified: do not forecast which year revenue covers depreciation.

### 4.2 Destocking / S4 hard landing

Usage stops near +50%, open source drives unit price down 50%. The matrix judges overhang. GPU spot versus contract concessions, HBM lead times shorten, CoWoS shows empty slots. TSMC HPC share rolls over from a high, Hynix HBM revenue share gives back from historical stress-test material's 40%. That is the back half of a classic capex cycle, not "AI is useless." First-layer inventory reprices first, second-layer lines idle, third-layer installed cabinets lose utilization, fourth-layer power contracts stay on the books. NVIDIA data-center revenue leaving the FY26 $193.7B order, gross margin leaving the 71.1% to 75.0% band — those two sentences are controls, not forecasts. Official text already wrote that some supply agreements can be rescheduled. Reschedulable is not already rescheduled. This volume does not invent reschedule amounts.

### 4.3 Clearing followed by reconcentration

A hard landing clears second-tier model companies and second-tier cloud regions. Quota and nuclear contracts stay with a few giants. The 2036 oligopoly scenario is strengthened by the bubble. The opposing path is an algorithm break: intelligence becomes cheap enough, infrastructure decays into a thin-margin utility, bubble residue becomes a regulated asset. historical stress-test material gave probabilities. This volume does not reuse them and does not open new percentages. The mechanism that can be written: after clearing, scarce-slice slots concentrate further, they do not disperse. A 19% historical customer revenue share is not a forward allocation guarantee; the relevant variable is the leading buyer's share of incremental advanced capacity after clearing. If destocking only clears the second tier, the leading buyer's increment share gets larger.

### 4.4 Testable markers (direction only)

- Combined four-cloud capex versus mixed-year 2024 about $211.9–213.9B and mixed-year 2025 about $354.0–356.5B: still adding, or decelerating sequentially. The 2026 three-name official-guidance midpoint about $490–520B (missing Microsoft) is already above mixed-year 2025, but it is guidance, not actual.
- Whether public-cloud token prices show a 30% or 50% annualized step. There is no official all-market index. Watch each firm's price page. Do not add them into an "industry unit price."
- Whether enterprise annual reports start disclosing AI incremental revenue separately, and whether disclosed AI revenue and utilization improve enough to cover rising infrastructure cost. The older $155B breakeven figure remains a stress-test value.
- Whether Nvidia data-center revenue can still accelerate from FY26 $193.7B; whether gross margin stays in the 71.1%–75.0% band.
- Whether supply commitments keep adding from $119.0B, or rescheduling appears.
- Whether HBM lead times and CoWoS quotes are premia or concessions; whether a bid-able market for second-hand training clusters appears.
- Whether justice.gov shows a *United States v. NVIDIA* complaint; whether France issues a statement of objections; whether the EU shows a 101/102 opening. Investigation without a complaint is the 2026-08-26 state, not an eternal state.
- Next TSMC customer split: whether the first customer leaves 19%. Jensen has said they are already the largest customer. The 20-F does not name names.

### 4.5 Opposition

Calling a stock-price drawdown a bubble burst ignores that depreciation has not yet entered peak years, and ignores that the mixed-year 2025 base is no longer $215B. Treating one DeepSeek training cost as the industry forever needing only $5.576 million ignores the report's own "excludes prior ablations," and ignores that inference scale can still eat a whole cabinet of power. Writing 2026 $670–750B as capex that has already happened. Adding four-cloud capex into "$215B of AI hardware." Writing FY26 data center $193.7B as a four-cloud line item paid to NVIDIA. Writing 10% of annual revenue as a fine about to be issued. Writing a subpoena as a breakup order. Reading a national-security memorandum as "therefore they have already decided not to break it up." Reading "regulators are looking" as "the depreciation wall will be taken down."

### 4.6 How to read the three books at once. Do not knock them into one tax rate

The three things in this volume's title — four-year depreciation, token unit price, destocking — are not three parallel news items. They are one cash-flow projected at three dates. The year capex goes in, the seller recognizes revenue and margin; for four years after, the buyer takes depreciation on schedule; token unit price decides how much cash each machine-hour recovers in those four years. Destocking is a channel phenomenon visible only in year three or four, but it is jointly decided by year-one bids and year-two usage. Compressing the three dates into "already a bubble now" or "not a bubble yet" misreads both.

The first book is buyer PPE. Scope: [Volume 8](vol-08.md). What can be written: the base is rising. Wall thickness depends on hardware share and useful life, which firms do not disclose to a reproducible add. "$45–55B of hardware depreciation a year" can only be a template.

The second book is seller seller-side value capture. See [Volume 1](vol-01.md). This book recognizes early and takes cash fast. It does not answer whether buyer machine-hours were sold. If destocking happens only in the second tier, this book can keep adding.

The third book is token unit price and usage. There is no all-market index on the public record. historical stress-test material matrix gives nine cells. This volume keeps it as a scenario and does not invent another. The only reading that can be written: the y-axis has been opened by open source; the x-axis still depends on whether the workflow produces cash. DeepSeek-V3's $5.576 million is a seller-side value capture conversion of one official training run, not a clearing price for the inference market. After inference turns tokens into cost of goods, application-layer margin pressure and cloud depreciation pressure meet on the same operating statement. Before they meet, the seller can keep collecting seller-side value capture, the buyer can keep adding PPE, and stocks can keep arguing "is it a bubble." After they meet, one can talk about which layer the first destocking knife hits.

The three books not matching is not a data error. The accounts were never one-to-one. [Volume 11](vol-11.md) forbids knocking mixed-year capex against data-center revenue. This volume obeys. What is forbidden is a tax rate, not the mechanism. The mechanism is still: the application layer grinds at the front, profit is siphoned at the rear. What grinds is token unit price and seat pricing. What is siphoned is cabinet invoices. Phones and PCs that do not buy GPUs still pay an overflow tax on memory residual. That tax does not enter this volume's matrix, but it makes the shortcut "destocking equals a consumer-electronics thaw" harder — makers have already retuned lines for HBM. Consumer bits are not another river.

Antitrust sits outside these three books. An investigation can eventually change software/interface or tying rules if it produces a formal remedy. It does not yet change PPE already booked, or cabinets already shipped. A fine is the seller's cost, depreciation the buyer's expense, tokens the application's cost of goods. The debit sides of the three tables are not the same legal person. So "wait for a fine to clear the bubble" does not hold in accounting. What waiting can get, at most, is a little give on interfaces, and ASICs able to attach to part of the network. Fat profit and prepayments are not touched. Four-year depreciation is still taken.

Power is a fourth book. This volume does not open installed megawatts. It only leaves the interface. Signed megawatts and poured campuses belong to fourth-layer inventory. Tokens can get cheaper. Power contracts will not reschedule on token pricing. If Agents fill machine-hours, power is the bottleneck. If Agents do not fill them, power is idle liability. Both readings hold. They depend on the x-axis, not on the next financing narrative.

Micro signals of an order cut often precede the filing. Lead time, prepayment terms, second-hand cabinet quotes: three thermometers for first-layer inventory. All three softening at once, and the matrix cell +50% / down 50% is no longer hypothetical. Conversely, as long as CoWoS and HBM are still allocated by quota, the main bubble narrative has not entered a clearing segment. Quota still there means the leading buyer is still using profit to lock slots. Slots still there means second-layer inventory has not idled enough to have to revert to a consumer line. This volume does not read "a cloud publicly says capex will still rise" as a disproof — guidance can rise while lead times shorten. Both at once only says seller and buyer narratives are not yet aligned. It does not say destocking has started or ended.

Prepayments can be rescheduled: a sentence the 10-K itself wrote, not already rescheduled. Reschedulable commitments create contract elasticity between physical capacity reservation and later market clearing. When that elasticity is used, the channel has not yet repriced and the line has already skipped the next wafer. That is an earlier internal signal than a spot concession, but outsiders cannot read a split. So the testable item can only be "whether the supply-commitment total keeps adding or rescheduling appears," not "how much was rescheduled to TSMC, how much to Hynix." No split, do not invent.

The China stack cannot catch Western destocking. The wrong layer was already written above. Here only one allocation implication: if Western first-layer inventory reprices, it does not automatically become cheap training cabinets for Huawei or domestic clouds. Export controls block the return channel. Cabinets that reprice and cannot leave the country resell inside the West, hitting Western new-goods prices, not an Eastern supply gap. The East wants domestic bits and packaging that can pass an administrative lock, not a Blackwell cabinet stopped by a license. Writing "global destocking" as "domestic compute copium" is the wrong layer again.

## 5. Gaps and what must not be treated as fact

historical stress-test material gave no cloud AI-segment split, no real token-price time series, no days of inventory, no supplier-channel inventory. P&L in the matrix — $45 / $80 / $20 / $90B and the rest — is scenario arithmetic, not an first-party result. $0.08/kWh, PUE=1.2, hardware 65% of capex, annualized depreciation $115.5B, breakeven incremental revenue $155B, 2026 four-cloud $670–750B: all historical stress-test assumptions or compilations and remain outside the current fact layer. 20%–30% chip-cost inflation, SaaS margin 85%→55%, MLA KV compression 93.3%, CoWoS monthly capacity 13k→130k and 60% lock: not a TSMC or NVIDIA line item. Do not promote them.

This volume did not audit full 10-Ks page by page. SEC HTML fetches from this machine were refused. Figures follow official earnings releases / Exhibit 99.1 / sentences already checked in the judgment. If a 10-K restates, the 10-K wins. Specific destocking quarters, price-drop sizes, and clearing lists cannot be derived from historical stress-test material or [Volume 11](vol-11.md). This volume does not invent them.

Not yet happened, cannot be written as already happened: a DOJ complaint, a settlement, a Mellanox split, a forced opening of CUDA; a French statement of objections, a French or EU fine; "a 10% of annual revenue fine about to be issued"; a White House / Pentagon text already forbidding a breakup; four-cloud "AI hardware capex $215B"; 2026 four-cloud already spending $670–750B; token unit price already down 50% annualized; a bid-able second-hand cabinet market already there.

What can be written: the depreciation-wall mechanism is there; template numbers are not an audit; the token matrix is a scenario. Whether a bubble is already clearing: the public record still has no official sample of lead time, prepayments, and second-hand cabinets appearing together. No sample, do not write summer 2026 as a clearing segment.
