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

## Current Research Files

- **Project Report Resource Generation Guide.md** - Comprehensive guide covering Klipper calibration, firmware architecture, and deterministic calibration philosophy
- **EXTRACTED_FORMULAS.md** - Mathematical formulas for calibration calculators
- **Klipper Calibrations.xlsx** - Calibration reference data and lookup tables
- **jmmp-03-00064.md** - Systematic survey of FDM process parameters and their influence on part characteristics (useful for troubleshooting recommendations)
- **REFERENCES.md** - Citation list and research sources

## Key Topics

### Calibration and Troubleshooting (Core Focus)
- Klipper firmware calibration methods and formulas
- FDM process parameter optimization
- Defect detection and troubleshooting guides
- Deterministic calculation-based calibration tools

### AI-Powered Diagnosis (Supporting)
- Vision-based defect detection (image → diagnosis)
- Semantic routing for query classification
- Troubleshooting knowledge base integration

### Out of Scope (Separate Apps)
- Anisotropy and material properties → filament.minimal3dp.com
- ACO path optimization → separate tool
- Hardware sensors and real-time monitoring
- ML model training and predictive systems

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
