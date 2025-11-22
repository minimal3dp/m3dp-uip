#!/usr/bin/env python
"""Generate an SVG badge from Playwright JSON report.

Reads `playwright-report.json` (output of `npx playwright test --reporter=json`)
and writes `frontend-e2e-badge.svg` summarizing pass rate.

Color logic:
  - 100% passed: green
  - >=90% passed: yellow
  - else: red
"""

from __future__ import annotations

import json
from pathlib import Path

REPORT_PATH = Path("playwright-report.json")
BADGE_PATH = Path("frontend-e2e-badge.svg")


def main() -> None:
    if not REPORT_PATH.exists():
        raise SystemExit("playwright-report.json not found")

    data = json.loads(REPORT_PATH.read_text())
    # Counters
    total = 0  # all discovered tests (including skipped)
    passed = 0
    skipped = 0
    flaky = 0

    def walk(node):
        """Recursively traverse Playwright JSON accumulating test stats.

        Playwright JSON reporter places run results under each test object's
        `results` list. The test-level `status` is usually "expected" and
        not indicative of pass/fail. We treat a test as passed if ANY of its
        result entries have status == "passed" (all workers succeeded).
        Maintain backward compatibility by also checking test-level status
        in case of older schema variants.
        """
        nonlocal total, passed
        if isinstance(node, dict):
            tests_list = node.get("tests")
            if isinstance(tests_list, list):
                for t in tests_list:
                    total += 1
                    results = t.get("results", [])
                    # Collect statuses from results list
                    result_statuses = [r.get("status") for r in results]
                    if any(s == "passed" for s in result_statuses):
                        passed += 1
                    elif any(s == "skipped" for s in result_statuses):
                        skipped += 1
                    elif any(s == "flaky" for s in result_statuses):
                        flaky += 1
                    else:
                        # Fallback: schema variant where test-level status is authoritative
                        ts = t.get("status")
                        if ts == "passed":
                            passed += 1
                        elif ts == "skipped":
                            skipped += 1
                        elif ts == "flaky":
                            flaky += 1
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(data)

    if total == 0:
        raise SystemExit("No tests found in report")

    # Effective total excludes skipped tests for pass rate; flaky treated as pass-neutral (counted in denominator)
    effective_total = max(1, total - skipped)  # avoid divide-by-zero
    rate = passed / effective_total * 100

    # Determine color based on rate and presence of flaky tests
    if rate == 100 and flaky == 0:
        color = "#4c1"  # bright green
    elif rate >= 90:
        color = "#dfb317"  # yellow
    else:
        color = "#e05d44"  # red
    label = "frontend e2e"
    # Show pass percentage plus skipped/flaky counts if present
    meta_parts = [f"{rate:.0f}% pass"]
    if skipped:
        meta_parts.append(f"{skipped} skipped")
    if flaky:
        meta_parts.append(f"{flaky} flaky")
    value = " | ".join(meta_parts)

    # Simple Shields-style SVG
    svg = f"""
<svg xmlns='http://www.w3.org/2000/svg' width='170' height='20' role='img' aria-label='{label}: {value}'>
  <title>{label}: {value}</title>
  <linearGradient id='s' x2='0' y2='100%'>
    <stop offset='0' stop-color='#bbb' stop-opacity='.1'/>
    <stop offset='1' stop-opacity='.1'/>
  </linearGradient>
  <clipPath id='r'><rect width='170' height='20' rx='3' fill='#fff'/></clipPath>
  <g clip-path='url(#r)'>
    <rect width='90' height='20' fill='#555'/>
    <rect x='90' width='80' height='20' fill='{color}'/>
    <rect width='170' height='20' fill='url(#s)'/>
  </g>
  <g fill='#fff' text-anchor='middle'
     font-family='Verdana,Geneva,DejaVu Sans,sans-serif' font-size='11'>
    <text x='45' y='15' fill='#010101' fill-opacity='.3'>{label}</text>
    <text x='45' y='14'>{label}</text>
    <text x='130' y='15' fill='#010101' fill-opacity='.3'>{value}</text>
    <text x='130' y='14'>{value}</text>
  </g>
</svg>
""".strip()

    BADGE_PATH.write_text(svg)
    print(
        f"Generated {BADGE_PATH} (passed={passed}, total={total}, skipped={skipped}, flaky={flaky}, rate={rate:.2f}%)"
    )


if __name__ == "__main__":
    main()
