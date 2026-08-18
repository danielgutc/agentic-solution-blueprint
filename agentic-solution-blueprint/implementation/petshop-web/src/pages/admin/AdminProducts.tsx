import React from 'react'

const AdminProducts: React.FC = () => {
  return (
    <div className="admin-products">
      <h2>Product Management</h2>
      <button className="btn-primary" style={{ marginBottom: '16px' }}>Add Product</button>
      <p className="card">Product list will appear here.</p>
    </div>
  )
}

export default AdminProducts
