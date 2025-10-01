# TSZ Portal Deployment Checklist

## Phase 1: GitHub Setup ⏳

### Pre-requisites
- [x] GitHub account created
- [x] GitHub username: StartupZoneFZE
- [ ] Git configured locally

### Repository Creation
- [x] Logged into GitHub
- [x] Created new repository named "The-Startup-Zone-License-PRO-Ops-Portal"
- [x] Set as Private repository
- [x] Did NOT initialize with any files
- [x] Copied repository URL

### Local Git Setup
- [x] Opened Terminal in project directory
- [x] Added remote origin
- [x] Set branch to main
- [x] Pushed code successfully
- [x] Verified files appear on GitHub

---

## Phase 2: Supabase Setup 🔄

### Account Setup
- [ ] Supabase account created
- [ ] Logged into dashboard

### Project Creation
- [ ] Created new project
- [ ] Project name: tsz-portal-dev
- [ ] Region: Bahrain (me-south-1)
- [ ] Database password saved: ________________

### Credentials Collection
- [ ] Project URL copied
- [ ] Anon key copied
- [ ] Service role key copied
- [ ] Database URL copied
- [ ] Direct URL copied

### Database Setup
- [ ] Migrations run successfully
- [ ] RLS policies applied
- [ ] Seed data loaded (optional)

---

## Phase 3: Vercel Setup 🔄

### Account & Import
- [ ] Vercel account created
- [ ] GitHub repository imported
- [ ] Project name confirmed

### Configuration
- [ ] Root directory set to: apps/web
- [ ] Build command configured
- [ ] Environment variables added
- [ ] Deploy triggered

### Verification
- [ ] Build successful
- [ ] Preview URL working
- [ ] Application loads correctly

---

## Phase 4: GitHub Actions Setup 🔄

### Secrets Configuration
- [ ] SUPABASE_ACCESS_TOKEN added
- [ ] SUPABASE_DB_PASSWORD added
- [ ] SUPABASE_PROJECT_ID added
- [ ] DATABASE_URL added
- [ ] DIRECT_URL added
- [ ] NEXT_PUBLIC_SUPABASE_URL added
- [ ] NEXT_PUBLIC_SUPABASE_ANON_KEY added
- [ ] SUPABASE_SERVICE_ROLE_KEY added
- [ ] VERCEL_TOKEN added
- [ ] VERCEL_ORG_ID added
- [ ] VERCEL_PROJECT_ID added

### Pipeline Verification
- [ ] GitHub Actions running
- [ ] All checks passing
- [ ] Preview deployments working

---

## Phase 5: Final Testing 🔄

- [ ] Application accessible
- [ ] Database connected
- [ ] Authentication working
- [ ] Service Requests page loads
- [ ] Create modal works
- [ ] Data persists

---

## Credentials Storage

### GitHub
- Username: ________________
- Repository: https://github.com/________/tsz-portal

### Supabase
- Project URL: ________________
- Anon Key: ________________
- Service Role Key: ________________
- Database Password: ________________

### Vercel
- Project URL: ________________
- Deploy Hook: ________________

---

## Issues/Notes
_Document any problems or important notes here_

- 
- 
- 

---

Last Updated: [Date/Time]
Status: IN PROGRESS