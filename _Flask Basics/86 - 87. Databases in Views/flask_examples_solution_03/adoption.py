import os
from forms import AddForm_Pup, DeleteForm_Pup, AddForm_Owner
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
            return f'Puppy {self.name}\'s owner is {self.owner.name}'
        else:
            return f'Puppy {self.name} currently has no owner yet!'


class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    pupp_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.pupp_id = puppy_id

    def __repr__(self):
        return f'The owner is {self.name}'


## VIEW/s
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_pup', methods=['GET', 'POST'])
def add_pup():

    form = AddForm_Pup()

    if form.validate_on_submit():
        pup_name = form.name.data
        new_pup = Puppy(pup_name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pups'))
    return render_template('add_pup.html', form=form)
        
        
@app.route('/delete_pup', methods=['GET', 'POST'])
def delete_pup():

    form = DeleteForm_Pup()

    if form.validate_on_submit():
        if form.id.data or form.name.data:
            pup_id = form.id.data
            del_pup_id = Puppy.query.get(pup_id)

            name = form.name.data
            del_pup_name = Puppy.query.filter_by(name=name).first()

            db.session.delete[(del_pup_id, del_pup_name)]
            db.session.commit()

        return redirect(url_for('list_pups'))
    return render_template('delete_pup.html', form=form)


@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    
    form = AddForm_Owner()

    if form.validate_on_submit():
        id = form.id.data
        name = form.name.data
        new_owner = Owner(name, id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pups'))
    return render_template('add_owner.html', form=form)


@app.route('/list_pups')
def list_pups():
    puppies = Puppy.query.all()
    return render_template('list_pups.html', puppies=puppies)


@app.errorhandler(404)
def error_handler(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)