import json

from werkzeug.security import generate_password_hash

from .extensions import db
from .models import User, Youtuber


def read_json_from_file(filename):
    with open(filename) as file:
        return json.loads(file.read())


def fill_db():
    """fill the database with some data to work with"""
    data = read_json_from_file('initial_data.json')
    # there's probably a better way to do this
    for user in data['users']:
        new_user = User(email=user['email'],
                        username=user['username'],
                        password=generate_password_hash(user['password']))
        db.session.add(new_user)
    for youtuber in data['youtubers']:
        new_youtuber = Youtuber(id=youtuber['id'],
                                name=youtuber['name'],
                                description=youtuber['description'])
        db.session.add(new_youtuber)
    db.session.commit()
