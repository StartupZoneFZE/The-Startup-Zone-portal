"use client"

import { useEffect, useState } from "react"
import { useRouter } from "next/navigation"
import { useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import * as z from "zod"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { createClient } from "@/lib/supabase/client"

const serviceRequestSchema = z.object({
  title: z.string().min(1, "Title is required"),
  description: z.string().optional(),
  clientId: z.string().min(1, "Client is required"),
  category: z.enum([
    "LICENSE_NEW",
    "LICENSE_RENEWAL",
    "PRO_SERVICE",
    "VISA_SERVICE",
    "DOCUMENT_CLEARING",
    "OTHER",
  ]),
  priority: z.enum(["LOW", "MEDIUM", "HIGH", "URGENT"]),
  assigneeId: z.string().optional(),
  dueDate: z.string().optional(),
})

type ServiceRequestFormData = z.infer<typeof serviceRequestSchema>

interface CreateServiceRequestModalProps {
  isOpen: boolean
  onClose: () => void
}

export function CreateServiceRequestModal({
  isOpen,
  onClose,
}: CreateServiceRequestModalProps) {
  const [isSubmitting, setIsSubmitting] = useState(false)
  const router = useRouter()
  const supabase = createClient()
  const [error, setError] = useState<string | null>(null)
  const [clients, setClients] = useState<Array<{ id: string; name: string }>>([])
  const [assignees, setAssignees] = useState<Array<{ id: string; name: string }>>([])
  const [organizationId, setOrganizationId] = useState<string | null>(null)
  const [userId, setUserId] = useState<string | null>(null)

  useEffect(() => {
    const fetchData = async () => {
      const [{ data: userData }, { data: assigneeData }, { data: clientData }] = await Promise.all([
        supabase.auth.getUser(),
        supabase.from("users").select("id, name").eq("role", "STAFF").limit(50),
        supabase.from("clients").select("id, name").limit(100),
      ])

      const currentUser = userData?.user
      const currentOrgId = currentUser?.user_metadata?.organization_id ?? null
      setUserId(currentUser?.id ?? null)
      setOrganizationId(currentOrgId)

      setAssignees((assigneeData ?? []).map((assignee: any) => ({ id: assignee.id, name: assignee.name })))
      setClients((clientData ?? []).map((client: any) => ({ id: client.id, name: client.name })))
    }

    fetchData()
  }, [supabase])

  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
    setValue,
    watch,
  } = useForm<ServiceRequestFormData>({
    resolver: zodResolver(serviceRequestSchema),
    defaultValues: {
      priority: "MEDIUM",
      category: undefined,
      clientId: "",
      assigneeId: "",
    },
  })

  const selectedClient = watch("clientId")
  const selectedCategory = watch("category")
  const selectedPriority = watch("priority")
  const selectedAssignee = watch("assigneeId")

  useEffect(() => {
    if (!isOpen) {
      reset()
    }
  }, [isOpen, reset])

  const closeAndReset = () => {
    reset()
    onClose()
  }

  const onSubmit = async (data: ServiceRequestFormData) => {
    setIsSubmitting(true)
    setError(null)

    const { error: insertError } = await supabase.from("service_requests").insert({
      title: data.title,
      description: data.description,
      client_id: data.clientId,
      category: data.category,
      priority: data.priority,
      status: "SUBMITTED",
      assignee_id: data.assigneeId || null,
      due_date: data.dueDate || null,
      organization_id: organizationId,
      created_by_id: userId,
    })

    if (insertError) {
      setError(insertError.message)
      setIsSubmitting(false)
      return
    }

    router.refresh()
    setIsSubmitting(false)
    closeAndReset()
  }

  return (
    <Dialog
      open={isOpen}
      onOpenChange={(open) => {
        if (!open) {
          closeAndReset()
        }
      }}
    >
      <DialogContent className="sm:max-w-[600px]">
        <DialogHeader>
          <DialogTitle>Create Service Request</DialogTitle>
          <DialogDescription>
            Create a new service request for a client.
          </DialogDescription>
        </DialogHeader>
        <form onSubmit={handleSubmit(onSubmit)} noValidate>
          <div className="grid gap-4 py-4">
            <div className="grid gap-2">
              <Label htmlFor="title">Title</Label>
              <Input
                id="title"
                {...register("title")}
                aria-invalid={errors.title ? "true" : "false"}
                placeholder="Enter service request title"
              />
              {errors.title && (
                <p className="text-sm text-red-500">{errors.title.message}</p>
              )}
            </div>

            <div className="grid gap-2">
              <Label htmlFor="description">Description</Label>
              <Textarea
                id="description"
                {...register("description")}
                placeholder="Enter description (optional)"
                rows={3}
              />
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div className="grid gap-2">
                <Label htmlFor="client">Client</Label>
                <Select
                  value={selectedClient}
                  onValueChange={(value) =>
                    setValue("clientId", value, {
                      shouldValidate: true,
                    })
                  }
                >
                  <SelectTrigger aria-invalid={errors.clientId ? "true" : "false"}>
                    <SelectValue placeholder={clients.length ? "Select client" : "Loading clients..."} />
                  </SelectTrigger>
                  <SelectContent>
                    {clients.map((client) => (
                      <SelectItem key={client.id} value={client.id}>
                        {client.name}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
                {errors.clientId && (
                  <p className="text-sm text-red-500">{errors.clientId.message}</p>
                )}
              </div>

              <div className="grid gap-2">
                <Label htmlFor="category">Category</Label>
                <Select
                  value={selectedCategory}
                  onValueChange={(value: any) =>
                    setValue("category", value, {
                      shouldValidate: true,
                    })
                  }
                >
                  <SelectTrigger aria-invalid={errors.category ? "true" : "false"}>
                    <SelectValue placeholder="Select category" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="LICENSE_NEW">New License</SelectItem>
                    <SelectItem value="LICENSE_RENEWAL">License Renewal</SelectItem>
                    <SelectItem value="PRO_SERVICE">PRO Service</SelectItem>
                    <SelectItem value="VISA_SERVICE">Visa Service</SelectItem>
                    <SelectItem value="DOCUMENT_CLEARING">Document Clearing</SelectItem>
                    <SelectItem value="OTHER">Other</SelectItem>
                  </SelectContent>
                </Select>
                {errors.category && (
                  <p className="text-sm text-red-500">{errors.category.message}</p>
                )}
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div className="grid gap-2">
                <Label htmlFor="priority">Priority</Label>
                <Select
                  value={selectedPriority}
                  onValueChange={(value: any) =>
                    setValue("priority", value, {
                      shouldValidate: true,
                    })
                  }
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Select priority" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="LOW">Low</SelectItem>
                    <SelectItem value="MEDIUM">Medium</SelectItem>
                    <SelectItem value="HIGH">High</SelectItem>
                    <SelectItem value="URGENT">Urgent</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div className="grid gap-2">
                <Label htmlFor="assignee">Assignee</Label>
                <Select
                  value={selectedAssignee}
                  onValueChange={(value) =>
                    setValue("assigneeId", value, {
                      shouldDirty: true,
                    })
                  }
                >
                  <SelectTrigger>
                    <SelectValue placeholder={assignees.length ? "Select assignee" : "Loading team..."} />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="">Unassigned</SelectItem>
                    {assignees.map((assignee) => (
                      <SelectItem key={assignee.id} value={assignee.id}>
                        {assignee.name}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>
            </div>

            <div className="grid gap-2">
              <Label htmlFor="dueDate">Due Date</Label>
              <Input
                id="dueDate"
                type="date"
                {...register("dueDate")}
                aria-invalid={errors.dueDate ? "true" : "false"}
              />
              {errors.dueDate && (
                <p className="text-sm text-red-500">{errors.dueDate.message}</p>
              )}
              <p className="text-xs text-gray-500">Set a target date to help the team prioritize.</p>
            </div>
          </div>

          <DialogFooter>
            <Button
              type="button"
              variant="outline"
              onClick={closeAndReset}
              disabled={isSubmitting}
            >
              Cancel
            </Button>
            <Button type="submit" disabled={isSubmitting}>
              {isSubmitting ? "Creating..." : "Create Request"}
            </Button>
          </DialogFooter>
          {error && (
            <p className="rounded-md bg-red-50 p-3 text-sm text-red-600" role="alert">
              {error}
            </p>
          )}
        </form>
      </DialogContent>
    </Dialog>
  )
}