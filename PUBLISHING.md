# Publication Branch Policy

This repository is a research report, not an application project. GitHub Actions is not part of the research, evidence-audit, copy-editing, translation, or figure-production workflow.

## Branch roles

- `research` — working branch for research corrections, source repairs, evidence audits, English copy-editing, figures, and bilingual parity work.
- `main` — publication branch. A change reaches `main` only when it is intentionally ready to update the public edition.

GitHub Pages currently publishes the static site from `main`. GitHub may therefore create its own `pages build and deployment` run for every push to `main`, even when a commit does not modify `docs/`. This is hosting infrastructure, not report CI.

## Working rule

Do not use `main` for routine research iterations. Work on `research` (or a short-lived branch based on `research`) and keep intermediate commits there.

Only merge accepted work to `main` as an explicit publication event. Batch the accepted changes so one research cycle produces one publication update rather than one Pages deployment per intermediate commit.

## Canonical publication sequence

1. Research and revise the English canonical text on `research`.
2. Complete the evidence audit and freeze the accepted English revision.
3. Produce or synchronize the Chinese translation only after the English text is accepted.
4. Complete bilingual parity review where applicable.
5. Update the static `docs/` edition for that accepted revision.
6. Merge the publication batch to `main` once.

## Actions policy

- Do not add CI/CD workflows for the report itself.
- Do not add Release, package, PDF, EPUB, test-matrix, or application-style deployment workflows merely because the repository is hosted on GitHub.
- The only expected Actions activity is GitHub's own Pages deployment when an intentional publication commit reaches `main`.
- PDF, if produced later, is a publishing artifact after the text is finalized; it does not require a standing Actions pipeline.

## Manual acceptance gates (no CI)

The repository includes two opt-in, **manual** tools. They must run on a machine with a complete repository checkout and, for browser validation, a working network/browser policy. The presence of a script or successful static validation is **not** evidence that its run passed.

**1. Complete local Python/source and research calculation checks:**

```sh
python3 scripts/manual-release-audit.py --output ./manual-audit.json
```

This runs ten root structural/numeric/rights/model checks and nine Phase II reproducibility scripts (19 total). Nonzero exits, missing scripts and timeouts are explicit failures, not silent skips. External evidence URLs are optional and network-dependent:

```sh
python3 scripts/manual-release-audit.py --include-external --output ./manual-audit-with-links.json
```

**2. Real Chromium reader checks (desktop/mobile, English/Chinese):**

```sh
python3 -m pip install playwright
python3 -m playwright install chromium
python3 scripts/smoke-web-reader.py --base-url https://kamanager2012.github.io/ai-infra-hegemony/ --screenshot-dir ./smoke-shots
```

The browser script validates 18 independently reported cases: chapter 1, 32, 33 and the dated Q4 document in both languages on desktop and mobile, plus homepage CTA navigation. It checks rendered tables and footnotes, navigation, JavaScript exceptions, and horizontal overflow. A local system Chromium can be selected with `CHROMIUM_PATH` where supported. **Do not label the website visually accepted unless all cases actually run on an accessible site and exit 0**.

These are manual publishing checks only. They do **not** create GitHub Actions workflows, automate release publishing, or change the frozen 2026-08-28 evidence cutoff.

