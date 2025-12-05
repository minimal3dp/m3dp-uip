# M3DP-UIP Calculator Guide

## Overview

This guide explains how to add new calculators to M3DP-UIP. All calculators are formula-driven, sourced from CSV data and Klipper documentation.

## Current Status

**Implemented:** 10/16 (62.5%)
**Remaining:** 6/16 (37.5%)

### Implemented Calculators

1. ✅ Extruder Rotation Distance
2. ✅ OrcaSlicer Flow Calibration (Two-Pass)
3. ✅ OrcaSlicer Flow YOLO (Single-Pass)
4. ✅ Run Current (TMC2208/2209)
5. ✅ Pressure Advance
6. ✅ Input Shaping
7. ✅ X and Y Offsets
8. ✅ Max Volumetric Speed
9. ✅ Lead Screw Rotation Distance
10. ✅ Line Widths (OrcaSlicer)

### Remaining Calculators

11. ⏳ Skew Correction - XY/XZ/YZ skew commands
12. ⏳ Flow Calibration (Traditional) - Wall thickness method
13. ⏳ PA & OrcaSlicer - Alternative pressure advance
14. ⏳ Ellis Max Volumetric Speed - Manual extrusion method
15. ⏳ Extrusion Rate Smoothing (ERS) - Advanced OrcaSlicer
16. ⏳ Adaptive Pressure Advance - Matrix-based PA tuning

---

## Calculator Architecture

Each calculator consists of:

1. **CSV Data File** - Calibration parameters and metadata
2. **Pydantic Model** - Request/response validation
3. **Endpoint Function** - API logic and calculation
4. **HTML Template** - User interface form and results display
5. **Unit Tests** - Formula validation and edge cases

### File Locations

```
backend/
├── app/
│   ├── api/endpoints/calculators.py     # All endpoints (2845 lines)
│   ├── models/csv_schemas.py            # Pydantic models
│   ├── data/klipper_calibrations/
│   │   └── {name}.csv                   # CSV data
│   └── templates/
│       └── calculator_{name}.html       # UI template
├── tests/
│   └── test_calculators.py              # Unit tests
└── services/
    └── csv_loader.py                    # CSV loading
```

---

## Step-by-Step: Adding a Calculator

### Step 1: Create CSV Data File

**File:** `backend/app/data/klipper_calibrations/{name}.csv`

Example: `flow_calibration_traditional.csv`

```csv
parameter,value,unit,description,formula,notes
wall_thickness,3,mm,Measured wall thickness,new_flow = old_flow * (desired / measured),Use 3 walls minimum
measurement_tool,calipers,text,Tool for measurement,Not used in calculation,Digital caliper recommended
nozzle_diameter,0.4,mm,Nozzle size,new_flow = old_flow * (0.4 / nozzle),Affects wall thickness
first_layer_height,0.2,mm,First layer height,Not used,Must match print settings
```

**CSV Format Requirements:**
- Columns: `parameter`, `value`, `unit`, `description`, `formula`, `notes`
- First row is header
- One row per parameter
- Enclose text with commas in quotes
- No trailing commas or empty rows

### Step 2: Create Pydantic Models

**File:** `backend/app/api/endpoints/calculators.py`

Add request and response models:

```python
class FlowCalibrationTraditionalRequest(BaseModel):
    """Request for traditional flow calibration."""
    
    old_flow_rate: float = Field(
        1.0,
        gt=0,
        le=2,
        description="Current flow rate from slicer (1.0 = 100%)",
        examples=[0.95]
    )
    measured_wall_thickness: float = Field(
        ...,
        gt=0,
        le=10,
        description="Measured wall thickness from print (mm)",
        examples=[3.0]
    )
    desired_wall_thickness: float = Field(
        3.0,
        gt=0,
        le=10,
        description="Target wall thickness (mm)",
        examples=[3.0]
    )


class FlowCalibrationTraditionalResponse(BaseModel):
    """Response with flow calibration result."""
    
    new_flow_rate: float = Field(..., description="Calculated flow rate")
    change_percent: float = Field(..., description="Percentage change")
    adjustment: str = Field(..., description="OrcaSlicer adjustment value")
    test_parameters: dict = Field(..., description="Recommended test print settings")
    recommendation: str = Field(..., description="Action recommendation")
```

**Field Validation Rules:**
- `gt` - Greater than (exclusive)
- `ge` - Greater than or equal (inclusive)
- `lt` - Less than (exclusive)
- `le` - Less than or equal (inclusive)
- `Field(...)` - Required field
- `Field(default_value)` - Optional field with default
- `examples` - Example values for documentation

### Step 3: Implement Calculation Logic

In `backend/app/api/endpoints/calculators.py`, add the endpoint function:

```python
@router.post(
    "/flow-calibration-traditional",
    response_model=FlowCalibrationTraditionalResponse,
    tags=["Flow Calibration"],
    summary="Flow Calibration (Traditional - Wall Thickness Method)",
    description="Calculate flow rate adjustment using wall thickness measurement"
)
async def flow_calibration_traditional(
    request: FlowCalibrationTraditionalRequest
) -> FlowCalibrationTraditionalResponse:
    """
    Calculate flow rate adjustment using traditional wall thickness method.
    
    Formula:
        new_flow = old_flow × (desired_thickness / measured_thickness)
        change_percent = ((new_flow - old_flow) / old_flow) × 100
    """
    try:
        # Calculation
        new_flow_rate = request.old_flow_rate * (
            request.desired_wall_thickness / request.measured_wall_thickness
        )
        
        # Change percentage
        change_percent = (
            (new_flow_rate - request.old_flow_rate) / request.old_flow_rate * 100
        )
        
        # Adjustment value for OrcaSlicer
        adjustment = f"{new_flow_rate:.2%}"
        
        # Test parameters
        test_parameters = {
            "first_layer": request.old_flow_rate,
            "perimeter_speed": 25,
            "infill_speed": 50,
            "wall_thickness": request.desired_wall_thickness,
            "num_walls": 3
        }
        
        # Recommendation
        if abs(change_percent) <= 5:
            recommendation = "Change is acceptable. Update OrcaSlicer and print test."
        elif change_percent > 5:
            recommendation = "Change exceeds 5%. Verify measurement and re-measure."
        else:
            recommendation = "Large decrease. Check for over-extrusion on previous print."
        
        # Track usage
        track_calculator_use("flow_calibration_traditional")
        
        return FlowCalibrationTraditionalResponse(
            new_flow_rate=round(new_flow_rate, 4),
            change_percent=round(change_percent, 2),
            adjustment=adjustment,
            test_parameters=test_parameters,
            recommendation=recommendation
        )
    
    except ZeroDivisionError:
        raise HTTPException(
            status_code=400,
            detail="Measured wall thickness cannot be 0"
        )
    except Exception as e:
        logger.error(f"Flow calibration error: {e}")
        raise HTTPException(status_code=500, detail="Calculation failed")
```

**Pattern to Follow:**
1. Extract and validate inputs
2. Perform calculation
3. Format results
4. Generate recommendation
5. Track usage (GA4)
6. Return response
7. Handle errors gracefully

### Step 4: Create HTML Template

**File:** `backend/app/templates/calculator_flow_calibration_traditional.html`

```html
{% extends "base.html" %}

{% block title %}Flow Calibration (Traditional) - M3DP-UIP{% endblock %}

{% block content %}
<div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold mb-2">Flow Calibration (Traditional)</h1>
    <p class="text-zinc-400 mb-8">Calculate flow rate using wall thickness measurement</p>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <!-- Form -->
        <div class="bg-slate-800 rounded-lg p-6">
            <h2 class="text-2xl font-semibold mb-6">Calibration Data</h2>
            
            <form hx-post="/api/v1/calculators/flow-calibration-traditional"
                  hx-target="#result"
                  hx-swap="innerHTML"
                  class="space-y-6">
                
                <!-- Old Flow Rate -->
                <div>
                    <label for="old_flow" class="block text-sm font-medium mb-2">
                        Current Flow Rate (%)
                    </label>
                    <input type="number" 
                           id="old_flow"
                           name="old_flow_rate"
                           step="0.01" 
                           min="0.5" 
                           max="2" 
                           value="1.0"
                           class="w-full px-4 py-2 bg-slate-700 border border-slate-600 rounded text-white"
                           required>
                    <p class="text-xs text-zinc-400 mt-1">Current value from OrcaSlicer</p>
                </div>

                <!-- Measured Wall Thickness -->
                <div>
                    <label for="measured_wall" class="block text-sm font-medium mb-2">
                        Measured Wall Thickness (mm)
                    </label>
                    <input type="number" 
                           id="measured_wall"
                           name="measured_wall_thickness"
                           step="0.1" 
                           min="0.1" 
                           max="10" 
                           placeholder="3.0"
                           class="w-full px-4 py-2 bg-slate-700 border border-slate-600 rounded text-white"
                           required>
                    <p class="text-xs text-zinc-400 mt-1">Measure with digital caliper</p>
                </div>

                <!-- Desired Wall Thickness -->
                <div>
                    <label for="desired_wall" class="block text-sm font-medium mb-2">
                        Desired Wall Thickness (mm)
                    </label>
                    <input type="number" 
                           id="desired_wall"
                           name="desired_wall_thickness"
                           step="0.1" 
                           min="0.1" 
                           max="10" 
                           value="3.0"
                           class="w-full px-4 py-2 bg-slate-700 border border-slate-600 rounded text-white"
                           required>
                    <p class="text-xs text-zinc-400 mt-1">Usually 3.0mm for 0.4 nozzle</p>
                </div>

                <!-- Submit Button -->
                <button type="submit" 
                        class="w-full bg-brand-orange hover:bg-amber-600 text-white font-bold py-3 rounded-lg transition">
                    Calculate Flow Rate
                </button>
            </form>

            <!-- Information Box -->
            <div class="mt-8 bg-blue-500/10 border border-blue-500/50 rounded-lg p-4">
                <h3 class="font-semibold mb-2">📊 How It Works</h3>
                <p class="text-sm text-zinc-300">
                    Measure the wall thickness of a 3-wall test print. The calculator adjusts 
                    your flow rate to match the desired thickness.
                </p>
                <p class="text-sm text-zinc-300 mt-2">
                    Formula: <code class="bg-slate-700 px-2 py-1 rounded">
                        new_flow = old_flow × (desired / measured)
                    </code>
                </p>
            </div>
        </div>

        <!-- Results -->
        <div id="result" class="lg:col-span-1">
            <div class="bg-slate-800 rounded-lg p-6 h-full">
                <p class="text-zinc-400">Results will appear here...</p>
            </div>
        </div>
    </div>
</div>

<!-- Result Template (returned by HTMX) -->
<template id="result-template">
    <div class="bg-slate-800 rounded-lg p-6">
        <h2 class="text-2xl font-semibold mb-6">Results</h2>
        
        <!-- Main Result -->
        <div class="bg-brand-orange/20 border border-brand-orange rounded-lg p-4 mb-6">
            <p class="text-zinc-400 text-sm">New Flow Rate</p>
            <p class="text-4xl font-bold text-brand-orange" id="new-flow"></p>
            <p class="text-sm text-zinc-400 mt-2">
                Change: <span id="change-percent"></span>
            </p>
        </div>

        <!-- OrcaSlicer Value -->
        <div class="bg-slate-700 rounded-lg p-4 mb-6">
            <p class="text-sm text-zinc-400 mb-2">OrcaSlicer Adjustment</p>
            <code class="text-lg font-mono text-brand-orange" id="adjustment"></code>
            <button class="mt-2 text-sm px-3 py-1 bg-slate-600 hover:bg-slate-500 rounded"
                    onclick="copyToClipboard(this)">
                Copy to Clipboard
            </button>
        </div>

        <!-- Test Parameters -->
        <div class="mb-6">
            <h3 class="font-semibold mb-3">Test Print Settings</h3>
            <div class="space-y-2 text-sm">
                <p><span class="text-zinc-400">First Layer:</span> <span id="first-layer"></span></p>
                <p><span class="text-zinc-400">Perimeter Speed:</span> <span id="perim-speed"></span> mm/s</p>
                <p><span class="text-zinc-400">Infill Speed:</span> <span id="infill-speed"></span> mm/s</p>
                <p><span class="text-zinc-400">Wall Thickness:</span> <span id="wall-thick"></span> mm</p>
            </div>
        </div>

        <!-- Recommendation -->
        <div class="bg-green-500/20 border border-green-500/50 rounded-lg p-4">
            <p class="text-sm" id="recommendation"></p>
        </div>
    </div>
</template>

<script>
function copyToClipboard(button) {
    const text = button.previousElementSibling.textContent;
    navigator.clipboard.writeText(text).then(() => {
        const original = button.textContent;
        button.textContent = '✓ Copied!';
        setTimeout(() => button.textContent = original, 2000);
    });
}
</script>
{% endblock %}
```

**Template Structure:**
1. Form section (left column on desktop)
2. Results section (right column on desktop, hidden until calculation)
3. Information/help box
4. Responsive design (mobile-first)
5. HTMX integration for form submission
6. Copy-to-clipboard functionality

### Step 5: Write Unit Tests

**File:** `backend/tests/test_calculators.py`

Add tests for the new calculator:

```python
def test_flow_calibration_traditional_basic():
    """Test basic flow calibration calculation."""
    response = client.post(
        "/api/v1/calculators/flow-calibration-traditional",
        json={
            "old_flow_rate": 1.0,
            "measured_wall_thickness": 2.8,
            "desired_wall_thickness": 3.0
        }
    )
    assert response.status_code == 200
    data = response.json()
    
    # Check response structure
    assert "new_flow_rate" in data
    assert "change_percent" in data
    assert "adjustment" in data
    assert "test_parameters" in data
    assert "recommendation" in data
    
    # Verify calculation
    expected_flow = 1.0 * (3.0 / 2.8)  # 1.0714
    assert abs(data["new_flow_rate"] - expected_flow) < 0.001


def test_flow_calibration_traditional_high_flow():
    """Test with over-extrusion scenario."""
    response = client.post(
        "/api/v1/calculators/flow-calibration-traditional",
        json={
            "old_flow_rate": 1.0,
            "measured_wall_thickness": 3.5,
            "desired_wall_thickness": 3.0
        }
    )
    assert response.status_code == 200
    data = response.json()
    
    # Should reduce flow
    assert data["new_flow_rate"] < 1.0
    assert data["change_percent"] < 0


def test_flow_calibration_traditional_validation():
    """Test input validation."""
    # Missing required field
    response = client.post(
        "/api/v1/calculators/flow-calibration-traditional",
        json={
            "old_flow_rate": 1.0,
            "measured_wall_thickness": 3.0
            # missing desired_wall_thickness
        }
    )
    assert response.status_code == 422
    
    # Out of range
    response = client.post(
        "/api/v1/calculators/flow-calibration-traditional",
        json={
            "old_flow_rate": 5.0,  # > 2.0
            "measured_wall_thickness": 3.0,
            "desired_wall_thickness": 3.0
        }
    )
    assert response.status_code == 422


def test_flow_calibration_traditional_zero_division():
    """Test division by zero protection."""
    response = client.post(
        "/api/v1/calculators/flow-calibration-traditional",
        json={
            "old_flow_rate": 1.0,
            "measured_wall_thickness": 0,  # Would cause division by zero
            "desired_wall_thickness": 3.0
        }
    )
    assert response.status_code == 422  # Validation catches this


def test_flow_calibration_traditional_cors_headers():
    """Test CORS headers are present."""
    response = client.post(
        "/api/v1/calculators/flow-calibration-traditional",
        json={
            "old_flow_rate": 1.0,
            "measured_wall_thickness": 3.0,
            "desired_wall_thickness": 3.0
        }
    )
    assert response.status_code == 200
    assert "access-control-allow-origin" in response.headers
```

**Test Coverage Requirements:**
- Basic calculation (happy path)
- Edge cases (min/max values)
- Validation errors (invalid inputs)
- Division by zero / overflow protection
- CORS headers present
- Response structure validation

### Step 6: Add Navigation Links

**File:** `backend/app/templates/base.html`

Add calculator to navigation and calculator grid:

```html
<!-- In calculator grid section -->
<a href="/calculator-flow-calibration-traditional" 
   class="calculator-card">
    <h3>Flow Calibration (Traditional)</h3>
    <p>Wall thickness method</p>
</a>
```

### Step 7: Update Documentation

1. **README.md** - Add to calculator list
2. **API.md** - Document endpoint with examples
3. **TODO.md** - Mark as completed
4. **ARCHITECTURE.md** - Update status

---

## Testing Your Calculator

### Run All Tests
```bash
cd /Users/wilsonm/development/m3dp-uip
uv run pytest backend/tests/test_calculators.py -v
```

### Run Specific Test
```bash
uv run pytest backend/tests/test_calculators.py::test_flow_calibration_traditional_basic -v
```

### Check Coverage
```bash
uv run pytest backend/tests/test_calculators.py --cov=backend/app/api/endpoints/calculators --cov-report=html
```

### Manual Testing with cURL
```bash
curl -X POST http://localhost:8000/api/v1/calculators/flow-calibration-traditional \
  -H "Content-Type: application/json" \
  -d '{
    "old_flow_rate": 1.0,
    "measured_wall_thickness": 2.8,
    "desired_wall_thickness": 3.0
  }'
```

---

## Common Patterns

### Formula Validation
Always verify formulas against source material:
- Cross-reference with `research/EXTRACTED_FORMULAS.md`
- Compare with Klipper documentation
- Test with known values from community

### Tolerance Checking
Many calculators include tolerance ranges:

```python
# Example: Rotation distance tolerance is ±2%
within_tolerance = abs(change_percent) <= 2.0

if within_tolerance:
    recommendation = "Change is within acceptable range"
else:
    recommendation = "Change exceeds tolerance. Verify inputs"
```

### Recommendation Logic
Tailor recommendations based on calculation results:

```python
if new_value < old_value:
    recommendation = "Value decreased. This indicates..."
elif new_value > old_value:
    recommendation = "Value increased. This indicates..."
else:
    recommendation = "No change needed."
```

### CSV Data Integration

If your calculator needs CSV data:

```python
# Load CSV
csv_loader = get_csv_loader()
df = csv_loader.load_csv("flow_calibration_traditional.csv")

# Access rows
for idx, row in df.iterrows():
    parameter = row["parameter"]
    value = row["value"]
    unit = row["unit"]
    formula = row["formula"]
    notes = row["notes"]
```

---

## Troubleshooting

### Test Failures

**Issue:** Validation tests fail
```bash
# Check Pydantic model field definitions
# Verify Field constraints (gt, le, examples)
# Ensure request data matches model
```

**Issue:** Calculation is incorrect
```bash
# Verify formula against research docs
# Check for rounding/precision issues
# Test with known values from other sources
```

### Import Errors

**Issue:** `ModuleNotFoundError: No module named...`
```bash
# Verify .csv file exists in correct location
# Check import paths in endpoints
# Ensure all dependencies installed: uv pip install -e '.[dev]'
```

### Template Issues

**Issue:** Form not submitting
```bash
# Check HTMX endpoint path is correct
# Verify HTTP method (POST)
# Check hx-target div exists
# Inspect browser console for errors
```

---

## Quick Checklist

- [ ] CSV data file created with correct schema
- [ ] Pydantic request/response models defined
- [ ] Endpoint function implemented with formula
- [ ] HTML template created with form and results
- [ ] Unit tests written (5+ tests)
- [ ] All tests passing (100%)
- [ ] Manual testing with cURL or browser
- [ ] Documentation updated (README, API, TODO)
- [ ] Navigation links added
- [ ] CORS headers verified
- [ ] Code formatted: `ruff format .`
- [ ] Code linted: `ruff check .`

---

## Need Help?

1. Review existing calculator implementations in `calculators.py`
2. Check API documentation for endpoint patterns
3. Reference ARCHITECTURE.md for data flow
4. Examine test examples in `test_calculators.py`
5. Open issue: https://github.com/minimal3dp/m3dp-uip/issues

---

## Next Steps

Once your calculator is complete:

1. **Create Pull Request** with clear description
2. **Link to formula source** (CSV row or documentation)
3. **Request review** from maintainers
4. **Merge to main** after approval
5. **Deploy to production** (automatic via Railway)
