from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return "<a href='{{ url_for('lesson') }}'>The lesson</a>\n<a href='{{ url_for('exercise') }}'>The exercise</a>"


@app.route("/")
def lesson():
    return render_template("less.html")


@app.route("/")
def exercise():
    return render_template("ex.html")


if __name__ == "__main__":
    app.run()
