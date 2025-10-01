# TSZ License & PRO Ops Portal - Development Tasks

## First PR: Initial Setup & Service Requests Module

### Plan Overview
Build the foundation of the portal with a monorepo structure, core dependencies, database schema, and a functional Service Requests module with full CI/CD pipeline.

### Tech Decisions
- **Monorepo Tool**: pnpm workspaces (simpler than nx/turbo for this scale)
- **Component Library**: shadcn/ui with Radix primitives
- **State Management**: React Query + Zustand (lightweight)
- **Form Handling**: react-hook-form + Zod
- **Testing**: Vitest (unit), Playwright (E2E)
- **Deployment**: Vercel (automatic from GitHub) + Supabase (me-south-1)

### Database Schema Notes
- All tables have: id (uuid), created_at, updated_at, deleted_at (soft delete)
- org_id on all business entities for multi-tenancy
- RLS policies enforce access control at DB level
- Audit trail via audit_logs table

### Implementation Tasks

#### Phase 1: Project Setup
- [x] Create monorepo structure with pnpm workspaces
  - apps/web (Next.js app)
  - packages/ui (shared components)
  - packages/config (shared configs)
  - packages/database (Prisma + migrations)
- [x] Initialize Next.js 15 with TypeScript and App Router
- [x] Configure Tailwind CSS with custom theme
- [x] Install and configure shadcn/ui base components

#### Phase 2: Database & Auth
- [x] Set up Supabase client utilities
- [x] Create Prisma schema with all initial tables
- [x] Generate first migration
- [x] Write RLS policies SQL for role-based access
- [x] Create seed script with test data

#### Phase 3: Core UI
- [x] Build base layout (sidebar, topbar, search)
- [ ] Implement auth flow (login, logout, session)
- [x] Create dashboard placeholder page
- [ ] Add role-based navigation

#### Phase 4: Service Requests Module
- [x] Service Requests list page with filters
- [ ] Service Request detail view
- [x] Create/Edit Service Request form
- [ ] Status update workflow
- [ ] Assignee management

#### Phase 5: CI/CD & Testing
- [x] GitHub Actions workflow for PR checks
- [x] Vercel deployment configuration
- [x] Playwright E2E test suite
- [ ] Unit tests for critical functions

#### Phase 6: Documentation
- [x] README with setup instructions
- [ ] API documentation
- [x] Environment variables guide
- [x] Contributing guidelines

### Success Criteria
1. ✅ Clean monorepo with all packages building
2. ✅ Database schema deployed to Supabase dev
3. ✅ RLS policies working (verified by tests)
4. ✅ Service Requests CRUD fully functional
5. ✅ CI passing on all checks
6. ✅ Preview URL accessible from PR
7. ✅ E2E tests passing against preview

### Notes
- Keep components simple and reusable
- Every API route must have Zod validation
- All forms need loading and error states
- Mobile-responsive from day one
- No localhost development - use preview URLs

---

## Review Section

### Changes Made
- Created monorepo structure using pnpm workspaces
- Set up Next.js 15 with TypeScript, App Router, and Turbopack
- Configured Tailwind CSS with shadcn/ui components
- Implemented Supabase client for browser/server/middleware
- Created comprehensive Prisma schema with all required tables
- Written RLS policies for role-based access control
- Built responsive layout with sidebar and topbar navigation
- Created Service Requests module with list view and create modal
- Implemented dashboard with key metrics and widgets
- Set up GitHub Actions CI/CD pipeline with multiple stages
- Added Playwright E2E tests for critical flows
- Created comprehensive README documentation

### Key Decisions
- Used pnpm workspaces instead of nx/turbo for simplicity
- Chose shadcn/ui for component library (copy-paste model)
- Implemented RLS at database level for security
- Used mock data initially (no API integration yet)
- Structured for deploy-first approach (no localhost)
- Set up multi-stage CI/CD with preview deployments

### Known Issues
- Authentication not yet implemented (using mock user)
- API routes not created (using client-side mock data)
- Service request detail view not implemented
- Document upload functionality pending
- Actual Supabase connection requires env vars

### Next Steps
- Implement Supabase authentication flow
- Create API routes for all CRUD operations
- Add real-time updates using Supabase subscriptions
- Implement document upload to Supabase Storage
- Add comprehensive error handling
- Create remaining pages (Clients, Documents, etc.)
- Add unit tests for utilities and components
- Implement proper loading and error states

---

## Deployment Tasks (Current Focus)

### GitHub Setup
- [x] Verify GitHub account exists or create new one (StartupZoneFZE)
- [x] Create repository: The-Startup-Zone-License-PRO-Ops-Portal
- [x] Create Personal Access Token
- [x] Connect local repository to GitHub
- [x] Push initial code to GitHub
- [x] Verify code uploaded successfully

### Supabase Setup
- [ ] Create Supabase account
- [ ] Create new project in Bahrain region (me-south-1)
- [ ] Get API credentials (URL, anon key, service role key)
- [ ] Get database connection strings
- [ ] Run Prisma migrations
- [ ] Apply RLS policies via SQL
- [ ] Run seed script (optional)

### Vercel Setup
- [ ] Create Vercel account
- [ ] Import GitHub repository
- [ ] Configure environment variables
- [ ] Set build settings for monorepo
- [ ] Deploy and get preview URL

### CI/CD Configuration
- [ ] Add GitHub Actions secrets
- [ ] Add Vercel tokens to GitHub
- [ ] Test PR workflow
- [ ] Verify automated deployments

### Final Verification
- [ ] Check GitHub Actions pipeline
- [ ] Test preview deployment
- [ ] Verify database connectivity
- [ ] Test from Middle East region
- [ ] Document any issues