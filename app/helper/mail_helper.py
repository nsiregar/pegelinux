import requests
from app import app
from flask import render_template


def send_mail(sender, recipient, subject, messages):
    url = app.config.get("MAILGUN_URL")
    auth = ("api", app.config.get("MAILGUN_API_KEY"))
    data = {"from": sender, "to": recipient, "subject": subject, "text": messages}

    response = requests.post(url, auth=auth, data=data)
    return response.raise_for_status()

def send_token_mail(user, subject, template):
    token = user.get_token()
    send_mail(
        sender=app.config.get("MAILGUN_USER"),
        recipient=user.email,
        subject=subject,
        messages=render_template(template, user=user, token=token),
    )