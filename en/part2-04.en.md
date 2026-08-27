# Macro Essay 4: Hyperscaler CapEx, System-Stack Counterattack, and Architecture-Driven Cost Reduction

Chinese original: [part2-04.md](part2-04.md)

Mixed-year four-cloud scope: `四云Capex口径核对.md`. Whether ASICs retreated to 5nm + DDR5: [Volume 4](vol-04.md) and [Volume 24](vol-24.md). How to use the DeepSeek training books: [Volume 26](vol-26.md). This essay does not reopen the spec table. This essay only collects: group-wide PPE is not an AI-hardware line item; broad training substitution remains incomplete.

## 1. The question this essay answers

What the four clouds have already spent — is it group-wide property-and-equipment purchases, or an "AI hardware" line item? Has a self-built ASIC pulled hyperscale pretraining off Nvidia cabinets? DeepSeek-V3's MLA and the draft's training-cost figure — did they ease this spend, or make already-sunk group capital harder to recover?

This essay does not write the draft's "2024 AI hardware $215B" and "2026 four-cloud $670–$750B" as facts that have already happened. What can be checked is the PPE line on each cash-flow statement, and node and memory on each firm's own product pages. ASIC products exist. broad training substitution remains incomplete. Public next-generation specs are 3nm-class logic plus HBM, not a retreat to 5nm plus commodity DDR5.

## 2. Accounting and evidence boundary

The core accounting rule is simple: hyperscaler PPE / CapEx is company-wide and must not be rewritten as a clean AI-hardware line item.

The 2024 mixed-year reconstruction is roughly **$211.9B–$213.9B**; the 2025 mixed-year level is roughly **$354.0B–$356.5B**. By August 2026, the public scale indicators were Microsoft ~**$190B** calendar-year CapEx expectation, Alphabet **$180–190B**, Meta **$125–145B**, and Amazon about **$169B** of TTM net PPE purchase. These windows still differ and cannot be mechanically summed into one official AI-hardware total.

Historical 2026 $670–750B scenarios, fixed depreciation tables, unverified rack ASPs, and cloud-ASIC TCO percentages remain stress-test material. DeepSeek-V3's **2.788M H800 GPU-hours** is a first-party technical anchor; the report-side **$5.576M** conversion is not a complete company R&D cost.
## 3. Mechanism (physical / commercial / geopolitical)

### 3.1 Group-wide PPE is observable; an AI-only line item usually is not

The accounting base comes from company IR cash-flow statements and statutory filings, with each firm's own scope preserved. Line-item alignment follows the check file.

Microsoft's fiscal year ends 30 June. The line is Additions to property and equipment. FY25 official cash-flow statement writes $(64,551) million, versus FY24 $(44,477), FY23 $(28,107). Source: https://www.microsoft.com/en-us/investor/earnings/fy-2025-q4/cash-flows . FY26 official earnings release writes the same line as full-year $(115,948) million, the quarter $(35,802) million, versus prior full year $(64,551). Source: https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q4/press-release-webcast . FY26 is July 2025 to June 2026. It cannot be added into the same cell as Amazon, Alphabet, Meta calendar 2025, and still less can FY26 actuals be treated as the fourth item of a "calendar-2026 four-cloud total."

Amazon is calendar year. The company's own capex / FCF definition is Purchases of property and equipment, net of proceeds from sales and incentives. Exhibit 99.1 (2026-02-05) writes 2025 purchases $(131,819) million, sales and incentives $3,499 million, net TTM $128,320 million; 2024 net $77,658 million (82,999 − 5,341). Jassy in the same piece writes: expect to invest about $200 billion in capital expenditures across Amazon in 2026, group-wide, including AI / chips / robotics / satellites. Source: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm .

Alphabet is calendar year. The line is Purchases of property and equipment. Q4/full-year 2025 Exhibit 99.1 writes full-year $(91,447) million, versus 2024 $(52,535) million. Source: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000012/googexhibit991q42025.htm . The Q4 2025 earnings commentary then gave 2026 guidance $175–$185 billion. June 2026 investor materials rewrote the full-year expectation as $180–$190 billion. Both bins are guidance, not actuals. Whichever bin is used, they cannot be added with the other three names' different period-ends into "four-cloud 2026 $750B."

Meta's main table uses Purchases of property and equipment; the company's oral capex also adds Principal payments on finance leases. Full-year 2025 equipment purchases $(69,691) million, finance-lease principal $(2,524) million, company scope $72.215 billion (the release writes $72.22 billion); 2024 equipment $37,256 million + leases $1,969 million = $39.225 billion. Source: https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx . The check file's 2026 guidance is the annual-report-time $115–$135 billion (including finance-lease principal). Later official Outlook raised and narrowed: Q2 2026 written as $130–$145 billion. The raise is guidance, not already happened.

On a re-addable scope, 2025 actuals (Microsoft still FY2025, the rest CY2025): equipment purchases, Amazon net, Meta without leases, 64,551 + 128,320 + 91,447 + 69,691 = $354,009 million (about $354.0B); Meta on company scope about $356.5B. This is already not $215B. 2024 mixed-year summary sentences and 2025 actuals cannot be written as the same fact. The 2026 public figures now cover all four hyperscalers at different accounting windows; they show continued capital intensity but still do not form one directly addable calendar-year AI-hardware total.

The physical object is still a three-piece set: accelerator cards or ASICs, power, packaging. Group-wide PPE getting larger only proves buyers are still paying for halls and machines. It does not prove "AI cabinets" have already been spent on the draft's split. Without a CoWoS official split of the 120k–130k wafers/month class, this essay does not write a capacity-ceiling figure. The mechanism that can be written: PPE is capped by packaging, HBM, and interconnect licenses, not a scale a CFO budget can freely choose.

PPE additions and depreciation expense are not the same row. Microsoft's FY25 cash-flow statement on the same page writes Depreciation, amortization, and other $34,153 million, while PPE additions are $64,551 million; FY26 D&A $38,534 million, PPE additions $115,948 million. Depreciation is the expense of assets already landed. PPE is cash still being formed. Using PPE directly as "annualized hardware depreciation" folds in civil works, construction-in-progress not yet placed in service, and fulfillment networks. Amazon's net definition also subtracts sales and incentives. Meta's company scope adds finance-lease principal back. Four period-ends staggered by half a year: any "four-cloud total" is an analyst addition, not a line the four jointly disclosed. The check file locked this: do not knock it against Nvidia revenue. Buyer and seller line items differ.

### 3.2 Cloud system stacks are real; broad training substitution remains incomplete

Public hyperscaler systems increasingly compete at the system-stack level, not only the die. However, next-generation systems still rely on HBM, advanced logic, high-speed interconnect, packaging, and power. That can divert NVIDIA platform profit while increasing competition for the same upstream scarce resources.

The first-party conclusion is narrow: TPU, Trainium, Maia, and MTIA are real system programs, but public data do not yet establish an industry-wide training-share transfer away from purchased accelerators.

The limiting question is ecosystem completeness: compiler/runtime maturity, scale-up and scale-out fabrics, workload portability, and dependence on HBM/advanced packaging. A custom accelerator is not automatically a substitute for a production training system.

### 3.3 DeepSeek: a first-party compute-efficiency anchor, not a universal cost curve

DeepSeek-V3 reports 671B total parameters, 37B activated per token, and **2.788M H800 GPU-hours** of formal training. Its report-side $2/GPU-hour conversion yields about **$5.576M**, excluding prior research and ablations. This is useful evidence that architecture and systems design can reduce formal training compute. It does not imply that every frontier model has the same full development cost, or that HBM, packaging, and power cease to matter.

## 4.
## 4. Scenarios, counterarguments, and testable indicators

The 2026 by-firm forecast table is unverified. Do not treat it as audit fact.

Scenario A: group-wide PPE keeps expanding with disclosed guidance. Internal accelerators absorb recommendation and part of inference, while external systems continue to carry a meaningful share of training. Algorithmic efficiency lowers unit cost without triggering broad destocking. This is a state of continued infrastructure expansion with incomplete system-stack substitution.

Scenario B: usage parks at +50%, unit price falls 50% on open source, the matrix declares overhang. The draft's $115.5B depreciation cannot find $155B of increment — those two figures are draft arithmetic, not 2025 actual depreciation. If order cuts happen, they start with training cabinets. ASIC projects will be cut with them, because internal teams also have to prove ROI. Mixed-year 2025 four-cloud PPE is still adding, which says this cell has not appeared.

Scenario C: the MLA path becomes default. 8-card servers take a large share of inference. The draft's $750B becomes excessive. Capital turns from buying cabinets to buying workflow software. Cloud moats partly retreat from quota to data and distribution. This is the algorithm-breakthrough cell, not the present.

Counters: treating a $750B sum as an already-approved budget; writing mixed-year about $211.9B group-wide PPE as "AI hardware $215B"; extrapolating $5.576 million to "every frontier model needs only five million dollars"; treating a TPU spec table as obtainable training share for external customers; writing Maia 200 / Trainium3 / Ironwood / MTIA 300+ HBM specs as "already won training."

Testable indicators: whether each next cash-flow statement's PPE still adds on guidance; whether there is AI incremental revenue as its own row; whether Trainium / TPU / Maia external instances are still complained about on dynamic shapes; whether open-source model training cost keeps landing below ten million dollars; whether public token prices show a 30%–50% annualized fall; whether any cloud writes on an official page "the training mainstay has left bought-in cabinets." Shipments and training-share estimates remain unquantified until first-party or high-quality institutional evidence is available.

The executable sentence for a CFO is only one: do not assume in the same budget "usage +300%, unit price does not fall, and the draft's $750B must be spent." The right order: first take a usage cell you are willing to believe, then see whether that cell still covers already-happened group-wide PPE depreciation when unit price falls 30% and 50%, and only then decide whether next year still approaches the forecast table. ASIC projects use the same order: first ask whether they are truly cheaper than bought-in cabinets on dynamic shapes and long context, then ask whether the compiler team's cost is below the purchase saved. DeepSeek is not a slogan to stop spending. It is a reason to change spend from "buy a full set of cabinets" to "buy enough effective tokens to cover the workflow."

Win and loss are not in a press-release capex figure. They are in depreciation per effective token. Whoever can still make this unit fall after MLA and ASICs is still on the field. Whoever can only let this unit rise with cabinet price is making a market for the seller's high gross margin. Cloud system-stack substitution is meaningful but incomplete, so incumbent platform value capture remains substantial. Not winning is not already closed. Writing $750B, ASICs, and DeepSeek as three parallel stories is wrong. They are three terms of one equation. The left side is already-happened group-wide PPE and the next few years of depreciation. The right side is incremental revenue. The conversion coefficient in the middle is hardware cost per unit of intelligence. ASICs lower the private-purchase term in the coefficient. MLA lowers the memory and training terms. The draft's $750B enlarges the left side. When all three expand in the same direction, the equation is harder to balance. DeepSeek lets the right-side unit price fall, and then requires usage to make it up. If a cloud giant does three things at once — add group capital hard, push self-build hard, cut price hard — it puts mutually fighting demands in front of the same CFOs. This essay only writes the fight down. It does not announce who has already won.

## 5. Gaps and what must not be treated as fact

The 2026 forecast table is a mix of guidance and forecasts, not an audited total. $121.875B, $115.5B depreciation, $155B incremental revenue are draft assumed formulas. $670–$750B cannot be added. It does not enter the fact layer. "AI hardware $215B" does not hold: what can be re-added is mixed-year group-wide PPE about $211.9–$213.9B. Foundries for TPU / Trainium / Maia / MTIA: write only sentences the company itself named. Google and AWS latest generations officially do not name TSMC; cannot write "already left TSMC," and cannot write "already foundried by TSMC." MTIA 300–500 officially writes Broadcom + HBM, does not name 3nm. NVL72 dollars per cabinet, ASIC TCO savings of what percent, Broadcom's percent of CoWoS: the companies themselves did not say so on the pages above. Do not write them. DeepSeek $5.576 million is the report's conversion at $2 / GPU-hour rent, official training only. $35–50B "current increment" has no by-firm source. Microsoft now provides a calendar-2026 CapEx expectation, but the four hyperscaler figures still use different windows and definitions. This essay does not claim to audit 10-Ks.
