#!/usr/bin/env python3
"""Cross-layer consistency gate for the Phase II research-validation layer system.

The repository has no CI. The other gates cover the frozen 32-chapter text and
the 96-file research corpus; `research-validation/` is outside all of them. This
gate closes that hole, and it closes it with the rule Phase II actually needs.

Phase II numbers are not sourced by URL. A Phase II number is sourced by one of:

  (a) a value an upstream layer already publishes (e.g. `18` asserting against
      `15`'s published required-cash table), or
  (b) a script recomputing it from a versioned JSON input under this directory.

Neither is a link, so the URL-based source-coverage gate cannot see them. The
stronger rule that fits is: every registered headline token must appear in the
layer's script stdout AND in the English canonical AND in the Chinese
translation. Those three cannot drift apart silently, so a documented number can
never survive a script that stopped producing it.

Two classes of defect this catches that nothing else does:

  * **Rot.** A layer's script output moves and its documentation does not, or
    the translation stops tracking the canonical. Nothing in the repository
    currently connects a published number to the script that produced it.
  * **Wiring drift.** A layer is added, renamed, or renumbered and the README
    stops describing the layer system it claims to be the maintenance contract
    for.

Convention boundary: layers 00-13 predate the Phase II documentation convention
and are checked only for boundary-free invariants. `convention_epoch` in
`data/layer-consistency.json` records where the convention starts and why; the
gate does not retro-fit the convention onto layers that never claimed it.

Exit 0 on success, 1 on any failed check.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHASE2 = ROOT / "research-validation"
REGISTRY = PHASE2 / "data" / "layer-consistency.json"

DOC_RE = re.compile(r"^(\d{2}[a-z]?)-(.+)\.md$")


def norm(text: str) -> str:
    """Fold the two multiplication glyphs so a script's `3.83x` matches `3.83×`."""
    return text.replace("×", "x")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_if_present(path: Path) -> str:
    """Empty string when absent, so a stale registry path fails a check rather
    than aborting the run partway through the checks with a traceback."""
    return read(path) if path.exists() else ""


def section(text: str, heading: str) -> str | None:
    """Body of `## <heading>`, up to the next `## `."""
    m = re.search(rf"^## {re.escape(heading)}\s*$", text, re.M)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def layer_title(path: Path) -> str:
    """The layer's name, derived from its H1: the work order keys off the title.

    Deriving it rather than storing it means a layer renamed in its own document
    but not in the work order fails, instead of two hand-kept strings agreeing
    with each other and disagreeing with the file.
    """
    body = read_if_present(path)
    if not body:
        return "<missing>"
    title = re.sub(r"^#\s*Phase II\s*·\s*", "", body.splitlines()[0])
    title = re.sub(r"\s+v\d+\.\d+\s*$", "", title)
    return re.sub(r"\s+Layer\s*$", "", title).strip()


def numbered_items(region: str) -> dict[int, str]:
    """Numbered list items, with continuation lines folded into the item text."""
    items: dict[int, str] = {}
    current: int | None = None
    for line in region.splitlines():
        m = re.match(r"^(\d+)\.\s+(.*)$", line)
        if m:
            current = int(m.group(1))
            items[current] = m.group(2)
        elif current is not None and line.strip() and not line.startswith("#"):
            items[current] += " " + line.strip()
        elif not line.strip():
            current = None
    return items


def main() -> int:
    reg = json.loads(read(REGISTRY))
    readme = read(PHASE2 / reg["readme"])
    epoch = reg["convention_epoch"]
    layers = reg["layers"]
    failures: list[str] = []

    def check(ok: bool, label: str) -> None:
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if not ok:
            failures.append(label)

    def at_or_after_epoch(ident: str) -> bool:
        return ident.isdigit() and int(ident) >= int(epoch)

    # ---------------------------------------------------------------- 1. pairing
    print("1. translation pairing")
    on_disk: dict[str, Path] = {}
    for p in sorted(PHASE2.glob("*.md")):
        m = DOC_RE.match(p.name)
        if not m:
            continue
        doc_id, slug = m.group(1), m.group(2)
        if slug.endswith(".zh"):
            continue
        on_disk[doc_id] = p
    zh_present = {i for i in on_disk if (PHASE2 / f"{i}-{DOC_RE.match(on_disk[i].name).group(2)}.zh.md").exists()}

    missing_zh = sorted(i for i in on_disk if at_or_after_epoch(i) and i not in zh_present)
    check(not missing_zh, f"every layer from {epoch} on has a .zh.md sibling"
                          + (f" (missing: {missing_zh})" if missing_zh else ""))

    orphans = []
    for p in sorted(PHASE2.glob("*.zh.md")):
        base = PHASE2 / (p.name[: -len(".zh.md")] + ".md")
        if not base.exists():
            orphans.append(p.name)
    check(not orphans, "no orphan .zh.md without its canonical"
                       + (f" (orphans: {orphans})" if orphans else ""))

    # ------------------------------------------------------------ 2. registry
    print("2. registry completeness")
    # The registry is what makes the rest of this gate exhaustive rather than
    # opt-in. A layer added under the convention but never registered would
    # otherwise skip every README wiring check silently.
    unregistered_layers = sorted(i for i in on_disk
                                 if at_or_after_epoch(i) and i not in layers)
    check(not unregistered_layers,
          "every layer from the epoch on has a registry entry"
          + (f" (unregistered: {unregistered_layers})" if unregistered_layers else ""))
    stale = sorted(set(layers) - set(on_disk))
    check(not stale,
          "every registry entry names a layer file on disk"
          + (f" (stale: {stale})" if stale else ""))
    # --------------------------------------------------------------- 3. contract
    print("3. ownership contract and Sources")
    for ident in sorted(on_disk, key=lambda s: (len(s), s)):
        if not at_or_after_epoch(ident):
            continue
        doc_path = on_disk[ident]
        slug = DOC_RE.match(doc_path.name).group(2)
        zh_path = PHASE2 / f"{ident}-{slug}.zh.md"
        for label, path in (("doc", doc_path), ("zh", zh_path)):
            if not path.exists():
                continue
            body = read(path)
            check(bool(re.search(r"^## 0\.", body, re.M)),
                  f"{ident} {label} carries an ownership contract (§0)")
            check(bool(re.search(r"^## Sources\s*$", body, re.M)),
                  f"{ident} {label} carries a Sources section")

    # ------------------------------------------------------------- 4. file index
    print("4. README file index")
    index = section(readme, "File index")
    if index is None:
        check(False, "README has a File index section")
        index = ""
    for ident, entry in layers.items():
        slug = entry["slug"]
        paths = [f"{ident}-{slug}.md", f"{ident}-{slug}.zh.md"] + \
                [f"data/{d}" for d in entry["data"]] + \
                ([f"scripts/{entry['script']}"] if entry["script"] else [])
        for rel in paths:
            # A registry entry naming a file that no longer exists is a stale
            # registry, not a README defect: report it as such instead of
            # crashing on the later read, and say so before the index claim.
            check((PHASE2 / rel).exists(), f"{ident} registry target {rel} exists on disk")
            check(rel in index, f"{ident} file index lists {rel}")

    # ---------------------------------------------------------- 5. authority graph
    print("5. authority graph")
    graph = section(readme, "Research Authority Graph")
    if graph is None:
        check(False, "README has a Research Authority Graph section")
        graph = ""
    graph_ids = set(re.findall(r"[├└]─\s+(\d{2}[a-z]?)", graph))
    for ident in sorted(layers, key=lambda s: (len(s), s)):
        if not at_or_after_epoch(ident):
            continue
        check(ident in graph_ids, f"authority graph lists {ident}")
    numeric_present = [int(i) for i in on_disk if i.isdigit()]
    if numeric_present:
        top_file = max(numeric_present)
        numeric_graph = [int(i) for i in graph_ids if i.isdigit()]
        top_graph = max(numeric_graph) if numeric_graph else None
        check(top_graph == top_file,
              f"authority graph top layer ({top_graph}) equals highest layer file ({top_file})")

    # ------------------------------------------------------ 6. README cross-links
    print("6. README work order / authority rules / next stage")
    offsets = reg["cross_reference_offsets"]
    anchor = int(offsets["anchor_layer"])
    work = numbered_items(section(readme, "Work order") or "")
    rules = numbered_items(section(readme, "Research Authority Graph") or "")
    rules = {k: v for k, v in rules.items() if "**" in v}
    nxt = numbered_items(section(readme, "Next stage") or "")
    for ident in sorted(layers, key=lambda s: (len(s), s)):
        if not at_or_after_epoch(ident):
            continue
        entry = layers[ident]
        step = int(ident) - anchor
        wpos, rpos, npos = (offsets["work_order"] + step,
                            offsets["authority_rule"] + step,
                            offsets["next_stage_item"] + step)
        title = layer_title(PHASE2 / f"{ident}-{entry['slug']}.md")
        check(title in work.get(wpos, ""),
              f"work order item {wpos} is about {ident} ({title!r})")
        check(f"`{ident}`" in rules.get(rpos, ""),
              f"authority rule {rpos} assigns {ident}")
        check(f"`{ident}`" in nxt.get(npos, ""),
              f"next-stage item {npos} maintains {ident}")

    # ------------------------------------------------------------ 7. scripts
    print("7. recompute scripts")
    scripts = sorted((PHASE2 / "scripts").glob("recompute_*.py"))
    check(bool(scripts), "research-validation carries recompute scripts")
    outputs: dict[str, str] = {}
    for path in scripts:
        proc = subprocess.run([sys.executable, str(path)],
                              capture_output=True, text=True, cwd=ROOT)
        check(proc.returncode == 0,
              f"{path.name} exits 0" + (f" (rc={proc.returncode})" if proc.returncode else ""))
        if proc.returncode != 0:
            print(proc.stdout[-800:])
            print(proc.stderr[-800:])
        outputs[path.name] = norm(proc.stdout)

    # ------------------------------------------------------- 8. headline tokens
    print("8. headline tokens appear in script stdout, canonical and translation")
    registered = {e["script"] for e in layers.values() if e["script"]}
    unregistered = [p.name for p in scripts if p.name not in registered]
    check(not unregistered,
          "every recompute script has a registry entry"
          + (f" (unregistered: {unregistered})" if unregistered else ""))
    for ident in sorted(layers, key=lambda s: (len(s), s)):
        entry = layers[ident]
        if not entry["script"]:
            continue
        slug = entry["slug"]
        doc = norm(read_if_present(PHASE2 / f"{ident}-{slug}.md"))
        zh = norm(read_if_present(PHASE2 / f"{ident}-{slug}.zh.md"))
        out = outputs.get(entry["script"], "")
        for token in entry["headline_tokens"]:
            where = "".join(k for k, src in (("script", out), ("canonical", doc), ("zh", zh))
                            if token in src)
            check(where == "scriptcanonicalzh",
                  f"{ident} headline {token!r} in script+canonical+zh"
                  + (f" (found only in: {where or 'nothing'})" if where != "scriptcanonicalzh" else ""))

    # ------------------------------------------------------ 9. back-references
    print("9. upstream layers acknowledge the layers built on them")
    # A new layer is one-directional by default: its own §0 says which layer
    # continues to own the underlying facts, and nothing makes that upstream
    # file point back. The reader who reaches the authority first then sees a
    # bridge listed as future work when it already exists. The registry names
    # only those dependencies - see acknowledgement_note - so a layer whose
    # upstream already points at it declares none.
    for ident, entry in layers.items():
        for upstream in entry.get("upstream_must_acknowledge", []):
            # Layer ids are written `04C` in prose but `04c-` on disk.
            matches = sorted(PHASE2.glob(f"{upstream.lower()}-*.md"))
            matches = [m for m in matches if not m.name.endswith(".zh.md")]
            if not matches:
                check(False, f"{ident} declares upstream {upstream}, which has no layer file")
                continue
            # Only the upstream canonical is checked: the layers being
            # acknowledged here are 00-13, which predate the translation
            # convention and have no .zh.md to carry the pointer.
            ack_doc = read_if_present(matches[0])
            # Two accepted forms: the backticked layer id, or a markdown link
            # whose target is that layer's document. Matching a bare `NN-`
            # prefix would also match a year or a line reference.
            points_back = f"`{ident}`" in ack_doc or f"]({ident}-" in ack_doc
            check(points_back,
                  f"{upstream} acknowledges {ident} (the layer built on it)")

    # ----------------------------------------------------------------- summary
    total_layers = len([i for i in on_disk])
    registered_layers = len(layers)
    tokens = sum(len(e["headline_tokens"]) for e in layers.values())
    print()
    print(f"Phase II consistency: layer files on disk={total_layers}, "
          f"registry entries={registered_layers}, "
          f"recompute scripts={len(scripts)}, headline tokens verified={tokens}")
    print(f"Convention epoch: layers >= {epoch} carry the full Phase II convention; "
          f"layers below it are checked for boundary-free invariants only.")
    print("Scope: PASS means every REGISTERED headline token is reproducible from "
          "its layer's script and agrees across canonical and translation. It is "
          "not a claim that every figure in research-validation/ is covered - the "
          "registry covers the headline set a layer stakes its conclusions on, and "
          "a layer with no registry entry would be caught by check 2, not by this. "
          "A token is usually a number but need not be: layer 21's set is section "
          "citations, because its output is a classification rather than a figure.")
    if failures:
        print(f"research-validation consistency check FAIL: {len(failures)} problem(s)")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("research-validation consistency check PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
