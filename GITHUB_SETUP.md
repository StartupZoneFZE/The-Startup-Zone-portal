# GitHub Repository Setup

## Option 1: Create Repository via GitHub Web Interface

1. Go to https://github.com/new
2. Repository name: `tsz-portal`
3. Description: "The Startup Zone License & PRO Ops Portal"
4. Choose: Private (recommended) or Public
5. Do NOT initialize with README, .gitignore, or license
6. Click "Create repository"

## Option 2: Install GitHub CLI and Create

```bash
# Install GitHub CLI on macOS
brew install gh

# Authenticate with GitHub
gh auth login

# Create the repository
gh repo create tsz-portal --private --description "The Startup Zone License & PRO Ops Portal"
```

## After Creating the Repository

Once the repository is created on GitHub, run these commands:

```bash
# Add the remote origin (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/tsz-portal.git

# Or if using SSH
git remote add origin git@github.com:YOUR_USERNAME/tsz-portal.git

# Push the code
git branch -M main
git push -u origin main
```

## Set up Secrets for GitHub Actions

Go to your repository Settings > Secrets and variables > Actions, and add:

- `SUPABASE_ACCESS_TOKEN`
- `SUPABASE_DB_PASSWORD`
- `SUPABASE_PROJECT_ID`
- `DATABASE_URL`
- `DIRECT_URL`
- `NEXT_PUBLIC_SUPABASE_URL`
- `NEXT_PUBLIC_SUPABASE_ANON_KEY`
- `SUPABASE_SERVICE_ROLE_KEY`
- `VERCEL_TOKEN`
- `VERCEL_ORG_ID`
- `VERCEL_PROJECT_ID`

## Vercel Setup

1. Go to https://vercel.com/new
2. Import your GitHub repository
3. Configure environment variables
4. Deploy

## Next Steps

After pushing to GitHub:
1. The CI/CD pipeline will automatically run
2. Check the Actions tab for build status
3. Review the PR preview URLs in pull requests
4. Monitor deployments in Vercel dashboard