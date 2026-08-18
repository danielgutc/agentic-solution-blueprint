import React from 'react'
import { Link } from 'react-router-dom'

const Home: React.FC = () => {
  return (
    <div className="home">
      <section className="hero">
        <h1>Welcome to PetShop</h1>
        <p>Your one-stop shop for all your pet needs</p>
        <Link to="/catalog">
          <button className="btn-primary" style={{ marginTop: '16px', padding: '12px 32px', fontSize: '16px' }}>
            Browse Catalog
          </button>
        </Link>
      </section>
      <section className="featured" style={{ marginTop: '48px' }}>
        <h2>Featured Products</h2>
        <div className="product-grid">
          <div className="card">
            <p>Coming soon...</p>
          </div>
        </div>
      </section>
    </div>
  )
}

export default Home
