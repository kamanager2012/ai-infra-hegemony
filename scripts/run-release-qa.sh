#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

need=(python3 pandoc xelatex qpdf pdfinfo pdftotext pdffonts pdftoppm unzip)
missing=()
for tool in "${need[@]}"; do
  command -v "$tool" >/dev/null 2>&1 || missing+=("$tool")
done
if (("${#missing[@]}" > 0)); then
  printf 'Missing release-QA tools: %s\n' "${missing[*]}" >&2
  printf 'On Ubuntu/WSL, install the matching packages (pandoc, texlive-xetex, texlive-latex-extra, texlive-lang-chinese, fonts-noto-cjk, fonts-dejavu-core, poppler-utils, qpdf, unzip).\n' >&2
  exit 2
fi

mkdir -p dist

echo '== Repository/source QA =='
python3 scripts/check-links.py
python3 scripts/check-required-sources.py
python3 scripts/check-research-numeric-claims.py
python3 scripts/check-publication-numeric-claims.py
python3 scripts/check-publication-rights.py
python3 scripts/check-publication-editorial.py
python3 scripts/recompute_models.py

echo '== Materialize bilingual publication sources =='
python3 scripts/build_publication.py
python3 scripts/check-materialized-publication.py
if command -v git >/dev/null 2>&1 && git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git diff --exit-code -- dist/publication.zh.md dist/publication.en.md
fi

echo '== Build Chinese PDF =='
pandoc dist/publication.zh.md   --from=markdown+pipe_tables+footnotes+raw_tex   --toc --toc-depth=2   --pdf-engine=xelatex   -V documentclass=report   -V geometry:margin=22mm   -V mainfont="Noto Serif CJK SC"   -V sansfont="Noto Sans CJK SC"   -V monofont="DejaVu Sans Mono"   -V CJKmainfont="Noto Serif CJK SC"   -H scripts/publication-header.tex   -o dist/ai-infrastructure-hegemony.zh.pdf   2>dist/zh-pdf.log

echo '== Build English PDF =='
pandoc dist/publication.en.md   --from=markdown+pipe_tables+footnotes+raw_tex   --toc --toc-depth=2   --pdf-engine=xelatex   -V documentclass=report   -V geometry:margin=22mm   -V mainfont="Noto Serif CJK SC"   -V sansfont="Noto Sans CJK SC"   -V monofont="DejaVu Sans Mono"   -H scripts/publication-header.tex   -o dist/ai-infrastructure-hegemony.en.pdf   2>dist/en-pdf.log

echo '== Build EPUB editions =='
pandoc dist/publication.zh.md   --from=markdown+pipe_tables+footnotes+raw_tex   --toc --toc-depth=2   -o dist/ai-infrastructure-hegemony.zh.epub
pandoc dist/publication.en.md   --from=markdown+pipe_tables+footnotes+raw_tex   --toc --toc-depth=2   -o dist/ai-infrastructure-hegemony.en.epub

echo '== Final machine proof =='
python3 scripts/proof_publication.py

echo '== Release QA PASS =='
ls -lh   dist/ai-infrastructure-hegemony.zh.pdf   dist/ai-infrastructure-hegemony.en.pdf   dist/ai-infrastructure-hegemony.zh.epub   dist/ai-infrastructure-hegemony.en.epub   dist/proof/publication-proof.json
echo 'Human visual/read-through proof and author COI confirmation remain separate release gates.'
