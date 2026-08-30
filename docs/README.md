# Web Edition

This directory contains the zero-build web reader for **The Age of AI Infrastructure Hegemony**.

## Publishing model

- **Website**: reader-facing primary entry.
- **Formal Markdown report**: source of truth under `publication/` and `en/publication/`.
- **GitHub repository**: research, evidence, methodology, citation history, and corrections.
- **PDF**: generated from the website's full-report print mode; it does not maintain a second body-text source.

## Hosting

The site is plain HTML/CSS/JavaScript. No Node.js, framework, GitHub Actions, or build pipeline is required.

For GitHub Pages, use the repository's `main /docs` directory as the Pages source. The reader first tries same-repository Markdown paths and then falls back to the public raw GitHub Markdown URLs.

Because the repository may be private during pre-publication work, the raw-GitHub fallback becomes publicly usable after the repository is made public. The same `docs/` directory can also be hosted by any static host that serves the repository tree.

## Reader routes

- Chinese home: `/?lang=zh`
- English home: `/?lang=en`
- Chapter example: `/?lang=zh&chapter=17`
- English chapter example: `/?lang=en&chapter=17`
- Full Chinese print/PDF view: `/?lang=zh&print=1`
- Full English print/PDF view: `/?lang=en&print=1`

## Freeze discipline

The website does not duplicate or rewrite research conclusions. It renders the frozen 32-chapter publication Markdown directly. Post-freeze changes remain limited to factual corrections, source-link repairs, citation-scope corrections, and material-error fixes.
