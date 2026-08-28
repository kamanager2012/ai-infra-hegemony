# Volume 01: Executive Summary and Core Judgments for the Next Decade

Chinese original: [../vol-01.md](../vol-01.md)

## 1. Core conclusion

AI-infrastructure competition is moving from **single-chip competition** toward **system-stack competition**. Long-term value capture is increasingly determined not by GPU share alone, but by whether one platform can coordinate advanced logic, HBM, advanced packaging, interconnect, compilers/runtimes, rack-scale systems, data centers, and power across product generations.

This report calls the mechanism **Scarce-layer Value Capture**. It does not assume permanent monopoly. The claim is narrower: when a platform combines high profitability, strong free cash flow, long-duration demand, software switching costs, and system-level product definition, it usually has greater ability to reserve the next generation of scarce resources and extend present advantages forward.

NVIDIA's most important structural change is that the sales unit has moved upward from the accelerator card toward the **rack-scale system**. The official GB200 NVL72 configuration includes **72 Blackwell GPUs, 36 Grace CPUs, 13.4 TB of HBM3E, and 17 TB of LPDDR5X**. The buyer is therefore purchasing a coordinated compute, memory, interconnect, software, cooling, and rack system rather than an isolated die.

For the same reason, Google TPU/Ironwood, AWS Trainium, Microsoft Maia, and Meta MTIA should not be reduced to “ASIC versus GPU.” The competitive unit is the complete **system stack**: compiler/runtime, interconnect, rack/pod design, large internal workloads, deployment tooling, and supply-chain execution.

## 2. Current factual baseline

### 2.1 NVIDIA: platform economics and capacity-reservation ability

NVIDIA FY26, ended January 25, 2026:

| Metric | FY26 |
|---|---:|
| Revenue | **US$215.938B** |
| Data Center revenue | **US$193.737B** |
| GAAP gross margin | **71.1%** |
| Operating income | **US$130.387B** |
| Net income | **US$120.067B** |
| Non-GAAP free cash flow (NVIDIA definition) | **US$96.575B** |
| R&D | **US$18.497B** |

Primary sources:
- SEC CFO commentary: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26cfocommentary.htm
- NVIDIA FY26 results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
- FY26 10-K: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm

FY27 Q2, ended July 26, 2026, showed that platform profitability remained exceptionally high:

| Metric | FY27 Q2 |
|---|---:|
| Revenue | **US$96.221B** |
| Data Center revenue | **US$89.0B** |
| GAAP gross margin | **75.0%** |
| GAAP operating income | **US$63.734B** |
| Net income | **US$59.688B** |
| Vera Rubin | **full production** |
| FY27 Q3 revenue guidance | **US$108.0B ±2%** |

The FY26 H20-related charge did not permanently reset the platform margin structure; by FY27 Q2, GAAP gross margin had returned to 75.0%.

Capacity commitments are equally important. NVIDIA's manufacturing, supply, and capacity commitments rose from **US$95.2B** on 2026-01-25 to **US$119B** on 2026-04-26 and then to **US$279B** on 2026-07-26. The FY27 Q2 10-Q says the latest commitments are primarily tied to memory and manufacturing facilities for data-center infrastructure systems supporting current and future architectures.

Public filings do **not** allocate the **US$279B** among TSMC, CoWoS, SK hynix, Micron, or Samsung. It is therefore evidence of aggregate supply and capacity commitments, not a customer-specific revenue number for any single supplier. Source: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm .

### 2.2 TSMC: advanced manufacturing and packaging remain physical constraints

TSMC's 2025 public disclosures include:

| Metric | 2025 |
|---|---:|
| 12-inch-equivalent wafer shipments | about **15.0M** |
| Annual capacity | above **17M** |
| 3 nm wafer-revenue share | **24%** |
| 5 nm wafer-revenue share | **36%** |
| 7 nm wafer-revenue share | **14%** |
| ≤7 nm wafer-revenue share | **74%** |
| HPC platform share | **58% of 2025 net revenue**; platform revenue **+48% YoY** |
| Smartphone platform share | **29% of 2025 net revenue**; platform revenue **+11% YoY** |
| Largest customer revenue share | **19%** |
| Second-largest customer revenue share | **17%** |
| Back-end revenue disclosure | 2024: **advanced packaging and testing >8%**; 2025: **advanced packaging slightly above 10%** (company-corrected; labels are not identical) |

TSMC management has repeatedly described advanced packaging as tight. In the 4Q24 call, C.C. Wei said capacity was “very tight” and unable to meet all customer demand; in 2Q26, he said packaging capacity had become tight enough to limit customer growth.

Three quantities must remain separate:

1. annual customer revenue share;
2. leading-edge wafer share;
3. CoWoS customer share.

The 19% largest-customer revenue share is neither an N2 wafer share nor a CoWoS share. TSMC has not disclosed a customer-level CoWoS allocation table. The forward variable is therefore **incremental resource-capture ability**, not a mechanical conversion from historical revenue share into wafers.

### 2.3 HBM: AI demand has entered the wafer-supply layer

Micron's FY24 Q2 prepared remarks provide a critical first-party physical anchor: at the same technology node and bit capacity, HBM3E requires roughly **3× the wafer supply of DDR5**. Micron's FY25 10-K further confirms that HBM requires more wafers and cleanroom space to produce the same number of bits.

The ~3× figure is therefore an **A-grade first-party wafer-supply trade ratio**. It is not a price multiple and should not be treated as a fixed manufacturing constant for every fab or HBM generation.

TrendForce further estimates that HBM plus RDIMM account for roughly **51% of DRAM bits** in 2026. AI and server demand are therefore affecting not only high-value HBM but also the residual structure of conventional DRAM supply.

### 2.4 Cloud CapEx: enormous scale, incompatible accounting scopes

Microsoft, Amazon, Alphabet, and Meta are all spending at historically high levels, but their fiscal windows and accounting definitions differ.

On a mixed-year 2025 basis, equipment/PPE purchases across the four companies were roughly **$354B**. Public 2026 expectations and TTM figures moved higher again, but they still cannot be collapsed into one official “AI hardware CapEx” number.

The reasons are structural:

- Amazon includes fulfillment and network infrastructure;
- Meta includes non-AI infrastructure;
- Alphabet includes offices and other technical facilities;
- Microsoft's fiscal calendar differs from calendar-year reporters.

The more useful analytical question is whether AI servers, networking, memory, data centers, power, and custom silicon continue to take a larger share of each company's investment structure.

## 3. Scarce-layer value-capture mechanism

### 3.1 From chip competition to system-stack competition

AI infrastructure contains at least eight interdependent layers:

1. Advanced logic
2. HBM / DRAM
3. Advanced packaging
4. Scale-up / scale-out interconnect
5. Compiler / runtime / framework
6. Rack / pod / system design
7. Data center
8. Power

Replacing one layer does not automatically replace the whole system.

Cloud custom silicon can reduce NVIDIA's value capture in chips, interconnect, or software while still increasing competition for advanced nodes, HBM, advanced packaging, and power. Platform-profit diversion and upstream resource competition can therefore occur at the same time.

### 3.2 Incremental resources matter more than historical share

The report uses **AHICR — Advanced HPC Incremental Capacity Capture Ratio** to model the share of newly added scarce AI/HPC resources captured by a leading platform.

Historical customer revenue share describes the past. Forward allocation depends on variables including:

- long-duration orders;
- prepayment;
- credit quality;
- utilization;
- roadmap certainty;
- supplier diversification;
- geopolitics.

The report therefore does not assume that TSMC or another supplier mechanically favors one customer. The narrower mechanism is that a buyer with superior scale, prepayment ability, credit, utilization, and roadmap certainty can gain bargaining power over the next tranche of incremental capacity, while suppliers still retain incentives to diversify customers and manage geopolitical and long-run bargaining risk.

### 3.3 Non-AI Residual Capacity

Consumer electronics and conventional servers do not face a simple condition in which “AI takes every wafer.” The relevant quantity is **Non-AI Residual Capacity**:

```text
NonAI_Residual(t)
= Effective_Supply(t)
- AI_Absorption(t)
- Other_Priority_Demand(t)
```

The effect differs by layer:

- smartphones remain TSMC's second-largest platform;
- PCs and conventional servers continue to exist;
- automotive has separate qualification cycles and node structures;
- HBM, RDIMM, advanced packaging, and power-management resources shared with AI/server demand are more exposed to high-value reallocation.

“AI crowding out consumer electronics” should therefore mean a decline in residual capacity at specific scarce layers, not the disappearance of non-AI semiconductor markets.

## 4. China's supply stack must be analyzed by layer

China's capabilities should be described neither as “phones only” nor as a completed frontier-AI full-stack substitute.

### Layer 1 — Smartphone / consumer computing

China can already form a relatively complete parallel supply base across parts of logic, DRAM/NAND, terminal design, system software, and device ecosystems.

### Layer 2 — PC / workstation / general computing

Substitution capability is improving but remains constrained by CPU/GPU ecosystems, advanced nodes, software compatibility, and high-performance memory.

### Layer 3 — Frontier AI system stack

Equivalent substitution for frontier AI requires simultaneous progress in:

- advanced logic;
- HBM-class memory;
- advanced packaging;
- high-speed interconnect;
- compiler/runtime;
- distributed-training software;
- large-scale system deployment.

CXMT's prospectus does not disclose an HBM product line. That is a document-bounded observation, not evidence that no HBM R&D exists.

Whether China's stack can become a second global-scale resource-gravity center remains a scenario variable rather than an accomplished fact.

## 5. Why Intel 1999 is not a complete analogue

Intel's 1999 financials were approximately:

| Metric | 1999 |
|---|---:|
| Net revenue | **US$29.389B** |
| Gross margin | about **59.7%** |
| Operating income | **US$9.767B** |
| Net income | **US$7.314B** |

Public source: Intel Corporation 1999 Annual Report  
https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-05/history-1999-annual-report.pdf

Intel's advantage centered on CPUs, x86 software compatibility, and in-house manufacturing.

Today's AI-platform advantage is broader and more system-dependent. Weakening a leading AI system stack requires more than a second chip with similar benchmark performance. It also requires:

- portable software;
- scalable high-speed interconnect;
- available HBM;
- available advanced packaging;
- deployable rack/pod systems;
- sufficient data-center capacity and power;
- large real workloads.

Chip-share erosion and platform-value-capture erosion are therefore separate events.

## 6. Five major interruption mechanisms

The current trajectory is not irreversible. At least five mechanisms can weaken scarce-layer value capture:

1. **Cloud system-stack substitution** — Google, AWS, Microsoft, and Meta expand substitution across training and inference.
2. **Buyer coordination** — major buyers create stronger alternative demand pools through shared standards, software compatibility, and long-term procurement.
3. **Power constraint** — purchased systems cannot be energized on schedule, reducing utilization, deliveries, and subsequent orders.
4. **China parallel stack** — China closes advanced logic, HBM, packaging, interconnect, and software gaps at sufficient scale.
5. **Regulatory structural remedy** — interface opening, anti-tying remedies, supply restrictions, or structural separation materially lower switching costs.

These variables must be evaluated through public, verifiable events rather than headlines or sentiment.

## 7. Current baseline scenario

As of August 2026, the evidence is most consistent with the following baseline:

- the AI sales unit continues moving toward rack/pod systems;
- NVIDIA's seller-side economics remain very strong;
- advanced packaging and HBM remain scarce;
- cloud custom silicon continues to divert platform profit without eliminating demand for advanced upstream resources;
- power is becoming a deployment constraint alongside packaging and HBM;
- China's supply stack continues to expand, but frontier-AI equivalent substitution is not yet closed across all layers.

This combination corresponds most closely to **S2 — Baseline Concentration**, not permanent monopoly.

If cloud system-stack substitution, buyer coordination, or China's parallel stack accelerates materially, the system can move toward **S1 — Competitive Expansion**. If advanced-resource concentration rises while software and interconnect lock-in strengthen, it can move toward **S3 — Resource Hegemony**. If utilization, token economics, CapEx, and subsequent supply commitments weaken together, the system can enter **S4 — Capital Hard Landing**.

## 8. Falsification conditions

The report should downgrade the thesis of strengthening scarce-layer value capture if several of the following occur:

- NVIDIA supply commitments decline for multiple periods or are materially cancelled;
- TSMC no longer describes advanced packaging as a growth constraint;
- HBM/DRAM supply becomes materially loose;
- cloud custom silicon achieves large-scale frontier-training migration;
- open interfaces materially reduce CUDA/NVLink migration costs;
- large AI data centers show sustained low utilization;
- power connection becomes a disclosed cause of delivery deferral;
- China's parallel AI system stack reaches verifiable scale across advanced logic, HBM, packaging, interconnect, and software.

Conversely, if seller cash flow, capacity commitments, HBM demand, and advanced-packaging tightness continue to strengthen together, the probability mass should shift from S2 toward S3.

---

This volume follows the common evidence system. Company disclosures, institutional research, sell-side estimates, and report stress tests are separated into A/B/C/D grades. See [Research Methodology and Evidence Grading](研究方法与证据分级.en.md), [Core Evidence Ledger](核心证据台账.en.md), and [Core Hypothesis Matrix](核心假设矩阵.en.md).

## Key public sources for this volume

- NVIDIA GB200 NVL72 official product page — 36 Grace CPUs, 72 Blackwell GPUs, 13.4 TB HBM3E, 17 TB LPDDR5X: https://www.nvidia.com/en-us/data-center/gb200-nvl72/
- NVIDIA FY26 official results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
- NVIDIA FY26 10-K: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
- NVIDIA FY27 Q2 official results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- NVIDIA FY27 Q2 10-Q — US$279B manufacturing, supply, and capacity commitments: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
- TSMC 2025 Annual Report: https://investor.tsmc.com/static/annualReports/2025/english/index.html
- TSMC 4Q25 Presentation — 2025 platform mix / growth: https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-01/2506fec872e6b99dc5391618ff38e3cd51ade2dd/4Q25%20Presentation%20%28E%29_WoG.pdf
- TSMC 4Q24 Transcript — advanced packaging and testing >8%: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-01/84aeb15bbe33894365d33f52e027c5268ba95dcf/TSMC%204Q24%20Transcript.pdf
- TSMC 4Q25 Transcript — 2025 advanced packaging slightly above 10%, company-corrected: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
- TSMC 2Q26 Earnings Conference Transcript — packaging capacity limits customers' growth: https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
- TSMC 2025 20-F — annual customer rankings: https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm
- TSMC 2025 consolidated report — Customer A/B: https://www.sec.gov/Archives/edgar/data/1046179/000104617926000024/a2025q4consolidatedreport-.htm
- TrendForce — 2026E HBM + RDIMM = 51% of DRAM bit supply: https://www.trendforce.com/presscenter/news/20260825-13198.html
- Micron FY24 Q2 event page: https://investors.micron.com/events/event-details/microns-second-quarter-2024-financial-call
- Micron FY24 Q2 Prepared Remarks — HBM3E ≈ 3× DDR5 wafer supply: https://s25.q4cdn.com/621799436/files/doc_financials/2024/q2/FY24-Q2-Prepared-Remarks.pdf
- Microsoft FY26 Q4 earnings / call: https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast
- Alphabet 2026 Q2 SEC Exhibit 99.1: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
- Meta 2026 Q2 SEC Exhibit 99.1: https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm
- Amazon 2026 Q2 Form 10-Q: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
