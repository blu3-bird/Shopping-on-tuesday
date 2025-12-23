"""
Admin route handlers for managing products and dashboard functionalities.

This module contains all the routes related to the admin panel, including:
- Displaying dashboard metrics
- Listing products
- Creating new products
- Editing existing products
- Deleting products

These routes are protected by authentication and interact with the Product model
to perform CRUD operations. Proper error handling and database transaction safety
are implemented for all write operations.
"""

from flask import redirect, render_template, flash, url_for
from flask_login import login_required, current_user
from app.admin import admin
from app.constants import LOW_STOCK_THRESHOLD, RECENT_PRODUCTS_LIMIT, CATEGORY_ANIME, CATEGORY_STATIONERY
from app.models import Product
from sqlalchemy.exc import DataError , OperationalError , IntegrityError,SQLAlchemyError
from app.admin.forms import ProductForm
from app import db


@admin.route('/')
@login_required
def dashboard():
    """
    Display the admin dashboard with product statistics.

    This route gathers various product-related metrics such as total count,
    category-wise counts, low-stock product count, and recently added products.
    The data is then rendered on the dashboard page.

    Returns:
        Response: Rendered admin dashboard HTML page with product statistics.
    """

    total_products=Product.query.count()
    anime_count=Product.query.filter_by(category=CATEGORY_ANIME).count()
    stationery_count = Product.query.filter_by(category=CATEGORY_STATIONERY).count()
    low_stock=Product.query.filter(Product.stock < LOW_STOCK_THRESHOLD).count()
    out_of_stock = Product.query.filter(Product.stock == 0).count()

    recent_products = Product.query.order_by(Product.created_at.desc()).limit(RECENT_PRODUCTS_LIMIT).all()

    return render_template('admin/dashboard.html',
                           total_products=total_products,
                           anime_count=anime_count,
                           stationery_count=stationery_count,
                           low_stock=low_stock,
                           out_of_stock=out_of_stock,
                           recent_products=recent_products)

@admin.route('/products')
@login_required
def products_list():
    """
    Display the list of all products for the admin.

    Products are shown in descending order of their creation date.

    Returns:
        Response: Rendered HTML page displaying the product list.
    """

    products = Product.query.order_by(Product.created_at.desc()).all()
    return render_template('admin/product_list.html',products = products)

@admin.route('/add-product', methods = ['GET', 'POST'])
@login_required
def add_product():
    """
    Create a new product and add it to the database.

    Handles both displaying the form (GET) and processing form submission (POST).
    Validates user input and inserts a new product into the database.
    If a database error occurs, the transaction is rolled back.

    Returns:
        Response: Rendered form page or redirect to the product list page.
    """
    form = ProductForm()

    if form.validate_on_submit():

        product = Product(
            name = form.name.data,
            price = form.price.data,
            original_price = form.original_price.data,
            discount_percentage = form.discount_percentage.data,
            highlights = form.highlights.data,
            category = form.category.data,
            stock = form.stock.data,
            description = form.description.data,
            image_url = form.image_url.data
        )

        try:
            db.session.add(product)
            db.session.commit()

            flash(f'Product {product.name} has been successfully added', 'success')

            return redirect(url_for('admin.products_list'))
        except (DataError, SQLAlchemyError, OperationalError, IntegrityError) as e:
            db.session.rollback()
            flash(f'Something Went Wrong, Please try again','error')
            return redirect(url_for('admin.add_product'))
    return render_template('admin/add_product.html', form = form)

@admin.route('/edit-product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    """
    Edit the details of an existing product.

    Fetches a product by ID and pre-fills the form with existing data.
    On submission, updates the product with new values.
    Rolls back if any database error occurs.

    Args:
        product_id (int): ID of the product to be edited.

    Returns:
        Response: Rendered edit form page or redirect after updating product.
    """

    product = Product.query.get_or_404(product_id)

    form = ProductForm(obj = product)

    if form.validate_on_submit():

        product.name = form.name.data
        product.price = form.price.data
        product.original_price = form.original_price.data
        product.discount_percentage = form.discount_percentage.data
        product.highlights = form.highlights.data
        product.category = form.category.data
        product.stock = form.stock.data
        product.description = form.description.data
        product.image_url = form.image_url.data

        try:
            db.session.commit()

            flash(f'Info Updated for Product: {product.name} has been updated!', 'success')

            return redirect(url_for('admin.products_list'))
        except (DataError, SQLAlchemyError, OperationalError, IntegrityError) as e:
            db.session.rollback()
            flash(f'Something went wrong, Please try again','error')
            return redirect(url_for('admin.edit_product', product_id=product_id))
        
    return render_template('admin/edit_product.html', form=form, product=product)


@admin.route('/delete-product/<int:product_id>',methods=['POST'])
@login_required
def delete_product(product_id):
    """
    Delete a product from the database.

    Fetches the product by ID and removes it. Rolls back on errors.

    Args:
        product_id (int): ID of the product to delete.

    Returns:
        Response: Redirect to product list page after deletion or rollback.
    """

    product = Product.query.get_or_404(product_id)

    product_name = product.name

    try:
        db.session.delete(product)
        db.session.commit()

        flash(f'Product {product_name} is deleted successfully!','success')
        return redirect(url_for('admin.products_list'))
    except (DataError, OperationalError, SQLAlchemyError, IntegrityError) as e:
        db.session.rollback()
        flash('Something went wrong, Please try again','error')
        return redirect(url_for('admin.products_list'))
  