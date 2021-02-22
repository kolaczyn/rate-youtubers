from flask import Blueprint, render_template, request

from .models import User
from .extensions import db

main = Blueprint('main', __name__)


@main.route('/')
def main_index():
    return 'Blueprint Views.py Hello'


@main.route('/auth', methods=['POST', 'GET'])
def auth():
    if request.method == 'POST':
        email = request.form['email']
        user = User(email=email)
        try:
            db.session.add(user)
            db.session.commit()
        except:
            return 'something went wrong'

    for user in User.query.all():
        print(user)
    return render_template('login.html')
