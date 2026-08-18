import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { catalogApi } from '../api/client'
import type { Product, Category } from '../types'

const Catalog: React.FC = () => {
  const [products, setProducts] = useState<Product[]>([])
  const [categories, setCategories] = useState<Category[]>([])
  const [search, setSearch] = useState('')
  const [selectedCategory, setSelectedCategory] = useState<string>('')
  const [minPrice, setMinPrice] = useState<number | undefined>()
  const [maxPrice, setMaxPrice] = useState<number | undefined>()
  const [page, setPage] = useState(1)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    loadCategories()
    loadProducts()
  }, [selectedCategory, search, minPrice, maxPrice, page])

  const loadCategories = async () => {
    try {
      const data = await catalogApi.getCategories()
      setCategories(data)
    } catch (error) {
      console.error('Failed to load categories:', error)
    }
  }

  const loadProducts = async () => {
    setLoading(true)
    try {
      const data = await catalogApi.getProducts({
        search: search || undefined,
        categoryId: selectedCategory || undefined,
        minPrice,
        maxPrice,
        page,
        pageSize: 20,
      })
      setProducts(data.items)
    } catch (error) {
      console.error('Failed to load products:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="catalog">
      <h1>Catalog</h1>
      <div className="catalog-filters">
        <input
          type="text"
          placeholder="Search products..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <select
          value={selectedCategory}
          onChange={(e) => setSelectedCategory(e.target.value)}
        >
          <option value="">All Categories</option>
          {categories.map((cat) => (
            <option key={cat.id} value={cat.id}>{cat.name}</option>
          ))}
        </select>
        <input
          type="number"
          placeholder="Min Price"
          value={minPrice ?? ''}
          onChange={(e) => setMinPrice(e.target.value ? Number(e.target.value) : undefined)}
        />
        <input
          type="number"
          placeholder="Max Price"
          value={maxPrice ?? ''}
          onChange={(e) => setMaxPrice(e.target.value ? Number(e.target.value) : undefined)}
        />
      </div>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <div className="product-grid">
          {products.map((product) => (
            <div key={product.id} className="card product-card">
              <Link to={`/products/${product.id}`}>
                <h3>{product.name}</h3>
                <p className="price">${product.price.toFixed(2)}</p>
                <p className="status">{product.status}</p>
                <p className="inventory">Stock: {product.inventoryCount}</p>
              </Link>
            </div>
          ))}
        </div>
      )}
      <div className="pagination">
        <button onClick={() => setPage(p => Math.max(1, p - 1))} disabled={page === 1}>
          Previous
        </button>
        <span>Page {page}</span>
        <button onClick={() => setPage(p => p + 1)}>Next</button>
      </div>
    </div>
  )
}

export default Catalog
