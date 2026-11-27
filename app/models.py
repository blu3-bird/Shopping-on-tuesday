"""
Database models for the application.

This module contains the SQLAlchemy models used throughout the application,
including the Product model for storing product-related information and the
Admin model for authentication and user management. It also includes utility
methods for password hashing and verification, as well as automatic timestamp
handling for created and updated records.
"""

#app/models
from app import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class Product(db.Model):
    """
    Represents a product in the store.

    This model stores essential information about each product, including
    its name, price, category, stock availability, description, and image URL.
    Timestamps track when products are created and last updated.

    Attributes:
        id (int): Primary key identifier for the product.
        name (str): Name of the product. Cannot be null.
        price (float): Product price. Cannot be null.
        description (str): Optional long description of the product.
        stock (int): Available product stock. Defaults to 1.
        category (str): Product category (e.g., "anime", "stationery"). Cannot be null.
        image_url (str): Optional URL to the product image.
        created_at (datetime): Timestamp when the product was created.
        updated_at (datetime): Timestamp when the product was last updated.

    Returns:
        Product: An instance representing a product record in the database.
    """
    __tablename__ = 'product'

    # getting values from a db
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    stock = db.Column(db.Integer,default=1)
    category = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(255))

    original_price = db.Column(db.Float)
    discount_percentage = db.Column(db.Float)

    highlights = db.Column(db.Text)

    # Meesho dropshipping fields
    source_url = db.Column(db.String(500))
    meesho_price = db.Column(db.Float)
    markup_percentage = db.Column(db.Float, default=20.0)
    last_synced = db.Column(db.DateTime)
    is_imported = db.Column(db.Boolean, default=False)

    images = db.relationship('ProductImage',backref='product',lazy='dynamic',cascade='all, delete-orphan',order_by = 'ProductImage.display_order')

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    #helper function
    def __repr__(self):
        """
        Return a string representation of the product.

        Returns:
            str: Human-readable representation of the Product instance.
        """
        return f'<Product {self.name}>'
    
    @property
    def has_discount(self):
        # discount activity (True/False)
        return self.original_price and self.original_price > self.price

    @property
    def discount_amount(self):
        # discount amount
        if self.has_discount:
            return self.original_price - self.price
        return 0

    @property
    def calculated_discount_percent(self):
        """
        discount percentage
        
        :param self: Description
        """
        if self.discount_percentage:
            return self.discount_percentage
        if self.has_discount:
            return int(((self.original_price - self.price) / self.original_price) * 100)
        return 0
    
    @property
    def selling_price(self):
        """
        Calculate selling price based on Meesho price and markup percentage.
        
        Returns:
            float: Selling price = meesho_price * (1 + markup_percentage / 100)
        """
        if self.meesho_price and self.markup_percentage:
            return round(self.meesho_price * (1 + self.markup_percentage / 100), 2)
        return self.price
    
    @property
    def primary_image(self):
        """
        Docstring for primary_image
        Return Primary Img or First img if no primary img exists
        """
        
        primary = ProductImage.query.filter_by(
            product_id = self.id,
            is_primary=True
        ).first()

        if primary:
            return primary
        
        first_image = ProductImage.query.filter_by(
            product_id=self.id
        ).order_by(ProductImage.display_order).first()

        return first_image
    
    @property
    def get_image_url(self):
        """
        Docstring for get_image_url
        to get the primary image url of primary image
        """

        primary = self.primary_image

        if primary:
            return primary.image_url
        
        return self.image_url
    
class ProductImage(db.Model):
    """
    Docstring for ProductImage
    Represent an image associated with a product.
    """

    __tablename__ = 'productImage'

    id = db.Column(db.Integer, primary_key = True)

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'),nullable=False)

    display_order = db.Column(db.Integer,default=0)

    image_url = db.Column(db.String(500),nullable=False)

    is_primary = db.Column(db.Boolean,default=False)

    created_at = db.Column(db.DateTime,default = datetime.utcnow)

    def __repr__(self):
        return f'<Product Image {self.id} for product {self.product_id}>'

class Admin(db.Model,UserMixin):
    """
    Represents an admin user with authentication capabilities.

    Stores login and identity information for administrator accounts,
    including username, email, and hashed password. Provides helper methods
    for setting and verifying passwords.

    Attributes:
        id (int): Primary key identifier for the admin user.
        username (str): Unique username for login. Cannot be null.
        email (str): Unique admin email address. Cannot be null.
        password_hash (str): Hashed representation of the admin's password.
        created_at (datetime): Timestamp when the admin account was created.

    Methods:
        set_password(password): Generates and stores the hashed password.
        check_password(password): Validates a password against the stored hash.

    Returns:
        Admin: An instance representing an admin user record.
    """
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)

    username= db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    password_hash = db.Column(db.String(200))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self,password):
        """
        Hash and store the provided password.

        Args:
            password (str): Plain text password to be hashed.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        """
        Verify the provided password against the stored hash.

        Args:
            password (str): Plain text password to validate.

        Returns:
            bool: True if the password is correct, False otherwise.
        """
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        """
        Return a string representation of the admin user.

        Returns:
            str: Human-readable representation of the Admin instance.
        """
        return f'<Admin {self.username}>'


class Cart(db.Model):
    """
    Represents a shopping cart for customers.
    
    Stores cart information for both guest users (session-based) and
    logged-in users (database-backed). Each cart can have multiple items.
    
    Attributes:
        id (int): Primary key identifier for the cart.
        user_id (int): Foreign key to Admin (customer) - nullable for guest carts.
        session_id (str): Session ID for guest users.
        created_at (datetime): Timestamp when the cart was created.
        updated_at (datetime): Timestamp when the cart was last updated.
    """
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=True)
    session_id = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    items = db.relationship('CartItem', backref='cart', lazy='dynamic', cascade='all, delete-orphan')

    @property
    def total(self):
        """Calculate cart total from all items."""
        return sum(item.subtotal for item in self.items.all())

    @property
    def item_count(self):
        """Return total number of items in cart."""
        return sum(item.quantity for item in self.items.all())

    def __repr__(self):
        return f'<Cart {self.id} ({self.item_count} items)>'


class CartItem(db.Model):
    """
    Represents an item in a shopping cart.
    
    Attributes:
        id (int): Primary key identifier for the cart item.
        cart_id (int): Foreign key to Cart.
        product_id (int): Foreign key to Product.
        quantity (int): Quantity of the product.
        added_at (datetime): Timestamp when the item was added.
    """
    __tablename__ = 'cart_item'

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1, nullable=False)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    product = db.relationship('Product', backref='cart_items')

    @property
    def subtotal(self):
        """Calculate line item subtotal."""
        return self.product.selling_price * self.quantity

    def __repr__(self):
        return f'<CartItem {self.id} x{self.quantity} of {self.product.name}>'


class Order(db.Model):
    """
    Represents a customer order.
    
    Stores order information including customer details, total amount,
    and order/payment status.
    
    Attributes:
        id (int): Primary key identifier for the order.
        order_number (str): Unique order number (e.g., ORD-1001).
        user_id (int): Foreign key to Admin (customer).
        customer_name (str): Customer name.
        customer_email (str): Customer email address.
        customer_phone (str): Customer phone number.
        total_amount (float): Order total amount.
        status (str): Order status (pending, paid, shipped, delivered, cancelled).
        payment_status (str): Payment status (unpaid, paid, failed, refunded).
        shipping_address (text): Delivery address.
        created_at (datetime): Timestamp when the order was created.
        updated_at (datetime): Timestamp when the order was last updated.
    """
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(20), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(20), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')
    payment_status = db.Column(db.String(20), default='unpaid')
    shipping_address = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    items = db.relationship('OrderItem', backref='order', lazy='dynamic', cascade='all, delete-orphan')

    @staticmethod
    def generate_order_number():
        """Generate a unique order number."""
        import random
        import string
        return 'ORD-' + ''.join(random.choices(string.digits, k=6))

    def __repr__(self):
        return f'<Order {self.order_number} ({self.status})>'


class OrderItem(db.Model):
    """
    Represents an item in an order.
    
    Stores a snapshot of the product at the time of order.
    
    Attributes:
        id (int): Primary key identifier for the order item.
        order_id (int): Foreign key to Order.
        product_id (int): Foreign key to Product.
        quantity (int): Quantity ordered.
        price (float): Price at the time of order.
    """
    __tablename__ = 'order_item'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    # Relationships
    product = db.relationship('Product', backref='order_items')

    @property
    def subtotal(self):
        """Calculate line item subtotal."""
        return self.price * self.quantity

    def __repr__(self):
        return f'<OrderItem {self.id} x{self.quantity} of {self.product.name}>'