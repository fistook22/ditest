import flask
from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return flask.render_template('index.html')


@app.route("/lesson")
@app.route("/")
def lesson():
    return flask.render_template("less.html")


@app.route("/ex")
@app.route("/")
def exercise():
    return flask.render_template("ex.html")


if __name__ == "__main__":
    app.run()
