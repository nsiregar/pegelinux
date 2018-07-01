from app import app
from app import db
from datetime import datetime


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    parent_id = db.Column(db.Integer, db.ForeignKey('comment.id'), index=True)
    messages = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    is_spam = db.Column(db.Boolean, default=False)
    replies = db.relationship('Comment', remote_side=id, backref='comment')
    depth = db.Column(db.Integer, default=0)

    def __repr__(self):
        return 'Comment {}'.format(self.id)
