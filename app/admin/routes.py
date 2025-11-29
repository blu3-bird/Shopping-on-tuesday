from flask import redirect, render_template, flash, url_for
from flask_login import login_required, current_user
from app.admin import admin
from app.models import Product
from sqlalchemy.exc import DataError , OperationalError , IntegrityError
from app.admin import ProductForm
from app.models import db

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
    out_of_stock = Product.query.filter(Product.stock == 0).count()

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
    return render_template('admin/product_detail.html',products=products)

@admin.route('/add-product', methods=['GET','POST'])
@login_required
def add_product():
    """
    add product
    """
    form = ProductForm()

    if form.validate_on_submit():

        product = Product(
            name=form.name.data,
            price=form.price.data,
            category=form.category.data,
            stock=form.stock.data,
            description=form.description.data,
            image_url=form.image_url.data
        )

        try:
            db.session.add(product)
            db.session.commit()

            flash(f'Product {product.name} has been successfully added', 'success')

            return redirect(url_for('admin.products_list'))
        except DataError as e:
            db.session.rollback()

            raise e
        except OperationalError as e:
            db.session.rollback()

            raise e
        
        except IntegrityError as e:
            db.session.rollback()

            raise e
    return render_template('admin/add_product.html', form=form)