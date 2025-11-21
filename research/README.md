# Research Articles & References

This directory contains research papers, articles, and references that inform the M3DP-UIP architecture and implementation.

## 🔄 PDF to Markdown Automation

**All PDFs are automatically converted to markdown for version control:**

- ✅ Markdown files (`.md`) are tracked in git
- ❌ PDF files (`.pdf`) are gitignored (too large)
- 🔄 Conversion happens automatically when PDFs are added

### Manual Conversion

```bash
# Convert all PDFs in research/
python scripts/convert_research_pdfs.py

# Convert specific PDF
python scripts/convert_research_pdfs.py --file research/paper.pdf

# Force reconversion (ignore cache)
python scripts/convert_research_pdfs.py --force

# Watch mode (auto-convert on changes)
python scripts/convert_research_pdfs.py --watch
```

### Automatic Conversion (macOS)

Set up background service that auto-converts PDFs:

```bash
chmod +x scripts/setup_pdf_watch.sh
./scripts/setup_pdf_watch.sh
```

This installs a LaunchAgent that monitors `research/` and converts PDFs automatically.

### GitHub Actions

When you push PDFs to GitHub, they're automatically converted to markdown via GitHub Actions.

## Organization

- `papers/` - Academic papers and research publications
- `articles/` - Technical articles and blog posts
- `references/` - Quick reference materials and cheat sheets

## Key Topics

### Vision-Language Models for Manufacturing
- 3D-LLMs and Vision-Language Models for defect detection
- Computer vision applications in 3D printing

### RAG (Retrieval Augmented Generation)
- Context window optimization
- Structured knowledge base integration
- Router-based classification systems

### 3D Printing Calibration
- Klipper firmware calibration methods
- OrcaSlicer optimization techniques
- Material-specific settings and profiles

## Adding New Research

When adding new research materials:

1. Place files in the appropriate subdirectory
2. Update this README with a brief description
3. Link to the material from relevant documentation in `docs/`
4. Tag with relevant topics for easy discovery

## Citation Format

For academic papers, use:
```
Author(s). (Year). Title. Publication. DOI/URL
```

Example:
```
Smith, J., et al. (2024). 3D-LLMs for Manufacturing Defect Detection.
arXiv:2407.04180v1. https://arxiv.org/abs/2407.04180
```
