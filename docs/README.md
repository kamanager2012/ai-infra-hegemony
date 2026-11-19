# Web Edition

This directory contains the zero-build primary web edition for **AI Infrastructure Reordering, 2026–2036: A Structural Industry Outlook**.

## Publishing model

- **Website**: primary reader-facing publication surface.
- **Formal Markdown report**: private source of truth under `en/publication/` and `publication/`.
- **Public edition bundles**: reader-facing snapshots under `docs/content/`; the website reads only these files at runtime.
- **Core figures**: canonical English SVG assets mirrored under `docs/figures/` for public web rendering.
- **Private GitHub repository**: source research, evidence architecture, source indexes, historical drafts, scripts, and corrections.
- **PDF / print**: paused as a secondary publication surface. It is not a primary website route and does not define the research text.

## Hosting

The site is plain HTML/CSS/JavaScript. No Node.js framework, GitHub Actions, application CI, or release pipeline is required.

For GitHub Pages, use the repository's `main /docs` directory as the Pages source. The reader never fetches `publication/`, `en/publication/`, or private repository paths at runtime.

Only reader-facing publication material is copied into `docs/content/`. Historical `vol-*`, legacy `part2-*`, internal scripts, and unpublished research material remain outside the public snapshot.

## Reader routes

- English home: `/?lang=en`
- Chinese home: `/?lang=zh`
- English chapter example: `/?lang=en&chapter=17`
- Chinese chapter example: `/?lang=zh&chapter=17`
- Research Brief: `/?lang=en&doc=RESEARCH_BRIEF.md`
- Evidence Ledger: `/?lang=en&doc=核心证据台账.md`

Legacy `en.html` and `full-report-*.html` URLs are compatibility redirects to the current interactive web edition. They are not independent full-text sources.

## Reader architecture

The website presents the same publication snapshot through:

- formal report landing page;
- decision-oriented reading paths;
- load-bearing evidence summary with denominator boundaries;
- 32-chapter searchable research map;
- three-column desktop reader: chapter navigation / article / section navigation;
- mobile chapter drawer;
- responsive tables;
- canonical SVG figures;
- rendered footnotes with back-links;
- publication and audit-companion library.

The website does not create a second research narrative.

## Post-cutoff special chapter

Chapter 33 (Jensen Huang succession and NVIDIA system coordination) is a dated 2026 Q4 special study with evidence cutoff **2026-11-19**. It is readable through `?lang=en&chapter=33` and `?lang=zh&chapter=33`, backed by `docs/content/{en,zh}/part-4.json`. This addition does not change the 32-chapter base evidence cutoff or imply that post-cutoff facts were available on 2026-08-28.

## Corrected 2026 Q4 research addendum

The 2026-11-19 Q4 v1.1 rolling research addendum **supersedes the factually incorrect Q4 v1.0**. Public reader routes are `?lang=en&doc=2026-Q4-ROLLING-ADDENDUM.md` and `?lang=zh&doc=2026-Q4-ROLLING-ADDENDUM.md`. Both are synchronized with the canonical English file and professional Chinese translation in `docs/content/{en,zh}/appendices-research.json`. The frozen 32-chapter baseline still has 2026-08-28 evidence cutoff; the Ch33 special study is a separate 2026-11-19 branch of analysis.

## Revision discipline

English is the canonical analytical edition. A substantive change is resolved in English first and then synchronized to Chinese. The web bundles are publication snapshots of those canonical files.

Evidence cutoff and edition revision remain distinct: facts after **2026-08-28** are not backdated into this evidence cycle. Later changes in this edition are limited to corrections, evidence-boundary repair, bilingual parity, and editorial / web-presentation work.

## Rights

The original research is distributed under **CC BY-NC-ND 4.0** as specified in the repository `LICENSE`. The public reader summary is in [`rights.html`](rights.html); the repository `LICENSE` remains authoritative for the source repository.
