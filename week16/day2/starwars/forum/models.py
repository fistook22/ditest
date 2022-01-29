from sqlalchemy import ForeignKey

from account import db


class Thread(db.Model):
    thread_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String)
    creator = db.Column(db.Integer, ForeignKey('user.user_id'))


class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String)
    thread = db.Column(db.Integer, ForeignKey('thread.thread_id'))
    user = db.Column(db.Integer, ForeignKey('user.user_id'))
