# Claim Ledger and Numeric Audit

This directory supports evidence traceability for **AI Infrastructure Reordering**. It is research/editorial tooling and does not constitute external audit assurance.

## Scope

The repository contains two different layers that must not be confused:

- **Historical research corpus:** 40 research volumes + 8 macro essays in Chinese, with English counterparts. These files are retained as source research and analytical working material.
- **Formal report layer:** 32 Chinese chapters + 32 English chapters under `publication/` and `en/publication/`. This is the reader-facing monograph.

The claim ledger and numeric-check scripts help prevent unsupported numbers, denominator drift, time-window drift, and forecast/actual identity errors from propagating from the research corpus into the formal report.

## Current role

The repository includes deterministic local checks for numeric-source traceability and required-source patterns.

They are **not automated acceptance gates**. Human editorial judgment remains necessary for:

- whether a source actually supports the sentence;
- whether numerator and denominator match;
- whether time windows are comparable;
- whether guidance / expectation / estimate / forecast remains correctly labeled;
- whether a number belongs to Fact, model, scenario, or counterexample material.

Passing a script is therefore not equivalent to sentence-by-sentence audit assurance.

## Required record fields

- claim_id and optional bilingual_id
- source file and line
- claim text
- F / H / M / S / X identity
- A / B / C / D evidence grade
- source URL and title when applicable
- source publication date and observation window
- unit and denominator
- actual / guidance / expectation / estimate / forecast / scenario / model identity
- access date
- review status and notes

Schema: `../claim-ledger.schema.json`

## Local research checks

Run as needed:

```bash
python scripts/check-required-sources.py
python scripts/check-research-numeric-claims.py
python scripts/check-publication-numeric-claims.py
python scripts/check-research-layer-consistency.py
```

The research-layer checker covers the retained historical corpus. The publication-layer checker covers the 64 formal bilingual chapters.

The publication-layer checker grants a numeric candidate coverage on four grounds: a footnote, URL or sourced table; a stated model/scenario boundary; a stated arithmetic block; or a repetition of a value already sourced in the same chapter. The boundary is read in the candidate's own paragraph, in the lead line of its list, and in a nine-line window around it. That window is the broadest of the three and crosses paragraph boundaries, so it accepts only phrases that name a number's epistemic status — an unavoidable word (`as of`, 截至, the report, `if`) is grammar, not a boundary. The paragraph and lead windows keep the full phrase set, because restricting them the same way turns nine frozen sentences into failures, every one of them a real boundary whose marker happens to be a common word. It has its own negative-path suite, which mutates a throwaway copy of the two publication trees:

```bash
python scripts/selftest-publication-numeric-gate.py
```

Its 10 cases (4 must fire, 6 must stay green) cover each concession in turn, and each declares how many candidates its fixture must add, so a case cannot pass by inserting text the gate never considered as a candidate at all.

The Phase II consistency checker covers `research-validation/`. That directory is outside the other two by construction: a Phase II number is sourced either by a value an upstream layer already publishes or by a script recomputing it from a versioned JSON input, and neither is a URL. Its rule is correspondingly stronger — every registered headline token must appear in the layer's script stdout, in the English canonical, and in the Chinese translation, so a documented number cannot survive a script that stopped producing it. It also fails on a layer added without README wiring, a translation that stops tracking its canonical, and an orphan or renamed layer file.

Four of its checks reach past the registered headline set. **Table parity** requires a layer's tables to carry the same quantities in both editions, which needs no exception list because a translation may not move a number at all. **Stated derivations** re-implement, inside the gate, an arithmetic rule a layer states in prose, and require it to reproduce the value the layer publishes — the layer's own script does the same arithmetic, so agreement means two implementations agree rather than one implementation believing itself. **Unaccounted values** enumerate the residue: quantities in a layer's canonical that no script output, versioned input or registered token produces, each declared with the reason it is legitimate, and checked in both directions so a new unaccounted quantity fails and a declaration that has gone stale fails too. The register declares 11; they were measured before the rule was enforced, which is why the list is short and every entry has a nameable reason. When the check was written the list held 13 — two of them (`15`'s unrounded 3.976, `18`'s requirement level 19.88) were values their scripts computed and did not print, and both left the list when the scripts were changed to print them. That is the direction the check is meant to push. **README summaries** close the same accounting one level out: every quantity on the README's bullet for a layer must be one that layer produces, with a fraction also accepted as its percent. It credits the layer's tables, tokens and script output but not its prose, because prose is where retired values legitimately live — crediting it makes the rule vacuous, which was measured rather than assumed.

A failing Phase II check additionally prints the layers it affects, not just the check that failed: the layers to re-run, their scripts, the sections of their canonical that cite the broken value, and the layers downstream of them that read the value second-hand. It has its own negative-path suite, which mutates a throwaway copy of the tree rather than the working copy:

```bash
python scripts/selftest-layer-consistency-gate.py
```

Candidate extraction:

```bash
python scripts/extract_numeric_claim_candidates.py --corpus all
```

Default output:

```text
data/generated/numeric-claim-candidates.jsonl
```

The extractor is intentionally high-recall. A line containing a number is a candidate, not automatically a historical fact. URLs and References sections are excluded to reduce noise.

## Audited ledgers

- `high-risk-research-claims.zh.jsonl`
- `high-risk-research-claims.en.jsonl`

The bilingual ledgers preserve actual / guidance / expectation / estimate / forecast / model identities and allow the same claim to be tracked across languages.

## Audit rule

A candidate may be closed only as:

- verified;
- downgraded;
- removed; or
- explicitly bounded as model / scenario / counterexample material.

The governing principle is the same as the publication methodology:

> **traceability is necessary, but semantic correctness still requires reading the source and the sentence together.**
