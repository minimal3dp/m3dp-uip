# Development Server Scripts

Scripts to manage M3DP-UIP development server (Python fullstack).

## Quick Start

### Start Server (Python Fullstack)

```bash
./scripts/dev-python-fullstack.sh
```

This starts FastAPI with Python templates on http://localhost:8000

Press `Ctrl+C` to stop the server.

### Alternative: Start/Stop Scripts

```bash
# Start server
./scripts/start_servers.sh

# Stop server
./scripts/stop_servers.sh
```

### Backend Only (API without UI)

```bash
./scripts/run_dev.sh
```

Starts FastAPI backend with hot reload on http://localhost:8000

Options:
- `--host HOST` - Bind to specific host (default: 127.0.0.1)
- `--port PORT` - Use specific port (default: 8000)

## Testing URLs

Once server is running:

- **Web UI Home**: http://localhost:8000/home
- **Calculators**: http://localhost:8000/calculators-ui
- **Diagnosis**: http://localhost:8000/diagnosis-ui
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## Logs

Logs are written to `/tmp/m3dp-backend.log`

View logs in real-time:
```bash
tail -f /tmp/m3dp-backend.log
```

## Troubleshooting

### Port Already in Use

If you see "port already in use" errors:
```bash
./scripts/stop_servers.sh
```

Or manually kill the process:
```bash
lsof -ti:8000 | xargs kill -9
```

### Server Won't Start

Check logs:
```bash
cat /tmp/m3dp-backend.log
```

### Dependencies Missing

```bash
cd /path/to/m3dp-uip
uv pip install -e ".[dev]"
```

## Development Workflow

1. **Start server**:
   ```bash
   ./scripts/dev-python-fullstack.sh
   ```

2. **Open browser** to http://localhost:8000/home

3. **Test pages**:
   - Calculators at /calculators-ui
   - Diagnosis at /diagnosis-ui
   - API at /docs

4. **Make changes** - server auto-reloads

5. **Stop server** when done:
   ```bash
   # Press Ctrl+C in the terminal
   # or
   ./scripts/stop_servers.sh
   ```

## Environment Variables

Server uses environment variables from `.env`:
- `GOOGLE_GENAI_API_KEY` - For AI diagnosis features
- `ENVIRONMENT` - Set to "development"
- `DEBUG` - Set to true for detailed logs

Override defaults:
```bash
BACKEND_PORT=9000 ./scripts/dev-python-fullstack.sh
```

## Testing

Run automated page tests:
```bash
python test_pages.py
```

This tests all major pages and verifies they return 200 status codes.
