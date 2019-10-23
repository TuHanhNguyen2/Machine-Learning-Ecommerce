"""
Data class for orders.
"""


from dataclasses import dataclass
from typing import List


@dataclass
class Shipping:
    """
    Data class for shipping information.
    """
    address: str
    city: str
    email: str
    mobile: str


    @staticmethod
    def deserialize(data):
        """
        Helper function for parsing a dict of shipping data to a Shipping object.

        Parameters:
           data (dict): A dict of shipping data.

        Output:
           A Shipping object.
        """
        if data:
            return Shipping(
                address=data.get('address'),
                city=data.get('city'),
                email=data.get('email'),
                mobile=data.get('mobile')
            )

        return None


@dataclass
class Order:
    """
    Data class for orders.
    """
    amount: float
    shipping: Shipping
    status: str
    items: List[str]
    id: str = None


    @staticmethod
    def deserialize(document):
        """
        Helper function for parsing a Firestore document to an Order object.

        Parameters:
          document (DocumentSnapshot): A snapshot of Firestore document.

        Output:
          An Order object.
        """
        data = document.to_dict()
        if data:
            return Order(
                id=document.id,
                amount=data.get('amount'),
                shipping=Shipping.deserialize(data.get('shipping')),
                status=data.get('status'),
                items=data.get('items')
            )

        return None
