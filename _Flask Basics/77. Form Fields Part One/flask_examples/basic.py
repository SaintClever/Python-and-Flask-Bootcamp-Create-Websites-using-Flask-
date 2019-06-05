from flask import Flask, render_template, session, redirect, url_for # We grab the data from the session object. Similiar to a cookie however it's a time interval on the server when a client is logging in.

from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, RadioField, SelectField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

# Form setup
class InfoForm(FlaskForm):
    breed = StringField('What breed are you?', validators=[DataRequired()])
    neutered = BooleanField('Have you neutered your dog?')
    mood = RadioField('Please choose your mood:',
                        choices=[('mood_one','Happy'), ('mood_two','Excited')])

    food_choice = SelectField(u'Pick your favorite food:',
                                choices=[('chi','Chicken'), ('bf','Beef'),
                                ('fish','Fish')])

    feedback = TextAreaField()
    submit = SubmitField('Submit')


# index page
@app.route('/', methods=['GET','POST'])
def index():

    form = InfoForm() #Instance of form object

    if form.validate_on_submit(): #Grab data from the form on submit
        #The left is a made up key, meanwhile the right is the data within our class InfoForm
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))

    return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)