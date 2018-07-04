from app import app
from app import db

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

from flask_login import login_required, current_user

from app.forms.feed_form import SubmissionForm
from app.forms.feed_form import FeedModerationForm

from app.models.feed import Feed

from app.helper.auth_helper import requires_roles

feed = Blueprint("feed", __name__)


@feed.route("/submit", methods=["GET", "POST"])
@login_required
def submit():
    form = SubmissionForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            feed = Feed(owner=form.owner.data, rss=form.rss.data, html=form.html.data, user_id=current_user.id)
            db.session.add(feed)
            db.session.commit()
        return redirect(url_for("home.index"))
    return render_template("/feed/submit.html", title="submission", form=form)


@feed.route("/moderate", methods=["GET"])
@login_required
@requires_roles("admin", "momod")
def moderation():
    submission = Feed.query.all()
    return render_template(
        "/feed/moderation.html", title="moderation", submission=submission
    )


@feed.route("/moderate/<int:id>", methods=["GET", "POST"])
@login_required
@requires_roles("admin", "momod")
def modify(id):
    news = Feed.query.filter_by(id=id).first()
    form = FeedModerationForm(obj=news)
    if form.validate_on_submit():
        news.approved = form.approved.data
        db.session.commit()
        return redirect(url_for("feed.moderation"))
    if request.method == "GET":
        form.approved.data = news.approved
    return render_template("/feed/modify.html", title="modify", form=form, news=news)
