#!/usr/bin/env python3
"""Research-layer every-number source-coverage gate.

Scope: 40 research volumes + 8 macro essays in Chinese and English (96 files).
The gate is intentionally high-recall for unit-bearing numeric claims and
requires one of:
- inline URL / footnote,
- nearby explicit source block,
- sourced table,
- explicit model / scenario / counterexample boundary,
- same numeric identity already source-covered elsewhere in the same file.

This gate checks traceability/identity. Semantic high-risk claims remain
independently verified in the bilingual claim ledgers.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

ZH = sorted(ROOT.glob("vol-*.md")) + sorted(ROOT.glob("part2-*.md"))
EN = sorted((ROOT / "en").glob("vol-*.en.md")) + sorted((ROOT / "en").glob("part2-*.en.md"))
FILES = ZH + EN

FOOTNOTE_USE = re.compile(r"\[\^[^\]]+\]")
FOOTNOTE_DEF = re.compile(r"^\[\^[^\]]+\]:")
TABLE_SEPARATOR = re.compile(r"^\|(?:\s*:?-+:?\s*\|)+$")
STRONG_NUM = re.compile(
    r"(?:US\$|RMB|KRW|\$)\s*\d[\d,.]*(?:\.\d+)?(?:\s*[BMTK])?"
    r"|\d[\d,.]*(?:\.\d+)?\s*(?:%|×|x|kW|MW|GW|MWe|kWh|MWh|TWh|"
    r"KB|MB|GB|TB|PB|Gb/s|Tb/s|Mbps|Gbps|nm|mm²|GPU-hours?|"
    r"systems?|chips?|racks?|wafers?|years?|months?|days?|年|月|天)"
)
NON_FACT = re.compile(
    r"D[- ]?grade|D\s*级|scenario|情景|sensitivity|stress test|压力测试|"
    r"geometry|几何|assumption|assume|假设|假定|arithmetic|算术|"
    r"illustrative|示例|for example|例如|比如|cannot|must not|"
    r"not actual|not shipment|not consumption|does not mean|"
    r"不能|不允许|不是实际|不代表|不得|不采用|没有披露|未披露|不.*披露|"
    r"does.*not.*disclose|not disclose|not as|mechanically|机械|"
    r"absolute claim|绝对化|target|目标|threshold|阈值|formula|公式|"
    r"if\b|如果|假如|本报告|本书|this report|the report",
    re.I,
)
SOURCE_LABEL = re.compile(
    r"^\s*(?:[-*]\s*)?(?:主要来源|来源|数据来源|Source|Sources|Evidence|"
    r"官方来源|一手来源|References?)\s*[:：]",
    re.I,
)

def paragraph_ids(lines: list[str]) -> list[int]:
    out: list[int] = []
    pid = 0
    for line in lines:
        if not line.strip():
            pid += 1
        out.append(pid)
    return out

def table_source_map(lines: list[str]) -> dict[int, bool]:
    out: dict[int, bool] = {}
    i = 0
    while i < len(lines):
        if not lines[i].lstrip().startswith("|"):
            i += 1
            continue
        start = i
        while i < len(lines) and lines[i].lstrip().startswith("|"):
            i += 1
        end = i
        if not any(TABLE_SEPARATOR.match(x.strip()) for x in lines[start:end]):
            continue
        look = "\n".join(lines[end:min(len(lines), end + 10)])
        sourced = bool(re.search(r"https?://", look) or SOURCE_LABEL.search(look))
        for n in range(start, end):
            out[n] = sourced
    return out

def inherited_list_lead(lines: list[str], i: int) -> str:
    if not re.match(r"^\s*[-*]\s", lines[i]):
        return ""
    for j in range(i - 1, max(-1, i - 10), -1):
        q = lines[j].strip()
        if not q:
            continue
        if re.match(r"^[-*]\s", q):
            continue
        return q
    return ""

def values(line: str) -> list[str]:
    line = re.sub(r"https?://\S+", "", line)
    line = re.sub(r"\bN\d+\s+wafers?\b", "", line, flags=re.I)
    return [m.group(0).strip() for m in STRONG_NUM.finditer(line)]

def norm(value: str) -> str:
    return re.sub(r"\s+", "", value).lower()

def nearby_source(lines: list[str], i: int) -> bool:
    lo = max(0, i - 3)
    hi = min(len(lines), i + 11)
    block = "\n".join(lines[lo:hi])
    return bool(re.search(r"https?://", block) or SOURCE_LABEL.search(block))

def main() -> int:
    failures: list[str] = []
    total = 0

    if len(ZH) != 48 or len(EN) != 48:
        print(f"unexpected corpus size: zh={len(ZH)} en={len(EN)}")
        return 1

    for path in FILES:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        pids = paragraph_ids(lines)
        tables = table_source_map(lines)
        in_code = False
        in_refs = False
        candidates: list[tuple[int, str, list[str], bool]] = []
        source_values: set[str] = set()

        for i, raw in enumerate(lines):
            line = raw.strip()
            if line.startswith("```"):
                in_code = not in_code
                continue
            if re.match(r"^##\s+(References|参考文献)", line, re.I):
                in_refs = True
                continue
            if (
                in_code
                or in_refs
                or not line
                or re.match(r"^#{1,6}\s", line)
                or FOOTNOTE_DEF.match(line)
                or SOURCE_LABEL.match(line)
                or re.match(r"^\d+[.)]\s", line)
            ):
                continue
            if re.search(r"\]\([^)]*\.md(?:#[^)]*)?\)", line):
                continue

            vals = values(line)
            if not vals:
                continue

            same_para = "\n".join(
                lines[j] for j in range(len(lines)) if pids[j] == pids[i]
            )
            lead = inherited_list_lead(lines, i)
            explicit = bool(
                FOOTNOTE_USE.search(same_para)
                or re.search(r"https?://", same_para)
                or FOOTNOTE_USE.search(lead)
                or re.search(r"https?://", lead)
                or tables.get(i)
                or nearby_source(lines, i)
            )
            model_boundary = bool(NON_FACT.search(same_para))
            arithmetic_block = line.startswith(">") and bool(
                re.search(r"[=≈×÷]|\b(?:plus|minus|times|divided)\b", line, re.I)
            )
            covered = explicit or model_boundary or arithmetic_block
            candidates.append((i, line, vals, covered))
            if covered:
                source_values.update(norm(v) for v in vals)

        for i, line, vals, covered in candidates:
            total += 1
            if covered:
                continue
            if all(norm(v) in source_values for v in vals):
                continue
            failures.append(f"{path.relative_to(ROOT)}:{i + 1}: {line}")

    print(f"research numeric candidates checked: {total}")
    if failures:
        print(f"Research every-number source-coverage gate FAILED: {len(failures)} unresolved")
        for item in failures:
            print(f"- {item}")
        return 1

    print("Research every-number source-coverage gate PASS: 96/96 files structurally traceable.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
