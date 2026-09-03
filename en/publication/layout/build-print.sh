#!/usr/bin/env bash
set -euo pipefail

LAYOUT_DIR="$(cd "$(dirname "$0")" && pwd)"
PUB_DIR="$(cd "$LAYOUT_DIR/.." && pwd)"
OUT="${1:-$PUB_DIR/AI-Infrastructure-Reordering-2026-2036-EN.pdf}"

mapfile -t SOURCES < <(grep -vE '^[[:space:]]*(#|$)' "$LAYOUT_DIR/print-order.txt")

cd "$PUB_DIR"

pandoc "${SOURCES[@]}" \
  --from=markdown+footnotes+pipe_tables+raw_tex+smart \
  --standalone \
  --top-level-division=chapter \
  --pdf-engine=lualatex \
  --metadata-file="$LAYOUT_DIR/metadata.yaml" \
  --include-in-header="$LAYOUT_DIR/preamble.tex" \
  --include-before-body="$LAYOUT_DIR/titlepage.tex" \
  --lua-filter="$LAYOUT_DIR/print.lua" \
  --resource-path=".:figures:figure-data" \
  --wrap=none \
  --output="$OUT"

printf 'Built %s\n' "$OUT"
