import { createServiceRoleClient } from "@/lib/supabase/server"
import { Card } from "@/components/ui/card"
import { EmptyState } from "@/components/ui/empty-state"

interface ClientRecord {
  id: string
  name: string
  company_name?: string | null
  email?: string | null
  phone?: string | null
}

async function fetchClients() {
  const supabase = await createServiceRoleClient()
  const { data, error } = await supabase
    .from("clients")
    .select("id, name, company_name, email, phone")
    .order("created_at", { ascending: false })
    .limit(100)

  if (error) {
    console.error("Failed to load clients", error)
    return [] as ClientRecord[]
  }

  return (data ?? []) as ClientRecord[]
}

export default async function ClientsPage() {
  const clients = await fetchClients()

  return (
    <div>
      <div className="mb-6">
        <h1 className="text-3xl font-bold">Clients</h1>
        <p className="text-gray-600">View and manage client profiles.</p>
      </div>

      {clients.length === 0 ? (
        <EmptyState
          title="No clients yet"
          description="Clients you add will appear here once the Supabase tables are connected to the UI."
        />
      ) : (
        <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          {clients.map((client) => (
            <Card key={client.id} className="p-5">
              <div className="space-y-2">
                <div>
                  <p className="text-lg font-semibold text-gray-900">{client.name}</p>
                  {client.company_name && (
                    <p className="text-sm text-gray-500">{client.company_name}</p>
                  )}
                </div>
                <div className="space-y-1 text-sm text-gray-600">
                  {client.email && <p>Email: {client.email}</p>}
                  {client.phone && <p>Phone: {client.phone}</p>}
                </div>
              </div>
            </Card>
          ))}
        </div>
      )}
    </div>
  )
}
