import { PrismaClient, UserRole, ServiceRequestCategory, ServiceRequestPriority, ServiceRequestStatus, StageKind, StageStatus, TaskStatus, PaymentMethod } from '@prisma/client'

const prisma = new PrismaClient()

async function main() {
  console.log('🌱 Starting seed...')

  // Create organization
  const org = await prisma.organization.create({
    data: {
      name: 'The Startup Zone',
      slug: 'tsz',
    },
  })
  console.log('✅ Created organization:', org.name)

  // Create users
  const adminUser = await prisma.user.create({
    data: {
      id: 'admin-user-id',
      email: 'admin@thestartupzone.ae',
      name: 'Admin User',
      role: UserRole.ADMIN,
      organizationId: org.id,
    },
  })

  const staffUser = await prisma.user.create({
    data: {
      id: 'staff-user-id',
      email: 'staff@thestartupzone.ae',
      name: 'Staff Member',
      role: UserRole.STAFF,
      organizationId: org.id,
    },
  })

  const clientUser = await prisma.user.create({
    data: {
      id: 'client-user-id',
      email: 'client@example.com',
      name: 'John Client',
      role: UserRole.CLIENT,
      organizationId: null,
    },
  })
  console.log('✅ Created users')

  // Create clients
  const client1 = await prisma.client.create({
    data: {
      name: 'ABC Trading LLC',
      email: 'contact@abctrading.ae',
      phone: '+971501234567',
      companyName: 'ABC Trading LLC',
      tradeLicense: 'TL-2024-001',
      emiratesId: '784-1990-1234567-1',
      organizationId: org.id,
    },
  })

  const client2 = await prisma.client.create({
    data: {
      name: 'XYZ Consulting',
      email: 'info@xyzconsulting.ae',
      phone: '+971507654321',
      companyName: 'XYZ Consulting FZ-LLC',
      tradeLicense: 'TL-2024-002',
      organizationId: org.id,
    },
  })
  console.log('✅ Created clients')

  // Create service requests
  const serviceRequest1 = await prisma.serviceRequest.create({
    data: {
      title: 'New Trade License Application',
      description: 'Apply for new trade license in Dubai mainland',
      category: ServiceRequestCategory.LICENSE_NEW,
      priority: ServiceRequestPriority.HIGH,
      status: ServiceRequestStatus.IN_PROGRESS,
      clientId: client1.id,
      assigneeId: staffUser.id,
      createdById: adminUser.id,
      organizationId: org.id,
      dueDate: new Date('2024-02-15'),
      stages: {
        create: [
          {
            kind: StageKind.PAYMENT_PENDING,
            status: StageStatus.COMPLETED,
            startedAt: new Date('2024-01-01'),
            completedAt: new Date('2024-01-03'),
          },
          {
            kind: StageKind.DOCUMENTS_COLLECTION,
            status: StageStatus.IN_PROGRESS,
            startedAt: new Date('2024-01-04'),
          },
          {
            kind: StageKind.SUBMISSION_PREP,
            status: StageStatus.NOT_STARTED,
          },
        ],
      },
      tasks: {
        create: [
          {
            title: 'Collect passport copies',
            description: 'Get passport copies for all shareholders',
            status: TaskStatus.COMPLETED,
            assigneeId: staffUser.id,
            completedAt: new Date('2024-01-05'),
          },
          {
            title: 'Prepare MOA documents',
            description: 'Draft memorandum of association',
            status: TaskStatus.IN_PROGRESS,
            assigneeId: staffUser.id,
            dueAt: new Date('2024-01-20'),
          },
        ],
      },
      payments: {
        create: [
          {
            amount: 5000.00,
            currency: 'AED',
            method: PaymentMethod.BANK_TRANSFER,
            reference: 'TRF-2024-001',
            paidAt: new Date('2024-01-03'),
            notes: 'Initial deposit for license application',
          },
        ],
      },
    },
  })

  const serviceRequest2 = await prisma.serviceRequest.create({
    data: {
      title: 'License Renewal - XYZ Consulting',
      description: 'Annual license renewal',
      category: ServiceRequestCategory.LICENSE_RENEWAL,
      priority: ServiceRequestPriority.MEDIUM,
      status: ServiceRequestStatus.SUBMITTED,
      clientId: client2.id,
      assigneeId: staffUser.id,
      createdById: staffUser.id,
      organizationId: org.id,
      dueDate: new Date('2024-03-01'),
      stages: {
        create: [
          {
            kind: StageKind.PAYMENT_PENDING,
            status: StageStatus.NOT_STARTED,
          },
        ],
      },
    },
  })

  const serviceRequest3 = await prisma.serviceRequest.create({
    data: {
      title: 'PRO Services - Visa Processing',
      description: 'Process employment visa for 3 employees',
      category: ServiceRequestCategory.PRO_SERVICE,
      priority: ServiceRequestPriority.URGENT,
      status: ServiceRequestStatus.IN_PROGRESS,
      clientId: client1.id,
      assigneeId: staffUser.id,
      createdById: adminUser.id,
      organizationId: org.id,
      dueDate: new Date('2024-01-31'),
      stages: {
        create: [
          {
            kind: StageKind.IMMIGRATION_PROCESS,
            status: StageStatus.IN_PROGRESS,
            startedAt: new Date('2024-01-10'),
          },
          {
            kind: StageKind.MEDICAL_FITNESS,
            status: StageStatus.NOT_STARTED,
          },
          {
            kind: StageKind.EMIRATES_ID,
            status: StageStatus.NOT_STARTED,
          },
        ],
      },
    },
  })
  console.log('✅ Created service requests with stages, tasks, and payments')

  // Create documents
  await prisma.document.create({
    data: {
      filename: 'trade_license_application.pdf',
      storagePath: 'documents/sr1/trade_license_application.pdf',
      mimeType: 'application/pdf',
      size: 1024000,
      ownerType: 'service_request',
      ownerId: serviceRequest1.id,
      serviceRequestId: serviceRequest1.id,
      uploadedById: staffUser.id,
      organizationId: org.id,
      tags: ['license', 'application'],
    },
  })

  await prisma.document.create({
    data: {
      filename: 'passport_copy.pdf',
      storagePath: 'documents/clients/client1/passport_copy.pdf',
      mimeType: 'application/pdf',
      size: 512000,
      ownerType: 'client',
      ownerId: client1.id,
      clientId: client1.id,
      uploadedById: adminUser.id,
      organizationId: org.id,
      tags: ['identity', 'passport'],
    },
  })
  console.log('✅ Created documents')

  // Create notes
  await prisma.note.create({
    data: {
      body: 'Client requested expedited processing',
      ownerType: 'service_request',
      ownerId: serviceRequest1.id,
      serviceRequestId: serviceRequest1.id,
      createdById: staffUser.id,
      organizationId: org.id,
    },
  })
  console.log('✅ Created notes')

  console.log('🎉 Seed completed successfully!')
}

main()
  .catch((e) => {
    console.error('❌ Seed failed:', e)
    process.exit(1)
  })
  .finally(async () => {
    await prisma.$disconnect()
  })