# First, we are in a different file, so we need to import the app
from app import app
from flask import render_template, url_for, redirect


@app.route("/")
def index():
    return redirect(url_for('add_city_form'))


@app.route("/add", methods=("GET", "POST"))
def add_city_form():
    return render_template("add_city.html")
