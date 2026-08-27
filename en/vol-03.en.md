# Volume 03: AI Resource Gravity and Non-AI Residual Capacity

Chinese original: [vol-03.md](vol-03.md)

The residual model is in [Volume 5](vol-05.md). First-wave whole systems are in [Volume 9](vol-09.md). The consumer-electronics tax is in [Volume 22](vol-22.md). This volume does not reopen 51% or analyst SoC prices. This volume only writes demand as the identity cabinets × BOM. It does not write that a global percentage has already been bought away.

## 1. Core question

Can total semiconductor and memory supply expand while consumer and general-purpose computing still receive less effective supply than they otherwise would?

This volume formalizes **AI Resource Gravity** and **Non-AI Residual Capacity**. The key distinction is:

```text
NonAI_Residual
= Effective_Supply
- AI_Absorption
- Other_Priority_Demand
```

The mechanism is not “AI drains everything.” It is that high-value, high-certainty AI/server demand can absorb a disproportionate share of the increment, leaving smartphones, PCs, gaming, and general-purpose servers with a smaller residual pool.
## 2. Official and institutional sources

### 2.1 Official cabinet materials, not a dollar table

Source: https://www.nvidia.com/en-us/data-center/gb200-nvl72/

Product-page body: The NVIDIA GB200 NVL72 connects 36 Grace CPUs and 72 Blackwell GPUs in a rack-scale, liquid-cooled design. Spec table: Configuration 36 Grace, 72 Blackwell; GPU memory 13.4 TB HBM3E; CPU memory 17 TB LPDDR5X. This is the official bill of materials. historical stress-test material's 13.8 TB does not match the official site. Use the official site.

They already made cards. What changed is selling training as a cabinet. Once the cabinet is the default sales unit, customers do not compare single-card FLOPs. They compare whether they can enter a 72-card high-speed domain. Once inside, the next generation is bought inside the same domain. This volume does not split the cabinet into a dollar table. A dollar table is a historical stress-test extrapolation, not a product page. What can enter the identity is only unit counts and terabytes.

The reticle limit welds this cabinet onto packaging. H100 GPU die 814 mm², NVIDIA's own technical blog: The full GH100 GPU that powers the H100 GPU is fabricated using the TSMC 4N process customized for NVIDIA, with 80 billion transistors, a die size of 814 mm2. Source: https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/ B200 is two dice, each about 800 mm², package total about 1,600 mm². 800 and 1,600 are confirm in Electronic Design and IEEE Spectrum, not the product page and not a 10-K. Electronic Design original: The B200 consists of a pair of silicon die manufactured at the reticle limit ... currently around 800 mm2. IEEE Spectrum original: The newly announced Blackwell GPUs are two 800-square-millimeter silicon dies joined along one edge. A single die cannot hold it. It must walk CoWoS, laying multiple dice and HBM on an interposer. Packaging becomes the delivery constraint before transistors.

### 2.2 Multiply by cabinet: the identity stops per cabinet. It is not written as already having bought a global percentage

Identity: demand equals cabinets shipped times materials per cabinet. NVIDIA does not report cabinet counts. Makers do not report full-year absolute bits. The arithmetic stops at per cabinet, per thousand cabinets, and scenario cabinet counts. It is not written as already having bought a global percentage.

Units must be normalized first. 1 PB equals 1,000 TB. 1 EB equals 1,000 PB. Per thousand cabinets (scenario, not shipments): HBM 13.4 PB, LPDDR 17 PB. 10,000 cabinets: HBM 134 PB, LPDDR 170 PB. 30,000 cabinets: 402 PB and 510 PB. 50,000 cabinets: 670 PB and 850 PB. An earlier external calculation mislabeled 134 PB as 134 EB, a 1,000× unit error. This volume uses the corrected PB-scale arithmetic.

FY26 data center $193,737M cannot be multiplied as a full year of 72-card cabinets. Blackwell is ramping. The main line is explicit: only Q1 FY27 writes a Blackwell 300 pull. Hypothesis from here: once shipments walk as cabinets, demand multiplies by cabinet; supply cannot keep up with the product. Dividing full-year data-center revenue by a self-made cabinet ASP and treating the quotient as annual shipments is another wrong sum. This volume does not do it.

The same identity on packaging has to change pools. 5.39 is a packaging-wafers-per-cabinet estimate: 72 GPU packages divided by about 13.4 packages per wafer. 72 is official. About 13.4 is a geometry working hypothesis: two dice totaling about 1,600 mm², plus eight HBM stacks, an interposer far larger than a single GPU. A 300 mm wafer area is π times 150 squared, 70,686 mm². There is no official TSMC "how many B200 packages per packaging wafer." 5.39 is an estimate. It is not fiction. It is also not logic wafers per cabinet for the whole factory.

Front-end logic is another line. GPU dice per cabinet: 72 times 2 equals 144. About 2.9 wafers per cabinet at 70% yield. That does not match 5.39. Mixing them is the wrong pool. 835,000 cabinets equals 4.5 million wafers divided by 5.39. 4.5 million is 30% of TSMC's 2025 shipments of 15 million. 5.39 is packaging wafers per cabinet. Most of the 15 million are phones, MCUs, auto, and mature nodes. Dividing the whole factory, or 30% of it, by 5.39 yields a cabinet count with no physical meaning. The binding line is packaging. Sell-side puts NVIDIA at about 60%, 595k to 630k wafers (Morgan Stanley paraphrase / Mizuho at another date). TSMC has no split. At 5.39, about 100k cabinets take more than half of this packaging line. You do not need 800,000 cabinets to lock 3nm. About 100k cabinets is a sell-side pool times an estimate coefficient. The direction matches the main line. The coefficient is not an annual report.

### 2.3 Who can bid, increment, packaging, memory past half, gaming cards giving way

Profit is in [Volume 1](vol-01.md). TSMC increment and packaging are in [Volume 4](vol-04.md) and [Volume 24](vol-24.md). 51% is in [Volume 5](vol-05.md). Gaming cards giving way is in [Volume 1](vol-01.md). This volume does not reopen them. This volume only writes demand as cabinets × BOM. It does not write that a global percentage has already been bought away.

## 3. Push the mechanism forward

### 3.1 Who is the first wave. Not auto

The first-wave pressure falls on products that compete with AI systems for overlapping logic, memory, packaging, or component capacity. The list has four items: leading-edge logic wafers, CoWoS, HBM, and server RDIMMs. PCs want leading-edge logic and discrete GPUs. Commercial PCs want general server DIMMs. General-purpose servers want RDIMMs. Phones want leading-edge logic and LPDDR. All four stand downstream of the same river. Cabinets multiply by cabinet, first pulling HBM and RDIMMs, then packaging and first-to-market nodes. Downstream sees price, not a notice that says "already requisitioned."

HDDs are not in this cabinet. They sit beside cloud storage and are equally sucked by hall budgets. This volume does not report unverified drive shipments. The direction is: hall budgets keep training cabinets first, then object storage; consumer drives are residual farther out.

Auto is not the first wave. TSMC's automotive platform in 2025 is still 5%, up 34% year on year. Auto electronics have their own qualification cycle and process node. They are not the same week's slot conflict as a 72-card cabinet. If intelligent driving walks centralized compute, it joins the bid. What it joins is the HPC slice, not another foundry. Writing auto as already stopped is writing next wave's scenario as this quarter's fact. This volume does not write a count of plants stopped.

The world does not blow up. Upgrades stop one node down. Phones can still ship. The AP and memory are just more expensive, and replacement is slower. PCs can still ship. Discrete GPUs and DIMMs just become residual. General-purpose servers can still ship. DDR5 is already inside the 51%. It is not another cheap river. One firm writes the rules. What it specifies is mix and slots, not which phone maker closes.

### 3.2 Why multiply-by-cabinet is more honest than "already bought a global percentage"

NVIDIA does not report cabinet counts. Makers do not report full-year absolute bits. TSMC does not split packaging customers. Three blanks stacked together mean any "already bought a global percentage" is filling a blank as fact. The identity does not fill blanks. It only says: once shipments walk as cabinets, each cabinet fixedly pulls 13.4 TB of HBM and 17 TB of LPDDR; on packaging, about 5.39 wafers per cabinet. If supply cannot keep up with the product, residual is even smaller. That is a mechanism, not a completed census.

A unit error writes the mechanism as a myth. 10,000 cabinets of HBM is 134 PB, not 134 EB. A number a thousand times too large forces the reader to believe "global memory has already been drained." This volume confirm the unit so a myth does not replace the identity.

Scenario cabinet counts are not shipments. 10,000 / 30,000 / 50,000 are rulers for order of magnitude. How to use the ruler: if shipments walk to this tranche, how many PB of HBM and LPDDR each; if the packaging pool is counted as sell-side 1 million wafers, half is about 100k cabinets. The ruler cannot be used backwards: you cannot announce that 10,000 cabinets have already happened because 134 PB multiplied out.

FY26 data center $193,737M is the rent the world paid, not a cabinet count. The main line writes: that $193.7B is the rent the world paid. This volume treats that money as the result side of the resource reallocation, not the left side of the product. The left side can only be cabinet counts. Cabinet counts are empty, so the product stops per cabinet.

### 3.3 Makers, packaging, power, the other side

Makers turning to high price: [Volume 5](vol-05.md). The packaging gate: [Volume 24](vol-24.md). Power is not this quarter's cut-supply: [Volume 13](vol-13.md). Three other-side points: [Volume 8](vol-08.md). This volume does not reopen them. The first wave is not auto: see 3.1 above. Why multiply-by-cabinet is honest: see 3.2 above.

### 3.7 Checks that can be tested, not adjectives

This volume does not claim that resource reallocation is already complete across every semiconductor category. What can be checked in the next official write-up is the following.

TSMC platforms: whether smartphone share keeps falling or stops; whether HPC share stays at 58% or walks the full year in the direction of 2Q26's 66%. Whether auto is still near 5%. Whether packaging-and-test revenue stays a bit over 10% or walks to the low-teens outlook. Whether C.C. Wei still says tight, cannot meet, limits customer growth. If those sentences change, the foundry side of the resource reallocation has to be rewritten.

Customer A / B: whether A is still walking up from 12%, whether B is still walking down from 22%. If booked 19% returns to the old structure of a phone customer at forty-plus points, the identity-swap story has to be rewritten. This volume does not write the mapping as a name. It only treats the share direction as a check.

Supply commitments: after $95.2B to $119.0B, does the next quarter keep adding or go flat. Whether gross margin is still near 75%. Whether operating income is still on the order of $53B a quarter. Those three lines are bidding power. While bidding power holds, slots are not given back to the second name for no reason.

TrendForce bit supply: whether 51% stays high or falls back below half. Memory at 47% to 68% of cloud capex is an institutional estimate. If the next write-up revises it down hard, the residual narrative has to follow. Channel prices are not an annual report, but if the direction moves from following the rise to collapsing, look back at whether makers cut back to commodity.

Gaming cards: whether the official reason sentence is still limited supply. If it changes to weak demand, the giving-way story has to be downgraded. If it keeps writing limited supply, consumer-end giving way is still on.

Cabinet counts, full-year global absolute HBM bits, an official number for packages per packaging wafer: if they are not found, do not invent them. A check that cannot be found cannot be replaced by an adjective.

## 4. What this volume cannot write as fact

Cabinet counts, full-year global absolute HBM bits, an official number for B200 packages per packaging wafer: not found.

A 3:1 wafer penalty as a measured factory constant: Micron says the same bits take more wafers; Micron's first-party materials disclose ~3×. That is not a maker formula. historical stress-test material's 12-high composite yield 48.6% and area up 50% to 55% are examples. Do not promote them.

Qualcomm 8 Elite purchase price $180–$190, MediaTek about $155, AP at 30% of BOM, a 40-month replacement cycle: analyst. This volume does not reopen them. The earlier $20,000–$22,000 3 nm wafer-price estimate is not supported by the TSMC management material used here and therefore does not enter the fact layer.

Huaqiangbei 450 to 1,800: channel talk.

A percentage of consumer-electronics margin extracted, procurement cost up 20% to 30%, a count of auto plants stopped: historical stress-test extrapolations, no sample.

Writing 10,000 / 30,000 / 50,000 cabinets as shipments that already happened. Writing 835,000 cabinets as locking 3nm. 5.39 cannot divide TSMC's full-year 15 million wafers.

C.C. Wei at the shareholders' meeting, "sold out through 2026": the Focus Taiwan shareholders' meeting copy we opened does not have that sentence. What official text can confirm is tight, cannot meet, already limits customer growth.

Converting 19%, 58%, and 24% into tens of thousands of wafers. Revenue share is not unit share.

CoWoS monthly capacity 13k to 130k, NVIDIA exclusive 60%: not a TSMC split. Sell-side stays sell-side. Do not mix the Morgan Stanley paraphrase and Mizuho at another date into an official table.

Samsung Taylor 16k / 24k / 40k wafers per month: not in the announcement. CXMT 350k wafers per month: not in the announcement.

Counting equity marks as money that bids for capacity. Q1 net income $58.321B includes about $15.9B of unrealized equity gains. Bidding looks at operating income.

historical stress-test material "four-cloud 2024 capex officially broke $215B of AI" cannot be treated as fact. What can be added is mixed-year group-wide equipment purchases of about $211.9B to $213.9B, not an AI-hardware line item. This volume does not treat that money as cabinets the resource reallocation has already bought.

Backdoors, stolen training data: no public forensics. They do not enter the fact layer.

"Intelligence rent" is a metaphor, not an accounting line. Flows this volume can point to: data-center invoices, supply commitments, and institutional bit supply past half. None of the three is an accounting line named rent.

2nm first-silicon prepayment dollars, a High-NA bulk buyout, TSMC already a captive fab: no official sentence was found. Leave them empty.
