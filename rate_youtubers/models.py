from .extensions import db


# class Youtuber(db.Model):
#     id = db.Column(db.String(11), unique=True, nullable=False)
#     name = db.Column(db.String(20), unique=False, nullable=False)
#     description = db.Column(db.String(1000), unique=False, nullable=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), unique=True, nullable=False)

    def __repr__(self):
        return f'User, email:{self.email}'
