from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from flask_login import login_required, current_user

from .forms import PitchForm, CommentForm
from .. import db
from ..models import Category, Pitch, Upvote, Downvote, Comment

pitch = Blueprint('pitch', __name__)

@pitch.context_processor
def inject_user():
    return dict(user=current_user)

@pitch.route('/upvote_pitch')
def upvote_pitch():
    pitch_id = request.args.get('pitch_id')
    pitch = Pitch.query.get(pitch_id)
    upvotes = 0
    upvote_exists = False
    for upvote in pitch.upvotes:
        upvotes += 1
        if upvote.user.id == int(current_user.get_id() or 0):
            upvote_exists = True
            upvote_id = upvote.id

    if current_user.is_authenticated:
        downvotes = 0
        downvote_changed = False
        for downvote in pitch.downvotes:
            downvotes += 1
            if downvote.user.id == int(current_user.get_id() or 0):
                db.session.delete(downvote)
                db.session.commit()
                downvotes -= 1
                downvote_changed = True

        if not upvote_exists:
            new_upvote = Upvote(pitch_id = pitch_id, user_id = current_user.get_id())
            db.session.add(new_upvote)
            db.session.commit()
            upvotes += 1
            return jsonify(
                auth = True,
                upvote = True,
                upvotes = upvotes,
                downvotes = downvotes,
                downvotechange = downvote_changed
                )
        else:
            
            upvote_to_delete = Upvote.query.get(upvote_id)
            db.session.delete(upvote_to_delete)
            db.session.commit()
            upvotes -= 1
            return jsonify(
                auth = True,
                upvote = False,
                upvotes = upvotes, 
                downvotes = downvotes,
                downvotechange = downvote_changed
                )
    else:
        return jsonify(auth = False)


@pitch.route('/downvote_pitch')
def downvote_pitch():
    pitch_id = request.args.get('pitch_id')
    pitch = Pitch.query.get(pitch_id)
    downvotes = 0
    downvote_exists = False
    for downvote in pitch.downvotes:
        downvotes += 1
        if downvote.user.id == int(current_user.get_id() or 0):
            downvote_exists = True
            downvote_id = downvote.id

    if current_user.is_authenticated:
        upvotes = 0
        upvote_changed = False
        for upvote in pitch.upvotes:
            upvotes += 1
            if upvote.user.id == int(current_user.get_id() or 0):
                db.session.delete(upvote)
                db.session.commit()
                upvotes -= 1
                upvote_changed = True
        if not downvote_exists:
            new_downvote = Downvote(pitch_id = pitch_id, user_id = current_user.get_id())
            db.session.add(new_downvote)
            db.session.commit()
            downvotes += 1
            return jsonify(
                auth = True,
                downvote = True,
                downvotes = downvotes,
                upvotes = upvotes,
                upvotechange = upvote_changed
                )
        else:
            downvote_to_delete = Downvote.query.get(downvote_id)
            db.session.delete(downvote_to_delete)
            db.session.commit()
            downvotes -= 1
            return jsonify(
                auth = True,
                downvote = False,
                downvotes = downvotes,
                upvotechanged = upvote_changed
                )
    else:
        return jsonify(auth = False)



@pitch.route('/redirect_login')
def redirect_login():
    return redirect(url_for('auth.login'))

@pitch.route('/pitches')
def show_pitches():
    pitches = Pitch.query.all()
    list_of_pitches = []
    for pitch in pitches:
        id = pitch.id
        name = f'{pitch.user.f_name} {pitch.user.l_name}'
        pitch = pitch.message[0:180]
        a_pitch = {
            'id':id,
            'name': name,
            'pitch': pitch
        }
        list_of_pitches.append(a_pitch)

   
    return render_template('pitches/pitches.html', pitches = list_of_pitches)

@pitch.route('/make-pitch', methods = ['GET', 'POST'])
@login_required
def make_pitch():
    form = PitchForm()
    form.categories.choices = [(cat.id, cat.name) for cat in Category.query.all()]

    if form.validate_on_submit():
        category_id = form.categories.data
        user_id = current_user.id
        pitch = form.message.data

        new_pitch = Pitch(message = pitch, user_id = user_id, category_id = category_id)
        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('pitch.show_pitches'))


    return render_template('pitches/makeapitch.html', pitch_form = form)


@pitch.route('/pitches/<int:id>', methods = ['GET', 'POST'])
def show_pitch(id):
    form = CommentForm()
    pitch = Pitch.query.get(id)
    upvoted = False
    upvotes = 0
    for upvote in pitch.upvotes:
        upvotes += 1
       
        if upvote.user.id == int(current_user.get_id() or 0):
            upvoted = True

    downvoted = False
    downvotes = 0
    for downvote in pitch.downvotes:
        downvotes += 1
        if downvote.user.id == int(current_user.get_id() or 0):
            downvoted = True

    comments_counter = 0
    for comments in pitch.comments:
        comments_counter += 1

    return render_template('pitches/pitch.html',comment_form = form, pitch = pitch, upvoted = upvoted, upvotes = upvotes,  downvotes = downvotes, comments = pitch.comments, comments_count = comments_counter)


@pitch.route('/comment/<int:id>', methods = ['POST'])
def comment_pitch(id):  
    if current_user.is_authenticated:
        comment = request.values['comment']
        new_comment = Comment(pitch_id = id, user_id = current_user.get_id(), comment = comment)
        db.session.add(new_comment)
        db.session.commit()

        comments_counter = 0
        for comment in Pitch.query.get(id).comments:
            comments_counter += 1

        return jsonify(
            auth = True,
            comment_message = new_comment.comment,
            comment_f_name = new_comment.user.f_name,
            comment_l_name = new_comment.user.l_name,
            comments_count = comments_counter
        )
    else:
        return jsonify(auth = False)
