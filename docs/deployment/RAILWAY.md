# M3DP-UIP Railway Deployment Guide

## Overview

M3DP-UIP is a stateless, containerized FastAPI application ready for Railway deployment. This guide covers setup, configuration, and production deployment.

## Prerequisites

- GitHub account (for repository access)
- Railway account (free tier available at https://railway.app)
- Git CLI installed
- Docker (optional, for local testing)

---

## Quick Start (5 minutes)

### 1. Connect GitHub Repository

1. Go to https://railway.app
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Authorize Railway to access your GitHub account
5. Select `minimal3dp/m3dp-uip` repository
6. Select `refactor/v2-lean` branch

### 2. Configure Environment

Railway will automatically detect the project type. Ensure these settings:

- **Framework:** Python
- **Start Command:** `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`
- **Dockerfile:** Auto-detected from project

### 3. Set Environment Variables

In Railway dashboard, go to **Variables** and add:

```env
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=info
ALLOWED_ORIGINS=https://minimal3dp.com,https://www.minimal3dp.com
```

### 4. Deploy

Click "Deploy" button. Railway will:
1. Build Docker image (~3-5 minutes)
2. Run health checks
3. Deploy to production
4. Assign temporary URL (e.g., `https://m3dp-uip-prod.railway.app`)

---

## Production Configuration

### Docker Configuration

Railway automatically uses the `Dockerfile` in the project root. Current setup:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -e .
RUN pip install --no-cache-dir jinja2

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# Start server
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Key Points:**
- Listens on `0.0.0.0:8000` (Railway automatically maps to $PORT)
- Health check ensures availability
- Slim Python image (~200MB vs 500MB+ full image)
- System dependencies installed for pandas

### Environment Variables

Set these in Railway dashboard (Variables tab):

| Variable | Value | Purpose |
|----------|-------|---------|
| `ENVIRONMENT` | `production` | Disables debug mode |
| `DEBUG` | `false` | Disables FastAPI debug UI |
| `LOG_LEVEL` | `info` | Production logging |
| `ALLOWED_ORIGINS` | See below | CORS configuration |
| `DATABASE_URL` | Leave empty | Not needed (stateless) |

#### CORS Configuration

For single domain:
```env
ALLOWED_ORIGINS=https://minimal3dp.com
```

For multiple domains:
```env
ALLOWED_ORIGINS=https://minimal3dp.com,https://www.minimal3dp.com,https://api.minimal3dp.com
```

For development (temporary):
```env
ALLOWED_ORIGINS=*
```

---

## Custom Domain Setup

### 1. In Railway Dashboard

1. Go to project settings
2. Click "Domain"
3. Add custom domain: `https://minimal3dp.com`
4. Railway generates SSL certificate automatically (Let's Encrypt)

### 2. In Domain Registrar

Point your domain to Railway:

**Option A: CNAME (Recommended)**
```
Subdomain: @
Type: CNAME
Value: railway.app (Railway provides exact CNAME)
TTL: 3600
```

**Option B: A Record**
```
Type: A
Value: <Railway IP address>
```

**Option C: Nameserver**
Use Railway's nameservers (if supported by registrar)

### 3. Verify SSL Certificate

- Wait 5-15 minutes for DNS propagation
- Visit `https://minimal3dp.com` in browser
- Verify lock icon appears (HTTPS working)
- Check certificate is valid (Let's Encrypt)

---

## Monitoring & Logging

### Application Logs

In Railway dashboard, click "Logs" to view:

```
2025-12-04 23:00:00 🚀 Starting M3DP-UIP Backend...
2025-12-04 23:00:01 📊 Environment: production
2025-12-04 23:00:05 INFO:     Uvicorn running on http://0.0.0.0:8000
2025-12-04 23:00:10 POST /api/v1/calculators/rotation_distance 200 15ms
```

**Log Levels:**
- `DEBUG` - Development only
- `INFO` - Startup messages, requests
- `WARNING` - Validation issues
- `ERROR` - Calculation failures, exceptions

### Metrics

Railway provides built-in metrics:

- **CPU Usage** - Should stay < 20% at typical load
- **Memory Usage** - Should stay < 100MB (Python 3.12 optimized)
- **Disk Usage** - ~500MB (Docker image + dependencies)
- **Network** - Outbound only (no database)

### Health Checks

Railway monitors the `/health` endpoint:

```
GET http://localhost:8000/health
Response: {"status": "healthy"}
```

If health check fails 3 times, deployment is marked unhealthy.

---

## Continuous Deployment

### Automatic Deployment on Push

Railway automatically deploys when you push to the configured branch:

```bash
# Make changes locally
git add .
git commit -m "feat: add new calculator"
git push origin refactor/v2-lean

# Railway detects push, builds, deploys automatically
# Check Railway dashboard for deployment status
```

### Manual Redeploy

1. Go to Railway dashboard
2. Click project
3. Click "Deployments" tab
4. Click "Redeploy" on latest deployment

---

## Scaling

### Vertical Scaling (Larger Instance)

Railway provides different instance sizes:

| Instance | CPU | Memory | Cost/Month | Use Case |
|----------|-----|--------|-----------|----------|
| Starter | Shared | 512MB | Free | Development |
| Pro Small | 0.5 CPU | 1GB | $5 | Low traffic |
| Pro Medium | 1 CPU | 2GB | $10 | Medium traffic |
| Pro Large | 2 CPU | 4GB | $20 | High traffic |

**To upgrade:**
1. Go to project settings
2. Click "Pricing" or "Instance Size"
3. Select new size
4. Wait for redeployment (~2 minutes)

### Horizontal Scaling (Multiple Instances)

Railway supports replica deployments:

1. Go to project settings
2. Click "Replica" or "Scaling"
3. Set number of replicas (e.g., 3)
4. Railway load balances between instances

**Recommended:** Start with 1 instance, scale to 2-3 if needed.

---

## Backup & Recovery

### Backup Strategy

Since M3DP-UIP is **stateless**:
- No database to backup
- No persistent data to restore
- All state in application code (git) or read-only CSV files

**What to backup:**
- GitHub repository (version control)
- `.env` file (environment variables) - **Store separately, never in git**
- Custom CSV data (if modified)

### Disaster Recovery

If production goes down:

```bash
# 1. Stop current deployment
#    (In Railway: Go to Deployments, click "Stop")

# 2. Check logs for error
#    (In Railway: Click "Logs")

# 3. Fix issue in code
git add .
git commit -m "fix: correct calculation error"
git push origin refactor/v2-lean

# 4. Railway automatically redeploys
#    (Monitor in Railway dashboard)

# 5. Verify new deployment
curl https://minimal3dp.com/health
```

**Typical recovery time:** 3-5 minutes

---

## Performance Tuning

### Cold Starts

First request after deployment may be slow (5-10s):
- Uvicorn initializes
- Jinja2 templates compile
- CSV files load into memory

Subsequent requests: ~10-20ms

**To minimize cold start impact:**
1. Pre-warm cache (optional)
2. Use larger instance during peak usage
3. Monitor cold start performance in metrics

### Request Performance

**Typical request breakdown:**
- Validation: 1ms
- Calculation: 0.5ms
- Template rendering: 5ms
- Network overhead: 2-5ms
- **Total: 10-15ms**

**Throughput:** ~100-200 requests/second per instance

**To improve performance:**
1. Enable response caching (if implemented)
2. Use CDN for static files
3. Add more instances (horizontal scaling)

### Static File Optimization

TailwindCSS, HTMX, and Alpine.js are loaded from CDN in production:

```html
<!-- In base.html -->
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/htmx.org"></script>
<script src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
```

Benefits:
- Reduced server bandwidth
- Faster load times (cached globally)
- No server CPU used for CSS generation

---

## Security Best Practices

### 1. Environment Variables

**Never commit secrets to git:**

```bash
# ✅ Good
git add .gitignore  # Contains .env
git add pyproject.toml

# ❌ Bad
git add .env  # Contains secrets!
```

**Railway security:**
- Environment variables stored encrypted
- Only available at runtime
- Not visible in git history
- Accessible only to authorized users

### 2. CORS Configuration

**Production CORS:**

```env
ALLOWED_ORIGINS=https://minimal3dp.com,https://www.minimal3dp.com
```

**Not recommended in production:**
```env
ALLOWED_ORIGINS=*  # Allows any origin
```

### 3. HTTPS Only

Railway automatically provides HTTPS with Let's Encrypt:
- SSL certificate auto-renewed
- No manual configuration needed
- Redirects HTTP → HTTPS automatically

### 4. Regular Updates

Keep dependencies updated:

```bash
# Check for outdated packages
pip list --outdated

# Update pyproject.toml
# Then commit and push
git add pyproject.toml
git commit -m "chore: update dependencies"
git push
```

---

## Troubleshooting

### Deployment Fails

**Check logs:**
1. Go to Railway dashboard
2. Click "Logs" tab
3. Look for error messages

**Common issues:**

| Error | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError` | Missing dependency | Add to `pyproject.toml` and redeploy |
| `Port already in use` | Invalid port config | Use `$PORT` environment variable |
| `Segmentation fault` | Memory leak | Increase instance size, check code |
| `Connection timeout` | Health check failing | Check `/health` endpoint works |

### High Memory Usage

If memory usage exceeds limit:

1. **Check for memory leaks:**
   ```bash
   # In Railway logs, search for "MemoryError"
   ```

2. **Increase instance size:**
   - Go to project settings
   - Upgrade from 512MB → 1GB

3. **Optimize code:**
   - Profile memory usage
   - Check for large data structures

### Slow Requests

If requests are slow (> 100ms):

1. **Check CSV loading:**
   - CSV files cached after first load
   - First requests slower than subsequent

2. **Monitor instance CPU:**
   - If maxed out, scale up or add replicas

3. **Check network latency:**
   - Use browser DevTools Network tab
   - Check Railway metrics

### Custom Domain Not Working

If domain doesn't resolve:

1. **Check DNS propagation:**
   - Open https://whatsmydns.net
   - Search for your domain
   - Verify CNAME resolves to Railway

2. **Verify Railway configuration:**
   - Go to project settings → Domain
   - Confirm custom domain is set

3. **Wait for SSL certificate:**
   - Let's Encrypt can take 15+ minutes
   - Check status in Railway dashboard

4. **Flush DNS cache:**
   ```bash
   # macOS
   dscacheutil -flushcache
   
   # Linux
   sudo systemctl restart systemd-resolved
   
   # Windows
   ipconfig /flushdns
   ```

---

## Cost Optimization

### Free Tier

Railway offers free tier for prototyping:
- 1 Starter instance (shared CPU, 512MB RAM)
- 1GB bandwidth/month
- Limitations: Shared resources, ~30 minute inactivity timeout

**Cost:** Free

### Pro Tier

For production workloads:

| Usage | Est. Cost/Month |
|-------|-----------------|
| 1 Pro Small instance | $5 |
| + 1 replica (2 instances) | $10 |
| + Custom domain | Included |
| + Custom SSL cert | Included |

**Compared to alternatives:**
- Heroku: $50-100/month
- AWS EC2: $10-30/month (but requires ops overhead)
- DigitalOcean: $5-12/month

### Optimization Tips

1. **Start small** - Use Starter tier initially
2. **Monitor metrics** - Only scale when needed
3. **Combine resources** - Run multiple projects on one instance
4. **Use free tier for dev** - Separate branch for testing

---

## Monitoring Production

### Weekly Checks

- [ ] Check logs for errors
- [ ] Verify HTTPS certificate is valid
- [ ] Test calculator endpoints
- [ ] Check CPU/memory usage metrics
- [ ] Verify custom domain resolves

### Monthly Checks

- [ ] Update dependencies (`pip list --outdated`)
- [ ] Review cost analysis
- [ ] Check for security updates
- [ ] Backup `.env` configuration
- [ ] Test disaster recovery procedure

### Quarterly Checks

- [ ] Performance benchmarking
- [ ] Scalability assessment
- [ ] Security audit
- [ ] Feature roadmap review
- [ ] User feedback analysis

---

## Advanced Configuration

### Custom Start Command

If you need a different start command, edit in Railway:

```bash
# Default
uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT

# With logging
uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT --log-level info

# With workers (not needed for stateless app)
gunicorn -w 4 -b 0.0.0.0:$PORT backend.app.main:app
```

### Environment-Specific Configuration

In `backend/app/core/config.py`:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENVIRONMENT: str = "development"
    DEBUG: bool = False
    LOG_LEVEL: str = "info"
    ALLOWED_ORIGINS: str = "*"
    
    # Auto-load from .env (development) or environment variables (production)
    model_config = SettingsConfigDict(env_file=".env")
```

### Webhook Integration (Optional)

Set up Railway webhooks for notifications:

1. Go to project settings
2. Click "Integrations"
3. Add webhook for Slack, Discord, or custom endpoint
4. Receive deployment status notifications

---

## Related Documentation

- [Architecture Guide](../ARCHITECTURE.md) - System design
- [API Documentation](../API.md) - Endpoint reference
- [Development Setup](../development/SETUP.md) - Local development
- [Contributing Guide](../../CONTRIBUTING.md) - Contribution workflow

---

## Support

For deployment issues:
1. Check Railway dashboard Logs
2. Review Troubleshooting section above
3. Check Railway status: https://railway.app/status
4. Open issue: https://github.com/minimal3dp/m3dp-uip/issues

---

## Next Steps

1. **Set up production monitoring**
   - Email alerts for errors
   - Slack notifications for deployments

2. **Configure custom domain**
   - Point DNS to Railway
   - Verify HTTPS certificate

3. **Monitor metrics**
   - Set baseline for CPU/memory
   - Plan scaling triggers

4. **Plan scaling**
   - When to upgrade instance size
   - When to add replicas
   - When to use CDN

5. **Document runbooks**
   - Emergency contact procedures
   - Rollback procedures
   - On-call rotation
