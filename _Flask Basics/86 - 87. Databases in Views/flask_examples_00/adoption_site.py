import os
from forms import AddForm, DelForm
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


### MODEL/s ###
class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Puppy name is {self.name}'


    
### VIEW/s ###
@app.route('/')
def index():
    return render_template('index.html')



### CREATE ###
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



### DELETE ###
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



### LIST ###
@app.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


if __name__ == '__main__':
    app.run(debug=True)
