# Volume 23: HBM4, Logic Base Dies, and Memory Capital Intensity

Chinese original: [vol-23.md](vol-23.md)

The residual-capacity model is in [Volume 5](vol-05.md), consumer transmission in [Volume 22](vol-22.md), and China's layered memory constraints in [Volume 12](vol-12.md). This volume focuses on HBM's physical wafer intensity, stacking complexity, logic-base-die integration, and the conditions under which HBM capital intensity changes.

## 1. Core question

Why does HBM absorb more manufacturing resources than conventional DRAM, and how might HBM4 change the capital structure of memory production?

The report uses one current first-party numerical anchor: Micron disclosed that, at the same node and bit capacity, **HBM3E requires roughly 3× the wafer supply of DDR5**, with a higher HBM4 trade ratio expected. That figure is not a finished-product price multiple and not a fixed constant for all future generations.

The forward question is how stacking, bonding, yield, cleanroom requirements, advanced packaging, and logic base dies change resource intensity—not whether a single self-derived yield formula can predict an industry-wide 4:1 or 5:1 ratio.
## 2. Evidence boundary

Historical engineering notes used assumed die-area penalties, stack yields, whole-rack HBM BOMs, and possible 16-Hi HBM4 configurations. These assumptions are not used as current first-party facts.

Current evidence supports:
- the **~3× HBM3E-versus-DDR5 wafer-supply trade ratio** from Micron;
- the direction that HBM requires more wafers and cleanroom space for the same bit output;
- HBM4 commercialization across leading memory vendors;
- increasing integration between memory stacks, advanced packaging, and logic base dies.

Specific 16-Hi yields, 4:1 or 5:1 trade ratios, rack-level HBM dollar cost, and undisclosed base-die foundry allocation remain future engineering questions.
## 3. What can hold ~3× is Micron's first-party disclosure, not historical stress-test material's 48.6% formula

Oil scarcity value holds because wells, pipes, and refineries cannot be copied in one quarter. If HBM scarcity value holds, it must land on the same class of loss that cannot be copied quickly. historical stress-test material explains 3:1 with three things: area, a yield product, and the base die. The direction of all three is right. The precision is not enough. What can enter the fact layer is not historical stress-test material's 48.6% yield formula. The primary numeric anchor is Micron's FY24 Q3 prepared remarks: industry-wide HBM3E consumes approximately **3× the wafer supply of DDR5** to produce a given number of bits in the same technology node, with HBM4 expected to require an even higher trade ratio. Micron's FY25 10-K later confirms the physical direction: HBM requires more wafers and cleanroom space for the same bits. The early self-derived 3:1 formula is therefore rejected as calibration; the company-disclosed ~3× trade ratio remains usable as A-grade evidence.

Hot Chips 2026 later provided additional engineering context around why the HBM3E-versus-DDR5 silicon gap exists. That conference coverage is corroborating evidence, not the primary source of the ~3× ratio. The scope remains the same-bit, same-node HBM3E-versus-DDR5 wafer-supply trade ratio, not a literal rule that one finished HBM wafer always "equals three DDR5 wafers."

So the economic meaning of 3:1 can stand without that uncalibrated formula: every high-bandwidth order a maker accepts gives up more conventional DRAM output. Area is eaten by TSV and KOZ. Cleanroom is eaten by stacking and the base die. Capex is eaten by sites such as Cheongju, Yongin, and Indiana. Whoever controls working TSV-stack and base-die yield has pricing power. The firms that can publicly volume-produce high-bandwidth stacks are still Hynix, Micron, and Samsung. CXMT's prospectus has 0 mentions of HBM. A fourth name cannot be written into 2026 effective supply.

Bit share still understates how much wafer is pulled away. The 51% confirm in Volume 5 is already HBM plus RDIMM bits. HBM's own bit share must be smaller than 51%. Micron's first-party ~3× disclosure and its later 10-K both show: for the same bits, HBM eats more wafers and cleanroom. A direct inference, no new percentage invented: HBM's weight in wafers and cleanroom is higher than its weight in bits. One maker sentence on conversion, and consumption loses more than 1:1. All that can be said is direction — move a line to stacking, and residual falls by more than the bits moved. That is why "shift onto DDR5" looks like saving HBM on the books and like a tax on the wafer.

## 4. HBM4 logic base dies may shift part of value capture toward foundry and packaging

If the base die runs 3nm / 5nm, HBM is no longer "the memory maker's own affair." It has to queue at TSMC. historical stress-test material writes the HBM4 16-Hi penalty as 4:1 to 5:1, because layers walk from 12 to 16, the yield product gets steeper, and one leading-edge logic chip is added. Direction can stay. The meter cannot. Hynix official text writes HBM3E and HBM4 supplied at the same time, and HBM4 already in large-scale production. No 16-Hi and no public yield formula; this does not negate Micron's separate first-party ~3× HBM3E-versus-DDR5 trade-ratio disclosure. Samsung official text writes HBM4 delivery starting Q1 2026, including 11.7Gbps. Also no 16-Hi. Micron's 10-K writes HBM4 36GB 12-Hi already sampled. The stack height that can be publicly confirm is 12-Hi, not the title's 16.

So a stretch of the "new oil" pipe network may be laid in someone else's fab. Until makers and TSMC both give checkable base-die shipments, that migration is mechanism, not a profit reallocation already done. Official TSMC sentences the current evidence review can still use: advanced packaging and test revenue about 8% in 2024, a bit over 10% in 2025; C.C. Wei, CoWoS tight / cannot meet demand; 2Q26, limits customers' growth. There is no split that says "how much 3nm the HBM base die ate."

The title puts 16-Hi beside the logic base die exactly to flag this migration. If the base die stays on the memory maker's mature process, scarcity value stays mostly with Korean makers. If the base die must enter TSMC, a slice of scarcity value moves to foundry, and HBM is no longer a single industry's well. The watch item can stay. The fact cannot be written.

## 5. Why the “new oil” metaphor has limits

HBM can almost never be used as inventory oil. Oil in a tank can still wait for the price. HBM's interface, stack height, and base die are bound to a given GPU generation. Four-year hardware depreciation means one generation of dice can hardly be sold at the original price across two system generations. Crude has a public benchmark and a futures curve. HBM is an annual or semi-annual large-customer negotiation. The price almost never appears in a 10-K line this report can cite. "New oil" therefore slides into narrative more easily: in shortage everyone says it is like oil; in glut there is no future in which to short a generation of 12-Hi dice. If the investment side holds memory stocks as oil companies, it must accept no inventory buffer, no public curve, only generation lock. The enterprise side should treat HBM as the threshold part without which a cabinet cannot ship, not as a consumable that can be topped up on the spot market.

MLA compressing KV Cache by 93.3% (draft number) is demand-side substitute energy. It does not make HBM vanish. It lowers "resident video memory per token." If firms turn the saving at once into longer context and higher concurrency, demand is still there. If they cannot, capex sunk into higher stacks and a leading-edge base die becomes an idle well. NVL72 writing 13.4 TB as unified memory is half defined by the system: NVLink first welds 72 cards into one logical chip, and only then does HBM look like fuel that must be bought by the cabinet. If more workloads can later be split inside the memory wall, the unit of measure walks from "whole-cabinet TB" back to "per-card GB." Until that day, procurement racing for 8-Hi / 12-Hi by the cabinet looks a lot like racing for crude berths at the dock. This volume does not forecast the year of that day. Once the unit of measure changes, the words "new oil" have to be rewritten, because oil rarely stops needing tanks just because the combustion algorithm improved.

Custom stacks tear the oil metaphor one more slit. Hynix's FY25 press release writes Custom HBM as a differentiator that continues to draw attention. This is not a volume number. It is a product form. Custom means stack, base die, and channel count are cut to one accelerator. Still less can it be flipped as inventory crude on a spot board. The coach sets the mix. The maker changes the tool to the mix. The die binds tighter to the generation, the cabinet, even a single customer. If the investment side still holds on "the memory cycle is warming," what it has misread is not profit elasticity. It is the inventory assumption.

On geography, three Korean-US-Japanese makers plus a possible TSMC base die make HBM easier to cut with export controls than a logic GPU. Reading HBM as a national "oil reserve" overstates tradability. It cannot be flexibly delivered on a spot market the way crude can. The reserve logic should be written as "working stack capacity plus foundry access for the base die," not tonnage.

## 6. Three scenarios, and what not to do

Three scenarios. No new probabilities attached:

- **New oil holds.** 12-Hi walks steady on the official already-shipping scope. The penalty still earns its keep economically. Hynix operating margin still near 49%; Micron CMBU still far thicker than almost-flat MCBU. If 16-Hi still appears only on a roadmap, that does not deny this scenario. What holds it is half the bits and maker books, not the stack height in the title.
- **Base-die bottleneck.** Memory makers announce the next generation. Shipments are stuck on a leading-edge logic base die or a packaging quota. What it looks like: maker press releases keep writing HBM4; what whole cabinets lack is "a complete solderable HBM set," not DRAM wafers themselves. A slice of scarcity value moves to foundry.
- **Algorithms or architecture cut demand.** A jump like MLA / MoE spreads, or clouds actually adopt what TrendForce itself wrote — "reduce the HBM integrated into each AI chip." Maker margins fall back from 49%. The 10-K sentence "same bits need more wafers" still holds on physics, but no longer earns its keep economically. Conventional DRAM flows back on Micron's 10-K reverse sentence.

The other side must be written fully, or "new oil" inflates on its own. First: about 1,200 dice versus about 400, and 48.6% set beside the figure's 54% to 65%, show that draft 3:1 is an order-of-magnitude conclusion, not a calibrated process-control chart. Second: Hynix 49% and Micron CMBU $13.52B contain a present shortage premium. They are not long-run equilibrium scarcity value. Third: calling HBM oil makes people think demand has no elasticity. Fourth: 51% is bit supply, not revenue. 47% / 68% are not four-cloud 10-K line items.

Testable: whether Micron's next 10-K still writes "same bits need more wafers"; whether HBM4 is 12-Hi samples or a higher stack shipping; whether Hynix and Samsung official pages show a 16-Hi spec sheet; whether TSMC earnings calls have a checkable base-die sentence.

What not to do: do not write 16-Hi as already in volume production; do not write 3:1 as a factory control chart; do not multiply 13.4 TB out to 50,000 cabinets and then divide by unpublished global HBM bits; do not convert Hynix and Samsung won into dollars and add them to Micron; do not write the CXMT IPO into the HBM supply function. The full residual and multiply-by-cabinet write-up is [Volume 5](vol-05.md).
