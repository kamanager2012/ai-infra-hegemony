#!/usr/bin/env python3
"""Manual, local-only research audit runner (no GitHub Actions/CI).

Run at a full git checkout:
    python scripts/manual-release-audit.py --output ./manual-audit.json
    python scripts/manual-release-audit.py --include-external --output ./manual-audit-with-links.json

The default suite uses only local data and stdlib-compatible repo scripts.
The optional external URL check needs working Internet access. Results are
not marked PASS unless the actual command completed successfully.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
ROOT_CHECKS = (
    "scripts/check-links.py",
    "scripts/check-publication-editorial.py",
    "scripts/check-publication-numeric-claims.py",
    "scripts/check-publication-rights.py",
    "scripts/check-required-sources.py",
    "scripts/check-research-layer-consistency.py",
    "scripts/check-research-numeric-claims.py",
    "scripts/recompute_models.py",
    "scripts/selftest-layer-consistency-gate.py",
    "scripts/selftest-publication-numeric-gate.py",
)
RESEARCH_CHECKS = (
    "recompute_capital_to_cash.py",
    "recompute_chain_amplification.py",
    "recompute_channel_discriminator.py",
    "recompute_demand_composition.py",
    "recompute_energization.py",
    "recompute_frozen_gate_status.py",
    "recompute_ramp_gap.py",
    "recompute_vswo_breakeven.py",
    "verify_sol_event.py",
)


def run_check(relative: str, timeout_s: int) -> dict:
    target = ROOT / relative
    start = time.monotonic()
    record = {"command": [sys.executable, relative], "status": "not_run"}
    if not target.is_file():
        record.update(status="missing", detail=f"File not found: {relative}")
        return record
    try:
        cp = subprocess.run(
            [sys.executable, str(target)], cwd=str(ROOT), text=True,
            capture_output=True, timeout=timeout_s, check=False,
        )
        record["exit_code"] = cp.returncode
        record["status"] = "pass" if cp.returncode == 0 else "fail"
        record["stdout_tail"] = cp.stdout[-1200:]
        record["stderr_tail"] = cp.stderr[-1200:]
    except subprocess.TimeoutExpired:
        record.update(status="timeout", detail=f"Timeout after {timeout_s}s")
    except OSError as exc:
        record.update(status="error", detail=f"{type(exc).__name__}: {exc}")
    finally:
        record["elapsed_s"] = round(time.monotonic() - start, 3)
    return record


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--timeout-s", type=int, default=180)
    ap.add_argument("--include-external", action="store_true", help="also check external evidence URLs (requires internet)")
    ap.add_argument("--output", type=Path, help="write audit JSON to this path")
    args = ap.parse_args()
    if args.timeout_s < 1:
        ap.error("--timeout-s must be positive")
    entries = list(ROOT_CHECKS)
    entries += ["research-validation/scripts/" + name for name in RESEARCH_CHECKS]
    if args.include_external:
        entries.append("scripts/check-external-links.py")
    results = [run_check(name, args.timeout_s) for name in entries]
    summary = {
        "repository": ROOT.name,
        "checks": len(results),
        "passed": sum(row["status"] == "pass" for row in results),
        "failed_or_unrun": sum(row["status"] != "pass" for row in results),
        "external_link_check_included": args.include_external,
        "results": results,
    }
    data = json.dumps(summary, ensure_ascii=False, indent=2)
    print(data)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data + "\n", encoding="utf-8")
    return 0 if summary["failed_or_unrun"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
