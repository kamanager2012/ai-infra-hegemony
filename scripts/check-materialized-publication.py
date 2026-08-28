#!/usr/bin/env python3
"""Validate materialized bilingual publication sources before PDF/EPUB export."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "dist" / "publication.zh.md",
    ROOT / "dist" / "publication.en.md",
]
CHAPTER = re.compile(r"^# Part [IVX]+ · ", re.M)
LOCAL_MD_LINK = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:)([^)]+\.md(?:#[^)]+)?)\)")
FOOTNOTE_USE = re.compile(r"\[\^([^\]]+)\]")
FOOTNOTE_DEF = re.compile(r"^\[\^([^\]]+)\]:", re.M)
EMBEDDED_MEDIA = re.compile(r"!\[[^\]]*\]\([^)]+\)|<img\b|<iframe\b", re.I)

def main() -> int:
    failures: list[str] = []
    for path in FILES:
        if not path.exists() or path.stat().st_size == 0:
            failures.append(f"{path.relative_to(ROOT)}: missing or empty")
            continue

        text = path.read_text(encoding="utf-8", errors="strict")
        chapters = len(CHAPTER.findall(text))
        local_links = LOCAL_MD_LINK.findall(text)
        used = set(FOOTNOTE_USE.findall(text))
        defined = set(FOOTNOTE_DEF.findall(text))
        media = EMBEDDED_MEDIA.findall(text)

        if chapters != 32:
            failures.append(f"{path.relative_to(ROOT)}: expected 32 chapters, found {chapters}")
        if local_links:
            failures.append(
                f"{path.relative_to(ROOT)}: local .md links remain: {len(local_links)}"
            )
        if used != defined:
            missing = sorted(used - defined)
            unused = sorted(defined - used)
            failures.append(
                f"{path.relative_to(ROOT)}: footnote mismatch "
                f"missing_defs={missing[:10]} unused_defs={unused[:10]}"
            )
        if media:
            failures.append(
                f"{path.relative_to(ROOT)}: embedded media/iframe found: {len(media)}"
            )

        print(
            f"{path.relative_to(ROOT)}: chapters={chapters}, "
            f"footnotes={len(used)}, local_md_links={len(local_links)}, "
            f"embedded_media={len(media)}"
        )

    if failures:
        print("Materialized publication gate FAILED:")
        for item in failures:
            print(f"- {item}")
        return 1

    print("Materialized publication gate PASS: bilingual 32/32 sources are structurally closed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
