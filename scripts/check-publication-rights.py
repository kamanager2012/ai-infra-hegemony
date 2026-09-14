#!/usr/bin/env python3
"""Check that embedded media in the formal bilingual report has an explicit rights record."""
from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "third-party-materials.json"
EDITIONS = (ROOT / "publication", ROOT / "en" / "publication")
FILES = sorted(EDITIONS[0].glob("*.md")) + sorted(EDITIONS[1].glob("*.md"))
MD_IMAGE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HTML_IMAGE = re.compile(r"<img\b[^>]*\bsrc=[\"']([^\"']+)[\"']", re.I)
IFRAME = re.compile(r"<iframe\b", re.I)

def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    third_party = {x["ref"] for x in data.get("assets", [])}
    first_party = {x["ref"] for x in data.get("first_party_assets", [])}
    allowed = third_party | first_party
    found: list[tuple[str, str]] = []
    embeds: list[str] = []

    for path in FILES:
        text = path.read_text(encoding="utf-8", errors="replace")
        for rx in (MD_IMAGE, HTML_IMAGE):
            for m in rx.finditer(text):
                found.append((path.relative_to(ROOT).as_posix(), m.group(1).strip()))
        if IFRAME.search(text):
            embeds.append(path.relative_to(ROOT).as_posix())

    missing = [(p, ref) for p, ref in found if ref not in allowed]

    # A first-party declaration must point at a file that actually exists in at
    # least one edition, so a stale declaration cannot silently authorize a
    # figure that was renamed or removed.
    stale = [
        ref
        for ref in sorted(first_party)
        if not any((base / ref).exists() for base in EDITIONS)
    ]

    if embeds:
        print("Unapproved iframe/embed markup:")
        for p in embeds:
            print(f"- {p}")
        return 1

    if missing:
        print("Embedded media without rights manifest entry:")
        for p, ref in missing:
            print(f"- {p}: {ref}")
        return 1

    if stale:
        print("Declared first-party assets with no file on disk:")
        for ref in stale:
            print(f"- {ref}")
        return 1

    print(
        "publication media rights check PASS: "
        f"embedded assets={len(found)}, third-party entries={len(third_party)}, "
        f"first-party declared={len(first_party)}"
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
