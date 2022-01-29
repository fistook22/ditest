from flask_login import login_required

from account.models import User
from admin import admin
from forum.models import Thread
from market.models import Card


@admin.route('/delete', methods=['GET', 'POST'])
@login_required
def Delete():
    User.query.filter_by(id=123).delete()
    Thread.query.filter_by(id=123).delete()
    Card.query.filter_by(id=123).delete()