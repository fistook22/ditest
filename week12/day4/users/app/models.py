import random

from app import db


class User(db.Model):
    cod = ["client", "admin"]
    item = random.choice(cod)
    name = db.Column(db.String, primary_key=True)
    city_name = db.Column(db.String)
    status = db.Column(db.String(item), nullable=False)

    def add_to_user_table(self):
        self.name = User.name
        self.city_name = User.city_name
        self.status = User.status

        db.session.add(self)
        db.session.commit()
