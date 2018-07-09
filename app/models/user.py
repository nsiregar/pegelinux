from app import app
from app import db
from app import login
import jwt
from time import time
from app import app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from app.models.comment import Comment
from app.models.feed import Feed
from app.models.job import Job

USER_ROLES = ["admin", "momod", "jelata"]


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password = db.Column(db.String(255))
    is_verified = db.Column(db.Boolean, default=False)
    role = db.Column(db.String(6), default="jelata")
    feeds = db.relationship("Feed", backref="user", lazy="dynamic")
    comments = db.relationship("Comment", backref="user", lazy="dynamic")
    jobs = db.relationship("Job", backref="user", lazy="dynamic")

    @staticmethod
    def verify_token(token):
        try:
            id = jwt.decode(token, app.config.get("SECRET_KEY"), algorithms=["HS256"])[
                "reset_password"
            ]
            return User.query.get(id)
        except:
            return None

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_token(self, expires=3600 * 24):
        token = jwt.encode(
            {"reset_password": self.id, "exp": time() + expires},
            app.config.get("SECRET_KEY"),
            algorithm="HS256",
        ).decode("utf-8")
        return token

    def __repr__(self):
        return "User {}".format(self.username)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
