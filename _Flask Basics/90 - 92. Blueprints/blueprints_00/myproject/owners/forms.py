from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of Owner:')
    puppy_id = IntegerField('Id of Puppy:')
    submit = SubmitField('Submit')