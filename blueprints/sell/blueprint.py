"""
This module is the Flask blueprint for the sell page (/sell).
"""


import os
import time

from flask import Blueprint, redirect, render_template, url_for

from models import product_catalog
from middlewares.auth import auth_required
from middlewares.form_validation import SellForm, sell_form_validation_required

sell_page = Blueprint('sell_page', __name__)


@sell_page.route('/sell', methods=['GET'])
@auth_required
def display(auth_context):
    """
    View function for displaying the sell page.

    Parameters:
       auth_context (dict): The authentication context of request.
                            See middlewares/auth.py for more information.
    Output:
       Rendered HTML page.
    """

    # Prepares the sell form.
    # See middlewares/form_validation.py for more information.
    form = SellForm()
    return render_template('sell.html', auth_context=auth_context, form=form)


@sell_page.route('/sell', methods=['POST'])
@auth_required
@sell_form_validation_required
def process(auth_context, form):
   """
   View function for processing sell requests.

   Parameters:
      auth_context (dict): The authentication context of request.
                           See middlewares/auth.py for more information.
      form (SellForm): A validated sell form.
                     See middlewares/form_validation.py for more
                     information.
   Output:
      Rendered HTML page.
   """
   print('image',form.image.data)
   print('label', form.label.data)
   product = product_catalog.Product(name=form.name.data,
                                    description=form.description.data,
                                    image=form.image.data+'.png',
                                    labels=[form.label.data],
                                    price=form.price.data,
                                    created_at=int(time.time()))
   product_id = product_catalog.add_product(product)
   
   return redirect(url_for('home_page.display'))