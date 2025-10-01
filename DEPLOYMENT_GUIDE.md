# TSZ Portal Deployment Guide

## 1. GitHub Repository Setup ✅
- Create repository at https://github.com/new
- Name: `tsz-portal`
- Keep it private
- Don't initialize with any files

## 2. Push Code to GitHub
```bash
# Edit deploy-commands.sh and replace YOUR_USERNAME with your GitHub username
# Then run:
./deploy-commands.sh
```

## 3. Supabase Setup (Bahrain Region)

### Create Supabase Project:
1. Go to https://supabase.com/dashboard
2. Click "New Project"
3. **Project Settings:**
   - Name: `tsz-portal-dev`
   - Database Password: (save this securely!)
   - Region: **Bahrain (me-south-1)**
   - Pricing Plan: Free tier to start

### Get Credentials:
After creation, go to Settings > API and copy:
- `Project URL` → NEXT_PUBLIC_SUPABASE_URL
- `anon public` → NEXT_PUBLIC_SUPABASE_ANON_KEY  
- `service_role` → SUPABASE_SERVICE_ROLE_KEY

### Database URL:
Settings > Database:
- `Connection string` → DATABASE_URL
- `Connection pooling` → DATABASE_URL (for production)
- `Direct connection` → DIRECT_URL

### Run Migrations:
```bash
# In packages/database directory
cd packages/database

# Set environment variables
export DATABASE_URL="your-database-url"
export DIRECT_URL="your-direct-url"

# Run migrations
pnpm prisma migrate deploy

# Seed database (optional, for test data)
pnpm db:seed
```

### Apply RLS Policies:
1. Go to Supabase Dashboard > SQL Editor
2. Open `/packages/database/prisma/migrations/rls_policies.sql`
3. Copy and paste the entire content
4. Click "Run"

## 4. Vercel Deployment

### Import Repository:
1. Go to https://vercel.com/new
2. Import Git Repository → Select `tsz-portal`
3. Configure Project:
   - Framework: Next.js
   - Root Directory: `apps/web`
   - Build Command: `cd ../.. && pnpm install && pnpm build`
   - Output Directory: `.next`

### Environment Variables:
Add these in Vercel project settings:

```env
# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://[project-ref].supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...
SUPABASE_SERVICE_ROLE_KEY=eyJ...

# Database
DATABASE_URL=postgresql://postgres:[password]@db.[project-ref].supabase.co:5432/postgres
DIRECT_URL=postgresql://postgres:[password]@db.[project-ref].supabase.co:5432/postgres

# App
NEXT_PUBLIC_APP_URL=https://your-app.vercel.app
```

### Deploy:
1. Click "Deploy"
2. Wait for build to complete
3. Visit the preview URL

## 5. GitHub Actions Secrets

Go to: https://github.com/YOUR_USERNAME/tsz-portal/settings/secrets/actions

Add these repository secrets:
```
SUPABASE_ACCESS_TOKEN    # From Supabase dashboard
SUPABASE_DB_PASSWORD     # Database password
SUPABASE_PROJECT_ID      # Project reference ID
DATABASE_URL             # PostgreSQL connection string
DIRECT_URL               # Direct connection string
NEXT_PUBLIC_SUPABASE_URL # Supabase project URL
NEXT_PUBLIC_SUPABASE_ANON_KEY # Anonymous key
SUPABASE_SERVICE_ROLE_KEY # Service role key
VERCEL_TOKEN             # From Vercel account settings
VERCEL_ORG_ID            # From Vercel project settings
VERCEL_PROJECT_ID        # From Vercel project settings
```

### Get Vercel Tokens:
1. **VERCEL_TOKEN**: 
   - Go to https://vercel.com/account/tokens
   - Create new token with full scope

2. **VERCEL_ORG_ID & VERCEL_PROJECT_ID**:
   - Go to your Vercel project settings
   - Find in General > Project ID
   - Find Team ID (if applicable)

## 6. Verify Deployment

### Check GitHub Actions:
1. Go to repository > Actions tab
2. CI/CD Pipeline should run automatically
3. Check for green checkmarks

### Test Preview URLs:
1. Create a pull request
2. Vercel bot will comment with preview URL
3. Test the application

### Production Deployment:
When ready for production:
```bash
git tag -a v1.0.0 -m "Initial release"
git push origin v1.0.0
```

## 7. Post-Deployment

### Monitor:
- Supabase Dashboard for database metrics
- Vercel Dashboard for deployment logs
- GitHub Actions for CI/CD status

### Set up Domains:
1. In Vercel project settings > Domains
2. Add your custom domain
3. Configure DNS records

## Troubleshooting

### Database Connection Issues:
- Check if Supabase project is active
- Verify connection strings
- Ensure RLS policies are applied

### Build Failures:
- Check GitHub Actions logs
- Verify environment variables
- Check Vercel build logs

### Authentication Issues:
- Verify Supabase keys
- Check CORS settings in Supabase
- Ensure middleware is configured

## Support

For issues:
- Check GitHub Actions logs
- Review Vercel deployment logs
- Check Supabase logs
- Create issue in GitHub repository