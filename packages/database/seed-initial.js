const { PrismaClient } = require('@prisma/client');
const crypto = require('crypto');

const prisma = new PrismaClient();

async function seedInitialData() {
  console.log('🌱 Seeding initial data...\n');

  try {
    // 1. Create default organization
    console.log('Creating organization...');
    const org = await prisma.organization.create({
      data: {
        name: 'The Startup Zone FZE',
        slug: 'tsz-fze'
      }
    });
    console.log('✅ Organization created:', org.name);

    // 2. Create admin user
    console.log('\nCreating admin user...');
    const adminUser = await prisma.user.create({
      data: {
        email: 'admin@startupzone.ae',
        name: 'Admin User',
        role: 'ADMIN',
        organization: {
          connect: { id: org.id }
        },
        authId: crypto.randomUUID(), // This will be replaced by Supabase Auth ID
      }
    });
    console.log('✅ Admin user created:', adminUser.email);

    // 3. Create staff users
    console.log('\nCreating staff users...');
    const staffUsers = await Promise.all([
      prisma.user.create({
        data: {
          email: 'john@startupzone.ae',
          name: 'John Smith',
          role: 'STAFF',
          organization: { connect: { id: org.id } },
          authId: crypto.randomUUID(),
        }
      }),
      prisma.user.create({
        data: {
          email: 'sarah@startupzone.ae',
          name: 'Sarah Johnson',
          role: 'STAFF',
          organization: { connect: { id: org.id } },
          authId: crypto.randomUUID(),
        }
      })
    ]);
    console.log('✅ Staff users created:', staffUsers.map(u => u.email).join(', '));

    // 4. Create sample clients
    console.log('\nCreating sample clients...');
    const clients = await Promise.all([
      prisma.client.create({
        data: {
          name: 'Tech Innovators LLC',
          email: 'contact@techinnovators.ae',
          phone: '+971501234567',
          address: 'Business Bay, Dubai',
          trn: 'TRN123456789',
          tradeLicenseNumber: 'TL-2024-001',
          tradeLicenseExpiry: new Date('2025-12-31'),
          organization: { connect: { id: org.id } },
        }
      }),
      prisma.client.create({
        data: {
          name: 'Digital Solutions FZ',
          email: 'info@digitalsolutions.ae',
          phone: '+971502345678',
          address: 'DIFC, Dubai',
          trn: 'TRN987654321',
          tradeLicenseNumber: 'TL-2024-002',
          tradeLicenseExpiry: new Date('2025-06-30'),
          organization: { connect: { id: org.id } },
        }
      }),
      prisma.client.create({
        data: {
          name: 'Global Ventures DMCC',
          email: 'hello@globalventures.ae',
          phone: '+971503456789',
          address: 'JLT, Dubai',
          trn: 'TRN456789123',
          tradeLicenseNumber: 'TL-2024-003',
          tradeLicenseExpiry: new Date('2025-09-15'),
          organization: { connect: { id: org.id } },
        }
      })
    ]);
    console.log('✅ Clients created:', clients.map(c => c.name).join(', '));

    // 5. Create sample service requests
    console.log('\nCreating sample service requests...');
    const serviceRequests = await Promise.all([
      prisma.serviceRequest.create({
        data: {
          title: 'Trade License Renewal 2025',
          description: 'Annual trade license renewal for the year 2025',
          category: 'LICENSE_RENEWAL',
          priority: 'HIGH',
          status: 'IN_PROGRESS',
          client: { connect: { id: clients[0].id } },
          assignee: { connect: { id: staffUsers[0].id } },
          organization: { connect: { id: org.id } },
          dueDate: new Date('2024-12-15'),
          estimatedHours: 8,
        }
      }),
      prisma.serviceRequest.create({
        data: {
          title: 'VAT Registration',
          description: 'New VAT registration with FTA',
          category: 'VAT_REGISTRATION',
          priority: 'MEDIUM',
          status: 'SUBMITTED',
          client: { connect: { id: clients[1].id } },
          assignee: { connect: { id: staffUsers[1].id } },
          organization: { connect: { id: org.id } },
          dueDate: new Date('2024-11-30'),
          estimatedHours: 12,
        }
      }),
      prisma.serviceRequest.create({
        data: {
          title: 'Visa Application - 3 Employees',
          description: 'New employment visa applications for 3 software developers',
          category: 'VISA_PROCESSING',
          priority: 'HIGH',
          status: 'IN_PROGRESS',
          client: { connect: { id: clients[2].id } },
          assignee: { connect: { id: staffUsers[0].id } },
          organization: { connect: { id: org.id } },
          dueDate: new Date('2024-11-20'),
          estimatedHours: 16,
        }
      }),
      prisma.serviceRequest.create({
        data: {
          title: 'Corporate Bank Account Opening',
          description: 'Assistance with opening corporate account at Emirates NBD',
          category: 'BANK_ACCOUNT',
          priority: 'LOW',
          status: 'DRAFT',
          client: { connect: { id: clients[0].id } },
          organization: { connect: { id: org.id } },
          estimatedHours: 6,
        }
      })
    ]);
    console.log('✅ Service requests created:', serviceRequests.length);

    // 6. Create sample tasks
    console.log('\nCreating sample tasks...');
    const tasks = await prisma.task.createMany({
      data: [
        {
          title: 'Prepare renewal documents',
          description: 'Collect all required documents for license renewal',
          status: 'COMPLETED',
          priority: 'HIGH',
          serviceRequestId: serviceRequests[0].id } },
          assignee: { connect: { id: staffUsers[0].id } },
          organization: { connect: { id: org.id } },
          dueDate: new Date('2024-12-10'),
        },
        {
          title: 'Submit application to DED',
          description: 'Submit the renewal application online',
          status: 'IN_PROGRESS',
          priority: 'HIGH',
          serviceRequestId: serviceRequests[0].id } },
          assignee: { connect: { id: staffUsers[0].id } },
          organization: { connect: { id: org.id } },
          dueDate: new Date('2024-12-12'),
        },
        {
          title: 'Gather VAT registration requirements',
          description: 'Collect financial statements and business details',
          status: 'TODO',
          priority: 'MEDIUM',
          serviceRequestId: serviceRequests[1].id } },
          assignee: { connect: { id: staffUsers[1].id } },
          organization: { connect: { id: org.id } },
          dueDate: new Date('2024-11-25'),
        }
      ]
    });
    console.log('✅ Tasks created:', tasks.count);

    // 7. Create sample payments
    console.log('\nCreating sample payments...');
    const payments = await Promise.all([
      prisma.payment.create({
        data: {
          amount: 5500,
          currency: 'AED',
          status: 'COMPLETED',
          method: 'BANK_TRANSFER',
          reference: 'PAY-2024-001',
          description: 'Trade License Renewal Fee',
          paidAt: new Date('2024-10-15'),
          client: { connect: { id: clients[0].id } },
          serviceRequestId: serviceRequests[0].id } },
          organization: { connect: { id: org.id } },
        }
      }),
      prisma.payment.create({
        data: {
          amount: 2500,
          currency: 'AED',
          status: 'PENDING',
          method: 'CREDIT_CARD',
          reference: 'PAY-2024-002',
          description: 'VAT Registration Consultancy Fee',
          dueDate: new Date('2024-11-30'),
          client: { connect: { id: clients[1].id } },
          serviceRequestId: serviceRequests[1].id } },
          organization: { connect: { id: org.id } },
        }
      })
    ]);
    console.log('✅ Payments created:', payments.length);

    // 8. Create sample documents
    console.log('\nCreating sample documents...');
    const documents = await prisma.document.createMany({
      data: [
        {
          name: 'Trade License 2024.pdf',
          url: 'https://example.com/docs/trade-license-2024.pdf',
          type: 'LICENSE',
          size: 245678,
          uploadedById: adminUser.id,
          client: { connect: { id: clients[0].id } },
          organization: { connect: { id: org.id } },
        },
        {
          name: 'Passport - John Doe.pdf',
          url: 'https://example.com/docs/passport-john.pdf',
          type: 'PASSPORT',
          size: 456789,
          uploadedById: staffUsers[0].id } },
          client: { connect: { id: clients[2].id } },
          serviceRequestId: serviceRequests[2].id } },
          organization: { connect: { id: org.id } },
        },
        {
          name: 'Bank Statement Q3 2024.pdf',
          url: 'https://example.com/docs/bank-statement.pdf',
          type: 'FINANCIAL',
          size: 189456,
          uploadedById: staffUsers[1].id } },
          client: { connect: { id: clients[1].id } },
          serviceRequestId: serviceRequests[1].id } },
          organization: { connect: { id: org.id } },
        }
      ]
    });
    console.log('✅ Documents created:', documents.count);

    console.log('\n' + '='.repeat(50));
    console.log('🎉 Initial data seeded successfully!');
    console.log('='.repeat(50));
    console.log('\n📊 Summary:');
    console.log('- 1 Organization');
    console.log('- 3 Users (1 Admin, 2 Staff)');
    console.log('- 3 Clients');
    console.log('- 4 Service Requests');
    console.log('- 3 Tasks');
    console.log('- 2 Payments');
    console.log('- 3 Documents');
    console.log('\n🔑 Test Credentials:');
    console.log('Email: admin@startupzone.ae');
    console.log('Note: You need to create this user in Supabase Auth');

  } catch (error) {
    console.error('❌ Error seeding data:', error);
    throw error;
  } finally {
    await prisma.$disconnect();
  }
}

// Run the seed
seedInitialData()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  });