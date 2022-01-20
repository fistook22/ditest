from app import db


class User(db.Model):
    username = db.Column(db.String(64))
    email = db.Column(db.Email())
    password = db.Column(db.Password())


class Crypto(db.Model):
    crypto_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(64))
    symbol = db.Column(db.String(64))
    slug = db.Column(db.String(64))
    first_historical_data = db.Column(db.String(64))
    last_historical_data = db.Column(db.String(64))
    is_active = db.Column(db.Integer)
