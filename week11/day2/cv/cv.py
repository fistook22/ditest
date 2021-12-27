import flask
from flask import Flask, url_for

app = Flask(__name__)


# default-page
@app.route('/')
@app.route('/home')
def home():
    a = "<a href='{{ url_for('about') }}'> About Shai </a>"
    return flask.render_template_string(a)


# about-page
@app.route('/about')
def about():
    html = '''
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>ABOUT</title>
  </head>
  <body>
    <img src = "./shai.jpg">
    <h1>Shai Amir</h1>
    <h2>My skills: full-stack development</h2>
    <h3>My strengths: responsible, team player</h3>
    <h3>My weaknesses: lazy developer</h3>
  </body>
</html>'''

    return html


if __name__ == '__main__':
    app.run()
