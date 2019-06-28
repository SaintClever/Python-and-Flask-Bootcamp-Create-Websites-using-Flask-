from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Puppy name: ')
    submit = SubmitField('Submit Puppy')


class DelForm(FlaskForm):
    id = IntegerField('Puppy ID: ')
    submit = SubmitField('Submit Puppy')


class AddOwner(FlaskForm):
    id = IntegerField('Puppy ID: ')
    owner_name = StringField('Owner name: ')
    submit = SubmitField('Submit Owner')
