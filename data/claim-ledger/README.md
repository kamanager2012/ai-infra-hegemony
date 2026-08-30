# Claim Ledger and Numeric Audit

This directory supports evidence traceability for **The Age of AI Infrastructure Hegemony**. It is research/editorial tooling and does not constitute external audit assurance.

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
```

The research-layer checker covers the retained historical corpus. The publication-layer checker covers the 64 formal bilingual chapters.

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
