const { Client } = require('pg');

// Try both connection formats
const connections = [
  "postgresql://postgres.iutmcoftuakkuabghrlu:TSZPortal2024Secure@aws-0-ap-south-1.pooler.supabase.com:6543/postgres",
  "postgresql://postgres:TSZPortal2024Secure@db.iutmcoftuakkuabghrlu.supabase.co:5432/postgres"
];

async function testConnection(connectionString, label) {
  const client = new Client({
    connectionString: connectionString,
    ssl: { rejectUnauthorized: false }
  });

  try {
    console.log(`\nTesting ${label}...`);
    await client.connect();
    
    const result = await client.query('SELECT NOW()');
    console.log('✅ Connected successfully!');
    console.log('Current time from database:', result.rows[0].now);
    
    await client.end();
    return true;
  } catch (err) {
    console.error('❌ Connection failed:', err.message);
    return false;
  }
}

async function test() {
  for (let i = 0; i < connections.length; i++) {
    const success = await testConnection(connections[i], `Format ${i + 1}`);
    if (success) {
      console.log(`\n✅ Working connection string:`);
      console.log(connections[i]);
      break;
    }
  }
}

test();