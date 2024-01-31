from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
app.config['SECRET_KEY'] = os.urandom(16)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flask_shop.admin import routes
from flask_shop.products import routes
