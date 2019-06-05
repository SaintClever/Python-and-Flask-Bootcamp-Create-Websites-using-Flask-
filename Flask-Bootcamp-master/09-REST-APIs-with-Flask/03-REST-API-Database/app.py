import os
from flask import Flask,  request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource
from secure_check import authenticate,identity
from flask_jwt import JWT ,jwt_required
from flask_migrate import Migrate


app = Flask(__name__)

###################################################
################ CONFIGURATIONS ###################
##################################################

# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)
jwt = JWT(app, authenticate, identity)
api = Api(app)

###################################################
################ MODELS ###########################
##################################################


class Puppy(db.Model):
    name = db.Column(db.String(80),primary_key=True)


    def __init__(self,name):
        self.name=name

    def json(self):
        return {'name': self.name}

    def __str__(self):
        return f"{self.name} "

###################################################
################ RESOURCES ###########################
##################################################

class PuppyResource(Resource):
    def get(self,name):

        pup = Puppy.query.filter_by(name=name).first()

        if pup:
            return pup.json()
        else:
            # If you request a puppy not yet in the puppies list
            return {'name':'not found'}, 404

    def post(self,name):

        pup = Puppy(name=name)
        db.session.add(pup)
        db.session.commit()

        return pup.json()


    def delete(self,name):

        pup = Puppy.query.filter_by(name=name).first()
        db.session.delete(pup)
        db.session.commit()

        return {'note':'delete successful'}




class AllPuppies(Resource):

    @jwt_required()
    def get(self):
        # return all the puppies :)
        puppies = Puppy.query.all()

        # return json of (puppies)
        return [pup.json() for pup in puppies]


api.add_resource(PuppyResource, '/puppy/<string:name>')
api.add_resource(AllPuppies,'/puppies')

if __name__ == '__main__':
    app.run(debug=True)
