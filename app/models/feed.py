from app import app
from app import db


class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(120), unique=True, index=True)
    rss = db.Column(db.String(128), unique=True)
    html = db.Column(db.String(128), unique=True)
    approved = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def is_approved(self):
        return True if self.approved == 1 else False

    def __repr__(self):
        return 'Feed {}'.format(self.html)