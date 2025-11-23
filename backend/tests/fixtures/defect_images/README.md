# Defect Image Dataset

This directory contains reference images for vision model validation and benchmarking.

## Structure

```
defect_images/
├── stringing/
│   ├── image_001.jpg (with metadata.json)
│   ├── image_002.jpg
│   └── ...
├── warping/
├── layer_shift/
├── under_extrusion/
├── over_extrusion/
├── poor_bridging/
├── layer_separation/
├── spaghetti/
└── ...
```

## Metadata Format

Each image should have an accompanying `{filename}_metadata.json` file:

```json
{
  "defect_type": "Stringing",
  "severity": "Medium",
  "source": "All3DP",
  "source_url": "https://all3dp.com/...",
  "printer_type": "Generic",
  "material": "PLA",
  "expected_classification": "Stringing",
  "visual_markers": [
    "thin plastic threads",
    "strings between parts",
    "cobweb appearance"
  ],
  "notes": "Clear example of stringing with good lighting"
}
```

## Image Collection Sources

### Industry Guides (Public Sources)
1. **All3DP**: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
   - 40+ defect types with clear visual examples
   - Download strategy: Screenshot with attribution

2. **Prusa Knowledge Base**: https://help.prusa3d.com/category/print-quality-troubleshooting_225
   - Photo-documented before/after images
   - **CRITICAL**: Best source for vision training
   - Check licensing for fair use

3. **Simplify3D**: https://www.simplify3d.com/resources/print-quality-troubleshooting/
   - 23 quality issues with side-by-side comparisons
   - Educational use with attribution

4. **RepRap Pictorial Guide**: https://reprap.org/wiki/Print_Troubleshooting_Pictorial_Guide
   - Community-sourced catalog
   - Open-licensed content (can be integrated directly)

### Collection Guidelines

1. **Diversity**: 5-10 images per defect category minimum
2. **Quality**: High resolution, good lighting, clear defect visibility
3. **Variety**: Different angles, severities, materials, printer types
4. **Attribution**: Always track source and maintain proper licensing
5. **Anonymization**: Remove any personal information from images

### Licensing Considerations

- **Fair Use**: Educational/research purposes, non-commercial
- **Attribution**: Credit original sources in metadata
- **RepRap Content**: Use freely (open license)
- **Commercial Sources**: Limited screenshots with attribution for testing only

## Dataset Goals

- **Coverage**: All 63 defect types from troubleshooting.csv
- **Minimum**: 5 images per major defect (8 primary classes)
- **Target**: 10+ images per defect for robust validation
- **Total**: 300-600 images for comprehensive testing

## Usage

Images in this directory are used by:
1. `backend/app/services/validation/vision_validator.py` - Automated accuracy testing
2. `backend/tests/test_vision_validation.py` - Integration tests
3. Vision model fine-tuning (future Phase 7)

## Status

- [ ] Collect Stringing examples (0/10)
- [ ] Collect Warping examples (0/10)
- [ ] Collect Layer Shift examples (0/10)
- [ ] Collect Under-Extrusion examples (0/10)
- [ ] Collect Over-Extrusion examples (0/10)
- [ ] Collect Poor Bridging examples (0/10)
- [ ] Collect Layer Separation examples (0/10)
- [ ] Collect Spaghetti examples (0/10)
- [ ] Add metadata for all images (0/80)
