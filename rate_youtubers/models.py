from .extensions import db


class Youtuber(db.Model):
    id = db.Column(db.String(24), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    description = db.Column(db.String(1000), unique=False, nullable=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), unique=True, nullable=False)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'User no. {self.id} | email: {self.email} | username: {self.username}'
