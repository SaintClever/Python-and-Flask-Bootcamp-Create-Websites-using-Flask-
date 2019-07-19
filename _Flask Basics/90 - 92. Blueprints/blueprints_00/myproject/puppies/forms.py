from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of Puppy')
    submit = SubmitField('Submit')


class DelForm(FlaskForm):
    id = IntegerField('Id Number of Puppy to Remove:')
    submit = SubmitField('Submit')