import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../stores/authStore'
import type { LoginRequest } from '../types'

const Login: React.FC = () => {
  const { login, isLoading } = useAuth()
  const navigate = useNavigate()
  const [formData, setFormData] = useState<LoginRequest>({
    email: '',
    password: '',
  })
  const [error, setError] = useState('')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')
    try {
      await login(formData)
      navigate('/')
    } catch {
      setError('Invalid email or password.')
    }
  }

  return (
    <div className="auth-form">
      <h1>Login</h1>
      {error && <p className="error">{error}</p>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            id="email"
            type="email"
            value={formData.email}
            onChange={(e) => setFormData({ ...formData, email: e.target.value })}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            id="password"
            type="password"
            value={formData.password}
            onChange={(e) => setFormData({ ...formData, password: e.target.value })}
            required
          />
        </div>
        <button type="submit" className="btn-primary" disabled={isLoading}>
          {isLoading ? 'Logging in...' : 'Login'}
        </button>
      </form>
      <p style={{ marginTop: '16px' }}>
        Don't have an account? <Link to="/register">Register</Link>
      </p>
    </div>
  )
}

export default Login
