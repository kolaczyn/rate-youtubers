from flask import Blueprint, render_template, request, session, redirect, url_for

from ..models import User
from ..extensions import db
from ..forms import LoginForm, RegisterForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return render_template('auth/login.html', form=form)

    # if request.method == 'POST':
    #     email = request.form['email']
    #     user = User(email=email)
    #     try:
    #         db.session.add(user)
    #         db.session.commit()
    #     except:
    #         return 'something went wrong'

    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        return render_template('auth/register.html', form=form)
    #     print(form.username.data, form.password.data)
    #     return render_template('auth/register.html', form=form)
        # return redirect(url_for('main.login'))

    return render_template('auth/register.html', form=form)


@auth.route('/me')
def me():
    return 'you hit me'
