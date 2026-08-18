import axios from 'axios'
import type { Product, Paging, Category, PlaceOrderRequest, Order, OrderListResponse } from '../types'
import { getAccessToken } from './auth'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8080/api'

function getHeaders(): Record<string, string> {
  const token = getAccessToken()
  return token ? { Authorization: `Bearer ${token}` } : {}
}

export const catalogApi = {
  async getProducts(params?: {
    search?: string
    categoryId?: string
    minPrice?: number
    maxPrice?: number
    page?: number
    pageSize?: number
  }): Promise<Paging<Product>> {
    const response = await axios.get(`${API_URL}/catalog/products`, {
      params,
      headers: getHeaders()
    })
    return response.data
  },

  async getProduct(id: string): Promise<Product> {
    const response = await axios.get(`${API_URL}/catalog/products/${id}`, {
      headers: getHeaders()
    })
    return response.data
  },

  async getCategories(): Promise<Category[]> {
    const response = await axios.get(`${API_URL}/catalog/categories`, {
      headers: getHeaders()
    })
    return response.data
  },

  async createProduct(data: {
    name: string
    description: string
    price: number
    categoryId: string
    imageUrl?: string
    inventoryCount: number
  }): Promise<Product> {
    const response = await axios.post(`${API_URL}/catalog/products`, data, {
      headers: getHeaders()
    })
    return response.data
  },

  async updateProduct(id: string, data: Partial<typeof data>): Promise<Product> {
    const response = await axios.put(`${API_URL}/catalog/products/${id}`, data, {
      headers: getHeaders()
    })
    return response.data
  },

  async deleteProduct(id: string): Promise<void> {
    await axios.delete(`${API_URL}/catalog/products/${id}`, {
      headers: getHeaders()
    })
  },
}

export const cartApi = {
  async getCart(): Promise<any> {
    const response = await axios.get(`${API_URL}/cart`, {
      headers: getHeaders()
    })
    return response.data
  },

  async addItem(productId: string, quantity: number): Promise<any> {
    const response = await axios.post(`${API_URL}/cart/items`, {
      productId,
      quantity
    }, {
      headers: getHeaders()
    })
    return response.data
  },

  async updateItem(itemId: string, quantity: number): Promise<any> {
    const response = await axios.put(`${API_URL}/cart/items/${itemId}`, {
      quantity
    }, {
      headers: getHeaders()
    })
    return response.data
  },

  async removeItem(itemId: string): Promise<void> {
    await axios.delete(`${API_URL}/cart/items/${itemId}`, {
      headers: getHeaders()
    })
  },

  async clearCart(): Promise<void> {
    await axios.delete(`${API_URL}/cart/clear`, {
      headers: getHeaders()
    })
  },
}

export const ordersApi = {
  async placeOrder(data: PlaceOrderRequest): Promise<Order> {
    const response = await axios.post(`${API_URL}/orders`, data, {
      headers: getHeaders()
    })
    return response.data
  },

  async getOrders(params?: {
    status?: string
    page?: number
    pageSize?: number
  }): Promise<OrderListResponse> {
    const response = await axios.get(`${API_URL}/orders`, {
      params,
      headers: getHeaders()
    })
    return response.data
  },

  async getOrder(id: string): Promise<Order> {
    const response = await axios.get(`${API_URL}/orders/${id}`, {
      headers: getHeaders()
    })
    return response.data
  },

  async updateOrderStatus(id: string, status: string): Promise<Order> {
    const response = await axios.put(`${API_URL}/orders/${id}/status`, {
      status
    }, {
      headers: getHeaders()
    })
    return response.data
  },
}

export const usersApi = {
  async getProfile(): Promise<any> {
    const response = await axios.get(`${API_URL}/users/profile`, {
      headers: getHeaders()
    })
    return response.data
  },

  async updateProfile(data: {
    firstName?: string
    lastName?: string
    phone?: string
    address?: string
  }): Promise<any> {
    const response = await axios.put(`${API_URL}/users/profile`, data, {
      headers: getHeaders()
    })
    return response.data
  },
}
