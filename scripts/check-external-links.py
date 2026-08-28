#!/usr/bin/env python3
"""Check critical external evidence URLs, including redirect destinations."""
from __future__ import annotations
from pathlib import Path
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "critical-external-links.json"
UA = "ai-infra-hegemony-publication-link-check/1.0 (+https://github.com/kamanager2012/ai-infra-hegemony)"

def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Range": "bytes=0-4095"})
    with urllib.request.urlopen(req, timeout=30) as r:
        r.read(4096)
        return r.status, r.geturl()

def main():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures = []
    for item in data["links"]:
        last = None
        for attempt in range(3):
            try:
                status, final_url = fetch(item["url"])
                if status not in {200, 206}:
                    raise RuntimeError(f"HTTP {status}")
                needle = item.get("final_url_contains")
                if needle and needle not in final_url:
                    raise RuntimeError(f"redirected to unexpected URL: {final_url}")
                print(f"PASS {item[\"id\"]}: {status} {final_url}")
                last = None
                break
            except Exception as exc:
                last = exc
                if attempt < 2:
                    time.sleep(2 ** attempt)
        if last is not None:
            failures.append((item["id"], item["url"], str(last)))
            print(f"FAIL {item[\"id\"]}: {last}")

    print(f"checked {len(data[\"links\"])} critical external links; failures={len(failures)}")
    if failures:
        for ident, url, err in failures:
            print(f"  {ident}: {url} :: {err}")
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
