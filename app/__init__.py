import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from flask_login import LoginManager
from flask_misaka import Misaka
from app.helper import sentry

app_config = os.environ.get("APP_CONFIG")
app = Flask(__name__, static_folder="assets", template_folder="views")
app.config.from_object(app_config)

moment = Moment(app)
login = LoginManager(app)
login.login_view = "auth.login"
Misaka(app, no_intra_emphasis=True, escape=True, autolink=True, math=True)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

sentry.init()

from app.controllers import routes
from app.controllers import scheduler
from app.controllers import error_controller
from app.helper import template_tags
from scripts import user_script
