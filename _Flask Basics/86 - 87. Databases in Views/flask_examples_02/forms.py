from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    name = StringField('Puppy name: ', validators=[DataRequired()])
    submit = SubmitField('Submit Puppy')

class DelForm(FlaskForm):
    del_name = StringField('Delete Puppy by name: ', validators=[DataRequired()])
    submit = SubmitField('Delete Puppy')