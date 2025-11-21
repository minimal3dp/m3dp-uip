# Copilot Instructions for M3DP-UIP

## Project Overview

**Minimal 3DP Unified Intelligence Platform (M3DP-UIP)** is an AI-powered diagnostic platform for 3D printing that uses vision models and structured knowledge bases to troubleshoot print failures. The project combines:

- **Frontend prototype**: `index.html` - A Tailwind CSS + vanilla JS interactive diagnostic wizard
- **Backend (planned)**: FastAPI with RAG (Retrieval Augmented Generation) architecture
- **Knowledge Base**: CSV data containing Klipper calibrations and OrcaSlicer settings
- **Vision AI**: Gemini 1.5 Pro for analyzing print failure photos

This is part of the **minimal3dp.com** ecosystem (5K+ YouTube subscribers, multiple tools deployed).

## Architecture & Design Philosophy

### The "Router" Pattern
The core architectural decision is to **avoid context window pollution**. Instead of feeding all CSV knowledge at once:

1. **Router classifies** issue type: `Mechanical` (Klipper) | `Slicer` (OrcaSlicer) | `Material` (Filament)
2. **Retrieval fetches** only relevant CSV data (e.g., `Klipper Calibrations - Pressure Advance.csv`)
3. **Calculator renders** precise Python formula-based solutions (not generic LLM advice)

### Tech Stack (Current + Planned)

**Frontend Prototype** (`index.html`):
- Tailwind CSS 3.x (CDN) + Lucide icons
- Vanilla JavaScript (no build step - intentional for prototyping)
- Glass morphism UI (`backdrop-filter: blur(10px)`)
- Implements rotation distance calculator from Klipper CSV

**Planned Backend** (not yet implemented):
- **FastAPI** (Python 3.11+) - See `README.md` scaffold
- **PostgreSQL** for session storage
- **pandas** for CSV math operations
- **google-generativeai** for vision analysis
- **Firestore** for user printer profiles

**Deployment Target**: Vercel (all minimal3dp.com tools use this)

## Key Files & Their Roles

- `index.html` - Working prototype wizard with calculator logic
- `main.py` - Placeholder entry point (just prints "Hello")
- `pyproject.toml` - Python 3.12+ project, no dependencies yet
- `README.md` - Contains full architecture plan and TODO phases
- `guide/MINIMAL3DP_APP_GUIDE.md` - **2156-line comprehensive deployment/SEO/branding guide** (read this for minimal3dp.com conventions)
- `guide/Minimal 3DP Development Strategy Report.md` - Technical architecture deep-dive

## Development Workflows

### Running the Frontend Prototype
```bash
# No build step needed - open in browser
open index.html  # or use Live Server extension
```

The calculator implements this formula from CSV:
```javascript
// Formula: New Rotation Distance = (current * actual) / requested
const newRotDist = (currentRotDist * actual) / requested;
```

### Python Environment Setup
```bash
# Project uses Python 3.12+ (see .python-version)
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
```

**Note**: Backend not yet implemented. See `README.md` Phase 2 for FastAPI scaffold plan.

## Project-Specific Conventions

### 1. CSV-Driven Logic
All calculators must be **direct translations of spreadsheet formulas**, not LLM hallucinations. Example from `index.html`:

```javascript
// This mirrors "Klipper Calibrations - Extruder Rotation Distance.csv"
// Row 18-22: Measure and Trim logic
const newRotDist = (currentRotDist * actual) / requested;
```

When implementing new calculators:
1. Find the CSV formula in `guide/` docs
2. Port formula exactly to Python/JavaScript
3. Add inline comments referencing CSV row numbers

### 2. Minimal3DP Brand Standards
This project is part of the minimal3dp.com ecosystem. Follow conventions from `guide/MINIMAL3DP_APP_GUIDE.md`:

- **Amazon Affiliate Tag**: Always use `mwf064-20`
- **YouTube Channel**: `UCM_8Mv-0S1LnnJpRJLjahaw` - link in all tools
- **Color Palette**: Orange (#F97316) for brand, zinc-900 for backgrounds
- **Deployment**: Vercel with subdomain pattern (e.g., `settings.minimal3dp.com`)
- **SEO**: Include Schema.org markup, OG images (1200x630px), FAQ sections

### 3. UI/UX Patterns
From the `index.html` prototype:

```javascript
// Always show loading state during async operations
btn.innerHTML = '<i data-lucide="loader-2" class="animate-spin"></i> Analyzing...';

// Auto-scroll to results after generation
document.getElementById('analysis-result').scrollIntoView({ behavior: 'smooth' });

// Visual feedback for calculations (green flash)
resultEl.classList.add('text-green-400');
setTimeout(() => resultEl.classList.remove('text-green-400'), 500);
```

### 4. Data Validation
The current prototype shows validation pattern:

```javascript
if (!actual) {
    alert("Please enter the Actual Extruded Distance measured.");
    return;
}
```

**For FastAPI**: Use Pydantic models with validators (see `README.md` structure).

## Critical Technical Details

### Vision API Integration (Planned)
System prompt for Gemini 1.5 Pro (from `README.md`):
> "You are an expert 3D printing diagnostician. Analyze this image for defects. Return a JSON object classifying the error type (e.g., VFA, Under-extrusion, Layer Shift)."

Response must be structured JSON for the router to process.

### Calculator Component Pattern
Each CSV becomes a calculator. From `index.html`:

1. **Input Section**: User enters measurements
2. **Formula Application**: Python/JS calculates new values
3. **Config Output**: Show Klipper/OrcaSlicer config snippet
4. **Copy Button**: Allow one-click copy to clipboard

Example output format:
```
rotation_distance: 20.313
```

### CSV Knowledge Base Location (Planned)
```
backend/app/data/
├── klipper_calibrations/
│   ├── extruder_rotation_distance.csv
│   ├── pressure_advance.csv
│   └── input_shaping.csv
└── orca_recommendations/
    └── material_profiles.csv
```

## Common Tasks

### Adding a New Calculator
1. Locate the CSV formula in `guide/` documentation
2. Add UI form in `index.html` or create new component
3. Implement formula in JavaScript (prototype) or Python (backend)
4. Add GA4 tracking event: `gtag('event', 'calculator_use', {...})`
5. Update navigation links

### Implementing FastAPI Backend
Follow scaffold in `README.md`:

```python
# backend/app/api/endpoints/diagnosis.py
@router.post("/analyze")
async def analyze_image(file: UploadFile):
    # 1. Call Gemini Vision API
    # 2. Route to appropriate CSV loader
    # 3. Return recommendations + calculator params
    pass
```

### Updating Brand Assets
- **Affiliate links**: Use Amazon tag `mwf064-20`
- **YouTube embeds**: Link to channel for subscribers
- **OG images**: 1200x630px PNG, <300KB (use Canva)
- **GA4**: Measurement ID `G-VQ8RPWC2MK` (from main site)

## Environment Variables (Future)
From `guide/MINIMAL3DP_APP_GUIDE.md`:

```bash
# .env (not created yet)
PAAPI_ACCESS_KEY=<Amazon Product API>
PAAPI_SECRET_KEY=<Amazon Product API>
PAAPI_ASSOCIATE_TAG=mwf064-20
GOOGLE_GENAI_API_KEY=<Gemini API>
GA4_MEASUREMENT_ID=G-VQ8RPWC2MK
```

## Testing Patterns
No test suite yet. When implementing:

- **Manual testing checklist**: Every button, every input, mobile + desktop
- **Error scenarios**: API failures, no internet, invalid inputs
- **Validation**: Client-side AND server-side
- **Browser testing**: Chrome, Safari, Firefox, Edge

## External Dependencies & Integration Points

### APIs (Planned)
- **Gemini 1.5 Pro**: Vision analysis (`google-generativeai` library)
- **Amazon PA-API**: Product recommendations (Phase 2 - optional)
- **Google Analytics 4**: User behavior tracking
- **YouTube Data API**: Content strategy (see `guide/MINIMAL3DP_APP_GUIDE.md`)

### Main Site Integration
All tools cross-link to:
- `https://minimal3dp.com` (main site)
- `https://minimal3dp.com/tools` (calculator suite)
- `https://youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw`

## Documentation Location
- **Architecture decisions**: `README.md` + `guide/Minimal 3DP Development Strategy Report.md`
- **Deployment guide**: `guide/MINIMAL3DP_APP_GUIDE.md` (comprehensive 2156 lines)
- **Brand guidelines**: `guide/Minimal 3DP_ A Comprehensive Brand Specification...md`
- **This is a design/planning phase**: Backend not yet implemented

## What NOT to Do
- ❌ Don't generate generic LLM advice - use CSV formulas
- ❌ Don't feed all CSVs at once - use router pattern
- ❌ Don't use different affiliate tags - always `mwf064-20`
- ❌ Don't ignore mobile responsiveness - prototype already has it
- ❌ Don't skip GA4 tracking - all user actions should be tracked
- ❌ Don't create standalone components without minimal3dp.com branding

## Development Environment

### UV-Based Python Environment
All Python development must occur in the **UV-based Python environment**:

```bash
# Activate UV environment
source .venv/bin/activate

# Install dependencies with UV (when backend is implemented)
uv pip install -r requirements.txt

# Run Python scripts
uv run python main.py
```

**Why UV?** UV provides:
- Faster dependency resolution than pip
- Reproducible builds
- Better virtual environment management
- Compatible with existing Python tooling

## Prompt Efficiency & Cost-Awareness

### Goal
Help minimize heavy or expensive model calls and reduce token usage while preserving result quality.

### When to Flag High-Cost Prompts
Copilot should heuristically detect and flag prompts that request:

1. **Complete dumps of large files or entire datasets**
   - ❌ "Show me all 10,000 rows of this CSV"
   - ✅ "Show me the first 10 rows and schema of this CSV"

2. **Extremely long code reviews** (>2,000 lines) or multi-file refactors in one prompt
   - ❌ "Review and refactor all files in `backend/app/`"
   - ✅ "Review `backend/app/api/endpoints/diagnosis.py` for optimization opportunities"

3. **Requests for full dataset transformations** on millions of rows without a sample
   - ❌ "Process 1M rows and return the full CSV"
   - ✅ "Process a 100-row sample and provide the transformation code I can run locally"

4. **Output of enormous binary blobs or large base64 content**
   - ❌ "Generate and encode a 10MB test image"
   - ✅ "Show me the code to generate a test image, I'll run it locally"

### Actionable Behavior
When Copilot detects expensive prompts, it should:

1. **Politely notify the user** that the prompt appears expensive and explain why
2. **Suggest concrete, lower-cost alternatives**:
   - Split the task into steps
   - Provide a small sample first
   - Request a small proof-of-concept
   - Ask to confirm before proceeding
3. **Include a succinct example** of a more efficient prompt the user can copy/paste

### Example Response Pattern

**User asks:** "Process all 1M CSV rows and return the full transformed dataset"

**Copilot response:**
> ⚠️ **Cost Alert**: Processing and returning 1M rows would consume significant tokens (~$5-10 in API costs).
>
> **Suggested approach:**
> 1. Let me process a **100-row sample** and verify the logic
> 2. I'll provide the complete transformation **code** you can run locally
> 3. The code will write results to a CSV file instead of returning them
>
> **More efficient prompt:**
> ```
> Process the first 100 rows of this CSV and provide the transformation code
> I can run locally on the full dataset. Write output to transformed_output.csv
> ```
>
> Would you like me to proceed with the sample approach?

### Prompt Compression Techniques

Based on [Microsoft's LLMLingua methodology](https://www.freecodecamp.org/news/how-to-compress-your-prompts-and-reduce-llm-costs/), consider these optimization strategies:

1. **Remove redundant context**
   - Don't repeat information already in conversation history
   - Reference prior messages: "As mentioned in my previous response..."

2. **Use structured compression**
   - Preserve critical sections (code, formulas, CSV headers)
   - Compress verbose explanations
   - Example: Keep CSV row 18-22 formula comments, compress surrounding text

3. **Leverage file references instead of full content**
   - ❌ "Here's the full 500-line file: [paste entire file]"
   - ✅ "See `index.html` lines 150-180 for the calculator logic"

4. **Request targeted sections**
   - ❌ "Analyze the entire codebase"
   - ✅ "Analyze the router pattern in `README.md` section 1"

5. **Use code snippets over full files**
   - Show only relevant functions/classes
   - Reference line numbers for context
   - Example: "The rotation distance calculation (lines 234-241) uses..."

6. **Batch related questions**
   - Instead of 5 separate prompts, combine into one structured request
   - Use numbered lists for multiple questions
   - Copilot can process multiple related tasks more efficiently

### Integration with This Project

For M3DP-UIP specifically:

- **CSV Processing**: Always request samples first (10-100 rows), never full datasets
- **Calculator Formulas**: Reference CSV row numbers, don't paste entire spreadsheets
- **Vision API Testing**: Use small test images (<500KB), not full-resolution photos
- **Code Reviews**: Target specific files/functions, not entire directories
- **Documentation**: Reference sections by heading, don't copy entire guide files

## Questions to Ask
- Which CSV formula am I implementing? (Reference row numbers)
- Does this need vision API or just calculator logic?
- Is this part of the router (classification) or retrieval (specific CSV)?
- Where should GA4 tracking be added?
- Does this follow the glass morphism UI pattern from `index.html`?
- **Is this prompt requesting large data dumps that could be optimized?**
- **Can this task be split into smaller, cost-effective steps?**
