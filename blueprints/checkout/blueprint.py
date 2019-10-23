"""
This module is the Flask blueprint for the checkout page (/checkout).
"""


from flask import Blueprint, redirect, render_template, request, url_for

from models import product_catalog
from middlewares.auth import auth_optional
from middlewares.form_validation import CheckOutForm

checkout_page = Blueprint("checkout_page", __name__)


@checkout_page.route('/checkout')
@auth_optional
def display(auth_context):
    """
    View function for displaying the checkout page.

    Parameters:
       auth_context (dict): The authentication context of request.
                            See middlewares/auth.py for more information.
    Output:
       Rendered HTML page.
    """

    products = []
    # Prepares the checkout form.
    # See middlewares/form_validation.py for more information.
    form = CheckOutForm()
    product_id = request.args.get('id')
    # Checkout one single item if parameter id presents in the URL query string.
    product = product_catalog.get_product(product_id)
    products.append(product)

    if products:
        return render_template('checkout.html',
                               products=products,
                               auth_context=auth_context,
                               form=form,
                               bucket=product_catalog.BUCKET)

    return redirect(url_for('home_page.display'))
