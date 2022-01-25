from flask_login import UserMixin
from flask_login._compat import unicode

from account import db


class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, )
    password = db.Column(db.String)

    def get_id(self):
        return unicode(self.user_id)
