# form.py puppies
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Puppy name: ')
    submit = SubmitField('Submit')


class DelForm(FlaskForm):
    id = IntegerField('Puppy ID: ')
    submit = SubmitField('Submit')