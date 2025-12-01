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

    name = StringField('Product Name',validators=[DataRequired(message='Name of the product is required'),Length(min=3,max=50, message='Name must be between 3 to 50 characters')])

    price = FloatField('Price of Product',validators=[DataRequired(message='Price is required'),NumberRange(min=1, message='Price of Product cant be negative')])

    category = SelectField('Product Category',choices=[('anime','Anime'),('stationery','Stationery')],validators=[DataRequired(message='Category of product is required')])

    stock = IntegerField('Stock',validators=[DataRequired(message='Stock is empty'),NumberRange(min=0, message='Stock cannot be negative')])

    description = TextAreaField('Product Description',validators=[Length(max=1000, message='Word limit exceeds'),Optional()])

    image_url = StringField('Image URL',validators=[Optional()])

    submit = SubmitField('Add Product')