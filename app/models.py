from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from . import db

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50), nullable = False)
    l_name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(80), unique = True)
    password_hash = db.Column(db.String(100))

    @property
    def password(self):
        raise AttributeError('Password not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    

    def __repr__(self):
        
        return '<User %r>' % self.f_name

class Pitch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1000), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    user = db.relationship('User', backref = 'pitches', lazy = True)
    category = db.relationship('Category', backref = 'categories', lazy = True)

    def __repr__(self):
        
        return '<Pitch %r>' % self.message


class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))

    def __repr__(self):
        
        return '<Category %r>' % self.name

class Upvote(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    pitch = db.relationship('Pitch', backref = 'upvotes', lazy = True)
    user = db.relationship('User', backref = 'upvotes', lazy = True)


class Downvote(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    pitch = db.relationship('Pitch', backref = 'downvotes', lazy = True)
    user = db.relationship('User', backref = 'downvotes', lazy = True)

   
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment = db.Column(db.String(1000))

    pitch = db.relationship('Pitch', backref = 'comments', lazy = True)
    user = db.relationship('User', backref = 'comments', lazy = True)