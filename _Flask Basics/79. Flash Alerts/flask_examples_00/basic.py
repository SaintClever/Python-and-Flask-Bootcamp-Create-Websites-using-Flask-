from flask import (Flask, flash, redirect,
                    render_template, session, url_for)

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'

# CLASS
class InfoForm(FlaskForm):
    breed = StringField('Whats your animal breed:',
                        validators=[DataRequired()])

    submit = SubmitField('Submit Form')

# ROUTES 
@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash('You just entered ' + session['breed'])
        
        return redirect(url_for('index'))

    return render_template('index.html', form=form)


@app.errorhandler(404)
def error_handler(error):
    return render_template('404.html'), 404


# APP.RUN
if __name__ == '__main__':
    app.run(debug=True)