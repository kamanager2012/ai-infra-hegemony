#!/usr/bin/env python3
"""Local editorial checker for the formal bilingual 32-chapter report.

Checks draft-marker residue and malformed unit casing. Link and media checks
remain separate local research/editorial checks.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DIRS = [ROOT / "publication", ROOT / "en" / "publication"]

DRAFT_MARKERS = re.compile(
    r"\b(?:TODO|TBD|FIXME|PLACEHOLDER)\b|"
    r"待补|待核|待完善|草稿|内部稿|仅供内部|后续补充|暂不发布",
    re.I,
)

BAD_UNITS = re.compile(
    r"\b(?:Kw|KW|KWh|KWH|Mhz|MHZ|Ghz|GHZ|TBPS|GBPS|MW/h|GW/h)\b"
)


def publication_files() -> list[Path]:
    out: list[Path] = []
    for directory in DIRS:
        out.extend(sorted(directory.glob("*.md")))
    return out


def main() -> int:
    failures: list[str] = []
    checked = 0

    for path in publication_files():
        text = path.read_text(encoding="utf-8", errors="strict")
        checked += 1
        for lineno, line in enumerate(text.splitlines(), start=1):
            if DRAFT_MARKERS.search(line):
                failures.append(
                    f"{path.relative_to(ROOT)}:{lineno}: draft marker: {line.strip()}"
                )
            if BAD_UNITS.search(line):
                failures.append(
                    f"{path.relative_to(ROOT)}:{lineno}: unit casing: {line.strip()}"
                )

    print(f"publication editorial files checked: {checked}")
    if failures:
        print(f"Publication editorial check FAILED: {len(failures)} issue(s)")
        for item in failures:
            print(f"- {item}")
        return 1

    print("Publication editorial check PASS: no draft markers or unit-casing issues detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
