#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

ZH_CHAPTERS = [
    *[f"publication/part-I-ch{i:02d}-{slug}.md" for i, slug in [
        (1,"executive-summary"),(2,"nvidia-system-stack"),(3,"resource-gravity"),
        (4,"tsmc-advanced-logic"),(5,"hbm-memory"),(6,"advanced-packaging"),
        (7,"power-constraint"),(8,"quantitative-framework"),(9,"semiconductor-redundancy")]],
    *[f"publication/part-II-ch{i:02d}-{slug}.md" for i, slug in [
        (10,"model-economics"),(11,"nvidia-ai-factory"),(12,"hyperscaler-system-stack"),
        (13,"anchor-compute-buyer"),(14,"agent-software"),(15,"physical-ai"),
        (16,"differentiated-competitors"),(17,"china-parallel-stack"),(18,"antitrust-policy")]],
    *[f"publication/part-III-ch{i:02d}-{slug}.md" for i, slug in [
        (19,"capex-supercycle"),(20,"value-capture-map"),(21,"consumer-transmission"),
        (22,"depreciation-wall"),(23,"capital-financing"),(24,"capital-clearing"),
        (25,"labor-market"),(26,"education-talent")]],
    *[f"publication/part-IV-ch{i:02d}-{slug}.md" for i, slug in [
        (27,"research-method"),(28,"timeline-2026-2036"),(29,"monitoring-framework"),
        (30,"scenarios"),(31,"strategy-endgame"),(32,"master-judgment")]],
]

EN_CHAPTERS = [p.replace("publication/", "en/publication/", 1) for p in ZH_CHAPTERS]

LOCAL_MD_LINK = re.compile(r"\[([^\]]+)\]\((?!https?://|mailto:)([^)]+\.md(?:#[^)]+)?)\)")
FOOTNOTE = re.compile(r"\[\^([^\]]+)\]")

def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        raise FileNotFoundError(rel)
    return path.read_text(encoding="utf-8")

def strip_local_md_links(text: str) -> str:
    return LOCAL_MD_LINK.sub(lambda m: m.group(1), text)

def namespace_footnotes(text: str, namespace: str) -> str:
    return FOOTNOTE.sub(lambda m: f"[^{namespace}-{m.group(1)}]", text)

def front_body(text: str, heading: str) -> str:
    # Front-matter source contains title/byline metadata above a horizontal rule.
    parts = re.split(r"\n---\n", text, maxsplit=1)
    body = parts[1] if len(parts) == 2 else text
    body = strip_local_md_links(body)
    return f"# {heading}\n\n" + body.strip() + "\n"

def process(text: str, namespace: str) -> str:
    text = strip_local_md_links(text)
    text = namespace_footnotes(text, namespace)
    return text.strip() + "\n"

def build(language: str, chapters: list[str]) -> str:
    zh = language == "zh"
    yaml = """---
title: "AI基础设施霸权时代"
subtitle: "The Age of AI Infrastructure Hegemony"
author: "James (kamanager2012)"
date: "Research and revision cutoff: 2026-08-28"
lang: zh-CN
---
""" if zh else """---
title: "The Age of AI Infrastructure Hegemony"
subtitle: "Structural Reallocation of Compute, Semiconductors, Memory, Advanced Packaging, Power, and Capital"
author: "James (kamanager2012)"
date: "Research and revision cutoff: August 28, 2026"
lang: en-US
---
"""

    base = "publication" if zh else "en/publication"
    chunks = [yaml]
    chunks.append(front_body(read(f"{base}/00-front-matter.md"),
                             "报告定位、证据边界与免责声明" if zh else
                             "Scope, Evidence Boundaries, Disclaimer, and Copyright"))
    chunks.append("\\newpage\n")
    chunks.append(process(read(f"{base}/02-list-of-tables.md"), "lot"))
    chunks.append("\\newpage\n")
    chunks.append(process(read(f"{base}/03-abbreviations-and-glossary.md"), "glossary"))
    chunks.append("\\newpage\n")
    chunks.append(process(read(f"{base}/04-research-transparency.md"), "transparency"))
    chunks.append("\\newpage\n")
    chunks.append(process(read(f"{base}/05-competitive-evidence-matrix.md"), "competition"))

    for rel in chapters:
        chapter = re.search(r"ch(\d+)", rel)
        ns = f"ch{chapter.group(1)}" if chapter else Path(rel).stem
        chunks.append("\\newpage\n")
        chunks.append(process(read(rel), ns))

    return "\n\n".join(chunks).strip() + "\n"

def main() -> None:
    DIST.mkdir(exist_ok=True)
    (DIST / "publication.zh.md").write_text(build("zh", ZH_CHAPTERS), encoding="utf-8")
    (DIST / "publication.en.md").write_text(build("en", EN_CHAPTERS), encoding="utf-8")
    print("Built combined publication Markdown sources:")
    print(DIST / "publication.zh.md")
    print(DIST / "publication.en.md")

if __name__ == "__main__":
    main()
