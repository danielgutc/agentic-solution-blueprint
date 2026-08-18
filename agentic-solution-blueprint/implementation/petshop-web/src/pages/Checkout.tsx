import React from 'react'

const Checkout: React.FC = () => {
  return (
    <div className="checkout">
      <h1>Checkout</h1>
      <div className="checkout-form card">
        <h2>Shipping Information</h2>
        <div className="form-group">
          <label htmlFor="fullName">Full Name</label>
          <input id="fullName" type="text" required />
        </div>
        <div className="form-group">
          <label htmlFor="address">Address</label>
          <input id="address" type="text" required />
        </div>
        <div className="form-group">
          <label htmlFor="city">City</label>
          <input id="city" type="text" required />
        </div>
        <h2>Payment Information</h2>
        <div className="form-group">
          <label htmlFor="cardNumber">Card Number</label>
          <input id="cardNumber" type="text" placeholder="1234 5678 9012 3456" required />
        </div>
        <div className="form-group">
          <label htmlFor="expiry">Expiry Date</label>
          <input id="expiry" type="text" placeholder="MM/YY" required />
        </div>
        <div className="form-group">
          <label htmlFor="cvv">CVV</label>
          <input id="cvv" type="text" placeholder="123" required />
        </div>
        <button className="btn-primary" style={{ width: '100%', padding: '12px' }}>
          Place Order
        </button>
      </div>
    </div>
  )
}

export default Checkout
