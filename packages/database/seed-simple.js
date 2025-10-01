const { PrismaClient } = require('@prisma/client');
const crypto = require('crypto');

const prisma = new PrismaClient();

async function seedData() {
  console.log('🌱 Seeding initial data...\n');

  try {
    // Clean existing data
    console.log('Cleaning existing data...');
    await prisma.payment.deleteMany();
    await prisma.task.deleteMany();
    await prisma.document.deleteMany();
    await prisma.serviceRequest.deleteMany();
    await prisma.client.deleteMany();
    await prisma.user.deleteMany();
    await prisma.organization.deleteMany();
    
    // 1. Create organization
    console.log('Creating organization...');
    const org = await prisma.organization.create({
      data: {
        name: 'The Startup Zone FZE',
        slug: 'tsz-fze'
      }
    });
    console.log('✅ Organization created');

    // 2. Create users
    console.log('\nCreating users...');
    const admin = await prisma.user.create({
      data: {
        email: 'admin@startupzone.ae',
        name: 'Admin User',
        role: 'ADMIN',
        organization: { connect: { id: org.id } }
      }
    });

    const staff1 = await prisma.user.create({
      data: {
        email: 'john@startupzone.ae',
        name: 'John Smith',
        role: 'STAFF',
        organization: { connect: { id: org.id } }
      }
    });

    const staff2 = await prisma.user.create({
      data: {
        email: 'sarah@startupzone.ae',
        name: 'Sarah Johnson',
        role: 'STAFF',
        organization: { connect: { id: org.id } }
      }
    });
    console.log('✅ Users created: 1 Admin, 2 Staff');

    // 3. Create clients
    console.log('\nCreating clients...');
    const client1 = await prisma.client.create({
      data: {
        name: 'Tech Innovators LLC',
        email: 'contact@techinnovators.ae',
        phone: '+971501234567',
        address: 'Business Bay, Dubai',
        trn: 'TRN123456789',
        tradeLicenseNumber: 'TL-2024-001',
        tradeLicenseExpiry: new Date('2025-12-31'),
        organization: { connect: { id: org.id } }
      }
    });

    const client2 = await prisma.client.create({
      data: {
        name: 'Digital Solutions FZ',
        email: 'info@digitalsolutions.ae',
        phone: '+971502345678',
        address: 'DIFC, Dubai',
        organization: { connect: { id: org.id } }
      }
    });

    const client3 = await prisma.client.create({
      data: {
        name: 'Global Ventures DMCC',
        email: 'hello@globalventures.ae',
        phone: '+971503456789',
        address: 'JLT, Dubai',
        organization: { connect: { id: org.id } }
      }
    });
    console.log('✅ Clients created: 3');

    // 4. Create service requests
    console.log('\nCreating service requests...');
    const sr1 = await prisma.serviceRequest.create({
      data: {
        title: 'Trade License Renewal 2025',
        description: 'Annual trade license renewal for the year 2025',
        category: 'LICENSE_RENEWAL',
        priority: 'HIGH',
        status: 'IN_PROGRESS',
        client: { connect: { id: client1.id } },
        assignee: { connect: { id: staff1.id } },
        organization: { connect: { id: org.id } },
        dueDate: new Date('2024-12-15'),
        estimatedHours: 8,
      }
    });

    const sr2 = await prisma.serviceRequest.create({
      data: {
        title: 'VAT Registration',
        description: 'New VAT registration with FTA',
        category: 'VAT_REGISTRATION',
        priority: 'MEDIUM',
        status: 'SUBMITTED',
        client: { connect: { id: client2.id } },
        assignee: { connect: { id: staff2.id } },
        organization: { connect: { id: org.id } },
        dueDate: new Date('2024-11-30'),
        estimatedHours: 12,
      }
    });

    const sr3 = await prisma.serviceRequest.create({
      data: {
        title: 'Visa Application - 3 Employees',
        description: 'New employment visa applications for 3 software developers',
        category: 'VISA_PROCESSING',
        priority: 'HIGH',
        status: 'IN_PROGRESS',
        client: { connect: { id: client3.id } },
        assignee: { connect: { id: staff1.id } },
        organization: { connect: { id: org.id } },
        dueDate: new Date('2024-11-20'),
        estimatedHours: 16,
      }
    });
    console.log('✅ Service requests created: 3');

    // 5. Create tasks
    console.log('\nCreating tasks...');
    await prisma.task.create({
      data: {
        title: 'Prepare renewal documents',
        description: 'Collect all required documents for license renewal',
        status: 'COMPLETED',
        priority: 'HIGH',
        serviceRequest: { connect: { id: sr1.id } },
        assignee: { connect: { id: staff1.id } },
        organization: { connect: { id: org.id } },
        dueDate: new Date('2024-12-10'),
      }
    });

    await prisma.task.create({
      data: {
        title: 'Submit application to DED',
        description: 'Submit the renewal application online',
        status: 'IN_PROGRESS',
        priority: 'HIGH',
        serviceRequest: { connect: { id: sr1.id } },
        assignee: { connect: { id: staff1.id } },
        organization: { connect: { id: org.id } },
        dueDate: new Date('2024-12-12'),
      }
    });
    console.log('✅ Tasks created: 2');

    // 6. Create payments
    console.log('\nCreating payments...');
    await prisma.payment.create({
      data: {
        amount: 5500,
        currency: 'AED',
        status: 'COMPLETED',
        method: 'BANK_TRANSFER',
        reference: 'PAY-2024-001',
        description: 'Trade License Renewal Fee',
        paidAt: new Date('2024-10-15'),
        client: { connect: { id: client1.id } },
        serviceRequest: { connect: { id: sr1.id } },
        organization: { connect: { id: org.id } }
      }
    });

    await prisma.payment.create({
      data: {
        amount: 2500,
        currency: 'AED',
        status: 'PENDING',
        method: 'CREDIT_CARD',
        reference: 'PAY-2024-002',
        description: 'VAT Registration Consultancy Fee',
        dueDate: new Date('2024-11-30'),
        client: { connect: { id: client2.id } },
        serviceRequest: { connect: { id: sr2.id } },
        organization: { connect: { id: org.id } }
      }
    });
    console.log('✅ Payments created: 2');

    // 7. Create documents
    console.log('\nCreating documents...');
    await prisma.document.create({
      data: {
        name: 'Trade License 2024.pdf',
        url: 'https://example.com/docs/trade-license-2024.pdf',
        type: 'LICENSE',
        size: 245678,
        uploadedBy: { connect: { id: admin.id } },
        client: { connect: { id: client1.id } },
        organization: { connect: { id: org.id } }
      }
    });

    await prisma.document.create({
      data: {
        name: 'Passport - John Doe.pdf',
        url: 'https://example.com/docs/passport-john.pdf',
        type: 'PASSPORT',
        size: 456789,
        uploadedBy: { connect: { id: staff1.id } },
        client: { connect: { id: client3.id } },
        serviceRequest: { connect: { id: sr3.id } },
        organization: { connect: { id: org.id } }
      }
    });
    console.log('✅ Documents created: 2');

    console.log('\n' + '='.repeat(50));
    console.log('🎉 Initial data seeded successfully!');
    console.log('='.repeat(50));
    
    // Summary
    const counts = {
      organizations: await prisma.organization.count(),
      users: await prisma.user.count(),
      clients: await prisma.client.count(),
      serviceRequests: await prisma.serviceRequest.count(),
      tasks: await prisma.task.count(),
      payments: await prisma.payment.count(),
      documents: await prisma.document.count()
    };

    console.log('\n📊 Database Summary:');
    Object.entries(counts).forEach(([table, count]) => {
      console.log(`  ${table}: ${count}`);
    });

    console.log('\n🔑 Test Credentials:');
    console.log('  Email: admin@startupzone.ae');
    console.log('  Note: Create this user in Supabase Auth to login');

  } catch (error) {
    console.error('❌ Error seeding data:', error);
    throw error;
  } finally {
    await prisma.$disconnect();
  }
}

seedData().catch((e) => {
  console.error(e);
  process.exit(1);
});