# Web Edition

This directory contains the zero-build web reader for **The Age of AI Infrastructure Hegemony: 2026–2036 Industry Outlook Research Report**.

## Publishing model

- **Website**: reader-facing primary entry.
- **Formal Markdown report**: private source of truth under `publication/` and `en/publication/`.
- **Public snapshot bundles**: frozen reader-facing copies under `docs/content/`; the website reads only these files at runtime.
- **Private GitHub repository**: source research, evidence, methodology, citation history, historical drafts, scripts, and corrections.
- **PDF**: generated from the same public frozen snapshot; it does not maintain a second manually edited body-text source.

## Hosting

The site is plain HTML/CSS/JavaScript. No Node.js, framework, GitHub Actions, or build pipeline is required.

For GitHub Pages, use the repository's `main /docs` directory as the Pages source. The reader never fetches `publication/`, `en/publication/`, or `raw.githubusercontent.com` at runtime. A private source repository can therefore remain private while the selected `docs/` publication snapshot is served by a compatible static host / Pages configuration.

Only reader-facing publication material should be copied into `docs/content/`. Historical `vol-*`, legacy `part2-*`, internal audit files, scripts, and unpublished research material remain outside the public snapshot.

## Reader routes

- Chinese home: `/?lang=zh`
- English home: `/?lang=en`
- Chapter example: `/?lang=zh&chapter=17`
- English chapter example: `/?lang=en&chapter=17`
- Full Chinese print/PDF view: `/?lang=zh&print=1`
- Full English print/PDF view: `/?lang=en&print=1`

## Freeze discipline

The website does not duplicate or rewrite research conclusions. It renders the frozen 32-chapter publication Markdown directly. Post-freeze changes remain limited to factual corrections, source-link repairs, citation-scope corrections, and material-error fixes.

## Rights

Original research material is **All Rights Reserved**. The public web summary is in [`rights.html`](rights.html); the repository `LICENSE` file is authoritative for the source repository.
