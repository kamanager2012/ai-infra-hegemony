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
