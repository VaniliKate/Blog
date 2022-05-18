from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class Quote():
    def __init__(self, author, text):
        self.author=author
        self.text=text


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    

class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    about = db.Column(db.String(255))
    avatar = db.Column(db.String())
    password_encrypt=db.Column(db.String(128))
    pitches = db.relationship('Pitches', backref='user', lazy='dynamic')
    comments = db.relationship('Comments', backref='comments', lazy='dynamic')

    @property   #write-only
    def password(self):
        raise AttributeError('You can only read this attribute')

    @password.setter
    def password(self, password):
        self.password_encrypt = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_encrypt, password)

    def __repr__(self):
        return f'User{self.username}'


class Pitches(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comments', backref='pitch', lazy='dynamic')
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Pitches{self.text}'


class Comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    comment = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comments.query.filter_by(pitch_id=pitch_id)
        return comments
    
    def __repr__(self):
        return f'Comments:{self.comment}'