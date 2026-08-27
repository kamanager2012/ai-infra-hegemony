# Volume 29: A breakout analysis of China’s AI chain (Ascend 910C, CANN 8.0, SMIC leading edge, and indigenous substitution)

Chinese original: [vol-29.md](vol-29.md)

Three layers of the China stack are not one layer. CXMT: 0 mentions of HBM. Near gate and far gate: [Volume 12](vol-12.md). This volume does not retell those sentences. It only compares specs that actually appear in the draft: HCCS against NVLink, CANN against CUDA, DUV multi-patterning against a leading-edge node, domestic HBM against Hynix. Running is not breaking the lock.

## 1. The question this volume answers

After export controls put high-end GPUs and leading-edge nodes behind customs, does the Huawei Ascend plus CANN plus SMIC plus CXMT chain replace "can train and infer," or only "can deliver"? There is no addable 910C shipment to knock against NVIDIA FY26 data center 1,937.37 hundred-million dollars. The draft gave no 910C peak FLOPs, HBM capacity, process node, unit price, or shipments, and no concrete SMIC nanometer node or yield. Do not fill them in.

## 2. Draft comparisons that can stay (not promoted)

Ascend 910B / 910C ship with self-designed HCCS chip-to-chip interconnect at 392 GB/s, paired with CloudEngine switches, into a SuperPoD that "supports linear scale-out of thousands of cards." CANN 8.0 aligns operators and auto-tunes against PyTorch and vLLM. Open-source model migration rewrites "fall to under 5%." SMIC uses DUV multi-patterning (SADP / SAQP) to attack a leading-edge "yield balance line." CXMT pushes DDR5 / LPDDR5 into volume and attacks 3D TSV domestic HBM. All of the above are draft numbers. This volume did not read the makers' own documents.

Western fabric for comparison (draft numbers): NVLink 5.0 1.8 TB/s bidirectional per GPU; 72-card backplane 130 TB/s; unified memory 13.8 TB; latency under 100 ns. RoCE 800G at 100 GB/s, 1.5 to 3.0 µs. The judgment's official single cabinet is 13.4 TB HBM plus 17 TB LPDDR, not the same scope as the draft's 13.8 TB. HBM physical ledger and 3:1: [Volume 23](vol-23.md). This volume does not reopen the formula.

## 3. Interconnect wall: 392 GB/s against 1.8 TB/s

Both are draft numbers. The conversion is analysis only: 1.8 TB/s = 1800 GB/s, about 4.6× 392 GB/s. Against a cabinet-class 130 TB/s, a single Ascend HCCS link does not automatically equal "one giant logic chip." The draft claims thousands-of-card linear scale-out with SuperPoD plus CloudEngine. It gives no latency equivalent to under-100 ns unified memory, and no effective compute utilization on collective communication. HCCS scope (uni- or bidirectional, how many links per card, matching latency) is unclear. 4.6× is a rough arithmetic. Do not write it as a measured generation gap.

If a breakout holds, it is more likely "make the cluster larger, trade more cards for per-card bandwidth" plus "use MLA / MoE to cut pathological dependence on unified memory," not catching NVLink 5.0 on a single link. Whether scale-out is truly linear must be tested on communication share. "Thousands of cards" is not proof. The counter also holds: 392 GB/s already sits above RoCE 800G at 100 GB/s (draft numbers). A domestic fabric need not match NVLink to beat an "Ethernet cluster." Good enough and peer are not the same sentence.

SuperPoD "thousands of cards" is a claim, not a cabinet. The judgment's official cabinet is 72 GPUs, 36 Grace, 13.4 TB HBM, 17 TB LPDDR. There is no addable domestic cabinet count to multiply by that spec. There is no domestic packaging split. 5.39: `测算-投片与柜-20260826.md`.

## 4. Software wall: a 5% rewrite is a migration cost, not ecological rent

CANN 8.0 cutting open-source model migration rewrites to under 5% (draft numbers) shows that inference and training frameworks can be pointed at PyTorch / vLLM. That solves "can it run." In an NVIDIA cabinet BOM, 40% to 45% is CUDA / TensorRT-LLM / DOCA and brand premium (draft numbers). That is pricing power after it already runs. It is an estimate, not a segment filing. Do not promote it to verified. What CANN has to match is operator coverage, compiler stability, and multi-generation hardware compatibility, not the line count of one migration patch. 5% is a necessary threshold, not a sufficient moat.

The judgment writes binding software into one stack as one of the interrupt conditions. The embryo is an open interface of the unified-accelerator-library kind. It is not done. The China stack lives on people who cannot buy NVIDIA, not on cheapness punching through CUDA. A 71.1% to 75.0% pad means it can also cut price. Model firms split into "use its stack" and "pay the cloud bill": [Volume 26](vol-26.md). The China stack catches people who cannot buy in the first pile. It does not tear global labs off CUDA. Cheapness does not fill the CUDA tax.

## 5. Manufacturing wall: DUV buys "can make." HBM is still in progress

SMIC walks SADP / SAQP (draft statement). No node, no yield. Multi-patterning trades time, mask count, and overlay error for resolution. Capacity and cost curves differ from single-exposure EUV. Even if logic chips can ship, HBM still has to pass stacks and a base. CXMT "attacking domestic HBM" is progressive tense in the draft. Prospectus: 0 mentions of HBM. The main line is conventional DRAM. See [Volume 12](vol-12.md). 35 × 10,000 wafers per month is not an announcement. Do not write it. Without domestic HBM, a 910C cluster hits the memory-capacity wall first. Interconnect has not had its turn.

TrendForce 2026 Q1 SMIC share 5.1%. SMIC takes phones, TVs, notebooks, and mature nodes, not Azure / GCP training cabinets. Export control and trust: the third item does not pass. Samsung 6.5% can divert Tesla's long, not domestic cabinets. 16,000 / 24,000 / 40,000 wafers per month are not in any announcement.

## 6. Algorithm leverage: why 557.6 × $10,000 is named

DeepSeek used H800 and 278.8 × 10,000 GPU-hours to make 671B / 37B (draft numbers), placed next to the sentence "architectural and algorithm innovation as leverage against a hardware blockade." If a training bill can land at millions of dollars rather than tens of billions in cabinets, export-control damage falls from "cannot make a frontier model" to "cannot make the largest dense model on the highest-bandwidth fabric." Power partly returns from customs to the research team. The premise is that H800-class or Ascend-class supply still exists, and that MLA's 93.3% KV compression holds for Chinese and multimodal tasks. The draft did not measure the latter. 557.6 × $10,000 is a compute conversion, not full cost. The comparison baseline has no sample. This pass did not re-check the paper. Do not write "training is already cheap enough to leave HBM." H800 itself shows that dependence has a license dimension. If the domestic side reproduces on Ascend, the draft comparison is interconnect 392 GB/s against 1.8 TB/s, and CXMT prospectus 0 mentions of HBM. The layer is wrong. Not the same river.

## 7. What this volume does not write

It does not retell the three layers (see [Volume 12](vol-12.md)). It does not reopen the Maia / TPU / Trainium spec table (see [Volume 4](vol-04.md), [Volume 24](vol-24.md)). It does not retell 51% and cabinets-times-spec (see [Volume 5](vol-05.md)). It does not reopen the FY26 and TSMC tables (see [Volume 1](vol-01.md)). It does not write SuperPoD thousands of cards as already-peer cabinets. It does not write a 5% rewrite as already having dug through CUDA.
