from flask import Flask, Blueprint
from flask.cli import with_appcontext
import click

from .extensions import db
from .views.auth import auth
from .views.main import main


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(main)

    @click.command(name='create')
    @with_appcontext
    def create():
        db.create_all()

    app.cli.add_command(create)

    return app
