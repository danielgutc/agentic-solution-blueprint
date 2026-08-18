export function useCatalog() {
  // Placeholder for catalog data fetching hook
  // Will be implemented with React Query or SWR in production
  return {
    products: [],
    categories: [],
    isLoading: false,
    error: null as string | null,
  }
}

export function useOrders() {
  // Placeholder for order data fetching hook
  return {
    orders: [],
    isLoading: false,
    error: null as string | null,
  }
}
