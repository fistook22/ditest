from flask import Flask, render_template, render_template_string

app = Flask(__name__)

products = render_template_string("static/product_db.json")


@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/products')
def products():
    return


#
# @app.route('/products/<product_id>')
# def product_details():
#     open('product_db.json', 'r').read()
#     return render_template_string('static/product_db.json')


app.run()
