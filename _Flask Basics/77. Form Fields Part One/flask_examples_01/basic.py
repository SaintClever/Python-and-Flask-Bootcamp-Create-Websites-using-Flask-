from flask import Flask, redirect, render_template, session, url_for
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import (StringField, BooleanField, SelectField,
                    RadioField, TextAreaField, SubmitField)

app = Flask(__name__)


app.config['SECRET_KEY'] = 'secret_key'

class InfoForm(FlaskForm):

    breed = StringField('What is your animals breed:',
    validators=[DataRequired()])

    neutered = BooleanField('Is your pet neutered:')

    food = SelectField(u'What food does your pet like:',
    choices=[('chosen_chicken', 'Chicken'), ('chosen_beef', 'Beef'), ('chosen_fish', 'Fish')])

    mood = RadioField('What mood is your pet in:',
    choices=[('chosen_excited', 'Excited'), ('chosen_happy', 'Happy')])

    feedback = TextAreaField('Please provide some Feedback:')

    submit = SubmitField('Submit Form')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['food'] = form.food.data
        session['mood'] = form.mood.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thank_you'))

    return render_template('index.html', form=form)


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')


@app.errorhandler(404)
def error_handler(error):
    return render_template('404.html'), 404


if  __name__ == '__main__':
    app.run(debug=True)