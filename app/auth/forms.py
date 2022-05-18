from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField,SubmitField, validators
from wtforms.validators import Required, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    f_name = StringField('First Name', validators = [Required()])
    l_name = StringField('Last Name',validators = [Required()])
    email = StringField('Email Address', validators = [Required(), Email()])
    password = PasswordField('Enter Password', validators = [ Required(), Length(min=8, max=20), EqualTo('confirm', message='Passwords must match.') ])
    confirm = PasswordField('Confirm Password',validators = [ Required() ])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email Address', validators = [Required(), Email()])
    password = PasswordField('Confirm Password',validators = [ Required() ])
    submit = SubmitField('Login')