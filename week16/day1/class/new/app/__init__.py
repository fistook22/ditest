from flask import flask, Flask
from flask_babel import Babel

app = Flask('__name__')
babel = Babel(app)

