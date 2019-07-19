import os
from forms import AddForm, DelForm
from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


## MODEL/s ##
class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text) #! name variable is used in DELETE. filter_by(name=etc) 

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Puppy name: {self.name}'

## VIEW/S ##
#- INDEX -#
@app.route('/')
def index():
    return render_template('index.html')


#- CREATE -#
@app.route('/add', methods=['GET', 'POST'])
def add_pup():

    form = AddForm()

    if form.validate_on_submit():
        pup_name = form.name.data
        new_pup = Puppy(pup_name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_pups'))

    return render_template('add.html', form=form)


#- DELETE -#
@app.route('/delete', methods=['GET', 'POST'])
def delete_pup():

    form = DelForm()

    # if form.validate_on_submit():
    #     pup_id = form.id.data
    #     del_pup = Puppy.query.get(pup_id)
    #     db.session.delete(del_pup)
    #     db.session.commit()

    if form.validate_on_submit():
        #! NOTE: del_name is imported from forms.py
        pup_name = form.del_name.data
        print(pup_name)

        #! NOTE: The name variable is from our MODELS above. We select the first occurance by filter_by(name=etc).first() 
        del_pup = Puppy.query.filter_by(name=pup_name).first() # name is from model variable
        print(del_pup)

        db.session.delete(del_pup)
        db.session.commit()
        
        return redirect(url_for('list_pups'))

    return render_template('delete.html', form=form)


#- LIST -#
@app.route('/list')
def list_pups():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


#- 404 ERROR -#
@app.errorhandler(404)
def error_handler(e):
    return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(debug=True)