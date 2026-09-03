# Phase II · Developer Distribution Chokepoint v0.6

> **Status:** Research-side validation layer; not a claim that software monopoly or foreclosure has already occurred.  
> **Evidence-cutoff interaction:** the Reuters transaction report is dated 2026-08-27 and therefore falls inside the formal report's 2026-08-28 evidence snapshot. Any status check after 2026-08-28 remains research-side only unless the formal report is explicitly reopened.

## 0. Ownership contract v0.6

This file owns:
- transaction-status gating for the NVIDIA/Hugging Face research trigger;
- DDC-A / DDC-B / DDC-C distribution-conduct states;
- ranking / backend / portability / multi-homing / deployment-friction evidence;
- contrary evidence against foreclosure;
- adjacent **Model Production Gravity** evidence only where it directly changes the developer-distribution mechanism.

It does **not** own:
- antitrust liability or legal remedy conclusions;
- S1–S4 aggregation — `10` owns scenario relevance;
- live capital-clearing state — `01A` owns clearing adjudication;
- formal-report wording — frozen unless explicitly reopened.

Hard rule:

> **A distribution/competition state may affect scenario persistence, but it cannot be promoted into a capital-clearing state or legal monopoly conclusion by this file alone.**

## 1. Trigger event

Reuters reported on 2026-08-27, citing The Information, that NVIDIA had agreed to acquire Hugging Face for approximately **US$12.9B**.

The report does **not** treat that as a completed acquisition because, as of the evidence cutoff, the formal source set did not contain a NVIDIA or Hugging Face closing / merger-approval announcement.

This distinction is mandatory:

```text
reported agreement
≠ first-party verified definitive agreement
≠ regulatory approval
≠ closed transaction
≠ realized platform conduct
```

### 1.1 Transaction-status gate v0.4

As of the **2026-09-03 research-side status check**:

| State | Evidence status | Research treatment |
|---|---|---|
| media-reported agreement | **Observed** — Reuters reported NVIDIA agreed to acquire Hugging Face for ~US$12.9B, citing The Information | valid trigger for vertical-integration monitoring |
| first-party definitive-agreement announcement | **not verified in the current first-party source set** | do not upgrade transaction status |
| regulatory approval / clearance | **not verified** | do not infer approval from agreement reporting |
| legal closing / ownership transfer | **not verified** | do not write “NVIDIA owns Hugging Face” as a current fact |
| post-transaction platform conduct | **not observable as ownership conduct until ownership/control is verified** | DDC-B/C cannot be inferred from pre-closing product behavior |

A fresh 2026-09-03 check of NVIDIA Newsroom / Investor Relations and Hugging Face's official blog did not surface a first-party definitive-agreement, regulatory-clearance, or closing announcement in the reviewed source set.

This is a **status-control result**, not proof that no private signed document exists.

Hard rule:

> **The ledger tracks what can be publicly verified, not what may exist privately.**

## 2. Why Hugging Face matters structurally

Hugging Face's official product surface spans:

- Hub / model repositories;
- datasets;
- Spaces;
- Transformers;
- inference providers / endpoints;
- deployment and developer tooling.

The mechanism under test is therefore not "NVIDIA buys a website."

It is:

```text
Accelerator
→ CUDA / runtime
→ model discovery / distribution
→ optimization artifact
→ inference / deployment path
→ accelerator demand
```

If ownership changes the defaults across those layers, platform power can move upstream from execution into the developer funnel.

## 3. Proposed mechanism: Developer Distribution Chokepoint

A chokepoint exists only if control of a major distribution gateway changes **real developer choice**.

Potential reinforcing loop:

```text
NVIDIA installed base
→ more CUDA software assets
→ more NVIDIA-optimized model artifacts / benchmarks
→ lower NVIDIA deployment friction
→ more workloads deployed on NVIDIA
→ more model creators optimize for NVIDIA first
→ stronger NVIDIA installed base
```

The loop is a hypothesis until observable conduct and workload outcomes support it.

## 3A. Adjacent mechanism — Model Production Gravity v0.5

The Hugging Face trigger concerns **distribution**.

A separate but adjacent pre-cutoff development concerns NVIDIA's potential influence over **open-model production capability**.

Media reports in August 2026 described a Poolside / NVIDIA transaction structure involving:
- approximately **US$6B** for a non-exclusive license to Poolside's model-development technology / Model Factory;
- approximately **US$1B** of NVIDIA equity investment;
- transfer / hiring of more than 100 Poolside personnel into NVIDIA-linked model work, including Nemotron.

The current research source set does **not** contain a first-party NVIDIA or Poolside transaction announcement confirming all of those commercial terms.

Therefore the transaction identity remains:

> **C-grade media-reported license / investment / talent-transfer structure.**

It must not be rewritten as:
- NVIDIA acquired Poolside;
- NVIDIA owns Poolside's Model Factory;
- Poolside ceased to exist independently;
- NVIDIA obtained exclusive control of Poolside technology.

### 3A.1 First-party capability anchor: Poolside Model Factory

Poolside's **May 25, 2026 Laguna M.1 / XS.2 Technical Report** provides first-party evidence for what the relevant capability actually is.

Poolside describes its Model Factory as a tightly integrated system combining:

```text
versioned data
+
training
+
evaluation
+
inference
```

to turn model development into an industrial process.

That matters because the strategic object is not merely one model checkpoint.

It is a **repeatable model-production system**.

The report also states that Laguna models were trained end-to-end inside this Model Factory, and that Laguna XS.2 weights were released under Apache 2.0.

### 3A.2 NVIDIA first-party open-model anchor

NVIDIA's own August 11, 2026 materials show that Nemotron is already being developed as an open / customizable model family for agentic workloads.

Nemotron 3.5 Lightning:
- is a 30B-parameter MoE model with 3B active parameters;
- is positioned for high-volume, long-running agentic execution;
- ships with open/customizable weights, training data / recipes and NVIDIA optimization tooling;
- is distributed through NVIDIA channels and Hugging Face.

Therefore the relevant strategic question is no longer only:

> "Does NVIDIA have CUDA?"

It is increasingly:

> **How much of the model-production → distribution → deployment chain becomes economically coordinated around NVIDIA?**

### 3A.3 Model Production Gravity mechanism

The adjacent loop is:

```text
Compute / CUDA installed base
→ model-production tooling + training infrastructure
→ model talent / training recipes / evaluation systems
→ NVIDIA open-model family
→ distribution through major model hubs
→ NVIDIA-optimized deployment
→ accelerator demand
```

This report calls the upstream mechanism:

> **Model Production Gravity (MPG)**

MPG is distinct from DDC:

- **MPG** asks whether model-creation capability, tooling, talent and production systems increasingly gravitate toward NVIDIA.
- **DDC** asks whether a distribution gateway changes developer choice through ranking, defaults, economics or deployment friction.

They can reinforce each other, but neither proves the other.

### 3A.4 Combined vertical-loop hypothesis

If both mechanisms strengthen, the possible stack becomes:

```text
GPU / networking / systems
→ CUDA / NeMo / runtime
→ model-production capability
→ NVIDIA open models
→ major model distribution gateway
→ inference / deployment
→ GPU demand
```

This would be strategically more important than CUDA lock-in alone because it could influence both:

1. **what models get built / optimized**, and
2. **how developers discover and deploy them**.

But current evidence supports only the **possibility of a reinforcing vertical loop**, not completed control.

### 3A.5 Minimum MPG observables

| Variable | Strengthens MPG | Contrary evidence |
|---|---|---|
| Model-production technology control | exclusive or effectively exclusive access to important training/eval systems | non-exclusive licensing; independent continued development |
| Talent concentration | sustained transfer of model-training teams into NVIDIA | independent teams remain viable / expand elsewhere |
| Training-recipe dependence | NVIDIA tooling becomes required for competitive open models | recipes remain portable across training stacks |
| Model-family production cadence | NVIDIA open-model releases accelerate materially | broad independent open-model ecosystem remains competitive |
| Hardware coupling | model training / quantization / serving artifacts become NVIDIA-specific by default | models remain efficiently portable to competing accelerators |
| Distribution coupling | NVIDIA-produced models receive preferential placement / tooling | neutral multi-homing and equal discoverability persist |
| Economic bundling | compute credits / hosting / tooling / distribution are bundled | independent pricing and provider choice remain viable |

### 3A.6 Hard boundary: open models can strengthen NVIDIA without constituting foreclosure

NVIDIA can rationally invest in permissive/open models because wider open-model adoption can increase accelerator demand.

That alone is not anticompetitive.

MPG becomes a competition concern only if the economic path changes from:

> **better open-model capability creates more competition**

toward:

> **model production becomes practically dependent on NVIDIA-controlled tooling, talent, financing or hardware, while competing production paths become materially less viable.**

The distinction is essential.

### 3A.7 Relationship to the Poolside media reports

The reported Poolside structure is strategically notable precisely because it is described as a **license / investment / talent** arrangement rather than a conventional full acquisition.

If verified, that could allow NVIDIA to absorb important capability without necessarily buying the whole company.

Research implication:

> **vertical concentration should track control of capability, talent and dependency — not only legal ownership.**

But because the commercial terms remain media-reported in the current source set, they do not change a formal concentration state by themselves.

### 3A.8 Current MPG state

Current evidence supports:

> **MPG-WATCH — NVIDIA has a first-party open-model strategy and media reports describe a potentially material Poolside model-production license/talent relationship, but exclusive control, dependency, or foreclosure are not established.**

This MPG-WATCH label is an **adjacent research state**, not DDC-B.

The DDC state remains separately adjudicated below.

---

## 3B. Capability Absorption Without Acquisition (CAWA) v0.6

The Poolside line suggests a broader mechanism that should not be reduced to model-production gravity.

NVIDIA can potentially absorb economically important capability through:

```text
non-exclusive technology license
+
key-personnel transfer
+
product integration
+
ecosystem certification / distribution
```

without acquiring the underlying company.

This research pattern is called:

> **Capability Absorption Without Acquisition (CAWA)**

CAWA is not automatically anticompetitive.

It is a control / dependency question:

> **How much practical capability moves into the platform even when legal ownership of the source company does not?**

### 3B.1 First-party positive case — Groq

Groq provides a substantially stronger evidence anchor than the Poolside media reports.

On **December 24, 2025**, Groq officially announced:

- a **non-exclusive licensing agreement** with NVIDIA for Groq inference technology;
- Groq founder **Jonathan Ross**;
- Groq president **Sunny Madra**;
- and other Groq team members

would join NVIDIA to help advance and scale the licensed technology.

Groq simultaneously stated that:

- Groq would continue operating as an **independent company**;
- GroqCloud would continue operating.

This is a clean first-party example of:

> **technology capability + key people transfer without corporate acquisition.**

### 3B.2 Capability moved from license into NVIDIA product stack

The case is stronger because the licensed capability did not remain an abstract agreement.

On **August 24, 2026**, NVIDIA officially announced **NVIDIA Groq 3 LPX** in full production as an extension of the Vera Rubin platform.

That creates an observable sequence:

```text
Groq independent technology
→ non-exclusive NVIDIA license
→ founder / senior-team transfer
→ NVIDIA product integration
→ Vera Rubin system-stack deployment
```

This is first-party evidence that legal ownership is not the only relevant measure of platform capability accumulation.

### 3B.3 Groq remains a counterexample to “absorption = destruction”

The same case also provides mandatory contrary evidence.

Groq:
- remained an independent legal company;
- continued GroqCloud;
- raised new growth capital in 2026;
- joined NVIDIA Cloud Partner while continuing to operate its own cloud business.

Therefore the case does **not** support:

> NVIDIA acquired Groq and eliminated the competitor.

A more precise statement is:

> **NVIDIA internalized licensed inference capability and key personnel while the source company continued operating independently.**

That distinction matters for competition analysis.

### 3B.4 Poolside as a second, lower-confidence candidate

The Poolside evidence is structurally similar but weaker in transaction verification.

Current evidence stack:

**A-grade capability evidence**
- Poolside first-party technical report confirms the Model Factory as an integrated model-development system.

**C-grade transaction evidence**
- media reports describe a large non-exclusive NVIDIA license;
- NVIDIA investment;
- movement of substantial Poolside personnel into NVIDIA/Nemotron work.

Until first-party transaction confirmation is available:

> **Poolside is a CAWA candidate, not a first-party closed case.**

### 3B.5 CAWA observables

| Variable | Stronger capability absorption | Contrary evidence |
|---|---|---|
| License scope | broad rights to commercially important technology | narrow / non-core license |
| Exclusivity | exclusive or effectively exclusive rights | genuinely non-exclusive rights with active third-party use |
| Key-person dependency | founders / core research or engineering team move | source company retains comparable core team |
| Product integration | technology becomes named platform component | license remains unused / peripheral |
| Source-company viability | independent roadmap weakens materially after transfer | company raises capital, ships product, grows independently |
| Ecosystem coupling | source company becomes dependent on NVIDIA certification / compute / distribution | multi-vendor commercial path remains viable |
| Repeat pattern | similar license+talent structures occur across multiple capability layers | isolated one-off transaction |
| Substitution impact | rival capability becomes harder to access outside NVIDIA | technology remains broadly licensable / competitive alternatives expand |

### 3B.6 CAWA is different from M&A

Traditional merger analysis starts from:

> who owns the company?

CAWA requires an additional question:

> **who controls or internalizes the economically important capability after licensing and personnel movement?**

This matters in fast-moving AI markets where:
- talent is highly concentrated;
- software / model-production systems are portable;
- IP can be licensed rather than purchased;
- integration speed can matter more than legal ownership.

The correct denominator is therefore not:

> number of acquired startups.

It is closer to:

> **capability concentration after transaction / licensing / talent flows.**

### 3B.7 CAWA and antitrust boundary

CAWA does not itself prove foreclosure.

Competition concern rises if several elements align:

```text
critical capability licensed / internalized
+
core personnel migrate
+
NVIDIA product stack integrates capability
+
source-company or rival access weakens
+
repeat pattern across multiple layers
```

Groq currently confirms the first three elements strongly.

It does **not** establish that Groq or other rivals lost market access.

Poolside may provide a second cross-layer example, but transaction confirmation is weaker.

### 3B.8 Relationship among the three mechanisms

Keep the mechanisms separate:

**CAWA**
> How does NVIDIA internalize third-party capabilities without buying the legal entity?

**MPG**
> Are model-production systems / talent / recipes concentrating around NVIDIA?

**DDC**
> Does model distribution / deployment control change developer choice?

Potential combined loop:

```text
CAWA
→ more internal model / inference capability
→ MPG strengthens
→ NVIDIA open-model / inference stack improves
→ DDC becomes more valuable if distribution control is obtained
→ more workloads flow into NVIDIA deployment paths
```

This is a hypothesis chain, not a current foreclosure finding.

### 3B.9 Current CAWA state

Current research state:

> **CAWA-OBSERVED**

Reason:
- Groq provides first-party confirmation of non-exclusive technology licensing + key-person transfer + subsequent NVIDIA product integration.

But:

> **CAWA-OBSERVED ≠ CAWA-FORECLOSURE.**

No evidence threshold for foreclosure has been met.

### 3B.10 Formal-report reopen gate

Groq / Poolside are both **pre-2026-08-28 events**, but Phase II does not automatically reopen formal Ch02/Ch11.

Current adjudication:

> **HOLD — research-side mechanism materially strengthens the evidence for platform capability accumulation, but does not contradict the formal report's existing system-stack thesis or change the S2 baseline.**

Formal reopening becomes justified only if one of these occurs:

1. CAWA repeats across enough independent layers to become a defining NVIDIA strategy rather than isolated transactions;
2. capability access outside NVIDIA demonstrably deteriorates;
3. formal text contains a materially false implication that legal acquisition is required for platform integration;
4. the combined CAWA + MPG + DDC loop changes the competition judgment.

---

## 4. Minimum observable variables

| Variable | Supportive evidence | Contrary evidence |
|---|---|---|
| Default ranking / discovery | NVIDIA-optimized artifacts receive systematic preferential placement | ranking remains vendor-neutral / user-controlled |
| Runtime neutrality | first-party flows default to CUDA/TensorRT/NIM while alternatives lose first-class paths | ROCm/XLA/CPU/other backends retain equivalent first-class integration |
| Benchmark neutrality | official evaluations systematically privilege NVIDIA-specific stacks | methodology stays hardware-neutral and reproducible |
| Deployment friction | non-NVIDIA deployment requires more manual steps / loses managed features | multi-vendor endpoint and local deployment paths remain comparable |
| Artifact portability | NVIDIA-specific containers/quantizations become de facto required | model weights and formats remain portable / mirrorable |
| Commercial terms | pricing / visibility / credits favor NVIDIA-linked deployment | terms remain non-discriminatory |
| Model-creator behavior | important creators publish NVIDIA-optimized variants first/exclusively | creators multi-home and publish equivalent variants |
| Workload distribution | production open-model workloads concentrate further on NVIDIA because of the distribution path | production deployment remains multi-vendor |
| Alternative hubs | competitors are forced to build mirrors / registries to preserve reach | alternative distribution remains optional rather than defensive |

## 4A. Pre-control / unverified-control neutrality baseline v0.4

A useful foreclosure test requires a **before-state**.

As of 2026-09-03, transaction control is still not first-party verified in the research source set. Therefore current Hugging Face product behavior must be recorded as:

> **baseline platform conduct — not post-acquisition conduct.**

### 4A.1 Local / heterogeneous-device path

On **2026-09-02**, Hugging Face published `@huggingface/kernels`, describing more than 200 WebGPU kernels intended to make browser/local inference fast across **many different devices and browser implementations**.

Research interpretation:

- this is contrary evidence against an already-realized NVIDIA-only execution narrowing;
- WebGPU/local execution preserves a route that is not conceptually tied to one CUDA cloud backend;
- but because ownership/control is not verified, this cannot be credited to or blamed on NVIDIA post-transaction governance.

### 4A.2 Multi-provider inference baseline

Hugging Face's official Inference Providers architecture continues to expose multiple serverless providers through Hub model pages and SDKs.

The baseline provider architecture includes non-NVIDIA-owned providers and is designed around provider choice rather than one mandatory backend.

This establishes a future comparison point for:

- provider count;
- provider-selection defaults;
- default ordering / recommendation;
- SDK parity;
- model availability by provider;
- pricing / credit treatment;
- NVIDIA-linked vs non-NVIDIA-linked backend visibility.

### 4A.3 Baseline rule

If control is later verified, DDC monitoring should compare future conduct against this dated baseline.

Do not ask only:

> "Are alternative providers still technically present?"

Ask:

> **Did their default visibility, feature parity, economics, or deployment friction deteriorate relative to the pre-control baseline?**

This makes self-preferencing testable.

### 4A.4 Current DDC state

Given:
- no first-party verified control transfer;
- continuing heterogeneous-device / local-runtime work;
- continuing multi-provider inference architecture;

the research state remains:

> **DDC-A / transaction-status WATCH — potential vertical-integration risk, no realized foreclosure evidence.**

DDC-A here does **not** mean the reported transaction is economically unimportant.

It means the conduct threshold for DDC-B has not been met.

---

## 5. Three research states

### DDC-A — Neutral ownership / no foreclosure evidence

- transaction may close;
- multi-vendor parity remains;
- open assets remain portable;
- alternative runtimes retain first-class support;
- no measurable increase in migration friction.

### DDC-B — Self-preferencing watch

- ranking, endpoint defaults, optimization artifacts, or commercial terms begin to favor NVIDIA;
- alternatives remain technically possible but require more work;
- multi-homing starts to increase defensively.

This is a competition-risk state, not yet proof of foreclosure.

### DDC-C — Distribution foreclosure

Require cross-confirmation:

- persistent self-preferencing;
- rising non-NVIDIA migration friction;
- declining first-class support for competing runtimes / accelerators;
- material developer/workload concentration attributable to the gateway;
- alternative hubs / mirrors become necessary to retain reach;
- preferably regulatory or contractual evidence of discriminatory treatment.

No fixed numeric threshold is assigned in v0.1.

## 6. Hard anti-overreach rules

Do not infer:

- reported acquisition = closed acquisition;
- platform ownership = ownership of model IP;
- Hugging Face control = control of all open source / open-weight AI;
- CUDA strength + Hugging Face ownership = completed software monopoly;
- technical presence of AMD/Intel/CPU backends = effective competitive parity;
- one default setting = systemic foreclosure.

The correct test is **persistent conduct + switching-cost effect + workload consequence**.

## 7. Countervailing mechanisms

The mechanism should lose weight if:

- open-weight models remain easily mirrorable;
- model creators systematically multi-home;
- alternative registries grow without major coordination cost;
- framework/runtime portability improves;
- neutral foundation governance expands around critical libraries;
- cloud marketplaces and local runtimes preserve independent distribution;
- regulators impose effective interoperability / non-discrimination remedies.

## 8. Relationship to existing report mechanisms

### Ch02 — System Stack

DDC extends CUDA lock-in upstream:

```text
traditional:
workload → runtime → accelerator

DDC:
model discovery → tooling → runtime → deployment → accelerator
```

### Ch18 — Antitrust

The relevant legal/economic question is **vertical foreclosure / self-preferencing**, not merely horizontal market share.

### Ch24 / S4

DDC is not a capital-clearing signal.

However, if a distribution chokepoint materially increases platform rents or slows substitution, it can increase the persistence of S2/S3 concentration states.

## 9. Monitoring protocol

At each major Hugging Face / NVIDIA ownership or product update, record:

1. transaction status;
2. governance / board / control structure;
3. ranking/recommendation changes;
4. backend/provider defaults;
5. changes in ROCm/XLA/CPU/other accelerator support;
6. endpoint / inference-provider parity;
7. model-creator multi-homing;
8. mirror / export / API portability;
9. commercial incentives / credits / bundling;
10. regulatory review / remedy;
11. observed production-workload distribution.

Every supportive observation must be paired with counterevidence.

## 10. Current v0.6 judgment

Current evidence supports three distinct mechanisms with different evidence status:

> **DDC:** a media-reported Hugging Face acquisition agreement with potentially high strategic relevance because, if verified and completed, it could connect accelerator/runtime power to a major open-model developer-distribution gateway.

> **MPG:** a first-party NVIDIA open-model strategy plus media-reported Poolside model-production licensing / investment / talent-transfer arrangements that could strengthen NVIDIA's upstream model-production capability.

> **CAWA:** first-party Groq evidence confirms that NVIDIA can internalize important inference technology and key personnel through a non-exclusive license while the source company remains legally independent; this is capability absorption, not proof of foreclosure.

Current evidence does **not** establish:

> **completed Hugging Face acquisition, realized self-preferencing, Poolside acquisition, exclusive model-production control, distribution foreclosure, or software monopoly.**

That boundary should remain in place until transaction status is first-party verified and, if control changes, post-transaction conduct can then be observed.

## Sources

- Reuters, 2026-08-27, “Nvidia agrees to buy Hugging Face for $12.9 billion, The Information reports”: https://www.reuters.com/technology/nvidia-talks-acquire-hugging-face-13-billion-deal-business-insider-reports-2026-08-27/
- NVIDIA Newsroom / Investor Relations — first-party transaction-status cross-check; no definitive-agreement / closing announcement identified in the source set reviewed for the 2026-09-03 research-side status gate: https://nvidianews.nvidia.com/news ; https://investor.nvidia.com/news-and-events/news-and-events/default.aspx
- Hugging Face official documentation: https://huggingface.co/docs
- Hugging Face Hub documentation: https://huggingface.co/docs/hub/index
- Hugging Face Transformers documentation: https://huggingface.co/docs/transformers/index


- Poolside Team, “Laguna M.1/XS.2 Technical Report,” 2026-05-25 — first-party Model Factory capability anchor: https://poolside.ai/assets/laguna/laguna-m1-xs2-technical-report.pdf
- The Information, 2026-08-20 — media report on approximately US$6B NVIDIA licensing arrangement with Poolside; C-grade transaction evidence: https://www.theinformation.com/briefings/nvidia-pay-6-billion-license-software-ai-startup-poolside
- Forbes, 2026-08-24 — secondary report on reported Poolside licensing/investment/personnel structure; corroborative only, not first-party: https://www.forbes.com/sites/jonmarkman/2026/08/24/nvidia-pays-poolside-6b-to-license-its-model-factory-and-109-workers/
- NVIDIA, 2026-08-11, Nemotron 3.5 Lightning / NeMo Switchyard — first-party open-model strategy anchor: https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/
- NVIDIA Nemotron 3.5 Lightning training recipe — first-party reproducible training/deployment tooling: https://docs.nvidia.com/nemotron/nightly/nemotron/lightning35/README.html


- Groq, 2025-12-24, “Groq and Nvidia Enter Non-Exclusive Inference Technology Licensing Agreement to Accelerate AI Inference at Global Scale” — first-party confirmation of non-exclusive technology license, founder/president/team transfer, and continued Groq independence: https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale
- Groq, 2026-06-22, growth-capital announcement — first-party contrary evidence that Groq continued operating and financing independently after the NVIDIA license: https://groq.com/newsroom/groq-raises-usd650m-to-scale-its-ai-inference-cloud-business
- Groq, 2026-08-12, NVIDIA Cloud Partner announcement — first-party evidence of deepened ecosystem integration after the licensing agreement: https://groq.com/newsroom/groq-becomes-an-nvidia-cloud-partner
- NVIDIA, 2026-08-24, “NVIDIA Groq 3 LPX Now in Full Production” — first-party evidence that licensed Groq capability became an integrated Vera Rubin platform component: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Groq-3-LPX-Now-in-Full-Production-With-World-Class-Speed-for-Agentic-AI/default.aspx
