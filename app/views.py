from flask import request, render_template, flash, redirect, url_for
from app import app, db,csrf, CORS
from app.models import User
from .routes import *


@app.route('/')
def home():
    return render_template('home.html')
    

@app.route('/signup', methods=['GET', 'POST'])
@csrf.exempt # exclude CSRF protection for GET requests
def signup():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = User(phonenumber=form.phonenumber.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/signin', methods=['GET', 'POST'])
@csrf.exempt # exclude CSRF protection for GET requests
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        # Process the form data here
        return 'Thanks for logging in!'
    return render_template('signin.html', form=form)