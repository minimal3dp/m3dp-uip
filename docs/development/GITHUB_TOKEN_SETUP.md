# GitHub Token Setup for CI Workflows

## Problem

GitHub Actions workflows are failing with 404 errors when attempting to:
- Create branches and pull requests programmatically
- Push badge updates (coverage-badge.svg) to the main branch

## Solution: Configure Personal Access Token

### Step 1: Create a GitHub Personal Access Token

#### Option 1: Fine-Grained Token (Recommended - More Secure)

1. Navigate to: [GitHub Settings → Developer settings → Personal access tokens → Fine-grained tokens](https://github.com/settings/tokens?type=beta)
2. Click **"Generate new token"**
3. Configure:
   - **Token name**: `m3dp-uip-ci-workflows`
   - **Expiration**: 90 days (or custom duration)
   - **Repository access**: Select "Only select repositories" → `minimal3dp/m3dp-uip`
   - **Permissions**:
     - **Repository permissions**:
       - Contents: **Read and write** (required for badge commits)
       - Pull requests: **Read and write** (required for PR creation)
       - Actions: **Read and write** (required for workflow triggers)
       - Commit statuses: **Read and write** (optional, for status checks)
4. Click **"Generate token"**
5. **Copy the token immediately** (you won't see it again)

#### Option 2: Classic Token (Simpler but Broader Access)

1. Navigate to: [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Click **"Generate new token (classic)"**
3. Configure:
   - **Note**: `m3dp-uip-ci-workflows`
   - **Expiration**: 90 days (or custom duration)
   - **Select scopes**:
     - ✅ `repo` (Full control of private repositories)
     - ✅ `workflow` (Update GitHub Action workflows)
4. Click **"Generate token"**
5. **Copy the token immediately**

### Step 2: Configure Token in Your Environment

#### For VS Code / Terminal Sessions

**Temporary (current session only)**:
```bash
export GITHUB_TOKEN=ghp_yourTokenHere
```

**Persistent (recommended)**:
```bash
# Add to your shell profile (~/.zshrc for zsh)
echo 'export GITHUB_TOKEN=ghp_yourTokenHere' >> ~/.zshrc

# Reload your shell
source ~/.zshrc
```

**Restart VS Code** after setting the environment variable to ensure tools pick up the token.

#### Alternative: GitHub CLI

If you have `gh` installed:
```bash
# Login with repo and workflow scopes
gh auth login

# Verify authentication
gh auth status
```

Many GitHub tools will automatically use `gh` credentials.

### Step 3: Enable Workflow Permissions

1. Go to: [Repository Settings → Actions → General](https://github.com/minimal3dp/m3dp-uip/settings/actions)
2. Scroll to **"Workflow permissions"**
3. Select: **"Read and write permissions"**
4. Check: **"Allow GitHub Actions to create and approve pull requests"** (if needed)
5. Click **"Save"**

### Step 4: Handle Protected Branch (if main is protected)

If `main` branch has protection rules:

**Option A: Allow GitHub Actions to bypass**
- Go to: Branch protection rules for `main`
- Under "Allow specified actors to bypass required pull requests"
- Add: **GitHub Actions**

**Option B: Exclude badge files from protection**
- Configure branch protection to allow commits to:
  - `coverage-badge.svg`


**Option C: Push badges to separate branch**
- Modify workflows to push badges to `badges` branch
- Serve badges from that branch instead of `main`

### Step 5: Verify Setup

After configuring the token, test by running:

```bash
# From the repository root
gh api user
# Should show your GitHub user info

# Test repository access
gh repo view minimal3dp/m3dp-uip
# Should show repository details
```

## Next Steps

Once the token is configured:

1. **Retry the CI workflow fixes**:
   - Create branch `ci/guards-and-badge-updates`
   - Push workflow updates that guard jobs when backend directory is missing
   - Open a PR with these changes

2. **Monitor Actions**:
   - Verify CI Pipeline passes
   - Verify Coverage Badge generates successfully
   - Verify Coverage Badge generates successfully

## Security Best Practices

- ✅ Use fine-grained tokens when possible (least privilege)
- ✅ Set token expiration (90 days or less)
- ✅ Store tokens in environment variables, never commit to repository
- ✅ Rotate tokens regularly
- ✅ Revoke tokens immediately if compromised
- ❌ Never share tokens in chat, email, or public forums
- ❌ Never commit tokens to `.env` files without adding them to `.gitignore`

## Troubleshooting

### 404 Errors Persist

- Verify token has `repo` scope (classic) or `contents:write` (fine-grained)
- Ensure token is granted to the specific repository (fine-grained tokens)
- Check token hasn't expired
- Restart VS Code after setting environment variable

### Badge Commits Fail

- Verify "Read and write permissions" are enabled for workflows
- Check if `main` branch protection is blocking GitHub Actions
- Review workflow logs for specific error messages

### Token Not Found

```bash
# Verify environment variable is set
echo $GITHUB_TOKEN

# Should output your token (ghp_...)
# If empty, token is not configured
```

## Resources

- [GitHub: Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [GitHub: Automatic token authentication](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)
- [GitHub CLI documentation](https://cli.github.com/manual/)
