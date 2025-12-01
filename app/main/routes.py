"""
Public-facing routes for the main user interface.

This module defines the routes responsible for rendering the homepage,
product listings, and individual product details. These routes fetch data
from the Product model and display it to users through the corresponding
HTML templates.

Routes:
    - /               : Homepage with featured products.
    - /products       : Full list of available products.
    - /products/<id>  : Detailed view of a specific product with related items.
"""

from app.main import main
from flask import render_template
from app.models import Product

@main.route('/')
def index():
    """
    Render the homepage with featured products.

    Fetches a limited number of products from the database to display
    on the homepage as featured or latest items.

    Returns:
        Response: Rendered homepage template with product data.
    """

    products = Product.query.limit(6).all()

    return render_template('main/index.html',products=products)

@main.route('/products')
def products():
    """
    Display the complete list of products.

    Retrieves all available products from the database and renders them
    on the main products listing page.

    Returns:
        Response: Rendered products listing HTML page with all products.
    """
    all_products = Product.query.all()
    return render_template ('main/products.html', products=all_products)


@main.route('/products/<int:product_id>')
def product_detail(product_id):
    """
    Display detailed information about a single product.

    Fetches a specific product by its ID. Additionally, retrieves a list
    of related products from the same category (excluding the current product)
    to show recommendations.

    Args:
        product_id (int): ID of the product to display.

    Returns:
        Response: Rendered product detail page with the selected product
                  and related product suggestions.
    """

    product = Product.query.get_or_404(product_id)

    related_product = Product.query.filter(
        Product.category == product.category,
        Product.id != product.id).limit(4).all()
    
    return render_template('main/product_detail.html',
                           product=product,
                           related_product=related_product)