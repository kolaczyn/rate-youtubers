from datetime import datetime

from flask import Flask, Blueprint, request, g, session
from flask.cli import with_appcontext
import click

from .extensions import db
from .views.auth import auth
from .views.youtubers import youtubers
from .views.main import main
from .fill_db_with_data import fill_db


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(youtubers, url_prefix='/youtubers')
    app.register_blueprint(main)

    @app.before_request
    def set_context():
        g.user_id = session.get('user_id')
        g.username = session.get('username')
        g.email = session.get('email')

    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()}

    @click.command(name='create')
    @with_appcontext
    def create():
        db.create_all()
        fill_db()

    app.cli.add_command(create)

    return app
