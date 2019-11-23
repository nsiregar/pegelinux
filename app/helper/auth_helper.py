import requests
import logging
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


class GithubAuth:
    def __init__(self, app):
        self.client_id = app.config.get("GITHUB_CLIENT_ID")
        self.secret = app.config.get("GITHUB_SECRET_ID")
        self.headers = {"Accept": "application/json"}

    def fetch_token(self, session_code):
        endpoint = "https://github.com/login/oauth/access_token"
        data = {
            "client_id": self.client_id,
            "client_secret": self.secret,
            "code": session_code,
        }
        response = self.__post(endpoint, data)
        return response.get("access_token", "")

    def fetch_user_data(self, access_token):
        endpoint = "https://api.github.com/user"
        data = {"access_token": access_token}
        response = self.__get(endpoint, data)
        return response

    def fetch_user_email(self, access_token):
        url = "https://api.github.com/user/emails"
        data = {"access_token": access_token}
        response = self.__get(endpoint, data)
        return response.json()[0]["email"]

    def __post(self, url, params):
        try:
            response = requests.post(url, params=params, headers=self.headers)
            return response.json()
        except Exception as e:
            logging.error(f"Error message: {e}")

    def __get(self, url, params):
        try:
            response = requests.get(url, params=params, headers=self.headers)
            return response.json()
        except Exception as e:
            logging.error(f"Error message: {e}")
