from app import db


class Association(db.Model):
    person = db.Column('person_id', db.Integer, db.Foreign_key('person.person_id')),
    nationality = db.Column('nationality_id', db.Integer, db.Foreign_key('nationality.nationality_id'))


class Person(db.Model):
    person_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    address = db.Column(db.String(64)),
    phonenumbers = db.relationship('PhoneNumber', backref='person', lazy='dynamic', cascade="all,delete")
    nationalities = db.relationship('Nationality', secondary=Association.__table__, backref='person')


class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(64))
    owner = db.Column(db.Integer, db.ForeignKey('person.person_id'))


class Nationality(db.Model):
    nationality_id = db.Column(db.Integer, primary_key=True),
    name = db.Column(db.String(64)),
    people = db.relationship('Person', secondary=Association.__table__, backref='nationality')
