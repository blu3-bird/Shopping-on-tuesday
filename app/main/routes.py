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
from flask import render_template, current_app , make_response
from app.constants import FEATURED_PRODUCTS_LIMIT, RELATED_PRODUCTS_LIMIT
from app.models import Product
from app.utils import get_recently_viewed, add_to_recently_viewed

@main.route('/')
def index():
    """
    Render the homepage with featured products.

    Fetches a limited number of products from the database to display
    on the homepage as featured or latest items.
    """

    featured_products = Product.query.limit(FEATURED_PRODUCTS_LIMIT).all()

    instagram_url = current_app.config["INSTAGRAM_URL"]

    return render_template(
        'main/index.html',
        products=featured_products,
        instagram_url=instagram_url
    )


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
    
    product = Product.query.get_or_404(product_id)

    related_products = Product.query.filter(
        Product.category == product.category,
        Product.id != product.id
    ).limit(RELATED_PRODUCTS_LIMIT).all()


    recently_viewed_products = []
    recently_viewed_ids = get_recently_viewed()

    if recently_viewed_ids:
        recently_viewed_products = Product.query.filter(
            Product.id.in_(recently_viewed_ids),
            Product.id != product.id
        ).all()

        recently_viewed_products.sort(
            key=lambda p : recently_viewed_ids.index(p.id)
        ) 

    response = make_response(
        render_template(
            'main/product_detail.html',
            product = product,
            related_products=related_products,
            recently_viewed_products = recently_viewed_products
        )
    )

    response = add_to_recently_viewed(response, product_id)

    return response