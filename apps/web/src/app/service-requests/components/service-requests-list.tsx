"use client"

import { useEffect, useState } from "react"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Card } from "@/components/ui/card"
import { EmptyState } from "@/components/ui/empty-state"
import { Plus, Search, Filter } from "lucide-react"
import { CreateServiceRequestModal } from "./create-service-request-modal"

interface ServiceRequestListProps {
  serviceRequests?: Array<{
    id: string
    title: string
    clientName: string
    category: string
    priority: string
    status: string
    assigneeName: string
    dueDate?: string
  }>
}

export function ServiceRequestsList({ serviceRequests = [] }: ServiceRequestListProps) {
  const [isCreateModalOpen, setIsCreateModalOpen] = useState(false)
  const [searchQuery, setSearchQuery] = useState("")
  const [isLoading, setIsLoading] = useState(false)

  useEffect(() => {
    if (searchQuery === "") {
      setIsLoading(false)
      return
    }

    setIsLoading(true)
    const timeout = setTimeout(() => setIsLoading(false), 300)

    return () => clearTimeout(timeout)
  }, [searchQuery])

  const filteredRequests = serviceRequests.filter((request) =>
    request.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
    request.clientName.toLowerCase().includes(searchQuery.toLowerCase())
  )

  const hasData = serviceRequests.length > 0

  return (
    <>
      <Card className="p-6">
        <div className="mb-6 flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-gray-400" />
              <input
                type="text"
                placeholder="Search requests..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-80 rounded-lg border border-gray-300 py-2 pl-10 pr-4 text-sm focus:border-primary focus:outline-none"
              />
            </div>
            <Button variant="outline" size="sm">
              <Filter className="mr-2 h-4 w-4" />
              Filter
            </Button>
          </div>
          <Button onClick={() => setIsCreateModalOpen(true)}>
            <Plus className="mr-2 h-4 w-4" />
            New Request
          </Button>
        </div>

        <div className="overflow-x-auto">
          {isLoading ? (
            <div className="space-y-4">
              {[...Array(3)].map((_, index) => (
                <div key={index} className="flex items-center justify-between rounded-lg border border-gray-200 p-4">
                  <div className="space-y-2">
                    <div className="h-3 w-52 animate-pulse rounded bg-gray-200" />
                    <div className="h-3 w-32 animate-pulse rounded bg-gray-200" />
                  </div>
                  <div className="flex items-center space-x-4">
                    <div className="h-6 w-20 animate-pulse rounded bg-gray-200" />
                    <div className="h-6 w-20 animate-pulse rounded bg-gray-200" />
                    <div className="h-8 w-16 animate-pulse rounded bg-gray-200" />
                  </div>
                </div>
              ))}
            </div>
          ) : !hasData ? (
            <EmptyState
              title="No service requests yet"
              description="Service requests you create will show up here."
              action={
                <Button onClick={() => setIsCreateModalOpen(true)}>
                  <Plus className="mr-2 h-4 w-4" />
                  Create Service Request
                </Button>
              }
            />
          ) : filteredRequests.length === 0 ? (
            <EmptyState
              title="No requests match your search"
              description="Try adjusting your filters or create a new request."
              action={
                <Button onClick={() => setIsCreateModalOpen(true)}>
                  <Plus className="mr-2 h-4 w-4" />
                  Create Service Request
                </Button>
              }
            />
          ) : (
            <table className="w-full">
              <thead>
                <tr className="border-b text-left text-xs uppercase tracking-wide text-gray-500">
                  <th className="pb-3 font-medium text-gray-700">Title</th>
                  <th className="pb-3 font-medium text-gray-700">Client</th>
                  <th className="pb-3 font-medium text-gray-700">Category</th>
                  <th className="pb-3 font-medium text-gray-700">Priority</th>
                  <th className="pb-3 font-medium text-gray-700">Status</th>
                  <th className="pb-3 font-medium text-gray-700">Assignee</th>
                  <th className="pb-3 font-medium text-gray-700">Due Date</th>
                  <th className="pb-3 font-medium text-gray-700">Actions</th>
                </tr>
              </thead>
              <tbody>
                {filteredRequests.map((request) => (
                  <tr key={request.id} className="border-b transition-colors hover:bg-gray-50">
                    <td className="py-4">
                      <div className="font-medium text-gray-900">{request.title}</div>
                    </td>
                    <td className="py-4 text-gray-600">{request.clientName}</td>
                    <td className="py-4">
                      <span className="text-sm text-gray-600">
                        {request.category.replace(/_/g, " ")}
                      </span>
                    </td>
                    <td className="py-4">
                      <Badge variant={request.priority}>
                        {request.priority}
                      </Badge>
                    </td>
                    <td className="py-4">
                      <Badge variant={request.status}>
                        {request.status.replace(/_/g, " ")}
                      </Badge>
                    </td>
                    <td className="py-4 text-gray-600">{request.assigneeName}</td>
                    <td className="py-4 text-gray-600">
                      {request.dueDate ? new Date(request.dueDate).toLocaleDateString() : "--"}
                    </td>
                    <td className="py-4">
                      <Button variant="ghost" size="sm">
                        View
                      </Button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </Card>

      <CreateServiceRequestModal
        isOpen={isCreateModalOpen}
        onClose={() => setIsCreateModalOpen(false)}
      />
    </>
  )
}