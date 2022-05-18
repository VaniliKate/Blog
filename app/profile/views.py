from flask import Blueprint, render_template
from flask_login import current_user

profile = Blueprint('profile', __name__)


@profile.context_processor
def inject_user():
    return dict(user=current_user)

@profile.route('/profile')
def view_profile():
    pitches = None
    if current_user.is_authenticated:
        pitches = current_user.pitches
        pitches_count = len(pitches)
    
    return render_template('profile.html', pitches = pitches, pitches_count = pitches_count)