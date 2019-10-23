# app/blueprints/home/blueprint.py
"""
This module is the Flask blueprint for the product catalog page (/).
"""


from flask import Blueprint, render_template

from models import product_catalog
from middlewares.auth import auth_optional

home_page = Blueprint('home_page', __name__)


@home_page.route('/')
@auth_optional
def display(auth_context):
    """
    View function for displaying the home page.

    Parameters:
       auth_context (dict): The authentication context of request.
                            See middlewares/auth.py for more information.
    Output:
       Rendered HTML page.
    """

    products = product_catalog.list_products()
    
    return render_template('home.html',
                           products=products,
                           auth_context=auth_context,
                           bucket=product_catalog.BUCKET)