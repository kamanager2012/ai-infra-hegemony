# Macro Essay 4: Hyperscaler CapEx, System-Stack Counterattack, and DeepSeek's Architecture-Driven Cost Reduction

Chinese source edition: [part2-04.md](../part2-04.md)

> Retrieval and revision cutoff: **2026-08-27**. Hyperscaler PPE is not an official AI-hardware line item. Cloud custom systems are now real system stacks, but full substitution in frontier training and the external ecosystem remains incomplete.

## 1. The core question

Three forces are interacting at once:

1. hyperscalers are expanding capital expenditure;
2. hyperscalers are building custom system stacks;
3. model architecture is lowering the compute required for some workloads.

The strategic question is:

> **Does architecture-driven efficiency relieve the capital burden, or does it make already-built infrastructure harder to monetize by lowering the unit price of intelligence?**

The answer depends on workload growth and utilization.

## 2. CapEx must be read by company and accounting scope

The four major clouds use different:

- fiscal calendars;
- PPE definitions;
- lease treatment;
- CapEx guidance conventions.

On a mixed-year 2025 basis, comparable equipment/PPE purchases reached roughly **US$354B** in aggregate scale.

By August 2026, company-specific public indicators include:

| Company | Public scope |
|---|---:|
| Microsoft | Calendar-2026 reported CapEx expectation about **US$175B** after the July 29 lease-classification change; underlying investment expectation unchanged |
| Alphabet | Q2 earnings-call 2026 CapEx guidance **US$195–205B** |
| Meta | Q2 2026 CapEx guidance **US$130–145B**, including finance-lease principal |
| Amazon | TTM PPE net purchases actual **US$169.007B** through 2026-06-30 |

These numbers demonstrate continued capital expansion.

They should not be mechanically added into one official four-cloud “AI hardware CapEx” total because the periods and accounting definitions differ.

## 3. PPE and depreciation are different economic objects

A cash-flow statement can show large PPE additions while depreciation reflects assets already placed in service.

For example, Microsoft reported materially different values for:

- additions to property and equipment;
- depreciation, amortization, and other.

The distinction matters because current CapEx can include:

- buildings;
- network assets;
- equipment not yet fully utilized;
- infrastructure with longer lives than servers.

A universal formula such as:

```text
AI Depreciation = Cloud CapEx ÷ 4
```

does not describe the full infrastructure stack.

## 4. Cloud custom silicon has become system-stack competition

The 2026 competitive unit is no longer a naked ASIC.

Google, AWS, Microsoft, and Meta increasingly combine:

- accelerators;
- HBM;
- interconnect;
- compiler/runtime;
- racks or pods;
- orchestration;
- internal workloads.

Examples include:

- Google TPU / Ironwood;
- AWS Trainium / UltraServer / Neuron;
- Microsoft Maia;
- Meta MTIA and its surrounding software stack.

The cloud counterattack has therefore reached the **system level**.

What remains unproven is complete replacement of NVIDIA across:

- broad external developer ecosystems;
- large frontier-training workloads;
- heterogeneous enterprise use.

## 5. Custom systems can lower platform dependence without lowering physical scarcity

A hyperscaler custom stack can reduce:

- external GPU purchases;
- software rent;
- dependence on one system platform.

But the same custom stack can still require:

- leading-edge logic;
- HBM;
- advanced packaging;
- large-scale power.

This creates an important split:

> **Platform concentration can fall while upstream physical competition remains intense.**

A cloud can successfully internalize system profit and still increase demand for TSMC, HBM, packaging, and power.

## 6. DeepSeek changes the unit-cost discussion

DeepSeek-V3 provides a first-party technical anchor:

- **671B** total parameters;
- **37B** activated per token;
- **14.8T** pre-training tokens;
- **2.788M H800 GPU-hours** for the formal training run.

Using the report-side rental assumption of **US$2 per GPU-hour** produces approximately:

```text
2.788M × US$2 ≈ US$5.576M
```

This is not the complete R&D cost.

It excludes:

- research iteration;
- failed experiments;
- payroll;
- infrastructure depreciation;
- data work;
- much of the broader development process.

The number is best interpreted as a **formal training-compute conversion**.

## 7. MLA and efficiency change the demand function

DeepSeek's MLA work demonstrates that architecture can materially reduce KV-cache requirements and improve serving efficiency. The quantitative **93.3% KV-cache reduction** and **5.76× maximum generation throughput** figures belong specifically to **DeepSeek-V2 relative to DeepSeek 67B**; they are not universal savings and should not be merged with DeepSeek-V3's training-compute figures.

The macro implication is not that “hardware no longer matters.”

It is:

> **The same business capability can require fewer bytes, fewer GPU-hours, or lower serving cost.**

That lowers the technical floor for model deployment.

It can also reduce token prices.

For hyperscalers with a large fixed asset base, lower unit prices increase the requirement for higher total usage.

## 8. Private cost reduction vs. public cost reduction

Hyperscaler custom silicon is largely a **private cost reduction**:

- it lowers one cloud's own infrastructure cost;
- competitors do not automatically receive the benefit.

Open model and architecture improvements are closer to a **public cost reduction**:

- they can pressure prices across the market;
- they can be adopted by many buyers.

That creates a strategic tension.

Clouds can simultaneously:

- spend more capital;
- lower their own hardware cost;
- face lower market prices for AI capability.

The balance only works if productive usage and monetization grow fast enough.

## 9. Three macro scenarios

### Scenario A — Parallel expansion

CapEx remains high, custom stacks absorb more internal workloads, and cheaper model architectures increase usage enough to maintain infrastructure returns.

### Scenario B — Unit price falls faster than workload grows

Efficiency and open competition reduce the price of intelligence while utilization fails to expand enough.

The asset base becomes harder to monetize and CapEx slows.

### Scenario C — Architecture reduces the need for large rack-scale inference

A larger share of inference moves to smaller systems or edge devices.

Capital shifts from infrastructure buildout toward workflow software and distribution.

## 10. What to monitor

The most useful indicators are:

- company-specific PPE/CapEx actuals;
- depreciation and utilization;
- production workload share on custom systems;
- external availability of TPU/Trainium/Maia/MTIA;
- token/API pricing;
- open-model training and serving efficiency;
- whether any cloud states that frontier training has materially moved away from external GPU systems.

The macro question is not whether CapEx, custom silicon, or DeepSeek “wins.”

They are three variables in one economic equation:

> **installed capital × utilization × unit price × workload growth**

The long-run winner is the system that keeps **cost per effective unit of intelligence** falling while preserving productive demand and cash return.

## Key public sources for this essay

- Microsoft FY26 Q4 Investor Relations / earnings call, July 29, 2026 — source for the revised calendar-2026 reported CapEx expectation and lease-classification discussion: https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast
- Alphabet Q2 2026 SEC Exhibit 99.1 — Q2 actuals: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
- Alphabet Q2 earnings-call guidance **US$195–205B** — Reuters report of CFO guidance, not a statutory actual: https://www.reuters.com/business/google-quarterly-cloud-revenue-growth-beats-expectations-2026-07-22/
- Meta Q2 2026 SEC Exhibit 99.1 — guidance **US$130–145B**, including finance-lease principal: https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm
- Amazon Q2 2026 10-Q — TTM PPE net purchases actual **US$169.007B**: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
- DeepSeek-V3 Technical Report — 2.788M H800 GPU-hours: https://arxiv.org/abs/2412.19437
- DeepSeek-V2 repository / technical report — 93.3% KV-cache reduction and 5.76× maximum generation throughput relative to DeepSeek 67B: https://github.com/deepseek-ai/DeepSeek-V2
