from flask_security import RoleMixin, UserMixin
from flask_security import Security, SQLAlchemyUserDatastore

from . import db, app



class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
     # Add fs_uniquifier attribute
    fs_uniquifier = db.Column(db.String(64), unique=True, nullable=False, server_default='')
    # Other attributes
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phonenumber = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    confirmed_at = db.Column(db.DateTime())

    roles = db.relationship('Role', secondary='user_roles',
                            backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return f"User('{self.name}')"


# create the user datastore with SQLAlchemyUserDatastore
user_datastore = SQLAlchemyUserDatastore(db, User, Role)

# Create the Flask-Security object
security = Security(app, user_datastore)