# Public Release Gate

**Repository:** `kamanager2012/ai-infra-hegemony`  
**Target:** first public publication of *The Age of AI Infrastructure Hegemony*  
**Research retrieval/revision cutoff:** 2026-08-28  
**Publication QA state:** 2026-08-28

This checklist separates research completion from publication operations. A checked research item means the underlying content has been reviewed; it does not imply that the repository has already been made public.

## 1. Research corpus

- [x] Chinese 40-volume corpus reviewed as source of truth.
- [x] Eight Chinese macro essays reviewed.
- [x] English 40-volume edition completed repository-wide publication QA.
- [x] Eight English macro essays structurally synchronized and publication-QA reviewed.
- [x] Root release page is English-first.
- [x] Chinese full landing page is available at `README.zh-CN.md`.
- [x] English and root indexes match the actual H1 titles for 40 volumes + 8 macro essays.
- [x] F→H→M→S→X ontology is synchronized across the release framework.
- [x] A/B/C/D evidence grading is synchronized across the release framework.
- [x] Targeted regression is clear for legacy workpaper phrasing, stale FY27 Q2 outlook framing, fixed 40/30/15/15 scenario weights, malformed unit capitalization, hidden control characters, and known bad Chinese-source link patterns.
- [x] Seven-way read-only fact audit findings were reconciled against public sources and current `main`: TSMC customer-series logic, smartphone share/growth scope, TrendForce 51% forecast status, rack-power scope, Gaming supply wording, packaging wording, rack power, four-cloud guidance timing, and English omissions were corrected.
- [x] NVIDIA manufacturing, supply, and capacity commitments are updated through FY27 Q2: **US$95.2B → US$119B → US$279B**, with the Q2 SEC source and supplier-allocation boundary preserved.
- [x] Repository-wide high-risk required-source regression passed for the Chinese research layer: **48/48** files (40 volumes + 8 macro essays) returned no missing required source anchor after remediation.
- [x] Equivalent English high-risk required-source regression passed: **48/48** files returned no missing required source anchor.
- [x] Deterministic CI gate added at `scripts/check-required-sources.py` and wired into `.github/workflows/links.yml`; the combined gate covers **96/96** research files.
- [x] Machine-readable high-risk claim ledgers exist for both languages with **32 verified records each**, identical `bilingual_id` sets, no duplicate claim IDs, and all referenced English research files present.
- [x] Central stale-scope regression is clear for the known 9622.1 conversion error, current-only US$119B wording, outdated four-cloud guidance, 51% forecast-as-actual wording, and stale 100 kW rack framing.
- [x] Complete deterministic **every-number source-coverage audit** across the bilingual research layer: Chinese **48/48** + English **48/48**. Final strict pass: **1,052 unit-bearing numeric candidates / 0 unresolved**.
- [ ] Complete lower-risk **semantic claim-by-claim editorial verification** where required. The strict gate proves traceability / model-boundary identity; high-risk claims are separately semantically verified in the bilingual claim ledgers. Do not describe structural source coverage as proof that every lower-risk source supports every sentence verbatim.

## 2. Publication metadata

- [x] `CITATION.cff` no longer declares CC BY 4.0 or an obsolete release date.
- [x] `CITATION.cff` uses an English-first title and a `preferred-citation` with `type: book` for the monograph.
- [x] `RELEASE_NOTES.md` distinguishes the current `main` research state from the archival `v0.1.0` snapshot.
- [x] `CONTRIBUTING.md` reflects the current bilingual publication state.
- [x] X/social launch copy points to the English root landing page and the correct Chinese landing page.
- [ ] Final repository description / About text set on GitHub.
- [ ] Final public release tag created.

## 3. Licensing — hard gate

- [x] Replace the previous license with the standard `CC-BY-NC-ND-4.0` license before changing repository visibility to public.
- [x] Ensure `LICENSE`, README files, and `CITATION.cff` all declare `CC-BY-NC-ND-4.0` consistently.
- [x] Confirm treatment of quotations, third-party figures, and source excerpts separately from original report text.
- [x] Confirm that the selected standard license prohibits commercial use and sharing derivative/adapted material. Note: it still permits noncommercial sharing of unadapted material under its terms.

**License hard gate passed:** the repository uses the standard SPDX-listed **CC-BY-NC-ND-4.0** license. Commercial use is prohibited; shared copies must remain unadapted and attributed under the license terms.

## 4. Final release verification

- [x] Re-read the remote `LICENSE`, `README.md`, `README.zh-CN.md`, `CITATION.cff`, `CONTRIBUTING.md`, `RELEASE_NOTES.md`, and `en/SHARE.md` after the final licensing commit.
- [x] Re-run the 40 + 8 English publication regression after the final licensing/release-preparation commit.
- [x] Verify all root and English index links from the remote repository.
- [ ] Verify the repository is public only after all hard gates pass.
- [ ] Create the public GitHub release from the verified release commit.
- [ ] Publish external launch copy only after the public URL and release tag resolve correctly.

## 5. Recommended release version

The archival `v0.1.0` should remain unchanged. For the first fully publication-QA-reviewed bilingual public edition, the recommended release tag is **`v1.0.0`** rather than rewriting the historical snapshot.

The tag should be created only after the final license is selected and the release commit is remotely re-verified.


## 6. Copy-ready GitHub metadata

These values are ready for the final GitHub UI step.

**Repository description**

> Bilingual 40-volume + 8-essay industry research monograph on AI infrastructure, semiconductors, HBM, advanced packaging, hyperscaler system stacks, power, capital, software economics, and the 2026–2036 industrial endgame.

**Recommended topics**

`ai-infrastructure`, `semiconductors`, `nvidia`, `tsmc`, `hbm`, `advanced-packaging`, `hyperscalers`, `data-centers`, `energy`, `industry-research`

**Release tag**

`v1.0.0`

**Release title**

> v1.0.0 — The Age of AI Infrastructure Hegemony

**Release body**

> First public, publication-QA-reviewed bilingual edition of *The Age of AI Infrastructure Hegemony*.
>
> - 40-volume industry research monograph + 8 macro essays.
> - English-first release landing page with a complete Chinese edition.
> - Chinese research corpus remains the source of truth for facts, evidence grades, and analytical scope.
> - Unified F→H→M→S→X framework and A/B/C/D evidence grading.
> - English 40 + 8 corpus completed repository-wide publication QA and title/link regression.
> - Research retrieval/revision cutoff: 2026-08-28.
> - Original report text is licensed under CC BY-NC-ND 4.0.
>
> This research is not an audit opinion, investment recommendation, or legal opinion.

## 7. Tooling boundary for the final publication step

The connected GitHub write tools used in this preparation cycle can update repository files on `main`, but they do not currently expose repository-About/visibility mutation or GitHub Release/tag creation. Those remaining unchecked publication operations must therefore be performed through a GitHub interface that exposes those controls. Do not mark them complete until the public repository and `v1.0.0` release can be remotely verified.

## Independent publication-audit remediation — 2026-08-28

The read-only publication audit benchmarked commit `38704ad23006f9417d7e561bdc435a1686821fce`. Findings below are tracked against later `main` commits and are not marked closed merely because the benchmark was older.

- [x] English Publication Layer resynchronized 32/32 from the current Chinese canonical edition; English TOC, List of Tables, glossary, inline footnotes, References, and external-reader prose added.
- [x] 32/32 bilingual publication chapters pass structural regression for Table-number sets, Reference counts, and numeric section sequences.
- [x] High-risk bilingual currency / percentage / power / capacity / process values were regression-checked after synchronization.
- [x] P1 model correction: `AI Capacity Gap` now means absolute effective demand minus effective capacity in one physical layer; `AI Capacity Growth Gap` separately tracks the growth-rate difference.
- [x] P1 model correction: Chapter 24 infrastructure demand now uses `Unit Resource Intensity × Workload Volume`, with a separate constant-elasticity demand response and reproducible D-grade sensitivity example.
- [x] P1 evidence correction: F-MEM-03 now has a central TrendForce source-index entry and remains B-grade / preliminary 2027 allocation research.
- [x] P1 evidence correction: 3Q26 mobile-DRAM +8–13% language explicitly retains forecast identity.
- [x] P1 evidence correction: redirected Micron robotics static-file URL replaced by the stable official Q3 2026 earnings deck.
- [x] P1 link correction: English Four-Cloud CapEx Scope Check now exists at `en/四云CapEx口径核对.en.md`, resolving the audited `en/vol-08.en.md` relative-link target.
- [x] P1 metadata correction: research retrieval/revision cutoff normalized to 2026-08-28 across the identified English research headers and release metadata.
- [x] Reproducibility foundation: versioned D-grade model inputs and one-command recomputation script added.
- [x] Claim-audit foundation: machine-readable claim-ledger schema and deterministic numeric-claim candidate extractor added.
- [x] High-risk research-claim source coverage: bilingual 48 + 48 required-source regression passed; 32 + 32 verified high-risk ledger records committed.
- [x] Complete strict **every-number source-coverage** regression beyond the high-risk rule set: bilingual research layer **96/96**, **1,052 candidates / 0 unresolved**; formal Publication Layer **64/64**, **529 candidates / 0 unresolved**.
- [ ] Complete any remaining lower-risk **semantic** claim-to-source verification required by final editorial sign-off; structural traceability and high-risk semantic verification are complete, but they are not the same assertion.
- [ ] Obtain a green relative-link CI run after GitHub Actions becomes diagnosable; current Actions runs fail before exposing normal step/log detail.
- [ ] Obtain green bilingual PDF/EPUB build and proof QA; the first Publication Build run failed before normal step/log detail was exposed.
- [x] Complete final critical external-link sweep under the curated fallback policy: **25/25** critical evidence items reachable; **24/25** primary URLs directly reachable, with `TSMC-2Q26-TRANSCRIPT` satisfied by the declared official TSMC 2026 Q2 Quarterly Results fallback because the encrypted PDF deep link remains unstable.
- [ ] Complete final human PDF/EPUB proofread and release operations.

## Historical fact audit hard gate — 2026-08-28

- [x] Correct TSMC customer-concentration logic: annual largest/second-largest rankings are **not** a same-customer time series; anonymized Customer A/B series is kept separate.
- [x] Separate TSMC smartphone **29% revenue mix** from **+11% platform-revenue growth**.
- [x] Preserve TrendForce **51% HBM + RDIMM** as a **2026E institutional forecast**, not an observed actual.
- [x] Correct GB200/NVL72 **~120 kW/rack** to whole-rack / rack-level power; do not relabel it as compute-only IT load.
- [x] Update NVIDIA manufacturing, supply, and capacity commitments through FY27 Q2: **US$95.2B → US$119B → US$279B**.
- [x] Replace unsourced Gaming-supply wording with NVIDIA FY26 10-K / CFO language and preserve causal limits.
- [x] Time-bound TSMC advanced-packaging margin commentary to the 2Q24 statement; do not freeze it into a timeless margin claim.
- [x] Refresh current four-cloud 2026 public scopes: Microsoft ~**US$175B** reported expectation, Alphabet **US$195–205B** guidance, Meta **US$130–145B** guidance, Amazon TTM PPE net purchases actual **US$169.007B**.
- [x] Separate DeepSeek-V2 **93.3% KV-cache reduction / 5.76× max generation throughput** from DeepSeek-V3 **2.788M H800 GPU-hours / US$5.576M formal-training compute conversion**.
- [x] Restore missing English evidence: consumer-memory price moves, TSMC Customer A/B series, and English public-source ledger section.
- [x] Mark social-release URLs as non-public while the repository remains private.
- [x] Add direct public-source links to the most heavily reused NVIDIA / TSMC / Micron / TrendForce / DeepSeek / power anchors in core volumes and master judgments.
- [x] Complete repository-wide **high-risk** per-chapter source-link coverage sweep: Chinese **48/48**, English **48/48**, enforced by CI.
- [x] Complete broader **every-number source-coverage** audit beyond the high-risk source-pattern gate: research **96/96 / 1,052 candidates / 0 unresolved**; Publication Layer **64/64 / 529 candidates / 0 unresolved**.
- [ ] Complete remaining lower-risk **semantic** verification during final editorial sign-off where source meaning, denominator, or time-window still warrants human judgment.

