from app import app

from app.controllers.home_controller import home
from app.controllers.auth_controller import auth
from app.controllers.feed_controller import feed

app.register_blueprint(home)
app.register_blueprint(auth)
app.register_blueprint(feed)