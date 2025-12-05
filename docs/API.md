# M3DP-UIP API Documentation

## Base URL

```
Development: http://localhost:8000
Production: https://minimal3dp.com
```

## Authentication

All endpoints are **public** - no authentication required.

## Response Format

All API responses use JSON with the following structure:

```json
{
  "status": "success|error",
  "data": { /* calculation results */ },
  "error": null,
  "timestamp": "2025-12-04T23:00:00Z"
}
```

## Status Codes

| Code | Meaning | Example |
|------|---------|---------|
| 200 | OK - Calculation successful | Valid calculator result |
| 422 | Validation Error - Invalid input | Missing required field, out of range |
| 400 | Bad Request - Logic error | Incompatible parameter combination |
| 500 | Server Error - Unexpected failure | CSV file not found, calculation overflow |

## Endpoints

### Health & Info

#### GET /
Home page (HTML)
```bash
curl http://localhost:8000/
```

#### GET /health
Health check
```bash
curl http://localhost:8000/health
# Returns: {"status": "healthy"}
```

#### GET /api/v1/calculators
List all available calculators (JSON)
```bash
curl http://localhost:8000/api/v1/calculators
```

**Response:**
```json
{
  "total": 10,
  "implemented": 10,
  "pending": 6,
  "calculators": [
    {
      "id": "rotation_distance",
      "name": "Extruder Rotation Distance",
      "category": "Extruder",
      "description": "Calculate E-steps and rotation distance",
      "status": "implemented"
    }
  ]
}
```

### Calculator Endpoints

All calculators follow this pattern:

```
POST /api/v1/calculators/{calculator_id}
```

#### 1. Rotation Distance

**Endpoint:** `POST /api/v1/calculators/rotation_distance`

**Description:** Calculate E-steps and rotation distance for extruder calibration

**Request:**
```json
{
  "current_rotation_distance": 33.5,
  "requested_extrusion": 100.0,
  "actual_extrusion": 98.5
}
```

**Parameters:**
| Field | Type | Range | Required | Description |
|-------|------|-------|----------|-------------|
| current_rotation_distance | float | 0 < x ≤ 100 | Yes | Current value from printer.cfg |
| requested_extrusion | float | 0 < x ≤ 500 | Yes | Requested filament (usually 100mm) |
| actual_extrusion | float | 0 < x ≤ 500 | Yes | Measured filament extruded |

**Response:**
```json
{
  "new_rotation_distance": 33.9137,
  "change_percent": 1.23,
  "within_tolerance": true,
  "klipper_config": "rotation_distance = 33.9137",
  "recommendation": "Update printer.cfg and test extrusion"
}
```

**Formula:**
```
new_rotation_distance = current_rd × (requested / actual)
change_percent = ((new_rd - old_rd) / old_rd) × 100
within_tolerance = |change_percent| ≤ 2.0
```

**Example:**
```bash
curl -X POST http://localhost:8000/api/v1/calculators/rotation_distance \
  -H "Content-Type: application/json" \
  -d '{
    "current_rotation_distance": 33.5,
    "requested_extrusion": 100,
    "actual_extrusion": 98.5
  }'
```

---

#### 2. OrcaSlicer Flow Calibration (Two-Pass)

**Endpoint:** `POST /api/v1/calculators/orcaslicer_flow`

**Description:** Calibrate flow rate using two-pass method in OrcaSlicer

**Request:**
```json
{
  "old_flow_rate": 0.99,
  "pass_1_slide_value": -10,
  "pass_2_slide_value": -5
}
```

**Parameters:**
| Field | Type | Range | Required | Description |
|-------|------|-------|----------|-------------|
| old_flow_rate | float | 0 < x ≤ 2 | Yes | Current flow rate (1.0 = 100%) |
| pass_1_slide_value | int | -50 to 50 | Yes | Slide number with smoothest surface |
| pass_2_slide_value | int | -50 to 50 | No | Optional second pass slide value |

**Response:**
```json
{
  "new_flow_rate": 0.98,
  "change_percent": -1.01,
  "slides_processed": 2,
  "smoothness_range": 9,
  "recommendation": "Apply 0.98 flow rate and verify"
}
```

**Example:**
```bash
curl -X POST http://localhost:8000/api/v1/calculators/orcaslicer_flow \
  -H "Content-Type: application/json" \
  -d '{
    "old_flow_rate": 0.99,
    "pass_1_slide_value": -10,
    "pass_2_slide_value": -5
  }'
```

---

#### 3. OrcaSlicer Flow YOLO (Single-Pass)

**Endpoint:** `POST /api/v1/calculators/orcaslicer_flow_yolo`

**Description:** Quick flow calibration using single-pass method

**Request:**
```json
{
  "old_flow_rate": 1.0,
  "slide_value": -15,
  "adjustment": 0.005
}
```

**Response:**
```json
{
  "new_flow_rate": 1.005,
  "slide_index": -15,
  "recommended_adjustment": 0.005,
  "note": "Single-pass method provides quick feedback"
}
```

---

#### 4. Run Current (TMC2208/2209)

**Endpoint:** `POST /api/v1/calculators/run_current`

**Description:** Calculate run current for TMC stepper drivers

**Request:**
```json
{
  "rms_current": 1.5,
  "driver_type": "TMC2209"
}
```

**Parameters:**
| Field | Type | Options | Required | Description |
|-------|------|---------|----------|-------------|
| rms_current | float | 0.1 - 3.0 | Yes | Current in Amps |
| driver_type | string | TMC2208, TMC2209 | Yes | Stepper driver model |

**Response:**
```json
{
  "run_current": 1.5,
  "hold_current": 0.75,
  "driver": "TMC2209",
  "klipper_config": "[tmc2209 stepper_x]\nrun_current: 1.5\nhold_current: 0.75"
}
```

---

#### 5. Pressure Advance (PA)

**Endpoint:** `POST /api/v1/calculators/pressure_advance`

**Description:** Calculate pressure advance values for different extruder types and materials

**Request:**
```json
{
  "extruder_type": "direct_drive",
  "material": "PLA",
  "nozzle_diameter": 0.4
}
```

**Parameters:**
| Field | Type | Options | Required | Description |
|-------|------|---------|----------|-------------|
| extruder_type | string | direct_drive, bowden | Yes | Extruder configuration |
| material | string | PLA, PETG, TPU | Yes | Filament material |
| nozzle_diameter | float | 0.2 - 1.0 | Yes | Nozzle size in mm |

**Response:**
```json
{
  "material": "PLA",
  "extruder_type": "direct_drive",
  "base_pressure_advance": 0.04,
  "range_min": 0.02,
  "range_max": 0.06,
  "test_parameters": {
    "first_layer": 0.04,
    "layer_height": 0.2,
    "speed": 50
  },
  "recommendation": "Start at 0.04 and tune in 0.01 increments"
}
```

---

#### 6. Input Shaping

**Endpoint:** `POST /api/v1/calculators/input_shaping`

**Description:** Calculate input shaping frequencies for resonance compensation

**Request:**
```json
{
  "axis": "X",
  "resonance_frequency": 45.0,
  "damping_ratio": 0.1
}
```

**Response:**
```json
{
  "axis": "X",
  "resonance_frequency": 45.0,
  "shaper_type": "mzv",
  "frequency": 45.0,
  "damping": 0.1,
  "klipper_config": "[input_shaper]\nshaper_freq_x: 45.0"
}
```

---

#### 7. X & Y Offsets

**Endpoint:** `POST /api/v1/calculators/xy_offset`

**Description:** Calculate probe Z offset and XY nozzle offsets

**Request:**
```json
{
  "current_z_offset": -0.5,
  "measured_z": -0.3,
  "x_offset": 20,
  "y_offset": -15
}
```

**Response:**
```json
{
  "new_z_offset": -0.7,
  "x_offset_mm": 20,
  "y_offset_mm": -15,
  "klipper_config": "probe_offset_x: 20\nprobe_offset_y: -15"
}
```

---

#### 8. Max Volumetric Speed

**Endpoint:** `POST /api/v1/calculators/max_volumetric_speed`

**Description:** Calculate safe maximum volumetric speed

**Request:**
```json
{
  "nozzle_diameter": 0.4,
  "layer_height": 0.2,
  "filament_diameter": 1.75
}
```

**Response:**
```json
{
  "max_volumetric_speed": 10.5,
  "recommended": 9.0,
  "unit": "mm³/s",
  "note": "Conservative estimate for safety margin"
}
```

---

#### 9. Lead Screw Rotation Distance

**Endpoint:** `POST /api/v1/calculators/lead_screw_rotation_distance`

**Description:** Calculate Z-axis lead screw rotation distance

**Request:**
```json
{
  "lead": 8,
  "microstepping": 16,
  "stepper_angle": 1.8
}
```

**Response:**
```json
{
  "rotation_distance": 8.0,
  "lead": 8,
  "microstepping": 16,
  "formula_used": "lead / (200 / (360 / stepper_angle))"
}
```

---

#### 10. Line Widths (OrcaSlicer)

**Endpoint:** `POST /api/v1/calculators/line_widths`

**Description:** Calculate optimal line widths for OrcaSlicer based on nozzle diameter

**Request:**
```json
{
  "nozzle_diameter": 0.4
}
```

**Response:**
```json
{
  "nozzle_diameter": 0.4,
  "thin_wall": 0.3,
  "perimeter": 0.4,
  "infill": 0.45,
  "support": 0.35,
  "raft": 0.4,
  "note": "Adjust based on material and print speed"
}
```

---

## Error Examples

### Validation Error (422)

**Request:**
```bash
curl -X POST http://localhost:8000/api/v1/calculators/rotation_distance \
  -H "Content-Type: application/json" \
  -d '{
    "current_rotation_distance": -5,
    "requested_extrusion": 100,
    "actual_extrusion": 98.5
  }'
```

**Response:**
```json
{
  "detail": [
    {
      "type": "greater_than",
      "loc": ["body", "current_rotation_distance"],
      "msg": "Input should be greater than 0",
      "input": -5
    }
  ]
}
```

### Logic Error (400)

**Request:**
```bash
curl -X POST http://localhost:8000/api/v1/calculators/rotation_distance \
  -H "Content-Type: application/json" \
  -d '{
    "current_rotation_distance": 33.5,
    "requested_extrusion": 100,
    "actual_extrusion": 0
  }'
```

**Response:**
```json
{
  "detail": "Division by zero: actual_extrusion cannot be 0"
}
```

---

## Rate Limiting

No rate limiting currently implemented. Production deployment may add:
- Per-IP rate limits
- Per-calculator request limits
- Burst limits

---

## CORS Headers

All endpoints include CORS headers for cross-origin requests:

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Headers: Content-Type
```

For production, configure `ALLOWED_ORIGINS` in `.env`

---

## Analytics Tracking

Calculator usage is tracked via Google Analytics 4 (GA4) if configured. No personal data is collected.

---

## OpenAPI Documentation

Interactive API documentation available at:

```
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
```

---

## Client Integration Examples

### JavaScript (HTMX)

```html
<form hx-post="/api/v1/calculators/rotation_distance" 
      hx-target="#result"
      hx-swap="innerHTML">
  <input type="number" name="current_rotation_distance" required>
  <input type="number" name="requested_extrusion" required>
  <input type="number" name="actual_extrusion" required>
  <button type="submit">Calculate</button>
</form>
<div id="result"></div>
```

### Python (httpx)

```python
import httpx

async with httpx.AsyncClient() as client:
    response = await client.post(
        "http://localhost:8000/api/v1/calculators/rotation_distance",
        json={
            "current_rotation_distance": 33.5,
            "requested_extrusion": 100,
            "actual_extrusion": 98.5
        }
    )
    result = response.json()
    print(f"New rotation distance: {result['new_rotation_distance']}")
```

### cURL

```bash
curl -X POST http://localhost:8000/api/v1/calculators/rotation_distance \
  -H "Content-Type: application/json" \
  -d '{
    "current_rotation_distance": 33.5,
    "requested_extrusion": 100,
    "actual_extrusion": 98.5
  }'
```

---

## Versioning

- Current API version: **v1**
- Breaking changes will trigger version bump to v2
- Deprecated endpoints will include `Deprecation` header

---

## Support

For API issues:
1. Check [Troubleshooting Guide](./development/DEBUG.md)
2. Review [Architecture](./ARCHITECTURE.md)
3. Open issue on GitHub: https://github.com/minimal3dp/m3dp-uip/issues
