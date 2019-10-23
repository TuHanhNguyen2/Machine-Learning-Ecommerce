# app/models/product_catalog/helpers.py
"""
A collection of helper functions for product related operations.
"""


from dataclasses import asdict
import os
import uuid

from google.cloud import firestore

from .data_classes import Product

BUCKET = os.environ.get('GCS_BUCKET')

firestore_client = firestore.Client()


def add_product(product):
    """
    Helper function for adding a product.

    Parameters:
       product (Product): A Product object.

    Output:
       The ID of the product.
    """

    product_id = uuid.uuid4().hex
    firestore_client.collection('products').document(product_id).set(asdict(product))
    return product_id

def get_product(product_id):
    """
    Helper function for getting a product.

    Parameters:
       product_id (str): The ID of the product.

    Output:
       A Product object.
    """

    product = firestore_client.collection('products').document(product_id).get()
    return Product.deserialize(product)


def list_products():
    """
    Helper function for listing products.

    Parameters:
       None.

    Output:
       A list of Product objects.
    """

    products = firestore_client.collection('products').order_by('created_at').get()
    product_list = [Product.deserialize(product) for product in list(products)]
    return product_list

def calculate_total_price(product_ids):
    """
    Helper function for calculating the total price of a list of products.

    Parameters:
       product_ids (List[str]): A list of product IDs.

    Output:
       The total price.
    """

    total = 0
    for product_id in product_ids:
        product = get_product(product_id)
        total += product.price
    return total