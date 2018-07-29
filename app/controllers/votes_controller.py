from app import app
from app import db

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask_login import login_required
from flask_login import current_user

from app.models.post import Post

votes = Blueprint("votes", __name__)

@votes.route("/votes/<int:id>/<str:value>/", methods=["GET"])
def vote(id, value):
    post = Post.query.get(int(id))
    goto = request.args.get("goto", "home", type=str)
    if value == "up":
        post.votes += 1
    if value == "down":
        post.votes -= 1
    db.session.commit()
    if goto == "home":
        return redirect(url_for("home.index"))
    return redirect(url_for("comment.comments", id=post.id))