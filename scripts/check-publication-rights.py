#!/usr/bin/env python3
"""Fail when Publication Layer embedded media lacks an explicit rights record."""
from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "third-party-materials.json"
FILES = sorted((ROOT / "publication").glob("*.md")) + sorted(
    (ROOT / "en" / "publication").glob("*.md")
)
MD_IMAGE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HTML_IMAGE = re.compile(r"<img\b[^>]*\bsrc=[\"']([^\"']+)[\"']", re.I)
IFRAME = re.compile(r"<iframe\b", re.I)

def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    allowed = {x["ref"] for x in data.get("assets", [])}
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

    print(
        "publication media rights gate PASS: "
        f"embedded assets={len(found)}, manifest entries={len(allowed)}"
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
