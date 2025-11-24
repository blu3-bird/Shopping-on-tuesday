from app.main import main
from flask import render_template
from app.models import Product

@main.route('/')
def index():
    """Homepage"""

    products = Product.query.limit(6).all()

    return render_template('main/index.html',products=products)

@main.route('/products')
def products():
    """Products listing page"""
    all_products = Product.query.all()
    return render_template ('main/products.html', products=all_products)


@main.route('/product/<int:product_id>')
def product_detail(product_id):
    """Product details route"""

    product = Product.query.get_or_404(product_id)

    related_product = Product.query.filter(
        Product.category == product.category,
        Product.id != product.id).limit(4).all()
    
    return render_template('main/product_detail.html',
                           product=product,
                           related_product=related_product)