from flask import redirect, request, flash, abort, render_template, url_for
from flask_login import login_required, login_user, logout_user

from myproject import app, db
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm

from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome')
@login_required ## imported from flask_login
def welcome_user():
    return render_template('welcome_user.html')


@app.route('/logout')
@login_required ## imported from flask_login
def logout():
    logout_user() ## imported from flask_login
    flash('You logged out!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in Successfully!')

            next = request.args.get('next')
            print(next)

            if next == None or not next[0] == '/':
                print(next)
                next = url_for('welcome_user')

            return redirect(next)

    return render_template('login.html', form=form)


