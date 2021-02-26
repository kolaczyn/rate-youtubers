from flask import Blueprint, render_template, request, session, redirect, url_for, redirect, g
from werkzeug.security import check_password_hash, generate_password_hash

from ..models import User
from ..extensions import db
from ..forms import LoginForm, RegisterForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # TODO this looks dumb, surely there's a better way
        user = User.query.filter_by(email=email).first()

        # this should probably redirect to the form and give user now found error
        if user is None:
            return 'Not found'

        if check_password_hash(user.password, password):
            session.clear()
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('main.index'))
        else:
            return 'incorrect password'

    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data

        user = User(email=email, username=username,
                    password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return redirect('login', 201)

    return render_template('auth/register.html', form=form)


@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))


@auth.route('/me')
def me():
    return 'you hit me'
