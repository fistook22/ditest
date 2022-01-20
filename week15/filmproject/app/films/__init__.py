import random

import flask_login
from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True

my_blueprint = Blueprint('films', __name__, template_folder='templates', static_folder='static')

db_info = {'host': 'localhost',
           'database': 'imdb',
           'psw': 'fistook22',
           'user': 'postgres',
           'port': ''}

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
login_mngr = flask_login.LoginManager(app)
login_mngr.login_view = 'login'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
