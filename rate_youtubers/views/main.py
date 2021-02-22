from flask import Blueprint, render_template

from ..models import User

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('pages/home.html')


@main.route('/admin-panel')
def admin_panel():
    users = User.query.all()
    return render_template('pages/admin-panel.html', users=users)
