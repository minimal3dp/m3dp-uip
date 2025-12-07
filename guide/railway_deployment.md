# Deploying M3DP-UIP to Railway

This guide outlines the steps to deploy the *Minimal 3DP Unified Intelligence Platform* to [Railway.app](https://railway.app/).

## 1. Prerequisites

*   A [GitHub](https://github.com/) account with the `m3dp-uip` repository pushed.
*   A [Railway](https://railway.app/) account (Sign up with GitHub recommended).
*   **Affiliate Tags/Links**: Ensure `calculators.py` has the production affiliate links (done).

## 2. Project Configuration

The project is configured to use `pyproject.toml` and standard Python build tools. Railway will automatically detect the Python environment.

### Key Settings detected by Railway:
*   **Build System**: `hatchling` (via `pip install`)
*   **Python Version**: `3.12` (specified in `pyproject.toml`)
*   **Start Command**: We need to explicitly set this.

## 3. Deployment Steps

### Step 1: Create New Project
1.  Log in to the Railway Dashboard.
2.  Click **"New Project"**.
3.  Select **"Deploy from GitHub repo"**.
4.  Choose the `m3dp-uip` repository.
5.  Click **"Deploy Now"**.

### Step 2: Configure Environment Variables
*Once the project is created, go to the **Settings** or **Variables** tab for the service.*

Add the following variables:

| Variable | Value | Description |
| :--- | :--- | :--- |
| `ENVIRONMENT` | `production` | Enables production mode |
| `App_Name` | `M3DP-UIP` |  |
| `PORT` | `8000` | (Optional) Railway sets this automatically, but good to be explicit |
| `PAAPI_ASSOCIATE_TAG` | `mwf064-20` | Your Amazon Associate Tag |

*Note: You do not need `PAAPI_ACCESS_KEY` or `PAAPI_SECRET_KEY` yet as we are using direct links for now.*

### Step 3: Configure Build & Start Command
1.  Go to the **Settings** tab.
2.  Scroll to **Build** section.
3.  **Build Command**: Leave empty (Railway installs dependencies from `pyproject.toml` automatically).
4.  Scroll to **Deploy** section.
5.  **Start Command**: Enter the following:
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port $PORT
    ```
    *Note: The `$PORT` variable is injected by Railway.*

### Step 4: Verify Deployment
1.  Railway will trigger a re-deploy after setting variables/commands.
2.  Watch the **Deploy Logs**. You should see:
    *   `Installing dependencies...`
    *   `Uvicorn running on http://0.0.0.0:xxxx`
3.  Once "Active", click the generated **Public Domain** URL (e.g., `m3dp-uip-production.up.railway.app`).

## 4. Post-Deployment Checks
*   **Health Check**: Visit `/health` to verify status.
*   **Calculators**: Test the "Max Volumetric Speed" calculator and verify the Amazon link works.
*   **Assets**: Ensure CSS/JS load correctly (no 404s).

## 5. Troubleshooting

*   **"Module not found"**: Ensure the file structure in GitHub matches local (everything under `backend/app`?).
    *   *Correction*: The `pyproject.toml` defines `packages = ["backend/app"]`. If imports fail, try changing the Start Command to set python path:
        ```bash
        PYTHONPATH=backend uvicorn app.main:app --host 0.0.0.0 --port $PORT
        ```
*   **"Application Error"**: Check the logs. If it's a port issue, ensure `host` is `0.0.0.0` (not localhost).
