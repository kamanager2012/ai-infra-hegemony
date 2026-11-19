#!/usr/bin/env python3
"""Manual two-language desktop/mobile smoke of the published research reader.

Run from a network-enabled computer (not in CI):
    python scripts/smoke-web-reader.py --base-url https://kamanager2012.github.io/ai-infra-hegemony/
    python scripts/smoke-web-reader.py --base-url http://127.0.0.1:8000/ --screenshot-dir ./smoke-shots

Requires: pip install playwright && python -m playwright install chromium
Set CHROMIUM_PATH if using a system browser instead of a Playwright-managed binary.
No account, no mutations, no external actions beyond reading the chosen website.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
from urllib.parse import urlencode

from playwright.sync_api import Error as PlaywrightError, TimeoutError as PlaywrightTimeout, sync_playwright

VIEWPORTS = {"desktop": (1440, 900), "mobile": (390, 844)}
CASES = (
    ("en", "chapter", "1", "Executive Summary"),
    ("zh", "chapter", "1", "执行摘要"),
    ("en", "chapter", "32", "Master View"),
    ("zh", "chapter", "32", "Master View"),
    ("en", "chapter", "33", "Jensen Huang"),
    ("zh", "chapter", "33", "黄仁勋"),
    ("en", "doc", "2026-Q4-ROLLING-ADDENDUM.md", "Q4"),
    ("zh", "doc", "2026-Q4-ROLLING-ADDENDUM.md", "Q4"),
)


def run(base_url: str, *, screenshot_dir: Path | None = None, timeout: int = 20000) -> dict:
    base_url = base_url.rstrip("/") + "/"
    results: list[dict] = []
    if screenshot_dir:
        screenshot_dir.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        browser_kwargs: dict = {"headless": True}
        if os.environ.get("CHROMIUM_PATH"):
            browser_kwargs["executable_path"] = os.environ["CHROMIUM_PATH"]
        browser = pw.chromium.launch(**browser_kwargs)
        try:
            for viewport_name, (width, height) in VIEWPORTS.items():
                context = browser.new_context(
                    viewport={"width": width, "height": height},
                    is_mobile=(viewport_name == "mobile"),
                    has_touch=(viewport_name == "mobile"),
                    device_scale_factor=(2 if viewport_name == "mobile" else 1),
                )
                page = context.new_page()
                page.set_default_timeout(timeout)
                page_errors: list[str] = []
                page.on("pageerror", lambda err: page_errors.append(str(err)))
                for lang, key, value, expected in CASES:
                    params = urlencode({"lang": lang, key: value})
                    target = base_url + "?" + params
                    row = {"viewport": viewport_name, "lang": lang, "route": f"{key}={value}", "ok": False}
                    try:
                        page_errors.clear()
                        response = page.goto(target, wait_until="domcontentloaded", timeout=timeout)
                        if response is None or response.status >= 400:
                            raise AssertionError(f"route HTTP status: {response.status if response else 'none'}")
                        page.wait_for_function(
                            """() => {
                              const shell = document.getElementById('readerView');
                              const body = document.getElementById('readerBody');
                              if (!shell || !body || shell.classList.contains('hidden')) return false;
                              const value = body.textContent || '';
                              return value.length > 120 && !value.includes('Loading report')
                                && !value.includes('正在载入报告') && !value.includes('This chapter is unavailable')
                                && !value.includes('本章当前未包含') && !value.includes('This document is not included')
                                && !value.includes('该文档未包含');
                            }""",
                            timeout=timeout,
                        )
                        rendered = page.locator("#readerBody").inner_text()
                        if expected not in rendered:
                            raise AssertionError(f"expected text not found: {expected!r}")
                        if len(rendered.strip()) < 120:
                            raise AssertionError("rendered article is unexpectedly short")
                        if key == "doc" or value == "33":
                            if not page.locator("#readerBody table").count():
                                raise AssertionError("Markdown tables did not render")
                            if not page.locator("#readerBody .footnotes").count():
                                raise AssertionError("linked source footnotes did not render")
                        overflow = page.evaluate("document.documentElement.scrollWidth - window.innerWidth")
                        if overflow > 4:
                            raise AssertionError(f"unexpected document horizontal overflow: {overflow}px")
                        if viewport_name == "mobile" and key == "chapter" and value == "33":
                            toggle = page.locator("#readerNavToggle")
                            if not toggle.is_visible():
                                raise AssertionError("mobile chapter-drawer control not visible")
                            toggle.click()
                            if not page.locator("#readerNav.open").count():
                                raise AssertionError("mobile drawer did not open")
                        if page_errors:
                            raise AssertionError("JavaScript errors: " + "; ".join(page_errors[:3]))
                        if screenshot_dir:
                            page.screenshot(path=str(screenshot_dir / f"{viewport_name}-{lang}-{key}-{value.replace('.', '_')}.png"), full_page=True)
                        row.update(ok=True, chars=len(rendered))
                    except (AssertionError, PlaywrightError, PlaywrightTimeout) as exc:
                        row["error"] = str(exc)[:300]
                    results.append(row)
                row = {"viewport": viewport_name, "route": "home-navigation", "ok": False}
                try:
                    response = page.goto(base_url + "?lang=zh", wait_until="domcontentloaded", timeout=timeout)
                    if response is None or response.status >= 400:
                        raise AssertionError("homepage not reachable")
                    q4 = page.locator("#q4ResearchUpdate")
                    ch33 = page.locator("#specialStudy")
                    if q4.count() != 1 or ch33.count() != 1:
                        raise AssertionError("Q4/Ch33 homepage links missing")
                    if "2026-Q4-ROLLING-ADDENDUM.md" not in (q4.get_attribute("href") or ""):
                        raise AssertionError("Q4 link points to wrong document")
                    if "chapter=33" not in (ch33.get_attribute("href") or ""):
                        raise AssertionError("Ch33 homepage link missing route")
                    ch33.click()
                    page.wait_for_url("**chapter=33", timeout=timeout)
                    page.wait_for_function(
                        "() => (document.getElementById('readerBody')?.textContent || '').includes('黄仁勋')",
                        timeout=timeout,
                    )
                    row["ok"] = True
                except (AssertionError, PlaywrightError, PlaywrightTimeout) as exc:
                    row["error"] = str(exc)[:300]
                results.append(row)
                context.close()
        finally:
            browser.close()
    return {
        "base_url": base_url,
        "total": len(results),
        "passed": sum(bool(x["ok"]) for x in results),
        "failed": sum(not x["ok"] for x in results),
        "results": results,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base-url", default="https://kamanager2012.github.io/ai-infra-hegemony/")
    ap.add_argument("--screenshot-dir", type=Path)
    ap.add_argument("--timeout-ms", type=int, default=20000)
    args = ap.parse_args()
    try:
        result = run(args.base_url, screenshot_dir=args.screenshot_dir, timeout=args.timeout_ms)
    except Exception as exc:
        print(json.dumps({"fatal": type(exc).__name__, "message": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
