import click
from app import app
from app import db
from flask.cli import AppGroup
from app.models.user import User

user_command = AppGroup("user")


@user_command.command("create")
@click.argument("username")
@click.argument("email")
@click.argument("password")
def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.role = "jelata"
    db.session.add(user)
    db.session.commit()
    print("User {} created".format(username))


@user_command.command("promote")
@click.argument("username")
@click.option("--role", default="momod", help="user role")
def promote_user(username):
    user = User.query.filter_by(username=username).first()
    user.role = role
    db.session.commit()
    print("User {} promoted to {}".format(username, role))


@user_command.command("demote")
@click.argument("username")
def demote_user(username):
    user = User.query.filter_by(username=username).first()
    user.role = "jelata"
    db.session.commit()
    print("User {} demoted".format(username))


app.cli.add_command(user_command)
