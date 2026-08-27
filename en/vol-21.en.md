# Volume 21: AI Infrastructure Capital Flows and Profit-Pool Structure

Chinese original: [vol-21.md](vol-21.en.md)

FY26 and prepayments are [Volume 1](vol-01.en.md). Four-cloud mixed year is `四云Capex口径核对.md`. Residual is [Volume 5](vol-05.en.md). This volume does not invent a falsely precise input-output table, and it does not knock NVIDIA revenue against four-cloud capex into a share.

## 1. Core question

How does capital move through the AI-infrastructure stack, which layers retain value, and which accounting lines are merely pass-through flows?

The report does not add hyperscaler CapEx, NVIDIA revenue, foundry revenue, and memory revenue into one “market size,” because the same physical system would be counted multiple times. The useful model is a **layered cash-flow and value-capture map**:

```text
end demand / cloud budget
→ data-center and system purchases
→ accelerator / interconnect / memory / packaging / power
→ seller revenue and margin
→ prepayments / supplier CapEx / capacity expansion
→ next-generation supply
```

Each layer must retain its own accounting scope.
## 2. Current financial anchors and evidence boundary

The current map uses first-party or clearly graded data rather than an old cross-company “profit pool” table:

- NVIDIA FY26 revenue **$215.938B**, Data Center **$193.737B**, FCF **$96.575B**; FY27 Q2 operating income **$63.734B**.
- TSMC 2025 HPC share **58%**, gross margin **59.9%**, advanced packaging/testing slightly above **10%** of revenue.
- SK hynix FY25 operating margin **49%** and HBM revenue more than doubled year over year.
- Four-cloud company-wide CapEx/PPE roughly **$354.0B–$356.5B** on the 2025 mixed-year reconstruction.
- NVIDIA supply-related commitments **$119.0B** at FY27 Q1.

Historical cabinet BOM estimates, fixed software-premium percentages, mixed-year “$215B AI CapEx,” and fixed depreciation amounts are not issuer-disclosed profit-pool splits and remain outside the fact layer.
## 3. Mechanism: flows, retention, reinvestment, and residual supply

**First hop: capital enters through multiple buyer classes, including hyperscalers and Anchor Compute Buyers.** Model companies can now influence infrastructure directly through long-duration commitments, even when the underlying assets remain on cloud, data-center, utility, or financing-partner balance sheets. The first hop is: cloud capex to the whole cabinet, then to foundry and packaging, memory, liquid cooling, power, copper, and contract assembly. Four-cloud scope is [四云Capex口径核对](四云Capex口径核对.md). earlier stress-test material $215B can no longer be the profit-pool denominator. The line is group-wide, not a GPU split.

**Knocking is forbidden: system seller revenue is not a half-share of four-cloud capex.** FY26 data center is [Volume 1](vol-01.en.md). Given that four-cloud capex is not all accelerator cards, the relative position only shows that systems ate the fattest slice of capex. It cannot be written as a share. The lines differ, the years differ, buyer and seller each book their own. If a profit-pool model knocks here, every later percentage is pulled off.

**Retention: value capture depends on scarcity, substitutability, and bargaining power—not one universal margin comparison.** Intel 1999 and the FY26 table are [Volume 1](vol-01.en.md). This volume does not reopen them. Once the sales unit moves from the chip to the cabinet, the collection unit of the profit pool also moves from a single die to one cabinet. Whoever can prepay, and whoever can swallow memory and packaging price-ups into the whole cabinet, can add a tranche.

**Refill: asset-light outsources line refill.** The profit pool has two faces. The income statement is thick. The cash-flow statement must keep refilling lines. NVIDIA itself is asset-light. Most refill work is not in its own plants. TSMC must turn margin back into the next leading-edge process and packaging. Memory makers must turn operating profit back into HBM stack lines. The second hop of cash is: the system seller's prepayments and the cloud's purchase orders become foundry and memory capex, then become the next, more expensive cabinet. Depreciation bites on the cloud side. The depreciation wall is [Volume 30](vol-30.en.md).

**Second profit pool: half the bits already go to cabinets.** 51% and 47%/68% are [Volume 5](vol-05.en.md). If clouds shift inference onto DDR5, they grab residual already inside that half. The China stack is [Volume 12](vol-12.en.md). This volume does not invent an input-output table.

## 4. Scenarios, counterarguments, and testable indicators

Four value-capture scenarios are considered without introducing new probabilities or unsupported percentages:

First: the pool keeps concentrating upstream. Cloud capex does not fall. NVIDIA data-center revenue walks another step from $115.186B to $193.737B. TSMC HPC and Hynix HBM shares keep rising. If the move of supply commitments from $95.2B to $119.0B still repeats, prepayments lock the next packaging and stack lines first. Whether the software premium is still earlier stress-test material's about 40% has no official split table. It cannot be treated as already held. What can be an anchor: gross margin still in the 71% to 75% band; maker operating margins still in the Hynix 49% and Samsung Memory high-value-add-priority band. The scarce-layer value-capture story holds on this band.

Second: the pool is thinned by algorithms. A jump like compressing KV cache lets the same service buy less HBM and fewer whole cabinets. The HBM slice of bit supply loosens first. Hynix 49% gives back. Cloud depreciation pressure eases. system seller shipment growth falls. Even after a break, the residual-capacity pressure does not vanish at once: makers have already turned lines toward high value-add, and cutting back takes time. Micron's 10-K itself writes the reverse sentence: only when demand weakens do wafers return to conventional DRAM. Until the return is done, phones and PCs still pay the tax.

Third: the pool breaks at the cloud layer. If enterprise incremental revenue stops at earlier stress-test material's $35B to $50B row, while capex still charges ahead at TrendForce's another +98% and another +50%, the flow will first be cut in cloud boardrooms, and the upstream profit pool will shrink with it. $35B to $50B and $670B to $750B are both extrapolations, unverified; do not treat as first-party fact. Observable substitutes: whether four-cloud mixed-year capex turns from the $354.0B order of magnitude, and whether TrendForce's memory-as-share-of-cloud-capex 47% to 68% is held or revised in later notes.

Fourth: the residual-capacity pressure holds on its own. Even if cabinet growth slows, as long as makers do not cut HBM lines back, conventional bits remain a scarce residual. Huaqiangbei talk and TrendForce contract-price outlooks can both be true: the tip smashes first, contract prices follow later. In this scenario the profit pool does not return to the 2023 Hynix operating-loss page. It only moves from cabinet fat to stick-and-drive fat. The watch item is whether Hynix still writes in the press release both HBM doubling and a sharp rise in conventional server memory.

Three other-side sentences must enter the model, or the profit pool will be frightened by whole-cabinet unit prices. First: drawing four-cloud gross margins and NVIDIA gross margin in the same profit pool misleads. The denominators differ. Amazon includes retail. Meta includes ads. NVIDIA is almost data-center systems. The correct comparison is AI-related segments. The only segment the current evidence review can align is NVIDIA data center $193.737B. Microsoft Intelligent Cloud, Google Cloud, and Meta AI have no peer segment margins newly opened in this volume. Leave them empty. Second: the whole-cabinet BOM is an engineering-estimate range. $1.10M to $1.40M of software premium cannot be added straight into company-level 75%. Third: ASICs shunting internal load is real, but public next generations have not retreated to commodity memory. Firms and states that bet they can leave the whole-cabinet system next year and shift onto DDR5 have misread the river.

Testable marks refill only the columns that can be checked against a table each year. NVIDIA: whether revenue is still walking up from the $215.938B band, whether data center is still walking up from the $193.737B band, whether gross margin is still 71% to 75%, whether free cash is still on the order of $96.575B, whether supply commitments still add from $119.0B. Four clouds: whether mixed-year equipment purchases stay near $354.0B to $356.5B or turn. TSMC: whether HPC is still 58%, whether the first customer is still 19%. Hynix: whether operating margin is still 49%, whether HBM revenue is still written in the press release as more than doubled year on year. Micron: whether the cloud-memory slice is still far larger than the phone-and-PC slice. TrendForce: whether 51%, 47%, 68% are held or revised in later notes. CXMT: whether a prospectus or later statutory disclosure shows a standalone HBM row. Until a reliable segment disclosure of enterprise AI software revenue appears, the $35B to $50B row cannot enter the profit-pool main table.

Cash flow still lacks several edges that should exist and that official notes do not give: the dollar amount of HBM logic base dies flowing back to TSMC, the packaging split inside TSMC revenue, liquid-cooling and copper-cable vendor revenue, and annual power bills on nuclear offtakes. Without those edges, so-called full-chain true upstream and downstream only covers the four or five brightest nodes. The honest use of the model is to watch direction year by year: whether the spend side is still expanding, whether the collection-side margin stack is still the 75%, 59.9%, 49% band, whether bit supply is still half to cabinets. If the direction changes, rewrite the profit pool. If it has not, do not invent a falsely precise percentage for more precision.

The five interrupts are the Judgment and [Volume 8](vol-08.en.md). The case file is [Volume 11](vol-11.en.md). The use of a profit-pool model inside the window is not to forecast an end price. It is to check each year: whether money still stops at the whole-cabinet band that can swallow a price-up, and whether the residual is still taxing phones and PCs.

If a data-version model must be given a skeleton that can be hand-calculated, it can only stop at already-allowed sums. It cannot invent coefficients. Known spend side: four-cloud mixed year $211.9B to $213.9B, and the next mixed year $354.0B to $356.5B. Known collection side, brightest: NVIDIA data center $193.737B, TSMC 2025 gross margin 59.9%, Hynix 49% operating margin. These three cannot be added. Currencies differ, scopes differ, and they contain a large non-AI mass. Hand calculation only asks direction, not a falsely precise global AI market size.

## 5. Gaps and what cannot be treated as fact

1. There is no true input-output table or inter-company transaction matrix. NVIDIA data-center revenue and four-cloud capex cannot be treated as each other's counterpart.
2. Older mixed-scope $215B and Microsoft range estimates are not used as current anchors. The publication baseline uses the reconciled mixed-year $211.9B–$213.9B 2024 equipment-purchase range and Microsoft FY25 point figures.
3. Won and dollars are used together. SK hynix and Samsung figures are kept in their reported KRW denomination where the company source provides no conversion rate.
4. Downstream 20% to 30%, SaaS 85% to 55%, 2026 $750B and $115.5B depreciation, and $35B to $50B software revenue may not be treated as first-party fact.
5. The two whole-cabinet BOM number sets are unreconciled, and they are not NVIDIA-confirmed revenue tables. Maker gross margin over 60% and per-die switch margin greater than 85% do not enter the fact layer.
6. Micron, Samsung, AMD, Broadcom, Amphenol, Hon Hai and others appear in the BOM but have no peer segment tables newly opened in this volume. Chain coverage is still incomplete.
7. 47%, 68%, and 51% are TrendForce institutional estimates, not four-cloud filing line items. Micron's ~3× HBM3E-versus-DDR5 wafer-supply trade ratio is A-grade first-party company evidence. CXMT monthly capacity is not written; YMTC's public layer statement is kept separate from monthly-wafer claims.
8. This volume relies on the cited financial, memory, and source-index evidence and does not constitute an audit opinion on each firm's full annual report.
9. 8.6, 13.2, three-maker 1.80 million wafers per month, and Samsung cutting 80k wafers back from HBM stay empty per the memory-residual evidence list. This volume does not write them.

(This volume invents no new profit-pool percentages or transaction amounts. New judgments are marked Quantitative forecasts without a source are marked unverified; do not treat as first-party fact.)
