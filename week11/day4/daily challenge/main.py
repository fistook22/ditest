from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blank/<color>')
def blank(color):
    return render_template('blank.html', color=color)


app.run()
