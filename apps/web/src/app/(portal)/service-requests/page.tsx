import { createServiceRoleClient } from "@/lib/supabase/server"
import { ServiceRequestsList } from "@/app/service-requests/components/service-requests-list"

interface ServiceRequestRecord {
  id: string
  title: string
  category: string
  priority: string
  status: string
  due_date?: string | null
  clients: { name?: string | null; company_name?: string | null } | null
  assignees: { name?: string | null; email?: string | null } | null
}

async function fetchServiceRequests() {
  const supabase = await createServiceRoleClient()
  const { data, error } = await supabase
    .from("service_requests")
    .select(
      `id, title, category, priority, status, due_date,
       clients ( name, company_name ),
       assignees:users!service_requests_assignee_id_fkey ( name, email )`
    )
    .order("created_at", { ascending: false })
    .limit(50)

  if (error) {
    console.error("Failed to load service requests", error)
    return [] as ServiceRequestRecord[]
  }

  return (data ?? []) as ServiceRequestRecord[]
}

export default async function ServiceRequestsPage() {
  const records = await fetchServiceRequests()

  const serviceRequests = records.map((record) => ({
    id: record.id,
    title: record.title,
    clientName: record.clients?.name ?? record.clients?.company_name ?? "Unknown client",
    category: record.category,
    priority: record.priority,
    status: record.status,
    assigneeName: record.assignees?.name ?? record.assignees?.email ?? "Unassigned",
    dueDate: record.due_date ?? undefined,
  }))

  return (
    <div>
      <div className="mb-6">
        <h1 className="text-3xl font-bold">Service Requests</h1>
        <p className="text-gray-600">Manage all client service requests</p>
      </div>
      <ServiceRequestsList serviceRequests={serviceRequests} />
    </div>
  )
}
