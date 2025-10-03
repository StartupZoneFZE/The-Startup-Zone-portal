# Vercel Deployment Guide for TSZ Portal

## Step 1: Go to Vercel Dashboard
Visit: https://vercel.com/dashboard

## Step 2: Import Project
1. Click "Add New..." → "Project"
2. Import Git Repository
3. Select: `The-Startup-Zone-License-PRO-Ops-Portal`

## Step 3: Configure Project Settings

### Framework Preset
- Select: **Next.js**

### Root Directory
- Set to: `apps/web`

### Build and Output Settings
- **Build Command**: `cd ../.. && npm run build`
- **Output Directory**: `.next`
- **Install Command**: `cd ../.. && npm install`

### Environment Variables
Add the following environment variables:

```
DATABASE_URL=postgresql://postgres.iutmcoftuakkuabghrlu:TSZPortal2024Secure@aws-1-ap-south-1.pooler.supabase.com:6543/postgres?pgbouncer=true

DIRECT_URL=postgresql://postgres.iutmcoftuakkuabghrlu:TSZPortal2024Secure@aws-1-ap-south-1.pooler.supabase.com:5432/postgres

NEXT_PUBLIC_SUPABASE_URL=https://iutmcoftuakkuabghrlu.supabase.co

NEXT_PUBLIC_SUPABASE_ANON_KEY=[Get from Supabase dashboard → Settings → API]

SUPABASE_SERVICE_ROLE_KEY=[Get from Supabase dashboard → Settings → API]
```

## Step 4: Deploy
1. Click "Deploy" button
2. Wait for deployment to complete
3. Your app will be available at: `https://[your-project].vercel.app`

## Important Notes
- The project is already configured with `vercel.json` in `apps/web/`
- Database migrations are already applied
- Seed data has been added to the database
- The app is ready for production deployment

## Post-Deployment Checklist
- [ ] Verify the deployment URL works
- [ ] Check database connection
- [ ] Test the dashboard loads correctly
- [ ] Verify all pages render properly

## Deployment URL
Once deployed, update this with your URL:
- Production: `https://__________.vercel.app`