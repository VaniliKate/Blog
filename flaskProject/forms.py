from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed

from flaskProject.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
    ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired()
    ])
    content = StringField('Content', validators=[
        DataRequired(),
    ], widget=TextArea())
    image = FileField('Image', validators=[
        FileAllowed(['jpeg', 'png', 'jpg']),
    ])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = StringField('Comment', validators=[
        DataRequired(),
    ], widget=TextArea())
    submit = SubmitField('Submit')


class RegistrationForm(FlaskForm):
    first_name = StringField('First name', validators=[
        DataRequired(),
        Length(min=2, max=20),
    ])
    last_name = StringField('Last name', validators=[
        DataRequired(),
        Length(min=2, max=20),
    ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
    ])
    confirm_password = PasswordField('Re-enter Password', validators=[
        DataRequired(),
        EqualTo('password'),
    ])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email Already Registered")


class AdminRegistrationForm(FlaskForm):
    first_name = StringField('First name', validators=[
        DataRequired(),
        Length(min=2, max=20),
    ])
    last_name = StringField('Last name', validators=[
        DataRequired(),
        Length(min=2, max=20),
    ])
    interests = StringField('Interests', validators=[], widget=TextArea())
    skills = StringField('Skills', validators=[], widget=TextArea())
    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
    ])
    confirm_password = PasswordField('Re-enter Password', validators=[
        DataRequired(),
        EqualTo('password'),
    ])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email Already Registered")
