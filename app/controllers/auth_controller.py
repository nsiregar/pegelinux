from app import app
from app import db

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from werkzeug.urls import url_parse

from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from app.models.user import User
from app.forms.user_form import LoginForm
from app.forms.user_form import RegistrationForm
from app.forms.user_form import UserForm
from app.forms.user_form import ResetPasswordRequestForm
from app.forms.user_form import ResetPasswordForm
from app.helper.auth_helper import requires_roles
from app.helper.mail_helper import send_token_mail

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("home.index")
        return redirect(next_page)
    return render_template("/auth/login.html", title="login", form=form)


@auth.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("home.index"))


@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home.index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        subject = "Verify Registration pegelinux.id"
        send_token_mail(user, subject, "/auth/verification.txt")
        return redirect(url_for("auth.login"))
    return render_template("/auth/register.html", title="register", form=form)


@auth.route("/user", methods=["GET"])
@login_required
@requires_roles("admin")
def moderation():
    users = User.query.all()
    return render_template(
        "/auth/moderation.html", title="user moderation", users=users
    )


@auth.route("/user/<int:id>", methods=["GET", "POST"])
@login_required
@requires_roles("admin")
def modify(id):
    user = User.query.filter_by(id=id).first()
    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.role = form.role.data
        db.session.commit()
        return redirect(url_for("auth.moderation"))
    if request.method == "GET":
        form.role.data = user.role
    return render_template("/auth/modify.html", title="modify", form=form, user=user)


@auth.route("/user/reset", methods=["GET", "POST"])
def request_reset():
    if current_user.is_authenticated:
        return redirect(url_for("home.index"))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            subject = "Reset Password Account {} pegelinux.id".format(user.username)
            send_token_mail(user, subject, "/auth/reset_password.txt")
        return redirect(url_for("auth.login"))
    return render_template(
        "/auth/request_reset.html", title="request reset password", form=form
    )


@auth.route("/user/reset/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("home.index"))
    user = User.verify_token(token)
    if not user:
        return redirect(url_for("home.index"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template(
        "/auth/reset_password.html", title="reset password", form=form
    )

@auth.route("/user/verify/<token>", methods=["GET"])
def verify(token):
    if current_user.is_authenticated and current_user.is_verified:
        return redirect(url_for("home.index"))
    user = User.verify_token(token)
    if not user:
        return redirect(url_for("home.index"))
    user.is_verified = True
    db.session.commit()
    return redirect(url_for("home.index"))


@auth.route("/user/<int:id>/verify", methods=["GET"])
@login_required
@requires_roles("admin")
def send_verification(id):
    user = User.query.get(int(id))
    if user.is_verified:
        return redirect(url_for("auth.moderation"))
    subject = "Reminder verify registration pegelinux.id"
    send_token_mail(user, subject, "/auth/verification.txt")
    return redirect(url_for("auth.moderation"))