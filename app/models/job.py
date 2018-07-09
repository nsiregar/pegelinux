from app import app
from app import db


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    company = db.Column(db.String(120))
    location = db.Column(db.String(255))
    description = db.Column(db.Text)
    skills = db.Column(db.Text)
    website = db.Column(db.String(120))
    contact = db.Column(db.Text)
    employment = db.Column(db.String(100))
    on_site = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=False)
    is_removed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_at = db.Column(db.DateTime)

    def __repr__(self):
        return "Job {}".format(self.id)
