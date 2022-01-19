from app import app
from flask import render_template


@app.route('/homepage', methods=['GET', 'POST'])
def index():
    return render_template('homepage.html')


@app.route('/addFilm', methods=['GET', 'POST'])
def addFilm():
    return render_template('addFilm.html')


@app.route('/addDirector', methods=['GET', 'POST'])
def addDirector():
    return render_template('addDirector.html')
