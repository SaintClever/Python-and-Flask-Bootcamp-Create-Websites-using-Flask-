from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to Remove: ')
    submit = SubmitField('Remove Puppy')


class AddOwner(FlaskForm):
    pup_id = IntegerField('Puppy ID: ')
    name = StringField('Owner name: ')
    submit = SubmitField('Add Owner')