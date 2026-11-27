"""
Customer-facing routes for cart, checkout, and orders.

This module defines the routes responsible for handling the customer shopping
flow: adding products to cart, viewing cart, checking out, placing orders,
and viewing order history.

Routes:
    - /cart               : View cart contents.
    - /cart/add/<id>      : Add product to cart.
    - /cart/remove/<id>   : Remove item from cart.
    - /cart/update/<id>   : Update item quantity.
    - /checkout           : Checkout page and place order.
    - /order/<id>         : Order confirmation page.
    - /orders             : Customer order history.
"""

from flask import render_template, redirect, url_for, flash, request, session
from flask_login import current_user, login_required
from app.customer import customer
from app.models import db, Product, Cart, CartItem, Order, OrderItem
import uuid


def _get_or_create_cart():
    """Get or create a cart for the current user/session."""
    if current_user.is_authenticated:
        cart = Cart.query.filter_by(user_id=current_user.id).first()
        if not cart:
            cart = Cart(user_id=current_user.id)
            db.session.add(cart)
            db.session.commit()
    else:
        sid = session.get('cart_session_id')
        cart = None
        if sid:
            cart = Cart.query.filter_by(session_id=sid).first()
        if not cart:
            sid = str(uuid.uuid4())
            session['cart_session_id'] = sid
            cart = Cart(session_id=sid)
            db.session.add(cart)
            db.session.commit()
    return cart


@customer.route('/cart')
def cart():
    """View cart contents."""
    cart = _get_or_create_cart()
    items = cart.items.all()
    return render_template('customer/cart.html', cart=cart, items=items)


@customer.route('/cart/add/<int:product_id>', methods=['POST'])
def cart_add(product_id):
    """Add a product to the cart."""
    product = Product.query.get_or_404(product_id)
    cart = _get_or_create_cart()

    # Check if item already in cart
    existing = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    if existing:
        existing.quantity += 1
    else:
        item = CartItem(cart_id=cart.id, product_id=product_id, quantity=1)
        db.session.add(item)

    db.session.commit()
    flash(f'{product.name} added to cart', 'success')
    return redirect(request.referrer or url_for('main.index'))


@customer.route('/cart/remove/<int:item_id>', methods=['POST'])
def cart_remove(item_id):
    """Remove an item from the cart."""
    item = CartItem.query.get_or_404(item_id)
    cart = _get_or_create_cart()
    if item.cart_id != cart.id:
        flash('Unauthorized', 'error')
        return redirect(url_for('customer.cart'))

    product_name = item.product.name
    db.session.delete(item)
    db.session.commit()
    flash(f'{product_name} removed from cart', 'success')
    return redirect(url_for('customer.cart'))


@customer.route('/cart/update/<int:item_id>', methods=['POST'])
def cart_update(item_id):
    """Update item quantity in cart."""
    item = CartItem.query.get_or_404(item_id)
    cart = _get_or_create_cart()
    if item.cart_id != cart.id:
        flash('Unauthorized', 'error')
        return redirect(url_for('customer.cart'))

    try:
        quantity = int(request.form.get('quantity', 1))
    except (ValueError, TypeError):
        quantity = 1

    if quantity < 1:
        db.session.delete(item)
        flash('Item removed from cart', 'success')
    else:
        item.quantity = quantity
        flash('Cart updated', 'success')

    db.session.commit()
    return redirect(url_for('customer.cart'))


@customer.route('/checkout', methods=['GET', 'POST'])
def checkout():
    """Checkout page and place order."""
    cart = _get_or_create_cart()
    items = cart.items.all()

    if not items:
        flash('Your cart is empty', 'error')
        return redirect(url_for('customer.cart'))

    if request.method == 'POST':
        customer_name = request.form.get('customer_name', '').strip()
        customer_email = request.form.get('customer_email', '').strip()
        customer_phone = request.form.get('customer_phone', '').strip()
        shipping_address = request.form.get('shipping_address', '').strip()

        if not all([customer_name, customer_email, customer_phone, shipping_address]):
            flash('Please fill in all fields', 'error')
            return render_template('customer/checkout.html', cart=cart, items=items)

        # Create order
        order = Order(
            order_number=Order.generate_order_number(),
            user_id=current_user.id if current_user.is_authenticated else None,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone,
            total_amount=cart.total,
            status='pending',
            payment_status='unpaid',
            shipping_address=shipping_address,
        )
        db.session.add(order)
        db.session.flush()

        # Create order items from cart
        for item in items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.product.selling_price,
            )
            db.session.add(order_item)

        # Clear cart
        db.session.query(CartItem).filter_by(cart_id=cart.id).delete()
        db.session.commit()

        flash(f'Order {order.order_number} placed successfully!', 'success')
        return redirect(url_for('customer.order_detail', order_id=order.id))

    return render_template('customer/checkout.html', cart=cart, items=items)


@customer.route('/order/<int:order_id>')
def order_detail(order_id):
    """Order confirmation page."""
    order = Order.query.get_or_404(order_id)
    # Ensure user can only view their own orders
    if current_user.is_authenticated and order.user_id != current_user.id:
        flash('Unauthorized', 'error')
        return redirect(url_for('main.index'))
    items = order.items.all()
    return render_template('customer/order_detail.html', order=order, items=items)


@customer.route('/orders')
@login_required
def orders():
    """Customer order history."""
    orders_list = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc()).all()
    return render_template('customer/orders.html', orders=orders_list)


@customer.route('/admin/orders')
@login_required
def admin_orders():
    """Admin: list all orders."""
    orders_list = Order.query.order_by(Order.created_at.desc()).all()
    return render_template('admin/orders.html', orders=orders_list)


@customer.route('/admin/orders/<int:order_id>')
@login_required
def admin_order_detail(order_id):
    """Admin: order detail."""
    order = Order.query.get_or_404(order_id)
    items = order.items.all()
    return render_template('admin/order_detail.html', order=order, items=items)


@customer.route('/admin/orders/<int:order_id>/status', methods=['POST'])
@login_required
def admin_update_order_status(order_id):
    """Admin: update order status."""
    order = Order.query.get_or_404(order_id)
    new_status = request.form.get('status', '').strip()
    valid_statuses = ['pending', 'paid', 'shipped', 'delivered', 'cancelled']

    if new_status not in valid_statuses:
        flash('Invalid status', 'error')
        return redirect(url_for('customer.admin_order_detail', order_id=order_id))

    order.status = new_status
    if new_status == 'paid':
        order.payment_status = 'paid'
    db.session.commit()
    flash(f'Order {order.order_number} status updated to {new_status}', 'success')
    return redirect(url_for('customer.admin_order_detail', order_id=order_id))
