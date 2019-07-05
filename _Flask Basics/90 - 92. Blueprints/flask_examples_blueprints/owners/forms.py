from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField

class AddForm(FlaskForm):
    id = IntegerField('Puppy ID: ')
    name = StringField('Owner name: ')
    submit = SubmitField('Submit')