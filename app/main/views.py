from flask import render_template, abort, request, redirect, url_for, flash
from . import main
from .. import db
from app.models import Tale, User
from .forms import CreateBlog, UpdateProfile
from flask_login import login_required, current_user
from ..requests import random_quotes


@main.route('/', methods = ['GET', 'POST'])
def index():
    quotes = random_quotes()
    tales = Tale.query.all()
    return render_template('index.html', quotes = quotes, tales=tales)

@main.route('/tale/new', methods=['GET', 'POST'])
@login_required
def new_tale():
    form = CreateBlog()
    if form.validate_on_submit():
        print(form.title.data)
        tale = Tale(title =form.title.data, blog=form.content.data, author=current_user.name)
        db.session.add(tale)
        db.session.commit()
        flash('Your Blog-Tale has been created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('create-blog.html', title='New_Tale', form=form)

@main.route('/profile/<name>')
@login_required
def profile(name):
    user = User.query.filter_by(username = name).first()

    if user is None:
        abort(404)
    return render_template('profile.html', user=user)


@main.route('/user/<name>/update',methods = ['Get', 'POST'])
@login_required
def update_profile(name):
    user = User.query.filter_by(username = name).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    
    if form.validate_on_submit():
        user.bio = form.bio.data


        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile', username=user.name))

    return render_template('profile/update.html', form = form)
