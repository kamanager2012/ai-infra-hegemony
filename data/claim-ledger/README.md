# Claim Ledger and Numeric Audit

This directory defines the machine-readable audit contract for historical and forward-looking quantitative claims.

## Current status

**Infrastructure: implemented. Full claim-by-claim audit: not yet complete.**

The schema and extractor do not satisfy the public-release hard gate by themselves. A numeric candidate becomes publication-audited only after a reviewer assigns claim identity, evidence grade, source, time window, denominator, and status.

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

## Candidate extraction

Run:

    python scripts/extract_numeric_claim_candidates.py --corpus all

Default output:

    dist/numeric-claim-candidates.jsonl

The extractor is intentionally high-recall. A line containing a number is a candidate, not automatically one historical fact. URLs and References sections are excluded to reduce noise.

## Audit rule

A candidate may be closed only as verified, downgraded, removed, or unreviewed. The release checklist must remain unchecked for full historical-number audit until the required corpus has no unresolved historical-Fact candidates.
