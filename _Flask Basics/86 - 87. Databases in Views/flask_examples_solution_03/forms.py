from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class AddForm_Pup(FlaskForm):
     name = StringField('Puppy name: ', validators=[DataRequired()])
     submit = SubmitField('Submit')


class DeleteForm_Pup(FlaskForm):
    id = IntegerField('Puppy ID: ')
    name = StringField('Puppy name: ')
    submit = SubmitField('Submit')


class AddForm_Owner(FlaskForm):
    id = IntegerField('Puppy ID: ', validators=[DataRequired()])
    name = StringField('Owner name: ', validators=[DataRequired()])
    submit = SubmitField('Submit')