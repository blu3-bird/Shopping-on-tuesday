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

from flask import redirect, render_template, flash, url_for , request
from flask_login import login_required
from app.admin import admin
from app.constants import LOW_STOCK_THRESHOLD, RECENT_PRODUCTS_LIMIT, CATEGORY_ANIME, CATEGORY_STATIONERY
from app.models import Product , ProductImage
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

@admin.route('/add-product',methods=['GET','POST'])
@login_required
def add_product():

    form = ProductForm()

    if form.validate_on_submit():

        product = Product(
            name = form.name.data,
            description = form.description.data,
            stock = form.stock.data,
            image_url = form.image_url.data,
            original_price = form.original_price.data,
            discount_percent = form.discount_percentage.data,
            category = form.category.data,
            price = form.price.data,
            highlights = form.highlights.data
        )

        db.session.add(product)
        db.session.flush()

        image_urls = request.form.getlist('image_urls[]')
        primary_image_index = request.form.data('primary_image',0)

        for index, url in enumerate(image_urls):
            if url.strip():
                image = ProductImage(
                    product_id = product.id,
                    image_url = url.strip(),
                    is_primary =(str(index) == primary_image_index),
                    display_order = index
                )
                db.session.add(image)

            if not any(url.strip() for url in image_urls):
                if form.image_url.data:
                    product.image_url = form.image_url.data
            
            db.session.commit()
            flash(f'{product.name} is successfully added', 'success')

            return redirect(url_for('admin/product_list'))
    return render_template('admin/add_product.html', form=form)

@admin.route('/edit-product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    """
    to edit the existing products
    """

    product = Product.query.get_or_404(product_id)

    form = ProductForm()

    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        product.description = form.description.data
        product.stock = form.stock.data
        product.category = form.category.data
        product.hightlights = form.highlights.data
        product.original_price = form.original_price.data
        product.discount_percentage = form.discount_percentage.data

        #handle image deletions
        image_to_delete = request.form.getlist('delete_images[]')

        for img_id in image_to_delete:
                image = ProductImage.query.get(int(img_id))
                if image and image.product_id == product.id:
                    db.session.delete(image)

        #adding new image
        image_to_add = request.form.getlist('new_image_urls[]')
        current_image_count = product.images.count()

        for index, url in enumerate(image_to_add):
            if url.strip():
                image = ProductImage(
                    is_primary = False,
                    image_url = url.strip(),
                    display_order = current_image_count + index,
                    product_id = product.id
                )
                db.session.add(image)

        #handles the primary image
        primary_image_id = request.form.get('primary_image')
        if primary_image_id:
            for img in product.images:
                img.is_primary=False
            
            primary_image = ProductImage.query.get(int(primary_image_id))
            if primary_image and primary_image.product_id == product.id:
                primary_image.is_primary = True

        if form.image_url.data:
            product.image_url = form.image_url.data
        
        db.session.commit()
        flash(f'Product {product.name} updated successfully,', 'success')
        return redirect(url_for('admin.products_list'))
    
    #Pre-populate form
    form.name.data = product.name
    form.price.data = product.price
    form.description.data = product.description
    form.stock.data = product.stock
    form.category.data = product.category
    form.image_url.data = product.image_url
    form.original_price.data = product.original_price
    form.discount_percentage.data = product.discount_percentage
    form.highlights.data = product.highlights

    # existin images
    existing_images = product.images.order_by(ProductImage.display_order).all()

    return render_template('admin/edit_product.html',
                           existing_images=existing_images,
                           form=form,
                           product=product)



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
  