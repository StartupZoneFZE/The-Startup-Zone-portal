"use client"

import { useState, useEffect } from "react"
import { Sidebar } from "./sidebar"
import { Topbar } from "./topbar"
import { useRouter } from "next/navigation"
import { createClient } from "@/lib/supabase/client"

interface MainLayoutProps {
  children: React.ReactNode
}

export function MainLayout({ children }: MainLayoutProps) {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false)
  const [user, setUser] = useState<any>(null)
  const router = useRouter()

  useEffect(() => {
    const supabase = createClient()
    supabase.auth.getUser().then(({ data }) => {
      setUser(data.user)
    })
  }, [])

  const handleSignOut = async () => {
    const supabase = createClient()
    await supabase.auth.signOut()
    router.replace("/login")
    router.refresh()
  }

  const closeSidebar = () => setIsSidebarOpen(false)

  return (
    <div className="flex min-h-screen bg-gradient-to-b from-slate-50 to-white">
      <Sidebar
        className="hidden md:flex"
        onNavigate={closeSidebar}
        user={user}
        onSignOut={handleSignOut}
      />
      <div className="flex flex-1 flex-col">
        <Topbar onMenuClick={() => setIsSidebarOpen(true)} user={user} onSignOut={handleSignOut} />
        <main className="flex-1 overflow-y-auto p-4 md:p-6">
          <div className="mx-auto w-full max-w-7xl">{children}</div>
        </main>
      </div>
      {isSidebarOpen && (
        <div className="fixed inset-0 z-50 flex md:hidden" role="dialog" aria-modal="true">
          <div className="absolute inset-0 bg-black/50" onClick={closeSidebar} />
          <Sidebar
            isMobile
            onClose={closeSidebar}
            onNavigate={closeSidebar}
            className="relative z-10 h-full w-64 shadow-xl"
            user={user}
            onSignOut={handleSignOut}
          />
        </div>
      )}
    </div>
  )
}