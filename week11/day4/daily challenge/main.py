import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/blank/<color>')
def blank(color):
    return flask.render_template('blank.html', color=color)


app.run()
