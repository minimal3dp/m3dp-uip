# Vision Validation Dataset

This directory contains reference images for validating the vision AI's defect detection accuracy.

## Structure

Each defect type has its own subdirectory containing:
- **images/**: Reference images (5-10 per defect type)
- **metadata.json**: Ground truth labels and context for each image

## Defect Types

Based on the 8-class defect taxonomy (from research):

1. **stringing** - Thin strands between parts where there shouldn't be material
2. **warping** - Corners lifting or edges curling up
3. **layer_shifting** - Layers misaligned, creating a stepped appearance
4. **under_extrusion** - Gaps, weak infill, or missing material
5. **over_extrusion** - Bulging, blob artifacts, or excess material
6. **first_layer_adhesion** - Poor bed adhesion, corners lifting on first layer
7. **surface_quality** - Rough surface, visible layer lines, or inconsistent texture
8. **support_issues** - Failed supports, support scarring, or hard-to-remove supports

## Metadata Schema

Each `metadata.json` file should follow this structure:

```json
{
  "defect_type": "stringing",
  "images": [
    {
      "filename": "stringing_001.jpg",
      "ground_truth": "stringing",
      "severity": "moderate",
      "description": "Clear stringing between towers on temperature test",
      "printer_context": {
        "model": "Ender 3 V2",
        "filament_type": "PLA",
        "nozzle_temp": 200,
        "print_speed": 60
      },
      "expected_recommendations": [
        "Enable retraction",
        "Increase retraction distance",
        "Lower printing temperature"
      ]
    }
  ]
}
```

## Usage

Run validation:
```bash
python backend/app/services/validation/run_validation.py
```

This will:
1. Load all metadata files
2. Send each image to the vision API
3. Compare predictions to ground truth
4. Generate accuracy report with confusion matrix
5. Identify misclassified images for prompt improvement

## Target Accuracy

- **Overall**: 80%+ correct classification
- **Per-defect**: 70%+ for each defect type
- **Confidence**: Average 0.6+ for correct predictions

## Data Collection Guidelines

### Image Quality
- Clear, well-lit photos
- Focus on the defect area
- Include context (full part or relevant section)
- Avoid extreme angles or heavy post-processing

### Diversity
- Different printer models
- Various filament types and colors
- Range of defect severities (mild, moderate, severe)
- Both Cartesian and CoreXY kinematics

### Ground Truth Accuracy
- Single dominant defect per image (avoid multi-defect images initially)
- Clear, unambiguous classification
- Expert validation recommended

## Contributing Images

1. Create subdirectory: `validation_data/{defect_type}/`
2. Add images: `validation_data/{defect_type}/images/`
3. Create metadata: `validation_data/{defect_type}/metadata.json`
4. Run validation script to verify format
5. Commit and push to feature branch

## Sources

Recommended sources for reference images:
- RepRap forums: https://reprap.org/wiki/Print_Troubleshooting_Pictorial_Guide
- All3DP guide: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
- Prusa Knowledge Base: https://help.prusa3d.com/
- Simplify3D guide: https://www.simplify3d.com/resources/print-quality-troubleshooting/
- Community submissions (with permission)

**Note**: Respect image copyrights. Only use images with explicit permission or from permissive licenses (CC-BY, CC0, etc.).
