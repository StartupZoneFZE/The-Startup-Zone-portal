# TSZ License & PRO Ops Portal

Internal operations portal for The Startup Zone to manage license applications, PRO services, and client operations.

## Tech Stack

- **Frontend**: Next.js 15 (App Router), TypeScript, Tailwind CSS, shadcn/ui
- **Backend**: Next.js Route Handlers, Prisma ORM
- **Database**: Supabase (PostgreSQL with RLS)
- **Authentication**: Supabase Auth
- **Storage**: Supabase Storage
- **Deployment**: Vercel (with GitHub Actions CI/CD)
- **Testing**: Playwright (E2E), Vitest (Unit)

## Project Structure

```
tsz-portal/
├── apps/
│   └── web/                 # Next.js application
├── packages/
│   ├── database/            # Prisma schema & migrations
│   ├── ui/                  # Shared UI components
│   └── config/              # Shared configurations
├── .github/
│   └── workflows/           # CI/CD pipelines
└── tasks/
    └── todo.md              # Development tasks tracking
```

## Features

### Phase 1 (Current)
- ✅ Service Requests management (CRUD)
- ✅ License & Stage tracking
- ✅ Client management
- ✅ Document vault with tagging
- ✅ Task management on requests
- ✅ Payment logging
- ✅ Renewal pipeline
- ✅ Role-based access control (Admin/Staff/Client)

### Phase 2 (Planned)
- [ ] OCR for document processing
- [ ] Advanced reporting & analytics
- [ ] Email notifications
- [ ] WhatsApp integration
- [ ] Client portal
- [ ] Advanced search & filtering

## Environment Setup

### Prerequisites

- Node.js 20+
- pnpm 8+
- Supabase account
- Vercel account
- GitHub account

### Environment Variables

Create `.env.local` in `apps/web/`:

```bash
# Supabase
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key

# Database
DATABASE_URL=postgresql://...
DIRECT_URL=postgresql://...

# App
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

### Local Development

```bash
# Install dependencies
pnpm install

# Set up database
cd packages/database
pnpm prisma migrate dev
pnpm prisma db seed

# Start development server
pnpm dev

# Open http://localhost:3000
```

## Database Schema

Key entities:
- **Organizations**: Multi-tenant support
- **Users**: Admin, Staff, Client roles
- **Service Requests**: Main workflow entity
- **Stages**: Track progress through license process
- **Documents**: File attachments with tags
- **Tasks**: Subtasks on service requests
- **Payments**: Payment tracking
- **Renewals**: License renewal management

### Row Level Security (RLS)

All tables have RLS enabled:
- Admins: Full access
- Staff: Access within their organization
- Clients: Access only their own data

## Deployment

### Environments

1. **Development**: `tsz-dev` (Supabase), PR previews (Vercel)
2. **Staging**: `tsz-staging` (Supabase), `main` branch (Vercel)
3. **Production**: `tsz-prod` (Supabase), tagged releases (Vercel)

### CI/CD Pipeline

On PR:
1. Type checking & linting
2. Database migration to dev
3. Deploy preview to Vercel
4. Run E2E tests against preview
5. Check accessibility from Middle East

On merge to main:
1. Deploy to staging
2. Run full test suite
3. Manual approval for production

### Deployment Commands

```bash
# Deploy to Vercel (handled by CI)
vercel

# Apply database migrations
pnpm prisma migrate deploy

# Seed database (dev only)
pnpm db:seed
```

## Testing

### E2E Tests

```bash
# Run E2E tests
pnpm test:e2e

# Run with UI
pnpm test:e2e:ui
```

### Unit Tests

```bash
# Run unit tests
pnpm test
```

## API Routes

Key endpoints:
- `/api/service-requests` - Service request CRUD
- `/api/clients` - Client management
- `/api/documents` - Document upload/download
- `/api/auth` - Authentication endpoints

## Security

- Row Level Security (RLS) on all database tables
- JWT-based authentication via Supabase
- Service role key only in server-side code
- Rate limiting on write endpoints
- Input validation with Zod
- CORS configured for production domains

## Contributing

1. Create feature branch from `main`
2. Make changes following existing patterns
3. Update `tasks/todo.md` with progress
4. Create PR with description
5. Wait for CI checks to pass
6. Get code review approval
7. Merge to main

## Support

For issues or questions:
- Check `tasks/todo.md` for known issues
- Create GitHub issue
- Contact admin@thestartupzone.ae

## License

Private - The Startup Zone © 2024