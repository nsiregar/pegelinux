from app import app
from app import db
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

USER_ROLES = ['admin', 'momod', 'jelata']

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(6), default='jelata')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return 'User {}'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))