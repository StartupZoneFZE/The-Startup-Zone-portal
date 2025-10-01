# Reset Supabase Database Password

## Steps to Reset Password:

1. Go to your Supabase Dashboard: https://supabase.com/dashboard/project/iutmcoftuakkuabghrlu

2. Click on **Settings** (gear icon) in the sidebar

3. Click on **Database** in the left menu

4. Look for **Database Password** section

5. Click **Reset Database Password**

6. Set a NEW password WITHOUT special characters:
   ```
   TSZPortal2024Secure
   ```
   (No @ # ! symbols - just letters and numbers)

7. Click **Reset Password**

8. Wait 1-2 minutes for the password to update

## After Reset:

Once you've reset the password, tell me and I'll update our connection strings.

The new connection string will be:
```
postgresql://postgres.iutmcoftuakkuabghrlu:TSZPortal2024Secure@aws-0-ap-south-1.pooler.supabase.com:6543/postgres
```

## Important Notes:
- This password is only for database connections
- Your Supabase dashboard login remains the same
- The API keys remain unchanged
- This only affects direct database connections (Prisma)