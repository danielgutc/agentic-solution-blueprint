import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../stores/authStore'
import type { RegisterRequest } from '../types'

const Register: React.FC = () => {
  const { register, isLoading } = useAuth()
  const navigate = useNavigate()
  const [formData, setFormData] = useState<RegisterRequest>({
    email: '',
    password: '',
    firstName: '',
    lastName: '',
  })
  const [error, setError] = useState('')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')
    try {
      await register(formData)
      navigate('/')
    } catch {
      setError('Registration failed. Please try again.')
    }
  }

  return (
    <div className="auth-form">
      <h1>Register</h1>
      {error && <p className="error">{error}</p>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="firstName">First Name</label>
          <input
            id="firstName"
            type="text"
            value={formData.firstName}
            onChange={(e) => setFormData({ ...formData, firstName: e.target.value })}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="lastName">Last Name</label>
          <input
            id="lastName"
            type="text"
            value={formData.lastName}
            onChange={(e) => setFormData({ ...formData, lastName: e.target.value })}
            required
          />
        </div>
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
            minLength={8}
          />
        </div>
        <button type="submit" className="btn-primary" disabled={isLoading}>
          {isLoading ? 'Registering...' : 'Register'}
        </button>
      </form>
      <p style={{ marginTop: '16px' }}>
        Already have an account? <Link to="/login">Login</Link>
      </p>
    </div>
  )
}

export default Register
