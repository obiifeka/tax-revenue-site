from flask import Flask
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
import secrets
from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tax.db'

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
CORS(app)
from .models import User, Role

# create the user datastore with SQLAlchemyUserDatastore
user_datastore = SQLAlchemyUserDatastore(db, User, Role)

from . import views
