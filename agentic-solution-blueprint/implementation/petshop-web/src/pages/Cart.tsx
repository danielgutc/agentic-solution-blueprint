import React from 'react'
import { useCart } from '../stores/cartStore'

const Cart: React.FC = () => {
  const { items, subtotal, tax, total, removeItem, updateItem } = useCart()

  if (items.length === 0) {
    return (
      <div className="cart">
        <h1>Shopping Cart</h1>
        <p>Your cart is empty.</p>
      </div>
    )
  }

  return (
    <div className="cart">
      <h1>Shopping Cart</h1>
      <div className="cart-items">
        {items.map((item) => (
          <div key={item.id} className="card cart-item">
            <div className="cart-item-info">
              <h3>{item.productName}</h3>
              <p className="price">${item.unitPrice.toFixed(2)}</p>
            </div>
            <div className="cart-item-quantity">
              <button onClick={() => updateItem(item.id, Math.max(1, item.quantity - 1))}>-</button>
              <span>{item.quantity}</span>
              <button onClick={() => updateItem(item.id, item.quantity + 1)}>+</button>
            </div>
            <div className="cart-item-total">
              <p>${item.lineTotal.toFixed(2)}</p>
              <button onClick={() => removeItem(item.id)} className="btn-danger">Remove</button>
            </div>
          </div>
        ))}
      </div>
      <div className="cart-summary card">
        <h3>Order Summary</h3>
        <div className="summary-row">
          <span>Subtotal:</span>
          <span>${subtotal.toFixed(2)}</span>
        </div>
        <div className="summary-row">
          <span>Tax (8%):</span>
          <span>${tax.toFixed(2)}</span>
        </div>
        <div className="summary-row total">
          <span>Total:</span>
          <span>${total.toFixed(2)}</span>
        </div>
        <a href="/checkout">
          <button className="btn-primary" style={{ width: '100%', marginTop: '16px', padding: '12px' }}>
            Proceed to Checkout
          </button>
        </a>
      </div>
    </div>
  )
}

export default Cart
