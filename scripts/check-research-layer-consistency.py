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
HEADING_RE = re.compile(r"^(#{2,3})\s+(.+)$", re.M)

# The numbered checks, in order. This is load-bearing rather than decorative:
# main() prints the headings from here, and the self-test reads this dict to
# assert that every check has at least one case that makes it fire. A check
# added without a case therefore fails the self-test rather than sitting
# unverified - which is the whole reason the self-test exists.
CHECK_NAMES = {
    1: "translation pairing",
    2: "registry completeness",
    3: "ownership contract and Sources",
    4: "README file index",
    5: "authority graph",
    6: "README work order / authority rules / next stage",
    7: "recompute scripts",
    8: "headline tokens appear in script stdout, canonical and translation",
    9: "upstream layers acknowledge the layers built on them",
    10: "borrowed anchors still exist where the layer says they do",
    11: "README states the register's own size correctly",
}


def counts_line(layers: dict, scripts: list[Path]) -> str:
    """The register's size, in one canonical sentence.

    Counts stated in prose rot faster than anything else here - the README's
    claim about this register was wrong within the hour of being written - so
    the gate builds the sentence from the registry rather than trusting a hand
    count, exactly as it derives a layer's title from its H1."""
    plural = lambda n, one, many: f"{n} {one if n == 1 else many}"
    return ("**Registers:** "
            + ", ".join([
                plural(len(layers), "layer", "layers"),
                plural(sum(len(e["data"]) for e in layers.values()),
                       "versioned input", "versioned inputs"),
                plural(len(scripts), "recompute script", "recompute scripts"),
                plural(sum(len(e["headline_tokens"]) for e in layers.values()),
                       "headline token", "headline tokens"),
                plural(sum(len(e.get("borrowed_anchors", [])) for e in layers.values()),
                       "borrowed anchor", "borrowed anchors"),
            ]) + ".")


def use_root(path: Path) -> None:
    """Point the gate at a different checkout.

    The self-test runs this gate against a throwaway copy of the tree, so a
    mutation it expects to be caught cannot touch the real repository."""
    global ROOT, PHASE2, REGISTRY
    ROOT = path.resolve()
    PHASE2 = ROOT / "research-validation"
    REGISTRY = PHASE2 / "data" / "layer-consistency.json"


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


def sections_citing(path: Path, literal: str) -> list[str]:
    """Headings of the sections in `path` that contain `literal`.

    This is what turns a failure from "the anchor is gone" into "these are the
    places that have to change": the layer's own canonical is the thing a
    maintainer would otherwise have to grep."""
    body = read_if_present(path)
    if not body:
        return []
    marks = [(m.start(), m.group(2).strip()) for m in HEADING_RE.finditer(body)]
    found = []
    for i, (pos, title) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(body)
        if literal in body[pos:end]:
            found.append(title)
    return found


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    for arg in argv:
        if arg.startswith("--root="):
            use_root(Path(arg.split("=", 1)[1]))
        else:
            print(f"unknown argument: {arg}", file=sys.stderr)
            return 2

    reg = json.loads(read(REGISTRY))
    readme = read(PHASE2 / reg["readme"])
    epoch = reg["convention_epoch"]
    layers = reg["layers"]
    failures: list[str] = []
    # A failing check says what is wrong. This says what to do about it: which
    # layer is affected, what to re-run, and which of its sections cite the
    # broken thing. Keyed by layer id so a layer with several failures is
    # reported once, with all of them under it.
    impacts: dict[str, list[str]] = {}

    def check(ok: bool, label: str) -> None:
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if not ok:
            failures.append(label)

    def note(ident: str, first: str, *rest: str) -> None:
        """Record one item of guidance under a layer. `first` is the bullet;
        `rest` are the indented lines under it."""
        impacts.setdefault(ident, []).append([first, *rest])

    # source id (lowercase, as anchors spell it) -> layers that read from it.
    borrowers: dict[str, set[str]] = {}
    for lid, entry in layers.items():
        for anchor in entry.get("borrowed_anchors", []):
            borrowers.setdefault(anchor["source"].lower(), set()).add(lid)

    def downstream_of(ident: str) -> list[str]:
        """Registered layers that read a value from `ident`, transitively.

        A broken anchor two hops up is still a broken anchor: `18` reads 1.87
        from `15`, so if a `04c` figure that `15` republishes moves, `18` has to
        be re-checked even though it never cites `04c` itself. Without this the
        report would name the layer that failed and stop one hop short of the
        work."""
        spelling = {lid.lower(): lid for lid in layers}
        seen: set[str] = set()
        queue = [ident.lower()]
        while queue:
            for nxt in borrowers.get(queue.pop(), set()):
                low = nxt.lower()
                if low in seen or low == ident.lower():
                    continue
                seen.add(low)
                queue.append(low)
        return sorted((spelling.get(s, s) for s in seen), key=lambda s: (len(s), s))

    def at_or_after_epoch(ident: str) -> bool:
        return ident.isdigit() and int(ident) >= int(epoch)

    # ---------------------------------------------------------------- 1. pairing
    print(f"1. {CHECK_NAMES[1]}")
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
    print(f"2. {CHECK_NAMES[2]}")
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
    print(f"3. {CHECK_NAMES[3]}")
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
    print(f"4. {CHECK_NAMES[4]}")
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
    print(f"5. {CHECK_NAMES[5]}")
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
    print(f"6. {CHECK_NAMES[6]}")
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
    print(f"7. {CHECK_NAMES[7]}")
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
    print(f"8. {CHECK_NAMES[8]}")
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
            if where == "scriptcanonicalzh":
                continue
            # Two failure modes with different repairs, so do not merge them:
            # if the script still prints the token, a document drifted away from
            # its script and the script is the authority; if it does not, the
            # token no longer exists at all and the registry entry is presuming
            # a figure nothing produces.
            doc_rel = f"{ident}-{slug}.md"
            if "script" not in where:
                note(ident,
                     f"headline token {token!r} is no longer printed by scripts/{entry['script']}",
                     "either the computation changed, or this registry entry presumes a "
                     "figure nothing produces any more")
            else:
                missing = [n for n, src in (("canonical", doc), ("zh", zh)) if token not in src]
                note(ident,
                     f"headline token {token!r} is missing from {' and '.join(missing)} ({doc_rel})",
                     "the script still emits it, so the document drifted from its script")
                # Point at the sections that still carry it, so the repair is
                # local to those - that is the whole difference between "this
                # layer is broken" and a maintainable failure.
                for name, src in (("canonical", doc), ("zh", zh)):
                    if token not in src:
                        continue
                    path = PHASE2 / (f"{ident}-{slug}.md" if name == "canonical"
                                     else f"{ident}-{slug}.zh.md")
                    cited = sections_citing(path, token)
                    note(ident,
                         f"the {name} carries it under:",
                         *([f"§{c}" for c in cited] or ["(not under a heading)"]))

    # ------------------------------------------------------ 9. back-references
    print(f"9. {CHECK_NAMES[9]}")
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

    # --------------------------------------------------- 10. borrowed anchors
    print(f"10. {CHECK_NAMES[10]}")
    # "No new numeric identities" has been a rule this repository states and a
    # reader has to take on trust. This makes it executable: every anchor a
    # layer reads from outside itself must still be findable in the document it
    # came from. Layer 18's script already does this for layer 15's table; this
    # generalises it, and extends it to the frozen chapters, which are the
    # fixed point the research side is not permitted to move.
    chapter_files = reg.get("frozen_chapter_files", {})
    for ident, entry in layers.items():
        for anchor in entry.get("borrowed_anchors", []):
            source = anchor["source"]
            if source in chapter_files:
                targets = [ROOT / rel for rel in chapter_files[source]]
            else:
                targets = [m for m in sorted(PHASE2.glob(f"{source.lower()}-*.md"))
                           if not m.name.endswith(".zh.md")]
            if not targets:
                check(False, f"{ident} anchor {anchor['literal']!r} names unknown source {source}")
                note(ident, f"anchor {anchor['literal']!r} names source {source}, which is "
                            f"neither a layer on disk nor a mapped frozen chapter - fix the "
                            f"registry entry before reading anything else into this")
                continue
            found_in = [t.name for t in targets
                        if t.exists() and anchor["literal"] in read_if_present(t)]
            check(bool(found_in),
                  f"{ident} anchor {anchor['literal']!r} still in {source} ({anchor['role']})"
                  + ("" if found_in else f" - searched {[t.name for t in targets]}"))
            if found_in:
                continue
            slug = layers[ident]["slug"]
            cited = sections_citing(PHASE2 / f"{ident}-{slug}.md", anchor["literal"])
            note(ident,
                 f"anchor {anchor['literal']!r} ({anchor['role']}) is gone from {source}",
                 f"the change happened upstream, in {source}; this layer publishes a value "
                 f"derived from it, so {ident}-{slug}.md (+ .zh.md) has to be re-run and "
                 f"reviewed" + (", in the sections that cite the anchor:" if cited else
                                 ". The anchor is not cited verbatim in its prose - it "
                                 "reaches this layer through the script's JSON inputs."),
                 *[f"§{c}" for c in cited])
            # The layers that read from this one cannot have been unaffected:
            # they publish numbers this anchor feeds.
            for down in downstream_of(ident):
                note(down,
                     f"downstream of {ident}",
                     f"reads a value {ident} republishes from this anchor, without citing "
                     f"{source} itself - re-check after {ident} is updated")

    # ------------------------------------------------------- 11. README counts
    print(f"11. {CHECK_NAMES[11]}")
    # The register's own size, as the README states it. This is the audit-facing
    # claim - how much is actually covered - and the one a reader uses to decide
    # whether the register is worth anything, so it is the last number that
    # should be allowed to drift.
    wanted_counts = counts_line(layers, scripts)
    status = section(readme, "Current status") or ""
    check(wanted_counts in status,
          "README Current status states the register's size"
          + ("" if wanted_counts in status else f" - expected verbatim: {wanted_counts}"))

    # ----------------------------------------------------------------- summary
    total_layers = len([i for i in on_disk])
    registered_layers = len(layers)
    tokens = sum(len(e["headline_tokens"]) for e in layers.values())
    anchors = sum(len(e.get("borrowed_anchors", [])) for e in layers.values())
    print()
    print(f"Phase II consistency: layer files on disk={total_layers}, "
          f"registry entries={registered_layers}, "
          f"recompute scripts={len(scripts)}, headline tokens verified={tokens}, "
          f"borrowed anchors verified={anchors}")
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
        if impacts:
            print()
            print("Affected layers, and what each has to update:")
            for ident in sorted(impacts, key=lambda s: (len(s), s)):
                entry = layers.get(ident, {})
                slug = entry.get("slug")
                print(f"  {ident}  {ident}-{slug}.md" if slug else f"  {ident}")
                if entry.get("script"):
                    print(f"      re-run: research-validation/scripts/{entry['script']}")
                for block in impacts[ident]:
                    print(f"      - {block[0]}")
                    for extra in block[1:]:
                        print(f"          {extra}")
        print()
        print("Affected layers are listed because a failing anchor is not a "
              "cosmetic defect: the layer that borrowed it is publishing a "
              "number its source no longer carries. Never repair this by "
              "widening the literal - that deletes the check.")
        return 1
    print("research-validation consistency check PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
