from flask import render_template, redirect, url_for, flash, request
from . import auth
from flask_login import login_user, logout_user, login_required, login_manager
from ..models import User
from .forms import subscriptionForm, loginForm
from .. import db
from flask_sqlalchemy import sqlalchemy
from werkzeug import check_password_hash


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = loginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username of Password')
    title = 'New User? Subscribe Here'    
    return render_template('login.html', loginForm=login_form, title=title)



@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = subscriptionForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data)
        user.password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = 'New Account'
    return render_template('register.html', subscriptionForm = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))