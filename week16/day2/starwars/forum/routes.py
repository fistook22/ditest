import flask
from flask import url_for, redirect
from flask_login import login_required

from account import db
from forum import forum
from forum.models import Thread


@forum.route('/create_thread', methods=['GET', 'POST'])
@login_required
def New_thread():

    form = create_thread()

    if form.validate_on_submit():
        subject = form.subject.data
        creator = form.creator.data

        thread = Thread(subject=subject, creator=creator)
        db.session.add(thread)
        db.session.commit()

        return flask.redirect(url_for('forum.forum'))

    return flask.render_template('create_thread.html', form=form)


@forum.route('/forum', methods=['GET', 'POST'])
@login_required
def forum():
    thread = Thread.query.filter_by(thread_id=thread.thread_id.data).first()
    return flask.render_template('forum.html')