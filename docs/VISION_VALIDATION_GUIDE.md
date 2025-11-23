# Vision Model Validation Guide

This guide explains how to validate the vision API accuracy using reference defect images.

## Overview

The vision validation system allows you to:
1. Test vision API predictions against known defect classifications
2. Measure accuracy across different defect types
3. Identify misclassifications and edge cases
4. Track improvements over time as the system prompt evolves

## Quick Start

### 1. Collect Reference Images

Add defect images to `backend/tests/fixtures/defect_images/`:

```bash
backend/tests/fixtures/defect_images/
├── stringing/
│   ├── stringing_001.jpg
│   ├── stringing_001_metadata.json
│   ├── stringing_002.jpg
│   ├── stringing_002_metadata.json
│   └── ...
├── warping/
├── layer_shift/
└── ...
```

### 2. Create Metadata Files

For each image, create a JSON metadata file:

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
  "notes": "Clear example with good lighting"
}
```

### 3. Run Validation

```bash
# Validate all defects
python -m backend.scripts.validate_vision_model

# Validate specific defect type
python -m backend.scripts.validate_vision_model --defect stringing

# Save report to custom location
python -m backend.scripts.validate_vision_model --output reports/validation.json

# Verbose logging
python -m backend.scripts.validate_vision_model --verbose
```

### 4. Review Results

The script outputs:
- Overall accuracy percentage
- Per-defect accuracy breakdown
- List of misclassified images
- Detailed JSON report

## Image Collection Sources

### Recommended Sources

1. **RepRap Pictorial Guide** (Open License)
   - URL: https://reprap.org/wiki/Print_Troubleshooting_Pictorial_Guide
   - License: Open/Community
   - Best for: Direct integration without licensing concerns

2. **All3DP Troubleshooting Guide**
   - URL: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
   - Coverage: 40+ defect types
   - Best for: Comprehensive examples

3. **Prusa Knowledge Base**
   - URL: https://help.prusa3d.com/category/print-quality-troubleshooting_225
   - Best for: High-quality before/after photos
   - **CRITICAL**: Best source for vision training

4. **Simplify3D Guide**
   - URL: https://www.simplify3d.com/resources/print-quality-troubleshooting/
   - Coverage: 23 quality issues
   - Best for: Side-by-side comparisons

### Collection Guidelines

1. **Diversity**: 5-10 images per defect category minimum
2. **Quality**: High resolution (min 800px), good lighting
3. **Variety**: Different angles, severities, materials
4. **Attribution**: Track source in metadata
5. **Licensing**: Respect copyright (educational/fair use)

### Priority Defect Types

Focus on the 8 primary defect classes from troubleshooting.csv:

1. **Stringing** (HIGH) - Thin threads between parts
2. **Warping** (HIGH) - Corners lifting from bed
3. **Layer Shift** (HIGH) - Misaligned layers
4. **Under-Extrusion** (HIGH) - Gaps in walls/top layers
5. **Over-Extrusion** (MEDIUM) - Blobs, zits, bulges
6. **Poor Bridging** (MEDIUM) - Sagging between supports
7. **Layer Separation** (MEDIUM) - Delamination
8. **Spaghetti** (HIGH) - Failed adhesion, tangled mess

## Understanding Results

### Accuracy Metrics

```
Total Images: 100
Correct Predictions: 85
Overall Accuracy: 85.00%

Accuracy by Defect Type:
  Stringing: 9/10 (90.00%)
  Warping: 8/10 (80.00%)
  Layer_Shift: 7/10 (70.00%)
  ...
```

### Interpreting Results

- **>90% accuracy**: Excellent - Model performs well
- **80-90% accuracy**: Good - May need prompt refinement
- **70-80% accuracy**: Fair - Investigate misclassifications
- **<70% accuracy**: Poor - System prompt needs improvement

### Common Misclassifications

1. **Stringing vs. Under-Extrusion**
   - Similar visual markers (thin lines)
   - Solution: Emphasize thread continuity in prompt

2. **Warping vs. Elephant Foot**
   - Both involve first layer issues
   - Solution: Focus on corner lifting vs. base expansion

3. **Over-Extrusion vs. Blobs**
   - Related defects with overlapping symptoms
   - Solution: Add these as related defects in CSV

## Iterative Improvement Process

### 1. Baseline Measurement

```bash
# Initial validation
python -m backend.scripts.validate_vision_model --output reports/baseline.json
```

### 2. Analyze Failures

Review `failed_predictions` in report:
- What patterns exist in misclassifications?
- Are specific defects consistently confused?
- Do visual markers need refinement?

### 3. Update System Prompt

Edit `backend/app/services/vision_service.py`:
- Add clarifying examples for confused defects
- Emphasize distinctive visual markers
- Include edge case handling

### 4. Re-validate

```bash
# After prompt changes
python -m backend.scripts.validate_vision_model --output reports/iteration_2.json
```

### 5. Compare Results

```python
# Compare two reports
import json

with open('reports/baseline.json') as f:
    baseline = json.load(f)

with open('reports/iteration_2.json') as f:
    current = json.load(f)

improvement = current['accuracy'] - baseline['accuracy']
print(f"Accuracy change: {improvement:+.2%}")
```

## Advanced Usage

### Programmatic Validation

```python
from backend.app.services.validation import VisionValidator
from backend.app.services.vision_service import VisionService

# Initialize services
vision_service = VisionService()
validator = VisionValidator(
    vision_service=vision_service,
    dataset_path="path/to/images"
)

# Run validation
report = await validator.validate_dataset()

# Access results
print(f"Accuracy: {report.accuracy:.2%}")
for defect, stats in report.by_defect_type.items():
    print(f"{defect}: {stats['accuracy']:.2%}")
```

### Integration with CI/CD

```yaml
# .github/workflows/vision-validation.yml
name: Vision Model Validation

on:
  pull_request:
    paths:
      - 'backend/app/services/vision_service.py'
      - 'backend/app/data/orca_recommendations/troubleshooting.csv'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run validation
        run: |
          python -m backend.scripts.validate_vision_model
      - name: Check accuracy threshold
        run: |
          # Fail if accuracy below 80%
          python -c "import json; report = json.load(open('backend/reports/vision_validation_report.json')); exit(0 if report['accuracy'] >= 0.80 else 1)"
```

## Dataset Statistics

Track your dataset growth:

```bash
# Count images by defect type
find backend/tests/fixtures/defect_images -name "*.jpg" | cut -d'/' -f5 | sort | uniq -c

# Count total images
find backend/tests/fixtures/defect_images -name "*.jpg" | wc -l

# Find images missing metadata
for img in backend/tests/fixtures/defect_images/**/*.jpg; do
  meta="${img%.jpg}_metadata.json"
  [ ! -f "$meta" ] && echo "Missing: $meta"
done
```

## Troubleshooting

### No Images Found

```
ERROR: No images found in backend/tests/fixtures/defect_images
```

**Solution**: Add reference images with metadata. See collection guidelines above.

### API Key Not Configured

```
ERROR: GOOGLE_GENAI_API_KEY not configured
```

**Solution**: Set API key in `.env`:
```
GOOGLE_GENAI_API_KEY=your_key_here
```

### Low Accuracy

```
WARNING: Accuracy (65.00%) below 80% threshold
```

**Solutions**:
1. Review failed predictions in report
2. Update vision service system prompt
3. Add more training examples to troubleshooting.csv
4. Refine visual markers in CSV

### Metadata Validation Errors

```
WARNING: No metadata found for image_001.jpg
```

**Solution**: Create `image_001_metadata.json` with required fields.

## Future Enhancements

- [ ] Confusion matrix visualization
- [ ] Confidence threshold tuning
- [ ] Multi-defect detection support
- [ ] Automated prompt optimization
- [ ] Visual similarity clustering
- [ ] Fine-tuning dataset preparation

## Related Documentation

- [Vision Service](../backend/app/services/vision_service.py) - Main vision API implementation
- [Troubleshooting CSV](../backend/app/data/orca_recommendations/troubleshooting.csv) - Defect taxonomy
- [Phase 2.5 Enhancement](../TODO.md#phase-25-csv-knowledge-base-enhancement) - CSV expansion details
