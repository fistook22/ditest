from app import db


class User(db.Model):
	name = db.Column(db.String, primary_key=True)
	city_name = db.Column(db.String)
	status = db.Column(db.string)

	def add_to_user_table(self):
		self.name = User.name
		self.city_name = User.city_name
		self.status = User.status

		db.session.add(self)
		db.session.commit()
