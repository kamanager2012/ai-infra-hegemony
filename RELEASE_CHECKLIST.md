# Public Release Gate

**Repository:** `kamanager2012/ai-infra-hegemony`  
**Target:** first public publication of *The Age of AI Infrastructure Hegemony*  
**Research retrieval/revision cutoff:** 2026-08-27  
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

## 2. Publication metadata

- [x] `CITATION.cff` no longer declares CC BY 4.0 or an obsolete release date.
- [x] `RELEASE_NOTES.md` distinguishes the current `main` research state from the archival `v0.1.0` snapshot.
- [x] `CONTRIBUTING.md` reflects the current bilingual publication state.
- [x] X/social launch copy points to the English root landing page and the correct Chinese landing page.
- [ ] Final repository description / About text set on GitHub.
- [ ] Final public release tag created.

## 3. Licensing — hard gate

- [ ] Replace the existing CC BY 4.0 `LICENSE` before changing repository visibility to public.
- [ ] Ensure the final license, README, and CITATION wording agree.
- [ ] Confirm treatment of quotations, third-party figures, and source excerpts separately from original report text.
- [ ] Confirm whether commercial reuse, redistribution, derivative translations, bulk copying, and model-training/data-mining use require explicit permission.

**Do not make the repository public while the current CC BY 4.0 file remains unless CC BY 4.0 is intentionally chosen.**

## 4. Final release verification

- [ ] Re-read the remote `LICENSE`, `README.md`, `README.zh-CN.md`, `CITATION.cff`, `CONTRIBUTING.md`, `RELEASE_NOTES.md`, and `en/SHARE.md` after the final licensing commit.
- [ ] Re-run the 40 + 8 English publication regression after the final release commit.
- [ ] Verify all root and English index links from the remote repository.
- [ ] Verify the repository is public only after all hard gates pass.
- [ ] Create the public GitHub release from the verified release commit.
- [ ] Publish external launch copy only after the public URL and release tag resolve correctly.

## 5. Recommended release version

The archival `v0.1.0` should remain unchanged. For the first fully publication-QA-reviewed bilingual public edition, the recommended release tag is **`v1.0.0`** rather than rewriting the historical snapshot.

The tag should be created only after the final license is selected and the release commit is remotely re-verified.
