# Q4 2026 Rolling Research v1.1 — Correction & Publication Audit

**Date and evidence cutoff:** 2026-11-19  
**Supersedes:** 2026 Q4 addendum v1.0 (evidence cutoff 2026-11-06).  
**Scope:** Rolling research publications and audit companions, **not** the 2026-08-28 frozen 32-chapter report.

## A. Repaired source / epistemic identities

| Claim family | v1.0 issue | v1.1 ruling / source anchor |
|---|---|---|
| FERC / AWS / Talen | Nov 2024 decision misdated as Nov 2026 new regulatory event | Official [FERC](https://ferc.gov/news-events/news/commissioner-christies-concurrence-pjms-susquehanna-co-location-proposal-er24-2172) dates it **2024-11-01**; [Talen SEC filing](https://www.sec.gov/Archives/edgar/data/1622536/000162253626000025/tln-2025annualreporttoshar.htm) confirms June 2025 PPA redesign and Jan 2026 appeal withdrawal |
| Microsoft Q3 | Cash PP&E 43.2B false; finance lease mixing | [First-party management/cash-flow](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1): **39.4B cash PP&E**, **45.2B management CapEx**, **7.4B leases** |
| Alphabet Q3 | PP&E 43.5B and 198–203B guidance false | [CFO Q3 transcript](https://abc.xyz/investor/events/event-details/2026/2026-Q3-Earnings-Call-2026-Ujou16CTw9/default.aspx): **51.4B Q3**, **195–205B** CY guidance |
| Meta Q3 | CapEx 33.5B and 138–142B guidance false | [IR release](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx): **34.91B**, **135–145B** guidance; finance lease included |
| Amazon Q3 | Single-quarter cash capex 46.8B, year-end 75B+ false | [Amazon 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm): **75.9B Q3**, ~**220B** CY2026 guidance |
| Tech cohort | o1 and Dimensity 9400 / A18 Pro 2024 launches misfiled as 2026 | [OpenAI](https://openai.com/index/learning-to-reason-with-llms/), [MediaTek](https://corp.mediatek.com/news-events/press-releases/mediateks-dimensity-9400-flagship-soc-offers-extreme-performance-and-efficiency-for-the-latest-ai-experiences), [Apple](https://www.apple.com/newsroom/2024/09/apple-debuts-iphone-16-pro-and-iphone-16-pro-max/) primary dates |
| Consumer pricing / NVLink | Unsupported sector-wide percentage / universal claims | Withdrawn as factual conclusions; production TCO and contract/spot/SKU denominators are demanded before reassertion |
| Memory and regulatory access | Missing differentiated 2026 data | NVIDIA commitments, TrendForce HBM4/NAND split, BIS scoped IFR integrated with sources and future evidence gates |

## B. Explicit denominator decisions

- Microsoft company quarter naming differs; capex vs cash PP&E vs finance lease principal separated.
- Alphabet/Meta/Amazon disclose different company-wide lines, not a joint four-cloud AI GPU total.
- HBM wafer intensity, HBM4 LTA, conventional DDR prices and NAND inventories treated as separate layers and channels.
- 2027 NAND oversupply is a **forecast as of Nov 18**, not an observation of 2027 actuals.
- NVIDIA US$390B is aggregate forward supply and capacity **commitment**, not cash funded nor supplier-specific.
- FERC permit and executed PPA do not identify currently energized compute.
- BIS remote-access requirements are scoped. Determining covered entities requires checking the operative rule.
- S1–S4 remain conditional; S2 remains provisional, no weights calibrated from this addendum.

## C. Read-back and selected static gates

**Completed in connected repository, on the review branch:**
1. EN canonical and ZH translated Q4 addenda **exactly match** each corresponding public reader JSON document.
2. Evidence ledger and hypothesis matrix EN+ZH **exactly match** corresponding public reader JSON documents.
3. All **16/16 numbered footnotes** exist in both languages; 10 body sections and 4 new tables each.
4. Corrected amounts and event dates present with company/source identities.
5. Web app JavaScript successfully parsed; document router, homepage CTA and sitemap each contain both-language Q4 routes.
6. Version metadata preserves original **32 chapters / 2026-08-28** baseline and labels Q4 v1.1 **2026-11-19** separately.
7. **21/21** selected content/route/metadata assertions **passed** after correcting a test error that confused US$B values with their US$100M representations.
8. **10/10 frozen EN/ZH 32-chapter + publication-appendix JSON files byte-for-byte unchanged** relative to publication main.
9. Source pages for major 2026 facts and the 2024 FERC original action independently consulted.

**Not claimed:**
- Entire repository Python check suite was **not run in a full local checkout**.
- No post-deployment interactive browser smoke has yet been obtained for both languages.
- This update has **not** independently recalculated all 32 historical chapter data or resolved existing research PRs #13–#15.
- The BIS rule's legal scope has not been given a formal legal opinion; the analysis avoids claiming blanket applicability.

## D. Publication protocol

Publication branch is main; work was authored off main in a dated research branch to avoid its stale diverged research branch overwriting the website. Authoritative EN first, ZH parity second, web snapshots third, selected manual gate fourth. A review PR should be merged only as an intentional publication batch. Repo policy explicitly does **not** introduce CI workflows for research reports.

The history of the retracted v1.0 remains accessible in Git. Reader-facing latest entry is v1.1 and should not cite v1.0's false factual claims.
