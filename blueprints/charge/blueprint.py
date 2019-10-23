"""
This module is the Flask blueprint for the charge page (/charge).
"""

import os

from flask import Blueprint, render_template

from models import orders, product_catalog
from middlewares.auth import auth_optional
from middlewares.form_validation import checkout_form_validation_required

charge_page = Blueprint('charge_page', __name__)


@charge_page.route('/charge', methods=['POST'])
@auth_optional
@checkout_form_validation_required
def process(auth_context, form):
    """
    View function for processing charges.

    Parameters:
       auth_context (dict): The authentication context of request.
                            See middlewares/auth.py for more information.
       form (CheckOutForm): A validated checkout form.
                            See middlewares/form_validation.py for more
                            information.
    Output:
       Rendered HTML page.
    """

    # Prepare the order
    product_ids = form.product_ids.data
    shipping = orders.Shipping(address=form.address.data,
                                city=form.city.data,
                                email=form.email.data,
                                mobile=form.mobile.data)
    amount = product_catalog.calculate_total_price(product_ids)
    order = orders.Order(amount=amount,
                        shipping=shipping,
                        status="order_created",
                        items=product_ids)
    order_id = orders.add_order(order)

    return render_template("charge.html", auth_context=auth_context)
