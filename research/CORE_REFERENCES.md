# Core Research References

## Calculator Formulas
See `EXTRACTED_FORMULAS.md` for 16 Klipper calibration calculators:
- ✅ Extruder Rotation Distance (implemented)
- ✅ OrcaSlicer Flow Calibration (implemented)
- ❌ 14 remaining calculators (see full file)

## Technical Foundation
See `FDM 3D Printer Calibration and Slicer Report.md` for comprehensive coverage:
- Volumetric flow models (rectangular vs capsule approximation)
- Firmware kinematics (steps/mm, lead screw mechanics)
- Input shaping algorithms (ZV, MZV, EI shaper types)
- Pressure advance tuning
- Complete defect taxonomy (under-extrusion, warping, stringing, layer shifting, ringing, etc.)
- Material parameters (PLA, PETG, ABS temperature ranges and properties)
- Support generation algorithms

## Vision Training Datasets
See `image_datasets.md` for 16 Roboflow Universe datasets:
- 3D printing defects detection
- Layer separation, stringing, warping examples
- Cambridge Caxton dataset (6000+ labeled images)
- Kaggle 3D printing errors dataset

## Source Data
- `Klipper Calibrations.xlsx` - Original spreadsheet with calculator logic

## Research Papers (Markdown Versions)
- `jmmp-03-00064.md` - FDM process parameters systematic survey
- Paper PDFs are gitignored (large files)

---

**For Lean Refactor:** Focus on `EXTRACTED_FORMULAS.md` for calculator implementation. Vision datasets needed only if keeping AI features (contradicts lean refactor goal).
