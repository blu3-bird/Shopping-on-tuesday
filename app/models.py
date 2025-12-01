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

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    stock = db.Column(db.Integer,default=1)
    category = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(255))

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