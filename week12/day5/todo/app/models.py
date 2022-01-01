from app import db


class User(db.Model):
    name = db.Column(db.String, primary_key=True)
    details = db.Column(db.String)

    def save_task_to_db(self):
        self.name = User.name
        self.details = User.details

        db.session.add(self)
        db.session.commit()
