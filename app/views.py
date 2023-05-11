from flask import request, render_template, flash, redirect, url_for
from app import app, db
from app.models import User
from .routes import *

@app.route('/')
def home():
     return render_template('home.html')
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
