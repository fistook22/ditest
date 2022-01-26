import flask_login
import flask_migrate
import flask_sqlalchemy
from flask import Blueprint

from admin import admin
from forum import forum
from market import market

account = Blueprint('account', __name__, url_prefix='/account')
db = flask_sqlalchemy.SQLAlchemy()
migrate = flask_migrate.Migrate()
login_manager = flask_login.LoginManager()


def create_app():
    from config import Config
    from flask import Flask
    from account import models
    from account import routes

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.app_context()
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'login'
    login_manager.refresh_view = 'accounts.reauthenticate'
    login_manager.needs_refresh_message = (
        u'To protect your account, please reauthenticate to access this page.')

    app.register_blueprint(account, url_prefix='/account')
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(forum, url_prefix='/forum')
    app.register_blueprint(market, url_prefix='/market')

    return app
