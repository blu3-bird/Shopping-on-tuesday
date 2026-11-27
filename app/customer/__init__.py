from flask import Blueprint
customer = Blueprint('customer', __name__)
from app.customer import routes
