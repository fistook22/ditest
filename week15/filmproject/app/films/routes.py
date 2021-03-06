import flask
import flask_login

from flask import render_template
from flask import url_for

from films import app, db, my_blueprint
from films.forms import Login, SignUp
from films.models import User

from app.films import login_mngr

app.register_blueprint(my_blueprint, url_prefix="/films")


@app.route('/homepage', methods=['GET', 'POST'])
def index():
    return render_template('homepage.html')


@app.route('/addFilm', methods=['GET', 'POST'])
def addFilm():
    return render_template('addFilm.html')


@app.route('/addDirector', methods=['GET', 'POST'])
def addDirector():
    return render_template('addDirector.html')


@login_mngr.user_loader
def load_user(userid):
    userid = int(userid)
    return User.query.get(userid)


@app.route('/login', methods=["GET", "POST"])
def login():
    if flask_login.current_user.is_authenticated:  # Check if the user is not already logged in
        return flask.redirect(url_for('homepage'))

    form = Login()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # Check if it exist and if the password is the right password
        if user is None or not user.password == form.password.data:
            flask.flash('Invalid username or password')
            return flask.redirect(url_for('login'))

        # Log the user in
        flask_login.login_user(user, remember=form.remember_me.data)
        return flask.redirect(url_for('homepage'))

    return flask.render_template('login.html', form=form)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUp()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password1.data

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return flask.redirect('/login')

    return flask.render_template('register.html', form=form)


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return flask.redirect(url_for('login'))


@app.route('/my_info')
@flask_login.login_required
def my_info(username):
    return flask.render_template('profile.html', username=username)
