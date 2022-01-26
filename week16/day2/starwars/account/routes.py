import flask
import flask_login
from flask import url_for, redirect
from flask_login import login_user, login_required, logout_user

from account import login_manager, db, account
from account.forms import Register, Login
from account.models import User, Profile


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(user_id=user_id).first()


@account.route('/index', methods=['GET', 'POST'])
def index():
    return 'May the force be with you'


@account.route('/create_profile', methods=['GET', 'POST'])
@login_required
def create_profile():

    form = create_profile()

    if form.validate_on_submit():
        username = form.username.data
        image = form.image.data

        profile1 = Profile(username=username, image=image)
        db.session.add(profile1)
        db.session.commit()

        return flask.redirect(url_for('account.profile'))

    return flask.render_template('create_profile.html', form=form)


@account.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return redirect(url_for('account.profile'))


@account.route('/register', methods=["GET", "POST"])
def register():
    form = Register()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return flask.redirect(url_for('account.login'))

    return flask.render_template('register.html', form=form)


@account.route('/login', methods=['GET', 'POST'])
def login():
    if flask_login.current_user.is_authenticated:
        return flask.redirect(url_for('account.profile'))

    form = Login()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, remember=True)

        flask.flash('Logged in successfully.')
        return flask.redirect(url_for('account.index'))
    return flask.render_template('login.html', form=form)


@account.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('account.login'))
