# Claim Ledger and Numeric Audit

This directory defines the machine-readable audit contract for historical and forward-looking quantitative claims.

## Current status

**High-risk semantic audit infrastructure: active and CI-enforced. Strict every-number source coverage is complete; lower-risk sentence-level semantic sign-off remains a separate editorial task.**

As of 2026-08-28:

- Chinese research required-source regression: **48/48 files PASS** (40 volumes + 8 macro essays).
- English research required-source regression: **48/48 files PASS**.
- Combined deterministic high-risk required-source gate: **96/96 research files clear**.
- Chinese high-risk ledger: **32 verified records**.
- English high-risk ledger: **32 verified mirror records** using the same `bilingual_id` set.
- Bilingual ledger integrity check: **32/32 bilingual IDs aligned; no duplicate claim IDs; no missing English source files**.
- Retired historical stress-test numbers in macro essays 3/4 are explicitly excluded from the Fact layer unless rebound to current A/B-grade evidence.
- Strict research-layer every-number source coverage: **96/96 files / 1,052 unit-bearing numeric candidates / 0 unresolved**.
- Strict formal Publication Layer numeric source coverage: **64/64 chapters / 529 candidates / 0 unresolved**.

The schema, extractor, required-source regression, and strict numeric coverage gates establish deterministic traceability and explicit model/scenario/counterexample boundaries for detected numeric claims. They do **not** constitute sentence-by-sentence external audit assurance. High-risk claims are separately reviewed in the bilingual ledgers; lower-risk source meaning, denominator, and time-window semantics remain part of final editorial sign-off where judgment is still required.

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

Schema: ../claim-ledger.schema.json

## Deterministic regression gates

Run:

    python scripts/check-required-sources.py
    python scripts/check-research-numeric-claims.py
    python scripts/check-publication-numeric-claims.py

`check-required-sources.py` checks paragraph-local high-risk claim patterns against required first-party or explicitly graded institutional source anchors across all **96** Chinese/English research files. The two strict numeric gates extend coverage across unit-bearing currency, percentages, power, storage/bandwidth, process, GPUs/CPUs, wafers, servers, tokens/parameters, and Chinese amount/count units in the research and formal publication layers. All three are enforced by `.github/workflows/links.yml`.

## Candidate extraction

Run:

    python scripts/extract_numeric_claim_candidates.py --corpus all

Default output:

    dist/numeric-claim-candidates.jsonl

The extractor is intentionally high-recall. A line containing a number is a candidate, not automatically one historical fact. URLs and References sections are excluded to reduce noise.

## Audited ledgers

- `high-risk-research-claims.zh.jsonl`
- `high-risk-research-claims.en.jsonl`

The two ledgers share the same 32 `bilingual_id` values and preserve actual / guidance / expectation / estimate / forecast / model identities.

## Audit rule

A candidate may be closed only as verified, downgraded, removed, or explicitly bounded as model/scenario/counterexample material. High-risk semantic verification and strict every-number source coverage are both closed as deterministic repository gates. The release checklist remains open only for lower-risk **semantic editorial sign-off** where a human still needs to judge whether source meaning, denominator, or time window exactly matches the sentence-level claim.
