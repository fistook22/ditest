from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to my store!"


@app.route("/products")
def products():
    return render_template(products.json)


@app.route("/product/product/<product_id>")
def product(product_id):
    return render_template(products.json.id)

@app.route("/cart")
def item():
    return

cart_item = []