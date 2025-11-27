from flask import redirect, render_template, flash, url_for
from flask_login import login_required, current_user
from app.admin import admin
from app.models import Product

@admin.route('/')
@login_required
def dashboard():
    """
    Docstring for dashboard
    """

    total_products=Product.query.count()
    anime_count=Product.query.filter_by(category='anime').count()
    stationary_count = Product.query.filter_by(category='stationary').count()
    low_stock=Product.query.filter(Product.stock <3).count()
    out_of_stock = Product.query.filter(Product.stock == 0).count

    recent_products = Product.query.order_by(Product.created_at.desc()).limit(5).all()

    return render_template('admin/dashboard.html',
                           total_products=total_products,
                           anime_count=anime_count,
                           stationary_count=stationary_count,
                           low_stock=low_stock,
                           out_of_stock=out_of_stock,
                           recent_products=recent_products)

@admin.route('/products')
@login_required
def products():
    """
    Docstring for products
    """

    products=Product.query.order_by(Product.created_at.desc()).all()
    return render_template('admin/product_list.html',products=products)