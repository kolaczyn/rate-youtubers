from flask import Blueprint, render_template, request

from .models import User
from .extensions import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('pages/home.html')


@main.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        user = User(email=email)
        try:
            db.session.add(user)
            db.session.commit()
        except:
            return 'something went wrong'

    return render_template('auth/login.html')

@main.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        return 'you cant register as of now'

    return render_template('auth/register.html')
