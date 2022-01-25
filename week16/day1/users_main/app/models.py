import flask_login

from app import db


class User(flask_login.UserMixin, db.Model):
	user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String, )
	password = db.Column(db.String)

	def get_id(self):
		# Returns the field that we (our database) consider as id (primary key)
		return self.user_id
