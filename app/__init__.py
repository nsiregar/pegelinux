from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from config.application import DevelopmentConfig

app = Flask(__name__, static_folder='assets', template_folder='views')
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)

from app.controllers import routes
from app.controllers import scheduler
from app.controllers import error_controller
