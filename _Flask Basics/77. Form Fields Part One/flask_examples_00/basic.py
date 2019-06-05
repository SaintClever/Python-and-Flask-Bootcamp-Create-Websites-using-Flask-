from flask import Flask, redirect, render_template, session, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, SelectField,
                    RadioField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you?', validators=[DataRequired()])
    neutered = BooleanField('Have you neutered your dog?')

    food = SelectField(u'Pick your favorite food:',
    choices=[('chose_chicken', 'Chicken'), ('chose_beef', 'Beef'),
    ('chose_fish', 'Fish')])

    mood = RadioField('Please choose your mood:',
    choices=[('chose_excited', 'Excited'), ('chose_happy', 'Happy')])

    feedback = TextAreaField('Please provide some feedback')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['food'] = form.food.data
        session['mood'] = form.mood.data
        session['feedback'] = form.feedback

        return redirect(url_for('thankyou'))

    return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

    
if __name__ == '__main__':
    app.run(debug=True)