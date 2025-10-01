# Supabase Credentials - TSZ Portal

## ⚠️ KEEP THIS FILE SECURE - DO NOT COMMIT TO GIT!

### Project Details
- **Project Name:** tsz-portal
- **Region:** Mumbai (ap-south-1)
- **Organization:** The Startup Zone

### Database Password
```
TSZ@Portal2024#Secure!
```

### API Credentials (Get from Settings → API)
```
# Project URL
NEXT_PUBLIC_SUPABASE_URL=https://iutmcoftuakkuabghrlu.supabase.co

# Anonymous Key (public)
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml1dG1jb2Z0dWFra3VhYmdocmx1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTkyOTQ0NzgsImV4cCI6MjA3NDg3MDQ3OH0.P9OCrF-x8YCNCRMJdq81vWLHOikbYgZ2c5GnKp39apE

# Service Role Key (secret - server only!)
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml1dG1jb2Z0dWFra3VhYmdocmx1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1OTI5NDQ3OCwiZXhwIjoyMDc0ODcwNDc4fQ.PJTRoar1yzlrv_EXNkvt69c5CdoVwJR37ZqsYshsYjM
```

### Database Connection (Get from Settings → Database)
```
# Connection String (Transaction Mode with Pooling)
DATABASE_URL=postgresql://postgres:TSZ@Portal2024#Secure!@db.iutmcoftuakkuabghrlu.supabase.co:6543/postgres?pgbouncer=true

# Direct Connection String
DIRECT_URL=postgresql://postgres:TSZ@Portal2024#Secure!@db.iutmcoftuakkuabghrlu.supabase.co:5432/postgres
```

### Project Reference
```
# Project Ref (from project URL)
SUPABASE_PROJECT_ID=

# JWT Secret (from Settings → API)
SUPABASE_JWT_SECRET=
```

---

## How to Get These Values:

1. **Wait for project to finish creating** (2-3 minutes)
2. Go to **Settings** (gear icon in sidebar)
3. Click **API** to get:
   - Project URL
   - anon key
   - service_role key
4. Click **Database** to get:
   - Connection strings

---

## Notes:
- Created: [Current Date/Time]
- Environment: Development
- Keep service_role key SECRET!