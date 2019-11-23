import requests
import logging
from app import app
from flask import render_template

class Mailer:
    def __init__(self, app):
        self.url = app.config.get("MAILGUN_URL")
        self.auth = ("api", app.config.get("MAILGUN_API_KEY"))
        self.sender = app.config.get("MAILGUN_USER")

    def send_token(self, user, subject, template):
        token = user.get_token()
        self.__send_mail(
            sender=self.sender,
            recipient=user.email,
            subject=subject,
            messages=render_template(template, user=user, token=token),
        )

    def __send_mail(self, sender, recipient, subject, messages):
        data = {
            "from": sender,
            "to": recipient,
            "subject": subject,
            "text": messages
        }
        try:
            response = requests.post(url, auth=auth, data=data)
            return response.raise_for_status()
        except Exception as e:
            logging.error(f"Error message: {e}")
