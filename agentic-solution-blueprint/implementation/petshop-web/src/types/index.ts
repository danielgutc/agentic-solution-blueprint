export interface Product {
  id: string
  name: string
  description: string
  price: number
  imageUrl: string | null
  status: 'Active' | 'Inactive' | 'OutOfStock'
  inventoryCount: number
  category: Category
}

export interface Category {
  id: string
  name: string
  description: string | null
  parentCategoryId: string | null
}

export interface Paging<T> {
  items: T[]
  totalCount: number
  page: number
  pageSize: number
  hasNextPage: boolean
}

export interface CartItem {
  id: string
  productId: string
  productName: string
  unitPrice: number
  quantity: number
  lineTotal: number
}

export interface Cart {
  items: CartItem[]
  subtotal: number
  tax: number
  total: number
  itemCount: number
}

export interface Order {
  id: string
  orderNumber: string
  customerId: string
  status: 'Pending' | 'Processing' | 'Shipped' | 'Delivered' | 'Cancelled'
  totalAmount: number
  currency: string
  items: OrderItem[]
  createdAt: string
}

export interface OrderItem {
  productId: string
  productName: string
  quantity: number
  unitPrice: number
  totalPrice: number
}

export interface UserProfile {
  id: string
  email: string
  firstName: string
  lastName: string
  phone: string | null
  address: string | null
  role: 'Customer' | 'Admin'
}

export interface AuthResponse {
  accessToken: string
  refreshToken: string
  expiresIn: number
}

export interface RegisterRequest {
  email: string
  password: string
  firstName: string
  lastName: string
}

export interface LoginRequest {
  email: string
  password: string
}

export interface PlaceOrderRequest {
  cartId: string
}

export interface UpdateOrderStatusRequest {
  status: 'Pending' | 'Processing' | 'Shipped' | 'Delivered' | 'Cancelled'
}
