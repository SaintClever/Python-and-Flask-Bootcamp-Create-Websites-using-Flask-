import os
from forms import AddForm, DelForm, AddOwner
from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


## MODEL/s
class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppies', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f'Puppy {self.name} has an owner named {self.owner.name}'
        else:
            return f'Puppy {self.name} has no owner yet'


class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f'Owner is {self.name}'


## VIEW/s
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    form = AddOwner()

    if form.validate_on_submit():
        new_owner = form.owner_name.data
        pup_id = form.id.data

        new_owner = Owner(new_owner, pup_id)
        print(new_owner)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add_owner.html', form=form)


@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html', form=form)


@app.route('/delete', methods=['GET', 'POST'])
def del_pup():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup_id = Puppy.query.get(id)
        db.session.delete(pup_id)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('delete.html', form=form)


@app.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@app.errorhandler(404)
def error_hander(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)