# Volume 31: Core Indicators and Evidence Monitoring Framework

Chinese original: [vol-31.md](vol-31.en.md)

Regulatory mechanism: [Volume 11](vol-11.en.md). Seller economics and supply commitments: [Volume 1](vol-01.en.md). Power-status framework: [Volume 35](vol-35.en.md).


## 1. Purpose of this volume

A long-duration industry report needs a monitoring system that can update conclusions without rewriting the entire narrative after every headline. This volume therefore tracks the variables most capable of changing the S1–S4 state:

- seller economics and supply commitments;
- foundry and advanced-packaging tightness;
- HBM / DRAM product mix;
- hyperscaler CapEx and utilization;
- power projects by announced / contracted / permitted / energized / utilized status;
- cloud system-stack substitution;
- China parallel-stack closure;
- regulatory procedure and structural remedies;
- capital-clearing signals.

Each indicator retains its own accounting scope and evidence grade. Seller revenue is not buyer CapEx; customer revenue share is not wafer share; statutory penalty ceilings are not fines; inquiries are not complaints; contracted MW is not energized load.
## 2. Monitoring anchors

The current monitoring baseline uses verified or clearly graded anchors rather than a single "audited master table":

- NVIDIA FY26 revenue **$215.938B**, Data Center revenue **$193.737B**, FCF **$96.575B**; FY27 Q2 revenue **$96.221B**, Data Center **$89.0B**, GAAP gross margin **75.0%**, operating income **$63.734B**.
- Supply-related commitments: **$95.2B** at FY26 year-end and **$119.0B** at FY27 Q1.
- TSMC 2025: about **15.0M** 12-inch-equivalent wafer shipments, HPC **58%**, smartphone **29%**, advanced packaging + testing slightly above **10%**.
- Micron: HBM3E requires roughly **3× the wafer supply of DDR5** at the same node and bit capacity — **A-grade first-party evidence**.
- TrendForce: NVIDIA represented more than **60% of 2025 CoWoS demand** — **B-grade institutional evidence**.
- Report geometry: **5.39 CoWoS wafers/rack** — **D-grade stress-test estimate**.
- Power projects: Microsoft/Constellation ~**835 MW**, Talen/AWS up to **1.92 GW**, Google/Kairos up to **500 MW**, each tracked by legal and physical status rather than nominal capacity alone.

Historical mixed-year CapEx sums, fixed depreciation templates, unverified BOMs, and point estimates of software premium remain stress-test material rather than monitoring facts.
## 3. Mechanism (physical / commercial / geopolitical)

### 3.1 Grade the cells first, then talk power

The appendix's first job is evidence grading.

- **A grade — first-party / directly checkable point evidence:** NVIDIA FY25/FY26 filing figures; Microsoft, Amazon, Alphabet, and Meta line items where the accounting scope is explicit; and Micron's first-party disclosure that, at the same node and bit capacity, HBM3E requires about **3× the wafer supply** of DDR5. DeepSeek-V3's $5.576M formal-training compute conversion is also checkable against its technical report, but it must retain the report's boundary: formal training only, excluding prior research and ablations.
- **B grade — institutional estimates / ranges:** TrendForce's estimate that NVIDIA accounts for **more than 60% of CoWoS demand** belongs here. It is not a TSMC customer disclosure. Old mixed-year ranges and "broke X" formulations can be used only for magnitude checks, not exact reconstruction.
- **C grade — qualitative statements:** "HPC overtook smartphones," "fully AI-enabled," or period-mixed narrative phrases are not quantitative anchors when a precise official line exists.
- **D grade — engineering geometry / stress tests / unsupported endpoints:** BOM ranges, MFU assumptions, the report's **5.39 CoWoS wafers-per-rack** coefficient, fixed SaaS-margin endpoints, future capacity-capture stress tests, and specific monthly capacity numbers without first-party support.

The central correction is explicit: **HBM ≈3× is no longer D grade; 5.39 still is. CoWoS >60% is B grade, not a TSMC fact.**

Scopes that cannot be compared must be separated before analysis. NVIDIA Data Center is seller segment revenue; cloud CapEx is group-wide buyer investment; SK hynix operating margin is not gross margin. Different business models' margins cannot be collapsed into a "who is better at AI" or monopoly score. The useful question is which evidence supports physical scarcity, value capture, and allocation mechanisms at which confidence level.

The 2024 four-cloud reconstruction remains about $211.9B–$213.9B on a mixed-year, mixed-scope basis; 2025 is about $354.0B–$356.5B. By August 2026, Microsoft had guided to roughly $190B of calendar-year CapEx, Alphabet to $180B–$190B, Meta to $125B–$145B, and Amazon's trailing-twelve-month net PPE was around $169B. These time windows and line items still differ and must not be added into one "AI hardware CapEx" number.

The four-year hardware + fifteen-year civil-works depreciation model remains a stress-test template rather than a sum of four audited asset-class schedules. Specific 2026–2028 depreciation expense is therefore not an first-party fact.

### 3.2 US Department of Justice: inquiry yes, complaint no

[Volume 11](vol-11.en.md) confirm this line: the inquiry is real. Litigation and a fine have not landed. The report does not treat a subpoena as a split order.

2024-08-02 Reuters, citing The Information: the Department of Justice had opened a probe after rivals complained NVIDIA may have abused a dominant position in AI-chip sales. The inquiry looks at whether it pressed cloud vendors to buy multiple products, and whether it sold networking gear at higher prices when customers wanted AMD or Intel AI chips. The same day CBS / AP checked with DOJ: no comment, no further information at the time. That is investigative reporting, not a complaint. URL: https://www.reuters.com/technology/nvidia-faces-us-doj-probe-over-complaints-rivals-information-reports-2024-08-02/

2024-09-03 Bloomberg (Ian King / Leah Nylen): DOJ sent subpoenas to NVIDIA and other companies seeking evidence it violated antitrust law; earlier it was questionnaires, now a legally binding request. Bloomberg Law adds two sentences of procedure: this moves the government closer to a formal complaint. Bloomberg wrote "closer to a formal complaint," not that a complaint had been filed. Reuters paraphrased the same piece. URL: https://www.bloomberg.com/news/articles/2024-09-03/nvidia-gets-doj-subpoena-in-escalating-antitrust-investigation

2024-09-04 NVIDIA spokesperson: We have inquired with the U.S. Department of Justice and have not been subpoenaed. Nonetheless, we are happy to answer any questions regulators may have about our business. Bloomberg's next-day piece carried the same denial and explained that civil investigative demands are often called subpoenas orally. The subpoena fact follows DOJ's own paper. The company then denied receipt. URL: https://www.reuters.com/technology/nvidia-did-not-receive-us-justice-department-subpoena-spokesperson-says-2024-09-04/

As of 2026-08-26: in the Antitrust Division public cases on `justice.gov`, the 2025 complaint that can be read is *U.S. v. Hewlett Packard Enterprise Co. and Juniper Networks, Inc.* (2025-01-30). The defendant is not NVIDIA. No Complaint for *United States v. NVIDIA Corp.* was read, and no Competitive Impact Statement / Proposed Final Judgment. A third-party docket (AI Lawsuit Tracker, last check written 2026-06-02) itself states: Active DOJ Investigation — No formal complaint filed as of April 2026; Settlement: No settlement on record. That is an aggregator, not DOJ. Use it only to check that "the public record is still empty." In March 2026 Warren / Blumenthal sent a letter on the Groq license. That is a congressional inquiry, not an antitrust complaint.

The US Sherman Act has no "10% of annual turnover" clause. What can change the rules overnight on the US side is a split, an injunction, forced interoperability — not copying the EU ceiling. As a matter of doctrine, the US does not punish a monopoly "won by product and foresight." What it would hit is tying, supply discrimination, using capacity to punish stack-switchers. Those need contracts, mail, and customer testimony. An inquiry can run for years. The public record stops at an inquiry. The appendix cannot write that a complaint has been filed, a settlement reached, Mellanox already split, or CUDA already forced open.

### 3.3 France: near the end, no statement of objections issued

The company itself wrote that France was looking. NVIDIA 2023-11-21 quarterly (Reuters 2023-11-24 quoting the original): For example, the French Competition Authority collected information from us regarding our business and competition in the graphics card and cloud service provider market as part of an ongoing inquiry into competition in those markets. The same paragraph writes that EU and Chinese regulators also asked for information on GPU sales and supply allocation. The same Reuters piece writes: France raided the Paris office in September (people familiar). That is an inquiry, not a sanction decision.

2026-07-09 Reuters wire (full text reprinted on Euronext): The French competition authority said on Thursday its probe into chipmaker Nvidia Corp is coming to an end. Rapporteur général Umberto Berkani: We are nearing the end of the investigation. Reuters writes clearly: the end of an investigation is not a necessary sanction. The investigation service must first decide whether to issue a statement of objections, or close. If it issues, NVIDIA has a chance to reply, then the Authority's board makes a final ruling. Global Competition Review the same day (paywalled): France’s Competition Authority is “approaching” a decision on whether or not to formally accuse Nvidia. This public pass can still read CNA and The Next Web paraphrases of the same wire. The sentences do not go beyond "near the end; the next step is whether to issue a statement of objections." From 2026-07-09 to 2026-08-26: no communication des griefs or sanction decision on NVIDIA was read on the Autorité de la concurrence site. Secondary pieces that write "near a decision on whether to accuse" as "about to issue charges" are adding a step. The original does not have it.

French Commercial Code L464-2: the fine ceiling on an undertaking is 10% of the highest worldwide untaxed turnover. 10% of FY26 revenue $215,938M is $21,593.8M. That is a statutory ceiling, not a fine about to be issued. Without a statement of objections, this product cannot be written as "France is about to issue $21.6B."

### 3.4 EU: questionnaires sent, no formal opening, no fine

Reuters 2024-12-06: EU antitrust regulators were asking NVIDIA's rivals and customers whether the chipmaker bundled products to gain an unfair advantage; people familiar said the move could lead to a formal investigation. Reuters 2024-12-04: the same round of questionnaires hung on the Run:ai merger review, not an already-opened 101/102 case.

The merger itself: the Commission on 2024-12-20 unconditionally approved Run:ai. The public decision is Case M.11766 – NVIDIA / RUN:AI, under Article 6(1)(b) of the Merger Regulation. The deal itself had no EU dimension. The Italian competition authority submitted it under Article 22. The Commission accepted on 2024-10-31. NVIDIA on 2025-01-10 sued the Commission over Italy's Article 22 referral (T-15/25). Reuters 2025-02-24: the suit does not affect the already-approved Run:ai deal. That is a merger-jurisdiction suit, not a fine for abuse of dominance. EUR-Lex has the T-15/25 application summary: request to annul the 2024-10-31 decision accepting the Italian referral; first plea that the Article 22 reading is inconsistent with *Illumina*.

Capitol Forum 2026-02-11, citing sources, said the Commission was still asking about the definition of data-center components. That is news, not a Commission *Opening of proceedings* press release. Fortune 2024-07-05 quoting Vestager: chip supply is a bottleneck, not equal to a regulatory action. As of 2026-08-26: no formal DG COMP opening, statement of objections, or fine on NVIDIA under 101/102 was read.

Questionnaires sent is true. Unconditional Run:ai clearance shows that, on the merger slice, the Commission then did not find structural remedies necessary. T-15/25 shows the company is fighting jurisdiction. It does not show an abuse-of-dominance case has been opened. If the appendix writes "the EU is looking at NVIDIA" as "a formal case has been opened" or "a 10% fine is about to issue," it has added questionnaires and a statutory ceiling into a complaint.

### 3.5 10% of annual turnover is a statute, not a fine

Regulation 1/2003 Article 23(2): For each undertaking and association of undertakings participating in the infringement, the fine shall not exceed 10 % of its total turnover in the preceding business year. The Commission's fines page writes the sentence again. Article 7 of the same regulation is the clause that can split structure: the Commission may impose behavioural or structural remedies; structural remedies only when behavioural remedies would be equally ineffective or more burdensome. That is a list of powers, not a power already used on NVIDIA. URLs: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32003R0001 and https://competition-policy.ec.europa.eu/index/fines_en

The French ceiling is L464-2 above. Arithmetic is not a fine. NVIDIA FY26 revenue $215,938M. 10% is $21,593.8M. That is a statutory ceiling times the company's own annual report, not a number issued by the Commission or the French Authority. Without an opening and without a statement of objections, this product cannot be written as "about to issue $21.6B."

Money can be compared. The comparison cannot be written as a sanction decision. Q1 FY27 one-quarter operating income $53.536B. The French or EU statutory ceiling of about $21.6B is about 40% of that quarter's operating income, and about 18% of FY26 net income $120.067B. As long as there is no split, no forced-open interface, and no ban on prepayments locking capacity, a fine is a cost. Buybacks plus dividends returned $41.1B to shareholders in a year. a fine primarily changes earnings unless it alters interfaces, tying, supply conduct, or structure. Capacity allocation must still be analyzed through commitments, order scale, credit, utilization, supplier diversification, and geopolitics. Write $21.6B into cost and the prepayment slice that locks capacity is still there.

### 3.6 National security: advanced compute is already written as national security

A split is doable as a matter of doctrine. After the files below write the same chip slice as national security, it is harder to land administratively. The files prove only "written as national security." They do not prove "already decided not to split."

White House 2024-10-24 first AI national-security memorandum NSM-25. Fact sheet: Developing advanced AI systems requires large volumes of advanced chips. ... The NSM directs actions to improve the security and diversity of chip supply chains. Body: National Security Memorandum/NSM–25. URL: https://www.govinfo.gov/content/pkg/DCPD-202400945/pdf/DCPD-202400945.pdf

Commerce BIS 2022-10-07 interim final rule, Federal Register 2022-10-13 (87 FR 62186): implements necessary controls on advanced-computing integrated circuits, computer commodities that contain them, and certain semiconductor-manufacturing items. 2025-01-15 interim final rule (AI Diffusion IFR): revises the EAR to control global diffusion of the most advanced AI models and large clusters of advanced-computing ICs, to protect US national security and foreign-policy interests. NVIDIA FY26 10-K itself writes the consequence (fiscal year ended 2026-01-25): As of the end of fiscal year 2026, we were effectively foreclosed from competing in China's data center computing/compute market. Same 10-K: the 2025-01 AI Diffusion IFR was going to put global licensing on H200 / GB200 / GB300; in 2025-05 the US government announced it would withdraw and write a replacement, scope unset. That is export control changing, not an antitrust close.

Pentagon 2023 Data, Analytics, and Artificial Intelligence Adoption Strategy, released by the Deputy Secretary of Defense 2023-11-02. The public strategy links AI adoption directly to the National Defense Strategy and deterrence requirements: The NDS also describes the need for the United States to sustain and strengthen deterrence against the People’s Republic of China ... Accelerating adoption of data, analytics, and AI technologies will enable enduring decision advantage.

The White House on one side dislikes fat margins drawing blood from US clouds and manufacturing. On the other it needs this stack to sit on the East in armament. A split or a forced-open CUDA would slow its own iteration. National security over competition is a political constraint pushed from these files. Raised high, what lands is more likely a settlement, a little give on interconnect, ASICs able to attach to part of the network. Fat margins and prepayments are not touched. Antitrust slows the step and forces protection money. It does not split the machine that prints profit. 80% accelerator share is media and sell-side scope, not a DOJ relevant-market definition. The report does not treat it into a finding. No White House or Pentagon order that says "therefore do not split NVIDIA" was read. Writing "a split is hard under national security" as a signed no-split order is promoting a push to a file. The appendix does not allow it.

### 3.7 compute-platform value capture: $193.7B is seller rent. It does not match "$215B of AI hardware"

FY26 Data Center revenue of **$193.737B** is a seller-side revenue anchor. It is not a measure of all global compute spending and cannot be equated with four-cloud CapEx. Consumer devices may still experience memory and leading-edge allocation pressure without purchasing NVIDIA systems directly.

Seller-side value capture should be described using NVIDIA's own reported financials. FY26 revenue $215.9B, up 65% year on year; data center full year $193.7B, up 68%. It is not a split of four-cloud capex, and cannot be written as "the four clouds paid NVIDIA the entire $193.7B" — outside the four there are still Oracle, sovereign clouds, model firms, and enterprises. FY25 data center is another line (framework-checked $115,186M). Do not mix years with FY26 $193.7B. Q4 FY25 only says CSPs about 50% of that quarter's data-center revenue. That quarter's data center is $35,580M. There is no full-year CSP split. Seller revenue ≠ buyer capex.

The buyer end: [Volume 8](vol-08.en.md). The four clouds each report their own equipment purchases. Line items and fiscal years do not line up. They cannot be added into one calendar year.

What can be written: the four clouds are adding group-wide capex; NVIDIA FY26 data center collected $193.7B. The direction is that a slice of cloud capex becomes cabinets, then NVIDIA revenue. TrendForce puts 47% of 2026 major-CSP capex and 68% of 2027 into memory. The money flow is cloud → cabinet → NVIDIA and memory makers. Startups walk the cloud channel. The path is the same. The mix differs by firm. The report does not treat "a $1B raise puts $700–800M in Jensen's pocket" — there is no such split table. The report does not treat "four-cloud 2024 AI hardware = $215B"; that the entire $193.7B came from these four; or knock mixed-year capex against DC revenue into a "synthetic value-capture ratio." Buyer and seller line items differ. Buyers still have civil works, power, self-designed ASICs, memory, and optics.

Cloud buyers also have substantial capital capacity. Microsoft FY25 net income was **$101.832B** and PPE additions were **$64.551B**. The distinction is functional: hyperscaler cash funds buildings, power, networks, custom silicon, and third-party systems, while NVIDIA cash and supply commitments can be directed more directly toward inventory and future manufacturing capacity. Self-designed ASICs still bid for the same 3nm and HBM. Miss first silicon and, to keep cloud customers, they still have to keep ordering cabinets. Hypothesis from here: the cloud becomes a channel that distributes cabinets downstream. downstream distribution channel means that. It does not mean hundreds of thousands of Rubin cabinets already ordered. Unverified: do not forecast the year the cloud becomes a pure channel.

Phones and PCs, even if they never buy a GPU, are still absorbing residual-capacity pressure. Residual bits: [Volume 5](vol-05.en.md). That is memory collective liability, not a check they wrote to NVIDIA.

### 3.8 A fine does not change the bid; the five interrupts are not done

A fine does not change the bid. Profit, prepayments, supply commitments: [Volume 1](vol-01.en.md). The 1999 Intel comparison is in 3.9 below: that was CPU share. Today the comparison is free cash and one quarter of operating income. A-grade cells: 3.1 above.

The five interrupts: [Volume 8](vol-08.en.md). The docket: [Volume 11](vol-11.en.md). Cloud custom-chip specs: [Volume 4](vol-04.en.md). China stack: [Volume 12](vol-12.en.md). US antitrust does not save Huawei. What it would split is domestic tying and supply discrimination, not open 2nm for SMIC, and not open HBM for CXMT.

A structural split or a forced-open CUDA: what can change the rules overnight is not AMD. It is a split, forced interoperability, a ban on tied supply. A fine does not change the bid. The monitoring discipline is simple: record inquiry, complaint, formal proceeding, decision, and remedy as separate legal states; record statutory ceilings as legal boundaries rather than expected fines; and update the scenario only when the formal status changes.

### 3.9 Prepayments lock capacity. That is not tying inside a subpoena

The appendix easily writes two different things as one. One is the prepayment the central framework already confirm: 10-K original prepaid manufacturing and capacity agreements. Supply commitments $95.2B at FY26 year-end, $119.0B at Q1 FY27 end, a three-month add of $23.8B, substantially all to be paid in fiscal 2027. Official text writes locking inventory and capacity. It does not split to TSMC or CoWoS. Some agreements can be rescheduled. This is the seller using free cash it already earned (FY26 $96.575B) to bid for the next slice of material. TSMC's board answers to shareholders. A buyer with larger long-duration orders, prepayments, strong credit, high utilization, and roadmap certainty can have greater leverage over incremental capacity. Suppliers still balance diversification, geopolitics, utilization, and long-run bargaining power; no deterministic one-customer allocation rule is assumed. What is not yet written as fact: TSMC already a captive fab, High-NA bought out in bulk, Apple or Qualcomm already unable to get any leading-edge node. TSMC 2025 booked first customer 19%, second 17%. Jensen said it is already the largest customer. Concrete percentages wait for TSMC's 2026 annual report.

The other is sales conduct named in the DOJ inquiry: whether it pressed cloud vendors to buy multiple products; whether it sold networking gear at higher prices when customers wanted to mix AMD or Intel chips. That is the inquiry direction of tying and supply discrimination. It needs contracts, mail, and customer testimony. On the public record, do not add these two into one sentence that "NVIDIA has already completed the tying under inquiry by using prepayments." Prepayments lock foundry and inventory. The inquiry asks about sales terms to clouds and networking. The former is in the 10-K supply commitments. The latter is in Reuters and Bloomberg inquiry reporting. The appendix keeps two cells. It does not weld them into one.

What can interrupt prepayments is not a $21.6B statutory ceiling. What can interrupt is: the West binds prepayments so TSMC cannot recognize only one buyer; or a split, a forced-open CUDA, a ban on capacity discrimination, opening sales terms and the capacity lock together. The inquiry stops at questionnaires and subpoena reporting. The opening has not happened. Supply commitments adding $23.8B in three months is the cell already done in 2026. When the appendix tracks, supply commitments walk A grade (company disclosure, still must go back to the 10-K). Tying allegations walk the procedure cell (inquiry yes, complaint no). Do not use one cell to prove the other.

Intel 1999 revenue $29,389M, net income $7,314M, gross margin 59.7%, is the historical anchor the central framework uses for comparison. That was CPU share. Foundry was in-house. Customers could dual-source. There was no today's slice of CoWoS / HBM / 2nm first silicon that has to be bid with a hundred-billion prepayment. historical stress-test material appendix title writes "historical data tracker for the global semiconductor and compute market," yet has no WSTS, no Intel row, no Cisco 2000. Share will break, because the next slice of capacity is not something one firm can lock with prepayments. Today the comparison is not share. It is one year of free cash $96.6B, one quarter of operating income $53.5B, and gross margin back near 75%. That is strong seller-side economics, not proof of a permanent monopoly. Historical switching, customer diversification, and supplier incentives remain part of the mechanism. If the appendix only chases "80% accelerator share," it treats media scope as a DOJ relevant market and misses the cell that can actually lock the next slice of material: prepayments and free cash.

## 4. Scenarios, counterarguments, and testable indicators

The tracking list this appendix suggests uses only existing scopes. It does not add unverified targets. Scenarios are branches, not probabilities already issued.

Scenario 1: France issues a statement of objections. The public record walks from "near the end" to "already accused." NVIDIA enters reply and oral hearing. The Authority's board then rules. This scenario changes procedure. It does not automatically change the bid. Until a statement of objections lands, $21.6B is still only the L464-2 ceiling. Testable: whether communication des griefs or a sanction decision appears on the Autorité de la concurrence site.

Scenario 2: France closes without a statement of objections. The other exit from "near the end" is to shut it. This scenario also cannot be written as "antitrust has already failed" — the US inquiry is still there, EU questionnaires are still there. Testable: whether a clôture / no further action-class close appears on the site.

Scenario 3: DOJ files a formal complaint. The public record walks from inquiry to *United States v. NVIDIA*. The tools that can change the rules overnight only then enter court: a split, an injunction, forced interoperability, a ban on tied supply. Subpoenas and questionnaires themselves are not those tools. Testable: whether a Complaint, Competitive Impact Statement, or Proposed Final Judgment appears on justice.gov, and whether the defendant is NVIDIA.

Scenario 4: The inquiry keeps dragging. National-security constraints stay. This is the state the 2026-08-26 public record already presents. Supply commitments already at $119.0B. While gross margin stays in the 71.1%–75.0% band, prepayments keep locking the next generation. If a fine finally issues and does not touch structure, it is a cost. Testable: whether supply commitments keep rising; whether gross margin leaves the band; whether the 10-K still writes China's data center as "effectively foreclosed."

Counter 1: cloud buyers are large enough (Microsoft Intelligent Cloud $106,265M; 2025 mixed-year four-cloud group capex already about $354.0B) to exert buyer-side pricing pressure through volume. platform value capture need not collapse into a single revenue or margin line. The condition for this counter is that buyers, selling cabinets, can outbid 71.1%–75.0%, or that joint prepayments are large enough that TSMC cannot recognize only one buyer. What is visible now is an each-for-itself sum, not joint prepayments. Counter 2: CSPs were only about 50% of Q4 FY25 data center. Sovereign and enterprise self-build dilute "the four clouds decide everything." This counter weakens "the entire $193.7B came from the four clouds." It does not weaken "$193.7B is NVIDIA FY26 Data Center revenue and a seller-side value-capture anchor." Counter 3: the inquiry itself has already changed conduct — Run:ai open-sourced, a little give on interconnect, ASICs able to attach to part of the network — without waiting for a complaint. if conduct converges, write it into next quarter's product docs and supply terms. Do not back out "tying is already undone" from "an inquiry exists." Counter 4: national security can also demand a split the other way, so a single vendor does not become a single point of failure. Public files now write supply-chain security and diversity. There is no order that says "therefore split NVIDIA." Writing this counter as a policy that already happened is not allowed.

Indicators to check and update year by year (or fiscal year by fiscal year):

1. NVIDIA total revenue, data-center revenue, GAAP gross margin, operating income, free cash, supply commitments. Compare FY26 215,938 / 193,737 / 71.1% / 130,387 / 96,575 / $95.2B, and $119.0B at Q1 FY27 end.
2. Four-cloud cash-flow equipment purchases (Microsoft Additions to property and equipment; Amazon net; Alphabet purchases; Meta purchases and company figure apart). Compare mixed-year $211.9B–$213.9B and $354.0B–$356.5B. The report does not treat "AI hardware $215B" again.
3. DOJ: whether *United States v. NVIDIA* appears on justice.gov. If not, keep writing "inquiry yes, complaint no."
4. France: whether a statement of objections or a close has appeared. If not, keep writing "near the end, no statement of objections issued."
5. EU: whether a formal 101/102 opening, statement of objections, or fine has appeared. If not, keep writing "questionnaires sent, no formal opening." Run:ai stays unconditionally approved. T-15/25 is a jurisdiction suit, tracked separately.
6. 10% product: only the statutory ceiling times the annual report, marked "not a fine." Do not copy this line onto the US side.
7. National-security files: whether NSM, BIS, and DoD strategy still write advanced chips and large clusters as license items; whether the 10-K China data-center sentence is still there. The report does not treat them as a "do-not-split order."
8. TSMC revenue, gross margin, HPC share, first-customer share, packaging-and-test share. Compare 2025: HPC 58%, first customer 19%, packaging and test a bit over 10%. CoWoS monthly 13k→130k and a 60% lock do not enter A grade.
9. Hynix revenue, operating margin, whether HBM revenue still writes "more than doubled in a year." Do not put operating profit in the gross-margin column.
10. Software: whether any SaaS with a reported gross margin is moving toward either 85% or 55%. Neither end has a sample now.
11. Nuclear, interconnection, algorithm cost, BOM: all stay D grade. Return to [Volume 13](vol-13.en.md), [Volume 6](vol-06.en.md), [Volume 2](vol-02.en.md). This volume did not re-check contracts and papers.

The counter that printing engineering BOMs and 10-Ks on one "evidence appendix" creates a precision illusion. The right method is split books — finance one, engineering one, regulatory procedure one, claims one. This volume already grades A/B/C/D and puts regulatory procedure in its own sections. That is accepting this counter.

## 5. Gaps and what cannot be treated as fact

- This volume did not audit 10-K / 20-F / TSMC and Hynix annual-report originals page by page. Verified point estimates come from IR / Exhibit 99.1 / official sentences already copied in the central framework. Do not claim "audited by this volume."
- Older Microsoft period/range estimates have been replaced by the current point figures and accounting scope. Azure above $75B is a company verbal magnitude, not a cash-flow-statement cell.
- AWS and Google Cloud lack exact segment revenue. Amazon $620.1B and Alphabet $349.7B are group totals. They cannot be cross-compared with NVIDIA data center.
- $215B and $45B~$55B depreciation cannot be closed inside this volume. The mixed-year addable can only be written to $211.9B–$213.9B (2024) and $354.0B–$356.5B (2025). 2026 guidance lacks Microsoft. $670–750B cannot be added.
- Putting Hynix operating profit in the gross-margin column is a structural error in historical stress-test material table. "About $25B" is a conversion. Official won is KRW 32.7657T.
- BOM, MFU, training dollars, CoWoS capacity, and nuclear MW are not SEC financial facts and not antitrust findings.
- Under the title "global semiconductor and compute market" there is no WSTS, IDC, or any third-party market total. An industry-size time series is missing.
- A DOJ complaint, settlement, Mellanox split, forced-open CUDA: have not happened. Subpoena reporting and the company's denial coexist. Follow DOJ paper.
- A French statement of objections, a French or EU fine: have not happened. "Near the end" is not "about to issue charges."
- "About to issue 10% of annual turnover" — that is a statutory ceiling. The US Sherman Act has no such clause.
- White House / Pentagon already issued a document forbidding a split: no such file. That a split is hard under national security is a push.
- "Four-cloud 2024 AI-hardware capex = $215B"; "the entire $193.7B came from these four"; knocking mixed-year capex against DC revenue into a synthetic value-capture ratio.
- 80% accelerator share: media and sell-side scope, not a DOJ relevant-market definition.
- "A $1B raise puts $700–800M in Jensen's pocket": no split table.
- Any forward numerical extrapolation: unverified. Do not treat as first-party fact.

If those five are not done, the line walks past half of the scarce slice. The window is the few years before the next first-to-market node is locked by commitments. What the appendix can do is stop inquiries, statutory ceilings, and mixed-year sums from inflating, in the next citation round, into remedies that already happened and AI-hardware bills that were already audited.

Future updates should change only the indicator whose public status has changed. DOJ inquiry, French competition procedure, EU questionnaires, Run:ai merger clearance, and T-15/25 jurisdiction litigation remain distinct legal states. NVIDIA Data Center revenue and hyperscaler equipment purchases remain separate accounting objects, and supply commitments should follow company filings rather than media inference. Scenario weights should change only when these monitored states materially change.
