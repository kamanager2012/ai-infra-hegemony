# Claim Ledger and Numeric Audit

This directory defines the machine-readable audit contract for historical and forward-looking quantitative claims.

## Current status

**High-risk research-claim audit infrastructure: active and CI-enforced. Full every-number claim-by-claim audit: not yet complete.**

As of 2026-08-28:

- Chinese research required-source regression: **48/48 files PASS** (40 volumes + 8 macro essays).
- English research required-source regression: **48/48 files PASS**.
- Combined deterministic high-risk required-source gate: **96/96 research files clear**.
- Chinese high-risk ledger: **32 verified records**.
- English high-risk ledger: **32 verified mirror records** using the same `bilingual_id` set.
- Bilingual ledger integrity check: **32/32 bilingual IDs aligned; no duplicate claim IDs; no missing English source files**.
- Retired historical stress-test numbers in macro essays 3/4 are explicitly excluded from the Fact layer unless rebound to current A/B-grade evidence.

The schema, extractor, and required-source regression do not by themselves prove that every numeric line in the corpus has been individually audited. A numeric candidate becomes publication-audited only after a reviewer assigns claim identity, evidence grade, source, time window, denominator, and status.

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

This gate checks paragraph-local high-risk claim patterns against required first-party or explicitly graded institutional source anchors across all **96** Chinese/English research files. It is enforced by `.github/workflows/links.yml`.

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

A candidate may be closed only as verified, downgraded, removed, or unreviewed. High-risk required-source coverage is now closed as a regression gate; the broader release checklist must remain unchecked for **full every-number historical-Fact audit** until all required numeric candidates—not only the high-risk rule set—have been reviewed.
