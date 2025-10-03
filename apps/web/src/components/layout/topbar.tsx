"use client"

import { Search, Bell, User, Menu } from "lucide-react"
import { Button } from "@/components/ui/button"

interface TopbarProps {
  onMenuClick?: () => void
  user?: { email?: string | null; user_metadata?: Record<string, any> } | null
  onSignOut?: () => void
}

export function Topbar({ onMenuClick, user, onSignOut }: TopbarProps) {
  const displayName = user?.user_metadata?.name || user?.email || "Portal User"

  return (
    <header className="flex h-16 items-center justify-between border-b bg-white px-4 md:px-6">
      <div className="flex items-center space-x-3 md:space-x-0">
        <Button
          variant="ghost"
          size="icon"
          className="md:hidden"
          onClick={onMenuClick}
          aria-label="Open menu"
        >
          <Menu className="h-5 w-5" />
        </Button>
        <div className="relative hidden w-full max-w-md md:block">
          <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-gray-400" />
          <input
            type="text"
            placeholder="Search..."
            className="w-full rounded-lg border border-gray-300 py-2 pl-10 pr-4 text-sm focus:border-primary focus:outline-none"
          />
        </div>
      </div>
      <div className="flex items-center space-x-4">
        <span className="hidden text-sm font-medium text-gray-700 md:inline">{displayName}</span>
        <Button variant="ghost" size="icon">
          <Bell className="h-5 w-5" />
        </Button>
        <Button variant="ghost" size="icon" onClick={onSignOut} aria-label="Sign out">
          <User className="h-5 w-5" />
        </Button>
      </div>
    </header>
  )
}