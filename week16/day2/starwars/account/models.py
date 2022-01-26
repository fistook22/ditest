from flask_login import UserMixin
from flask_login._compat import unicode
from sqlalchemy import ForeignKey

from account import db


class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    specie = db.relationship('Profile')

    def get_id(self):
        return unicode(self.user_id)


class Profile(db.Model):
    profile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    specie = db.Column(db.Integer, ForeignKey('user.user_id'))
    image = db.Column(db.LargeBinary)
    points = db.Column(db.Integer)
