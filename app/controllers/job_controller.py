from app import app
from app import db
from datetime import datetime

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import flash
from flask_login import current_user
from flask_login import login_required

from app.models.job import Job

from app.forms.job_form import JobSubmissionForm

from app.helper.auth_helper import requires_roles

job = Blueprint("job", __name__)

@job.route("/job", methods=["GET"])
def listing():
    jobs = Job.query.filter_by(is_active=True, is_removed=False).all()
    return render_template("/job/list.html", title="opening jobs", jobs=jobs)

@job.route("/job/<int:id>", methods=["GET"])
def view(id):
    jobs = Job.query.get(int(id))
    return render_template("/job/detail.html", title="job detail", jobs=jobs)

@job.route("/job/submit", methods=["GET", "POST"])
@login_required
def submit():
    form = JobSubmissionForm()
    if form.validate_on_submit():
        jobs = Job(
            title=form.title.data,
            company=form.company.data,
            description=form.description.data,
            skills=form.skills.data,
            website=form.website.data,
            contact=form.contact.data,
            employment=form.employment.data,
            on_site=form.on_site.data
        )
        jobs.user_id = current_user.id
        jobs.created_at = datetime.utcnow()
        db.session.add(jobs)
        db.session.commit()
        return redirect(url_for("job.listing"))
    return render_template("/job/submit.html", title="job submission", form=form)

@job.route("/job/moderation", methods=["GET"])
@login_required
@requires_roles("admin", "momod")
def moderation():
    jobs = Job.query.all()
    return render_template("/job/moderation.html", title="jobs moderation", jobs=jobs)

@job.route("/job/remove/<int:id>", methods=["GET"])
@login_required
@requires_roles("admin", "momod")
def remove(id):
    jobs = Job.query.get(int(id))
    jobs.is_removed = True
    db.session.commit()
    return redirect(url_for("job.moderation"))

@job.route("/job/activate/<int:id>", methods=["GET"])
@login_required
@requires_roles("admin", "momod")
def activate(id):
    jobs = Job.query.get(int(id))
    jobs.is_active = True
    db.session.commit()
    return redirect(url_for("job.moderation"))