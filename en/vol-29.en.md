# Volume 29: System-Level Assessment of China's Frontier-AI Parallel Stack

Chinese original: [vol-29.md](vol-29.en.md)

The layered China framework is established in [Volume 12](vol-12.en.md). This volume asks whether the domestic frontier-AI stack closes at the **system level** across accelerator, interconnect, HBM-class memory, advanced packaging, compiler/runtime, deployment scale, and workload performance.

## 1. Core question

China's frontier-AI capability cannot be judged from the existence of one domestic accelerator or one migration layer. The relevant question is whether a parallel system stack can deliver large-scale training and inference with acceptable performance, reliability, software migration cost, and physical supply.

The current evidence supports stronger parallel supply in smartphones, parts of consumer computing, domestic accelerators, networking, and software/runtime development. The unresolved frontier layers remain advanced logic, HBM-class memory, advanced packaging, high-speed system interconnect, software maturity, and scalable deployment.
## 2. Evidence boundary

Historical versions used figures such as specific HCCS bandwidth, “thousands of cards” scale-out, sub-5% migration rewrite, and direct NVLink-versus-HCCS ratios. Unless supported by current first-party documentation and like-for-like benchmarks, those values remain unverified engineering claims.

Current hard boundaries include:
- CXMT's prospectus did **not** disclose an HBM product line;
- SMIC's global foundry revenue share does not imply frontier-node equivalence;
- DeepSeek demonstrates an algorithmic-efficiency lever, but its formal training still used H800 hardware;
- CANN and Ascend demonstrate that a parallel software/hardware stack is being built;
- equivalent frontier substitution requires the full system, not one chip or one compiler.
## 3. Interconnect: benchmark comparable systems, not isolated link numbers

Both are historical stress-test values. The conversion is analysis only: 1.8 TB/s = 1800 GB/s, about 4.6× 392 GB/s. Against a cabinet-class 130 TB/s, a single Ascend HCCS link does not automatically equal "one giant logic chip." historical stress-test material claims thousands-of-card linear scale-out with SuperPoD plus CloudEngine. It gives no latency equivalent to under-100 ns unified memory, and no effective compute utilization on collective communication. HCCS scope (uni- or bidirectional, how many links per card, matching latency) is unclear. 4.6× is a rough arithmetic. The report does not treat it as a measured generation gap.

If a breakout holds, it is more likely "make the cluster larger, trade more cards for per-card bandwidth" plus "use MLA / MoE to cut pathological dependence on unified memory," not catching NVLink 5.0 on a single link. Whether scale-out is truly linear must be tested on communication share. "Thousands of cards" is not proof. The counter also holds: 392 GB/s already sits above RoCE 800G at 100 GB/s (historical stress-test values). A domestic fabric need not match NVLink to beat an "Ethernet cluster." Good enough and peer are not the same sentence.

SuperPoD "thousands of cards" is a claim, not a cabinet. The judgment's official cabinet is 72 GPUs, 36 Grace, 13.4 TB HBM, 17 TB LPDDR. There is no addable domestic cabinet count to multiply by that spec. There is no domestic packaging split. 5.39: `测算-投片与柜-20260826.md`.

## 4. Software wall: a 5% rewrite is a migration cost, not ecosystem switching power

CANN 8.0 cutting open-source model migration rewrites to under 5% (historical stress-test values) shows that inference and training frameworks can be pointed at PyTorch / vLLM. That solves "can it run." In an NVIDIA cabinet BOM, 40% to 45% is CUDA / TensorRT-LLM / DOCA and brand premium (historical stress-test values). That is pricing power after it already runs. It is an estimate, not a segment filing. It remains outside the first-party fact layer. What CANN has to match is operator coverage, compiler stability, and multi-generation hardware compatibility, not the line count of one migration patch. 5% is a necessary threshold, not a sufficient moat.

Open cross-architecture interfaces can reduce migration cost, but public evidence does not yet show negligible switching cost for frontier workloads across CUDA, CANN, and other stacks. The current China stack is driven by constrained access, domestic demand, strategic autonomy, and improving system capability—not by a demonstrated global cost advantage over CUDA-based frontier systems. A 71.1% to 75.0% pad means it can also cut price. Model firms split into "use its stack" and "pay the cloud bill": [Volume 26](vol-26.en.md). The current China stack is strongest where constrained access, domestic demand, and strategic autonomy support adoption. That is not the same as demonstrating global frontier-workload migration away from CUDA at low switching cost.

## 5. Manufacturing: logic progress does not automatically close HBM and packaging

SADP / SAQP are useful manufacturing mechanisms to discuss, but specific SMIC node and yield assumptions remain unverified here. Multi-patterning trades time, mask count, and overlay error for resolution. Capacity and cost curves differ from single-exposure EUV. Even if logic chips can ship, HBM still has to pass stacks and a base. CXMT "attacking domestic HBM" is progressive tense in historical stress-test material. Prospectus: 0 mentions of HBM. The main line is conventional DRAM. See [Volume 12](vol-12.en.md). 35 × 10,000 wafers per month is not an announcement. The report does not treat it. Without domestic HBM, a 910C cluster hits the memory-capacity wall first. Interconnect has not had its turn.

TrendForce 2026 Q1 SMIC share 5.1%. SMIC takes phones, TVs, notebooks, and mature nodes, not Azure / GCP training cabinets. Export control and trust: the third item does not pass. Samsung 6.5% can divert Tesla's long, not domestic cabinets. 16,000 / 24,000 / 40,000 wafers per month are not in any announcement.

## 6. Algorithmic efficiency is leverage, not supply-chain closure

DeepSeek used H800 and 278.8 × 10,000 GPU-hours to make 671B / 37B (historical stress-test values), placed next to the sentence "architectural and algorithm innovation as leverage against a hardware blockade." Lower formal-training compute cost can reduce the amount of scarce hardware required for some frontier workloads, but it does not by itself remove memory, packaging, interconnect, or availability constraints. Power partly returns from customs to the research team. The premise is that H800-class or Ascend-class supply still exists, and that MLA's 93.3% KV compression holds for Chinese and multimodal tasks. historical stress-test material did not measure the latter. 557.6 × $10,000 is a compute conversion, not full cost. The comparison baseline has no sample. the current evidence review did not re-check the paper. The report does not treat "training is already cheap enough to leave HBM." H800 itself shows that dependence has a license dimension. If the domestic side reproduces on Ascend, historical stress-test material comparison is interconnect 392 GB/s against 1.8 TB/s, and CXMT prospectus 0 mentions of HBM. The layer is wrong. Not the same river.

## 7. What this volume does not write

It does not retell the three layers (see [Volume 12](vol-12.en.md)). It does not reopen the Maia / TPU / Trainium spec table (see [Volume 4](vol-04.en.md), [Volume 24](vol-24.en.md)). It does not retell 51% and cabinets-times-spec (see [Volume 5](vol-05.en.md)). It does not reopen the FY26 and TSMC tables (see [Volume 1](vol-01.en.md)). It does not write SuperPoD thousands of cards as already-peer cabinets. It does not write a 5% rewrite as already having dug through CUDA.
