# P1.5 · China System-Stack Extension v0.1

> **Status:** Research-side extension; not part of the frozen 32-chapter formal report.  
> **Goal:** close four structural gaps in Chapter 17 without weakening its existing two-level closure discipline: **server/system delivery, Huawei full-stack comparison, auditable public-company map, and semiconductor industrial-policy political economy**.

## 1. Core correction

China should not be modeled as:

> Huawei + memory + foundry

The relevant system is:

```text
CPU / accelerator
→ memory
→ server / rack integration
→ interconnect
→ compiler/runtime
→ cluster operations
→ cloud / enterprise workload
→ data center / power
→ equipment / materials / services
→ capital / state procurement
```

The existing Chapter 17 remains correct on:

> **production-grade substitution ≠ autonomous frontier closure**

Phase II adds a second rule:

> **design origin ≠ manufacturing closure ≠ system-delivery closure**

---

# 2. Gap A — Server / rack / cluster delivery is an independent layer

Chapter 17 previously jumped from chips/memory/foundry toward system closure without explicitly modeling the server OEM / rack-integration layer.

That layer matters because production deployment requires:

- motherboard and server engineering;
- CPU + accelerator topology;
- NIC / fabric integration;
- firmware / BMC;
- power delivery;
- liquid/air cooling;
- burn-in and reliability;
- rack integration;
- field service;
- cluster deployment and O&M.

This is the layer that converts:

> **a chip exists**

into:

> **a repeatable production system can be delivered and serviced.**

## 2.1 China accelerated-server market

Public reports relaying IDC's **2025H1 China accelerated-server tracker** state:

- the market reached roughly **US$16B** in 2025H1;
- by vendor revenue, **Inspur, H3C and Lenovo** ranked top three and together accounted for nearly 50%;
- by unit shipments, **Inspur, H3C and Ningchang** ranked top three and together accounted for roughly 43%.

This supports:

> **China has a commercially large domestic server-integration and system-delivery layer.**

It does **not** support:

- Chinese vendors dominate global AI-server shipments;
- these systems are primarily based on domestic accelerators;
- server scale alone proves frontier-system autonomy.

Those denominators remain separate.

## 2.2 Product-level system-integration evidence

**H3C UniServer R5500 G7 X**
- 10U;
- 8-GPU module;
- official page states support for a next-generation domestic OAM GPU;
- positioned for distributed large-model training.

**xFusion FusionPoD for AI**
- rack-scale liquid-cooled system;
- 64 GPUs per cabinet;
- 105 kW centralized power;
- native liquid cooling;
- IB / Ethernet networking options.

These are system-engineering facts, not utilization or shipment facts.

## 2.3 New production-grade sub-gate

The China parallel-stack test should explicitly add:

> **server / rack / cluster integration must be repeatably manufacturable, thermally/power qualified, serviceable, and deployable at production scale.**

Accelerator specifications alone cannot satisfy this gate.

---

# 3. Gap B — Huawei must be analyzed as a full system stack

Chapter 17 §5 correctly says Ascend / CANN matters because of system completeness, not one-card peak FLOPS.

Phase II should carry that logic through the full stack.

## 3.1 Huawei public stack map

| Layer | Publicly observable Huawei element | Evidence boundary |
|---|---|---|
| Accelerator | Ascend family | chip existence ≠ autonomous manufacturing closure |
| SuperPoD / rack | Atlas 900 A3 / Atlas 950 | deployment claims require independent utilization/TCO evidence |
| Scale-up fabric | UnifiedBus | topology/bandwidth claims ≠ real workload scaling efficiency |
| Runtime / compiler | CANN | open-source availability ≠ CUDA-equivalent migration economics |
| Framework integration | PyTorch, vLLM, Triton, TileLang, verl, etc. | compatibility breadth must be tested on production workloads |
| General compute | TaiShan / Kunpeng | separate general compute from frontier-AI economics |
| Cloud / service | Huawei Cloud / SuperPoD services | availability ≠ audited utilization |
| Enterprise distribution | telecom, finance, manufacturing, government/enterprise channels | captive workload can accelerate learning loops |
| Upstream manufacturing | broader Chinese foundry / memory / packaging / equipment chain | autonomous frontier closure remains unproven |

## 3.2 Deployment evidence is stronger than the frozen chapter currently reflects

Huawei stated in July 2026 that:

- **750+ Ascend 384 SuperPoDs** had been commercially deployed;
- deployments covered more than 20 industries;
- the CANN open-source community had 67 projects and more than 12 million lines of open-source code.

Earlier Huawei disclosures in 2025 reported **300+ Atlas 900 A3 SuperPoDs** serving more than 20 customers.

These are **first-party deployment claims**.

They materially strengthen the evidence for:

> **production-scale system delivery**

but still do not establish:

- independently audited utilization;
- training/inference efficiency against alternatives;
- failure/recovery rates;
- customer TCO;
- upstream HBM / packaging / foundry autonomy.

Therefore the defensible conclusion is:

> **Huawei has public evidence of production-scale system deployment and the most vertically integrated publicly observable Chinese AI stack; autonomous frontier manufacturing closure remains unproven.**

## 3.3 NVIDIA comparison rule

Do not write:

> “Huawei is the only company in the world following NVIDIA's model.”

A better formulation is:

> **Among Chinese suppliers, Huawei is the clearest publicly observable case of an accelerator + interconnect + system + runtime + cloud/enterprise delivery stack, making it the natural Chinese counterpart for the report's system-stack framework.**

The question is not “Is Huawei equal to NVIDIA?”

It is:

> **Which layers are already production-grade, which still lack migration/economic evidence, and which upstream gates prevent autonomous frontier closure?**

---

# 4. Gap C — Public-company evidence map

The Chinese compute ecosystem should no longer be represented as “Huawei + footnotes.”

The correct map tracks each company through:

```text
R&D / product
→ customer qualification
→ commercial revenue
→ audited revenue
→ production cluster
→ repeat deployment
→ independent utilization / economics
```

## 4.1 Hygon / 海光信息

Hygon is a listed high-end processor company with auditable financials.

Its 2025 annual report reported approximately:

- **RMB14.38B revenue**;
- **+56.9% YoY**;
- positive operating cash flow.

Its core products are high-end processors, including CPU / DCU product lines.

This proves commercialization and scale.

Do **not** label it “China's largest domestic server-CPU supplier” without a reliable market-share denominator.

## 4.2 Cambricon / 寒武纪

SSE public material reports for 2025:

- **RMB6.497B revenue**;
- **+453.21% YoY**;
- **RMB2.059B net profit**;
- first full-year profit after listing.

This is a much stronger evidence state than “a domestic AI chip exists.”

The correct follow-up variables are:
- product mix;
- customer concentration;
- cloud/cluster deployment;
- cash conversion;
- repeat orders;
- independent utilization.

## 4.3 Moore Threads / 摩尔线程

Moore Threads' 2026H1 report disclosed:

- **RMB1.736B revenue**;
- **+147.42% YoY**;
- net loss narrowed sharply;
- operating cash flow remained strongly negative.

This is evidence of commercialization and scaling, not frontier equivalence.

## 4.4 MetaX / 沐曦 and Suiyuan / 燧原

**MetaX**
- listed on the Shanghai STAR Market on **2025-12-17**;
- official SSE listing records confirm ticker **688802**.

**Suiyuan**
- received CSRC approval for STAR Market IPO registration on **2026-07-09**.

These capital-market milestones increase auditability and financing capacity.

They do not by themselves prove production-scale frontier competitiveness.

## 4.5 Research rule

The report should classify Chinese accelerator companies by **evidence state**, not by political label:

> product → revenue → audited revenue → cluster → repeat deployment → utilization/economics.

This is superior to both:
- “all domestic chips are fake,” and
- “listing/revenue proves frontier equivalence.”

---

# 5. Gap D — Industrial-policy political economy

The formal report already states:

> subsidies can accelerate capacity formation but cannot directly buy yield learning.

That is technically correct but incomplete.

China's semiconductor system also needs to be modeled as:

> **capital allocation + political incentives + procurement + governance**

## 5.1 Policy channels

Relevant mechanisms include:

- National Integrated Circuit Industry Investment Fund (“Big Fund”);
- local government guidance funds;
- state-owned bank credit;
- direct grants;
- tax benefits;
- industrial parks / land / infrastructure;
- government and state-enterprise procurement;
- localization / “xinchuang” demand;
- capital-market listing channels.

The third phase of China's semiconductor Big Fund was registered in May 2024 with roughly **RMB344B / US$47.5B** of capital.

This is a large capital-formation mechanism.

It is not evidence that every funded project becomes technologically successful.

## 5.2 The causal chain that matters

```text
state capital / procurement
→ project selection
→ equipment + talent + process learning
→ qualified production
→ customer adoption
→ cash flow
→ reinvestment
→ next-generation capability
```

Public support enters early in the chain.

The report should judge the **conversion rate**, not only the funding amount.

## 5.3 Fraud and misallocation are real failure modes — but must not become an ecosystem label

Rhodium Group's 2026 review, drawing on Chinese audit/rectification material, reports:

- duplicated and inefficient local guidance-fund investment;
- governance incentives that favored politically connected or later-stage firms in some cases;
- 2024 audit findings involving fraudulent subsidy claims;
- a late-2025 rectification process that recovered or reallocated about **RMB5.975B** in misused funds and strengthened verification.

This supports:

> **fraud, duplication, local-government competition and misallocation are real political-economy risks.**

It does **not** support:

> “non-Huawei Chinese semiconductor companies are mostly subsidy frauds.”

That stronger statement conflicts with audited revenue, shipment and listing evidence across multiple firms.

## 5.4 Political-economy variables to add

Future China analysis should track:

1. **state-support intensity**;
2. **private-capital participation**;
3. **customer / procurement independence**;
4. **revenue outside policy-protected demand**;
5. **repeat commercial orders**;
6. **subsidy / grant share of economics**;
7. **cash conversion**;
8. **R&D conversion into qualified production**;
9. **local duplication / overcapacity**;
10. **governance / fraud / audit remediation**.

The central question is:

> **Does state support convert into self-reinforcing production economics, or does the project remain dependent on continued policy capital?**

---

# 6. Foundry dependence must be explicit

The frozen Chapter 17 has now been corrected on this point.

For UNISOC and Xiaomi:

> **design origin is not manufacturing closure.**

UNISOC official materials confirm current 6nm products; at least one official product page, M6870, explicitly identifies **TSMC 6nm EUV**. TSMC and Spreadtrum also have a long first-party manufacturing history.

This is sufficient to require a separate **foundry-continuity gate**.

It is **not** sufficient to claim that every UNISOC SoC is manufactured by TSMC.

The same discipline applies to Xiaomi XRing, where the Reuters source used in the formal chapter explicitly identifies TSMC manufacturing cooperation.

---

# 7. China stack should be scored by layer, not by nationality label

A Phase II matrix should eventually use:

| Layer | Production-grade evidence | External dependency | Autonomous-closure state |
|---|---|---|---|
| Smartphone SoC design | strong | foundry varies | not equivalent to manufacturing closure |
| General CPU | commercial | manufacturing/toolchain dependencies | partial |
| AI accelerator | multi-company commercial deployment | foundry/HBM/packaging constraints | partial |
| Server/rack integration | commercially large | accelerator/component mix varies | stronger |
| DRAM/NAND | real global scale | equipment/material/service constraints | partial |
| HBM | public volume evidence insufficient | high | open |
| Advanced foundry | real domestic production | equipment/service/process constraints | incomplete |
| Packaging/interconnect | growing | needs independent production-scale evidence | open/partial |
| Compiler/runtime | Huawei + other ecosystems exist | migration economics variable | production-grade in selected workloads |
| Power/data center | large domestic build capacity | less externally constrained | strong physical layer |
| Capital/procurement | very strong state capacity | governance/efficiency risk | not a technical-closure metric |

This prevents two opposite errors:

- “China has no alternative stack”;
- “China has already achieved full frontier autonomy.”

---

# 8. v0.1 conclusion

The missing China analysis is not another list of domestic chip companies.

It is a **system-delivery + capital-allocation map**.

The strongest current conclusion is:

> **China already has multiple commercial compute suppliers, a large server/system-integration layer, a uniquely vertically integrated Huawei stack, meaningful memory/foundry capacity, and strong state capital formation. The unresolved question is whether these layers can close simultaneously across HBM, advanced packaging, leading-edge manufacturing continuity, software migration, large-cluster economics, and multi-generation supply continuity.**

That is the correct level for treating China as a major 2026–2036 system variable.

## Sources

- IDC China accelerated-server market, 2025H1, public relay: https://www.itiger.com/news/1165230665
- H3C UniServer R5500 G7 X official product page: https://www.h3c.com/cn/Products_And_Solution/Server/H3C/Products/GPU_Server/Products_Series/Application_Optimization_GPU/R5500_G7_X/
- xFusion FusionPoD for AI official product page: https://www.xfusion.com/en/product/rack-scale-servers/fusionpod-for-ai
- Huawei, 2026-07, Atlas 950 / Ascend 384 SuperPoD deployment and CANN open-source update: https://www.huawei.com/cn/news/2026/7/atlas-950-superpod
- Huawei, 2025-09, SuperPoD / UnifiedBus / CANN strategy and >300 Atlas 900 A3 deployment: https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech
- Huawei, MWC 2026 SuperPoD portfolio: https://www.huawei.com/en/news/2026/3/mwc-superpod-computing
- Hygon 2025 annual-report data: https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12066610&stockid=688041
- Shanghai Stock Exchange, 2025 AI-chip annual-report summary including Cambricon: https://www.sse.com.cn/cpc/cpctheme/4th20thcpc/4th20thcpcgcxx/c/c_20260413_10815020.shtml
- Shanghai Stock Exchange, Moore Threads 2026H1 summary: https://english.sse.com.cn/news/newsrelease/voice/c/c_20260811_10828576.shtml
- Shanghai Stock Exchange, MetaX listing announcement: https://www.sse.com.cn/disclosure/announcement/listing/ipo/c/c_20251216_10801769.shtml
- CSRC, Suiyuan IPO registration approval, 2026-07-09: https://www.csrc.gov.cn/csrc/c105906/c7644477/content.shtml
- Reuters, Big Fund III, 2024-05-27: https://www.reuters.com/technology/china-sets-up-475-bln-state-fund-boost-semiconductor-industry-2024-05-27/
- Rhodium Group, China's Next-Generation Industrial Policy, 2026-05-11: https://rhg.com/research/chinas-next-generation-industrial-policy/
- UNISOC M6870 official product page, TSMC 6nm EUV: https://www.unisoc.com/en/solution/IDMetaverseUS/M6870
- TSMC / Spreadtrum 40nm production history: https://pr.tsmc.com/english/news/1655
