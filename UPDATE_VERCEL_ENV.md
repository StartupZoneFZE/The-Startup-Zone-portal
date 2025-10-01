# Update Vercel Environment Variables

## Go to Vercel Dashboard → Settings → Environment Variables

Update these two variables with the CORRECT connection strings:

### DATABASE_URL
```
postgresql://postgres.iutmcoftuakkuabghrlu:TSZPortal2024Secure@aws-1-ap-south-1.pooler.supabase.com:6543/postgres?pgbouncer=true
```

### DIRECT_URL  
```
postgresql://postgres.iutmcoftuakkuabghrlu:TSZPortal2024Secure@aws-1-ap-south-1.pooler.supabase.com:5432/postgres
```

## Steps:
1. Go to your Vercel project settings
2. Click on Environment Variables
3. Find DATABASE_URL and click the three dots → Edit
4. Replace with the new value above
5. Save
6. Find DIRECT_URL and click the three dots → Edit  
7. Replace with the new value above
8. Save
9. Go to Deployments tab
10. Click the three dots on the latest deployment → Redeploy

## What Changed:
- Fixed the AWS region: `aws-1-ap-south-1` (not aws-0)
- Updated password to: `TSZPortal2024Secure` (no special characters)

## Success!
✅ Database tables are now created in Supabase
✅ Prisma schema is synced
✅ Ready for the application to connect