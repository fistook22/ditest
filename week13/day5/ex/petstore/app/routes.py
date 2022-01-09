import requests
from app import app, db
from flask import redirect, render_template


@app.route('/', methods=['GET', 'POST'])
def index():
    response = requests.get('https://cat-fact.herokuapp.com/GET/facts/random')
    data = response.text
    return render_template('index.html', data=data)


@app.route('/pets', methods=['GET', 'POST'])
def pets():
    return render_template('pets.html')


@app.route('/pet/<int:pet_id>', methods=['GET', 'POST'])
def pet():
    return render_template('pet.html')


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    return render_template('cart.html')


@app.route('/add_pet/<int:pet_id>', methods=['GET', 'POST'])
def add_pet():
    return redirect('pets.html')
