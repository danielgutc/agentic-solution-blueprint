import axios from 'axios'
import type { AuthResponse, RegisterRequest, LoginRequest } from '../types'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8080/api'

export const authApi = {
  async register(data: RegisterRequest): Promise<AuthResponse> {
    const response = await axios.post(`${API_URL}/auth/register`, data)
    return response.data
  },

  async login(data: LoginRequest): Promise<AuthResponse> {
    const response = await axios.post(`${API_URL}/auth/login`, data)
    return response.data
  },

  async refresh(refreshToken: string): Promise<AuthResponse> {
    const response = await axios.post(`${API_URL}/auth/refresh`, { refreshToken })
    return response.data
  },

  async logout(): Promise<void> {
    await axios.post(`${API_URL}/auth/logout`, {}, {
      headers: { Authorization: `Bearer ${getAccessToken()}` }
    })
  },
}

export function getAccessToken(): string | null {
  return localStorage.getItem('access_token')
}

export function setAccessToken(token: string): void {
  localStorage.setItem('access_token', token)
}

export function getRefreshToken(): string | null {
  return localStorage.getItem('refresh_token')
}

export function setRefreshToken(token: string): void {
  localStorage.setItem('refresh_token', token)
}

export function clearAuth(): void {
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
}

export function isAuthenticated(): boolean {
  return !!getAccessToken()
}
