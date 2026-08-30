# Part I · Chapter 9: Semiconductor Supply-Chain Resilience — Equipment, Materials, and Geographic Redundancy

## 1. Resilience is a system-continuity problem

Frontier AI supply security cannot be reduced to the location of one fab or the nationality of one chip designer. The relevant test is whether the full industrial chain can keep producing, qualifying, servicing, and scaling through disruption.

The physical supply chain of a frontier AI system includes at least:

- lithography / deposition / etch / metrology equipment;
- silicon wafers and high-purity materials;
- leading-edge foundry;
- HBM;
- advanced packaging / substrates;
- testing;
- data-center power / cooling.

Supply security for an accelerator designer is therefore not determined by chip design alone. Multiple industrial layers must be simultaneously available.

## 2. ASML shows that equipment itself is a system-level capability

ASML's 2025 Annual Report reports **48 EUV lithography systems sold** during the year. By the end of 2025, customers had run more than **400,000 wafers** on High-NA systems while qualification continued.[^1]

On **July 15, 2026**, ASML announced the first High-NA EUV use in high-volume logic production on select Intel 18A layers for Panther Lake.[^8] That moves High-NA from a qualification-only phase into an observed HVM production milestone, while still not implying that High-NA has become universal across leading-edge logic.

The strategic constraint in advanced lithography cannot therefore be captured by a single-machine price.

The relevant variables are:

- system availability;
- throughput;
- imaging / overlay performance;
- customer qualification;
- field service;
- long-term coordination across optics / source / stage / metrology.

High-NA matters primarily as a process-roadmap and industrial-maturity path, not as a media-reported price tag.

## 3. A fab cannot exist independently of its supplier ecosystem

Leading-edge manufacturing depends on equipment installation, spare parts, software, process recipes, materials, metrology, and long-duration field service.

Even if two regions both contain fab buildings, their effective capacity will not be equivalent if supplier density, engineering talent, qualification cycles, tool service, and material stability differ.

This report therefore defines supply-chain independence as **system-level continuity**, not simply "a fab exists on the map."

### 3.1 Upstream Continuity: equipment, software, spare parts, and field service are separate constraints

The existence of a domestic fab does not automatically mean that capacity expansion is independent of external upstream supply.

ASML's public export-control statements provide an auditable boundary:[^2][^3]

- sales of EUV systems to China are already restricted;
- the most advanced immersion DUV systems require Dutch export licences;
- the 2024 U.S. update expanded restrictions to additional advanced semiconductor-manufacturing technologies, including metrology and software.

This does **not** support the claim that every Chinese fab would stop operating under a supply interruption. ASML itself notes that the controls focus on advanced technologies / specific fabs rather than every system.

The variables that matter are:

> **critical equipment availability + software/licensing + spare parts/field service + materials qualification**

These variables determine whether new capacity can ramp on schedule, whether existing lines can sustain yield, and whether process generations can continue advancing.

"Memory capacity is expanding" and "the memory supply chain is fully autonomous" are therefore different propositions.

## 4. Material qualification is an often-underestimated time cost

Advanced nodes are highly sensitive to contamination, particles, uniformity, defect density, and long-term stability.

Changing a materials supplier is not a normal procurement switch. Even chemically similar materials can require requalification and renewed learning across yield, tool recipes, and reliability.

The relevant materials constraint is therefore not an unsupported market-share statistic. It is:

> **Does a qualified alternative supplier exist, and how long would switching take?**

## 5. TSMC's geographic expansion shows that redundancy is real—and that the core cluster cannot be copied instantly

TSMC's 2025 Annual Report and 2026 Arizona updates show:[^4][^9]

- the first Arizona fab entered N4 high-volume production in **4Q24**;
- the second Arizona fab structure is complete and targets **3 nm volume production in 2H27**;
- construction of the third Arizona fab began in 2025, with N2 / A16 planned and volume production targeted around the end of this decade;
- a fourth fab and the first advanced-packaging facility entered early construction activity in 2026;
- the current Arizona plan has expanded to **six logic fabs + two advanced-packaging facilities + an R&D center**;
- the first Kumamoto fab in Japan entered volume production by the end of 2024, while the second fab plan includes 3 nm;
- the Dresden project in Germany targets automotive / industrial specialty technologies;
- Taiwan continues building 2 nm and more advanced capacity together with advanced packaging.

Geographic diversification is therefore a real trend, and it is extending from logic fabs into packaging and R&D.

It is still not the same as reproducing the Taiwan cluster overnight.

Different regions continue to differ in node mix, product mix, packaging, workforce, supplier density, and power/water conditions.

## 5A. Three kinds of redundancy must remain separate: Geographic, Supplier, and Technology

A TSMC fab in another country mainly increases **geographic redundancy**.

It does not automatically create:

- foundry supplier redundancy;
- EDA / equipment redundancy;
- HBM supplier redundancy;
- packaging supplier redundancy;
- design portability.

At least three forms of resilience therefore need to be separated.

### Geographic Redundancy

The same technology / supplier operates manufacturing capacity across multiple regions.

This reduces single-region disruption risk while potentially retaining dependence on the same company, process ecosystem, or key equipment base.

### Supplier Redundancy

The same workload / design can move between two or more qualified suppliers.

That requires:

- process portability;
- design requalification;
- packaging compatibility;
- yield / reliability validation;
- software / firmware adaptation.

This is materially harder than geographic expansion by the same supplier.

### Technology Redundancy

If one equipment class, process, or architecture is constrained, another technical path can still deliver acceptable performance / cost.

Therefore:

> **geographic diversification ≠ true second source ≠ technology independence**

For frontier-AI supply security, the highest-value resilience comes from improving all three forms of redundancy rather than merely making the fab map more geographically distributed.
## 6. Government subsidies reduce the cost of redundancy; they do not create instant independence

The U.S. Department of Commerce final CHIPS award for TSMC Arizona includes up to **US$6.6B of direct funding** supporting three leading-edge fabs. Final NAPMP advanced-packaging awards total **US$1.4B**, while Amkor's Arizona advanced-packaging/test facility received up to **US$407M of direct funding**.[^5][^6][^7]

These programs directly support a broader conclusion:

> **Strategic redundancy requires additional public capital to offset geographic duplication, cluster formation, and early-utilization risk.**

Subsidies cannot instantly reproduce decades of yield learning, supplier qualification, and engineering density. They can accelerate capacity formation, but they are not equivalent to immediate supply-chain independence.

## 7. Why redundancy inherently costs more

Greater resilience often requires:

- duplicated fabs / packaging lines;
- duplicated inventories;
- spare / reserve capacity;
- regional supplier qualification;
- lower initial utilization;
- government incentives;
- additional engineering / compliance overhead.

The supply chain can therefore move from:

> **lowest-cost global optimization**

toward:

> **higher-cost strategic redundancy**

This is not simply an efficiency failure. It is a changed cost function under a changed security objective.

## 8. AI demand accelerates geographic restructuring

Demand for leading-edge logic, HBM, packaging, and power has pushed advanced manufacturing beyond the normal commercial cycle toward strategic infrastructure.

TSMC's 2025 Annual Report links Arizona expansion to strong multi-year AI-related demand, while U.S. CHIPS programs treat AI/HPC as important use cases for leading-edge and advanced-packaging investment.[^4][^5][^6]

The AI-infrastructure cycle and industrial-policy cycle are therefore increasingly overlapping.

## 9. Geographic redundancy does not mean every layer is localized

A regional supply stack has to be tested across:

- equipment / service;
- materials;
- foundry;
- HBM;
- packaging / substrate;
- testing;
- power / water;
- workforce;
- customer qualification.

Localizing one layer reduces dependency in that layer only. It does not automatically close the other risks.

This is why the frontier-system resilience of China, the United States, Europe, or Japan cannot be summarized with one localization percentage.

## 10. China localization and Western reshoring face the same system problem

China's localization of equipment, materials, foundry, memory, and packaging and the U.S./European/Japanese reshoring or friend-shoring programs pursue different strategic objectives.

They nevertheless face the same engineering requirement:

> **performance + yield + scale + qualification + cost must all work at the same time.**

The existence of one product is not system closure. Real substitution must be sustainable at production scale, reliability, and long-duration service.

## 11. Geopolitical fragmentation can increase global investment while lowering single-system efficiency

If the world develops two or more relatively separate semiconductor / AI system ecosystems, the result can include:

- repeated fab investment;
- repeated packaging investment;
- duplicated software/runtime;
- higher strategic inventory;
- lower cross-region fungibility;
- more policy-driven capacity.

Fragmentation does not necessarily reduce global semiconductor CapEx. It can instead produce **more duplicated construction, lower utilization efficiency inside each individual system, and greater resilience**.

## 12. What qualifies as real supply-chain resilience

This report does not define complete self-sufficiency as the only valid objective.

More useful tests are:

1. have single points of failure been reduced?
2. does each critical layer have a qualified second source?
3. how long does system-level recovery take after disruption?
4. does regional capacity have sufficient power, workforce, and supplier support?
5. can the cost of redundancy still be covered by the economics of the final workload?

The real competition is therefore not which country produces every input domestically, but:

> **who can maintain the highest level of system continuity at an acceptable cost when a critical disruption occurs.**

## 13. Current read

As of 2026, public evidence supports a relatively clear direction:

- core leading-edge technologies remain highly concentrated;
- High-NA EUV has moved from qualification into real HVM logic production;
- geographic redundancy is accelerating and increasingly covers logic + packaging + R&D;
- supplier redundancy is improving more slowly than geographic redundancy;
- government participation has increased materially;
- advanced packaging is now an explicit policy and investment object;
- redundancy raises resilience while also raising capital and operating cost;
- overseas fab expansion still needs time to reproduce supplier, workforce, packaging, and infrastructure ecosystems.

The semiconductor supply chain of the next decade is therefore more likely to consist of **highly concentrated core technologies + greater regional redundancy + higher strategic inventories + greater public-capital participation** than to return quickly to a fully dispersed and fully substitutable global market.
## References

[^1]: ASML, 2025 Annual Report and Strategy & Stories, EUV / High-NA roadmap and system shipments, https://www.asml.com/en/investors/annual-report/2025
[^2]: ASML, 2023 statement on Dutch export-control regulations, EUV and advanced immersion DUV licensing, https://www.asml.com/en/news/press-releases/2023/statement-regarding-export-control-regulations-dutch-government
[^3]: ASML, 2024 statement on updated export restrictions covering additional advanced manufacturing technologies, metrology, and software, https://www.asml.com/en/news/press-releases/2024/asml-expects-impact-of-updated-export-restrictions-to-fall-within-outlook-for-2025
[^4]: TSMC, 2025 Annual Report, Arizona/Japan/Germany/Taiwan manufacturing footprint and AI-related demand context, https://investor.tsmc.com/static/annualReports/2025/english/index.html
[^5]: U.S. Department of Commerce, TSMC Arizona CHIPS final award, 2024-11, https://www.commerce.gov/news/press-releases/2024/11/biden-harris-administration-announces-chips-incentives-award-tsmc
[^6]: U.S. Department of Commerce, US$1.4B NAPMP advanced-packaging final awards, 2025-01, https://www.commerce.gov/news/press-releases/2025/01/us-department-commerce-announces-14-billion-final-awards-support-next
[^7]: U.S. Department of Commerce, Amkor Arizona advanced-packaging and test award, 2024-12, https://www.commerce.gov/news/press-releases/2024/12/biden-harris-administration-announces-chips-incentives-award-amkor
[^8]: ASML, “High NA EUV reaches new readiness milestone with first high-volume Logic product,” 2026-07-15, Intel 18A select layers / Panther Lake HVM, https://www.asml.com/en/news/press-releases/2026/high-na-euv-reaches-new-readiness-milestone
[^9]: TSMC Arizona, current project milestones and planned manufacturing footprint, 2026, https://www.tsmc.com/static/abouttsmcaz/index.htm ; TSMC 2026 AGM minutes, second-fab HVM timing and Arizona expansion context, https://investor.tsmc.com/sites/ir/shareholders-meeting/2026-06-04/2026AGM_Minutes_wmn.pdf
