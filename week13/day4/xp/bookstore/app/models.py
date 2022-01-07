from app import db


class PhoneNumber(db.Model):
	phone_number_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	number = db.Column(db.String(20))

	owner_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), )


class Person(db.Model):
	person_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(64))
	email = db.Column(db.String(64), unique=True)
	address = db.Column(db.String(64))

	phonenumbers = db.relationship('PhoneNumber', backref='person', lazy='dynamic', cascade="all,delete")
