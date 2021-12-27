# First, we are in a different file, so we need to import the app
import flask
from app import app


@app.route("/")
def index():
    a = "<a href='{{ url_for('add_city_form') }}'> Add city </a>"
    return flask.render_template_string(a)


@app.route("/", methods=("GET", "POST"))
def add_city_form():
    return flask.render_template("add_city.html")
