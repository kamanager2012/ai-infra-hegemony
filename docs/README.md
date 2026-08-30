# Web Edition

This directory contains the zero-build web reader for **AI Infrastructure Reordering: 2026–2036 Industry Outlook Research Report**.

## Publishing model

- **Website**: reader-facing primary entry.
- **Formal Markdown report**: private source of truth under `publication/` and `en/publication/`.
- **Public edition bundles**: reader-facing copies under `docs/content/`; the website reads only these files at runtime.
- **Private GitHub repository**: source research, evidence, methodology, citation history, historical drafts, scripts, and corrections.
- **Print / PDF export**: the browser print view renders the same public edition bundle; there is no second manually edited body-text source.

## Hosting

The site is plain HTML/CSS/JavaScript. No Node.js, framework, GitHub Actions, or build pipeline is required.

For GitHub Pages, use the repository's `main /docs` directory as the Pages source. The reader never fetches `publication/`, `en/publication/`, or `raw.githubusercontent.com` at runtime. A private source repository can therefore remain private while the selected `docs/` publication snapshot is served by a compatible static host / Pages configuration.

Only reader-facing publication material should be copied into `docs/content/`. Historical `vol-*`, legacy `part2-*`, internal audit files, scripts, and unpublished research material remain outside the public edition bundle.

## Reader routes

- Chinese home: `/?lang=zh`
- English home: `/?lang=en`
- Chapter example: `/?lang=zh&chapter=17`
- English chapter example: `/?lang=en&chapter=17`
- Full Chinese print/PDF view: `/?lang=zh&print=1`
- Full English print/PDF view: `/?lang=en&print=1`

## Revision discipline

The website does not create a second research narrative. It renders the 32-chapter publication content from `docs/content/`. Evidence cutoff and edition revision are separate: later edits may correct facts, source links, citation scope, bilingual parity, or editorial structure, but post-cutoff facts are not backdated into the edition's evidence set.

## Rights

Original research material is **All Rights Reserved**. The public web summary is in [`rights.html`](rights.html); the repository `LICENSE` file is authoritative for the source repository.
