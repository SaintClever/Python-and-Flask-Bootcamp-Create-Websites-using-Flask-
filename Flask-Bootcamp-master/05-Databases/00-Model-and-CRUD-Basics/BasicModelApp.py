import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
######################################
#### SET UP OUR SQLite DATABASE #####
####################################

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#####################################
####################################
###################################

# Let's create our first model!
# We inherit from db.Model class
class Puppy(db.Model):

    # If you don't provide this, the default table name will be the class name
    __tablename__ = 'puppies'

    # Now create the columns
    # Lots of possible types. We'll introduce through out the course
    # Full docs: http://docs.sqlalchemy.org/en/latest/core/types.html

    #########################################
    ## CREATE THE COLUMNS FOR THE TABLE ####
    #######################################

    # Primary Key column, unique id for each puppy
    id = db.Column(db.Integer,primary_key=True)
    # Puppy name
    name = db.Column(db.Text)
    # Puppy age in years
    age = db.Column(db.Integer)

    # This sets what an instance in this table will have
    # Note the id will be auto-created for us later, so we don't add it here!
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        # This is the string representation of a puppy in the model
        return f"Puppy {self.name} is {self.age} years old."
