import flask
from flask_login import login_required

from market import market


@market.route('/homepage', methods=['GET', 'POST'])
@login_required
def Homepage():
    return flask.render_template('homepage.html')


@market.route('/detail', methods=['GET', 'POST'])
@login_required
def Detail():
    return flask.render_template('detail.html')


@market.route('/leaderboard', methods=['GET', 'POST'])
@login_required
def Leaderboard():
    return flask.render_template('leaderboard.html')
