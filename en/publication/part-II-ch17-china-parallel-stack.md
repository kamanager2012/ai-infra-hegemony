# Part II · Chapter 17: China's Parallel Stack — Production-Grade Substitution vs. Autonomous Frontier Closure

## 1. The analytical error is collapsing three different thresholds into one

China's technology position cannot be represented by a single localization rate.

Three distinct questions have to remain separate:

1. **Can domestic consumer-computing systems ship at meaningful scale?**
2. **Can PC / workstation systems sustain software compatibility, performance, and commercial scale?**
3. **Can a frontier AI stack operate production workloads and continue advancing when critical external inputs are constrained?**

Evidence from one threshold does not close another. A strong smartphone supply chain is not proof of frontier-AI closure; frontier-AI constraints are not proof that China lacks semiconductor substitution capacity.

For frontier AI, two separate tests are required:

> **Production-Grade Parallel Stack:** can the stack run real workloads with acceptable performance, scale, portability, supply continuity, reliability, utilization, and economics?

> **Autonomous Frontier Closure:** can that stack keep scaling across generations when critical external manufacturing, equipment, materials, software, or service inputs are constrained?

The distinction is strategic. Production-grade substitution can become economically important before full autonomous closure exists.

## 2. Consumer computing: commercial substitution can precede manufacturing autonomy

Smartphones and parts of consumer computing can form a more complete domestic chain because they can draw on local SoCs, foundries, LPDDR/NAND, packaging, device manufacturing, operating-system/application ecosystems, and large domestic demand.

TSMC's 2025 platform mix still shows smartphone at **29%** of annual platform revenue and HPC at **58%**.[^1]

### 2.1 Shipment scale is broader than one vendor

Counterpoint Research's 2026 Q1 global smartphone AP-SoC shipment shares show:[^2]

- UNISOC: **14%**;
- HiSilicon: **4%**.

If commercial scale is measured by actual smartphone-SoC shipments, domestic supply is therefore not limited to Huawei.

Huawei / HiSilicon's more defensible distinction is that its **premium in-house device + SoC + software/ecosystem vertical loop is more mature**, not that it is the only domestic vendor with shipment scale.

Xiaomi has also moved beyond a pure demonstration stage. Xinhua reported in May 2025 that XRing O1 had entered mass production in the Xiaomi 15S Pro and Pad 7 Ultra.[^3] Reuters reported in August 2026 that O1 had powered **more than 1M devices**, while the next-generation O3 continues on TSMC 3 nm with projected initial device shipments of 200k–300k units.[^4]

The claim that Xiaomi has only "200k–300k scraps of capacity" or that the program is merely a branding exercise therefore does not enter the fact layer.

A better judgment is:

> **Xiaomi has achieved real production deployment, while multi-generation scale, modem/system integration, foundry dependency, and sustained shipment share still require validation.**

UNISOC represents a different commercial loop: much larger shipment scale in mass-market / entry-5G devices without proving premium-flagship system equivalence.

### 2.2 Design origin is not manufacturing closure

One additional supply-chain discipline is required here:

> **"Domestic design" does not mean "manufacturing autonomy," and shipment share cannot substitute for foundry continuity.**

UNISOC is a fabless IC-design company. Its public product materials confirm that multiple current 5G SoCs use **6nm EUV**; the official M6870 page goes further and explicitly identifies **TSMC 6nm EUV**.[^19] UNISOC / Spreadtrum also has a long first-party manufacturing history with TSMC: in 2011, TSMC disclosed that a Spreadtrum 40nm baseband processor had entered initial production at TSMC Fab 12.[^20]

Those observations do **not** support the stronger claim that "all UNISOC products are manufactured by TSMC." The T9100 official page, for example, confirms a **6nm process** but does not itself identify the foundry.[^21] The safe conclusion is therefore:

> **UNISOC's 14% smartphone AP-SoC shipment share proves real commercial design and shipment scale, but it does not prove domestic foundry closure. Public product and historical supply-chain evidence show TSMC is an important manufacturing dependency, so foundry continuity must be evaluated as a separate gate.**

The Xiaomi XRing case is more direct: the Reuters source already cited in this chapter explicitly reports TSMC manufacturing cooperation.[^4] Xiaomi's in-house SoC program is therefore also a case where design capability is real but manufacturing autonomy cannot be inferred from the design origin.

This changes the consumer-computing test. Any future "domestic SoC share" should be decomposed into at least:

1. **design origin**;
2. **foundry identity / process continuity**;
3. **packaging / memory dependency**;
4. **exposure to external licensing, service, or equipment rules**;
5. **multi-generation manufacturing continuity**.

The January 2025 U.S. BIS foundry due-diligence rule did broaden licensing and due-diligence requirements for front-end foundries / packaging companies handling **certain advanced-computing ICs**, and introduced the Approved / Authorized IC Designer framework; the relevant advanced-node definition includes 16/14nm-and-below or non-planar logic.[^22] But this cannot be simplified into "all PRC-designed smartphone SoCs below 16/14nm automatically require a license." Applicability depends on EAR classification, performance/transistor-count conditions, designer status, destination, and transaction structure.

The defensible risk statement for UNISOC / Xiaomi is therefore:

> **External-foundry dependence increases supply-continuity and policy exposure, but without product-specific EAR classification and licensing evidence it cannot be rewritten as an already-occurring or inevitable cutoff.**

Consumer parallel-supply capability should therefore be evaluated as its own layer—not used as proof for or against frontier-AI closure.

## 3. PCs / workstations: compatibility and scale are the binding tests

PCs, workstations, and general computing require CPU/GPU hardware, DDR5, professional software, drivers/tooling, desktop ecosystems, and developer compatibility.

It is also inaccurate to describe the domestic PC CPU/GPU segment as "blank."

Loongson's current official portfolio includes desktop/general-purpose CPUs such as the 3A6000 and 3B6000.[^5] Moore Threads publicly sells the MTT S80 gaming GPU.[^6]

These facts establish **real products and deployable domestic PC/graphics systems**.

They do not establish:

- mainstream consumer-PC shipment share approaching Intel/AMD/NVIDIA;
- equivalent coverage of professional software / games;
- equivalent performance-per-watt, driver maturity, developer ecosystem, or supply scale.

A more accurate description is:

> **real products and domestic ecosystems exist, while mainstream scale, compatibility, and system economics remain the closure barriers.**

## 4. Frontier AI is a system-closure problem

Frontier AI requires multiple advanced layers to work simultaneously:

- advanced accelerators;
- HBM-class memory;
- advanced packaging;
- high-speed scale-up / scale-out interconnect;
- compiler/runtime;
- distributed training;
- rack-scale deployment;
- data-center power.

A breakthrough in one layer does not automatically create an equivalent system.

An accelerator without HBM, hardware with very high migration cost, or a cluster with weak utilization/interconnect scaling can all produce materially weaker system economics.

A domestic chip being able to run a model is therefore not sufficient evidence of frontier substitution.

## 5. Ascend / CANN should be judged by system completeness, not peak-card metrics

The key value of a domestic accelerator stack is not the peak FLOPS of one generation.

It is whether compiler/runtime, framework adaptation, distributed communication, deployment tooling, and production-workload feedback form a closed loop.

The preferred observables include:

- large-cluster utilization;
- compiler stability;
- operator completeness;
- framework compatibility;
- failure recovery;
- multi-generation compatibility;
- production deployment scale.

Because some specific Ascend/CANN performance and migration-efficiency figures currently come primarily from secondary sources, this chapter does not upgrade unverified parameters into confirmed facts.

## 6. Memory: conventional scale and frontier HBM are different thresholds

CXMT's **May 27, 2026 STAR Market registration prospectus** discloses DDR and LPDDR products. The company subsequently began trading on Shanghai's STAR Market on **July 27, 2026**.[^7][^18]

Full-text searches of the relevant public offering / registration materials for `HBM` and the Chinese term for high-bandwidth memory do not provide evidence sufficient to confirm a volume HBM product line. The evidence therefore supports only a narrow conclusion:

> **Current public offering and product materials are insufficient to confirm a volume-deliverable HBM product line.**

This does **not** prove that the company has no HBM R&D. Listing changes the company's capital-market and financing state; it does not by itself cross the HBM, advanced-packaging, or frontier-system technical gates.

To move HBM from possible R&D into frontier-system supply, the evidence would need to include official products, customer qualification, volume production, bandwidth/capacity, and packaging integration.

The same prospectus also requires strict separation between project investment and planned offering proceeds. For the DRAM technology-upgrade project, **RMB18.0B total investment** and **RMB13.0B planned offering proceeds** are different denominators.[^7]

DDR/LPDDR supply expansion and HBM-class memory closure therefore have to remain separate.

### 6.1 Conventional DRAM / NAND can improve before HBM closure

CXMT's current official product page discloses DDR5 chips up to **8000 Mbps**, with 16Gb/24Gb densities and server/workstation/PC module coverage including RDIMM/MRDIMM.[^8]

YMTC officially describes itself as a 3D NAND IDM and discloses its Gen5/Xtacking 4.0 product path together with raw NAND, embedded memory, client SSD, and enterprise SSD portfolios.[^9]

These facts support a narrower conclusion:

> **consumer/general-purpose memory resilience can improve before frontier HBM closure is achieved.**

Front-end manufacturing for conventional DRAM and NAND is not the same physical pool as TSMC leading-edge logic foundry capacity.

But HBM-class AI systems can reintroduce advanced-logic/base-die, advanced-packaging, and accelerator-integration dependencies. Micron, for example, has publicly disclosed a TSMC partnership for manufacturing HBM4E base logic dies.[^10]

"Conventional memory can bypass TSMC logic foundry" and "the frontier AI memory stack is independent of TSMC" are therefore different propositions.

### 6.2 Revenue share and shipment share are different denominators

CXMT's prospectus, citing Omdia, provides an auditable metric: based on **2025 Q2 DRAM revenue**, CXMT held approximately **3.97% global share**, ranking fourth globally and first in China.[^11]

The claim that "CXMT already has 8% of global DRAM" therefore does not enter the fact layer.

YMTC's latest institutional metric uses a different denominator. Counterpoint Research's Q2 2026 Memory & Storage Tracker places YMTC at roughly **14% of NAND shipments**, ranking third globally.[^12] The same research firm's Q1 2026 **13%** figure is a NAND **revenue share**.[^13]

Those two percentages cannot be turned into one continuous time series because their denominators differ.

What they support is a narrower conclusion:

> **China's conventional DRAM / NAND presence in global supply has risen materially, but share growth does not by itself prove HBM, leading-edge logic, or frontier-system closure.**

Claims such as "capacity will double by 2027" or specific Phase-III monthly wafer output remain B/C-grade background unless they are disclosed directly by the company or another formal first-party source.

### 6.3 Storage resilience is broader than NAND

AI data-center storage also includes nearline HDD.

Public industry research shows that global nearline / mass-capacity HDD supply remains highly concentrated in Seagate, Western Digital, and Toshiba.

Stronger domestic NAND / SSD capability therefore cannot be rewritten as "the entire storage stack is domestically closed."

AI has also not simply eliminated HDD. Mass-capacity / cold-storage demand remains real, while QLC nearline SSD is accelerating substitution for selected workloads.

## 7. Foundry revenue share is not a frontier-AI capability metric

TrendForce's 1Q26 foundry revenue-share estimates are approximately:[^14]

**Table 17.1 — Global foundry revenue share, 1Q26 (TrendForce)**

| Foundry | Revenue share |
|---|---:|
| TSMC | 72% |
| Samsung Foundry (excluding System LSI) | 6.5% |
| SMIC | 5.1% |

**Source:** TrendForce, 2026-06-12.[^14]  
**Note:** These are foundry revenue shares, not advanced-node yield, AI wafer capacity, or frontier-system capability.

These are foundry **revenue shares**, not advanced-node yield, AI wafer capacity, or frontier-system delivery capability.

A frontier AI parallel supply stack requires more than logic dies. It also needs advanced packaging, substrates, HBM integration, yield, high-volume qualification, and power.

Node progress is one necessary condition, not the whole system.

## 8. Algorithmic efficiency can relax hardware constraints without closing the stack

The DeepSeek-V3 Technical Report shows that algorithmic and architectural design can materially lower the hardware required per unit of capability.

The paper reports **2.664M H800 GPU-hours for pre-training** and **2.788M H800 GPU-hours for full formal training**.[^15] Using the paper's US$2/GPU-hour assumption, **US$5.576M corresponds to full formal-training compute conversion**, not full R&D cost.

The supported mechanism is that in a supply-constrained environment, sparse architecture, memory efficiency, routing, quantization, and scheduling can improve effective compute productivity.

It does not support the claim that physical supply no longer matters, nor that any constrained system can automatically reproduce the same economics.

Algorithmic efficiency is a lever—not a substitute for HBM, packaging, interconnect, and power.

## 8A. System engineering can compensate for manufacturing disadvantage, but the compensation has a cost

A manufacturing-node disadvantage does not translate one-for-one into a system-output disadvantage.

A constrained stack can partially compensate through:

- sparsity, quantization, routing, and memory-efficiency gains;
- larger numbers of dies / accelerators;
- chiplet, board-level, or rack-level topology;
- more aggressive compiler / runtime co-design;
- workload-specific scheduling and communication optimization;
- narrower specialization around captive workloads.

This is a real competitive axis and prevents process-node position from being treated as a deterministic system verdict.

But compensation is not free. Using more devices, larger topologies, or more elaborate software can increase pressure on other denominators:

- logic-wafer input;
- package starts / integration complexity;
- memory capacity and bandwidth;
- interconnect and switch count;
- power and cooling;
- failure domains and operational complexity;
- capital required per delivered workload.

The correct test is therefore not “Which node is more advanced?” and not “Can software erase the node gap?”

It is:

> **Can system engineering convert the available manufacturing base into competitive production-workload economics without simply moving the bottleneck into memory, packaging, networking, power, reliability, or capital?**

Because those inputs use different physical units, they should not be collapsed into one synthetic compensation score. The relevant comparison uses bounded metrics such as throughput / cost per target workload, power per verified output, qualified package availability, memory intensity, utilization, and multi-generation continuity.

This gives engineering compensation its proper role: **it can compress a hardware disadvantage; it does not remove the need for system closure.**

---

## 9. Domestic workloads create the iteration loop

A parallel stack does not need to win the global developer ecosystem before it can create value.

A sufficiently large captive workload can generate production feedback in compiler behavior, deployment, failure recovery, operator coverage, and utilization.

The logic is similar to hyperscaler custom silicon:

> **large captive workloads can first support a narrower but complete system stack before the stack expands toward a broader external ecosystem.**

Long-run progress should therefore be evaluated from production workload scale and persistence—not benchmarks alone.

## 10. Export controls reach manufacturing continuity, not only accelerator access

Export restrictions raise the near-term cost of acquiring advanced hardware and can slow frontier-cluster deployment.

A separate upstream issue is semiconductor-manufacturing equipment, software, and service. ASML's public statements confirm that EUV sales to China are restricted, the most advanced immersion DUV systems require export licences, and later controls expanded to additional advanced manufacturing technologies, including metrology and software.[^16][^17]

This does not mean every domestic memory fab would immediately stop operating under a disruption.

It does mean:

> **domestic memory capacity growth ≠ upstream manufacturing autonomy**

Whether new capacity can ramp, process generations can advance, and installed tools can be sustained depends on critical equipment, software licences, spare parts, field service, and materials qualification continuity.

Over the longer run, the same restrictions increase the incentive for domestic substitution, local hardware/software integration, and parallel-ecosystem development.

Export control is therefore not a one-direction variable.

It can widen short-term performance/scale gaps while strengthening the long-run incentive to build a parallel system.

The final outcome depends on R&D efficiency, capital allocation, ecosystem adoption, and supply scaling—not policy alone.

## 11. Two closure tests

Treating "production substitution" and "full autonomy" as one threshold creates two opposite analytical errors.

They should therefore be separated.

### 11.1 Production-Grade Parallel Stack

A substitute system should be considered production-grade only when the following can operate at verifiable scale:

1. accelerator / compute delivery;
2. HBM-class or equivalent memory subsystem;
3. advanced packaging / integration;
4. high-speed scale-up / scale-out interconnect;
5. compiler/runtime with acceptable migration cost;
6. frontier or high-value production workloads with sustained feedback;
7. system utilization, reliability, power, and economics.

This standard asks whether the system works commercially in real workloads.

It does **not** require every component, tool, or material to be domestic.

### 11.2 Autonomous Frontier Closure

A higher standard applies when the question is whether the stack can continue scaling and advancing when critical external inputs are constrained.

That additionally requires:

8. **advanced-manufacturing continuity:** equipment, software, materials, spares, field service, and process upgrades remain available or substitutable;
9. **infrastructure / capital continuity:** HBM, packaging, LPS/power, and long-duration capital can support multi-generation expansion.

Therefore:

> **production-grade substitution ≠ full technological autonomy**

Import dependence does not prove that no production-grade parallel stack exists. Conversely, successful production deployment does not prove autonomous frontier closure.

## 12. Why partial closure already matters globally

If China's parallel stack scales simultaneously in advanced logic, HBM, packaging, interconnect, and software, it will do more than replace imports.

It will create a second large resource-gravity center, adding new foundry demand, memory demand, packaging demand, power demand, and long-duration capital commitments to regional and global resource allocation.

Current public evidence is not sufficient to show that this second frontier resource center has already reached equivalent full-stack scale.

The cited May 27, 2026 registration prospectus does not disclose an HBM product line. SMIC's 5.1% figure is foundry revenue share rather than frontier capability. Multiple non-silicon layers still require independent validation.

The most accurate current state is therefore:

> **China has moved beyond the stage of "no alternative system," and a real frontier parallel stack is iterating with partial production deployment. But under this chapter's seven Production-Grade Gates, public evidence is still insufficient to confirm that a complete production-grade frontier parallel stack has closed. Autonomous Frontier Closure remains a still higher and unproven threshold.**

## 13. Current read and falsification

As of August 2026:

- smartphone / consumer computing: relatively strong parallel-supply capability;
- PC / workstation: expanding substitution, with software and professional-workload compatibility still determining closure;
- frontier AI: a real and continuing accelerator/software parallel stack exists, while HBM, advanced packaging, interconnect, software migration, power, and scale still require simultaneous validation.

The system-closure judgment should be raised if first-party evidence appears for:

- an official HBM product / revenue line;
- auditable large-cluster utilization and frontier workloads;
- scaled advanced-packaging delivery;
- multi-generation compiler/runtime compatibility;
- stable and sustainable system economics.

If these gates remain uncrossed, "a domestic technology stack exists" cannot be upgraded into "frontier-equivalent substitution."

## References

[^1]: TSMC, 4Q25 Presentation / 2025 full-year platform mix, HPC 58%, smartphone 29%, https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
[^2]: Counterpoint Research, 2026 Q1 smartphone AP-SoC shipment share, UNISOC 14%, HiSilicon 4%, https://counterpointresearch.com/en/insights/global-smartphone-apsoc-market-share-quarterly
[^3]: Xinhua, 2025-05-22, Xiaomi XRing O1 entered mass production, https://english.news.cn/20250522/bca3bd53dab946d88696b0fb1625231d/c.html
[^4]: Reuters, 2026-08-24, XRing O1 device scale and O3 production plan, https://www.reuters.com/world/china/xiaomi-launches-new-xring-chip-partners-with-tsmc-production-sources-say-2026-08-24/
[^5]: Loongson, official CPU product line, https://www.loongson.cn/product/list?id=4
[^6]: Moore Threads, MTT S80 official product page, https://en.mthreads.com/product/S80
[^7]: CXMT, STAR Market registration prospectus, 2026-05-27, Shanghai Stock Exchange, https://static.sse.com.cn/stock/disclosure/announcement/c/202605/002170_20260527_23QQ.pdf ; earlier prospectus / stable fallback, 2025-12-30, https://static.sse.com.cn/stock/disclosure/announcement/c/202512/002170_20251230_B8QS.pdf
[^8]: CXMT, official DDR5 product page, https://www.cxmt.com/en/product.html
[^9]: YMTC, company profile and product portfolio, https://www.ymtc.com/en/aboutus.html ; https://www.ymtc.com/en/buslist.html?cat=35
[^10]: Micron Technology, investor material on HBM4E base logic die partnership with TSMC, https://investors.micron.com/static-files/5ea95475-639b-4cfc-91fd-b9b4a2bb5e63
[^11]: CXMT 2025 prospectus / Omdia, 2025 Q2 DRAM revenue share 3.97%, global #4, https://static.sse.com.cn/stock/disclosure/announcement/c/202512/002170_20251230_B8QS.pdf
[^12]: Counterpoint Research, 2026 Q2, YMTC 14% NAND shipment share, https://counterpointresearch.com/en/insights/server-led-essds-hit-48-percent-of-nand-shipments
[^13]: Counterpoint Research, 2026 Q1, YMTC 13% NAND revenue share, https://counterpointresearch.com/en/insights/global-nand-memory-market-share
[^14]: TrendForce, 2026-06-12, 1Q26 foundry revenue shares, https://www.trendforce.com/presscenter/news/20260612-13095.html
[^15]: DeepSeek-AI, “DeepSeek-V3 Technical Report,” https://arxiv.org/abs/2412.19437
[^16]: ASML, 2023 statement on Dutch export-control regulations, https://www.asml.com/en/news/press-releases/2023/statement-regarding-export-control-regulations-dutch-government
[^17]: ASML, 2024 statement on updated export restrictions covering additional advanced manufacturing technologies, metrology, and software, https://www.asml.com/en/news/press-releases/2024/asml-expects-impact-of-updated-export-restrictions-to-fall-within-outlook-for-2025
[^18]: Shanghai Stock Exchange, listing announcement for CXMT (688825), 2026-07-24; trading commenced 2026-07-27, https://www.sse.com.cn/disclosure/announcement/listing/ipo/c/c_20260724_10826610.shtml


[^19]: UNISOC, M6870 official product page, explicitly listing TSMC 6nm EUV, https://www.unisoc.com/en/solution/IDMetaverseUS/M6870
[^20]: TSMC / Spreadtrum, 2011-01-27, first commercialized 40nm TD-SCDMA baseband processor produced at TSMC Fab 12, https://pr.tsmc.com/english/news/1655
[^21]: UNISOC, T9100 official product page, 6nm process specification; the page does not itself identify the foundry, https://www.unisoc.com/en/product/SmartPhoneUS/T9100
[^22]: U.S. Bureau of Industry and Security, 2025-01-15, foundry due-diligence / advanced-computing IC controls and Approved / Authorized IC Designer framework, https://www.bis.gov/press-release/commerce-strengthens-restrictions-advanced-computing-semiconductors-enhance-foundry-due-diligence-prevent
