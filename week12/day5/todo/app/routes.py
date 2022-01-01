import flask

from app import app, db
from app.forms import AddTask
from app.models import User


# @app.route('/')
# def main_page():
#     return 'Wellcome to the main page'
#
#
# @app.route('/login', methods=["GET", "POST"])
# def login():
#     form = Login()
#
#     if form.validate_on_submit():
#         name = form.name.data
#
#         if check_if_user_exist(name):  # if check_if_user_exist(name) == True
#             return flask.redirect('/')
#         else:
#             flask.flash(f"there is no user with the following name {name}")
#
#     return flask.render_template('login.html', form=form)


@app.route('/todo', methods=["GET", "POST"])
def todo():
    form = todo()
    #
    # if form.validate_on_submit():
    #     name = form.name.data
    #     details = form.details.data
    #
    #     user = User(name=name, details=details)
    #     db.session.add(user)
    #     db.session.commit()
    #
        # return flask.redirect('/todo')

    # return flask.render_template('todo.html', form=form)


# def check_if_user_exist(name):
#     # all_users = User.query.all()
#     # for user in all_users:
#     # 	if user.name == name:
#     # 		return True
#     #
#     # return False
#     return User.query.filter_by(name=name).first()
