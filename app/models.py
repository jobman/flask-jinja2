from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    telegram = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(256))

    def __repr__(self):
        return 'id({}) username({}) email({}) tg({})'.format(self.id, self.username, self.email, self.telegram)
