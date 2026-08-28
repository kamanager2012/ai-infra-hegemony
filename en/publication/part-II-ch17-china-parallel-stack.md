# Part II · Chapter 17: China's Parallel Stack — From Product Substitution to Frontier System Closure

> **Publication-layer chapter.** Recompiled from [Volume 12](../vol-12.en.md), [Volume 29](../vol-29.en.md), and [Macro Essay 08](../part2-08.en.md). This chapter does not use one "domestic substitution rate" to judge China's AI supply capability. It separates consumer computing, general-purpose computing, and frontier AI systems into three different layers.

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

TSMC's 2025 platform mix still shows smartphone at **29%** of annual platform revenue and HPC at **58%**.

Consumer computing therefore remains a major market, but frontier AI and smartphones compete for different resources inside the same advanced-manufacturing ecosystem.

Consumer parallel-supply capability should be evaluated as its own layer—not used as proof for or against frontier-AI closure.

## 3. Layer two: PCs / workstations are constrained more by software compatibility and scale

PCs, workstations, and general computing require CPU/GPU hardware, DDR5, professional software, drivers/tooling, desktop ecosystems, and developer compatibility.

Hardware alternatives can exist without equivalent user experience, performance, or software-stack maturity.

The more accurate description is:

> **Substitution capability can expand, while system closure still depends on software compatibility, professional workloads, and long-duration developer support.**

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

CXMT's **May 27, 2026 STAR Market registration prospectus** discloses DDR and LPDDR products.

Full-text searches of the prospectus for `HBM` and the Chinese term for high-bandwidth memory return no matches. The publication layer therefore keeps one narrow conclusion:

> **The registration prospectus does not disclose an HBM product line.**

This does **not** prove that the company has no HBM R&D.

To move HBM from possible R&D into frontier-system supply, the evidence would need to include official products, customer qualification, volume production, bandwidth/capacity, and packaging integration.

The same prospectus also requires strict separation between project investment and planned offering proceeds. For the DRAM technology-upgrade project, **RMB18.0B total investment** and **RMB13.0B planned offering proceeds** are different denominators.

DDR/LPDDR supply expansion and HBM-class memory closure therefore have to remain separate.

## 7. Foundry revenue share is not frontier-AI capability

TrendForce's 1Q26 foundry revenue-share estimates are approximately:

| Foundry | Revenue share |
|---|---:|
| TSMC | 72% |
| Samsung Foundry (excluding System LSI) | 6.5% |
| SMIC | 5.1% |

These are foundry **revenue shares**, not advanced-node yield, AI wafer capacity, or frontier-system delivery capability.

A frontier AI parallel supply stack requires more than logic dies. It also needs advanced packaging, substrates, HBM integration, yield, high-volume qualification, and power.

Node progress is one necessary condition, not the whole system.

## 8. Algorithmic efficiency is an important asymmetric lever

The DeepSeek-V3 Technical Report shows that algorithmic and architectural design can materially lower the hardware required per unit of capability.

The paper reports **2.664M H800 GPU-hours for pre-training** and **2.788M H800 GPU-hours for full formal training**. Using the paper's US$2/GPU-hour assumption, **US$5.576M corresponds to full formal-training compute conversion**, not full R&D cost.

The supported mechanism is that in a supply-constrained environment, sparse architecture, memory efficiency, routing, quantization, and scheduling can improve effective compute productivity.

It does not support the claim that physical supply no longer matters, nor that any constrained system can automatically reproduce the same economics.

Algorithmic efficiency is a lever—not a substitute for HBM, packaging, interconnect, and power.

## 9. Domestic workloads are an important condition for parallel-system iteration

A parallel stack does not need to win the global developer ecosystem before it can create value.

A sufficiently large captive workload can generate production feedback in compiler behavior, deployment, failure recovery, operator coverage, and utilization.

The logic is similar to hyperscaler custom silicon:

> **large captive workloads can first support a narrower but complete system stack before the stack expands toward a broader external ecosystem.**

Long-run progress should therefore be evaluated from production workload scale and persistence—not benchmarks alone.

## 10. Export controls have different short-run and long-run effects

Export restrictions raise the near-term cost of acquiring advanced hardware and can slow frontier-cluster deployment.

Over the longer run, the same restrictions increase the incentive for domestic substitution, local hardware/software integration, and parallel-ecosystem development.

Export control is therefore not a one-direction variable.

It can widen short-term performance/scale gaps while strengthening the long-run incentive to build a parallel system.

The final outcome depends on R&D efficiency, capital allocation, ecosystem adoption, and supply scaling—not policy alone.

## 11. Seven Frontier System Closure Gates

This report treats "China has formed a complete frontier-AI parallel stack" as fact only when all seven gates reach verifiable scale:

1. advanced accelerators can be delivered at scale;
2. HBM-class memory can be delivered at scale;
3. advanced packaging can be delivered at scale;
4. high-speed interconnect can support large clusters;
5. compiler/runtime migration cost is acceptable;
6. frontier workloads can run stably;
7. system cost / utilization / power are sustainable.

These gates change the question from "Does a domestic product exist?" to "Can a production-grade system be sustained?"

A persistent weakness in any one gate can limit system-level equivalent substitution.

## 12. The real effect on global resource competition

If China's parallel stack scales simultaneously in advanced logic, HBM, packaging, interconnect, and software, it will do more than replace imports.

It will create a second large resource-gravity center, adding new foundry demand, memory demand, packaging demand, power demand, and long-duration capital commitments to regional and global resource allocation.

Current public evidence is not sufficient to show that this second frontier resource center has already reached equivalent full-stack scale.

CXMT's registration prospectus does not disclose an HBM product line. SMIC's 5.1% figure is foundry revenue share rather than frontier capability. Multiple non-silicon layers still require independent validation.

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

## Key public sources

- CXMT 2026-05-27 STAR Market registration prospectus (SSE): https://static.sse.com.cn/stock/disclosure/announcement/c/202605/002170_20260527_23QQ.pdf
- SSE listing notice — listed 2026-07-27, ticker 688825: https://www.sse.com.cn/disclosure/announcement/listing/ipo/c/c_20260724_10826610.shtml
- TrendForce, 2026-06-12 — 1Q26 foundry revenue shares: https://www.trendforce.com/presscenter/news/20260612-13095.html
- TSMC 4Q25 Presentation — HPC 58%, smartphone 29%: https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
- NVIDIA FY26 10-K — China Data Center / export-control risk disclosures: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
- DeepSeek-V3 Technical Report: https://arxiv.org/abs/2412.19437
