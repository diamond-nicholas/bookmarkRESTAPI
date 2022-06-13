from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import backref
from enum import unique
import string
import random

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(80), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), unique=True, nullable=False)
    created_at= db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    bookmarks = db.relationship('Bookmark', backref='user')


    def __ref__(self) -> str:
        return 'User>>>> {self.username}'

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    short_url = db.Column(db.String(3), nullable=True)
    visit= db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def generate_shortener(self):
        characters = string.digits+string.ascii_letters
        picked_char = ''.join(random.choice(characters, k=3))
        link = self.query.filter_by(short_url=picked_char).first()

        if link:
            self.generate_shortener()
        else:
            return picked_char

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.short_url= self.generate_shortener()




