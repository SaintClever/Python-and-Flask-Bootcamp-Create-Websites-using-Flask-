import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ is atomatically set to basic.py with the above code
# print(basedir)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite') # <-- Database location setup
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db) 

####################

# Model - AKA Table in database
class Puppy(db.Model):

    # MANUAL TABLE NAME CHOICE!
    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f'Puppy {self.name} is {self.age} year/s old'

if __name__ == '__main__':
    app.run(debug=True)


# Terminal Migrate commands


### INSTALL Flask-Migrate first ###
'''
pip install Flask-Migrate
export FLASK_APP=basic.py # set just once
flask db init
flask db migrate -m "some message"
flask db upgrade
'''