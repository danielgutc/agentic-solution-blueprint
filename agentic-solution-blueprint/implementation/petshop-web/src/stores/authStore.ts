import { create } from 'zustand'
import { authApi, setAccessToken, setRefreshToken, clearAuth, getAccessToken, getRefreshToken } from '../api/auth'
import type { AuthResponse, RegisterRequest, LoginRequest, UserProfile } from '../types'

interface AuthState {
  user: UserProfile | null
  isAuthenticated: boolean
  isAdmin: boolean
  isLoading: boolean
  login: (data: LoginRequest) => Promise<void>
  register: (data: RegisterRequest) => Promise<void>
  logout: () => Promise<void>
  refresh: () => Promise<void>
  loadUser: () => Promise<void>
}

export const useAuthStore = create<AuthState>((set, get) => ({
  user: null,
  isAuthenticated: false,
  isAdmin: false,
  isLoading: false,

  login: async (data) => {
    set({ isLoading: true })
    try {
      const response: AuthResponse = await authApi.login(data)
      setAccessToken(response.accessToken)
      setRefreshToken(response.refreshToken)
      set({ isAuthenticated: true, isLoading: false })
      await get().loadUser()
    } catch (error) {
      set({ isLoading: false })
      throw error
    }
  },

  register: async (data) => {
    set({ isLoading: true })
    try {
      const response: AuthResponse = await authApi.register(data)
      setAccessToken(response.accessToken)
      setRefreshToken(response.refreshToken)
      set({ isAuthenticated: true, isLoading: false })
      await get().loadUser()
    } catch (error) {
      set({ isLoading: false })
      throw error
    }
  },

  logout: async () => {
    try {
      await authApi.logout()
    } finally {
      clearAuth()
      set({ user: null, isAuthenticated: false, isAdmin: false })
    }
  },

  refresh: async () => {
    const refreshToken = getRefreshToken()
    if (!refreshToken) {
      clearAuth()
      set({ user: null, isAuthenticated: false, isAdmin: false })
      return
    }
    try {
      const response: AuthResponse = await authApi.refresh(refreshToken)
      setAccessToken(response.accessToken)
      setRefreshToken(response.refreshToken)
      set({ isAuthenticated: true })
    } catch {
      clearAuth()
      set({ user: null, isAuthenticated: false, isAdmin: false })
    }
  },

  loadUser: async () => {
    const token = getAccessToken()
    if (!token) {
      set({ user: null, isAuthenticated: false, isAdmin: false })
      return
    }
    try {
      const user = await (await import('../api/client')).usersApi.getProfile()
      const isAdmin = user.role === 'Admin'
      set({ user, isAuthenticated: true, isAdmin })
    } catch {
      await get().refresh()
    }
  },
}))

export function useAuth() {
  const store = useAuthStore()
  return {
    user: store.user,
    isAuthenticated: store.isAuthenticated,
    isAdmin: store.isAdmin,
    isLoading: store.isLoading,
    login: store.login,
    register: store.register,
    logout: store.logout,
    refresh: store.refresh,
    loadUser: store.loadUser,
  }
}
