from db import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "user"
    idx = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, default=18)
    name = db.Column(db.String(20))
    id = db.Column(db.String(20), unique=True)
    pw = db.Column(db.String(20))
    created = db.Column(db.DateTime, default=datetime.now)

class Comment(db.Model):
    __tablename__ = "comment"
    idx = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    who = db.Column(db.Integer, db.ForeignKey('user.idx'))

class Board(db.Model):
    __tablename__ = "board"
    idx = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    good = db.Column(db.String(100))
    bad = db.Column(db.String(100))
    count = db.Column(db.String(100))
    text = db.Column(db.String(10000))
    writer = db.Column(db.String(100))
    created = db.Column(db.DateTime, default=datetime.now)
    num = db.Column(db.Integer())
