import { useEffect } from 'react'
import { useAuthStore } from '../stores/authStore'

export function useLoadUser() {
  const loadUser = useAuthStore((s) => s.loadUser)

  useEffect(() => {
    loadUser()
  }, [loadUser])
}
