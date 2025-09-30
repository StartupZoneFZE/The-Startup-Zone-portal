-- Enable RLS on all tables
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE organizations ENABLE ROW LEVEL SECURITY;
ALTER TABLE clients ENABLE ROW LEVEL SECURITY;
ALTER TABLE service_requests ENABLE ROW LEVEL SECURITY;
ALTER TABLE stages ENABLE ROW LEVEL SECURITY;
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;
ALTER TABLE notes ENABLE ROW LEVEL SECURITY;
ALTER TABLE payments ENABLE ROW LEVEL SECURITY;
ALTER TABLE renewals ENABLE ROW LEVEL SECURITY;

-- Users policies
-- Admins can read all users
CREATE POLICY "Admins can read all users" ON users
  FOR SELECT
  USING (
    EXISTS (
      SELECT 1 FROM users 
      WHERE id = auth.uid() 
      AND role = 'ADMIN'
    )
  );

-- Staff can read users in their organization
CREATE POLICY "Staff can read users in their org" ON users
  FOR SELECT
  USING (
    organization_id = (
      SELECT organization_id FROM users 
      WHERE id = auth.uid()
    )
  );

-- Users can read their own profile
CREATE POLICY "Users can read own profile" ON users
  FOR SELECT
  USING (id = auth.uid());

-- Organizations policies
-- Users can read their own organization
CREATE POLICY "Users can read their organization" ON organizations
  FOR SELECT
  USING (
    id IN (
      SELECT organization_id FROM users 
      WHERE id = auth.uid()
    )
  );

-- Clients policies
-- Staff can manage clients in their organization
CREATE POLICY "Staff can read clients in their org" ON clients
  FOR SELECT
  USING (
    organization_id = (
      SELECT organization_id FROM users 
      WHERE id = auth.uid()
    )
  );

CREATE POLICY "Staff can insert clients in their org" ON clients
  FOR INSERT
  WITH CHECK (
    organization_id = (
      SELECT organization_id FROM users 
      WHERE id = auth.uid()
    )
  );

CREATE POLICY "Staff can update clients in their org" ON clients
  FOR UPDATE
  USING (
    organization_id = (
      SELECT organization_id FROM users 
      WHERE id = auth.uid()
    )
  );

-- Service Requests policies
-- Staff can read all service requests in their organization
CREATE POLICY "Staff can read service requests in their org" ON service_requests
  FOR SELECT
  USING (
    organization_id = (
      SELECT organization_id FROM users 
      WHERE id = auth.uid()
    )
  );

-- Clients can read their own service requests
CREATE POLICY "Clients can read own service requests" ON service_requests
  FOR SELECT
  USING (
    client_id IN (
      SELECT id FROM clients 
      WHERE email = (
        SELECT email FROM users WHERE id = auth.uid()
      )
    )
  );

-- Staff can create service requests
CREATE POLICY "Staff can create service requests" ON service_requests
  FOR INSERT
  WITH CHECK (
    organization_id = (
      SELECT organization_id FROM users 
      WHERE id = auth.uid()
    )
  );

-- Staff can update service requests in their org
CREATE POLICY "Staff can update service requests" ON service_requests
  FOR UPDATE
  USING (
    organization_id = (
      SELECT organization_id FROM users 
      WHERE id = auth.uid()
    )
  );

-- Stages policies
-- Read stages for accessible service requests
CREATE POLICY "Read stages for accessible requests" ON stages
  FOR SELECT
  USING (
    service_request_id IN (
      SELECT id FROM service_requests
    )
  );

-- Staff can manage stages
CREATE POLICY "Staff can insert stages" ON stages
  FOR INSERT
  WITH CHECK (
    service_request_id IN (
      SELECT id FROM service_requests
      WHERE organization_id = (
        SELECT organization_id FROM users 
        WHERE id = auth.uid()
      )
    )
  );

CREATE POLICY "Staff can update stages" ON stages
  FOR UPDATE
  USING (
    service_request_id IN (
      SELECT id FROM service_requests
      WHERE organization_id = (
        SELECT organization_id FROM users 
        WHERE id = auth.uid()
      )
    )
  );

-- Documents policies
-- Read documents in your organization
CREATE POLICY "Read documents in organization" ON documents
  FOR SELECT
  USING (
    organization_id = (
      SELECT organization_id FROM users 
      WHERE id = auth.uid()
    )
  );

-- Upload documents to your organization
CREATE POLICY "Upload documents to organization" ON documents
  FOR INSERT
  WITH CHECK (
    organization_id = (
      SELECT organization_id FROM users 
      WHERE id = auth.uid()
    )
  );

-- Tasks policies
-- Read tasks for accessible service requests
CREATE POLICY "Read tasks for accessible requests" ON tasks
  FOR SELECT
  USING (
    service_request_id IN (
      SELECT id FROM service_requests
    )
  );

-- Staff can manage tasks
CREATE POLICY "Staff can manage tasks" ON tasks
  FOR ALL
  USING (
    service_request_id IN (
      SELECT id FROM service_requests
      WHERE organization_id = (
        SELECT organization_id FROM users 
        WHERE id = auth.uid()
      )
    )
  );

-- Notes policies
-- Read notes in organization
CREATE POLICY "Read notes in organization" ON notes
  FOR SELECT
  USING (
    organization_id = (
      SELECT organization_id FROM users 
      WHERE id = auth.uid()
    )
  );

-- Create notes in organization
CREATE POLICY "Create notes in organization" ON notes
  FOR INSERT
  WITH CHECK (
    organization_id = (
      SELECT organization_id FROM users 
      WHERE id = auth.uid()
    )
  );

-- Payments policies
-- Read payments for accessible service requests
CREATE POLICY "Read payments for accessible requests" ON payments
  FOR SELECT
  USING (
    service_request_id IN (
      SELECT id FROM service_requests
    )
  );

-- Staff can manage payments
CREATE POLICY "Staff can manage payments" ON payments
  FOR ALL
  USING (
    service_request_id IN (
      SELECT id FROM service_requests
      WHERE organization_id = (
        SELECT organization_id FROM users 
        WHERE id = auth.uid()
      )
    )
  );

-- Renewals policies
-- Staff can read all renewals (no org context)
CREATE POLICY "Staff can read renewals" ON renewals
  FOR SELECT
  USING (
    EXISTS (
      SELECT 1 FROM users 
      WHERE id = auth.uid() 
      AND role IN ('ADMIN', 'STAFF')
    )
  );

-- Staff can manage renewals
CREATE POLICY "Staff can manage renewals" ON renewals
  FOR ALL
  USING (
    EXISTS (
      SELECT 1 FROM users 
      WHERE id = auth.uid() 
      AND role IN ('ADMIN', 'STAFF')
    )
  );