# Vision Model Accuracy Improvement Guide

## Current Status (Baseline)

**Validation Date:** November 28, 2025  
**Overall Accuracy:** 64.59%  
**Target Accuracy:** 80%+  
**Gap to Close:** +15.41 percentage points

### Per-Class Performance:
- ✅ **Stringing:** 81.70% (652/798) - Exceeds target
- ⚠️ **Spaghetti:** 62.52% (2,374/3,797) - Needs +17.48pp
- ❌ **Warping:** 44.71% (131/293) - Needs +35.29pp (CRITICAL)
- ❓ **Extrusion_Issue:** 0% (0/1,349) - No metadata (HIGH PRIORITY)

---

## Phase 1: Critical Fixes (Week 1)

### Step 1.1: Generate Metadata for Extrusion_Issue Class
**Time Estimate:** 2-3 hours  
**Priority:** HIGH  
**Impact:** Enable validation of 1,349 images

#### Actions:

1. **Create metadata generation script:**

```bash
cd /Users/wilsonm/development/m3dp-uip
```

Create `backend/scripts/generate_extrusion_metadata.py`:

```python
"""Generate metadata for merged Extrusion_Issue class."""
import json
from pathlib import Path
from datetime import datetime

def generate_metadata():
    """Generate metadata files for extrusion_issue images."""
    extrusion_dir = Path("backend/validation_data/extrusion_issue/images")
    
    if not extrusion_dir.exists():
        print(f"❌ Directory not found: {extrusion_dir}")
        return
    
    image_files = list(extrusion_dir.glob("*.jpg")) + list(extrusion_dir.glob("*.png"))
    print(f"Found {len(image_files)} images to process")
    
    for image_path in image_files:
        metadata_path = image_path.with_suffix("").with_suffix("") + "_metadata.json"
        
        # Skip if metadata already exists
        if metadata_path.exists():
            continue
        
        # Determine if under or over extrusion based on filename
        filename = image_path.name.lower()
        if "under" in filename:
            markers = ["under-extrusion", "gaps", "thin_walls"]
        elif "over" in filename:
            markers = ["over-extrusion", "bulging", "excess_material"]
        else:
            markers = ["extrusion_inconsistency"]
        
        metadata = {
            "expected_classification": "Extrusion_Issue",
            "visual_markers": markers,
            "source": "merged_from_legacy_classes",
            "created_at": datetime.now().isoformat(),
            "notes": "Automatically generated metadata for merged Extrusion_Issue class"
        }
        
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"✅ Created: {metadata_path.name}")
    
    print(f"\n✅ Metadata generation complete!")

if __name__ == "__main__":
    generate_metadata()
```

2. **Run the script:**

```bash
python3 backend/scripts/generate_extrusion_metadata.py
```

3. **Verify metadata creation:**

```bash
# Count metadata files
find backend/validation_data/extrusion_issue/images -name "*_metadata.json" | wc -l

# Should show ~1,349 files
```

4. **Run validation on Extrusion_Issue only:**

```bash
python3 -m backend.scripts.validate_vision_model --defect extrusion_issue
```

**Success Criteria:**
- ✅ 1,349 metadata files created
- ✅ Validation runs without errors
- ✅ Baseline accuracy established for Extrusion_Issue

---

### Step 1.2: Expand Warping Dataset
**Time Estimate:** 3-4 hours  
**Priority:** CRITICAL  
**Impact:** +500-1,000 images, potential +20-30pp accuracy

#### Actions:

1. **Search for Warping datasets on Roboflow Universe:**

Go to: https://universe.roboflow.com/

Search queries:
- "3D printing warping"
- "FDM bed adhesion failure"
- "3D print corner lifting"
- "warped 3D print"

2. **Download additional datasets:**

Target datasets with:
- ✅ High-quality images (>640px resolution)
- ✅ Verified labels
- ✅ Diverse bed materials (glass, PEI, textured)
- ✅ Various geometries (flat parts, corners)
- ✅ Different filament types (ABS, PLA, PETG)

3. **Download and extract:**

```bash
# Create temporary download directory
mkdir -p backend/validation_data/warping/downloads

# Download datasets (use Roboflow CLI or manual download)
# Example:
cd backend/validation_data/warping/downloads
# ... download files ...

# Extract and move to warping/images/
cd /Users/wilsonm/development/m3dp-uip
```

4. **Generate metadata for new images:**

Create `backend/scripts/generate_warping_metadata.py`:

```python
"""Generate metadata for new warping images."""
import json
from pathlib import Path
from datetime import datetime

def generate_warping_metadata():
    """Generate metadata files for new warping images."""
    warping_dir = Path("backend/validation_data/warping/images")
    
    image_files = list(warping_dir.glob("*.jpg")) + list(warping_dir.glob("*.png"))
    
    for image_path in image_files:
        metadata_path = image_path.with_suffix("").with_suffix("") + "_metadata.json"
        
        # Skip if metadata already exists
        if metadata_path.exists():
            continue
        
        metadata = {
            "expected_classification": "Warping",
            "visual_markers": [
                "corner_curl",
                "bed_separation",
                "first_layer_lift"
            ],
            "source": "roboflow_universe_expansion",
            "created_at": datetime.now().isoformat(),
            "notes": "Downloaded to expand warping dataset for improved accuracy"
        }
        
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"✅ Created: {metadata_path.name}")
    
    print(f"\n✅ Warping metadata generation complete!")

if __name__ == "__main__":
    generate_warping_metadata()
```

Run it:

```bash
python3 backend/scripts/generate_warping_metadata.py
```

5. **Validate new Warping images:**

```bash
python3 -m backend.scripts.validate_vision_model --defect warping
```

**Success Criteria:**
- ✅ 700-1,200 total Warping images (from 293)
- ✅ Metadata generated for all new images
- ✅ Initial accuracy >50%

---

### Step 1.3: Refine Warping Visual Discriminators
**Time Estimate:** 1-2 hours  
**Priority:** CRITICAL  
**Impact:** +10-15pp accuracy on Warping

#### Actions:

1. **Analyze current confusion patterns:**

```bash
# Extract Warping failures from validation report
python3 -c "
import json
with open('backend/reports/vision_validation_report.json', 'r') as f:
    report = json.load(f)
    
warping_failures = [
    p for p in report['failed_predictions'] 
    if p['expected_defect'] == 'Warping'
]

print(f'Total Warping failures: {len(warping_failures)}')
print('\nCommon misclassifications:')
confusion = {}
for fail in warping_failures:
    pred = fail['predicted_defect']
    confusion[pred] = confusion.get(pred, 0) + 1

for defect, count in sorted(confusion.items(), key=lambda x: x[1], reverse=True):
    print(f'  {defect}: {count}')
"
```

2. **Open the vision service file:**

```bash
code backend/app/services/vision_service.py
```

3. **Enhance the SYSTEM_PROMPT for Warping:**

Locate the Warping section in `SYSTEM_PROMPT` and update it:

```python
### 5. WARPING
**VISUAL MARKERS:**
- **Corner Lifting:** First layer corners curl upward away from bed
- **Edge Separation:** Part edges separate from build plate
- **Base Deformation:** Bottom surface is curved/bent instead of flat
- **Uneven First Layer:** First layer shows gaps or non-uniform adhesion

**KEY DISCRIMINATORS:**
- Warping vs. Layer_Separation:
  * Warping: Affects BOTTOM/BASE of print (bed adhesion failure)
  * Layer_Separation: Affects MIDDLE/TOP layers (vertical split/crack)
  
- Warping vs. Poor_Bridging:
  * Warping: Base/corners lift from bed, print tilted/curved
  * Poor_Bridging: Sagging between support points, rest of print normal

**DECISION RULE:**
If corners/edges lift from bed OR base is curved → Warping
If vertical split/crack in middle of print → Layer_Separation
If sagging between supports only → Poor_Bridging
```

4. **Save and test:**

```bash
# Quick test on a few Warping images
python3 -c "
import asyncio
from backend.app.services.vision_service import VisionService

async def test():
    service = VisionService()
    result = await service.analyze_print_defect(
        'backend/validation_data/warping/images/YOUR_TEST_IMAGE.jpg'
    )
    print(f'Classification: {result.defect_type}')
    print(f'Confidence: {result.confidence}')
    print(f'Analysis: {result.analysis_text}')

asyncio.run(test())
"
```

**Success Criteria:**
- ✅ Warping discriminators clearly distinguish from Layer_Separation and Poor_Bridging
- ✅ Test images correctly classified
- ✅ Confidence scores >0.7

---

## Phase 2: Spaghetti Improvements (Week 2)

### Step 2.1: Analyze Spaghetti Confusion Patterns
**Time Estimate:** 2 hours  
**Priority:** HIGH  
**Impact:** Identify root causes of 1,423 failures

#### Actions:

1. **Extract detailed failure analysis:**

Create `backend/scripts/analyze_spaghetti_failures.py`:

```python
"""Analyze Spaghetti classification failures."""
import json
from collections import Counter

def analyze_failures():
    with open('backend/reports/vision_validation_report.json', 'r') as f:
        report = json.load(f)
    
    spaghetti_failures = [
        p for p in report['failed_predictions']
        if p['expected_defect'] == 'Spaghetti'
    ]
    
    print(f"=== SPAGHETTI FAILURE ANALYSIS ===")
    print(f"Total failures: {len(spaghetti_failures)}")
    print(f"Total Spaghetti images: 3797")
    print(f"Failure rate: {len(spaghetti_failures)/3797*100:.1f}%\n")
    
    # Confusion breakdown
    confusion = Counter(p['predicted_defect'] for p in spaghetti_failures)
    print("Confused with:")
    for defect, count in confusion.most_common():
        pct = count/len(spaghetti_failures)*100
        print(f"  {defect}: {count} ({pct:.1f}%)")
    
    # Confidence analysis
    print("\nConfidence distribution in failures:")
    low_conf = sum(1 for p in spaghetti_failures if p['confidence'] < 0.7)
    mid_conf = sum(1 for p in spaghetti_failures if 0.7 <= p['confidence'] < 0.85)
    high_conf = sum(1 for p in spaghetti_failures if p['confidence'] >= 0.85)
    
    print(f"  Low (<0.7): {low_conf}")
    print(f"  Medium (0.7-0.85): {mid_conf}")
    print(f"  High (>0.85): {high_conf}")
    
    # Sample high-confidence failures
    print("\nHigh-confidence failures (should review):")
    high_conf_samples = [
        p for p in spaghetti_failures 
        if p['confidence'] >= 0.85
    ][:10]
    
    for fail in high_conf_samples:
        print(f"  {fail['image_path']}")
        print(f"    → Predicted: {fail['predicted_defect']} ({fail['confidence']:.2f})")

if __name__ == "__main__":
    analyze_failures()
```

Run it:

```bash
python3 backend/scripts/analyze_spaghetti_failures.py
```

2. **Manually review 10-20 high-confidence failures:**

```bash
# Open images in Finder
open backend/validation_data/spaghetti/images/
```

Look for patterns:
- Are images truly Spaghetti or mislabeled?
- What visual features caused confusion?
- Are there borderline cases (partial failures)?

**Success Criteria:**
- ✅ Identified top 3 confused classes
- ✅ Documented common visual patterns causing confusion
- ✅ Determined if dataset has labeling issues

---

### Step 2.2: Refine Spaghetti vs. Stringing Discriminators
**Time Estimate:** 1 hour  
**Priority:** HIGH  
**Impact:** +5-10pp accuracy on Spaghetti

#### Actions:

1. **Update SYSTEM_PROMPT in vision_service.py:**

```python
### 1. SPAGHETTI (Complete Print Failure)
**VISUAL MARKERS:**
- **No recognizable geometry:** Print has completely failed, no intended shape visible
- **Random filament pile:** Filament deposited in chaotic blob/pile
- **Nozzle dragging:** Evidence of nozzle dragging through failed material
- **No structural integrity:** No layers, no walls, just failed material

**KEY DISCRIMINATORS:**
- Spaghetti vs. Stringing:
  * Spaghetti: COMPLETE structural failure, no recognizable print shape AT ALL
  * Stringing: Print structure INTACT, just has thin threads between parts
  
- Spaghetti vs. Poor_Bridging:
  * Spaghetti: Entire print failed, blob of filament
  * Poor_Bridging: Print mostly successful, only bridging sections sagging

**CRITICAL DECISION RULE:**
Ask: "Can I see the intended print shape?"
- NO → Spaghetti (complete failure)
- YES, but with threads → Stringing
- YES, but with sag → Poor_Bridging
- YES, but with other issues → Check other defect types
```

2. **Add examples to prompt:**

```python
**EXAMPLES:**
- Spaghetti: Blob of filament on bed, no geometry, looks like pasta
- NOT Spaghetti: Print with lots of thin strings but shape is visible
- NOT Spaghetti: Print with sagging bridges but walls are intact
```

**Success Criteria:**
- ✅ Clear decision tree implemented
- ✅ Examples added to prompt
- ✅ Test cases pass

---

### Step 2.3: (Optional) Expand Spaghetti Dataset
**Time Estimate:** 3-4 hours  
**Priority:** MEDIUM  
**Impact:** +5-10pp accuracy if dataset quality is issue

#### Actions:

**Only do this if analysis shows:**
- Dataset has mislabeled images (>10% error rate)
- Lack of diversity in failure modes
- Need for more clear examples

1. **Search Roboflow for high-quality Spaghetti datasets:**

Search terms:
- "3D printing complete failure"
- "FDM spaghetti defect"
- "3D print blob"
- "failed 3D print"

2. **Download 300-500 additional images**

3. **Generate metadata using previous patterns**

4. **Re-validate**

**Success Criteria:**
- ✅ 4,000-4,500 total Spaghetti images
- ✅ Improved diversity in failure modes
- ✅ Accuracy >70%

---

## Phase 3: Fine-Tuning (Week 3)

### Step 3.1: Improve Stringing Discrimination
**Time Estimate:** 2 hours  
**Priority:** MEDIUM  
**Impact:** 81.70% → 85%+

#### Actions:

1. **Analyze Stringing failures:**

```bash
python3 -c "
import json
from collections import Counter

with open('backend/reports/vision_validation_report.json', 'r') as f:
    report = json.load(f)

stringing_failures = [
    p for p in report['failed_predictions']
    if p['expected_defect'] == 'Stringing'
]

confusion = Counter(p['predicted_defect'] for p in stringing_failures)
print('Stringing confused with:')
for defect, count in confusion.most_common():
    print(f'  {defect}: {count}')
"
```

2. **Enhance Stringing discriminators:**

```python
### 2. STRINGING
**VISUAL MARKERS:**
- **Thin filament threads:** Hair-like strings between separate parts
- **Vertical/diagonal wisps:** Threads hang in air, not part of structure
- **Clean main structure:** Print geometry itself is successful
- **Cobweb appearance:** Multiple thin threads create web-like pattern

**KEY DISCRIMINATORS:**
- Stringing vs. Poor_Bridging:
  * Stringing: VERTICAL/DIAGONAL threads in AIR between separate parts
  * Poor_Bridging: HORIZONTAL sagging BETWEEN two support points
  
- Stringing vs. Layer_Separation:
  * Stringing: Threads OUTSIDE/AROUND the main print body
  * Layer_Separation: Cracks/gaps WITHIN the print layers
  
- Stringing vs. Spaghetti:
  * Stringing: Print shape clearly visible, threads are addition
  * Spaghetti: No recognizable print shape, complete failure

**DECISION RULE:**
If thin threads BETWEEN parts + structure intact → Stringing
If horizontal SAG between supports → Poor_Bridging
If cracks WITHIN layers → Layer_Separation
```

**Success Criteria:**
- ✅ Stringing accuracy >85%
- ✅ Reduced confusion with Poor_Bridging and Layer_Separation

---

### Step 3.2: Implement Confidence Threshold Analysis
**Time Estimate:** 2-3 hours  
**Priority:** MEDIUM  
**Impact:** Identify low-confidence predictions for review

#### Actions:

1. **Create confidence analysis script:**

Create `backend/scripts/analyze_confidence.py`:

```python
"""Analyze validation results by confidence levels."""
import json

def analyze_confidence():
    with open('backend/reports/vision_validation_report.json', 'r') as f:
        report = json.load(f)
    
    # Combine all predictions (correct + failed)
    all_predictions = []
    
    # Add failed predictions
    all_predictions.extend(report['failed_predictions'])
    
    # Calculate accuracy by confidence bands
    bands = {
        '0.5-0.6': {'total': 0, 'correct': 0},
        '0.6-0.7': {'total': 0, 'correct': 0},
        '0.7-0.8': {'total': 0, 'correct': 0},
        '0.8-0.9': {'total': 0, 'correct': 0},
        '0.9-1.0': {'total': 0, 'correct': 0},
    }
    
    for pred in all_predictions:
        conf = pred['confidence']
        correct = pred['correct']
        
        if conf < 0.6:
            band = '0.5-0.6'
        elif conf < 0.7:
            band = '0.6-0.7'
        elif conf < 0.8:
            band = '0.7-0.8'
        elif conf < 0.9:
            band = '0.8-0.9'
        else:
            band = '0.9-1.0'
        
        bands[band]['total'] += 1
        if correct:
            bands[band]['correct'] += 1
    
    print("=== ACCURACY BY CONFIDENCE BAND ===")
    for band, stats in bands.items():
        if stats['total'] > 0:
            acc = stats['correct'] / stats['total'] * 100
            print(f"{band}: {acc:.1f}% ({stats['correct']}/{stats['total']})")
    
    # Low confidence predictions
    low_conf = [p for p in all_predictions if p['confidence'] < 0.7]
    print(f"\nLow confidence predictions (<0.7): {len(low_conf)}")
    print("Consider flagging these for human review")

if __name__ == "__main__":
    analyze_confidence()
```

Run it:

```bash
python3 backend/scripts/analyze_confidence.py
```

2. **Decide on confidence threshold policy:**

Options:
- **Flag for review:** Predictions <0.7 confidence
- **Auto-reject:** Predictions <0.6 confidence
- **High confidence:** Predictions >0.85 confidence

**Success Criteria:**
- ✅ Confidence analysis completed
- ✅ Policy documented
- ✅ Consider implementing confidence-based flagging in API

---

### Step 3.3: Generate Confusion Matrix
**Time Estimate:** 1-2 hours  
**Priority:** LOW  
**Impact:** Visual understanding of classification patterns

#### Actions:

1. **Create confusion matrix script:**

Create `backend/scripts/generate_confusion_matrix.py`:

```python
"""Generate confusion matrix from validation results."""
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def generate_confusion_matrix():
    with open('backend/reports/vision_validation_report.json', 'r') as f:
        report = json.load(f)
    
    # Get all defect types
    defect_types = [
        "Spaghetti",
        "Extrusion_Issue",
        "Stringing",
        "Layer_Shift",
        "Warping",
        "Ringing",
        "Poor_Bridging",
        "Layer_Separation"
    ]
    
    # Initialize confusion matrix
    n = len(defect_types)
    matrix = np.zeros((n, n))
    
    # Fill matrix from validation report
    # Note: Need to collect both correct and failed predictions
    
    # Plot
    plt.figure(figsize=(12, 10))
    sns.heatmap(
        matrix,
        annot=True,
        fmt='g',
        cmap='Blues',
        xticklabels=defect_types,
        yticklabels=defect_types
    )
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Vision Model Confusion Matrix')
    plt.tight_layout()
    
    # Save
    output_path = Path('backend/reports/confusion_matrix.png')
    plt.savefig(output_path, dpi=150)
    print(f"✅ Confusion matrix saved to: {output_path}")

if __name__ == "__main__":
    generate_confusion_matrix()
```

**Success Criteria:**
- ✅ Confusion matrix generated
- ✅ Asymmetric confusions identified
- ✅ Insights documented

---

## Phase 4: Full Re-Validation (End of Week 3)

### Step 4.1: Run Complete Validation
**Time Estimate:** 12-15 hours (overnight)  
**Priority:** HIGH

#### Actions:

```bash
# Full validation with verbose logging
python3 -m backend.scripts.validate_vision_model --verbose > validation_final.log 2>&1 &

# Track progress
tail -f validation_final.log
```

**Success Criteria:**
- ✅ All defect types validated
- ✅ No errors or crashes
- ✅ Report generated

---

### Step 4.2: Calculate Improvement & Document Results
**Time Estimate:** 1 hour

#### Actions:

1. **Compare before/after results:**

Create `backend/scripts/compare_results.py`:

```python
"""Compare validation results before and after improvements."""
import json
from datetime import datetime

def compare_results():
    # Load baseline (from conversation summary)
    baseline = {
        "date": "2025-11-28",
        "overall": 64.59,
        "by_class": {
            "Stringing": 81.70,
            "Spaghetti": 62.52,
            "Warping": 44.71,
            "Extrusion_Issue": 0.0
        }
    }
    
    # Load current
    with open('backend/reports/vision_validation_report.json', 'r') as f:
        current = json.load(f)
    
    print("=== ACCURACY IMPROVEMENT REPORT ===")
    print(f"Baseline: {baseline['date']}")
    print(f"Current: {datetime.now().strftime('%Y-%m-%d')}\n")
    
    print(f"Overall Accuracy:")
    print(f"  Before: {baseline['overall']:.2f}%")
    print(f"  After:  {current['accuracy']*100:.2f}%")
    improvement = (current['accuracy']*100) - baseline['overall']
    print(f"  Change: {improvement:+.2f}pp\n")
    
    print("Per-Class Accuracy:")
    for defect, stats in current['by_defect_type'].items():
        before = baseline['by_class'].get(defect, 0)
        after = stats['accuracy'] * 100
        change = after - before
        status = "✅" if after >= 80 else "⚠️" if after >= 70 else "❌"
        print(f"  {status} {defect}:")
        print(f"      Before: {before:.2f}%")
        print(f"      After:  {after:.2f}%")
        print(f"      Change: {change:+.2f}pp")

if __name__ == "__main__":
    compare_results()
```

Run it:

```bash
python3 backend/scripts/compare_results.py
```

2. **Document insights:**

Create summary in `backend/reports/improvement_summary.md`

**Success Criteria:**
- ✅ Overall accuracy ≥75% (stretch: 80%)
- ✅ Warping accuracy ≥60% (stretch: 70%)
- ✅ Spaghetti accuracy ≥70% (stretch: 75%)
- ✅ Extrusion_Issue accuracy ≥60%
- ✅ Stringing maintained ≥80%

---

## Expected Timeline & Outcomes

| Phase | Duration | Key Deliverables | Expected Impact |
|-------|----------|------------------|-----------------|
| **Phase 1** | Week 1 (15-20h) | Extrusion metadata, Warping expansion, prompt refinements | +15-20pp overall |
| **Phase 2** | Week 2 (10-15h) | Spaghetti analysis & improvements | +5-10pp overall |
| **Phase 3** | Week 3 (8-12h) | Stringing tuning, confidence analysis, confusion matrix | +3-5pp overall |
| **Phase 4** | End Week 3 (15h) | Full validation & documentation | Baseline established |

**Total Time Investment:** 50-60 hours  
**Target Overall Accuracy:** 75-80%  
**Target Per-Class Minimum:** 70%

---

## Troubleshooting

### Issue: Metadata generation fails
**Solution:**
```bash
# Check directory structure
ls -la backend/validation_data/extrusion_issue/images/

# Verify Python environment
python3 --version
which python3

# Run with verbose errors
python3 -u backend/scripts/generate_extrusion_metadata.py
```

### Issue: Validation takes too long
**Solution:**
```bash
# Validate one defect at a time
python3 -m backend.scripts.validate_vision_model --defect warping

# Run in background
nohup python3 -m backend.scripts.validate_vision_model &
```

### Issue: Download quota exceeded (Roboflow)
**Solution:**
- Use multiple Roboflow accounts
- Download smaller batches over multiple days
- Consider alternative sources (Kaggle, GitHub)

### Issue: Accuracy not improving
**Solution:**
1. Review confusion matrix to identify systematic issues
2. Manually review 50-100 failed predictions
3. Check if dataset has labeling errors
4. Consider adjusting Gemini model parameters (temperature, top_p)
5. Try different prompt structures

---

## Next Steps After 80% Accuracy

Once you reach 80% overall accuracy:

1. **Implement confidence-based flagging** in production API
2. **Add human-in-the-loop review** for low-confidence predictions
3. **Monitor production accuracy** with user feedback
4. **Expand to remaining defect classes** (Layer_Shift, Ringing, Poor_Bridging, Layer_Separation)
5. **Consider fine-tuning** a custom vision model if Gemini limitations persist
6. **Implement A/B testing** for prompt variations
7. **Add visual marker extraction** to metadata for explainability

---

## Progress Tracking Checklist

### Phase 1: Critical Fixes
- [ ] Generated metadata for Extrusion_Issue (1,349 files)
- [ ] Validated Extrusion_Issue baseline
- [ ] Downloaded 500+ additional Warping images
- [ ] Generated metadata for new Warping images
- [ ] Updated Warping discriminators in SYSTEM_PROMPT
- [ ] Validated Warping with expanded dataset
- [ ] Warping accuracy >60%

### Phase 2: Spaghetti Improvements
- [ ] Analyzed Spaghetti failure patterns
- [ ] Identified top confused classes
- [ ] Updated Spaghetti vs. Stringing discriminators
- [ ] Added examples to SYSTEM_PROMPT
- [ ] (Optional) Downloaded additional Spaghetti images
- [ ] Validated Spaghetti improvements
- [ ] Spaghetti accuracy >70%

### Phase 3: Fine-Tuning
- [ ] Enhanced Stringing discriminators
- [ ] Implemented confidence threshold analysis
- [ ] Generated confusion matrix
- [ ] Documented confidence policy
- [ ] Stringing accuracy >85%

### Phase 4: Final Validation
- [ ] Ran complete validation on all classes
- [ ] Generated comparison report
- [ ] Overall accuracy ≥75%
- [ ] All classes ≥60% (stretch: 70%)
- [ ] Documented insights and next steps

---

## Contact & Support

**Questions or Issues?**
- Check validation logs: `backend/reports/`
- Review error messages in terminal output
- Verify Python environment: `python3 --version`
- Check Gemini API quota: Google AI Studio dashboard

**Script Locations:**
- Validation: `backend/scripts/validate_vision_model.py`
- Vision Service: `backend/app/services/vision_service.py`
- Validator: `backend/app/services/validation/vision_validator.py`
- Reports: `backend/reports/vision_validation_report.json`

---

## Summary

This guide provides a structured, step-by-step approach to improve your vision model accuracy from 64.59% to 75-80%+ over 3 weeks. Focus on:

1. **Week 1:** Fix critical gaps (Extrusion metadata, Warping expansion)
2. **Week 2:** Improve largest class (Spaghetti refinements)
3. **Week 3:** Fine-tune and validate (Stringing, confidence, full validation)

Each step includes specific commands, expected outcomes, and success criteria. Follow the checklist to track progress, and adjust priorities based on your validation results.

Good luck! 🚀
