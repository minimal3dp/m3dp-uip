# Development Server Scripts

Scripts to manage M3DP-UIP backend and frontend servers for development and testing.

## Quick Start

### Start Both Servers (Recommended)

```bash
./scripts/start_servers.sh
```

This will start:
- **Backend** (FastAPI) on http://localhost:8000
- **Frontend** (Nuxt) on http://localhost:3000

Both servers run in the background. Press `Ctrl+C` to stop both.

### Stop All Servers

```bash
./scripts/stop_servers.sh
```

Kills all processes on ports 8000 and 3000.

## Individual Server Scripts

### Backend Only

```bash
./scripts/run_dev.sh
```

Starts FastAPI backend with hot reload on http://localhost:8000

Options:
- `--host HOST` - Bind to specific host (default: 127.0.0.1)
- `--port PORT` - Use specific port (default: 8000)

### Frontend Only

```bash
cd frontend
npm run dev
```

Starts Nuxt dev server on http://localhost:3000

## Testing URLs

Once servers are running:

- **Frontend Home**: http://localhost:3000
- **Calculators**: http://localhost:3000/calculators
- **Diagnosis**: http://localhost:3000/diagnosis
- **Backend API Docs**: http://localhost:8000/docs
- **Backend Health**: http://localhost:8000/health

## Logs

Logs are written to `/tmp/`:
- Backend: `/tmp/m3dp-backend.log`
- Frontend: `/tmp/m3dp-frontend.log`

View logs in real-time:
```bash
tail -f /tmp/m3dp-backend.log
tail -f /tmp/m3dp-frontend.log
```

## Troubleshooting

### Port Already in Use

If you see "port already in use" errors:
```bash
./scripts/stop_servers.sh
```

### Servers Won't Start

Check logs:
```bash
cat /tmp/m3dp-backend.log
cat /tmp/m3dp-frontend.log
```

### Backend Dependencies Missing

```bash
cd /path/to/m3dp-uip
uv pip install -e ".[dev]"
```

### Frontend Dependencies Missing

```bash
cd frontend
npm install
```

## Development Workflow

1. **Start servers**:
   ```bash
   ./scripts/start_servers.sh
   ```

2. **Open browser** to http://localhost:3000

3. **Test calculators** at /calculators

4. **Make changes** - servers auto-reload

5. **Stop servers** when done:
   ```bash
   ./scripts/stop_servers.sh
   # or press Ctrl+C in the terminal
   ```

## Environment Variables

Backend uses environment variables from `.env`:
- `GOOGLE_GENAI_API_KEY` - For diagnosis features
- `ENVIRONMENT` - Set to "development"
- `DEBUG` - Set to true for detailed logs

Frontend uses `nuxt.config.ts`:
- `apiBase` - Backend URL (default: http://localhost:8000)

## Phase 4 Integration Testing

The `start_servers.sh` script is designed for Phase 4 integration testing:
- ✅ Automatic port cleanup
- ✅ Health check validation
- ✅ Graceful shutdown
- ✅ Combined log output
- ✅ Easy manual testing

See `PHASE4_INTEGRATION_TESTS.md` for the full testing checklist.
