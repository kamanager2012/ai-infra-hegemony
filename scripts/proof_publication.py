#!/usr/bin/env python3
"""Publication artifact proof runner.

Runs deterministic structural checks on the final bilingual PDF/EPUB outputs
and renders representative PDF pages for human visual proof.

This does not replace human proofreading. It is the machine preflight that
must pass before the final visual/read-through sign-off.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIST = ROOT / "dist"

PDF_SPECS = {
    "zh": {
        "file": "ai-infrastructure-hegemony.zh.pdf",
        "anchors": ["AI Resource Gravity", "Anchor Compute Buyer", "S4", "证据"],
    },
    "en": {
        "file": "ai-infrastructure-hegemony.en.pdf",
        "anchors": ["AI Resource Gravity", "Anchor Compute Buyer", "S4", "Evidence"],
    },
}
EPUB_SPECS = {
    "zh": {
        "file": "ai-infrastructure-hegemony.zh.epub",
        "anchors": ["AI Resource Gravity", "Anchor Compute Buyer", "S4"],
    },
    "en": {
        "file": "ai-infrastructure-hegemony.en.epub",
        "anchors": ["AI Resource Gravity", "Anchor Compute Buyer", "S4"],
    },
}

REQUIRED_TOOLS = ["qpdf", "pdfinfo", "pdftotext", "pdffonts", "pdftoppm"]


class ProofFailure(RuntimeError):
    pass


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(
        cmd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and proc.returncode != 0:
        raise ProofFailure(
            f"command failed ({proc.returncode}): {' '.join(cmd)}\n"
            f"stdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
        )
    return proc


def require_tools() -> None:
    missing = [name for name in REQUIRED_TOOLS if shutil.which(name) is None]
    if missing:
        raise ProofFailure(f"missing required proof tools: {', '.join(missing)}")


def pdf_pages(path: Path) -> int:
    info = run(["pdfinfo", str(path)]).stdout
    match = re.search(r"^Pages:\s+(\d+)\s*$", info, re.M)
    if not match:
        raise ProofFailure(f"unable to read page count: {path}")
    return int(match.group(1))


def check_fonts(path: Path) -> dict:
    output = run(["pdffonts", str(path)]).stdout
    lines = [line.rstrip() for line in output.splitlines()]
    data = lines[2:] if len(lines) >= 3 else []
    fonts = []
    not_embedded = []
    for line in data:
        if not line.strip():
            continue
        # pdffonts uses whitespace-separated columns; embedded/subset are near
        # the end. Keep the raw line for portability across poppler versions.
        parts = line.split()
        fonts.append(line)
        if len(parts) >= 6:
            # Expected columns include: name type encoding emb sub uni object ID
            # Search the trailing flag zone rather than relying on one fixed
            # index across poppler releases.
            flag_zone = parts[-5:]
            if "no" in flag_zone[:2]:
                not_embedded.append(line)
    if not fonts:
        raise ProofFailure(f"no fonts reported by pdffonts: {path}")
    if not_embedded:
        raise ProofFailure(
            f"non-embedded fonts detected in {path.name}:\n" + "\n".join(not_embedded)
        )
    return {"font_rows": len(fonts), "not_embedded": 0}


def extract_pdf_text(path: Path, out: Path) -> str:
    run(["pdftotext", "-layout", str(path), str(out)])
    text = out.read_text(encoding="utf-8", errors="replace")
    if len(text.strip()) < 20_000:
        raise ProofFailure(f"extracted PDF text unexpectedly short: {path}")
    if "\ufffd" in text:
        raise ProofFailure(f"Unicode replacement character found in extracted PDF text: {path}")
    return text


def check_anchors(text: str, anchors: list[str], label: str) -> None:
    missing = [x for x in anchors if x not in text]
    if missing:
        raise ProofFailure(f"{label}: missing extracted-text anchors: {missing}")


def page_text_lengths(path: Path, pages: int, temp_dir: Path) -> list[int]:
    lengths: list[int] = []
    for page in range(1, pages + 1):
        out = temp_dir / f"page-{page:04d}.txt"
        run(["pdftotext", "-f", str(page), "-l", str(page), str(path), str(out)])
        txt = out.read_text(encoding="utf-8", errors="replace")
        lengths.append(len(re.sub(r"\s+", "", txt)))
    return lengths


def check_blank_pages(lengths: list[int], label: str) -> dict:
    blank = [i + 1 for i, n in enumerate(lengths) if n == 0]
    # A single intentionally blank page can appear due to book/report layout.
    # Multiple consecutive blanks or too many blanks indicate broken pagination.
    consecutive_pairs = [
        (a, b) for a, b in zip(blank, blank[1:]) if b == a + 1
    ]
    if consecutive_pairs or len(blank) > 4:
        raise ProofFailure(
            f"{label}: suspicious blank pages: {blank}; "
            f"consecutive={consecutive_pairs}"
        )
    return {"blank_pages": blank}


def check_bbox(path: Path, bbox_file: Path) -> dict:
    run(["pdftotext", "-bbox-layout", str(path), str(bbox_file)])
    raw = bbox_file.read_text(encoding="utf-8", errors="replace")
    if "<page" not in raw:
        raise ProofFailure(f"bbox extraction produced no pages: {path}")
    overflow = []
    current_w = current_h = None
    page_num = 0
    for line in raw.splitlines():
        pm = re.search(r'<page\s+width="([0-9.]+)"\s+height="([0-9.]+)"', line)
        if pm:
            page_num += 1
            current_w = float(pm.group(1))
            current_h = float(pm.group(2))
            continue
        if current_w is None or current_h is None:
            continue
        wm = re.search(
            r'<word\s+xMin="(-?[0-9.]+)"\s+yMin="(-?[0-9.]+)"\s+'
            r'xMax="(-?[0-9.]+)"\s+yMax="(-?[0-9.]+)"',
            line,
        )
        if not wm:
            continue
        x0, y0, x1, y1 = map(float, wm.groups())
        if x0 < -1 or y0 < -1 or x1 > current_w + 1 or y1 > current_h + 1:
            overflow.append(
                {"page": page_num, "box": [x0, y0, x1, y1], "page_size": [current_w, current_h]}
            )
            if len(overflow) >= 20:
                break
    if overflow:
        raise ProofFailure(f"{path.name}: text boxes outside page bounds: {overflow[:5]}")
    return {"bbox_overflow": 0}


def sample_pages(page_count: int) -> list[int]:
    candidates = {
        1,
        2,
        3,
        4,
        5,
        max(1, page_count // 4),
        max(1, page_count // 2),
        max(1, (page_count * 3) // 4),
        max(1, page_count - 4),
        max(1, page_count - 3),
        max(1, page_count - 2),
        max(1, page_count - 1),
        page_count,
    }
    return sorted(x for x in candidates if 1 <= x <= page_count)


def render_samples(path: Path, out_dir: Path, pages: list[int]) -> list[str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    rendered = []
    for page in pages:
        prefix = out_dir / f"page-{page:04d}"
        run(
            [
                "pdftoppm",
                "-f",
                str(page),
                "-l",
                str(page),
                "-singlefile",
                "-png",
                "-r",
                "150",
                str(path),
                str(prefix),
            ]
        )
        png = prefix.with_suffix(".png")
        if not png.exists() or png.stat().st_size < 10_000:
            raise ProofFailure(f"representative page render failed or too small: {png}")
        rendered.append(str(png.relative_to(ROOT)))
    return rendered


def check_pdf(path: Path, lang: str, proof_root: Path) -> dict:
    if not path.exists() or path.stat().st_size < 100_000:
        raise ProofFailure(f"PDF missing or unexpectedly small: {path}")
    run(["qpdf", "--check", str(path)])
    pages = pdf_pages(path)
    if pages < 60:
        raise ProofFailure(f"{path.name}: suspicious page count {pages} (<60)")

    work = proof_root / lang
    work.mkdir(parents=True, exist_ok=True)
    text_file = work / "extracted.txt"
    bbox_file = work / "bbox.html"

    text = extract_pdf_text(path, text_file)
    check_anchors(text, PDF_SPECS[lang]["anchors"], path.name)
    font_result = check_fonts(path)
    bbox_result = check_bbox(path, bbox_file)

    temp_pages = work / "page-text"
    temp_pages.mkdir(exist_ok=True)
    lengths = page_text_lengths(path, pages, temp_pages)
    blank_result = check_blank_pages(lengths, path.name)

    samples = sample_pages(pages)
    rendered = render_samples(path, work / "renders", samples)

    return {
        "file": str(path.relative_to(ROOT)),
        "bytes": path.stat().st_size,
        "pages": pages,
        **font_result,
        **bbox_result,
        **blank_result,
        "sample_pages": samples,
        "sample_renders": rendered,
    }


def epub_text(zf: zipfile.ZipFile) -> str:
    pieces = []
    for name in zf.namelist():
        lower = name.lower()
        if lower.endswith((".xhtml", ".html", ".htm", ".ncx", ".opf")):
            try:
                txt = zf.read(name).decode("utf-8", errors="replace")
            except Exception:
                continue
            txt = re.sub(r"<[^>]+>", " ", txt)
            pieces.append(html.unescape(txt))
    return "\n".join(pieces)


def check_epub(path: Path, lang: str) -> dict:
    if not path.exists() or path.stat().st_size < 50_000:
        raise ProofFailure(f"EPUB missing or unexpectedly small: {path}")
    if not zipfile.is_zipfile(path):
        raise ProofFailure(f"not a valid EPUB/ZIP: {path}")

    with zipfile.ZipFile(path) as zf:
        bad = zf.testzip()
        if bad:
            raise ProofFailure(f"{path.name}: corrupt ZIP member {bad}")
        names = zf.namelist()
        if "mimetype" not in names:
            raise ProofFailure(f"{path.name}: missing mimetype")
        if zf.read("mimetype") != b"application/epub+zip":
            raise ProofFailure(f"{path.name}: invalid mimetype")
        if "META-INF/container.xml" not in names:
            raise ProofFailure(f"{path.name}: missing META-INF/container.xml")

        try:
            container = ET.fromstring(zf.read("META-INF/container.xml"))
        except ET.ParseError as exc:
            raise ProofFailure(f"{path.name}: invalid container.xml: {exc}") from exc

        rootfiles = [
            el.attrib.get("full-path")
            for el in container.iter()
            if el.tag.endswith("rootfile")
        ]
        rootfiles = [x for x in rootfiles if x]
        if not rootfiles or not all(x in names for x in rootfiles):
            raise ProofFailure(f"{path.name}: unresolved OPF rootfile {rootfiles}")

        nav_like = [
            x for x in names
            if x.lower().endswith(("nav.xhtml", "toc.ncx"))
            or "/nav." in x.lower()
            or "/toc." in x.lower()
        ]
        if not nav_like:
            raise ProofFailure(f"{path.name}: no navigation/toc document found")

        text = epub_text(zf)
        check_anchors(text, EPUB_SPECS[lang]["anchors"], path.name)
        if "\ufffd" in text:
            raise ProofFailure(f"{path.name}: Unicode replacement character in EPUB text")

    return {
        "file": str(path.relative_to(ROOT)),
        "bytes": path.stat().st_size,
        "members": len(names),
        "opf": rootfiles,
        "navigation_files": nav_like[:10],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", type=Path, default=DEFAULT_DIST)
    parser.add_argument("--proof-dir", type=Path, default=DEFAULT_DIST / "proof")
    args = parser.parse_args()

    require_tools()
    args.proof_dir.mkdir(parents=True, exist_ok=True)

    report = {
        "status": "PASS",
        "scope": "bilingual PDF/EPUB machine proof",
        "pdf": {},
        "epub": {},
        "human_visual_proof_required": True,
    }

    try:
        for lang, spec in PDF_SPECS.items():
            report["pdf"][lang] = check_pdf(args.dist / spec["file"], lang, args.proof_dir)
        for lang, spec in EPUB_SPECS.items():
            report["epub"][lang] = check_epub(args.dist / spec["file"], lang)
    except ProofFailure as exc:
        report["status"] = "FAIL"
        report["error"] = str(exc)

    report_file = args.proof_dir / "publication-proof.json"
    report_file.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
