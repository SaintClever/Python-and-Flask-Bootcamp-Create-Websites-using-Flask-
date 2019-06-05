from flask import Flask, redirect, render_template, session, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, SelectField,
                    RadioField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'

# Form class
class InfoForm(FlaskForm):
    breed = StringField('What is the animal breed:', validators=[DataRequired()])
    neutered = BooleanField('Is your pet neutered:')

    food = SelectField(u'What is your pets prefered food:',
    choices=[('chose_chicken', 'Chicken'), ('chose_beef', 'Beef'),
    ('chose_fish','Fish')])

    mood = RadioField('What is your animals current mood:',
    choices=[('chose_excited', 'Excited'), ('chose_happy', 'Happy'), ('chose_grumpy', 'Grumpy')])

    feedback = TextAreaField('Please provide feedback:')
    submit = SubmitField('Submit Form')


# Routes
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
    

if __name__ == '__main__':
    app.run(debug=True)