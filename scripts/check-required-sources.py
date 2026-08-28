#!/usr/bin/env python3
"""Fail CI when high-risk research claims lose their required source anchors.

This is a deterministic regression gate, not a substitute for human fact review.
It uses paragraph-local claim patterns so unrelated numbers/names elsewhere in a
file cannot satisfy a claim trigger.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

ZH_FILES = [
    *[ROOT / f"vol-{i:02d}.md" for i in range(1, 41)],
    *[ROOT / f"part2-{i:02d}.md" for i in range(1, 9)],
]
EN_FILES = [
    *[ROOT / "en" / f"vol-{i:02d}.en.md" for i in range(1, 41)],
    *[ROOT / "en" / f"part2-{i:02d}.en.md" for i in range(1, 9)],
]

@dataclass(frozen=True)
class Rule:
    name: str
    claim: re.Pattern[str]
    source_markers: tuple[str, ...]

def rx(pattern: str) -> re.Pattern[str]:
    return re.compile(pattern, re.I | re.S)

COMMON_RULES = (
    Rule("NVL72 product specification",
         rx(r"13\.4\s*TB\s*HBM3E|17\s*TB\s*LPDDR5X"),
         ("nvidia.com/en-us/data-center/gb200-nvl72",)),
    Rule("NVIDIA FY26 seller economics",
         rx(r"US\$193\.737B|US\$96\.575B|US\$215\.938B|\$193,737M"),
         ("fourth-quarter-and-fiscal-2026",)),
    Rule("NVIDIA FY27 Q2 seller economics",
         rx(r"US\$96\.221B|US\$89\.0B|US\$63\.734B|890亿美元"),
         ("second-quarter-fiscal-2027",)),
    Rule("NVIDIA supply commitments",
         rx(r"(?=.*US\$279B)(?=.*commitment)"),
         ("nvda-20260726.htm",)),
    Rule("HBM + RDIMM 51% forecast",
         rx(r"(?=.*51%)(?=.*HBM)(?=.*RDIMM)"),
         ("20260825-13198.html",)),
    Rule("Micron HBM3E wafer-supply trade ratio",
         rx(r"(?:3×|3x|三倍|3倍).{0,120}(?:wafer|DDR5)|HBM3E.{0,140}(?:3×|3x|three times|三倍|3倍)"),
         ("FY24-Q2-Prepared-Remarks.pdf",)),
    Rule("TSMC corrected 2025 advanced-packaging identity",
         rx(r"advanced packaging slightly over 10%"),
         ("TSMC%204Q25%20Transcript.pdf",)),
    Rule("TSMC packaging growth constraint",
         rx(r"limits my customers.? growth|growth-limiting|限制客户增长"),
         ("TSMC%202Q26%20Transcript.pdf", "quarterly-results/2026/q2")),
    Rule("TrendForce NVIDIA CoWoS >60%",
         rx(r"CoWoS.{0,160}(?:>\s*60%|more than 60%|超过\s*60%|60%)"),
         ("RP250314ZJ",)),
    Rule("DeepSeek-V3 formal training compute",
         rx(r"2\.788M\s*H800\s*GPU-hours"),
         ("2412.19437",)),
    Rule("Talen/AWS revised PPA",
         rx(r"(?:Talen|AWS).{0,180}(?:1\.92\s*GW|1,920\s*MW)|(?:1\.92\s*GW|1,920\s*MW).{0,180}(?:Talen|AWS)"),
         ("tln-20260630.htm",)),
    Rule("Crane / Constellation 835 MW",
         rx(r"(?:Crane|Constellation|Microsoft).{0,180}835\s*MW|835\s*MW.{0,180}(?:Crane|Constellation|Microsoft)"),
         ("constellation-launch-crane",)),
    Rule("Kairos / Google 500 MWe",
         rx(r"(?:Kairos|Google).{0,180}500\s*MWe|500\s*MWe.{0,180}(?:Kairos|Google)"),
         ("kairospower.com/google",)),
    Rule("Stanford HAI education metrics",
         rx(r"(?=.*(?:Stanford|AI Index))(?=.*(?:4/5|4 out of 5|6%|11%|17%))"),
         ("hai.stanford.edu",)),
    Rule("NVIDIA >US$500B financing target",
         rx(r"(?=.*NVIDIA)(?=.*(?:>\s*US\$500B|more than US\$500B|over US\$500B|超过\s*US\$500B))(?=.*(?:third-party|第三方|mobiliz))"),
         ("Mobilize-Over-500-Billion",)),
    Rule("OpenAI Stargate US$500B",
         rx(r"(?=.*(?:OpenAI|Stargate))(?=.*US\$500B)"),
         ("announcing-the-stargate-project",)),
    Rule("Anthropic / AWS long-duration compute",
         rx(r"(?=.*Anthropic)(?=.*(?:US\$100B|5\s*GW|1M\s*Trainium2))"),
         ("anthropic-amazon-compute",)),
)

def paragraphs(text: str) -> list[str]:
    return [p for p in re.split(r"\n\s*\n", text) if p.strip()]

def has_required_source(text: str, markers: tuple[str, ...]) -> bool:
    return any(marker in text for marker in markers)

def audit(files: list[Path], language: str) -> list[str]:
    failures: list[str] = []
    for path in files:
        if not path.exists():
            failures.append(f"{path.relative_to(ROOT)}: missing file")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        paras = paragraphs(text)
        for rule in COMMON_RULES:
            if any(rule.claim.search(p) for p in paras) and not has_required_source(text, rule.source_markers):
                failures.append(f"{path.relative_to(ROOT)}: missing required source for {rule.name}")
    print(f"{language}: checked {len(files)} research files")
    return failures

def main() -> int:
    failures = audit(ZH_FILES, "zh") + audit(EN_FILES, "en")
    if failures:
        print("\nRequired-source gate FAILED:")
        for item in failures:
            print(f"- {item}")
        return 1
    print("Required-source gate PASS: 96/96 research files clear.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
