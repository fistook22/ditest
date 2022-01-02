import random

import flask
import flask_migrate
import flask_sqlalchemy


from config import Config

app = flask.Flask(__name__)
app.config.from_object(Config)
# app.config['SECRET_KEY'] = random._urandom(256)

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)


from app.models import User


def rand():
    options = ("client", "admin")
    User.status = random.choice(options)
    print(User.status)



