#!/usr/bin/env python3
"""Extract deterministic numeric-claim candidates for research/editorial review.

The extractor is high-recall but distinguishes source-covered facts, D-grade
models, and unresolved numeric prose. It does not itself verify a claim.
"""
from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "data" / "generated" / "numeric-claim-candidates.jsonl"

NUMERIC = re.compile(
    r"(?:US\$|RMB|KRW|\$)?\s*\d[\d,.]*(?:\.\d+)?"
    r"(?:\s*(?:%|×|x|B|M|T|K|kW|MW|GW|MWe|Wh|kWh|MWh|TWh|"
    r"KB|MB|GB|TB|PB|Gb/s|Tb/s|Mbps|Gbps|nm|mm|mm²|GPU-hours?|"
    r"GPUs?|CPUs?|racks?|wafers?|years?|months?|days?|年|月|天))?"
)
URL = re.compile(r"https?://\S+")
FOOTNOTE_USE = re.compile(r"\[\^[^\]]+\]")
FOOTNOTE_DEF = re.compile(r"^\[\^[^\]]+\]:")
HEADING = re.compile(r"^#{1,6}\s+")
TABLE_SEPARATOR = re.compile(r"^\|(?:\s*:?-+:?\s*\|)+$")
MODEL_MARKER = re.compile(
    r"\bD[- ]?grade\b|D\s*级|scenario|情景|sensitivity|stress test|"
    r"geometry|几何|assumption|假设|arithmetic|算术|示例|illustrative|"
    r"not actual|不是实际|不代表.*实际|不能.*实际",
    re.IGNORECASE,
)

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

def table_source_map(lines: list[str]) -> dict[int, bool]:
    """Map table-row line indexes to whether that table has a Source note."""
    result: dict[int, bool] = {}
    i = 0
    while i < len(lines):
        if not lines[i].lstrip().startswith("|"):
            i += 1
            continue
        start = i
        while i < len(lines) and lines[i].lstrip().startswith("|"):
            i += 1
        end = i
        block = [x.strip() for x in lines[start:end]]
        is_table = any(TABLE_SEPARATOR.match(x) for x in block)
        if not is_table:
            continue
        lookahead = "\n".join(lines[end:min(len(lines), end + 6)])
        sourced = "**Source:**" in lookahead or "**来源:**" in lookahead
        for idx in range(start, end):
            result[idx] = sourced
    return result

def source_anchor(line: str, is_table_row: bool, table_sourced: bool) -> str:
    if FOOTNOTE_USE.search(line):
        return "inline_footnote"
    if is_table_row and table_sourced:
        return "table_source"
    if MODEL_MARKER.search(line):
        return "model_marker"
    return "none"

def candidate_lines(path: Path):
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    table_map = table_source_map(lines)
    in_code = False
    in_refs = False
    for idx, raw in enumerate(lines):
        line_no = idx + 1
        line = raw.strip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if line.startswith("## References") or line.startswith("## 参考文献"):
            in_refs = True
            continue
        if not line or in_code or in_refs or FOOTNOTE_DEF.match(line):
            continue
        if HEADING.match(line) or line.startswith("**Source:**") or line.startswith("**来源:**") or line.startswith("**Note:**"):
            continue
        is_table_row = idx in table_map
        if is_table_row and TABLE_SEPARATOR.match(line):
            continue
        without_urls = URL.sub("", line)
        values = [m.group(0).strip() for m in NUMERIC.finditer(without_urls)]
        values = [v for v in values if any(ch.isdigit() for ch in v)]
        if not values:
            continue
        anchor = source_anchor(line, is_table_row, table_map.get(idx, False))
        yield {
            "line": line_no,
            "claim_text": line,
            "detected_values": values,
            "context_type": "table_row" if is_table_row else "prose",
            "source_anchor": anchor,
            "audit_status": "covered_candidate" if anchor != "none" else "unreviewed",
        }

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
        for row in candidate_lines(path):
            rows.append({"language": lang, "source_file": rel, **row})

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fields = ["language","source_file","line","claim_text","detected_values","context_type","source_anchor","audit_status"]
    if args.csv:
        with args.output.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=fields)
            writer.writeheader()
            for row in rows:
                out = dict(row)
                out["detected_values"] = json.dumps(out["detected_values"], ensure_ascii=False)
                writer.writerow(out)
    else:
        with args.output.open("w", encoding="utf-8") as fh:
            for row in rows:
                fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    unresolved = sum(r["source_anchor"] == "none" for r in rows)
    print(f"numeric claim candidates: {len(rows)}")
    print(f"unresolved source anchors: {unresolved}")
    print(args.output)

if __name__ == "__main__":
    main()
