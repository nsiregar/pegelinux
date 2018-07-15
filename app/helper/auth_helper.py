import requests
from functools import wraps
from app import app
from flask import redirect
from flask import url_for
from flask import flash
from flask_login import current_user


def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                return redirect(url_for("home.index"))
            return f(*args, **kwargs)

        return wrapped

    return wrapper


def get_github_token(session_code):
    url = "https://github.com/login/oauth/access_token"
    data = {
        "client_id": app.config.get("GITHUB_CLIENT_ID"),
        "client_secret": app.config.get("GITHUB_SECRET_ID"),
        "code": session_code,
    }
    response = requests.post(url, params=data, headers={"Accept": "application/json"})
    access_token = response.json()
    return access_token["access_token"]


def get_github_data(access_token):
    url = "https://api.github.com/user"
    data = {"access_token": access_token}
    response = requests.get(url, params=data, headers={"Accept": "application/json"})
    return response.json()


def get_github_email(access_token):
    url = "https://api.github.com/user/emails"
    data = { "access_token": access_token}
    response = requests.get(url, params=data, headers={"Accept": "application/json"})
    return response.json()[0]["email"]