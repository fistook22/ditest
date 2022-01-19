import random

from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import films

app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True

my_blueprint = Blueprint('films', __name__, template_folder='templates', static_folder='static')


def create_app():
    from .films import films_blueprint


app.register_blueprint(films, url_prefix="/films")

db_info = {'host': 'localhost',
           'database': 'imdb',
           'user': 'postgres',
           'port': ''}

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes

if __name__ == '__main__':
    app.run(debug=True)
