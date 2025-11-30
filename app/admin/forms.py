from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, FloatField , TextAreaField
from wtforms.validators import DataRequired, NumberRange, Length, Optional

class ProductForm(FlaskForm):

    name = StringField('Product Name',validators=[DataRequired(message='Name of the product is required'),Length(min=3,max=50, message='Name must be between 3 to 50 characters')])

    price = FloatField('Price of Product',validators=[DataRequired(message='Price is required'),NumberRange(min=1, message='Price of Product cant be negative')])

    category = SelectField('Product Category',choices=[('anime','Anime'),('stationary','Stationary')],validators=[DataRequired(message='Category of product is required')])

    stock = IntegerField('Stock',validators=[DataRequired(message='Stock is empty'),NumberRange(min=0, message='Stock cannot be negative')])

    description = TextAreaField('Product Description',validators=[Length(max=1000, message='Word limit exceeds'),Optional()])

    image_url = StringField('Image URL',validators=[Optional()])

    submit = SubmitField('Add Product')