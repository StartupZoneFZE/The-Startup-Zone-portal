"use client"

import Link from "next/link"
import { usePathname } from "next/navigation"
import { cn } from "@/lib/utils"
import {
  Home,
  FileText,
  Users,
  FolderOpen,
  Calendar,
  CreditCard,
  Settings,
  BarChart,
  X,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { createClient } from "@/lib/supabase/client"

interface SidebarProps {
  className?: string
  isMobile?: boolean
  onClose?: () => void
  onNavigate?: () => void
  user?: { email?: string | null; user_metadata?: Record<string, any> } | null
  onSignOut?: () => void
}

const navigation = [
  { name: "Dashboard", href: "/", icon: Home },
  { name: "Service Requests", href: "/service-requests", icon: FileText },
  { name: "Clients", href: "/clients", icon: Users },
  { name: "Documents", href: "/documents", icon: FolderOpen },
  { name: "Renewals", href: "/renewals", icon: Calendar },
  { name: "Payments", href: "/payments", icon: CreditCard },
  { name: "Reports", href: "/reports", icon: BarChart },
  { name: "Settings", href: "/settings", icon: Settings },
]

export function Sidebar({ className, isMobile, onClose, onNavigate, user, onSignOut }: SidebarProps) {
  const pathname = usePathname()

  const displayName = user?.user_metadata?.name || user?.email || "Signed in"

  return (
    <div
      className={cn(
        "flex h-full w-64 flex-col bg-gray-900 transition-transform",
        isMobile ? "translate-x-0" : "",
        className
      )}
    >
      <div className="flex h-16 items-center justify-between px-6">
        <h1 className="text-xl font-semibold text-white">TSZ Portal</h1>
        {isMobile && (
          <Button variant="ghost" size="icon" onClick={onClose} aria-label="Close menu">
            <X className="h-5 w-5 text-white" />
          </Button>
        )}
      </div>
      <nav className="flex-1 space-y-1 px-3 py-4">
        {navigation.map((item) => {
          const isActive = pathname === item.href
          return (
            <Link
              key={item.name}
              href={item.href}
              className={cn(
                "flex items-center rounded-lg px-3 py-2 text-sm font-medium transition-colors",
                isActive
                  ? "bg-gray-800 text-white"
                  : "text-gray-300 hover:bg-gray-800 hover:text-white"
              )}
              onClick={onNavigate}
            >
              <item.icon className="mr-3 h-5 w-5" />
              {item.name}
            </Link>
          )
        })}
      </nav>
      <div className="border-t border-gray-800 p-4">
        <div className="space-y-3">
          <div>
            <p className="text-sm font-medium text-white">{displayName}</p>
            <p className="text-xs text-gray-400">{user?.email}</p>
          </div>
          <Button variant="outline" size="sm" className="w-full bg-white/10 text-white hover:bg-white/20" onClick={onSignOut}>
            Sign out
          </Button>
        </div>
      </div>
    </div>
  )
}