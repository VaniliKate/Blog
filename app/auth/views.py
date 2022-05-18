from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user

from .. import db
from .forms import RegisterForm, LoginForm
from app.models import User
from ..emails import send_email

auth = Blueprint('auth', __name__)

@auth.context_processor
def inject_user():
    return dict(user=current_user)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email = email).first()

        if not user or not user.verify_password(password):
            return 'Please check your email or password'
        else:

            login_user(user)
            return redirect(url_for('app.home'))
    
    return render_template('auth/login.html', login_form = form)

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        first =  form.f_name.data
        last =  form.l_name.data
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email = email).first()

        if not user:
            new_user = User(f_name = first, l_name = last, email = email, password = password)
            db.session.add(new_user)
            db.session.commit()

            # email_obj = {
            #     'email_subject': 'Welcome to Elevator Pitch',
            #     'email_body': f'We are glad you are here.{first} ',
            # }
            # send_email(email_obj, email)
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html', register_form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('app.home'))
