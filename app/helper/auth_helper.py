from functools import wraps
from flask import redirect
from flask import url_for
from flask import flash
from flask_login import current_user

def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                return redirect(url_for('home.index'))
            return f(*args, **kwargs)
        return wrapped
    return wrapper