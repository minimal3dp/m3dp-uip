# Archived Documentation

This directory contains documentation from previous project phases that conflicts with the current **lean refactor** direction (no AI/ML libraries, pure calculator logic).

## Files Archived

**Vision AI Documentation (conflicts with lean refactor):**
- `VISION_AI_TESTING_GUIDE.md` - Vision model testing procedures
- `VISION_API_INTEGRATION.md` - Gemini API integration guide
- `ACCURACY_IMPROVEMENT_GUIDE.md` - Vision model accuracy improvement (64% → 80% target)

**Phase-Specific Documentation (consolidated into TODO.md):**
- `PHASE4_INTEGRATION_TESTS.md` - Phase 4 testing documentation
- `PHASE_5_REVIEW_CHECKLIST.md` - Phase 5 deployment checklist
- `PHASE_5_SUMMARY.md` - Phase 5 completion summary
- `PYTHON_FRONTEND_COMPLETE.md` - Python frontend migration completion
- `PYTHON_FRONTEND_MIGRATION.md` - Vue → Python frontend migration guide
- `CLEANUP_SUMMARY.md` - Previous cleanup documentation

## Why Archived?

**Vision AI Docs:** The lean refactor removes all AI/ML dependencies (LangChain, OpenAI, Gemini, Vector DBs). These docs describe features being removed.

**Phase Docs:** Multiple conflicting phase numbering systems. All active work now tracked in root `TODO.md`.

## Restoration

If vision AI features are needed later, these docs provide the implementation reference. The backend code in `backend/app/services/vision_service.py` and validation datasets remain available.
