"""
Forms used in the admin panel for managing product data.

This module contains the form definitions that handle validation and input
collection for creating and editing products in the admin interface.
It includes field validation rules, length constraints, and optional fields
such as product descriptions and image URLs.

These forms ensure that all product data submitted by admin users is properly
validated before being stored in the database.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, FloatField , TextAreaField
from wtforms.validators import DataRequired, NumberRange, Length, Optional

class ProductForm(FlaskForm):
    """
    Form for creating or editing product information.

    This form handles validation for all product-related fields used in the
    admin panel, including name, price, category, stock, description, and image URL.

    Fields:
        name (StringField): Name of the product. Required, 3–50 characters.
        price (FloatField): Price of the product. Must be positive.
        category (SelectField): Category selection (Anime or Stationery).
        stock (IntegerField): Available stock. Must be zero or greater.
        description (TextAreaField): Optional product description (max 1000 chars).
        image_url (StringField): Optional image URL of the product.
        submit (SubmitField): Button to submit the form.

    Returns:
        ProductForm: A validated form instance used for product creation or editing.
    """

    # Validation constants
    NAME_MIN_LENGTH = 3
    NAME_MAX_LENGTH = 50
    PRICE_MIN = 1
    STOCK_MIN = 0
    DESCRIPTION_MAX_LENGTH = 1000

    name = StringField(
        'Product Name',
        validators=[
            DataRequired(message='Name of the product is required'),
            Length(
                min=NAME_MIN_LENGTH,
                max=NAME_MAX_LENGTH,
                message=f'Name must be between {NAME_MIN_LENGTH} to {NAME_MAX_LENGTH} characters'
            ),
        ],
        render_kw={"placeholder": "Enter product name"},
    )

    price = FloatField(
        'Price of Product',
        validators=[
            DataRequired(message='Price is required'),
            NumberRange(
                min=PRICE_MIN,
                message=f'Price of Product must be at least {PRICE_MIN}',
            ),
        ],
        render_kw={"placeholder": "299"},
    )

    category = SelectField(
        'Product Category',
        choices=[('anime', 'Anime'), ('stationery', 'Stationery')],
        validators=[DataRequired(message='Category of product is required')],
    )

    stock = IntegerField(
        'Stock',
        validators=[
            DataRequired(message='Stock is empty'),
            NumberRange(min=STOCK_MIN, message=f'Stock cannot be less than {STOCK_MIN}'),
        ],
        render_kw={"placeholder": "10"},
    )

    description = TextAreaField(
        'Product Description',
        validators=[
            Length(
                max=DESCRIPTION_MAX_LENGTH,
                message=f'Description cannot exceed {DESCRIPTION_MAX_LENGTH} characters',
            ),
            Optional(),
        ],
        render_kw={"placeholder": "Enter product description (optional)"},
    )

    image_url = StringField(
        'Image URL',
        validators=[Optional()],
        render_kw={"placeholder": "https://i.postimg.cc/R032DzLF/8431562.jpg  (optional)"},
    )

    submit = SubmitField('Add Product')