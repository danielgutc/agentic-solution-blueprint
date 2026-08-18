import { create } from 'zustand'
import type { CartItem } from '../types'

interface CartState {
  items: CartItem[]
  subtotal: number
  tax: number
  total: number
  itemCount: number
  addItem: (item: Omit<CartItem, 'lineTotal'>) => void
  updateItem: (itemId: string, quantity: number) => void
  removeItem: (itemId: string) => void
  clearCart: () => void
  calculateTotals: () => void
}

export const useCartStore = create<CartState>((set) => ({
  items: [],
  subtotal: 0,
  tax: 0,
  total: 0,
  itemCount: 0,

  addItem: (item) => set((state) => {
    const existingIndex = state.items.findIndex((i) => i.productId === item.productId)
    let newItems: CartItem[]
    if (existingIndex >= 0) {
      newItems = [...state.items]
      newItems[existingIndex] = {
        ...newItems[existingIndex],
        quantity: newItems[existingIndex].quantity + item.quantity,
        lineTotal: (newItems[existingIndex].quantity + item.quantity) * newItems[existingIndex].unitPrice,
      }
    } else {
      newItems = [...state.items, { ...item, lineTotal: item.quantity * item.unitPrice }]
    }
    const subtotal = newItems.reduce((sum, i) => sum + i.lineTotal, 0)
    const tax = subtotal * 0.08 // 8% tax
    return { items: newItems, subtotal, tax, total: subtotal + tax, itemCount: newItems.reduce((s, i) => s + i.quantity, 0) }
  }),

  updateItem: (itemId, quantity) => set((state) => {
    const newItems = state.items.map((i) =>
      i.id === itemId ? { ...i, quantity, lineTotal: quantity * i.unitPrice } : i
    ).filter((i) => i.quantity > 0)
    const subtotal = newItems.reduce((sum, i) => sum + i.lineTotal, 0)
    const tax = subtotal * 0.08
    return { items: newItems, subtotal, tax, total: subtotal + tax, itemCount: newItems.reduce((s, i) => s + i.quantity, 0) }
  }),

  removeItem: (itemId) => set((state) => {
    const newItems = state.items.filter((i) => i.id !== itemId)
    const subtotal = newItems.reduce((sum, i) => sum + i.lineTotal, 0)
    const tax = subtotal * 0.08
    return { items: newItems, subtotal, tax, total: subtotal + tax, itemCount: newItems.reduce((s, i) => s + i.quantity, 0) }
  }),

  clearCart: () => set({ items: [], subtotal: 0, tax: 0, total: 0, itemCount: 0 }),

  calculateTotals: () => set((state) => {
    const subtotal = state.items.reduce((sum, i) => sum + i.lineTotal, 0)
    const tax = subtotal * 0.08
    return { subtotal, tax, total: subtotal + tax }
  }),
}))

export function useCart() {
  const store = useCartStore()
  return {
    items: store.items,
    subtotal: store.subtotal,
    tax: store.tax,
    total: store.total,
    itemCount: store.itemCount,
    addItem: store.addItem,
    updateItem: store.updateItem,
    removeItem: store.removeItem,
    clearCart: store.clearCart,
    calculateTotals: store.calculateTotals,
  }
}
