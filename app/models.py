from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True, index = True)
    username = db.Column(db.String(200))
    pass_secure = db.Column(db.String(255))
    name = db.Column(db.String(100))

    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)
    
    def __repr__(self):
        return f'{self.username}'


class Tale(db.Model):
    __tablename__ = 'tales'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(255), unique = True)
    blog = db.Column(db.Text, nullable = False)


    @classmethod
    def get_tales(cls,id):
        blogs = Tale.query.order_by(tale_id=id).desc().all()
        return blogs

    def __repr__(self):
        return f'Tale {self.blog_content}'