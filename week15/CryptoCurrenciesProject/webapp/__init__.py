import random

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import flask_login

app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True

db_info = {'host': 'localhost',
           'database': 'crypto',
           'psw': 'fistook22',
           'user': 'postgres',
           'port': ''}

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# login_mngr = flask_login.LoginManager(app)
# login_mngr.login_view = 'login'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from webapp import routes
