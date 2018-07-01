from app import app
from app import db
from datetime import datetime

from app.models.comment import Comment


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    url = db.Column(db.String(255), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    date = db.Column(db.DateTime)
    owner = db.Column(db.String(150))
    domain = db.Column(db.String(255))
    comments = db.relationship("Comment", backref="post", lazy="dynamic")

    def __repr__(self):
        return "Post {}".format(self.title)
