import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

# CLASS
class Character(db.Model):

    # Table name
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    universe = db.Column(db.Text)
    taunt = db.Column(db.Text)
    super_move = db.Column(db.Text)
    ultra_move = db.Column(db.Text)
    ultimate = db.Column(db.Text)


    def __init__(self, name, universe, taunt, super_move, ultra_move, ultimate):
        self.name = name
        self.universe = universe
        self.taunt = taunt
        self.super_move = super_move
        self.ultra_move = ultra_move
        self.ultimate = ultimate

    def __repr__(self):
        return f"Character: {self.name} | {self.universe} | {self.taunt} | {self.super_move} | {self.ultra_move} | {self.ultimate}"


if __name__ == '__main__':
    app.run(debug=True)