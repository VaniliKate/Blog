from flask import Flask, render_template, flash, redirect, request, url_for, abort
from flaskProject.models import User, Post, Comment, Like, ReadLater
from flaskProject.forms import RegistrationForm, LoginForm, PostForm, CommentForm, AdminRegistrationForm
from flaskProject import app, bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image


@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.order_by(Post.date_posted.desc()).limit(5).all()
    return render_template('home.html', posts=posts, admin=User.query.filter_by(superuser=True).first())


@app.route('/posts')
def posts():
    title = request.args.get('q')
    if title:
        posts = Post.query.filter(Post.title.like('%' + title + '%')).all()
        new_order = None
    else:
        order = request.args.get('order')
        if not order:
            order = 'desc'
        if order == "desc":
            posts = Post.query.order_by(Post.date_posted.desc()).all()
            new_order = 'asc'
        else:
            posts = Post.query.order_by(Post.date_posted.asc()).all()
            new_order = 'desc'
    return render_template('all_posts.html', posts=posts, new_order=new_order,
                           admin=User.query.filter_by(superuser=True).first())


@app.route('/registerAdmin', methods=['GET', 'POST'])
def registerAdmin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = AdminRegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            db.session.add(
                User(first_name=form.first_name.data, last_name=form.last_name.data, password=hashed_password,
                     email=form.email.data, superuser=True, skills=form.skills.data, interests=form.interests.data))
            db.session.commit()
            flash(f'Account created For {form.first_name.data} {form.last_name.data}!', 'success')
            return redirect(url_for('login'))
        else:
            flash(f'Register Failed!', 'danger')
    return render_template('registerAdmin.html', form=form, title="Register Admin")


@app.route('/about')
def about():
    return render_template('about.html', admin=User.query.filter_by(superuser=True).first())


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                flash(f'Welcome!', 'success')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            flash(f'Login Failed!', 'danger')
        else:
            flash(f'Login Failed!', 'danger')
    return render_template('login.html', title='Login', form=form, admin=User.query.filter_by(superuser=True).first())


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            db.session.add(
                User(first_name=form.first_name.data, last_name=form.last_name.data, password=hashed_password,
                     email=form.email.data))
            db.session.commit()
            flash(f'Account created For {form.first_name.data} {form.last_name.data}!', 'success')
            return redirect('login')
        else:
            flash(f'Register Failed!', 'danger')
    return render_template('register.html', title='Register', form=form,
                           admin=User.query.filter_by(superuser=True).first())


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account', admin=User.query.filter_by(superuser=True).first())


@app.route('/addPost', methods=['GET', 'POST'])
@login_required
def addPost():
    if current_user.superuser:
        form = PostForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                if form.image.data:
                    db.session.add(
                        Post(title=form.title.data, content=form.content.data, image=save_image(form.image.data)))
                else:
                    db.session.add(Post(title=form.title.data, content=form.content.data))
                db.session.commit()
                flash(f'Post Added!', 'success')
                return redirect(url_for('home'))
            flash(f'Posting Failed!', 'danger')
            return render_template('add_post.html', title='Add Post', form=form, legend="Whats on your mind",
                                   admin=User.query.filter_by(superuser=True).first())
        else:
            return render_template('add_post.html', title='Add Post', form=form, legend="Whats on your mind",
                                   admin=User.query.filter_by(superuser=True).first())
    return redirect(url_for('home'))


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if request.method == 'POST' and post:
        if form.validate_on_submit():
            db.session.add(Comment(comment=form.comment.data, post_id=post.id, user_id=current_user.id))
            db.session.commit()
            flash('Comment Added!', 'success')
    if current_user.is_authenticated:
        if Like.query.filter_by(post_id=post_id, user_id=current_user.id).first():
            liked = True
        else:
            liked = False
        if ReadLater.query.filter_by(post_id=post_id, user_id=current_user.id).first():
            saved = True
        else:
            saved = False
    else:
        liked = False
        saved = False
    return render_template('post.html', title=post.title, post=post, form=form,
                           admin=User.query.filter_by(superuser=True).first(), liked=liked, saved=saved)


def save_image(data):
    random_hex = secrets.token_hex(8)
    _, ext = os.path.splitext(data.filename)
    file_name = random_hex + ext
    image_path = os.path.join(app.root_path, "static/blog_images", file_name)
    # output_size = (125, 125)
    # i = Image.open(data)
    # i.thumbnail(output_size)
    # i.save()
    data.save(image_path)
    return file_name


@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if current_user.superuser:
        form = PostForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                if form.image.data:
                    post.image = save_image(form.image.data)
                post.title = form.title.data
                post.content = form.content.data
                db.session.commit()
                flash('Post updated!', 'success')
                return redirect(url_for('post', post_id=post.id))
        form.title.data = post.title
        form.content.data = post.content
        form.image.data = post.image
        return render_template('add_post.html', title=post.title, form=form, legend="Update Post",
                               admin=User.query.filter_by(superuser=True).first())
    abort(403)


@app.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if current_user.superuser:
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted!", 'info')
        return redirect(url_for('home'))


@app.route('/like/<int:post_id>', methods=['POST'])
@login_required
def like(post_id):
    like = Like.query.filter_by(post_id=post_id, user_id=current_user.id).first()
    if like:
        db.session.delete(like)
    else:
        db.session.add(Like(post_id=post_id, user_id=current_user.id))
    db.session.commit()
    return redirect(url_for('post', post_id=post_id))


@app.route('/tag/<int:post_id>', methods=['POST'])
@login_required
def tag(post_id):
    tag = ReadLater.query.filter_by(post_id=post_id, user_id=current_user.id).first()
    if tag:
        db.session.delete(tag)
    else:
        db.session.add(ReadLater(post_id=post_id, user_id=current_user.id))
    db.session.commit()
    return redirect(url_for('post', post_id=post_id))


@app.route('/readlater')
@login_required
def readLater():
    posts = []
    later = ReadLater.query.filter_by(user_id=current_user.id)
    for saved in later:
        posts.append(saved.post)
    return render_template('readLater.html', posts=posts, admin=User.query.filter_by(superuser=True).first())
