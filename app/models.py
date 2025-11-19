#app/models
from app import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class Product(db.Model):
    """Product Model for storing product information"""
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    stock = db.Column(db.Integer,default=1)
    category = db.Column(db.String(50), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    #helper function
    def __repr__(self):
        return f'<Product {self.name}>'

class Admin(db.Model,UserMixin):
    """Admin Model to store user data"""
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)

    username= db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    password_hash = db.Column(db.String(200))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self,password):
        """hashing the password"""
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        """Checking the password"""
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        return f'<Admin {self.username}>'