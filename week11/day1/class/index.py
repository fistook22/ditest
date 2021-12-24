import flask
from flask import render_template_string

app = flask.Flask(__name__)


@app.route('/')
def index():
    return """Hello, World!!!!!
    < a href = {{url_for('home_page')}} > home_page </a>"""


@app.route('/home_page/<username>/<lastname>')
def home_page(username, lastname):
    my_template = '''
            <html>
                <head>
                    <title>Home Page - Microblog</title>
                </head>
                <body>
                    <h1>{{ username }} {{ lastname }} says: Wubbalubbadubdub!</h1>
                </body>
            </html>
        '''

    html = render_template_string(my_template, username=username, lastname=lastname)
    return html


app.run(port=8080)
