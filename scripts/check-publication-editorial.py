#!/usr/bin/env python3
"""Editorial preflight for the formal bilingual Publication Layer.

This is a narrow release gate for publication hygiene. It is not a style
opinion engine and does not rewrite prose automatically.
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

LOCAL_MD_LINK = re.compile(
    r"\[[^\]]+\]\((?!https?://|mailto:)([^)]+\.md(?:#[^)]+)?)\)"
)

RAW_HTML_MEDIA = re.compile(r"<(?:img|iframe)\b", re.I)

def files() -> list[Path]:
    out: list[Path] = []
    for directory in DIRS:
        out.extend(sorted(directory.glob("*.md")))
    return out

def main() -> int:
    failures: list[str] = []
    checked = 0

    for path in files():
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
            if LOCAL_MD_LINK.search(line):
                failures.append(
                    f"{path.relative_to(ROOT)}:{lineno}: local .md link remains: {line.strip()}"
                )
            if RAW_HTML_MEDIA.search(line):
                failures.append(
                    f"{path.relative_to(ROOT)}:{lineno}: raw embedded media/iframe: {line.strip()}"
                )

    print(f"publication editorial files checked: {checked}")
    if failures:
        print(f"Publication editorial gate FAILED: {len(failures)} issue(s)")
        for item in failures:
            print(f"- {item}")
        return 1

    print("Publication editorial gate PASS: no release-hygiene blockers detected.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
