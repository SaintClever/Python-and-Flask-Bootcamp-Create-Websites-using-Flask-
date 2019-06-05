from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired


app = Flask(__name__)
# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'mysecretkey'

# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html
class InfoForm(FlaskForm):
    '''
    This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''
    breed = StringField('What breed are you?',validators=[DataRequired()])
    neutered  = BooleanField("Have you been neutered?")
    mood = RadioField('Please choose your mood:', choices=[('mood_one','Happy'),('mood_two','Excited')])
    food_choice = SelectField(u'Pick Your Favorite Food:',
                          choices=[('chi', 'Chicken'), ('bf', 'Beef'),
                                   ('fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')



@app.route('/', methods=['GET', 'POST'])
def index():

    # Create instance of the form.
    form = InfoForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.

        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for("thankyou"))


    return render_template('01-home.html', form=form)


@app.route('/thankyou')
def thankyou():

    return render_template('01-thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
