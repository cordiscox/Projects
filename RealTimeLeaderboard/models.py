# models.py

from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    rankings = db.relationship('Ranking', backref='game', lazy=True)
    img = db.Column(db.String(500), unique=True)

class Ranking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    user_name = db.Column(db.String(100))
    id_game = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)

