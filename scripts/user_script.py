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
    db.session.add(user)
    db.session.commit()
    print("User {} created".format(username))


app.cli.add_command(user_command)
