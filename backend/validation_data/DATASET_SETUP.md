# Validation Dataset Setup Guide

This guide explains how to download, organize, and prepare 3D printing defect datasets for vision model validation.

## Quick Start

```bash
# 1. Install dataset download dependencies
pip install -r requirements-datasets.txt

# 2. Configure API keys (see below)
export ROBOFLOW_API_KEY="your_key_here"
# For Kaggle: Place kaggle.json in ~/.kaggle/

# 3. Download all datasets
python scripts/download_validation_datasets.py --dataset all

# 4. Run validation
python -m backend.scripts.validate_vision_model
```

## Dataset Overview

### 1. Kaggle FDM Dataset (1,912 images)
- **Source**: https://www.kaggle.com/datasets/wengmhu/fdm-3d-printing-defect-dataset
- **License**: MIT (permissive)
- **Defect Types**: 
  - Cracking (427) → Layer_Separation
  - Layer_shifting (364) → Layer_Shift
  - Stringing (447) → Stringing
  - Warping (538) → Warping
  - Off_platform (91) → Skipped (not in taxonomy)

### 2. Roboflow Large Dataset (5,900+ images)
- **Source**: https://universe.roboflow.com/abdelrahman-elkafas-yjn0j/3d-printing-defects-tlhcb
- **License**: CC BY 4.0 (requires attribution)
- **Defect Types**:
  - Spaghetti → Spaghetti
  - Stringing → Stringing
  - Zits → Over_Extrusion

### 3. Roboflow Small Dataset (588 images)
- **Source**: https://universe.roboflow.com/3d-defects/3d-error-monitoring2
- **License**: CC BY 4.0
- **Defect Types**: 6 classes (all in taxonomy)
- **Note**: Review quality (low model accuracy in source)

**Total**: ~7,800+ images covering 6/9 defect types

## API Key Setup

### Kaggle API

1. Create Kaggle account: https://www.kaggle.com/
2. Go to Account Settings → API → "Create New API Token"
3. Download `kaggle.json`
4. Place in `~/.kaggle/kaggle.json`
5. Set permissions: `chmod 600 ~/.kaggle/kaggle.json`

**Alternative**: Set environment variables:
```bash
export KAGGLE_USERNAME="your_username"
export KAGGLE_KEY="your_key"
```

### Roboflow API

1. Create Roboflow account: https://app.roboflow.com/
2. Go to Settings → API → Copy your API key
3. Set environment variable:
```bash
export ROBOFLOW_API_KEY="your_key_here"
```

## Download Script Usage

### Download All Datasets
```bash
python scripts/download_validation_datasets.py --dataset all
```

### Download Specific Dataset
```bash
# Kaggle only
python scripts/download_validation_datasets.py --dataset kaggle

# Roboflow large only
python scripts/download_validation_datasets.py --dataset roboflow_large

# Roboflow small only
python scripts/download_validation_datasets.py --dataset roboflow_small
```

### Test Download (Sample Mode)
Download only 10 samples per defect type for testing:
```bash
python scripts/download_validation_datasets.py --dataset all --samples 10
```

### Custom Output Directory
```bash
python scripts/download_validation_datasets.py --dataset all --output /path/to/data
```

## Directory Structure After Download

```
backend/validation_data/
├── README.md                           # This file (tracked in git)
├── spaghetti/
│   ├── images/                         # Ignored by git
│   │   ├── kaggle_spaghetti_001.jpg
│   │   ├── roboflow_*.jpg
│   │   └── ...
│   ├── kaggle_metadata.json            # Tracked in git
│   └── roboflow_metadata.json          # Tracked in git
├── stringing/
│   ├── images/
│   ├── kaggle_metadata.json
│   └── roboflow_metadata.json
├── warping/
│   └── ...
├── under_extrusion/
│   └── ...
├── over_extrusion/
│   └── ...
└── layer_shift/
    └── ...
```

**Note**: Image files are excluded from git (see `.gitignore`). Only metadata JSON files are tracked.

## Post-Download Steps

### 1. Verify Download
Check downloaded image counts:
```bash
# Count images per defect type
for dir in backend/validation_data/*/; do
    echo "$(basename "$dir"): $(ls "$dir/images" 2>/dev/null | wc -l) images"
done
```

### 2. Create Per-Image Metadata (Required)
The validator needs metadata for each image. Create `{image_name}_metadata.json` files:

```json
{
  "defect_type": "Stringing",
  "severity": "moderate",
  "source": "kaggle",
  "source_url": "https://kaggle.com/datasets/...",
  "printer_type": "FDM",
  "material": "PLA",
  "expected_classification": "Stringing",
  "visual_markers": [
    "thin threads between parts",
    "cobweb-like strands",
    "wispy filament"
  ],
  "notes": "Clear stringing visible between tower segments"
}
```

**Helper Script** (TODO - create this):
```bash
python scripts/generate_image_metadata.py --dataset backend/validation_data
```

### 3. Review Image Quality
Manually inspect a sample of images to ensure:
- Images are clear and well-lit
- Defects are visible and unambiguous
- Labels match the defect shown
- No corrupt or duplicate images

### 4. Run Validation
```bash
# Validate all defects
python -m backend.scripts.validate_vision_model

# Validate specific defect
python -m backend.scripts.validate_vision_model --defect stringing

# Save report to custom location
python -m backend.scripts.validate_vision_model --output reports/validation.json
```

## Gap Analysis

After downloading, you'll have coverage for:

✅ **Covered** (6/9):
- Spaghetti
- Stringing  
- Warping
- Under_Extrusion
- Over_Extrusion
- Layer_Shift (as Layer_Separation from Kaggle)

❌ **Still Need** (3/9):
- Ringing (ghosting artifacts)
- Poor_Bridging (sagging bridges)
- Layer_Separation (true delamination, not just layer shifts)

**Recommendations for Missing Defects**:
1. Search for additional Roboflow datasets
2. Capture your own test prints with these defects
3. Request community contributions
4. Check RepRap forums and All3DP troubleshooting guides

## Troubleshooting

### Kaggle: "API credentials not found"
- Ensure `~/.kaggle/kaggle.json` exists and has correct permissions
- Alternative: Set KAGGLE_USERNAME and KAGGLE_KEY environment variables

### Roboflow: "Invalid API key"
- Verify ROBOFLOW_API_KEY is set correctly
- Get fresh key from https://app.roboflow.com/settings/api

### "Out of disk space"
- Each dataset can be 500MB-2GB
- Ensure at least 5GB free space
- Use `--samples 10` for testing with smaller dataset

### Low validation accuracy
1. Review failed predictions in validation report
2. Check if images are correctly labeled
3. Update vision service system prompt
4. Add more examples to CSV knowledge base

## License Compliance

When using these datasets:

**Kaggle FDM Dataset (MIT)**:
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ No attribution required (but appreciated)

**Roboflow Datasets (CC BY 4.0)**:
- ✅ Commercial use allowed
- ✅ Modification allowed
- ⚠️ **Attribution required**

**Required Attribution**:
```
3D Printing Defects Dataset by [Author Name]
Licensed under CC BY 4.0
Source: [Roboflow Universe URL]
```

## Next Steps

1. ✅ Download datasets with script
2. ⬜ Create per-image metadata files
3. ⬜ Run initial validation baseline
4. ⬜ Analyze failed predictions
5. ⬜ Refine vision service prompts
6. ⬜ Re-run validation to measure improvement
7. ⬜ Document results and update CSV knowledge base

## References

- [Vision Validation Guide](../docs/VISION_VALIDATION_GUIDE.md)
- [VisionValidator API](../backend/app/services/validation/vision_validator.py)
- [Validation Script](../backend/scripts/validate_vision_model.py)
