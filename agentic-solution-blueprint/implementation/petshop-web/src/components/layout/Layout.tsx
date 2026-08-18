import React from 'react'
import { Link, useNavigate, useLocation } from 'react-router-dom'
import { useAuth } from '../stores/authStore'

const Layout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { isAuthenticated, isAdmin, logout } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()

  const handleLogout = async () => {
    await logout()
    navigate('/')
  }

  return (
    <div className="layout">
      <header className="header">
        <div className="container header-content">
          <Link to="/" className="logo">
            🐾 PetShop
          </Link>
          <nav className="nav">
            <Link to="/catalog">Catalog</Link>
            {isAuthenticated && (
              <>
                <Link to="/cart">Cart</Link>
                <Link to="/orders">Orders</Link>
                <Link to="/profile">Profile</Link>
                {isAdmin && <Link to="/admin">Admin</Link>}
              </>
            )}
          </nav>
          <div className="header-actions">
            {isAuthenticated ? (
              <button onClick={handleLogout} className="btn-secondary">Logout</button>
            ) : (
              <>
                <Link to="/login"><button className="btn-secondary">Login</button></Link>
                <Link to="/register"><button className="btn-primary">Register</button></Link>
              </>
            )}
          </div>
        </div>
      </header>
      <main className="main">
        <div className="container">
          {children}
        </div>
      </main>
      <footer className="footer">
        <div className="container">
          <p>&copy; {new Date().getFullYear()} PetShop. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}

export default Layout
