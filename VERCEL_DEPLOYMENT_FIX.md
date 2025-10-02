# Fix Vercel Deployment

## Option 1: Check Git Connection
1. Go to your Vercel project: https://vercel.com/startup-zone-fze-s-projects/tsz-portal
2. Click on **Settings** tab
3. Click on **Git** in the left sidebar
4. Check if your GitHub repo is connected:
   - Should show: `StartupZoneFZE/The-Startup-Zone-License-PRO-Ops-Portal`
   - If not connected, click "Connect Git Repository"

## Option 2: Manual Deployment via Vercel CLI
Run these commands in your terminal:

```bash
cd /Users/macbookpro/Desktop/Portal
npx vercel --prod
```

When prompted:
- Setup and deploy: Y
- Which scope: Choose your account
- Link to existing project: Y
- Project name: tsz-portal
- Directory: ./apps/web

## Option 3: Redeploy from Vercel Dashboard
1. Go to: https://vercel.com/startup-zone-fze-s-projects/tsz-portal
2. Look for a "Deploy" or "Create Deployment" button
3. Or go to Settings → Git → Click "Deploy Hook" or "Create Deploy"

## Option 4: Import Project Again
If nothing works:
1. Go to: https://vercel.com/new
2. Import Git Repository
3. Select: `StartupZoneFZE/The-Startup-Zone-License-PRO-Ops-Portal`
4. Configure:
   - Root Directory: `apps/web`
   - Build Command: `cd ../.. && npm run build`
   - Install Command: `cd ../.. && npm install`

## Check These Settings:
In Settings → General:
- Root Directory: Should be `apps/web` or `apps`
- Framework Preset: Next.js
- Node.js Version: 18.x or 20.x

In Settings → Environment Variables:
- All 5 variables should be present

Let me know which option works!