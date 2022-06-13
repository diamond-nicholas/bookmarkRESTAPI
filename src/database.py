from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(80), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), unique=True, nullable=False)
    created_at= db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())


    def __ref__(self) -> str:
        return 'User>>>> {self.username}'