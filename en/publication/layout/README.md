# English Print Layout

This directory is the **publication layout layer** for the English canonical edition.

It does not redefine research content. The 32 chapter Markdown files, Research Brief, evidence architecture, figures, tables, and publication appendices remain the source material. Layout-specific files control only typography, pagination, assembly order, and print presentation.

## Editorial format

- **Page:** A4, two-sided, open-any chapter starts.
- **Margins:** larger inner margin for binding; compact but readable outer margin.
- **Body typography:** Noto Serif.
- **Information hierarchy:** Inter.
- **Code / literal technical text:** Noto Sans Mono.
- **Color:** restrained navy / blue / neutral gray; the report must remain legible in grayscale.
- **Chapter treatment:** every chapter starts on a fresh page; Part I–IV receive dedicated divider pages.
- **Tables:** smaller type, tighter cell padding, no claim promotion through styling.
- **Figures:** vector SVG remains canonical; figure source and boundary notes stay visible.
- **Footnotes:** kept together where possible; long URLs may break safely.
- **Headers:** report title / edition identity only; no decorative running graphics.

## Bound edition vs. audit companions

The main print edition includes:

1. Research Brief
2. scope / evidence boundaries
3. curated Table of Contents
4. List of Figures
5. List of Tables
6. glossary
7. Chapters 1–32
8. research transparency / correction policy
9. competitive evidence matrix

The raw Core Evidence Ledger, Core Source Index, Core Concept and Model Index, Core Hypothesis Matrix, and External Research Comparison Index remain **companion audit files** rather than being forced into the bound reader edition. This is a publication decision, not a deletion or downgrade of evidence.

## Build

From the repository:

```bash
bash en/publication/layout/build-print.sh
```

Or provide an explicit output path:

```bash
bash en/publication/layout/build-print.sh /path/to/report.pdf
```

The build is local and deterministic. It does **not** require GitHub Actions, CI, application tests, or a release pipeline.

## Files

- `metadata.yaml` — paper, margins, fonts, language.
- `titlepage.tex` — print cover and edition identity.
- `preamble.tex` — typography, headings, tables, captions, footnotes, running heads.
- `print.lua` — print-only structural transformation: removes the duplicate report-title heading, inserts Part divider pages, switches front matter / main matter / back matter.
- `print-order.txt` — authoritative bound-edition assembly order.
- `build-print.sh` — single local build command.

## Publication boundary

If a layout change would alter a number, source identity, denominator, evidence grade, causal claim, scenario definition, or falsification boundary, it is **not a layout change** and must return to the research workflow.
