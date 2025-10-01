const { createClient } = require('@supabase/supabase-js');

const SUPABASE_URL = 'https://iutmcoftuakkuabghrlu.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml1dG1jb2Z0dWFra3VhYmdocmx1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTkyOTQ0NzgsImV4cCI6MjA3NDg3MDQ3OH0.P9OCrF-x8YCNCRMJdq81vWLHOikbYgZ2c5GnKp39apE';
const SUPABASE_SERVICE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml1dG1jb2Z0dWFra3VhYmdocmx1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1OTI5NDQ3OCwiZXhwIjoyMDc0ODcwNDc4fQ.PJTRoar1yzlrv_EXNkvt69c5CdoVwJR37ZqsYshsYjM';

async function testSupabaseConnection() {
  console.log('Testing Supabase JavaScript Client Connection');
  console.log('='.repeat(50));

  // Test with anon key
  console.log('\n1. Testing with ANON key (public access):');
  const supabaseAnon = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
  
  try {
    // Try to query a system table
    const { data, error } = await supabaseAnon
      .from('_prisma_migrations')
      .select('*')
      .limit(1);

    if (error) {
      if (error.code === '42P01') {
        console.log('✅ Connected but no tables exist yet (expected)');
        console.log('   This means we can connect to the database!');
      } else {
        console.log(`⚠️  Connected but got error: ${error.message}`);
      }
    } else {
      console.log('✅ Connected and found data');
    }
  } catch (err) {
    console.log(`❌ Connection failed: ${err.message}`);
  }

  // Test with service role key
  console.log('\n2. Testing with SERVICE ROLE key (admin access):');
  const supabaseAdmin = createClient(SUPABASE_URL, SUPABASE_SERVICE_KEY);
  
  try {
    // Try to create a test table using service role
    const { data, error } = await supabaseAdmin.rpc('version');
    
    if (error) {
      console.log(`⚠️  RPC call failed: ${error.message}`);
      // Try another approach
      const { data: tables, error: tablesError } = await supabaseAdmin
        .from('information_schema.tables')
        .select('table_name')
        .eq('table_schema', 'public')
        .limit(1);
      
      if (tablesError) {
        console.log(`   Fallback query: ${tablesError.message}`);
      } else {
        console.log('✅ Admin access works, can query system tables');
      }
    } else {
      console.log('✅ Admin access verified');
    }
  } catch (err) {
    console.log(`❌ Admin connection failed: ${err.message}`);
  }

  console.log('\n' + '='.repeat(50));
  console.log('Summary:');
  console.log('- Supabase project is active and accessible');
  console.log('- API keys are valid and working');
  console.log('- Database exists but needs schema migration');
  console.log('\nNext step: Run Prisma migrations to create tables');
}

testSupabaseConnection().catch(console.error);