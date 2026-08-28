#!/usr/bin/env python3
"""Extract deterministic numeric-claim candidates for publication audit.

This script does not decide whether a line is a valid claim and does not assign
an evidence grade. It creates a reproducible queue for human/source review.
"""
from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "dist" / "numeric-claim-candidates.jsonl"

NUMERIC = re.compile(
    r"(?:US\\$|RMB|KRW|\\$)?\\s*\\d[\\d,.]*(?:\\.\\d+)?"
    r"(?:\\s*(?:%|×|x|B|M|T|K|kW|MW|GW|MWe|Wh|kWh|MWh|TWh|"
    r"KB|MB|GB|TB|PB|Gb/s|Tb/s|Mbps|Gbps|nm|mm|mm²|years?|months?|days?))?"
)
URL = re.compile(r"https?://\\S+")
FOOTNOTE_DEF = re.compile(r"^\\[\\^[^\\]]+\\]:")

def corpus_files(mode: str) -> list[Path]:
    files: list[Path] = []
    if mode in {"research", "all"}:
        files += sorted(ROOT.glob("vol-*.md"))
        files += sorted(ROOT.glob("part2-*.md"))
        files += [p for p in [ROOT / "总判.md"] if p.exists()]
        files += sorted((ROOT / "en").glob("vol-*.en.md"))
        files += sorted((ROOT / "en").glob("part2-*.en.md"))
        files += [p for p in [ROOT / "en" / "总判.en.md"] if p.exists()]
    if mode in {"publication", "all"}:
        files += sorted((ROOT / "publication").glob("part-*.md"))
        files += sorted((ROOT / "en" / "publication").glob("part-*.md"))
    return files

def candidate_lines(path: Path):
    in_code = False
    in_refs = False
    for line_no, raw in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        line = raw.strip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if line.startswith("## References") or line.startswith("## 参考文献"):
            in_refs = True
            continue
        if not line or in_code or in_refs or FOOTNOTE_DEF.match(line):
            continue
        without_urls = URL.sub("", line)
        values = [m.group(0).strip() for m in NUMERIC.finditer(without_urls)]
        values = [v for v in values if any(ch.isdigit() for ch in v)]
        if values:
            yield line_no, line, values

def main() -> None:
    ap = ArgumentParser()
    ap.add_argument("--corpus", choices=["research", "publication", "all"], default="all")
    ap.add_argument("--output", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--csv", action="store_true", help="write CSV instead of JSONL")
    args = ap.parse_args()

    rows = []
    for path in corpus_files(args.corpus):
        lang = "en" if "/en/" in path.as_posix() or path.as_posix().endswith(".en.md") else "zh"
        rel = path.relative_to(ROOT).as_posix()
        for line_no, claim_text, values in candidate_lines(path):
            rows.append({
                "language": lang,
                "source_file": rel,
                "line": line_no,
                "claim_text": claim_text,
                "detected_values": values,
                "audit_status": "unreviewed",
            })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.csv:
        with args.output.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=["language","source_file","line","claim_text","detected_values","audit_status"])
            writer.writeheader()
            for row in rows:
                out = dict(row)
                out["detected_values"] = json.dumps(out["detected_values"], ensure_ascii=False)
                writer.writerow(out)
    else:
        with args.output.open("w", encoding="utf-8") as fh:
            for row in rows:
                fh.write(json.dumps(row, ensure_ascii=False) + "\\n")

    print(f"numeric claim candidates: {len(rows)}")
    print(args.output)

if __name__ == "__main__":
    main()
