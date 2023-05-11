from flask import Blueprint, render_template

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/login')
def login():
    return render_template('login.html')

@auth_bp.route('/signup')
def signup():
    return render_template('signup.html')