#!/usr/bin/env python3
"""Formal-report numeric source-coverage check.

Audits the 32 Chinese + 32 English formal report chapters. It detects
unit-bearing numeric fact candidates and requires a citation/source anchor,
a sourced table, an explicit model/scenario boundary, or a previously sourced
repetition in the same chapter.

This is a structural research/editorial check. It does not replace semantic fact review.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FILES = sorted((ROOT / "publication").glob("part-*.md")) + sorted(
    (ROOT / "en" / "publication").glob("part-*.md")
)

FOOTNOTE_USE = re.compile(r"\[\^[^\]]+\]")
FOOTNOTE_DEF = re.compile(r"^\[\^[^\]]+\]:")
TABLE_SEPARATOR = re.compile(r"^\|(?:\s*:?-+:?\s*\|)+$")
STRONG_NUM = re.compile(
    r"(?:US\$|RMB|KRW|\$)\s*\d[\d,.]*(?:\.\d+)?(?:\s*[BMTK])?"
    r"|\d[\d,.]*(?:\.\d+)?\s*[KMBT]\b"
    r"|\d[\d,.]*(?:\.\d+)?\s*(?:%|×|x|kW|MW|GW|MWe|kWh|MWh|TWh|"
    r"KB|MB|GB|TB|PB|Gb/s|Tb/s|Mbps|Gbps|nm|mm²|GPU-hours?|GPUs?|CPUs?|"
    r"systems?|chips?|racks?|wafers?|servers?|units?|tokens?|parameters?|"
    r"years?|months?|days?|亿美元|亿元|万美元|万元|美元|人民币|"
    r"万片/月|片/月|万片|片|亿颗|万颗|颗|亿个|万个|个|台|柜|层|年|月|天)"
)
NON_FACT = re.compile(
    r"D[- ]?grade|D\s*级|scenario|情景|sensitivity|stress test|压力测试|"
    r"geometry|几何|assumption|assume|假设|假定|arithmetic|算术|illustrative|示例|"
    r"for example|例如|比如|cannot|must not|not actual|not shipment|"
    r"not consumption|does not mean|不能|不允许|不是实际|不代表|不得|不采用|"
    r"target|目标|threshold|阈值|formula|公式|if\b|如果|假如|"
    r"this report|the report|本书|本报告|截至|as of|"
    r"没有披露|未披露|不.*披露|does.*not.*disclose|not disclose|not as|"
    r"mechanically|机械|absolute claim|绝对化|fixed endpoints|"
    r"not industry facts|not treated as fact|not used as fact|不作为事实|不视为事实|"\n    r"scenario[- ]scale|scale markers?|情景尺度|尺度标记|headline|should not be restated|reconstruction|"
    r"未经一手披露验证|unverified|counterexample|反例",
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
        look = "\n".join(lines[end:min(len(lines), end + 8)])
        sourced = bool(
            re.search(
                r"\*\*(?:Source|来源):\*\*|^\s*(?:Source|来源)\s*[:：]",
                look,
                re.I | re.M,
            )
        )
        for n in range(start, end):
            out[n] = sourced
    return out

def inherited_list_lead(lines: list[str], i: int) -> str:
    if not re.match(r"^\s*[-*]\s", lines[i]):
        return ""
    for j in range(i - 1, max(-1, i - 9), -1):
        q = lines[j].strip()
        if not q:
            continue
        if re.match(r"^[-*]\s", q):
            continue
        return q
    return ""

def values(line: str) -> list[str]:
    line = re.sub(r"https?://\S+", "", line)
    # Process/product designators such as N2 wafers are names, not quantities.
    # Remove the designator phrase while preserving any real quantity later
    # in the same sentence (for example, "N2 ... 10,000 wafers").
    line = re.sub(r"\b(?:19|20)\d{2}\s*[–-]\s*(?:19|20)\d{2}\b", "", line)
    line = re.sub(r"\bN\d+\s+wafers?\b", "", line, flags=re.I)
    line = re.sub(r"\b[A-Za-z][A-Za-z0-9_-]*\d+\s+(?:chips?|systems?)\b", "", line, flags=re.I)
    line = re.sub(r"\b(?:DDR|LPDDR|HBM)\d+[A-Za-z0-9]*\s+wafers?\b", "", line, flags=re.I)
    line = re.sub(r"\b[A-Za-z][A-Za-z0-9_-]*\d+\s+racks?\b", "", line, flags=re.I)
    # Model-size designators ("DeepSeek 67B") are names, not quantities.
    line = re.sub(r"\b[A-Za-z][A-Za-z0-9_-]*(?:[\s-]+)\d+(?:\.\d+)?[KMBT]\b", "", line)
    return [m.group(0).strip() for m in STRONG_NUM.finditer(line)]

def norm(v: str) -> str:
    return re.sub(r"\s+", "", v).lower()

def main() -> int:
    failures: list[str] = []
    total = 0

    for path in FILES:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        pids = paragraph_ids(lines)
        tables = table_source_map(lines)
        in_code = False
        in_refs = False
        candidates: list[tuple[int, str, list[str], bool]] = []
        sourced_values: set[str] = set()

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
            ):
                continue
            if re.match(r"^\*\*(Source|Note|来源|注)", line, re.I):
                continue
            if re.search(r"\]\([^)]*\.md(?:#[^)]*)?\)", line):
                continue

            if re.match(r"^\d+[.)]\s", line):
                continue
            if re.match(r"^\*\*Table\s+\d", line, re.I):
                continue

            vals = values(line)
            if not vals:
                continue
            date_only = all(
                re.fullmatch(r"(?:19|20)\d{2}\s*年|(?:1[0-2]|[1-9])\s*月|(?:3[01]|[12]\d|[1-9])\s*天", v)
                for v in vals
            )
            node_only = all(v.lower().endswith("nm") for v in vals)
            if date_only or node_only:
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
            )
            blockquote_context = same_para
            if line.startswith(">"):
                blockquote_context = "\n".join(lines[max(0, i - 4): i + 1])
            arithmetic_block = line.startswith(">") and bool(
                re.search(r"[=≈×÷]|\b(?:plus|minus|times|divided)\b", line, re.I)
            )
            model_boundary = bool(
                NON_FACT.search(same_para)
                or NON_FACT.search(blockquote_context)
                or NON_FACT.search(lead)
                or arithmetic_block
            )
            covered = explicit or model_boundary
            candidates.append((i, line, vals, covered))
            if covered:
                sourced_values.update(norm(v) for v in vals)

        for i, line, vals, covered in candidates:
            total += 1
            if covered:
                continue
            if all(norm(v) in sourced_values for v in vals):
                continue
            failures.append(f"{path.relative_to(ROOT)}:{i + 1}: {line}")

    print(f"publication numeric candidates checked: {total}")
    if failures:
        print("Publication numeric source-coverage gate FAILED:")
        for item in failures:
            print(f"- {item}")
        return 1

    print(f"Publication numeric source-coverage gate PASS: {len(FILES)}/64 chapters clear.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
