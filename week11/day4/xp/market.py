from flask import Flask
import flask


app = flask.Flask(__name__)


@app.route('/')
def homepage():
    return "Welcome to Our marketplace"


@app.route('/products')
def products(product_db=None):
    product_db.json.load_database()
    open('my_template.jinja', 'r').read('name')
    return flask.render_template_string('product_db.json')


@app.route('/products/<product_id>')
def product_details():
    open('my_template.jinja', 'r').read()
    return flask.render_template_string('product_db.json', 'product = product_id')


app.run()
