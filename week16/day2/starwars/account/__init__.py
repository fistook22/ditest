import flask_migrate
import flask_sqlalchemy
from config import Config
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)


login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.refresh_view = 'accounts.reauthenticate'
login_manager.needs_refresh_message = (
    u'To protect your account, please reauthenticate to access this page.')

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from account import routes
