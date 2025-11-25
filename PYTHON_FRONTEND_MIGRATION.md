# Python Frontend Migration - HTMX + Alpine.js

This branch (`experiment/python-frontend-htmx`) replaces the Nuxt/Vue frontend with a Python-only stack using FastAPI templates, HTMX, and Alpine.js.

## ✅ Benefits

- **Single Language**: Everything in Python (no Node.js/npm)
- **Single Server**: One process instead of two
- **No Build Step**: No Vite, no PostCSS, no bundling
- **Zero Node Issues**: No more npm dependency hell
- **Hot Reload**: FastAPI auto-reloads on file changes
- **Same UI Quality**: Tailwind CSS (CDN), modern interactions

## 🏗️ Architecture

```
backend/
├── app/
│   ├── main.py              # FastAPI app + web routes
│   ├── api/endpoints/       # REST API (unchanged)
│   ├── templates/           # Jinja2 HTML templates
│   │   ├── base.html       # Base layout
│   │   ├── index.html      # Homepage
│   │   ├── calculators.html# Calculator list
│   │   └── calculator_*.html# Individual calculators
│   └── static/             # CSS, JS, images (if needed)
```

## 🚀 Running the New Stack

**Single command:**
```bash
./scripts/dev-python-fullstack.sh
```

Then visit:
- **Web UI**: http://localhost:8000/home
- **Calculators**: http://localhost:8000/calculators-ui
- **API Docs**: http://localhost:8000/docs

## 🎨 Technologies

| Component | Technology | Delivery |
|-----------|-----------|----------|
| Backend | FastAPI | Python |
| Templates | Jinja2 | Server-side |
| Styling | Tailwind CSS | CDN |
| Interactivity | Alpine.js | CDN (~15KB) |
| AJAX | HTMX | CDN (~14KB) |
| **Total JS** | | **~29KB** (vs 2MB+ for Nuxt) |

## 📝 Current Progress

### ✅ Completed
- [x] Base template with navigation
- [x] Homepage with feature grid
- [x] Calculators list page
- [x] Rotation Distance calculator (full working example)
- [x] FastAPI routes for web pages
- [x] Static file serving
- [x] Development script

### 🔄 In Progress
- [ ] Diagnosis page (image/text upload)
- [ ] Remaining calculator pages (13 more)
- [ ] Mobile menu functionality
- [ ] Error handling UI
- [ ] Loading states

### ⏳ TODO
- [ ] Convert all 17 calculator components
- [ ] Add file upload for image diagnosis
- [ ] Cookie consent banner
- [ ] Analytics integration
- [ ] Production build optimization
- [ ] Delete old frontend/ directory

## 🧪 Testing

### Test the new frontend:
```bash
# Start server
./scripts/dev-python-fullstack.sh

# In another terminal
curl http://localhost:8000/home

# Or open in browser:
open http://localhost:8000/home
```

### Test API still works:
```bash
curl -X POST http://localhost:8000/api/v1/calculators/rotation-distance \
  -H 'Content-Type: application/json' \
  -d '{"current_rotation_distance":33.5, "requested_extrusion":100, "actual_extrusion":98.5}'
```

## 💡 How It Works

### HTMX Example (AJAX without JavaScript)
```html
<button hx-post="/api/v1/calculators/rotation-distance"
        hx-vals='{"current": 33.5}'
        hx-target="#result">
    Calculate
</button>
<div id="result"></div>
```

### Alpine.js Example (Reactive UI)
```html
<div x-data="{ count: 0 }">
    <button @click="count++">Increment</button>
    <span x-text="count"></span>
</div>
```

### Jinja2 Template (Server-side rendering)
```html
{% extends "base.html" %}
{% block content %}
    <h1>{{ calculator_name }}</h1>
{% endblock %}
```

## 📊 Migration Status

| Page/Component | Status | Notes |
|----------------|--------|-------|
| Homepage | ✅ Done | Full feature grid, stats |
| Calculator List | ✅ Done | Fetches from API |
| Rotation Distance | ✅ Done | Full working calculator |
| Pressure Advance | ⏳ TODO | Port from Vue |
| Input Shaping | ⏳ TODO | Port from Vue |
| Max Volumetric Speed | ⏳ TODO | Port from Vue |
| ... (13 more) | ⏳ TODO | See frontend/components/ |
| Diagnosis Page | ⏳ TODO | Image + text upload |

## 🔄 Migration Steps for Each Calculator

1. **Copy Vue component** from `frontend/components/`
2. **Create Jinja template** in `backend/app/templates/`
3. **Replace Vue syntax** with Alpine.js:
   - `v-model` → `x-model`
   - `@click` → `@click`
   - `v-if` → `x-show`
4. **Use HTMX** for API calls instead of `$fetch`
5. **Add route** to `backend/app/main.py`
6. **Test** the new page

Example conversion time: **15-30 minutes per calculator**

## 🚀 Deployment

### Development
```bash
./scripts/dev-python-fullstack.sh
```

### Production
```bash
# Single Docker container
FROM python:3.12-slim
COPY backend/ /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Vercel/Fly.io/Render
All support FastAPI with zero configuration. No separate frontend build step needed!

## 📈 Performance Comparison

| Metric | Nuxt/Vue | HTMX/Alpine |
|--------|----------|-------------|
| Initial JS Load | ~2MB | ~29KB |
| Build Time | 30-60s | 0s (no build) |
| Dev Server Startup | 5-10s | 1-2s |
| Hot Reload | ~500ms | ~100ms |
| Server Count | 2 | 1 |
| Node Required | Yes | No |

## 🎯 Decision Point

### When to merge:
- [ ] All calculator pages converted
- [ ] Diagnosis page working
- [ ] Mobile UI tested
- [ ] No visual regressions
- [ ] Performance acceptable
- [ ] Team approves

### Rollback plan:
```bash
git checkout feature/phase-5-enhancements
./scripts/dev-all.sh  # Back to Vue
```

## 📚 Resources

- [HTMX Documentation](https://htmx.org/docs/)
- [Alpine.js Documentation](https://alpinejs.dev/)
- [FastAPI Templates](https://fastapi.tiangolo.com/advanced/templates/)
- [Tailwind CSS](https://tailwindcss.com/docs)

---

**Branch Status**: 🧪 Experimental
**Merge Target**: `main` (after testing)
**Fallback**: `feature/phase-5-enhancements`
