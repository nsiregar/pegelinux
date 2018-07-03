from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from datetime import datetime

from app.models.post import Post

home = Blueprint("home", __name__)


@home.route("/", methods=["GET"])
@home.route("/index", methods=["GET"])
def index():
    page = request.args.get("page", 1, type=int)
    posts = (
        Post.query.filter(Post.created_at <= datetime.utcnow())
        .order_by(Post.date.desc())
        .paginate(page, 20, False)
    )
    prev_page = url_for("home.index", page=posts.prev_num) if posts.has_prev else None
    next_page = url_for("home.index", page=posts.next_num) if posts.has_next else None
    return render_template(
        "/application/home.html", posts=posts, prev_page=prev_page, next_page=next_page
    )


@home.route("/about", methods=["GET"])
def about():
    return render_template("/application/about.html", title="about")
