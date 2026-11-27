# Phase 3: Cart + Orders

**Status:** Pending approval  
**Goal:** Add customer shopping cart and order management to the store.

---

## 1. Database Models

### Cart model
| Field | Type | Purpose |
|-------|------|---------|
| id | Integer | Primary key |
| user_id | Integer | Customer ID (nullable for guest carts) |
| session_id | String | Session ID for guest users |
| created_at | DateTime | Cart creation time |
| updated_at | DateTime | Last update time |

### CartItem model
| Field | Type | Purpose |
|-------|------|---------|
| id | Integer | Primary key |
| cart_id | Integer | Foreign key to Cart |
| product_id | Integer | Foreign key to Product |
| quantity | Integer | Quantity of product |
| added_at | DateTime | When added to cart |

### Order model
| Field | Type | Purpose |
|-------|------|---------|
| id | Integer | Primary key |
| order_number | String | Unique order number (e.g., ORD-1001) |
| user_id | Integer | Customer ID |
| customer_name | String | Customer name |
| customer_email | String | Customer email |
| customer_phone | String | Customer phone |
| total_amount | Float | Order total |
| status | String | pending, paid, shipped, delivered, cancelled |
| payment_status | String | unpaid, paid, failed, refunded |
| shipping_address | Text | Delivery address |
| created_at | DateTime | Order creation time |
| updated_at | DateTime | Last update time |

### OrderItem model
| Field | Type | Purpose |
|-------|------|---------|
| id | Integer | Primary key |
| order_id | Integer | Foreign key to Order |
| product_id | Integer | Foreign key to Product |
| quantity | Integer | Quantity ordered |
| price | Float | Price at time of order |

---

## 2. Customer Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/cart` | GET | View cart contents |
| `/cart/add/<product_id>` | POST | Add product to cart |
| `/cart/remove/<item_id>` | POST | Remove item from cart |
| `/cart/update/<item_id>` | POST | Update item quantity |
| `/checkout` | GET | Checkout page (order summary) |
| `/checkout` | POST | Place order |
| `/order/<order_id>` | GET | Order confirmation page |
| `/orders` | GET | Customer order history |

---

## 3. Admin Routes (new)

| Route | Method | Purpose |
|-------|--------|---------|
| `/admin/orders` | GET | List all orders |
| `/admin/orders/<id>` | GET | Order detail |
| `/admin/orders/<id>/status` | POST | Update order status |

---

## 4. Cart Logic

- Guest users: cart stored in session (cookie-based)
- Logged-in users: cart stored in database
- Merge guest cart into user cart on login
- Calculate total from product selling_price (with Meesho markup)
- Stock validation before placing order

---

## 5. Verification

- Add product to cart from product page
- View cart with correct totals
- Place order → order created in database
- Admin can view and update order status
- Order confirmation page shows order details

---

## Next phase (Phase 4): Payments

Payment integration (Razorpay/UPI/Stripe) after cart/orders work.

---

## Approval needed

Reply "Approved" for Phase 3, and I'll start building. Nothing is built until you say so.
