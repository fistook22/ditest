from webapp import db

user_crypto_table = db.Table('user_crypto',
                             db.Column('username', db.Integer, db.ForeignKey('user.username')),
                             db.Column('crypto_id', db.Integer, db.ForeignKey('crypto.crypto_id'))
                             )


class User(db.Model):
    username = db.Column(db.String(64))
    email = db.Column(db.Email())
    password = db.Column(db.Password())

    coins = db.relationship('Crypto', secondary=user_crypto_table, backref='user')


class Crypto(db.Model):
    crypto_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(64))
    symbol = db.Column(db.String(64))
    slug = db.Column(db.String(64))
    first_historical_data = db.Column(db.String(64))
    last_historical_data = db.Column(db.String(64))
    is_active = db.Column(db.Integer)

    users = db.relationship('User', secondary=user_crypto_table, backref='crypto')


