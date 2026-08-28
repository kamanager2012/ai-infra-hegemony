# Part I · Chapter 9: Global Semiconductor Supply Chains and Manufacturing Redundancy

> **Publication-layer chapter.** Based primarily on [Volume 34](../vol-34.en.md), with factual boundaries reinforced by public material from ASML, TSMC, and CHIPS for America. This chapter does not use unverified equipment-price claims or unsupported materials-share tables. It focuses on why "building another fab" is not equivalent to replicating a complete leading-edge supply chain, and why strategic redundancy increases both resilience and cost.

## 1. Frontier AI depends on an industrial chain spanning companies and countries

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

ASML's 2025 Annual Report reports **48 EUV lithography systems sold** during the year. Its High-NA TWINSCAN EXE platform remained in customer qualification toward high-volume manufacturing.

ASML stated that by the end of 2025 customers had run more than **400,000 wafers** on High-NA systems while work continued toward high-volume-manufacturing qualification.

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

## 4. Material qualification is an often-underestimated time cost

Advanced nodes are highly sensitive to contamination, particles, uniformity, defect density, and long-term stability.

Changing a materials supplier is not a normal procurement switch. Even chemically similar materials can require requalification and renewed learning across yield, tool recipes, and reliability.

The relevant materials constraint is therefore not an unsupported market-share statistic. It is:

> **Does a qualified alternative supplier exist, and how long would switching take?**

## 5. TSMC's geographic expansion shows that redundancy is real—and that the core cluster cannot be copied instantly

TSMC's 2025 Annual Report shows:

- the first Arizona fab entered **4 nm volume production in 4Q24**;
- the second Arizona fab is planned for 3 nm and more advanced technologies;
- construction of the third Arizona fab began in 2025, alongside announced plans for additional fabs, advanced-packaging facilities, and R&D expansion;
- the first Kumamoto fab in Japan entered volume production by the end of 2024, while the second fab plan includes 3 nm;
- the Dresden project in Germany targets automotive / industrial specialty technologies;
- Taiwan continued building Hsinchu / Kaohsiung 2 nm capacity and investing in leading-edge and advanced-packaging facilities.

Geographic diversification is therefore a real trend. It is not the same as reproducing the Taiwan cluster overnight.

Different regions continue to differ in node mix, product mix, packaging, workforce, supplier density, and power/water conditions.

## 6. Government subsidies reduce the cost of redundancy; they do not create instant independence

The U.S. Department of Commerce final CHIPS award for TSMC Arizona includes up to **US$6.6B of direct funding** supporting three leading-edge fabs.

Final NAPMP advanced-packaging awards total **US$1.4B**, while Amkor's Arizona advanced-packaging/test facility received up to **US$407M of direct funding**.

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

TSMC's 2025 Annual Report links Arizona expansion to strong multi-year AI-related demand, while U.S. CHIPS programs treat AI/HPC as important use cases for leading-edge and advanced-packaging investment.

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

## 12. What constitutes real Supply-Chain Resilience

This report does not define complete self-sufficiency as the only valid objective.

More useful tests are:

1. have single points of failure been reduced?
2. does each critical layer have a qualified second source?
3. how long does system-level recovery take after disruption?
4. does regional capacity have sufficient power, workforce, and supplier support?
5. can the cost of redundancy still be covered by the economics of the final workload?

The real competition is therefore not which country produces every input domestically, but:

> **who can maintain the highest level of system continuity at an acceptable cost when a critical disruption occurs.**

## 13. Current judgment

As of 2026, public evidence supports a relatively clear direction:

- core leading-edge technologies remain highly concentrated;
- geographic redundancy is accelerating;
- government participation has increased materially;
- advanced packaging is now an explicit policy and investment object;
- redundancy raises resilience while also raising capital and operating cost;
- overseas fab expansion still needs time to reproduce supplier, workforce, packaging, and infrastructure ecosystems.

The semiconductor supply chain of the next decade is therefore more likely to consist of **highly concentrated core technologies + greater regional redundancy + higher strategic inventories + greater public-capital participation** than to return quickly to a fully dispersed and fully substitutable global market.

## Key public sources

- ASML 2025 Annual Report: https://www.asml.com/en/investors/annual-report/2025
- ASML 2025 Strategy & Stories — EUV / High-NA roadmap: https://www.asml.com/en/investors/annual-report/2025/strategy-and-stories
- TSMC 2025 Annual Report — Arizona/Japan/Germany/Taiwan footprint: https://investor.tsmc.com/static/annualReports/2025/english/index.html
- U.S. Department of Commerce — TSMC Arizona CHIPS final award: https://www.commerce.gov/news/press-releases/2024/11/biden-harris-administration-announces-chips-incentives-award-tsmc
- U.S. Department of Commerce — US$1.4B NAPMP advanced-packaging awards: https://www.commerce.gov/news/press-releases/2025/01/us-department-commerce-announces-14-billion-final-awards-support-next
- U.S. Department of Commerce — Amkor Arizona advanced-packaging award: https://www.commerce.gov/news/press-releases/2024/12/biden-harris-administration-announces-chips-incentives-award-amkor
