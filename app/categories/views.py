from flask import render_template, Blueprint
from flask_login import current_user

from ..models import Category

category = Blueprint('category', __name__)

@category.context_processor
def inject_user():
    return dict(user=current_user)

@category.route('/categories')
def show_categories():
    categories = Category.query.all()
    return render_template('category/categories.html', categories = categories)

@category.route('/categories/<category>')
def show_category(category):
    category = Category.query.filter_by(name = category).first()
    pitches = category.categories
    pitches_count = len(pitches)
    return render_template('category/category.html', category = category, pitches = pitches, pitches_count = pitches_count)

@category.route('/categories/<category>/<int:id>')
def show_pitch(category, id):
    return render_template('category/pitch.html')