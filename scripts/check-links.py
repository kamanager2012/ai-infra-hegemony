#!/usr/bin/env python3
"""Check relative markdown links. Does not fetch the web. Does not edit files."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
broken = []
checked = 0

def exists_for(src: Path, raw: str) -> bool:
    target, _, _frag = raw.partition('#')
    if not target:
        return True
    candidates = [(src.parent / target).resolve()]
    # English files keep Chinese filenames; those live one directory up
    if src.parent.name == 'en':
        candidates.append((ROOT / target).resolve())
        if target.endswith('.md') and not target.endswith('.en.md'):
            stem = Path(target).name
            if stem.startswith('vol-') or stem.startswith('part2-') or stem in {'总判.md', '机制索引.md'}:
                en_name = stem.replace('.md', '.en.md') if not stem.endswith('.en.md') else stem
                candidates.append((src.parent / en_name).resolve())
                candidates.append((src.parent / Path(target).name.replace('.md', '.en.md')).resolve())
    return any(c.exists() for c in candidates)

for f in sorted(ROOT.rglob('*.md')):
    if '/.git/' in str(f):
        continue
    text = f.read_text(errors='replace')
    for m in LINK.finditer(text):
        raw = m.group(1).strip()
        if raw.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        checked += 1
        if not exists_for(f, raw):
            broken.append(f'{f.relative_to(ROOT)} -> {raw}')

print(f'checked {checked} relative links')
if broken:
    print('broken:')
    for b in broken:
        print(' ', b)
    sys.exit(1)
print('ok')
