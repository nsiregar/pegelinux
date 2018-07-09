from datetime import datetime

from app import app
from app import db

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask_login import login_required
from flask_login import current_user

from app.models.comment import Comment
from app.models.post import Post

from app.forms.comment_form import CommentForm
from app.helper.auth_helper import requires_roles

comment = Blueprint("comment", __name__)


@comment.route("/reply/<int:id>", methods=["GET", "POST"])
@login_required
def reply(id):
    parent = Comment.query.get(int(id))
    max_depth = app.config.get("MAX_DEPTH")
    current_depth = parent.depth + 1
    form = CommentForm()
    if form.validate_on_submit():
        r = Comment(messages=form.messages.data)
        r.parent_id = id
        r.post_id = parent.post_id
        r.user_id = current_user.id
        r.created_at = datetime.utcnow()
        r.depth = current_depth if current_depth <= max_depth else max_depth
        db.session.add(r)
        db.session.commit()
        return redirect(url_for("comment.comments", id=parent.post_id))
    if request.method == "GET":
        form.messages.data = ""
    return render_template(
        "/comment/replies.html", title="reply", form=form, parent=parent
    )


@comment.route("/comment/<int:id>", methods=["GET", "POST"])
def comments(id):
    post = Post.query.get(int(id))
    comments = (
        Comment.query.filter_by(post_id=id, depth=0).order_by(Comment.created_at).all()
    )
    form = CommentForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            c = Comment(messages=form.messages.data)
            c.post_id = post.id
            c.user_id = current_user.id
            c.created_at = datetime.utcnow()
            db.session.add(c)
            db.session.commit()
            return redirect(url_for("comment.comments", id=post.id))
        return redirect(url_for("auth.login"))
    if request.method == "GET":
        form.messages.data = ""
    return render_template(
        "/comment/comment.html",
        title="comment",
        form=form,
        post=post,
        comments=comments,
    )


@comment.route("/comment/<int:post_id>/<int:id>", methods=["GET"])
@requires_roles("admin", "momod")
def mark_spam(post_id, id):
    comments = Comment.query.get(int(id))
    comments.is_spam = True
    db.session.commit()
    return redirect(url_for("comment.comments", id=post_id))
