const { Client } = require('pg');

// Test various connection formats
const tests = [
  {
    name: "Direct connection with encoded password",
    connectionString: "postgresql://postgres.iutmcoftuakkuabghrlu:TSZ%40Portal2024%23Secure%21@aws-0-ap-south-1.pooler.supabase.com:5432/postgres"
  },
  {
    name: "Pooled connection (Transaction mode)",
    connectionString: "postgresql://postgres.iutmcoftuakkuabghrlu:TSZ%40Portal2024%23Secure%21@aws-0-ap-south-1.pooler.supabase.com:6543/postgres"
  },
  {
    name: "Using Supabase REST API",
    method: "rest"
  }
];

async function testPgConnection(config) {
  const client = new Client({
    connectionString: config.connectionString,
    ssl: { rejectUnauthorized: false }
  });

  try {
    await client.connect();
    const result = await client.query('SELECT NOW()');
    console.log(`✅ SUCCESS: Connected at ${result.rows[0].now}`);
    await client.end();
    return true;
  } catch (err) {
    console.log(`❌ FAILED: ${err.message}`);
    return false;
  }
}

async function testRestAPI() {
  const SUPABASE_URL = 'https://iutmcoftuakkuabghrlu.supabase.co';
  const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml1dG1jb2Z0dWFra3VhYmdocmx1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTkyOTQ0NzgsImV4cCI6MjA3NDg3MDQ3OH0.P9OCrF-x8YCNCRMJdq81vWLHOikbYgZ2c5GnKp39apE';

  try {
    const response = await fetch(`${SUPABASE_URL}/rest/v1/`, {
      headers: {
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': `Bearer ${SUPABASE_ANON_KEY}`
      }
    });

    if (response.ok) {
      console.log('✅ SUCCESS: Supabase REST API is accessible');
      console.log('   Project URL is valid and API key works');
      return true;
    } else {
      console.log(`❌ FAILED: REST API returned status ${response.status}`);
      return false;
    }
  } catch (err) {
    console.log(`❌ FAILED: ${err.message}`);
    return false;
  }
}

async function main() {
  console.log('='.repeat(60));
  console.log('Testing Supabase Connections');
  console.log('='.repeat(60));
  console.log('Project: iutmcoftuakkuabghrlu');
  console.log('Region: ap-south-1 (Mumbai)');
  console.log('');

  for (const test of tests) {
    console.log(`\n📍 Testing: ${test.name}`);
    console.log('-'.repeat(40));
    
    if (test.method === 'rest') {
      await testRestAPI();
    } else {
      await testPgConnection(test);
    }
  }

  console.log('\n' + '='.repeat(60));
  console.log('Connection Diagnostics:');
  console.log('1. REST API test confirms project exists and is accessible');
  console.log('2. Database connection failures suggest password issue');
  console.log('3. "Tenant or user not found" = wrong username/password combo');
  console.log('\nRecommended Action:');
  console.log('Reset database password in Supabase dashboard to a simpler one');
  console.log('(Settings → Database → Reset Database Password)');
}

main().catch(console.error);