import flask
from config import Config


app = flask.Flask(__name__)  # Remember: __name__ is the name of the file where the code is written
app.config.from_object(Config)
