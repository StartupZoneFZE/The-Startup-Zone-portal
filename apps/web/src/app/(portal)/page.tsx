import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { FileText, Clock, User, Ticket } from "lucide-react"
import { Skeleton } from "@/components/ui/skeleton"
import { Badge } from "@/components/ui/badge"
import { EmptyState } from "@/components/ui/empty-state"

const mockDashboardData = {
  metrics: [
    {
      label: "Active Requests",
      value: "24",
      change: "+12% from last month",
      icon: FileText,
    },
    {
      label: "Total Users",
      value: "120",
      change: "+5% from last month",
      icon: User,
    },
    {
      label: "New Tickets",
      value: "15",
      change: "+10% from last month",
      icon: Ticket,
    },
    {
      label: "Average Resolution Time",
      value: "2.5 hours",
      change: "-10% from last month",
      icon: Clock,
    },
  ],
  recentRequests: [
    {
      id: 1,
      title: "Website Maintenance",
      submitted: "2 hours ago",
      status: "High Priority",
      variant: "danger",
    },
    {
      id: 2,
      title: "Database Backup",
      submitted: "1 day ago",
      status: "Medium Priority",
      variant: "warning",
    },
    {
      id: 3,
      title: "Email Server Issue",
      submitted: "3 days ago",
      status: "Low Priority",
      variant: "info",
    },
  ],
  deadlines: [
    {
      id: 1,
      title: "Annual Report",
      client: "Finance Department",
      dueIn: "2 days",
      color: "text-blue-600",
    },
    {
      id: 2,
      title: "Quarterly Audit",
      client: "IT Department",
      dueIn: "1 week",
      color: "text-green-600",
    },
    {
      id: 3,
      title: "Software Update",
      client: "Operations Team",
      dueIn: "2 weeks",
      color: "text-purple-600",
    },
  ],
}

export default function DashboardPage() {
  const isLoading = false
  const hasData = mockDashboardData.metrics.length > 0

  return (
    <div>
      <div className="mb-6">
        <h1 className="text-3xl font-bold">Dashboard</h1>
        <p className="text-gray-600">Welcome to TSZ Portal</p>
      </div>

      {isLoading ? (
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
          {[...Array(4)].map((_, index) => (
            <Card key={index}>
              <CardContent className="space-y-3 p-6">
                <Skeleton className="h-4 w-24" />
                <Skeleton className="h-8 w-20" />
                <Skeleton className="h-3 w-28" />
              </CardContent>
            </Card>
          ))}
        </div>
      ) : hasData ? (
        <>
          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
            {mockDashboardData.metrics.map((metric) => (
              <Card key={metric.label} className="border-0 bg-white shadow-lg ring-1 ring-gray-200/60">
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                  <CardTitle className="text-sm font-medium text-gray-600">{metric.label}</CardTitle>
                  <div className="rounded-md bg-gray-100 p-2">
                    <metric.icon className="h-4 w-4 text-gray-500" />
                  </div>
                </CardHeader>
                <CardContent>
                  <div className="text-3xl font-semibold tracking-tight">{metric.value}</div>
                  <p className="mt-1 text-xs text-gray-500">{metric.change}</p>
                </CardContent>
              </Card>
            ))}
          </div>

          <div className="mt-6 grid gap-6 md:grid-cols-2">
            <Card>
              <CardHeader>
                <CardTitle>Recent Service Requests</CardTitle>
                <CardDescription>Latest requests requiring attention</CardDescription>
              </CardHeader>
              <CardContent>
                {mockDashboardData.recentRequests.length === 0 ? (
                  <EmptyState
                    title="No recent requests"
                    description="New requests will appear here once clients submit them."
                  />
                ) : (
                  <div className="space-y-4">
                    {mockDashboardData.recentRequests.map((request) => (
                      <div key={request.id} className="flex items-center justify-between rounded-xl border border-gray-200/70 bg-white px-4 py-3 shadow-sm">
                        <div>
                          <p className="font-medium text-gray-900">{request.title}</p>
                          <p className="text-sm text-gray-500">{request.submitted}</p>
                        </div>
                        <Badge variant={(request.variant as any) ?? "default"}>{request.status}</Badge>
                      </div>
                    ))}
                  </div>
                )}
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>Upcoming Deadlines</CardTitle>
                <CardDescription>Tasks and renewals due soon</CardDescription>
              </CardHeader>
              <CardContent>
                {mockDashboardData.deadlines.length === 0 ? (
                  <EmptyState
                    title="No upcoming deadlines"
                    description="You&apos;re all caught up. Deadlines will display as they approach."
                  />
                ) : (
                  <div className="space-y-4">
                    {mockDashboardData.deadlines.map((deadline) => (
                      <div key={deadline.id} className="flex items-center justify-between rounded-xl border border-gray-200/70 bg-white px-4 py-3 shadow-sm">
                        <div className="flex items-center space-x-3">
                          <Clock className={`h-4 w-4 ${deadline.color}`} />
                          <div>
                            <p className="font-medium text-gray-900">{deadline.title}</p>
                            <p className="text-sm text-gray-500">{deadline.client}</p>
                          </div>
                        </div>
                        <span className={`text-sm font-medium ${deadline.color}`}>{deadline.dueIn}</span>
                      </div>
                    ))}
                  </div>
                )}
              </CardContent>
            </Card>
          </div>
        </>
      ) : (
        <EmptyState
          title="Dashboard not configured"
          description="We couldn&apos;t find any dashboard widgets. Add metrics and sections to get started."
        />
      )}
    </div>
  )
}
