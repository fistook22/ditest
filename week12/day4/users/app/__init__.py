import random

import flask
import flask_migrate
import flask_sqlalchemy

from app.models import User
from config import Config

app = flask.Flask(__name__)
app.config.from_object(Config)

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)


def rand():
    options = ("client", "admin")
    User.status = random.choice(options)

from app import routes, models
