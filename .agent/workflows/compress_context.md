---
description: Reduces token usage by compressing prompts/code files using semantic minimization.
---

1. Ask the user for the file path they want to compress if not provided.
2. Run the compression script:
   - `python scripts/compress_context.py <filename>`
3. If the user provided a raw text prompt instead of a file, rewrite it using "Telegraphic Style" (remove articles, link verbs, fluff).
