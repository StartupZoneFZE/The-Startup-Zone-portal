# Vercel Environment Variables Setup

## Add these in Vercel Dashboard → Settings → Environment Variables

### 1. Public Variables (Available in Browser)

**NEXT_PUBLIC_SUPABASE_URL**
```
https://iutmcoftuakkuabghrlu.supabase.co
```

**NEXT_PUBLIC_SUPABASE_ANON_KEY**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml1dG1jb2Z0dWFra3VhYmdocmx1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTkyOTQ0NzgsImV4cCI6MjA3NDg3MDQ3OH0.P9OCrF-x8YCNCRMJdq81vWLHOikbYgZ2c5GnKp39apE
```

### 2. Secret Variables (Server-side Only)

**DATABASE_URL**
```
postgresql://postgres.iutmcoftuakkuabghrlu:TSZ@Portal2024%23Secure!@aws-0-ap-south-1.pooler.supabase.com:6543/postgres?pgbouncer=true
```

**DIRECT_URL**
```
postgresql://postgres.iutmcoftuakkuabghrlu:TSZ@Portal2024%23Secure!@aws-0-ap-south-1.pooler.supabase.com:5432/postgres
```

**SUPABASE_SERVICE_ROLE_KEY**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml1dG1jb2Z0dWFra3VhYmdocmx1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1OTI5NDQ3OCwiZXhwIjoyMDc0ODcwNDc4fQ.PJTRoar1yzlrv_EXNkvt69c5CdoVwJR37ZqsYshsYjM
```

## How to Add in Vercel:

1. Go to your project in Vercel Dashboard
2. Click "Settings" tab
3. Click "Environment Variables" in left sidebar
4. For each variable:
   - Enter the Key (name) exactly as shown above
   - Paste the Value 
   - Select environments: Production, Preview, Development
   - Click "Save"

## Important Notes:
- The DATABASE_URL uses URL-encoded password (# becomes %23)
- Add all 5 variables one by one
- Make sure to include "NEXT_PUBLIC_" prefix for client-side variables
- Don't add quotes around the values when pasting

## Order to Add (to avoid issues):
1. First add NEXT_PUBLIC_SUPABASE_URL
2. Then add NEXT_PUBLIC_SUPABASE_ANON_KEY
3. Then add DATABASE_URL
4. Then add DIRECT_URL
5. Finally add SUPABASE_SERVICE_ROLE_KEY

After adding all variables, trigger a redeploy from the Deployments tab.