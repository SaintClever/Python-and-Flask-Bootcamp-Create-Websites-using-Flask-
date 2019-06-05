from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    '''
    This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''
    breed = StringField('What breed are you?')
    submit = SubmitField('Submit')



@app.route('/', methods=['GET', 'POST'])
def index():

    # Create instance of the form.
    form = InfoForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.

        session['breed'] = form.breed.data
        flash(f"You just changed your breed to: {session['breed']}")
        return redirect(url_for("index"))


    return render_template('03-home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
