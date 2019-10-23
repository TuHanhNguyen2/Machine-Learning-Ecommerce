"""
This module is the main flask application.
"""


import firebase_admin
from flask import Flask

from blueprints import *


# Initialize Firebase Admin SDK.
# See https://firebase.google.com/docs/admin/setup for more information.
firebase = firebase_admin.initialize_app()

app = Flask(__name__)
app.secret_key = b'A Super Secret Key'


app.register_blueprint(home_page)
app.register_blueprint(signin_page)
app.register_blueprint(sell_page)
app.register_blueprint(upload_api)
app.register_blueprint(checkout_page)
app.register_blueprint(charge_page)


if __name__ == '__main__':
    app.run(debug=True)