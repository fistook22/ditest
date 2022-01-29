from sqlalchemy import ForeignKey

from account import db

cards_decks = db.Table('cards_decks', db.Model,
                       db.Column('card_id', db.Integer, db.ForeignKey('card.id')),
                       db.Column('deck_id', db.Integer, db.ForeignKey('deck.id')))


class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    card_type = db.Column(db.String)
    xp = db.Column(db.integer)

    user = db.relationship('User')
    deck = db.relationship("Deck", secondary=cards_decks)


class Deck(db.Model):
    deck_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, ForeignKey('user.user_id'))
    card = db.relationship("Card", secondary=cards_decks)


class Transaction(db.Model):
    pass