import flask
from app import app    # app.app is package_name.variable_name


@app.route("/")
def index():
    return flask.render_template('cv_forms.html')
