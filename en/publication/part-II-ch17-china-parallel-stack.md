# Part II · Chapter 17: China's Parallel Stack — From Production-Grade Substitution to Autonomous Frontier Closure

## 1. "It can run" and "it forms an equivalent system" are not the same standard

Any discussion of China's AI stack becomes misleading if the layers are not separated first.

At minimum, the analysis should distinguish:

1. **smartphone / consumer computing**;
2. **PC / workstation / general computing**;
3. **frontier AI system stack**.

These layers have very different requirements for advanced logic, memory, packaging, software, interconnect, and performance.

China's strong smartphone supply chain cannot be extrapolated into proof that frontier-training systems are already closed. Conversely, frontier-AI constraints cannot be rewritten as "China has no semiconductor substitution capability."

The relevant test is whether a system reaches production-grade acceptability across **functional availability, performance, scale, software portability, supply sustainability, and economics** at the same time.

## 2. Layer one: consumer computing is the easiest place to form parallel supply

Smartphones and parts of consumer computing can form a more complete domestic chain because they can draw on local SoCs, foundries, LPDDR/NAND, packaging, device manufacturing, operating-system/application ecosystems, and large domestic demand.

TSMC's 2025 platform mix still shows smartphone at **29%** of annual platform revenue and HPC at **58%**.[^1]

### 2.1 "Huawei is the only Chinese smartphone-SoC vendor with real scale" is no longer consistent with 2026 public data

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

Consumer parallel-supply capability should therefore be evaluated as its own layer—not used as proof for or against frontier-AI closure.

## 3. Layer two: PCs / workstations are constrained more by software compatibility and scale

PCs, workstations, and general computing require CPU/GPU hardware, DDR5, professional software, drivers/tooling, desktop ecosystems, and developer compatibility.

The claim that domestic PC CPUs/GPUs are "blank" is also too strong.

Loongson's current official portfolio includes desktop/general-purpose CPUs such as the 3A6000 and 3B6000.[^5] Moore Threads publicly sells the MTT S80 gaming GPU.[^6]

These facts establish **real products and deployable domestic PC/graphics systems**.

They do not establish:

- mainstream consumer-PC shipment share approaching Intel/AMD/NVIDIA;
- equivalent coverage of professional software / games;
- equivalent performance-per-watt, driver maturity, developer ecosystem, or supply scale.

The more accurate description is therefore:

> **the segment is not empty; products and domestic ecosystems exist, while mainstream scale, compatibility, and system economics remain the closure barriers.**

## 4. Layer three: frontier AI is a system-level threshold

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

This report therefore does not treat "one domestic chip can run a model" as sufficient evidence of frontier substitution.

## 5. The strategic meaning of Ascend / CANN lies in system completeness, not one card's peak number

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

## 6. Memory is the layer most easily hidden by the broad term "domestic memory"

CXMT's **December 30, 2025 Shanghai Stock Exchange prospectus** discloses DDR and LPDDR products. The company subsequently began trading on Shanghai's STAR Market on **July 27, 2026**.[^7][^18]

Full-text searches of the relevant public offering / registration materials for `HBM` and the Chinese term for high-bandwidth memory do not provide evidence sufficient to confirm a volume HBM product line. This report therefore keeps one narrow conclusion:

> **Current public offering and product materials are insufficient to confirm a volume-deliverable HBM product line.**

This does **not** prove that the company has no HBM R&D. Listing changes the company's capital-market and financing state; it does not by itself cross the HBM, advanced-packaging, or frontier-system technical gates.

To move HBM from possible R&D into frontier-system supply, the evidence would need to include official products, customer qualification, volume production, bandwidth/capacity, and packaging integration.

The same prospectus also requires strict separation between project investment and planned offering proceeds. For the DRAM technology-upgrade project, **RMB18.0B total investment** and **RMB13.0B planned offering proceeds** are different denominators.[^7]

DDR/LPDDR supply expansion and HBM-class memory closure therefore have to remain separate.

### 6.1 Conventional DRAM / NAND and frontier HBM are different supply-chain thresholds

CXMT's current official product page discloses DDR5 chips up to **8000 Mbps**, with 16Gb/24Gb densities and server/workstation/PC module coverage including RDIMM/MRDIMM.[^8]

YMTC officially describes itself as a 3D NAND IDM and discloses its Gen5/Xtacking 4.0 product path together with raw NAND, embedded memory, client SSD, and enterprise SSD portfolios.[^9]

These facts support a narrower conclusion:

> **consumer/general-purpose memory resilience can improve before frontier HBM closure is achieved.**

Front-end manufacturing for conventional DRAM and NAND is not the same physical pool as TSMC leading-edge logic foundry capacity.

But HBM-class AI systems can reintroduce advanced-logic/base-die, advanced-packaging, and accelerator-integration dependencies. Micron, for example, has publicly disclosed a TSMC partnership for manufacturing HBM4E base logic dies.[^10]

"Conventional memory can bypass TSMC logic foundry" and "the frontier AI memory stack is independent of TSMC" are therefore different propositions.

### 6.2 Domestic memory scale: revenue share and shipment share must remain separate

CXMT's prospectus, citing Omdia, provides an auditable metric: based on **2025 Q2 DRAM revenue**, CXMT held approximately **3.97% global share**, ranking fourth globally and first in China.[^11]

The claim that "CXMT already has 8% of global DRAM" therefore does not enter this report's fact layer.

YMTC's latest institutional metric uses a different denominator. Counterpoint Research's Q2 2026 Memory & Storage Tracker places YMTC at roughly **14% of NAND shipments**, ranking third globally.[^12] The same research firm's Q1 2026 **13%** figure is a NAND **revenue share**.[^13]

Those two percentages cannot be turned into one continuous time series because their denominators differ.

What they support is a narrower conclusion:

> **China's conventional DRAM / NAND presence in global supply has risen materially, but share growth does not by itself prove HBM, leading-edge logic, or frontier-system closure.**

Claims such as "capacity will double by 2027" or specific Phase-III monthly wafer output remain B/C-grade background unless they are disclosed directly by the company or another formal first-party source.

### 6.3 HDD must not be hidden by progress in NAND

AI data-center storage also includes nearline HDD.

Public industry research shows that global nearline / mass-capacity HDD supply remains highly concentrated in Seagate, Western Digital, and Toshiba.

Stronger domestic NAND / SSD capability therefore cannot be rewritten as "the entire storage stack is domestically closed."

AI has also not simply eliminated HDD. Mass-capacity / cold-storage demand remains real, while QLC nearline SSD is accelerating substitution for selected workloads.

## 7. Foundry revenue share is not frontier-AI capability

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

## 8. Algorithmic efficiency is an important asymmetric lever

The DeepSeek-V3 Technical Report shows that algorithmic and architectural design can materially lower the hardware required per unit of capability.

The paper reports **2.664M H800 GPU-hours for pre-training** and **2.788M H800 GPU-hours for full formal training**.[^15] Using the paper's US$2/GPU-hour assumption, **US$5.576M corresponds to full formal-training compute conversion**, not full R&D cost.

The supported mechanism is that in a supply-constrained environment, sparse architecture, memory efficiency, routing, quantization, and scheduling can improve effective compute productivity.

It does not support the claim that physical supply no longer matters, nor that any constrained system can automatically reproduce the same economics.

Algorithmic efficiency is a lever—not a substitute for HBM, packaging, interconnect, and power.

## 9. Domestic workloads are an important condition for parallel-system iteration

A parallel stack does not need to win the global developer ecosystem before it can create value.

A sufficiently large captive workload can generate production feedback in compiler behavior, deployment, failure recovery, operator coverage, and utilization.

The logic is similar to hyperscaler custom silicon:

> **large captive workloads can first support a narrower but complete system stack before the stack expands toward a broader external ecosystem.**

Long-run progress should therefore be evaluated from production workload scale and persistence—not benchmarks alone.

## 10. Export controls affect manufacturing continuity as well as accelerator access

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

## 11. Two levels of closure: Production-Grade Parallel Stack and Autonomous Frontier Closure

Treating "production substitution" and "full autonomy" as one threshold creates two opposite analytical errors.

The report therefore separates them.

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

## 12. The real effect on global resource competition

If China's parallel stack scales simultaneously in advanced logic, HBM, packaging, interconnect, and software, it will do more than replace imports.

It will create a second large resource-gravity center, adding new foundry demand, memory demand, packaging demand, power demand, and long-duration capital commitments to regional and global resource allocation.

Current public evidence is not sufficient to show that this second frontier resource center has already reached equivalent full-stack scale.

The cited Shanghai Stock Exchange prospectus does not disclose an HBM product line. SMIC's 5.1% figure is foundry revenue share rather than frontier capability. Multiple non-silicon layers still require independent validation.

The most accurate current state is therefore:

> **China has moved beyond the stage of "no alternative system," but has not yet crossed the threshold of globally equivalent scaled closure across all critical layers.**

## 13. Current judgment and falsification

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
[^7]: CXMT, prospectus, 2025-12-30, Shanghai Stock Exchange, https://static.sse.com.cn/stock/disclosure/announcement/c/202512/002170_20251230_B8QS.pdf
[^8]: CXMT, official DDR5 product page, https://www.cxmt.com/en/product.html
[^9]: YMTC, company profile and product portfolio, https://www.ymtc.com/en/aboutus.html ; https://www.ymtc.com/en/buslist.html?cat=35%3Fcat%3D35
[^10]: Micron Technology, investor material on HBM4E base logic die partnership with TSMC, https://investors.micron.com/static-files/5ea95475-639b-4cfc-91fd-b9b4a2bb5e63
[^11]: CXMT 2025 prospectus / Omdia, 2025 Q2 DRAM revenue share 3.97%, global #4, https://static.sse.com.cn/stock/disclosure/announcement/c/202512/002170_20251230_B8QS.pdf
[^12]: Counterpoint Research, 2026 Q2, YMTC 14% NAND shipment share, https://counterpointresearch.com/en/insights/server-led-essds-hit-48-percent-of-nand-shipments
[^13]: Counterpoint Research, 2026 Q1, YMTC 13% NAND revenue share, https://counterpointresearch.com/en/insights/global-nand-memory-market-share
[^14]: TrendForce, 2026-06-12, 1Q26 foundry revenue shares, https://www.trendforce.com/presscenter/news/20260612-13095.html
[^15]: DeepSeek-AI, “DeepSeek-V3 Technical Report,” https://arxiv.org/abs/2412.19437
[^16]: ASML, 2023 statement on Dutch export-control regulations, https://www.asml.com/en/news/press-releases/2023/statement-regarding-export-control-regulations-dutch-government
[^17]: ASML, 2024 statement on updated export restrictions covering additional advanced manufacturing technologies, metrology, and software, https://www.asml.com/en/news/press-releases/2024/asml-expects-impact-of-updated-export-restrictions-to-fall-within-outlook-for-2025
[^18]: Shanghai Stock Exchange, listing announcement for CXMT (688825), 2026-07-24; trading commenced 2026-07-27, https://big5.sse.com.cn/site/cht/www.sse.com.cn/disclosure/announcement/listing/ipo/c/c_20260724_10826610.shtml
