from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, SubmitField
from wtforms.validators import Length, Required

class PitchForm(FlaskForm):
    categories = SelectField('Category', coerce=int)
    message = TextAreaField('Make yoour pitch', validators = [Required() ,Length(min = 20, max = 1000, message = 'Check the length of your pitch')])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators = [Required() ,Length(max = 1000, message = 'Check your comment.')])
    submit = SubmitField()