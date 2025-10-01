const { Client } = require('pg');

// Try different connection string formats
const connectionStrings = [
  // Format 1: Standard Supabase format with encoded password
  "postgresql://postgres:TSZ%40Portal2024%23Secure!@db.iutmcoftuakkuabghrlu.supabase.co:5432/postgres",
  // Format 2: Try without encoding special chars
  "postgres://postgres:TSZ@Portal2024#Secure!@db.iutmcoftuakkuabghrlu.supabase.co:5432/postgres",
  // Format 3: AWS pooler format with project ref
  "postgresql://postgres.iutmcoftuakkuabghrlu:TSZ%40Portal2024%23Secure!@aws-0-ap-south-1.pooler.supabase.com:5432/postgres",
  // Format 4: Pooler with pgbouncer
  "postgresql://postgres:TSZ%40Portal2024%23Secure!@db.iutmcoftuakkuabghrlu.supabase.co:6543/postgres?pgbouncer=true",
];

async function testConnection(connStr, label) {
  console.log(`\nTesting ${label}...`);
  const client = new Client({
    connectionString: connStr,
    ssl: { rejectUnauthorized: false }
  });

  try {
    await client.connect();
    const res = await client.query('SELECT NOW()');
    console.log(`✅ SUCCESS: Connected at ${res.rows[0].now}`);
    await client.end();
    return true;
  } catch (err) {
    console.log(`❌ FAILED: ${err.message}`);
    return false;
  }
}

async function main() {
  console.log('Testing Supabase database connections...');
  
  for (let i = 0; i < connectionStrings.length; i++) {
    const success = await testConnection(connectionStrings[i], `Format ${i + 1}`);
    if (success) {
      console.log(`\n✅ Working connection string (Format ${i + 1}):`);
      console.log(connectionStrings[i]);
      break;
    }
  }
}

main().catch(console.error);