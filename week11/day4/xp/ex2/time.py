import datetime

import flask


app = flask.Flask(__name__)


@app.route('/')
def time():
    d = datetime.datetime.now()

    return flask.render_template("clock.html", datetime_obj = d)


app.run()
