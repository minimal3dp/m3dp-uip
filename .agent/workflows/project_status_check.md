---
description: M3DP Project Manager. Enforces scope, timeline, and strategy.
---

1. Scope Enforcement:
   - Verify current work is within the "Micro-App" definition (Calculators: Rotation, Flow, PA, Current, Lead Screw).
   - `grep_search "Micro-App" .`
2. AI Bloat Check:
   - Ensure no heavy AI libraries (LangChain, Vector Stores) are being added.
3. Status Check:
   - Ask: "Are we in a Sprint (High Energy) or Coast (Maintenance) phase?"
   - Sprint = Production (Coding logic, Filming).
   - Coast = Polishing (CSS, Editing, Docs).
4. Revenue Alignment:
   - Verify "Hardware Bridge" strategy: Every tool must link to a specific affiliate hardware item.
