# GitHub Actions Secrets Setup

## Add these secrets to your GitHub repository:

### Steps:
1. Go to: https://github.com/StartupZoneFZE/The-Startup-Zone-License-PRO-Ops-Portal
2. Click **Settings** tab
3. Click **Secrets and variables** → **Actions** (left sidebar)
4. Click **New repository secret** for each secret below

### Secrets to Add:

#### 1. DATABASE_URL
**Name:** `DATABASE_URL`
**Value:**
```
postgresql://postgres.iutmcoftuakkuabghrlu:TSZPortal2024Secure@aws-1-ap-south-1.pooler.supabase.com:6543/postgres?pgbouncer=true
```

#### 2. DIRECT_URL
**Name:** `DIRECT_URL`
**Value:**
```
postgresql://postgres.iutmcoftuakkuabghrlu:TSZPortal2024Secure@aws-1-ap-south-1.pooler.supabase.com:5432/postgres
```

#### 3. NEXT_PUBLIC_SUPABASE_URL
**Name:** `NEXT_PUBLIC_SUPABASE_URL`
**Value:**
```
https://iutmcoftuakkuabghrlu.supabase.co
```

#### 4. NEXT_PUBLIC_SUPABASE_ANON_KEY
**Name:** `NEXT_PUBLIC_SUPABASE_ANON_KEY`
**Value:**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml1dG1jb2Z0dWFra3VhYmdocmx1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTkyOTQ0NzgsImV4cCI6MjA3NDg3MDQ3OH0.P9OCrF-x8YCNCRMJdq81vWLHOikbYgZ2c5GnKp39apE
```

#### 5. SUPABASE_SERVICE_ROLE_KEY
**Name:** `SUPABASE_SERVICE_ROLE_KEY`
**Value:**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml1dG1jb2Z0dWFra3VhYmdocmx1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1OTI5NDQ3OCwiZXhwIjoyMDc0ODcwNDc4fQ.PJTRoar1yzlrv_EXNkvt69c5CdoVwJR37ZqsYshsYjM
```

## After Adding All Secrets:
- GitHub Actions workflows will have access to these environment variables
- CI/CD pipeline can run database migrations
- Tests can connect to the database

## Verification:
After adding all secrets, you should see 5 repository secrets listed in the Actions secrets page.