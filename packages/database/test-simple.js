const { Client } = require('pg');

// Connection string with URL-encoded password
// Original password: TSZ@Portal2024#Secure!
// URL encoded: TSZ%40Portal2024%23Secure%21
const connectionString = "postgresql://postgres.iutmcoftuakkuabghrlu:TSZ%40Portal2024%23Secure%21@aws-0-ap-south-1.pooler.supabase.com:6543/postgres";

async function test() {
  const client = new Client({
    connectionString: connectionString,
    ssl: { rejectUnauthorized: false }
  });

  try {
    console.log('Connecting to Supabase...');
    await client.connect();
    
    const result = await client.query('SELECT version()');
    console.log('✅ Connected successfully!');
    console.log('PostgreSQL version:', result.rows[0].version);
    
    await client.end();
  } catch (err) {
    console.error('❌ Connection failed:', err.message);
    console.error('Full error:', err);
  }
}

test();