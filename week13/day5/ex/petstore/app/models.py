import datetime

from sqlalchemy.orm import validates

from app import db


class Pet(db.Model):
    pet_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet_name = db.Column(db.String(64), unique=True)
    gender = db.Column(db.String(2))
    breed = db.Column(db.String(64))
    date_of_birth = db.Column(db.Date(), default=datetime.date.today())
    details = db.Column(db.Text)
    price = db.Column(db.Integer)
    image = db.Column(db.String(64))

    cart = db.Column(db.Integer, db.ForeignKey('cart.cart_id'))

    @validates('gender')
    def validate_gender(self, key, gender):
        if gender not in ['M', 'F']:
            raise Exception(f'the gender {gender} must be "M" or "F"')


class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    pets = db.relationship('Pet', backref='cart', lazy='dynamic')
#
#     def add_to_cart(self, pet_id):
#         self.cart_id.append(pet_id)
#
#     def get_cart(self):
#         return Cart.query.all()
#
#     def get_total(self):
#         return sum(Pet.price)
