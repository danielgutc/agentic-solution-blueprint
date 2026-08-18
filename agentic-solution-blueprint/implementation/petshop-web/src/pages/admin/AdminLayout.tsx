import React from 'react'
import { Outlet, Link } from 'react-router-dom'

const AdminLayout: React.FC = () => {
  return (
    <div className="admin">
      <h1>Admin Panel</h1>
      <nav className="admin-nav">
        <Link to="/admin" className={window.location.pathname === '/admin' ? 'active' : ''}>Products</Link>
        <Link to="/admin/orders" className={window.location.pathname === '/admin/orders' ? 'active' : ''}>Orders</Link>
      </nav>
      <div className="admin-content">
        <Outlet />
      </div>
    </div>
  )
}

export default AdminLayout
