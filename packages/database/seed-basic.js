const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();

async function main() {
  console.log('🌱 Starting database seed...\n');

  // Clear existing data
  await prisma.payment.deleteMany();
  await prisma.task.deleteMany(); 
  await prisma.document.deleteMany();
  await prisma.serviceRequest.deleteMany();
  await prisma.client.deleteMany();
  await prisma.user.deleteMany();
  await prisma.organization.deleteMany();

  // Create organization
  const org = await prisma.organization.create({
    data: {
      name: 'The Startup Zone FZE',
      slug: 'tsz-fze'
    }
  });
  console.log('✅ Organization created');

  // Create users
  const admin = await prisma.user.create({
    data: {
      email: 'admin@startupzone.ae',
      name: 'Admin User',
      role: 'ADMIN',
      organization: { connect: { id: org.id } }
    }
  });

  const staff = await prisma.user.create({
    data: {
      email: 'staff@startupzone.ae',
      name: 'Staff User',
      role: 'STAFF',
      organization: { connect: { id: org.id } }
    }
  });
  console.log('✅ Users created');

  // Create clients
  const client1 = await prisma.client.create({
    data: {
      name: 'Tech Innovators LLC',
      email: 'contact@techinnovators.ae',
      phone: '+971501234567',
      companyName: 'Tech Innovators LLC',
      tradeLicense: 'TL-2024-001',
      organization: { connect: { id: org.id } }
    }
  });

  const client2 = await prisma.client.create({
    data: {
      name: 'Digital Solutions FZ',
      email: 'info@digitalsolutions.ae',
      phone: '+971502345678',
      companyName: 'Digital Solutions FZ',
      tradeLicense: 'TL-2024-002',
      organization: { connect: { id: org.id } }
    }
  });
  console.log('✅ Clients created');

  // Create service requests
  const sr1 = await prisma.serviceRequest.create({
    data: {
      title: 'Trade License Renewal',
      category: 'LICENSE_RENEWAL',
      priority: 'HIGH',
      status: 'IN_PROGRESS',
      client: { connect: { id: client1.id } },
      assignee: { connect: { id: staff.id } },
      createdBy: { connect: { id: admin.id } },
      organization: { connect: { id: org.id } }
    }
  });

  const sr2 = await prisma.serviceRequest.create({
    data: {
      title: 'VAT Registration',
      category: 'PRO_SERVICE',
      priority: 'MEDIUM',
      status: 'SUBMITTED',
      client: { connect: { id: client2.id } },
      assignee: { connect: { id: staff.id } },
      createdBy: { connect: { id: admin.id } },
      organization: { connect: { id: org.id } }
    }
  });
  console.log('✅ Service requests created');

  // Create tasks
  await prisma.task.create({
    data: {
      title: 'Prepare documents',
      status: 'IN_PROGRESS',
      serviceRequest: { connect: { id: sr1.id } },
      assignee: { connect: { id: staff.id } }
    }
  });
  console.log('✅ Tasks created');

  // Create payments
  await prisma.payment.create({
    data: {
      amount: 5500,
      currency: 'AED',
      method: 'BANK_TRANSFER',
      paidAt: new Date(),
      reference: 'PAY-001',
      serviceRequest: { connect: { id: sr1.id } }
    }
  });
  console.log('✅ Payments created');

  console.log('\n🎉 Seed completed successfully!');
  
  // Show summary
  console.log('\n📊 Database Summary:');
  console.log(`  Organizations: ${await prisma.organization.count()}`);
  console.log(`  Users: ${await prisma.user.count()}`);
  console.log(`  Clients: ${await prisma.client.count()}`);
  console.log(`  Service Requests: ${await prisma.serviceRequest.count()}`);
  console.log(`  Tasks: ${await prisma.task.count()}`);
  console.log(`  Payments: ${await prisma.payment.count()}`);
}

main()
  .catch((e) => {
    console.error('❌ Error:', e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });