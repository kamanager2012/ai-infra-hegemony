# Volume 17: Ultimate AI-Infrastructure Risks — Physical, Capital, Substitution, and Institutional Constraints

Chinese original: [vol-17.md](vol-17.md)

The power interrupt is [Volume 13](vol-13.md). Residual and 3:1 are [Volume 5](vol-05.md) and [Volume 23](vol-23.md). The depreciation wall is [Volume 30](vol-30.md). This volume does not reopen nuclear contracts or 2600GW. The title's safety challenge has almost no standalone paragraph in the forty volumes. This volume does not invent one.

## 1. Core question

Which mechanisms could materially interrupt the AI-infrastructure expansion cycle between 2026 and 2036?

The report separates four classes of interruption:
1. **physical constraints** — advanced logic, HBM, packaging, interconnect, power, and cooling;
2. **capital constraints** — utilization and workflow cash flow fail to cover depreciation and long-duration infrastructure commitments;
3. **substitution constraints** — alternative system stacks, algorithmic efficiency, or architecture changes reduce dependence on the current scarce stack;
4. **institutional constraints** — regulation, export controls, licensing, safety, or permitting change the rules or the deployable resource pool.

These risks can reinforce one another, but none should be treated as an already-completed end state.
## 2. Evidence boundary

Historical versions used a three-wall narrative plus fixed CapEx, power, token-price, and probability values. The current report keeps the mechanisms but does not treat those old point estimates as facts.

Current hard anchors include:
- Micron's first-party **~3× HBM3E wafer-supply trade ratio versus DDR5** at the same node and bit capacity;
- repeated first-party advanced-packaging tightness statements from TSMC;
- ~**120 kW** rack-scale power density for GB200/GB300-class NVL72 systems;
- actual hyperscaler power contracts and their separate contracted / permitted / energized / utilized states;
- NVIDIA FY27 Q2 actuals and current supply commitments;
- S1–S4 rather than fixed point probabilities.

The title's “safety” dimension is treated as an institutional/deployment constraint only where public evidence exists; the report does not invent an independent safety-risk dataset.
## 3. Mechanism: bottlenecks migrate and can serialize

Physical limits begin with reticle-scale logic, memory bandwidth, advanced packaging, and power; exact reticle-area values require source-specific treatment. More bandwidth then walks CoWoS, HBM, and NVLink, not a density miracle at the next node. Micron FY24 Q3 prepared remarks disclose that, industry-wide, HBM3E requires approximately **3× the wafer supply of DDR5** to produce a given number of bits in the same technology node; Micron's FY25 10-K later confirms that HBM requires more wafers and cleanroom space for the same bits. The ~3× ratio is A-grade first-party evidence, while still not being a universal fab-control constant. If advanced logic and HBM-class memory tighten simultaneously, consumer products can face both wafer-level and bit-level residual pressure.

The power wall is [Volume 13](vol-13.md). What is exhausted is not the planet's generation. It is dispatchable, interconnectable, coolable power density. If cabinets cannot be installed, HBM orders do not cancel themselves.

The ledger wall is [Volume 30](vol-30.md). The trigger of a bubble washout is depreciation, not the share price. TrendForce writes that at the major CSPs it tracks, DRAM and NAND combined will be 47% of 2026 total CapEx and rise further to 68% in 2027. That is an institutional estimate, not a memory-purchase line in a four-cloud 10-K.

The memory-structure wall is [Volume 5](vol-05.md). 51% is bit supply. If clouds shift inference onto DDR5, they grab residual already inside that half. It is a tax, not a new river.

Maker books are [Volume 5](vol-05.md). What is rising is the cabinet, not phones and PCs. A risk story written as "memory makers will break first, so the cycle ends" runs against those three statements. The China stack is [Volume 12](vol-12.md). China's parallel stack can alter regional sourcing and substitution, but it does not automatically remove global constraints in advanced logic, HBM, packaging, interconnect, or power.

## 4. Scenarios, counterarguments, and testable indicators

Four risk states can coexist or reinforce one another; no separate probability system is introduced here:

- **Wall first:** interconnection and 120 kW cooling stall cabinets that can actually enter production. Book Capex is still rising, but GPU utilization and energization rates fall. The picture is "orders exist, power does not, thermal budget does not." HBM longs on the memory side need not cancel in step. The residual-capacity pressure continues.
- **Ledger first:** enterprise Agent workflows cannot recover $45B–$55B of annual depreciation (historical stress-test values). Stack the institutional path of memory toward 68% of CSP CapEx, and clouds cut hardware in 2026–2027 guidance. The picture is Nvidia data-center growth rolling over and CoWoS utilization easing off full load.
- **Residual first:** HBM+RDIMM is already 51% of 2026 DRAM bits. If clouds shift inference onto DDR5, they only fight phones and PCs for the slice already rising. Huaqiangbei channel talk of 16G DDR5 from about 450 yuan to 1800 yuan (CCTV Finance / Cailian Press 2026-07-07, https://m.cls.cn/detail/2418583 ) is a side proof that the residual dies first, not a maker ASP. The picture is consumer-electronics shipments collapsing first while training cabinets still run.
- **Wall and ledger hedge:** MLA / MoE compress KV Cache by 93.3%, and DeepSeek-V3 trains 671B on 2.788 million GPU-hours / about $5.576M (historical stress-test values, paraphrased from its technical report), which raises "effective Tokens per dollar," delays washout, but does not cancel the 4-year depreciation clock and does not automatically return 51% of bits to phones.

Counterargument: if advertising and cloud revenue continue to cover infrastructure depreciation (Meta 2024 gross margin 81.5%, Alphabet 57.6%, historical stress-test values), the "bubble" can go years without breaking. Value capture can migrate from software seats toward infrastructure and workflow layers without an immediate collapse. If the DeepSeek path spreads, risk flips from "not enough compute" to "too much compute" — in the Part II chapter-7 matrix, washout happens only when call volume cannot keep up with unit-price falls. Another other side: TrendForce's 47% / 68% is a scenario estimate. Some LTAs from 2Q26 carry price ceilings. HBM 2027 contract prices may still be +70–140%. A ceiling and a price-up can exist together. The report does not treat 68% as a four-cloud purchase budget already signed.

Testable marks (observe only; do not invent thresholds): the direction of the four clouds' next-year Capex guides relative to $215B; whether Nvidia data-center revenue still follows the FY24→FY25 slope of $47.525B→$115B+; whether TSMC HPC keeps pressing past smartphones and whether 3nm revenue share is still above 18%; whether Hynix still discloses a large year-on-year HBM-revenue rise and whether operating margin is still near 49%; whether TrendForce still writes HBM+RDIMM as more than half of DRAM bits and whether memory as a share of CSP CapEx still walks 47%→68%; whether PJM / ERCOT queue capacity is still on the order of 2,600 GW; actual energization of Three Mile Island 835 MW, Susquehanna 960 MW, and Kairos 500 MW, not signing news; whether later CXMT disclosure shows a standalone HBM project (the current prospectus does not).

The four risks are not mutually exclusive. They serialize. () Transistor shrink gets expensive and first concentrates orders on the few buyers who can afford 2nm / CoWoS; those buyers take cabinet power to 120 kW and then queue at the grid and at nuclear doors; while they queue, capital has already depreciated one round of hardware on a four-year clock, and memory then pushes CapEx structure toward the die; if this round has no matching enterprise cash flow, the next buildout order is pulled. A safety event — a liquid-cooling leak that stops a cabinet, a nuclear restart held by regulators, or an export license suddenly tightened — turns one link in that series from "slow" to "cut." historical stress-test material writes the strategic response as firms doing multi-chip scheduling, investors overweighting packaging consumables and liquid-cooling CDUs and interconnection marks, and states putting power infrastructure and leading-edge process on the same footing: those three are hedges, not evidence that the risk is already lifted. Hedging the memory residual needs one more: do not treat "shift inference onto DDR5" as a new river out of HBM. That is residual-capacity pressure, not an independent supply pool.

Accounting-scope conflicts must be resolved before ranking risk. The same "$215B" is written both as the four clouds' actual 2024 combined total and, in the introduction, as support for "annualized $50B+ depreciation" and SaaS gross margin from 85% to 55%. The latter has no sample. It cannot be treated as a software-industry collapse that already happened. 2026 $750B is a forecast on another table. It cannot be turned around to prove 2024 was already a bubble. Four-cloud mixed-year equipment purchases of about $211.9–$213.9B (see the four-cloud scope check) are not "AI hardware $215B." Megawatts on power contracts are contracted capacity, not energized capacity: if 835 MW, 960 MW, and 500 MW slip by node, the 2026–2028 depreciation window still has to be patched from grid stock. historical stress-test material gives no power price or emissions for that stock. This volume does not fill them in.

The Judgment writes the five interrupts as: the West actually bundles; cloud ASICs take training; power stops the buildout; the East stands up a second bid; a structural split or a forced-open CUDA. None of the five is done. What is done: supply commitments added to the hundred-billion-dollar order of magnitude; inquiries exist, complaints do not. A fine is a cost. A split is hard under national security. This volume's risk list is therefore not a prophecy of "which year the bubble breaks." It is the order in which wall, ledger, and residual become visible while those five are absent.

## 5. Gaps and what cannot be treated as fact

1. This volume and the book as a whole do not provide independently verified excerpts of every 10-K original. Microsoft revenue in the table is a range. Capex is written "broke $55B," which is not comparable to Amazon / Alphabet point figures. The old $215B four-cloud figure is not a unified AI-hardware total. The current framework uses company-specific CapEx/PPE scopes and preserves evidence boundaries.
2. 2026 Capex of $670B–$750B, annual depreciation $115.5B, enterprise AI incremental revenue $35B–$50B, the Token sensitivity matrix, and the 2036 four-scenario probabilities are historical stress-test extrapolations rather than first-party facts.
3. "Safety challenges" sit in the title beside physics, power, and capital. The body has no accident rate, no regulatory timetable, no red-team result, and no alignment metric. Do not pass off a nuclear PPA or a liquid-cooling test as a model-safety evaluation.
4. High-NA $380M / tool, a 2nm fab $20B–$25B, the foundry price ladder, and historical stress-test material HBM 4:1–5:1 come from historical stress-test material's paraphrase of the supply chain and white papers. The ~3× ratio is A-grade Micron first-party evidence, but it is not a checked fab process-control chart and must not be extended mechanically to later HBM generations.
5. Microsoft's "over $16B" Three Mile Island offtake appears only in Part II chapter 6. It is not reconciled, dollar-for-megawatt, with Volume 13's 835 MW.
6. TrendForce 47% / 68% / 51% is an institutional press note, not a four-cloud or maker 10-K split. CXMT monthly capacity in the 10k-wafer band is not in the prospectus. The report does not treat it. The report does not treat 8.6 / 13.2 or a three-maker monthly-capacity split.

This volume adds no unsupported filing, capacity, or price figures; new conclusions remain mechanism- or scenario-level unless tied to a cited source.

## 6. The serial order is already written in section 3

Section 3 already ranks the walls as one causal chain: physics narrows the buyer set, power stalls energization, depreciation turns money already spent into a rigid cost, and memory pushes capex structure toward the die. This section does not recopy the Micron original sentence, 51%, 47% to 68%, or nuclear megawatts. Power detail is [Volume 13](vol-13.md). Residual is [Volume 5](vol-05.md). Depreciation is [Volume 30](vol-30.md).

## 7. Maker books, the China stack, four-corner ranking

Maker books are [Volume 5](vol-05.md). The China stack is [Volume 12](vol-12.md). The four corners are the Judgment. The five interrupts are [Volume 8](vol-08.md). Cloud in-house specs are [Volume 4](vol-04.md). This volume does not reopen them. This volume only ranks the walls as one causal chain.

## 10. Safety and institutional risk require observable constraints

The title puts safety beside physics, power, and capital. The forty-volume body has almost no standalone paragraph. What can be written is only the engineering safety that has already appeared: a 120 kW microchannel liquid-cooling zero-leak test is thermal runaway and leakage, not alignment in an alignment paper. A nuclear restart must pass regulators and local politics. Its time constant is longer than an accelerator generation. Model misuse and runaway autonomous agents: historical stress-test material has no mechanism, no case, no metric. Do not pass off a nuclear power-purchase agreement or a liquid-cooling test as a model-safety evaluation. This paragraph keeps its pen down. It does not fill an empty paragraph. Writing safety as the fourth item among ultimate risks is, for now, a title promise, not a mechanism already opened. The honest writing admits the gap, rather than padding it with nuclear news or a liquid-cooling white paper.

## 11. The observation protocol is already written in section 4

Section 4 already writes wall-first, ledger-first, residual-first, and wall-and-ledger hedge as one set of watch items: energization, shipments, depreciation, replacement, bit structure, capex structure. This section does not recopy them. Combining them into one pretend-precise year of the break is a misuse of method.

## 12. Evidence boundary and handoff to later volumes

What can be confirm is the order: physics narrows the buyer set, power stalls energization, depreciation turns money already spent into a rigid cost, memory pushes capex structure toward the die, the China stack cannot fill global cabinets, the four corners decide who is entitled to wash others out rather than be washed out, and the five interrupt conditions are not done. What must be left to later volumes: where the profit pool stops, how consumer electronics pays a spillover tax, how HBM pulls wafers, and whether the advanced-packaging pool can be divided by full-factory shipments. Those volumes have their own authors. This volume does not seize the writing, and it does not promote their conclusions into already-first-party fact.

Also watch: copying the same set of institutional numbers into every volume looks thick and adds no new cause. This volume uses them only to rank risk. Timeline, profit retention, the consumer residual-pressure transmission, silicon consumption, and the packaging pool: each volume answers only that volume's question. On writing discipline, scenario judgments carry no unsupported output, price, margin, or probability. Any sentence that treats a post-2026 number as a fact that already happened must be rewritten as unverified; do not treat as first-party fact. Do not claim to have read an unopened annual report. The report does not treat a monthly capacity that is not in the prospectus. The report does not treat 8.6 and 13.2 from outside notes. The report does not treat a three-maker monthly-capacity split. The report does not treat advanced packaging from a low to a high monthly rate as about 60% locked by one name — TSMC has no split.

The estimate pool is [Volume 16](vol-16.md) and [Volume 24](vol-24.md). This volume only marks "about 100k cabinets take more than half this packaging line" as a risk that can already be observed, not something that waits for the next decade to start. The window is not waiting for a cabinet count divided from the wrong pool.

The world does not blow up. Upgrades stop one node down. One firm writes the rules. If those five are not done, the line walks past half of the scarce slice. This volume only writes ultimate risk as walls that can serialize, not as a year.
