---
description: The Repository Librarian. Reviews the repo against the Strategy Guide to ensure alignment.
---

1. Read the strategy guide to load context:
   - `view_file "strategy/M3DP Strategy Guide (2025-2026).md"`
2. Check for architectural drift (React/Next.js/AI Bloat):
   - `grep_search "React" .`
   - `grep_search "langchain" .`
   - `grep_search "openai" .`
   - `grep_search "vectorstore" .`
3. Verify Terminology Usage:
   - `grep_search "Hardware Bridge" .`
   - `grep_search "Sprint & Coast" .`
4. Report any findings that contradict the "Micro-App" stateless architecture or specific vocabulary.
