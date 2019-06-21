from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Puppy name:')
    submit = SubmitField('Submit Puppy')

class DelForm(FlaskForm):
    id = IntegerField('Puppy ID:')
    submit = SubmitField('Remove Puppy')
