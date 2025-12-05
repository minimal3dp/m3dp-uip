# Gemini Vision API Integration Guide

## Cost Analysis & Free Alternatives

### Gemini Vision API Pricing (As of Nov 2025)

#### Gemini 1.5 Flash (Recommended for Production)
- **Free Tier**: 15 requests per minute (RPM)
- **Cost**: $0 for free tier usage
- **Image Analysis**: Supports up to 4000 tokens per image
- **Context Window**: 1M tokens total
- **Best For**: Production apps with moderate traffic

#### Gemini 1.5 Pro
- **Free Tier**: 2 RPM (very limited)
- **Paid**: $0.00125 per 1000 characters input, $0.005 per 1000 characters output
- **Higher Quality**: Better accuracy but more expensive
- **Best For**: High-accuracy needs, not suitable for free apps

### ⚠️ Cost Concerns for Free App

**Estimated Usage for M3DP-UIP:**
- Average diagnosis: 1 image + 500 token prompt
- Expected: ~10-50 diagnoses/day (based on minimal3dp.com traffic)
- **Free Tier Verdict**: ✅ Gemini 1.5 Flash is sufficient (15 RPM = 900/hour)

**Potential Costs:**
- If you exceed free tier → Gemini 1.5 Flash paid tier: ~$0.10-0.50/day
- Annual worst case: ~$180/year (if heavily used beyond free limits)

### 🆓 Free Alternatives

#### 1. **Gemini 1.5 Flash (Free Tier)** ⭐ RECOMMENDED
- **Pros**:
  - 15 RPM is generous for your use case
  - Google-backed, reliable
  - Good vision capabilities
  - No credit card required for free tier
- **Cons**:
  - Rate limits (manageable for your traffic)
  - Requires API key management
- **Setup**: 5 minutes
- **Cost**: $0 for foreseeable future

#### 2. **LLaVA (Local Model)**
- **Pros**:
  - 100% free, runs locally
  - No API calls, no rate limits
  - Privacy-focused
- **Cons**:
  - Requires GPU (NVIDIA recommended)
  - More complex setup (Ollama or vLLM)
  - Lower accuracy than Gemini
  - You need to host it (VPS/cloud costs if deployed)
- **Setup**: 1-2 hours
- **Cost**: $0 locally, $10-20/month for cloud GPU

#### 3. **Hugging Face Vision Models (Free Inference API)**
- **Pros**:
  - Completely free for low-moderate usage
  - Multiple models (BLIP-2, InstructBLIP, etc.)
  - No credit card
- **Cons**:
  - Lower accuracy than Gemini
  - Rate limits (uncertain, depends on load)
  - Models may not be 3D printing-specific
- **Setup**: 10-15 minutes
- **Cost**: $0

#### 4. **OpenAI GPT-4 Vision**
- **Pros**:
  - Excellent accuracy
  - Well-documented
- **Cons**:
  - ❌ NO FREE TIER
  - Expensive: ~$0.01-0.03 per image analysis
  - Not suitable for free apps
- **Cost**: $5-30/month for your traffic

---

## Recommended Solution: Gemini 1.5 Flash (Free Tier)

### Why Gemini 1.5 Flash?
1. **Free tier is sufficient** for minimal3dp.com traffic (15 RPM)
2. **Google-backed** - reliable and maintained
3. **Good quality** vision analysis
4. **Easy integration** with Python SDK
5. **No credit card required** for free tier

### Cost Mitigation Strategies
1. **Cache responses**: Store common diagnoses in Firestore
2. **Rate limiting**: Queue requests if near 15 RPM limit
3. **Fallback to rules**: Use CSV-based diagnosis for known patterns
4. **User throttling**: Limit to 3 diagnoses/user/day

---

## Integration Steps

### Phase 1: Setup (5 minutes)

#### 1.1 Get Gemini API Key
```bash
# Visit: https://aistudio.google.com/app/apikey
# Click "Create API Key"
# Copy key (starts with "AIza...")
```

#### 1.2 Add to Environment
```bash
# backend/.env
GOOGLE_GENAI_API_KEY=AIzaSy...your_key_here
GEMINI_MODEL=gemini-1.5-flash  # Free tier model
GEMINI_RATE_LIMIT=15  # RPM limit
```

#### 1.3 Install Python SDK
```bash
cd backend
uv pip install google-generativeai Pillow
```

### Phase 2: Backend Implementation (30 minutes)

#### 2.1 Create Vision Service
**File**: `backend/app/services/vision_service.py`

```python
import os
import base64
from typing import Optional
import google.generativeai as genai
from PIL import Image
import io

class VisionService:
    def __init__(self):
        api_key = os.getenv("GOOGLE_GENAI_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_GENAI_API_KEY not set")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    async def analyze_print_failure(
        self,
        image_bytes: bytes,
        user_context: Optional[dict] = None
    ) -> dict:
        """
        Analyze 3D print failure image.

        Args:
            image_bytes: Raw image bytes (JPEG/PNG)
            user_context: Optional printer/material info

        Returns:
            {
                "error_type": "VFA" | "Under-extrusion" | "Layer Shift" | ...,
                "confidence": 0.0-1.0,
                "description": "Human-readable diagnosis",
                "recommended_calculator": "pressure-advance" | "flow-calibration" | null,
                "klipper_params": {...}
            }
        """
        # Compress image if > 2MB (reduce API costs)
        image = Image.open(io.BytesIO(image_bytes))
        if len(image_bytes) > 2_000_000:
            image = self._compress_image(image)

        # Build prompt with context
        prompt = self._build_diagnostic_prompt(user_context)

        # Call Gemini API
        response = await self.model.generate_content_async([
            prompt,
            image
        ])

        # Parse structured response
        return self._parse_vision_response(response.text)

    def _build_diagnostic_prompt(self, context: Optional[dict]) -> str:
        base_prompt = """
You are an expert 3D printing diagnostician specializing in FDM/FFF printing.

Analyze this print failure image and return a JSON object with:
{
  "error_type": "<primary defect category>",
  "confidence": <0.0-1.0>,
  "description": "<2-3 sentence explanation>",
  "recommended_calculator": "<which M3DP calculator to use>",
  "klipper_params": {<relevant config params if applicable>}
}

Error Categories:
- VFA (Vertical Fine Artifacts / ringing)
- Under-extrusion
- Over-extrusion
- Layer Shift
- Stringing
- Warping
- Poor Adhesion
- Z-banding
- Inconsistent Extrusion

Recommended Calculators (return null if not applicable):
- "rotation-distance": For extrusion calibration
- "orcaslicer-flow": For flow ratio tuning
- "pressure-advance": For VFA/bulging corners
- null: For mechanical issues (belts, leadscrew, etc.)
"""

        if context:
            base_prompt += f"\n\nPrinter Context:\n{context}"

        return base_prompt

    def _compress_image(self, image: Image.Image, max_size: int = 1_500_000) -> Image.Image:
        """Compress image to reduce API costs."""
        # Resize if too large
        max_dimension = 1920
        if image.width > max_dimension or image.height > max_dimension:
            image.thumbnail((max_dimension, max_dimension), Image.Resampling.LANCZOS)

        # Convert to JPEG with quality reduction
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG", quality=85, optimize=True)
        buffer.seek(0)

        return Image.open(buffer)

    def _parse_vision_response(self, response_text: str) -> dict:
        """Parse Gemini's JSON response."""
        import json
        import re

        # Extract JSON from markdown code block if present
        json_match = re.search(r'```json\s*(\{.*?\})\s*```', response_text, re.DOTALL)
        if json_match:
            response_text = json_match.group(1)

        try:
            return json.loads(response_text)
        except json.JSONDecodeError:
            # Fallback if JSON parsing fails
            return {
                "error_type": "Unknown",
                "confidence": 0.0,
                "description": response_text[:200],
                "recommended_calculator": None,
                "klipper_params": {}
            }
```

#### 2.2 Create Diagnosis Endpoint
**File**: `backend/app/api/endpoints/diagnosis.py`

```python
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.vision_service import VisionService
from pydantic import BaseModel

router = APIRouter(prefix="/api/diagnosis", tags=["diagnosis"])
vision_service = VisionService()

class DiagnosisResponse(BaseModel):
    error_type: str
    confidence: float
    description: str
    recommended_calculator: Optional[str]
    klipper_params: dict

@router.post("/analyze", response_model=DiagnosisResponse)
async def analyze_print_failure(
    file: UploadFile = File(...),
    printer_type: Optional[str] = None,
    material: Optional[str] = None
):
    """
    Analyze uploaded print failure image.

    Accepts: JPEG, PNG, WebP
    Max size: 10MB (enforced by frontend)
    """
    # Validate file type
    if file.content_type not in ["image/jpeg", "image/png", "image/webp"]:
        raise HTTPException(400, "Invalid file type. Use JPEG, PNG, or WebP.")

    # Read image bytes
    image_bytes = await file.read()

    # Validate size
    if len(image_bytes) > 10_000_000:
        raise HTTPException(400, "File too large. Max 10MB.")

    # Build context
    context = {
        "printer": printer_type,
        "material": material
    } if printer_type or material else None

    # Analyze with Gemini
    try:
        result = await vision_service.analyze_print_failure(image_bytes, context)
        return result
    except Exception as e:
        raise HTTPException(500, f"Vision analysis failed: {str(e)}")
```

#### 2.3 Register Endpoint
**File**: `backend/app/main.py`

```python
from app.api.endpoints import diagnosis

# Add to your existing router registration
app.include_router(diagnosis.router)
```

### Phase 3: Frontend Integration (45 minutes)

#### 3.1 Create Upload Component
**File**: `frontend/components/DiagnosisUpload.vue`

```vue
<template>
  <div class="glass-card p-6">
    <h2 class="text-2xl font-bold mb-4">Print Failure Diagnosis</h2>

    <!-- File Upload -->
    <div class="mb-6">
      <label class="block text-sm font-medium mb-2">
        Upload Print Photo
      </label>
      <input
        type="file"
        accept="image/jpeg,image/png,image/webp"
        @change="handleFileSelect"
        class="w-full"
      />
      <p class="text-xs text-gray-400 mt-1">
        JPEG, PNG, or WebP • Max 10MB
      </p>
    </div>

    <!-- Optional Context -->
    <div class="grid grid-cols-2 gap-4 mb-6">
      <input
        v-model="printerType"
        placeholder="Printer model (optional)"
        class="input"
      />
      <input
        v-model="material"
        placeholder="Material (optional)"
        class="input"
      />
    </div>

    <!-- Analyze Button -->
    <button
      @click="analyzePrint"
      :disabled="!selectedFile || isAnalyzing"
      class="btn-primary w-full"
    >
      <i v-if="isAnalyzing" data-lucide="loader-2" class="animate-spin" />
      {{ isAnalyzing ? 'Analyzing...' : 'Analyze Print' }}
    </button>

    <!-- Results -->
    <div v-if="result" class="mt-6 glass-card p-4">
      <h3 class="text-lg font-semibold text-orange-400">
        Diagnosis: {{ result.error_type }}
      </h3>
      <p class="text-sm text-gray-300 mt-2">{{ result.description }}</p>

      <div v-if="result.recommended_calculator" class="mt-4">
        <NuxtLink
          :to="`/calculators#${result.recommended_calculator}`"
          class="btn-secondary"
        >
          Use {{ result.recommended_calculator }} Calculator
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const selectedFile = ref<File | null>(null);
const printerType = ref('');
const material = ref('');
const isAnalyzing = ref(false);
const result = ref<any>(null);

const handleFileSelect = (event: Event) => {
  const target = event.target as HTMLInputElement;
  selectedFile.value = target.files?.[0] || null;
};

const analyzePrint = async () => {
  if (!selectedFile.value) return;

  isAnalyzing.value = true;
  result.value = null;

  try {
    const formData = new FormData();
    formData.append('file', selectedFile.value);
    if (printerType.value) formData.append('printer_type', printerType.value);
    if (material.value) formData.append('material', material.value);

    const response = await fetch('http://localhost:8000/api/diagnosis/analyze', {
      method: 'POST',
      body: formData
    });

    if (!response.ok) throw new Error('Analysis failed');

    result.value = await response.json();
  } catch (error) {
    console.error('Diagnosis error:', error);
    alert('Failed to analyze image. Please try again.');
  } finally {
    isAnalyzing.value = false;
  }
};
</script>
```

#### 3.2 Add to Diagnosis Page
**File**: `frontend/pages/diagnosis.vue`

```vue
<template>
  <div class="container mx-auto px-4 py-12">
    <DiagnosisUpload />
  </div>
</template>
```

### Phase 4: Rate Limiting & Caching (30 minutes)

#### 4.1 Add Rate Limiter
**File**: `backend/app/middleware/rate_limit.py`

```python
from fastapi import HTTPException, Request
from collections import defaultdict
import time

class RateLimiter:
    def __init__(self, requests_per_minute: int = 15):
        self.rpm = requests_per_minute
        self.requests = defaultdict(list)

    async def check_rate_limit(self, request: Request):
        client_ip = request.client.host
        now = time.time()

        # Clean old requests
        self.requests[client_ip] = [
            t for t in self.requests[client_ip]
            if now - t < 60
        ]

        # Check limit
        if len(self.requests[client_ip]) >= self.rpm:
            raise HTTPException(429, "Rate limit exceeded. Try again in 60 seconds.")

        self.requests[client_ip].append(now)
```

#### 4.2 Apply to Endpoint
```python
from app.middleware.rate_limit import RateLimiter

rate_limiter = RateLimiter(requests_per_minute=10)  # Conservative limit

@router.post("/analyze")
async def analyze_print_failure(
    request: Request,
    file: UploadFile = File(...)
):
    await rate_limiter.check_rate_limit(request)
    # ... rest of implementation
```

---

## Testing Vision API

### Test Script
**File**: `backend/scripts/test_vision.py`

```python
import asyncio
import os
from app.services.vision_service import VisionService

async def test_vision():
    service = VisionService()

    # Load test image
    with open("test_images/vfa_sample.jpg", "rb") as f:
        image_bytes = f.read()

    # Analyze
    result = await service.analyze_print_failure(image_bytes)

    print("Diagnosis:", result)

if __name__ == "__main__":
    asyncio.run(test_vision())
```

### Run Test
```bash
cd backend
uv run python scripts/test_vision.py
```

---

## Cost Monitoring

### Track API Usage
1. Visit [Google AI Studio Usage](https://aistudio.google.com/app/billing)
2. Monitor daily requests
3. Set up alerts at 80% of free tier

### Emergency Fallback
If you approach limits, implement:
```python
# backend/app/services/fallback_service.py
class FallbackDiagnosisService:
    def analyze_without_vision(self, user_description: str) -> dict:
        """Rule-based diagnosis from text description."""
        # Use keyword matching against CSV knowledge base
        pass
```

---

## Summary & Recommendation

### ✅ Use Gemini 1.5 Flash (Free Tier)
- **Cost**: $0 for your expected traffic
- **Quality**: Good enough for 3D print diagnosis
- **Reliability**: Google-backed
- **Integration**: 1-2 hours total

### 🚨 Implement These Safeguards
1. Rate limiting (10 diagnoses/hour per IP)
2. Image compression (reduce API costs)
3. Response caching (Firestore for common issues)
4. Fallback to CSV-based diagnosis

### 📊 Expected Costs Over Time
- **Year 1**: $0 (within free tier)
- **If you exceed free tier**: ~$5-10/month worst case
- **Migration path**: If costs become an issue, switch to LLaVA (local) or add user limits

**You can confidently proceed with Gemini 1.5 Flash at zero cost for the foreseeable future.**
