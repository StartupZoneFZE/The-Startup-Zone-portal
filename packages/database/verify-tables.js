const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient();

async function verifyTables() {
  console.log('Verifying database tables...\n');
  
  try {
    // Check if tables exist by counting records
    const tables = [
      { name: 'Organization', count: await prisma.organization.count() },
      { name: 'User', count: await prisma.user.count() },
      { name: 'Client', count: await prisma.client.count() },
      { name: 'ServiceRequest', count: await prisma.serviceRequest.count() },
      { name: 'Document', count: await prisma.document.count() },
      { name: 'Task', count: await prisma.task.count() },
      { name: 'Payment', count: await prisma.payment.count() },
      { name: 'Renewal', count: await prisma.renewal.count() }
    ];
    
    console.log('✅ All tables created successfully!\n');
    console.log('Table Status:');
    console.log('-'.repeat(30));
    
    for (const table of tables) {
      console.log(`${table.name.padEnd(20)} ${table.count} records`);
    }
    
    console.log('\n🎉 Database is ready for use!');
    
  } catch (error) {
    console.error('❌ Error verifying tables:', error);
  } finally {
    await prisma.$disconnect();
  }
}

verifyTables();